import io

ja = io.open('game/tl/japanese/dialogs.rpy', encoding='utf-8').read()
ru = io.open('game/tl/russian/dialogs.rpy', encoding='utf-8').read()

checks = [
    'Haruna-san, excuse me.',
    "How's your health?",
    "I-I wouldn't say that...",
    "Don't you dislike Haruna?",
    'Fufufu, fufufufu...',
    'It was Louise who started it!',
]
print('JA file:')
for c in checks:
    print(' ', repr(c), '->', c in ja)
print('RU file:')
for c in checks:
    print(' ', repr(c), '->', c in ru)