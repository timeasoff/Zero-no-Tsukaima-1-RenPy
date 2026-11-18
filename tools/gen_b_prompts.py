#!/usr/bin/env python3
"""Build independent macro-semantic (B) prompts from generated A prompts.

semantic-audit-b is absent in this project. B prompts reuse A's isolated input
but replace role/focus with macro semantics and write to b/<new_run_id>.md.
"""
from pathlib import Path
import re
import datetime

ROOT = Path(__file__).parent.parent
SRC = ROOT / 'reports/full_audit/prompts'
FOCUS_B = '''ФОКУС AUDITOR B — макросемантика и логика:
- субъект и объект действий (кто делает, кто претерпевает, о ком речь);
- местоименные связи (он/она/его/её/это/тот);
- причинно-следственные связи и временная последовательность;
- намерения персонажей и их отношения, цели действий;
- идиомы, метафоры, устойчивые выражения;
- логические противоречия между соседними репликами, целостность сцены.

ЧТО НЕ ВХОДИТ В ЗАДАЧУ:
- лексические оттенки, эмоции, мимика, модальность — микро-семантика (A);
- речевой акт, подтекст, сила реплики — прагматика (C);
- грамматика, стиль, оформление — отдельные слои.

ПРОЦЕДУРА (TARGET — реплика/строка этой части):
1. Прочитай TARGET (JA и EN/RU); PREVIOUS и NEXT — ТОЛЬКО как контекст.
2. Установи логику JA: кто действует, на кого, почему, в каком порядке.
3. Сверь с EN и RU: сохранены ли субъекты, объекты, связи, цели.
4. Для каждого расхождения создай находку: source + current + problem +
   reason + suggestion + issue_type + severity + classification.

ЕДИНИЦА АУДИТА: одна реплика/строка этой части (TARGET); соседние — контекст.
ПРАВИЛА: не считай литературное предпочтение ошибкой; не дублируй другие слои;
будь точен в цитатах; не выдумывай; не исправляй перевод — только evidence.
'''


def main():
    seq = 0
    for p in sorted(SRC.glob('a_ch*.txt')):
        s = p.read_text(encoding='utf-8')
        s = s.replace('Ты - Semantic Auditor A.', 'Ты - Semantic Auditor B (macro semantics and logic).')
        s = s.replace('.agents/skills/semantic-audit-a/SKILL.md',
                      '(отдельного B-скилла в проекте нет — работай по этому заданию)')
        # replace focus block from "ФОКУС AUDITOR A" up to "ЕДИНИЦА АУДИТА"
        s = re.sub(r'ФОКУС AUDITOR A.*?(?=ЕДИНИЦА АУДИТА)', FOCUS_B + '\n', s, flags=re.S)
        s = re.sub(r'1\. Прочитай свой SKILL.*?\n', '', s)
        s = s.replace('"audit_id": "sma-a"', '"audit_id": "sma-b"')
        s = s.replace('"audit_type": "semantic-audit-a"', '"audit_type": "semantic-audit-b (manual)"')
        # new unique run_id and b/ output path
        seq += 1
        stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        newid = f'{stamp}-b{seq:02d}'
        s = re.sub(r'"run_id": "[0-9]{8}-[0-9]{6}-[a-z0-9]+"', f'"run_id": "{newid}"', s)
        # replace all a/<id>.md paths with b/<newid>.md
        s = re.sub(r'/a/[0-9]{8}-[0-9]{6}-[a-z0-9]+\.md', f'/b/{newid}.md', s)
        s = re.sub(r'(reports/sma/[^/\s]+/[^/\s]+/)a/[0-9]{8}-[0-9]{6}-[a-z0-9]+\.md',
                   rf'\1b/{newid}.md', s)
        out = SRC / p.name.replace('a_ch', 'b_ch')
        out.write_text(s, encoding='utf-8')
        paths = re.findall(r'reports/sma/\S+?\.md', s)
        print(out.name, newid, paths[:2])


if __name__ == '__main__':
    main()
