# Dao Data

Structured data hub for the [Dao knowledge base](https://daoismhub.com/) — the machine-readable layer
behind the knowledge graph.

This site documents entities, relationships, sources and schemas. Data files live
in the main repository under `src/data/` (`concepts.json`, `practices.json`,
`relationships.json`, `sources.json`); authored entities live in the content
collections (`texts/`, `people/`, `translations/`, `timeline/`, `questions/`).

## Current state

Generated automatically from the main-site content collections and data files;
do not edit by hand. Counting basis: published records per collection (status:
published), graph edges in `relationships.json`, source records in `sources.json`.

| Layer | Count |
|---|---|
| Concepts | 18 |
| Practices | 10 |
| People | 31 |
| Texts | 10 |
| Translations | 39 |
| Timeline events | 18 |
| Research pages | 9 |
| Questions | 28 |
| Problems | 17 |
| Comparisons | 11 |
| Glossary entries | 55 |
| Stories | 70 |
| Experiences | 32 |
| Patterns | 3 |
| Guides | 9 |
| Tools | 3 |
| Blog posts | 4 |
| Knowledge-graph edges | 1550 |
| Sources | 200 |

- **Experience system**: 32 anonymized experiences, 3 patterns,
  28 questions from Chinese community sources (see the source map in the main repo).
- Main site: see [daoismhub.com](https://daoismhub.com/).

## Explore the main site

Every registry row and every entity page on this site links back to the full
article on [daoismhub.com](https://daoismhub.com/). Start here:

- [DaoismHub home](https://daoismhub.com/) — the complete knowledge base
- [Concepts](https://daoismhub.com/concepts/) · [Practices](https://daoismhub.com/practices/) · [Glossary](https://daoismhub.com/glossary/)
- [Texts](https://daoismhub.com/texts/) · [Translations](https://daoismhub.com/translations/) · [People](https://daoismhub.com/people/)
- [Research](https://daoismhub.com/research/) · [Comparisons](https://daoismhub.com/comparisons/) · [Problems](https://daoismhub.com/problems/)
- [Experiences](https://daoismhub.com/experiences/) · [Stories](https://daoismhub.com/stories/) · [Timeline](https://daoismhub.com/timeline/)
- [Guides](https://daoismhub.com/guides/) · [Tools](https://daoismhub.com/tools/)

## What is here

- **Entities** — concepts, practices, people, texts, translations, timeline
- **Experience system** — anonymized practitioner records, patterns, questions
- **Knowledge graph** — typed relationships between entities
- **Schemas** — data schema and evidence classification reference

!!! note "Evidence discipline"
    Every record carries an evidence class. Practitioner reports are never
    conflated with scientific evidence; legends are never presented as history.
