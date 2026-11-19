#!/usr/bin/env python3
"""Extract choices that the parser absorbed into dialogue text.

For every dlg whose ja contains '【選択肢】', split it into:
  - the dialogue part (ja trimmed), and
  - choice items inserted immediately after (indices of earlier items unchanged).
Also repairs EN/RU translations in trans_<ch>.json: trims the absorbed choice
text from the dialogue translation and adds c<scene>_<target> entries.
"""
import json
import re

JA_C = re.compile(r'【選択肢】(.+?) → scene (\d+)')
EN_C = re.compile(r'【Choice】(.+?) → scene (\d+)')
RU_C = re.compile(r'【Выбор】(.+?) → scene (\d+)')


def main():
    for ch in ['90', '91']:
        pp = f'reports/extra/parse_{ch}.json'
        tp = f'reports/extra/trans_{ch}.json'
        data = json.load(open(pp, encoding='utf-8'))
        trans = json.load(open(tp, encoding='utf-8'))
        fixed_sc = fixed_tr = 0
        for sc in data['scenes']:
            new_items = []
            for item_i, it in enumerate(sc['items']):
                if it['kind'] != 'dlg' or '【選択肢】' not in it['ja']:
                    new_items.append(it)
                    continue
                cs = list(JA_C.finditer(it['ja']))
                if not cs:
                    new_items.append(it)
                    continue
                it['ja'] = it['ja'][:cs[0].start()].rstrip()
                new_items.append(it)
                for c in cs:
                    new_items.append({'kind': 'choice', 'text': c.group(1),
                                      'target': int(c.group(2))})
                fixed_sc += 1
                key = f"s{sc['no']}_{item_i}"
                pair = trans.get(key)
                if isinstance(pair, list) and len(pair) == 2:
                    en, ru = pair
                    ens, rus = list(EN_C.finditer(en)), list(RU_C.finditer(ru))
                    if ens:
                        trans[key] = [en[:ens[0].start()].rstrip(), ru[:rus[0].start()].rstrip() if rus else ru]
                        for e, r in zip(ens, rus):
                            trans[f"c{sc['no']}_{e.group(2)}"] = [e.group(1).rstrip(), r.group(1).rstrip()]
                        fixed_tr += 1
            sc['items'] = new_items
        json.dump(data, open(pp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        json.dump(trans, open(tp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(ch, 'scenes fixed', fixed_sc, 'translations fixed', fixed_tr)


if __name__ == '__main__':
    main()
