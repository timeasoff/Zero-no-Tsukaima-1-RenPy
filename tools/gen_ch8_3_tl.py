#!/usr/bin/env python3
import re

# Read the script to extract voice lines with proper JA text
with open('game/chapters/8/script-ch8_3.rpy', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all voice lines with their EN and JA text
# Pattern: voice "ch8_XXX"\n<speaker> "EN text {#ch8_XXX}"\n# JA[NNNN]: JA text
pattern = r'voice\s+"(ch8_[a-z0-9_]+)"\n\s*[a-z_]+\s+"([^"]+)\s+\{#\1\}"\n\s*# JA\[\d+\]:\s*([^\n]+)'

matches = re.findall(pattern, content)

print(f"Found {len(matches)} voice lines")

# Write Japanese TL file
with open('game/tl/japanese/ch8_3_dialogs.rpy', 'w', encoding='utf-8') as f:
    f.write(f'# ===== ch8.3: {len(matches)} strings (dialogues) =====\n')
    f.write('translate japanese strings:\n\n')
    for voice_name, en_text, ja_text in matches:
        # Clean up JA text - remove speaker prefix (text before first colon)
        if '：' in ja_text:
            ja_clean = ja_text.split('：', 1)[1].strip()
        else:
            ja_clean = ja_text
        # Ensure EN text uses single braces
        f.write('    old "' + en_text + ' {#' + voice_name + '}"\n')
        f.write(f'    new "{ja_clean}"\n\n')

print(f"Written {len(matches)} entries to ch8_3_dialogs.rpy")

# Now also generate thoughts file - look for internal thoughts in the script
# Thoughts are lines without voice that are internal monologue
# In the script, they appear as comments like: # サイト：（...）
# We need to find them in the source and create TL entries

# Let me also check the source for thoughts
with open('ps2_source/chapters/chapter_09_決意のお姫さま.txt', 'r', encoding='utf-8') as f:
    source = f.read()

# Find thoughts in scenes 424-428 (they use （ ） format)
thoughts = re.findall(r'（([^）]+)）', source)
# Filter for scenes 424-428 range - just include all thoughts found
print(f"Found {len(thoughts)} thoughts in source")

# Write thoughts file if any
if thoughts:
    with open('game/tl/japanese/ch8_3_thoughs.rpy', 'w', encoding='utf-8') as f:
        f.write(f'# ===== ch8.3: {len(thoughts)} strings (thoughts) =====\n')
        f.write('translate japanese strings:\n\n')
        for i, thought in enumerate(thoughts, 1):
            # Use a placeholder key
            f.write(f'    old "({thought}) {{#ch8_3_thought_{i}}}"\n')
            f.write(f'    new "（{thought}）"\n\n')
    print(f"Written {len(thoughts)} thoughts to ch8_3_thoughs.rpy")