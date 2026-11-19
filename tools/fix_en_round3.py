#!/usr/bin/env python3
"""Round-3 audit: fix EN base strings that diverge from JA (JA new is canonical/read-only).

For each tag, the EN script line and the `old` lines in tl/japanese + tl/russian
are replaced together. JA `new` strings are never touched.
"""
from pathlib import Path
import glob

ROOT = Path(__file__).parent.parent

# tag -> (old EN text without tag, new EN text without tag)
FIXES = {
    'ch23_s_101': (
        'So… the woman who took care of me when I first came to this world was Weatherly!?',
        'So… the woman who took care of Haruna when she first came to this world was Weatherly!?',
    ),
    'ch23_l_012': (
        "The bomber's attack got the Zero Fighter too… It looks like it was destroyed this morning.",
        "The bomber's attack made the Zero Fighter prey too… It looks like it was destroyed this morning.",
    ),
    'ch25_k_012': (
        "I-I'm not gloomy at all…",
        "I-I'm not gloomy or anything…",
    ),
    'ch25_s_057': (
        'Um, I was hoping you could tell me about that letter…',
        "Um, I wouldn't mind hearing about that letter…",
    ),
    'ch26_l_026': (
        'Saito! What are you doing!? You can\'t win them over like that!',
        'Saito! What are you doing!? They\'d never forgive you for that!',
    ),
    'ch27_s_008': (
        "So they intend to attack amid Tristain's chaos.",
        "So they intend to take advantage of Tristain's chaos.",
    ),
    'ch27_l_042': (
        "What's the problem?",
        "Where's the problem?",
    ),
}

for tag, (old, new) in FIXES.items():
    for path in [Path(f) for f in glob.glob(str(ROOT / 'game/chapters/2[2-8]/*.rpy'))] + \
                [Path(f) for f in glob.glob(str(ROOT / 'game/tl/japanese/*.rpy'))] + \
                [Path(f) for f in glob.glob(str(ROOT / 'game/tl/russian/*.rpy'))]:
        text = path.read_text(encoding='utf-8')
        needle = old + '{#' + tag + '}'
        repl = new + '{#' + tag + '}'
        if needle in text:
            text = text.replace(needle, repl)
            path.write_text(text, encoding='utf-8')
            print(tag, '->', path.relative_to(ROOT))
