#!/usr/bin/env python3
"""Apply Analyzer-confirmed semantic/pragmatic fixes (prompt 09).

Each change is keyed by the Ren'Py translation tag so identical old strings
in different places are handled independently. JA `new` is NEVER touched.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent

# tag -> (new EN string with tag, new RU string)
SP90 = {
 'sp90_s1565_008': ("Y-Yes, that's right!{#sp90_s1565_008}", "Д-Да, так и есть!"),
 'sp90_s1580_041': ("(Hm, those are serious eyes…){#sp90_s1580_041}", "_Хм… Глаза у неё серьёзные…_"),
 'sp90_s1608_013': ("(I-If it had failed, my head would've ended up like that?){#sp90_s1608_013}",
                    "_Е-Если бы не получилось, моя голова была бы такой?_"),
 'sp90_s1608_015': ("(S-So I was made a practice dummy for magic she wasn't even sure of… Me…){#sp90_s1608_015}",
                    "_Так я стал подопытным для магии, в которой она даже не уверена… Я…_"),
 'sp90_s1613_002': ("(I-I have to run… but…){#sp90_s1613_002}", "_Н-Нужно бежать… но…_"),
 'sp90_s1613_003': ("(...No good. The rope won't come undone!){#sp90_s1613_003}",
                    "_…Не выходит. Верёвка не развязывается!_"),
 'sp90_s1617_002': ("(R-Really… it might actually succeed?){#sp90_s1617_002}", "_П-Правда… может, и получится?_"),
 'sp90_s1617_003': ("(N-No. I've got to believe in Louise…){#sp90_s1617_003}", "_Н-Нет. Я должен верить Луизе…_"),
 'sp90_s1617_007': ("(...Y-You've got to be kidding! Louise is in a terrible mood today!){#sp90_s1617_007}",
                    "_…Ч-Чёрт! Сегодня настроение Луизы точно не к добру!_"),
 'sp90_s1618_002': ("(...I-If it fails, what'll happen?){#sp90_s1618_002}", "_…А-Если не получится, что тогда?_"),
 'sp90_s1618_003': ("(...A pleasant splatter? Or before that I'll be wiped out without a trace…){#sp90_s1618_003}",
                    "_…Весёлый сплэттер? Или раньше этого от меня не останется и следа…_"),
 'sp90_s1618_005': ("(...A-Ah? Maybe I… die?){#sp90_s1618_005}", "_…А-Ах? Может, я… умру?_"),
 'sp90_s1556_041': ("Y-Yes! What is it?!{#sp90_s1556_041}", "Д-Да! Что случилось?!"),
}

SP91_RU = {
 'sp91_s1740_013': "Не смей бросать такую прекрасную госпожу и вилять хвостом перед другими девочками, ладно?",
 'sp91_s1808_030': "…Не ослышайся слов госпожи, ладно?",
 'sp91_s1810_006': "Мм, если убежишь — я закричу, ладно?",
 'sp91_s1824_004': "…Разве это не странно?",
}

CH27_RU = {
 'ch27_s_142': "Хм… Наверное, на ней вина как у бомбардировщика…",
 'ch27_s_140': "Из-за отдельной личности Акины оказаться в таком положении…",
}


def patch_pairs(path, mapping, lang):
    """Replace `old` (all langs) and `new` (RU/EN only) tagged by mapping keys."""
    lines = Path(path).read_text(encoding='utf-8').split('\n')
    out, old = [], None
    changed = []
    for line in lines:
        mo = re.match(r'^\s*old "(.*)"', line)
        if mo:
            old = mo.group(1)
            mtag = re.search(r'\{#([^}]+)\}', old)
            tag = mtag.group(1) if mtag else None
            if tag and tag in mapping and mapping[tag][0] is not None:
                line = re.sub(r'(old \").*(\")', lambda m: m.group(1) + mapping[tag][0] + m.group(2), line)
                if tag + '/old' not in changed:
                    changed.append(tag + '/old')
            out.append(line)
            continue
        mn = re.match(r'^\s*new "(.*)"', line)
        if mn and old is not None:
            mtag = re.search(r'\{#([^}]+)\}', old)
            tag = mtag.group(1) if mtag else None
            if tag and tag in mapping and lang == 'russian' and mapping[tag][1] is not None:
                line = re.sub(r'(new \").*(\")', lambda m: m.group(1) + mapping[tag][1] + m.group(2), line)
                if tag + '/new' not in changed:
                    changed.append(tag + '/new')
            old = None
        out.append(line)
    Path(path).write_text('\n'.join(out), encoding='utf-8')
    return changed


def patch_script(path, mapping):
    lines = Path(path).read_text(encoding='utf-8').split('\n')
    out = []
    changed = []
    # dialogue lines contain EN string + {#tag}
    for line in lines:
        mtag = re.search(r'\{#([^}]+)\}', line)
        tag = mtag.group(1) if mtag else None
        if tag and tag in mapping and re.match(r'^\s*[A-Za-z_]\w*\s+"', line):
            line = re.sub(r'(\").*(\"{#)', lambda m: m.group(1) + mapping[tag][0].split('{#')[0] + m.group(2), line)
            changed.append(tag)
        out.append(line)
    Path(path).write_text('\n'.join(out), encoding='utf-8')
    return changed


def main():
    print('sp90 TL ja:', patch_pairs(ROOT / 'game/tl/japanese/sp90_dialogs.rpy', SP90, 'japanese'))
    print('sp90 TL ru:', patch_pairs(ROOT / 'game/tl/russian/sp90_dialogs.rpy', SP90, 'russian'))
    print('sp90 script:', patch_script(ROOT / 'game/chapters/extra/sp90.rpy', SP90))
    # sp91 RU only (EN unchanged)
    m91 = {k: (None, v) for k, v in SP91_RU.items()}
    print('sp91 TL ru:', patch_pairs(ROOT / 'game/tl/russian/sp91_dialogs.rpy', m91, 'russian'))
    # ch27 RU only
    m27 = {k: (None, v) for k, v in CH27_RU.items()}
    print('ch27 TL ru:', patch_pairs(ROOT / 'game/tl/russian/ch27_3_dialogs.rpy', m27, 'russian'))
    # ch26_4b typo
    for p in [ROOT / 'game/tl/russian/ch26_4b_choises.rpy', ROOT / 'tools/gen_ch26_4b.py']:
        s = p.read_text(encoding='utf-8')
        if 'как следуют' in s:
            p.write_text(s.replace('как следуют', 'как следует'), encoding='utf-8')
            print('typo fixed', p.name)


if __name__ == '__main__':
    main()
