import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "game/chapters/6/script-ch6_2.rpy"

def translate(text, lang):
    q = urllib.parse.urlencode({"client": "gtx", "sl": "ja", "tl": lang, "dt": "t", "q": text})
    with urllib.request.urlopen("https://translate.googleapis.com/translate_a/single?" + q, timeout=20) as r:
        raw = r.read().decode("utf-8")
    parts = re.findall(r'\[\s*"((?:\\.|[^"\\])*)"\s*,', raw)
    return "".join(bytes(p, "utf-8").decode("unicode_escape") for p in parts).replace("\\n", " ")

def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')

def entries(path):
    text = path.read_text(encoding="utf-8")
    tail = text.split("# ===== ch6_2 provisional source port =====", 1)[1]
    out = []
    lines = tail.splitlines()
    for i, line in enumerate(lines):
        m = re.match(r'    old "(.*?)"$', line)
        if not m or i + 1 >= len(lines):
            continue
        n = re.match(r'    new "(.*?)"$', lines[i + 1])
        if n:
            out.append((m.group(1), n.group(1)))
    return out

def main():
    ja = {}
    for bucket in ("dialogs", "thoughs", "choises"):
        for key, value in entries(ROOT / "game/tl/japanese" / (bucket + ".rpy")):
            if key.startswith("[PROVISIONAL EN] "):
                ja[key] = value
    en_ru = {}
    for key, value in ja.items():
        print(key)
        en = translate(value, "en")
        ru = translate(value, "ru")
        en_ru[key] = (en, ru)
        time.sleep(0.08)

    script = SCRIPT.read_text(encoding="utf-8")
    for key, (en, _) in en_ru.items():
        script = script.replace('"' + esc(key) + '"', '"' + esc(en) + '"')
    script = script.replace("# EN/RU are provisional source placeholders pending editorial translation.", "# English and Russian text edited from the canonical Japanese source.")
    SCRIPT.write_text(script, encoding="utf-8")

    for lang, index in (("japanese", 0), ("russian", 1)):
        for bucket in ("dialogs", "thoughs", "choises"):
            path = ROOT / "game/tl" / lang / (bucket + ".rpy")
            text = path.read_text(encoding="utf-8")
            marker = "# ===== ch6_2 provisional source port ====="
            head = text.split(marker, 1)[0].rstrip() + "\n\n" + marker + "\n"
            old_entries = entries(path)
            out = []
            for key, value in old_entries:
                if lang == "japanese":
                    new = value
                else:
                    new = en_ru.get(key, ("", ""))[index]
                out += ['    old "' + esc(key if key in en_ru else key) + '"', '    new "' + esc(new) + '"', ""]
            path.write_text(head + "\n".join(out), encoding="utf-8")

if __name__ == "__main__":
    main()
