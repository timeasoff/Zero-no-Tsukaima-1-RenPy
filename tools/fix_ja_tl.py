import io

lines = io.open('game/tl/japanese/dialogs.rpy', encoding='utf-8').read().splitlines()
# Find last complete entry (old + new)
end = 0
for i in range(len(lines)):
    if lines[i].startswith('old ') and i + 1 < len(lines) and lines[i+1].startswith('    new '):
        end = i + 2
    elif lines[i].startswith('old ') and i + 1 >= len(lines):
        break

print('Last complete entry ends at line:', end)
print('Total lines:', len(lines))

clean = '\n'.join(lines[:end])

new_entries = '''

    old "Don't you dislike Haruna?"
        new "春奈のこと、気に入らないのか？"

    old "I-I wouldn't say that..."
        new "いいです……。"
'''

io.open('game/tl/japanese/dialogs.rpy', 'w', encoding='utf-8').write(clean + new_entries)
print('JA file fixed')