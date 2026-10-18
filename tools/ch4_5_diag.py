"""Диагностика расхождения голосов ch4.5: скрипт vs канон."""
import re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, "game", "chapters", "4", "script-ch4_5.rpy")

with open(SCRIPT, encoding="utf-8") as f:
    content = f.read()

# All voice lines in order
voices = re.findall(r'voice "(ch4\.5_([a-z]+)_(\d+))"', content)
print(f"Total voice lines in script: {len(voices)}")

# Count per speaker
from collections import Counter
spk_count = Counter(spk for _, spk, _ in voices)
for spk, cnt in sorted(spk_count.items()):
    print(f"  {spk}: {cnt}")

# Check for duplicates
seen = {}
for full, spk, num in voices:
    key = f"{spk}_{num}"
    if key in seen:
        print(f"  !! DUPLICATE: {full} (first at line {seen[key]})")
    else:
        seen[key] = full

# List all voice names in order
print("\nAll voice names in script order:")
for i, (full, spk, num) in enumerate(voices, 1):
    print(f"  {i:3d}. {full}")

# Canon voices count
CANON_VOICES_COUNT = 109
print(f"\nCanon voices in CANON_VOICES: {CANON_VOICES_COUNT}")
print(f"Difference: {len(voices) - CANON_VOICES_COUNT}")
