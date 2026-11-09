# -*- coding: utf-8 -*-
"""Генератор tl (japanese/russian) + приложение манифеста голосов для ch7_3.

Данные берутся из трёх источников с жёсткой кросс-проверкой:
  - game/chapters/7/script-ch7_3.rpy  — EN-текст, теги {#ch7.3_*}, voice-строки,
    JA-комментарии;
  - ps2_source/chapters/chapter_08_失望のお姫さま.txt — канонический JA
    (сцены 400-404, 1169-1173);
  - tools/ch7_3_ru.py — русский перевод по тегам.

Пишет добавочные блоки в конец:
  game/tl/{japanese,russian}/dialogs.rpy   (95 пар — все с голосом)
  game/tl/{japanese,russian}/thoughs.rpy   (1 пара — мысль Сайто, сцена 404)
  game/tl/{japanese,russian}/choises.rpy   (6 пар)
  references/voice_id_map.csv              (95 строк)

Повторный запуск запрещён (идемпотентность по маркеру «# ===== ch7_3»).
"""
import glob
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ch7_3_ru


class Fail(Exception):
    pass


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "game", "chapters", "7", "script-ch7_3.rpy")
VOCAB = os.path.join(ROOT, "references", "voice_id_map.csv")
WAV_DIR = os.path.join(ROOT, "wav_files")
SPAN_FROM, SPAN_TO = 400, 1173

# ожидаемое распределение голосов по говорящим — по канону
# (400 → 401 → 402 → 403 → 404 → 1169 → 1170 → 1171 → 1172 → 1173)
EXPECTED_TOTALS = {"s": 36, "l": 13, "si": 8, "g": 2, "m": 3, "h": 28,
                   "k": 4, "t": 1}
# говорящие, чьи wav в wav_files/ лежат под префиксом имени
WAV_PREFIX = {"g": u"guiche ", "t": u"tabitha "}


def ess(s):
    return s.replace(u"\\", u"\\\\").replace(u'"', u'\\"')


def join_lines(parts):
    """Склейка строк исходника для JA-new: разделитель U+3000, но без
    удвоения, если очередная строка сама начинается с U+3000."""
    if not parts:
        return u""
    out = parts[0]
    for p in parts[1:]:
        if not out.endswith(u"　") and not p.startswith(u"　"):
            out += u"　"
        out += p
    return out


# ---------------------------------------------------------------- сценарий
def parse_script():
    """Разбор script-ch7_3.rpy: диалоги/мысль/пункты меню + voice/ids."""
    text = io.open(SCRIPT, encoding="utf-8").read()
    dialogs, thoughts, choices = [], [], []
    seen_tags = set()
    lines = text.splitlines()
    i = 0
    pend_voice = None
    while i < len(lines):
        st = lines[i].strip()
        m = re.match(r'^voice "([^"]+)"$', st)
        if m:
            if pend_voice is not None:
                raise Fail("две voice-строки подряд: %s, %s" % (pend_voice, m.group(1)))
            pend_voice = m.group(1)
            i += 1
            continue
        m = re.match(r'^(\w+)\s+"(.*)\{#([^}]+)\}"$', st)
        if m:
            spk, en, tag = m.group(1), m.group(2), m.group(3)
            kind = "th" if spk == "th" else "d"
            # следующий значимый элемент — JA-комментарий
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            mj = re.match(r'^#\s*JA(?:\[(\d+)\])?:\s*(.*)$',
                          lines[j].strip() if j < len(lines) else "")
            if not mj:
                raise Fail("после строки с тегом %s нет JA-комментария" % tag)
            vid = int(mj.group(1)) if mj.group(1) else None
            ja_lines = mj.group(2).split(u" / ")
            i = j + 1
            rec = {"tag": tag, "en": en, "spk": spk, "voice": pend_voice,
                   "vid": vid, "ja_lines": ja_lines, "line_no": i + 1}
            if tag in seen_tags:
                raise Fail("дубль тега в сценарии: %s" % tag)
            seen_tags.add(tag)
            if kind == "th":
                thoughts.append(rec)
            else:
                dialogs.append(rec)
            pend_voice = None
            continue
        m = re.match(r'^"(.*)\{#([^}]+)\}":$', st)
        if m:
            en, tag = m.group(1), m.group(2)
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            mj = re.match(r'^#\s*JA(?:\[(\d+)\])?:\s*(.*)$',
                          lines[j].strip() if j < len(lines) else "")
            if not mj:
                raise Fail("после пункта меню %s нет JA-комментария" % tag)
            if tag in seen_tags:
                raise Fail("дубль тега в сценарии: %s" % tag)
            seen_tags.add(tag)
            choices.append({"tag": tag, "en": en,
                            "ja": mj.group(2).strip()})
            pend_voice = None
            i = j + 1
            continue
        if st:
            # не voice, не реплика, не JA: посторонняя строка — нужна для
            # контроля случаев voice без реплики
            if pend_voice is not None and re.match(
                    r'^(play|stop|menu|\$|#|\}|$)', st):
                pass  # разрыв между voice и репликой недопустим всё равно
            else:
                pend_voice = None
        i += 1
    if pend_voice is not None:
        raise Fail("voice-строка %s без реплики" % pend_voice)
    if pend_voice is None and not dialogs:
        raise Fail("сценарий не разобран")
    return text, dialogs, thoughts, choices, seen_tags


# ---------------------------------------------------------------- источник
def normalize(s):
    return re.sub(r"[\s\u3000\u00a0]+", u"", s)


def load_source():
    paths = glob.glob(os.path.join(ROOT, "ps2_source", "chapters",
                                   "chapter_08_*.txt"))
    if len(paths) != 1:
        raise Fail("ожидался ровно один файл chapter_08: %r" % paths)
    lines = io.open(paths[0], encoding="utf-8").read().splitlines()
    units, choices = [], []
    scene = None
    buf, pend_voice = [], None

    def flush():
        nonlocal buf, pend_voice
        if not buf:
            pend_voice = None
            return
        if pend_voice is not None:
            units.append(["v", scene, pend_voice, list(buf)])
        elif any(u"（" in b for b in buf):
            units.append(["th", scene, None, list(buf)])
        else:
            units.append(["nv", scene, None, list(buf)])
        buf, pend_voice = [], None

    for raw in lines:
        ln = raw.rstrip(u"\r\n").rstrip()
        base = ln.lstrip(u" \t")
        mv = re.match(r"^---- SCENE (\d+) ----$", base)
        if mv:
            flush()
            scene = int(mv.group(1))
            continue
        mc = re.match(r"^【選択肢】(.+?)\s*→\s*scene\s+(\d+)$", base)
        if mc:
            flush()
            if scene is not None and SPAN_FROM <= scene <= SPAN_TO:
                choices.append((int(mc.group(2)), mc.group(1).strip()))
            continue
        # прочие метки 【…】 (【デート】, 【デート進行】) — не текст реплик
        if base.startswith(u"【"):
            flush()
            continue
        if not base or base.startswith(u"[") or base.startswith(u"→"):
            flush()
            continue
        if scene is None or not (SPAN_FROM <= scene <= SPAN_TO):
            continue
        # строка с префиксом «имя：» начинает новый абзац (repлика без голоса
        # не будет слита с последующей репликой с [voice N])
        if buf and re.match(r"^[^：]{1,25}：", base):
            flush()
        mvoice = re.search(r"\s*\[voice\s+(\d+)\]\s*$", base)
        if mvoice:
            body = base[:mvoice.start()].rstrip()
            if body:
                buf.append(body)
            pend_voice = int(mvoice.group(1))
            flush()
        else:
            buf.append(base)
    flush()

    # снять префикс «имя：» с первой строки каждого юнита
    for u in units:
        first = u[3][0]
        m = re.match(r"^([^：]{1,25})：(.*)$", first)
        if m:
            u[3] = [m.group(2)] + u[3][1:]
    return units, choices


# ---------------------------------------------------------------- сверка
def check(data):
    _, dialogs, thoughts, choices, _ = data
    units, src_choices = load_source()

    voiced = [d for d in dialogs if d["voice"] is not None]
    novoice = [d for d in dialogs if d["voice"] is None]
    src_v = [u for u in units if u[0] == "v"]
    src_th = [u for u in units if u[0] == "th"]
    src_nv = [u for u in units if u[0] == "nv"]

    if len(voiced) != 95:
        raise Fail("голосовых реплик в сценарии %d, ожидалось 95" % len(voiced))
    if len(novoice) != 0:
        raise Fail("реплик без голоса в сценарии %d, ожидалось 0" % len(novoice))
    if len(thoughts) != 1:
        raise Fail("мыслей в сценарии %d, ожидалось 1" % len(thoughts))
    if len(src_v) != 95:
        raise Fail("голосовых юнитов в источнике %d, ожидалось 95" % len(src_v))
    if len(src_th) != 1:
        raise Fail("мыслей в источнике %d, ожидалось 1" % len(src_th))
    if len(src_nv) != 0:
        raise Fail("реплик без голоса в источнике %d, ожидалось 0" % len(src_nv))
    if len(src_choices) != 6:
        raise Fail("пунктов меню в источнике %d, ожидалось 6" % len(src_choices))

    # распределение говорящих + нумерация с 001
    ctr = {}
    for d in voiced:
        m = re.match(r"^ch7\.3_([a-z_]+)_(\d+)$", d["tag"])
        if not m:
            raise Fail("тег голосовой реплики не распознан: %s" % d["tag"])
        spk, num = m.group(1), int(m.group(2))
        if d["spk"] != spk:
            raise Fail("говорящий строки %s не совпал с тегом (%s)" % (d["spk"], spk))
        if d["voice"] != d["tag"]:
            raise Fail("voice-имя %s не совпало с тегом %s" % (d["voice"], d["tag"]))
        ctr[spk] = ctr.get(spk, 0) + 1
        if num != ctr[spk]:
            raise Fail("нумерация говорящего %s: ожидалось %03d, в теге %03d"
                       % (spk, ctr[spk], num))
    if ctr != EXPECTED_TOTALS:
        raise Fail("итоги говорящих %r против канона %r" % (ctr, EXPECTED_TOTALS))

    # соответствие голосов: id и JA-текст
    for i, (d, (tsc, vid, lines)) in enumerate(zip(voiced, [(u[0], u[2], u[3]) for u in src_v])):
        if d["vid"] != vid:
            raise Fail("реплика %d (%s): id сценария %s против источника %s"
                       % (i, d["tag"], d["vid"], vid))
        if [normalize(x) for x in d["ja_lines"]] != [normalize(x) for x in lines]:
            raise Fail("JA-текст реплики %s не совпал с источником:\n сценарий: %r\n источник: %r"
                       % (d["tag"], d["ja_lines"], lines))

    # мысль
    th, sth = thoughts[0], src_th[0]
    if th["tag"] != u"ch7.3_th_404a":
        raise Fail("тег мысли %s — ожидался ch7.3_th_404a" % th["tag"])
    if th["spk"] != "th":
        raise Fail("говорящий мысли %s — ожидался th" % th["spk"])
    if [normalize(x) for x in th["ja_lines"]] != [normalize(x) for x in sth[3]]:
        raise Fail("JA мысли не совпал с источником: %r против %r"
                   % (th["ja_lines"], sth[3]))

    # пункты меню
    if len(choices) != len(src_choices):
        raise Fail("пунктов меню в сценарии %d против источника %d"
                   % (len(choices), len(src_choices)))
    for c, (target, text) in zip(choices, src_choices):
        m = re.match(r"^ch7\.3_c(\d+)$", c["tag"])
        if not m or int(m.group(1)) != target:
            raise Fail("цель пункта %s против источника %s" % (c["tag"], target))
        if normalize(c["ja"]) != normalize(text):
            raise Fail("JA пункта %s: %r против %r" % (c["tag"], c["ja"], text))

    # JP-строки подряд с U+3000 внутри — на всякий случай
    for u in units:
        for ln in u[3][1:]:
            if u"　" in ln.strip(u"　"):
                raise Fail("внутренняя U+3000 в строке источника: %r" % (u[3],))

    return voiced, thoughts[0], choices, src_v, src_th[0], src_choices


# ---------------------------------------------------------------- запись
def load_tl_tail(path):
    t = io.open(path, encoding="utf-8").read()
    if u"# ===== ch7_3" in t:
        raise Fail("%s уже содержит блок ch7_3 — нельзя добавлять вторично" % path)
    return t


def append_pairs(path, lang, pairs, header_note):
    t = load_tl_tail(path)
    existing = set()
    for m in re.finditer(r'^\s*old "(.*)"$', t, re.M):
        existing.add(m.group(1))
    for old, _new in pairs:
        if old in existing:
            raise Fail("в %s уже есть old %r" % (path, old[:60]))
        if old in (u"",):
            raise Fail("пустая пара в %s" % path)
    oess = [ess(o) for o, _n in pairs]
    for e in oess:
        if e in existing:
            raise Fail("дубль после экранирования: %r" % e[:60])
    L = [u"", u"", u"# ===== ch7_3 (generated by tools/gen_ch7_3_tl.py) =====",
         u"# %s" % header_note, u"translate %s strings:" % lang]
    for i, (old, new) in enumerate(pairs):
        if i:
            L.append(u"")
        L.append(u'    old "%s"' % ess(old))
        L.append(u'    new "%s"' % new)
    body = u"\n".join(L) + u"\n"
    if t and not t.endswith(u"\n"):
        t += u"\n"
    io.open(path, "w", encoding="utf-8", newline="\n").write(t + body)
    return len(pairs)


def append_voice_manifest(rows):
    t = io.open(VOCAB, encoding="utf-8").read()
    for name, _vid, _wav in rows:
        if re.search(r"^%s," % re.escape(name), t, re.M):
            raise Fail("voice_id_map уже содержит строку %s" % name)
    wavs = set(r[2] for r in rows)
    if len(wavs) != len(rows):
        raise Fail("wav-имена не уникальны")
    for _name, vid, wav in rows:
        base = wav.split(u" ", 1)[1] if u" " in wav else wav
        if base != u"VOICE_ID.BIN_%08X.wav" % int(vid):
            raise Fail("wav %s не соответствует id %s" % (wav, vid))
        if not os.path.isfile(os.path.join(WAV_DIR, wav)):
            raise Fail("нет wav-файла %s" % wav)
    with io.open(VOCAB, "a", encoding="utf-8", newline="\n") as f:
        f.write(u"\n".join(u"%s,%s,%s" % r for r in rows) + u"\n")


def build():
    text, dialogs, thoughts, chs, _tags = parse_script()
    voiced, th, chs, src_v, src_th, src_choices = check(
        (text, dialogs, thoughts, chs, _tags))

    # final pairs — в порядке сценария (нарративном)
    d_ja, d_ru = [], []
    for d in dialogs:
        tag = d["tag"]
        src = next(u for u in src_v if u[2] == d["vid"])
        ja = join_lines(src[3])
        try:
            ru = ch7_3_ru.RU[tag]
        except KeyError:
            raise Fail("net RU dlja %s" % tag)
        d_ja.append((u"%s{#%s}" % (d["en"], tag), ja))
        d_ru.append((u"%s{#%s}" % (d["en"], tag), ru))
    t_ja = [(u"%s{#%s}" % (th["en"], th["tag"]), join_lines(src_th[3]))]
    t_ru = [(u"%s{#%s}" % (th["en"], th["tag"]), ch7_3_ru.RU[th["tag"]])]
    c_ja = [(u"%s{#%s}" % (c["en"], c["tag"]), c["ja"]) for c in chs]
    c_ru = [(u"%s{#%s}" % (c["en"], c["tag"]), ch7_3_ru.RU[c["tag"]]) for c in chs]

    # голосовые строки манифеста (в порядке канона)
    rows = []
    ctr = {}
    for u in src_v:
        d = next(d for d in voiced if d["vid"] == u[2])
        m = re.match(r"^ch7\.3_([a-z_]+)_(\d+)$", d["tag"])
        spk = m.group(1)
        ctr[spk] = ctr.get(spk, 0) + 1
        wav = u"VOICE_ID.BIN_%08X.wav" % u[2]
        prefix = WAV_PREFIX.get(spk)
        if prefix:
            name = prefix + wav
        else:
            name = wav
        rows.append((d["tag"], str(u[2]), name))

    # полный набор тегов в dict RU должен в точности совпасть
    all_tags = ([d["tag"] for d in voiced] + [th["tag"]] +
                [c["tag"] for c in chs])
    missing = [t for t in all_tags if t not in ch7_3_ru.RU]
    extra = [t for t in ch7_3_ru.RU if t not in all_tags]
    if missing or extra:
        raise Fail("толковый dict RU: отсутствуют %d, лишние %d" %
                   (len(missing), len(extra)))

    header = u"chast 3 glavy 7 (сцены 400-404, 1169-1173)"
    tasks = [
        (os.path.join(ROOT, "game", "tl", "japanese", "dialogs.rpy"),
         "japanese", d_ja, header),
        (os.path.join(ROOT, "game", "tl", "russian", "dialogs.rpy"),
         "russian", d_ru, header),
        (os.path.join(ROOT, "game", "tl", "japanese", "thoughs.rpy"),
         "japanese", t_ja, header),
        (os.path.join(ROOT, "game", "tl", "russian", "thoughs.rpy"),
         "russian", t_ru, header),
        (os.path.join(ROOT, "game", "tl", "japanese", "choises.rpy"),
         "japanese", c_ja, header),
        (os.path.join(ROOT, "game", "tl", "russian", "choises.rpy"),
         "russian", c_ru, header),
    ]
    appended = 0
    if "--manifest-only" not in sys.argv[1:]:
        for path, lang, pairs, note in tasks:
            appended += append_pairs(path, lang, pairs, note)
    append_voice_manifest(rows)
    print("OK: tl pairs: %d; voice manifest rows: %d; totals: %r"
          % (appended, len(rows), ctr))


if __name__ == "__main__":
    build()
    print("OK tl ch7_3")
