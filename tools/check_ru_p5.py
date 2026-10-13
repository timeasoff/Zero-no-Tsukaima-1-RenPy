import io

ru = io.open('game/tl/russian/dialogs.rpy', encoding='utf-8').read()
checks = [
    'Did you hear what she said? ...Louise!?',
    'N-no, not that... anyway!',
    'W-what...?',
]
for c in checks:
    print(repr(c), '->', c in ru)