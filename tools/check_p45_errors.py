import io

r = io.open('reports/check_project.md', encoding='utf-8').read()
for ln in r.splitlines():
    if 'script-ch3_4' in ln or 'script-ch3_5' in ln:
        print(ln)
print('--- total errors line ---')
for ln in r.splitlines():
    if ln.startswith('## ERROR') or ln.startswith('## WARN'):
        print(ln)