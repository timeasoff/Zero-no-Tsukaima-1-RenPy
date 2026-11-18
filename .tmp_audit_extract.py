import re, io

base = "/workspace/.tmp/opencode/review-ch2-5/"
out = io.open(base + ".tmp_audit_scope.txt", "w", encoding="utf-8")

def scenes_in_range(path, pattern, lo, hi):
    lines = io.open(base + path, encoding="utf-8").read().split("\n")
    result = []
    cur = None
    for ln in lines:
        m = re.match(pattern, ln.strip())
        if m:
            cur = int(m.group(1))
        if cur is not None and lo <= cur <= hi:
            result.append(ln)
    return result

out.write("########## CHAPTERS scenes 0076-0089 ##########\n")
out.write("\n".join(scenes_in_range(
    "ps2_source/chapters/chapter_03_黒髪の来訪者.txt",
    r"---- SCENE (\d+) ----", 76, 89)))
out.write("\n\n########## EVENTS_FULL scenes 0076-0089 ##########\n")
out.write("\n".join(scenes_in_range(
    "ps2_source/events_full/chapter_03_黒髪の来訪者.txt",
    r"## SCENE (\d+)", 76, 89)))
out.close()
print("done")
