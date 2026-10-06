# Data Schema (v1)

| Dataset | Key fields |
|---|---|
| concepts.json | id, name, chinese, pinyin, tradition, page, evidence, related[] |
| practices.json | id, name, chinese, pinyin, tradition, page, evidence, related[] |
| experiences.json | experience_id, practice, tradition, anonymity, evidence_type, publication_status, page |
| patterns.json | id, phenomenon, report_count, practices[], evidence_basis, page |
| relationships.json | from, to, relation |
| sources.json | id, title, type, language, url, pages_used_in[] |
