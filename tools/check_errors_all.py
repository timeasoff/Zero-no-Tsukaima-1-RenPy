import io

r = io.open('reports/check_project.md', encoding='utf-8').read()
grab = False
for ln in r.splitlines():
    if ln.startswith('## ERROR'):
        grab = True
        print(ln)
        continue
    if ln.startswith('## '):
        grab = False
        continue
    if grab and ln.startswith('- '):
        print(ln)
