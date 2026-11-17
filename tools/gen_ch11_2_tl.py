#!/usr/bin/env python3
"""Generate TL files for ch11_2 from script + source."""
import re
import sys

SCRIPT = 'game/chapters/11/script-ch11_2.rpy'
SRC = 'ps2_source/chapters/chapter_12_ハルナの決意.txt'

# ---- 1. Parse source: voice_id -> JA text (scenes 472-477) ----
with open(SRC, encoding='utf-8') as f:
    src_lines = f.read().split('\n')

# Find scenes 472-477
start = None
end = None
for i, ln in enumerate(src_lines):
    if ln.strip().startswith('---- SCENE 0472'):
        start = i
    elif ln.strip().startswith('---- SCENE 0478'):
        end = i
        break
if end is None:
    end = len(src_lines)

# Parse dialogues with [voice N]
# Accumulate text lines until a line with [voice N]
voice_ja = {}
cur_text = []
for ln in src_lines[start:end]:
    stripped = ln.strip()
    if stripped.startswith('[') or stripped.startswith('----') or not stripped:
        continue
    m = re.search(r'\[voice (\d+)\]', stripped)
    if m:
        vid = int(m.group(1))
        # Clean the text: remove [voice N] suffix
        text = re.sub(r'\s*\[voice \d+\]$', '', stripped)
        cur_text.append(text)
        # Join accumulated text
        full = ''.join(cur_text) if len(cur_text) == 1 else ' / '.join(cur_text)
        voice_ja[vid] = ' / '.join(cur_text)
        cur_text = []
    else:
        # Dialogue text line, add speaker prefix if not present
        cur_text.append(stripped)

# ---- 2. Parse script: voice_name -> (en_text, tag, voice_id from comments) ----
with open(SCRIPT, encoding='utf-8') as f:
    script_lines = f.read().split('\n')

entries = []
i = 0
while i < len(script_lines):
    ln = script_lines[i]
    vm = re.match(r'^    voice "([^"]+)"$', ln)
    if vm:
        vname = vm.group(1)
        # Look backwards for # JA[NNNN]: comment
        vid = None
        for j in range(i-1, max(i-6, -1), -1):
            jm = re.search(r'# JA\[(\d+)\]', script_lines[j])
            if jm:
                vid = int(jm.group(1))
                break
        # Look forward for dialogue line
        if i+1 < len(script_lines):
            dm = re.match(r'^    ([a-z]+) "([^"]+)"$', script_lines[i+1])
            if dm:
                speaker = dm.group(1)
                en_text = dm.group(2)
                entries.append({
                    'voice_name': vname,
                    'speaker': speaker,
                    'en_text': en_text,
                    'voice_id': vid,
                })
                i += 2
                continue
    i += 1

print(f"Script entries: {len(entries)}")
print(f"Source voices: {len(voice_ja)}")

# Check which entries have voice_id
missing = [e for e in entries if e['voice_id'] is None]
print(f"Entries without voice_id: {len(missing)}")

for e in entries:
    ja = voice_ja.get(e['voice_id'], '???')
    print(f"{e['voice_name']} vid={e['voice_id']}: JA={ja[:40]}")
