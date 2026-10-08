#!/usr/bin/env python3
"""Regenerate all data-site entity/graph pages from main-site frontmatter + data JSON.
Run after every main-site batch. Idempotent. Skips _template.md files."""
import os, json, re, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, 'site/src/content')
OUT = os.path.join(ROOT, 'data-site/docs')

def fm(path):
    t = open(path).read()
    m = re.match(r'^---\n(.*?)\n---', t, re.S)
    d = {}
    if m:
        for line in m.group(1).split('\n'):
            line = line.strip()
            if not line or line.startswith('#'): continue
            if ':' in line:
                k, v = line.split(':', 1)
                d[k.strip()] = v.strip().strip('"')
    return d

def collect(coll):
    d = os.path.join(SITE, coll)
    items = []
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if f.endswith('.md') and not f.startswith('_'):
                items.append((f[:-3], fm(os.path.join(d, f))))
    return items

specs = [
    ('concepts', 'Concepts', 'concept', ['title','chinese','pinyin','tradition','evidence']),
    ('practices', 'Practices', 'practice', ['title','chinese','pinyin','tradition','difficulty']),
    ('people', 'People', 'person', ['title','chinese','dates','tradition','historicity','page']),
    ('texts', 'Texts', 'text', ['title','chinese','author','dynasty','genre']),
    ('translations', 'Translations', 'translation', ['title','sourceText','chapter']),
    ('timeline', 'Timeline', 'event', ['title','periodStart','periodEnd','eventType']),
    ('glossary', 'Glossary', 'term', ['title','chinese','pinyin','literalMeaning','recommended']),
    ('stories', 'Stories', 'story', ['title','tradition','sourceText']),
    ('research', 'Research', 'study', ['title','question']),
    ('comparisons', 'Comparisons', 'comparison', ['title','entities']),
    ('problems', 'Problems', 'problem', ['title','question','shortAnswer']),
    ('questions', 'Questions', 'question', ['title','question','answerState']),
    ('tools', 'Tools', 'tool', ['title','purpose']),
]
counts = {}
for coll, name, singular, cols in specs:
    items = collect(coll)
    if not items: continue
    counts[coll] = len(items)
    hdr = '| id | ' + ' | '.join(cols) + ' |'
    lines = [f'# {name}', '', f'{singular} records from the {coll} content collection — {len(items)} records.', '', hdr, '|' + '---|'*(len(cols)+1)]
    for slug, d in items:
        vals = []
        for c in cols:
            if c == 'page':
                v = f"/{coll}/{slug}/"
            else:
                v = str(d.get(c,'')).replace('|','/').strip()
                if c == 'evidence': v = v[:60]
            vals.append(v)
        lines.append('| ' + slug + ' | ' + ' | '.join(vals) + ' |')
    open(os.path.join(OUT, 'entities', f'{coll}.md'),'w').write('\n'.join(lines)+'\n')

exps = collect('experiences')
rows = [f"| {d.get('experienceId',slug)} | {d.get('title','')} | {d.get('confidence','—')} | /experiences/{slug}/ |" for slug, d in exps]
t = """# Experience System

Anonymized practitioner material — cleaned, classified, structured.

**Status:** seeded from Chinese community sources (Tieba meditation forums via
search index, 163.com teacher Q&A, Xinli001 Q&A, Baidu Health, Zhihu columns).
All records paraphrased and anonymized; no usernames, no direct quotes without
permission.

## Current records — %d

| id | theme | confidence | page |
|---|---|---|---|
%s

## Privacy rules

Every record is paraphrased and anonymized before entry: no usernames, no
locations, no direct quotes without permission. Missing fields are recorded
as "Not reported" — never filled in.

## Three-layer interpretation

Each record carries practitioner / traditional / alternative interpretations
kept strictly separate; confidence is graded high (direct long report), medium
(community article), low (short snapshot material).
""" % (len(exps), '\n'.join(rows))
open(os.path.join(OUT, 'experiences', 'index.md'),'w').write(t)

pats = collect('patterns')
rows = [f"| {slug} | {d.get('phenomenon','')} | {d.get('reportCount','')} | {d.get('evidenceBasis','')} | /patterns/{slug}/ |" for slug, d in pats]
t = """# Experience Patterns

Recurring phenomena across independent anonymized reports — %d patterns.

| id | phenomenon | reports | evidence basis | page |
|---|---|---|---|---|
%s

Language discipline: "recurring reports in the practitioner archive" —
never "scientifically proven" unless actual research supports it. Evidence
basis is graded conservatively: `partially-researched` only when adjacent
research exists in a weak sense; `practitioner-reports-only` otherwise.
""" % (len(pats), '\n'.join(rows))
open(os.path.join(OUT, 'experiences', 'patterns.md'),'w').write(t)

qs = collect('questions')
rows = [f"| {slug} | {d.get('answerState','')} | {d.get('question','')} | /questions/{slug}/ |" for slug, d in qs]
t = """# Questions

The question collection — %d records, with answer states.

| id | answer state | question | page |
|---|---|---|---|
%s

## Discipline

A question is `answered` only when the sources settle the terminology or the
record; questions where empirical literature is missing stay `open` (or
`investigating` when adjacent evidence exists) with the absence stated
explicitly — never closed by assertion.
""" % (len(qs), '\n'.join(rows))
open(os.path.join(OUT, 'experiences', 'questions.md'),'w').write(t)

r = json.load(open(os.path.join(SITE, '../data/relationships.json')))
edges = r['items']; relc = Counter(e['relation'] for e in edges)
rows = "\n".join(f"| {e['from']} | {e['to']} | {e['relation']} |" for e in sorted(edges, key=lambda x:(x['from'],x['to'])))
md = f"""# Relationship Registry

Knowledge-graph edges — {len(edges)} total. Top-level key: `items` in
`site/src/data/relationships.json`.

## Relation types

| relation | count |
|---|---|
""" + "\n".join(f"| {k} | {v} |" for k,v in sorted(relc.items())) + f"""

## All edges

| from | to | relation |
|---|---|---|
{rows}

Generated from the site data file; do not edit by hand.
"""
open(os.path.join(OUT, 'graph', 'relationships.md'),'w').write(md)

s = json.load(open(os.path.join(SITE, '../data/sources.json')))
items = s['items']; tc = Counter(i['type'] for i in items)
md = f"""# Sources Registry

All sources used on the site — {len(items)} total. Registry file:
`site/src/data/sources.json`.

## By type

| type | count |
|---|---|
""" + "\n".join(f"| {k} | {v} |" for k,v in sorted(tc.items())) + f"""

## Full registry

| id | title | type | pages used in |
|---|---|---|---|
"""
for i in sorted(items, key=lambda x:x['id']):
    pages = "; ".join(i.get('pages_used_in',[]))
    md += f"| {i['id']} | {i['title']} | {i['type']} | {pages} |\n"
md += "\nGenerated from the site data file; do not edit by hand.\n"
open(os.path.join(OUT, 'graph', 'sources.md'),'w').write(md)

print("counts:", counts)
print("edges:", len(edges), "sources:", len(items), "experiences:", len(exps), "patterns:", len(pats), "questions:", len(qs))
