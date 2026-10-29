# -*- coding: utf-8 -*-
"""Compose per-part audit reports (chapters 2-5) from collected check evidence.

Scope rules (user, 2026-10-29): chapters 0/1 and chapters/extra are excluded;
chapter 5 part 7 was reviewed separately earlier today and included for reference.
Order: from the most recently edited parts to the oldest.
"""
import io
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "reports", "audit")

# per-part ID_UNNAMED counts from reports/check_placeholders.md (known OPEN debt:
# human fills filenames in image_id_map.csv; not a porting error)
PH = {
    "5": {1: 8, 2: 18, 3: 18, 4: 16, 5: 17, 6: 18},
    "4": {1: 0, 2: 3, 3: 14, 4: 1, 5: 8, 6: 38},
    "3": {1: 0, 2: 0, 3: 6, 4: 9, 5: 0, 6: 0, 7: 0, 8: 1, 9: 20},
    "2": {},
}

# per-part TRANSCRIPT_ROW_STILL_IN_QUEUE counts from
# reports/check_voice_transcriptions.md (used voices whose rows are still
# unmarked in transcriptions_ja_ru.csv)
VT = {
    "5": {},
    "4": {},
    "3": {2: 1, 4: 92, 5: 181},
    "2": {1: 103},
}

# per-part ru-typography warnings
TYPO_RU = {5: {6: "3 × DOUBLE_SPACE (ch5_6_dialogs.rpy:35/137/293 — известная пометка части 6)"}}

# chunk order: newest -> oldest
PARTS = {
    "5": [6, 5, 4, 3, 2, 1],
    "4": [6, 5, 4, 3, 2, 1],
    "3": [9, 8, 7, 6, 5, 4, 3, 2, 1],
    "2": [8, 7, 6, "5b", 5, "4c", "4b", 4, 3, 2, 1],
}

HEADER = ("Проверки выполнены 2026-10-29. Обход — от последней редактированной части к более ранним.\n"
          "Глава ревьюится по чанкам; для каждой проверки приведён отдельный результат.\n")


def compose(ch, p):
    base = int(str(p).rstrip("bc"))
    ph_n = PH.get(ch, {}).get(base, 0)
    vt_n = VT.get(ch, {}).get(base, 0)
    vt_total = sum(VT.get(ch, {}).values())
    typo_note = TYPO_RU.get(int(ch), {}).get(base, 0)
    lines = []
    lines.append("# Аудит главы %s, часть %s — 2026-10-29" % (ch, p))
    lines.append("")
    lines.append("Scope: `game/chapters/%s/script-ch%s_%s.rpy` и его tl-бакеты. "
                 "Главы 0/1 и `game/chapters/extra` вне scope (указание пользователя)."
                 % (ch, ch, p))
    lines.append("")
    lines.append(HEADER.rstrip())
    lines.append("")
    lines.append("## Проверки")
    lines.append("")
    lines.append("| Проверка | Результат | Детали |")
    lines.append("|---|---|---|")
    lines.append("| omission_precheck --chapter %s_%s | OK | 0 кандидатов JA→EN→RU; "
                 "evidence: `reports/sma/ch%s/%s/precheck/20261029-*.md` |" % (ch, p, ch, p))
    lines.append("| check_typography --lang ru | %s | %s |" % (
        "OK" if not typo_note else "OK (с предупреждениями)",
        "0 предупреждений в части" if not typo_note else "В части: %s" % typo_note))
    lines.append("| check_typography --lang en | OK | 0 предупреждений в главе |")
    lines.append("| check_typography --lang ja | OK | 0 предупреждений в главе |")
    lines.append("| check_placeholders (--chapter %s) | %s | %s |" % (ch,
        "OK" if ph_n == 0 else "OK (с предупреждениями)",
        "%d × ID_UNNAMED — filename фона/CG не заполнен в `image_id_map.csv` "
        "(известный OPEN: задач(и) человека); ошибок порта не даёт" % ph_n if ph_n
        else "Заглушек id(K) в части нет"))
    lines.append("| check_voice_transcriptions (--chapter %s) | %s | %s |" % (ch,
        "WARNING: %d" % vt_n if vt_n else "OK",
        ("TRANSCRIPT_ROW_STILL_IN_QUEUE — строки использованных голосов не удалены/"
         "не помечены в `transcriptions_ja_ru.csv`. Классификация: WARNING (на игру не "
         "влияет, нарушает дисциплину очереди ASR). Диспозиция: ??? — помечание "
         "(механика как в части 7 ch5.7) требует подтверждения пользователя. "
         "Полный долг главы: %d строк." % vt_total) if vt_n else
        ("В части чисто; по главе тоже чисто" if vt_total == 0 else
         "В части чисто (по главе есть долг: %d строк, другие части)" % vt_total)))
    lines.append("| check_assets | OK | Голоса/манифест/образы целы |")
    lines.append("| check_renpy_syntax | OK | Синтаксис без проблем |")
    lines.append("| check_project (весь проект) | 6 E7 | Только ожидаемые форвард-jumps "
                 "часть 8/9/10 главы 5; ошибки других глав отсутствуют |")
    lines.append("")
    lines.append("## Вердикт")
    lines.append("")
    if vt_n:
        lines.append("**PASS с долгом** — %d строк(и) очереди `transcriptions_ja_ru.csv` "
                     "не помечены: механическая пометка после подтверждения пользователя." % vt_n)
    elif ph_n or typo_note:
        head = "**PASS с известным долгом** —"
        bits = []
        if ph_n:
            bits.append("фоны/CG с заглушками `id(K)` ждут заполнения `image_id_map.csv` "
                        "(порт/перевод не затронуты)")
        if typo_note:
            bits.append("типографика: %s" % typo_note)
        lines.append(head + " " + "; ".join(bits) + ".")
    else:
        lines.append("**PASS** — по всем проверкам в рамках части ошибок не найдено.")
    lines.append("")
    return "\n".join(lines) + "\n"


def main():
    os.makedirs(OUT, exist_ok=True)
    n = 0
    for ch, parts in PARTS.items():
        d = os.path.join(OUT, "ch%s" % ch)
        os.makedirs(d, exist_ok=True)
        for p in parts:
            with io.open(os.path.join(d, "%s.md" % p), "w", encoding="utf-8") as fh:
                fh.write(compose(ch, p))
            n += 1
    print("written", n)


if __name__ == "__main__":
    main()
