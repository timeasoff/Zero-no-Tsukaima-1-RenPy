#!/usr/bin/env python3
"""Add missing [TITLE] overlay_screen calls to chapters 23-28 (prompt 07).

ps2_to_renpy.csv id 15: [TITLE title("...")] -> call overlay_screen(...)
from _call_overlay_screen_K with globally unique K.  Uses K=20..26.
"""
from pathlib import Path

ROOT = Path(__file__).parent.parent
TITLES = {
    23: ("Twenty-Three", "Silent Support", "第二十三章「沈黙の応援」", "Глава двадцать третья. «Молчаливая поддержка»"),
    24: ("Twenty-Four", "Uniform's Appeal", "第二十四章「制服の魅力」", "Глава двадцать четвёртая. «Очарование формы»"),
    25: ("Twenty-Five", "Secret of the Letter", "第二十五章「手紙の秘密」", "Глава двадцать пятая. «Тайна письма»"),
    26: ("Twenty-Six", "Tabitha's Secret", "第二十六章「タバサの秘密」", "Глава двадцать шестая. «Тайна Табасы»"),
    27: ("Twenty-Seven", "Haruna's Secret", "第二十七章「ハルナの秘密」", "Глава двадцать седьмая. «Тайна Харуны»"),
    28: ("Twenty-Eight", "Night's Secret", "第二十八章「夜の秘密」", "Глава двадцать восьмая. «Тайна ночи»"),
}


def main():
    for idx, ch in enumerate(sorted(TITLES)):
        word, en_title, ja, ru = TITLES[ch]
        k = 20 + idx
        script = ROOT / 'game' / 'chapters' / str(ch) / ('script-ch%d.rpy' % ch)
        text = script.read_text(encoding='utf-8')
        if 'from _call_overlay_screen_%d' % k in text:
            print('skip (already present)', script.relative_to(ROOT), 'K=%d' % k)
            continue
        marker = 'label ch%d:\n    $ tndl(None)\n' % ch
        assert marker in text, script
        old_en = "Chapter %s: '%s'{#ch%d_title}" % (word, en_title, ch)
        call = ('    # [TITLE] титульная карточка → overlay_screen (K=%d)\n'
                '    call overlay_screen("overlay", "%s", isUseBlur=False, text_mode="black") from _call_overlay_screen_%d\n'
                '    pause(2)\n' % (k, old_en, k))
        text = text.replace(marker, marker + call, 1)
        script.write_text(text, encoding='utf-8')
        for lang, value in (('japanese', ja), ('russian', ru)):
            p = ROOT / 'game' / 'tl' / lang / ('ch%d_1_overlays.rpy' % ch)
            body = ('# ch%d: title overlay\n'
                    'translate %s strings:\n\n'
                    '    old "%s"\n'
                    '    new "%s"\n' % (ch, lang, old_en, value))
            p.write_text(body, encoding='utf-8')
            print('wrote', p.relative_to(ROOT))
        print('patched', script.relative_to(ROOT), 'K=%d' % k)


if __name__ == '__main__':
    main()
