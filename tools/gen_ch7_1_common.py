# -*- coding: utf-8 -*-
"""ch7_1: общий разбор манифеста + читаемого вида главы 08, кросс-проверки.

Используется tools/gen_ch7_1_script.py (сценарий) и tools/gen_ch7_1_tl.py (tl),
чтобы оба работали с одними и теми же данными и жёстким контролем.

Запуск: из корня проекта (cwd = ZnT1), python gen_ch7_1_common.py — прогон
самопроверки без записи файлов.
"""
import io
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WS = u" \t\u3000\u00a0"


class Fail(Exception):
    pass


def norm(s):
    """Нормализация для сравнения: убрать все пробельные символы."""
    return re.sub(r"[\s\u3000\u00a0]+", u"", s)


def rel(*p):
    return os.path.join(ROOT, *p)


# ---------------------------------------------------------------- манифест
def load_manifest():
    path = rel("reports", "_tmp_manifest.txt")
    lines = io.open(path, encoding="utf-8").read().splitlines()
    voice_rows = []          # (name, id, wav) — строки voice_id_map
    events = []              # последовательные события потока
    totals = {}              # итоги по говорящим
    in_events = False
    for ln in lines:
        if ln.startswith("ch7_"):
            m = re.match(r"^(ch7_\w+),(\d+),(.+?\.wav)$", ln)
            if m:
                voice_rows.append((m.group(1), m.group(2), m.group(3)))
            continue
        if ln.startswith("# speaker"):
            in_events = "totals"
            continue
        if in_events == "totals":
            m = re.match(r"^(\w+)=(\d+)$", ln.strip())
            if m:
                totals[m.group(1)] = int(m.group(2))
            continue
        if not ln.startswith("E|"):
            continue
        parts = ln.split(u"|")
        kind = parts[1]
        ev = {"kind": kind}
        if kind == "D":
            ev["spk"] = parts[3]
            ev["name"] = parts[4]
            ev["vid"] = parts[5]
            ev["wav"] = parts[6]
            ev["lines"] = [x.strip() for x in parts[7:] if x.strip()]
            ev["spk_rc"] = parts[3]
        elif kind == "TH":
            ev["spk"] = parts[9]
            ev["lines"] = [x.strip() for x in parts[10:] if x.strip()]
        elif kind == "CHOICE":
            ev["target"] = int(parts[9])
            ev["lines"] = [u" ".join(parts[10:]).strip()]
        elif kind == "TNDL":
            ev["value"] = parts[9]
        elif kind == "BGM":
            ev["value"] = parts[9]           # play=5 / stop=1000
        elif kind == "BG":
            ev["value"] = parts[9]           # +N / hide
            ev["args"] = u"".join(parts[10:])
        elif kind == "SET":
            ev["layer"] = parts[2]
            ev["args"] = parts[10] if len(parts) > 10 else u""
        elif kind == "EVENT_CG":
            ev["args"] = u"".join(parts[10:])
        elif kind == "SCENE":
            ev["scene"] = int(parts[2])
        elif kind == "GOTO":
            v = u"".join(parts[9:])
            m = re.search(r"\+(\d+)\)", v)
            ev["target"] = int(m.group(1)) if m else None
        elif kind in ("RESET", "MSGOFF", "MSGON", "BACK", "TRANS", "WAIT",
                      "MENUINIT", "MENU", "BGU", "TITLE", "SKIP", "UNK3", "if",
                      "ITEM"):
            ev["value"] = u"".join(parts[9:]) if len(parts) > 9 else u""
            ev["spk"] = parts[2] if len(parts) > 2 else u""
        events.append(ev)
    return voice_rows, events, totals


# ---------------------------------------------------- читаемый вид главы 08
SPANfrom = 375
SPANto = 388


def load_chapters():
    paths = glob.glob(rel("ps2_source", "chapters", "chapter_08_*.txt"))
    assert len(paths) == 1, paths
    lines = io.open(paths[0], encoding="utf-8").read().splitlines()
    units = []       # ('d'|'th', scene, vid, [ja lines])
    choices = []     # (scene, text)
    scene = None
    buf = []         # строки текущего абзаца
    pend_voice = None

    def flush():
        nonlocal buf, pend_voice
        if not buf:
            pend_voice = None
            return
        # говорящий префикс «имя：» на первой строке — снимаем
        first = buf[0]
        m = re.match(r"^[^：\n]{1,20}：(.*)$", first)
        body = ([m.group(1)] if m else [first]) + buf[1:]
        if pend_voice is not None:
            units.append(("d", scene, pend_voice, body))
        elif any(u"（" in b for b in body):
            units.append(("th", scene, None, body))
        else:
            raise Fail("chapters: абзац без голоса и без （…） в сцене %s: %r" % (scene, body))
        buf = []
        pend_voice = None

    for raw in lines:
        s = raw.strip()
        m = re.match(r"^---- SCENE (\d+) ----$", s)
        if m:
            flush()
            scene = int(m.group(1))
            continue
        mm = re.match(r"^【選択肢】(.+?)\s*→\s*scene\s+(\d+)$", s)
        if mm:
            flush()
            if scene is not None and SPANfrom <= scene <= SPANto:
                choices.append((int(mm.group(2)), mm.group(1).strip()))
            continue
        if s.startswith(u"→ next scene"):
            continue
        if s.startswith("[") or not s:
            # событие или пустая строка: если буфер копится — абзац ещё не
            # закрыт голосом; но это не打成 закрытия: голос может быть дальше
            if s.startswith("["):
                mv = re.match(r"\[voice\s+(\d+)\]", s)
                if mv and buf:
                    pend_voice = int(mv.group(1))
                    flush()
                else:
                    flush()
            continue
        if scene is not None and SPANfrom <= scene <= SPANto:
            mv2 = re.search(r"\[voice\s+(\d+)\]", s)
            if mv2:
                s = s[:mv2.start()].strip()
                buf.append(s)
                pend_voice = int(mv2.group(1))
                flush()
                continue
            buf.append(s)
    flush()
    return units, choices


# ------------------------------------------------------------- кросс-проверки
def cross_check(events, voice_rows, units, choices, totals):
    D = [e for e in events if e["kind"] == "D"]
    TH = [e for e in events if e["kind"] == "TH"]
    CH = [e for e in events if e["kind"] == "CHOICE"]
    ud = [u for u in units if u[0] == "d"]
    uth = [u for u in units if u[0] == "th"]

    if len(D) != len(voice_rows):
        raise Fail("голосов в потоке %d против строк манифеста %d" % (len(D), len(voice_rows)))
    if len(D) != len(ud):
        raise Fail("голосов в сценарии %d против единиц читаемого вида %d" % (len(D), len(ud)))
    if len(TH) != len(uth):
        raise Fail("мыслей в потоке %d против единиц %d" % (len(TH), len(uth)))
    if len(CH) != len(choices):
        raise Fail("пунктов меню в потоке %d против строк 【選択肢】 %d" % (len(CH), len(choices)))

    for i, (ev, (name, vid, wav)) in enumerate(zip(D, voice_rows)):
        if ev["name"] != name:
            raise Fail("порядок имен %d: %s против %s" % (i, ev["name"], name))
        if ev["vid"] != vid:
            raise Fail("voice id %d: поток %s против манифеста %s" % (i, ev["vid"], vid))
        if ev["wav"] != wav:
            raise Fail("wav %d: %s против %s" % (i, ev["wav"], wav))

    # тексты: поток против читаемого вида
    for i, (ev, u) in enumerate(zip(D, ud)):
        if str(ev["vid"]) != str(u[2]):
            raise Fail("id %d: поток %s против chapters %s" % (i, ev["vid"], u[2]))
        mtext = u"　".join(ev["lines"])
        ctext = u"　".join(u[3])
        if norm(mtext) != norm(ctext):
            raise Fail("текст D %d (%s) не совпал:\n поток:  %r\n глав:   %r" % (i, ev["name"], mtext, ctext))

    for i, (ev, u) in enumerate(zip(TH, uth)):
        if norm(u"　".join(ev["lines"])) != norm(u"　".join(u[3])):
            raise Fail("текст TH %d не совпал:\n поток:  %r\n глав:   %r" % (i, u"　".join(ev["lines"]), u"　".join(u[3])))

    for i, (ev, (tsc, text)) in enumerate(zip(CH, choices)):
        if ev["target"] != tsc:
            raise Fail("пункт %d: цель потока %s против глав %s" % (i, ev["target"], tsc))
        if norm(ev["lines"][0]) != norm(text):
            raise Fail("текст пункта %d: %r против %r" % (i, ev["lines"][0], text))

    # счётчики по говорящим
    seen = {}
    for ev in D:
        seen[ev["spk"]] = seen.get(ev["spk"], 0) + 1
    if seen != totals:
        raise Fail("итоги говорящих %r против манифеста %r" % (seen, totals))
    # нумерация с 001 по каждому говорящему
    ctr = {}
    for ev in D:
        ctr[ev["spk"]] = ctr.get(ev["spk"], 0) + 1
        if not re.match(r"^ch7_%s_%03d$" % (ev["spk"], ctr[ev["spk"]]), ev["name"]):
            raise Fail("имя %s не соответствует счётчику %d" % (ev["name"], ctr[ev["spk"]]))
    return D, TH, CH, ud, uth


def check_tndl(events):
    vals = [(e["value"], e["name"] if e.get("name") else None) for e in [] ]
    got = []
    prev_d = None
    for ev in events:
        if ev["kind"] == "D":
            prev_d = ev["name"]
        elif ev["kind"] == "TNDL":
            got.append((ev["value"], prev_d))
    expected = [("null", None), ("-40", "ch7_l_011"), ("-40", "ch7_l_027"),
                ("50", "ch7_l_029"), ("-40", "ch7_l_036"), ("50", "ch7_s_032")]
    if got != expected:
        raise Fail("TNDL-якоря %r не совпали с ожидаемыми %r" % (got, expected))


# ------------------------------------------------------------- словари EN/RU
def load_translations(dnames):
    names = [e["name"] for e in dnames]
    sets = []
    for mod_name in ("ch7_1_en", "ch7_1_ru"):
        mod = __import__(mod_name)
        d = getattr(mod, "EN") if mod_name.endswith("_en") else {}
        if mod_name.endswith("_ru"):
            d = getattr(mod, "RU")
        set2 = set(d)
        base = set(names) | {u"ch7_th_375a", u"ch7_th_375b"} | \
            {u"ch7_c%d" % n for n in (376, 377, 378, 381, 382, 383, 386, 387, 388)} | \
            {u"ch7_title"}
        if set2 != base:
            missing = sorted(base - set2)
            extra = sorted(set2 - base)
            raise Fail("словарь %s: отсутствуют %r, лишние %r" % (mod_name, missing, extra))
        sets.append(d)
    return sets


def full_check():
    voice_rows, events, totals = load_manifest()
    units, choices = load_chapters()
    D, TH, CH, ud, uth = cross_check(events, voice_rows, units, choices, totals)
    check_tndl(events)
    EN, RU = load_translations(D)
    # уникальность тегов
    tags = set()
    for e in D:
        t = "{#%s}" % e["name"]
        if t in tags:
            raise Fail("дубль тега %s" % t)
        tags.add(t)
    return {
        "voice_rows": voice_rows,
        "events": events,
        "totals": totals,
        "dialogs": [(dict(spk=e["spk"], name=e["name"], vid=e["vid"], wav=e["wav"],
                          ja=u"　".join(u[3]), ja_lines=u[3], en=EN[e["name"]],
                          ru=RU[e["name"]]))
                    for e, u in zip(D, ud)],
        "ths": [(dict(spk=e["spk"],
                      ja=u"　".join(u[3]), ja_lines=u[3],
                      en=EN[u"ch7_th_375%s" % ("ab"[i])],
                      ru=RU[u"ch7_th_375%s" % ("ab"[i])]))
                for i, (e, u) in enumerate(zip(TH, uth))],
        "choices": [(dict(target=e["target"], ja=e["lines"][0], en=EN[u"ch7_c%d" % e["target"]],
                          ru=RU[u"ch7_c%d" % e["target"]]))
                    for e, u in zip(CH, choices)],
        "blocks": None,
    }


if __name__ == "__main__":
    data = full_check()
    print("OK: voices=%d th=%d choices=%d totals=%r" % (
        len(data["voice_rows"]), len(data["ths"]), len(data["choices"]), data["totals"]))
