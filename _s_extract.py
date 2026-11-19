# -*- coding: utf-8 -*-
import re, io

base = "/workspace/.tmp/opencode/review-ch2-5"
script = base + "/game/chapters/2/script-ch2_3.rpy"

# Extract dialogue/choice/thought strings with their script line numbers.
# Pattern: a line containing a quote preceded by either a speaker token like
# `c "`, `th "`, `mage "`, `d "`, `unk "`, `l "`, `k "`, `s "`, or a menu choice
# `"...":`.  We just find the first double-quoted string on each line and take
# it as the EN string.
entries = []
with io.open(script, encoding="utf-8") as f:
    for lineno, raw in enumerate(f, 1):
        line = raw.rstrip("\n")
        # find first unescaped double quote
        m = re.search(r'(?<!\\)"', line)
        if not m:
            continue
        start = m.start()
        i = start + 1
        buf = []
        while i < len(line):
            ch = line[i]
            if ch == '\\' and i + 1 < len(line) and line[i+1] == '"':
                buf.append('\\"'); i += 2; continue
            if ch == '"':
                break
            buf.append(ch); i += 1
        s = ''.join(buf)
        # only consider strings that look like dialogue (reasonable length & content)
        entries.append((lineno, s))

# Load tl russian buckets into dict: old -> new (with line numbers)
tl_files = ["dialogs.rpy", "thoughs.rpy", "choises.rpy", "overlays.rpy", "characters.rpy"]
oldmap = {}
for fn in tl_files:
    path = base + "/game/tl/russian/" + fn
    try:
        lines = io.open(path, encoding="utf-8").read().split("\n")
    except FileNotFoundError:
        continue
    for idx, line in enumerate(lines):
        st = line.strip()
        if st.startswith("old "):
            # parse quoted old
            mm = re.match(r'old "(.*)"$', st)
            if not mm:
                continue
            old = mm.group(1).replace('\\"', '"')
            # find new on next lines
            new = None; newln = None
            for j in range(idx+1, min(idx+4, len(lines))):
                st2 = lines[j].strip()
                if st2.startswith("new "):
                    mm2 = re.match(r'new "(.*)"$', st2)
                    if mm2:
                        new = mm2.group(1); newln = j+1
                    break
            oldmap[old] = (new, fn, newln)

out = []
out.append("TOTAL SCRIPT STRING LINES: %d" % len(entries))
matched = 0
for lineno, s in entries:
    if s in oldmap:
        new, fn, newln = oldmap[s]
        matched += 1
        out.append("[L%d | %s:%s] OLD: %s" % (lineno, fn, newln, s))
        out.append("    NEW: %s" % (new if new is not None else "<MISSING>"))
    else:
        out.append("[L%d] OLD: %s" % (lineno, s))
        out.append("    NEW: <NO MATCH IN TL>")
out.append("MATCHED: %d / %d" % (matched, len(entries)))

with io.open(base + "/_s_dump.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("done", matched, len(entries))
