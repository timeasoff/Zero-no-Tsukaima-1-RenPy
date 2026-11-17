#!/usr/bin/env python3
"""Parse chapter_12 source scenes into an ordered item list for ch11 parts 3/4.

Output JSON: reports/ch11/parse_478_509.json — evidence/helper for the port.
Items are either:
  {"kind": "scene", "no": N}
  {"kind": "event", "src": "..."}               # raw bracketed event line
  {"kind": "dlg", "idx": i, "speaker": "...", "ja": "...", "voice": N|None,
   "thought": bool, "src": "..."}
  {"kind": "choice", "options": [{"text":..., "target":N}, ...]}
  {"kind": "date", "kind2": "date"|"proceed", "text":..., "target":N|None}
  {"kind": "goto", "target": N}
  {"kind": "like", "speaker": "...", "value": N}
"""
import json
import re
import sys

SRC = (sys.argv[4] if len(sys.argv) > 4 else
       'ps2_source/chapters/chapter_12_ハルナの決意.txt')


def parse(start_scene, end_scene):
    lines = open(SRC, encoding='utf-8').read().split('\n')
    # locate scene range
    a = next(i for i, l in enumerate(lines)
             if re.match(r'\s*---- SCENE %04d ----' % start_scene, l))
    b = next((i for i, l in enumerate(lines)
              if re.match(r'\s*---- SCENE %04d ----' % end_scene, l)), len(lines))

    items = []
    seq = 0  # unique sequential key per dialogue item
    cur = None  # pending dialogue
    scene = None

    def flush():
        nonlocal cur
        if cur is not None:
            items.append(cur)
            cur = None

    for raw in lines[a:b]:
        s = raw.strip()
        if not s:
            continue
        m = re.match(r'\s*---- SCENE (\d+) ----', raw)
        if m:
            flush()
            scene = int(m.group(1))
            items.append({'kind': 'scene', 'no': scene})
            continue
        if s.startswith('【選択肢】'):
            flush()
            mm = re.match(r'【選択肢】(.*?)\s*→\s*scene\s*(\d+)', s)
            text = mm.group(1) if mm else s
            target = int(mm.group(2)) if mm else None
            # choices are accumulated: attach to last choice item or create
            if items and items[-1].get('kind') == 'choice':
                items[-1]['options'].append({'text': text, 'target': target})
            else:
                items.append({'kind': 'choice', 'options': [
                    {'text': text, 'target': target}]})
            continue
        if s.startswith('【デート進行】'):
            flush()
            mm = re.search(r'scene\s*(\d+)', s)
            items.append({'kind': 'date', 'kind2': 'proceed', 'text': '',
                          'target': int(mm.group(1)) if mm else None})
            continue
        if s.startswith('【デート】'):
            flush()
            mm = re.match(r'【デート】(.*?)\s*→\s*scene\s*(\d+)', s)
            items.append({'kind': 'date', 'kind2': 'date',
                          'text': mm.group(1) if mm else s,
                          'target': int(mm.group(2)) if mm else None})
            continue
        if s.startswith('→ next scene'):
            flush()
            items.append({'kind': 'goto',
                          'target': int(re.search(r'(\d+)', s).group(1))})
            continue
        if s.startswith('【好感度】'):
            flush()
            mm = re.match(r'【好感度】(\S+)\s+(-?\d+)', s)
            items.append({'kind': 'like', 'speaker': mm.group(1),
                          'value': int(mm.group(2))})
            continue
        if s.startswith('['):
            flush()
            items.append({'kind': 'event', 'src': s})
            continue

        # dialogue: either starts a new one (speaker：) or continues current
        vm = re.search(r'\[voice (\d+)\]', s)
        dm = re.match(r'([^：]+)：(.*)', s)
        if dm:
            flush()
            speaker = dm.group(1).strip()
            text = dm.group(2)
            text = re.sub(r'\s*\[voice \d+\]\s*$', '', text).strip()
            cur = {'kind': 'dlg', 'idx': seq, 'speaker': speaker,
                   'ja': text, 'voice': int(vm.group(1)) if vm else None,
                   'thought': speaker == 'null' or text.startswith('（'),
                   'src': s}
            seq += 1
            if vm:
                flush()
            continue
        if cur is not None:
            text = re.sub(r'\s*\[voice \d+\]\s*$', '', s).strip()
            cur['ja'] += text
            if vm:
                cur['voice'] = int(vm.group(1))
                flush()
            continue
        # bare narrative line without voice (e.g. "………。")
        flush()
        items.append({'kind': 'dlg', 'idx': seq, 'speaker': 'null',
                      'ja': s, 'voice': None, 'thought': True, 'src': s})
        seq += 1

    flush()
    return items


if __name__ == '__main__':
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 478
    end = int(sys.argv[2]) if len(sys.argv) > 2 else 510
    out = sys.argv[3] if len(sys.argv) > 3 else \
        'reports/ch11/parse_%d_%d.json' % (start, end - 1)
    data = parse(start, end)
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    dlgs = [x for x in data if x['kind'] == 'dlg']
    print('items', len(data), 'dlgs', len(dlgs),
          'voiced', sum(1 for x in dlgs if x['voice']), 'out', out)
