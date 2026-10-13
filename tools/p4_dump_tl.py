import io
import csv
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def parse_pairs(path):
    pairs = []
    old = None
    for ln in io.open(path, encoding='utf-8').read().splitlines():
        s = ln.strip()
        if s.startswith('old '):
            old = s[4:].strip()
            if old.startswith('"') and old.endswith('"'):
                old = old[1:-1]
        elif s.startswith('new ') and old is not None:
            new = s[4:].strip()
            if new.startswith('"') and new.endswith('"'):
                new = new[1:-1]
            pairs.append((old, new))
            old = None
    return pairs


ja = parse_pairs('game/tl/japanese/dialogs.rpy')
ru = parse_pairs('game/tl/russian/dialogs.rpy')

ru_by_old = {}
for o, n in ru:
    ru_by_old.setdefault(o, []).append(n)

# P4 block starts at first pair whose old is a known P4 first line
boundary = None
for i, (o, n) in enumerate(ja):
    if o == 'Haruna-san, excuse me.':
        boundary = i
        break

print('total JA pairs:', len(ja))
print('boundary index:', boundary)
if boundary is None:
    sys.exit(1)

rows = []
for o, jn in ja[boundary:]:
    rn = ru_by_old.get(o, [''])[0]
    rows.append((o, jn, rn))

out = io.open('tools/p4_tl_dump.csv', 'w', encoding='utf-8', newline='')
w = csv.writer(out)
w.writerow(['old_en', 'ja_new', 'ru_new'])
for r in rows:
    w.writerow(r)
out.close()
print('dumped P4 pairs:', len(rows))
