import io, re

script = io.open('game/chapters/3/script-ch3_4.rpy', encoding='utf-8').read()
voices = re.findall(r'voice "([^"]+)"', script)

vm = {}
for ln in io.open('references/voice_id_map.csv', encoding='utf-8').read().splitlines():
    if ',' in ln and not ln.startswith('#'):
        k, v = ln.split(',', 1)
        vm[v.strip()] = k.strip()

missing = []
for vk in voices:
    if vk not in vm.values():
        missing.append(vk)

print('P4 voice keys in script:', len(set(voices)))
print('Missing keys:', set(missing))
print('Total unique keys:', len(vm.values()))