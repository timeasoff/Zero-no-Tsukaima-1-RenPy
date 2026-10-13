import io

ja = io.open('game/tl/japanese/dialogs.rpy', encoding='utf-8').read()
ru = io.open('game/tl/russian/dialogs.rpy', encoding='utf-8').read()

# Check last lines
print('Last 5 lines of JA file:')
for ln in ja.splitlines()[-5:]:
    print(repr(ln))

print()
print('Last 5 lines of RU file:')
for ln in ru.splitlines()[-5:]:
    print(repr(ln))