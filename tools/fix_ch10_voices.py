#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix ch10_1: add 2 missing non-voiced lines, renumber Haruna tags."""
import re

PATH = "game/chapters/10/script-ch10_1.rpy"

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: Renumber ch10_h_019..063 -> 020..064 (highest first to avoid collisions)
for n in range(63, 18, -1):
    old = f"ch10_h_{n:03d}"
    new = f"ch10_h_{n+1:03d}"
    content = content.replace(old, new)

# Step 2: Insert missing Haruna line after h_018 block.
# The h_018 block ends with:
#   h "I'm glad you found the bag. / Really. {#ch10_h_019}"   <- wait, after renumber this is h_019
# Let me find the anchor: the line "# ハルナ：……。  [null]" comment followed by "# ハルナ：ねぇ、平賀くん。"
# After renumber, the old h_019 became h_020. So the block now reads:
#   voice "ch10_h_020"
#   h "Hey, Hiraga-kun. {#ch10_h_020}"
# We need to insert before that:
#   h "…{#ch10_h_019}"
anchor = '        # ハルナ：……。  [null]\n        # ハルナ：ねぇ、平賀くん。  [voice 2474]'
assert anchor in content, "anchor for Haruna not found"
insert = ('        # ハルナ：……。  [null]\n'
          '        h "…{#ch10_h_019}"\n'
          '        # JA[null]: ハルナ：……。\n'
          '        # ハルナ：ねぇ、平賀くん。  [voice 2474]')
content = content.replace(anchor, insert)

# Step 3: Insert missing Colbert line in scene 436.
# Anchor: after l_005 block, before the SPRITE hide line.
# Current text:
#   l "…{#ch10_l_005}"
#   # JA[7146]: ルイズ：……。
#   # [SPRITE lay10 hide] [SPRITE lay9 image=+935 → c 1]
anchor2 = '        l "…{#ch10_l_005}"\n        # JA[7146]: ルイズ：……。\n        # [SPRITE lay10 hide] [SPRITE lay9 image=+935 → c 1]'
assert anchor2 in content, "anchor for Colbert not found"
insert2 = ('        l "…{#ch10_l_005}"\n'
           '        # JA[7146]: ルイズ：……。\n'
           '        # コルベール：……。\n'
           '        c "…{#ch10_c_003}"\n'
           '        # JA[null]: コルベール：……。\n'
           '        # [SPRITE lay10 hide] [SPRITE lay9 image=+935 → c 1]')
content = content.replace(anchor2, insert2)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("Done. Verifying...")
with open(PATH, "r", encoding="utf-8") as f:
    new_content = f.read()

# Count h tags
h_tags = re.findall(r"ch10_h_(\d+)", new_content)
print(f"Haruna tags: {len(h_tags)} occurrences, {len(set(h_tags))} unique")
nums = sorted(set(int(t) for t in h_tags))
print(f"Haruna range: {nums[0]:03d}..{nums[-1]:03d}")
# Check no gaps
expected = list(range(1, len(nums)+1))
if nums == expected:
    print("✓ Haruna numbering is sequential 001..%03d" % nums[-1])
else:
    missing = set(expected) - set(nums)
    print(f"✗ Gaps: {sorted(missing)}")

# Count c tags
c_tags = re.findall(r"ch10_c_(\d+)", new_content)
print(f"Colbert tags: {len(c_tags)} occurrences, {len(set(c_tags))} unique")

# Check the inserted lines
assert 'h "…{#ch10_h_019}"' in new_content, "Haruna insert missing"
assert 'c "…{#ch10_c_003}"' in new_content, "Colbert insert missing"
print("✓ Both missing lines inserted")

# Total dialogue lines
dlg = re.findall(r'^\s+[a-z]+\s+"', new_content, re.MULTILINE)
print(f"Total dialogue lines: {len(dlg)} (was 172, expect 174)")
