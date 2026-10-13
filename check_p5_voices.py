import io, re

script = io.open('game/chapters/3/script-ch3_5.rpy', encoding='utf-8').read()
voices = re.findall(r'voice "([^"]+)"', script)
unique = set(voices)
print('P5 voice keys:', len(unique))
for k in sorted(unique):
    print(k)