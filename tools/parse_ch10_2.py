#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract scenes 451-466 dialogue + events from chapter_11 source into structured JSON."""
import re, json

SRC = 'ps2_source/chapters/chapter_11_突然のスカウト.txt'
with open(SRC, encoding='utf-8') as f:
    lines = f.read().split('\n')

scenes = {}
cur = None
order = []
for ln in lines:
    m = re.match(r'---- SCENE (\d+) ----', ln)
    if m:
        cur = int(m.group(1))
        scenes[cur] = []
        order.append(cur)
        continue
    if cur is not None and cur >= 451 and cur <= 466:
        scenes[cur].append(ln)

def parse_scene(scene_lines):
    """Return list of items: ('event', text) or ('line', speaker, ja, voice_id)."""
    items = []
    buf = []  # accumulating dialogue text
    speaker = None
    voice = None
    for ln in scene_lines:
        s = ln.strip()
        if not s:
            continue
        em = re.match(r'(\[(?:BG|TRANS|BGM|SPRITE|LAYER|EVENT_CG|SE|TITLE|MOVE)\b.*\])', s)
        mm = re.match(r'【(選択肢|移動|デート|デート進行)】(.*)', s)
        if em:
            # flush pending
            if buf and speaker is not None:
                items.append(('line', speaker, ' / '.join(buf).strip(), voice))
                buf, speaker, voice = [], None, None
            items.append(('event', em.group(1)))
            continue
        if mm:
            if buf and speaker is not None:
                items.append(('line', speaker, ' / '.join(buf).strip(), voice))
                buf, speaker, voice = [], None, None
            items.append(('menu', mm.group(1), mm.group(2).strip()))
            continue
        # dialogue line: "Name：text" or "Name:text" (fullwidth colon) or continuation
        vm = re.search(r'\[voice\s+(\d+)\]', s)
        cm = re.match(r'([^：:]+)[：:](.*)$', s)
        if cm:
            # new speaker line
            if buf and speaker is not None:
                items.append(('line', speaker, ' / '.join(buf).strip(), voice))
                buf, speaker, voice = [], None, None
            speaker = cm.group(1).strip()
            txt = cm.group(2).strip()
            if vm:
                voice = int(vm.group(1))
                txt = re.sub(r'\[voice\s+\d+\]', '', txt).strip()
            buf = [txt]
        else:
            # continuation line
            txt = s
            if vm:
                voice = int(vm.group(1))
                txt = re.sub(r'\[voice\s+\d+\]', '', txt).strip()
            if speaker is None:
                # narration / null speaker
                speaker = 'null'
            buf.append(txt)
    if buf and speaker is not None:
        items.append(('line', speaker, ' / '.join(buf).strip(), voice))
    return items

out = {}
for sc in range(451, 467):
    out[sc] = parse_scene(scenes[sc])

with open('/tmp/ch10_2_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

# Print summary
total_lines = 0
total_voices = 0
for sc in range(451, 467):
    ls = [it for it in out[sc] if it[0] == 'line']
    vs = [it for it in out[sc] if it[0] == 'line' and it[3] is not None]
    total_lines += len(ls)
    total_voices += len(vs)
    print(f"scene {sc}: {len(ls)} lines ({len(vs)} voiced), {len(out[sc])} items")
print(f"TOTAL: {total_lines} lines, {total_voices} voiced")
