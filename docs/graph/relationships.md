# Relationships

Typed knowledge-graph edges from `data/relationships.json` — 44 edges.

| Relation | Count |
|---|---|
| `described_in` | 16 |
| `related_to` | 12 |
| `translated_as` | 5 |
| `associated_with` | 4 |
| `concerns` | 3 |
| `derived_from` | 2 |
| `discusses` | 1 |
| `investigates` | 1 |

## Supported relations

| Relation | Meaning |
|---|---|
| `belongs_to` | entity → tradition/category |
| `related_to` | concept ↔ concept |
| `described_in` | practice/concept → text or document |
| `translated_as` | concept → translation page |
| `associated_with` | person ↔ text |
| `concerns` | question → concept |
| `derived_from` | text → source text |
| `investigates` | research → concept |
| `discusses` | person → text |

## All edges

| from | relation | to |
|---|---|---|
| laozi | `associated_with` | daodejing |
| shouyi | `associated_with` | qi |
| zhuang-zhou | `associated_with` | zhuangzi |
| zuowang | `associated_with` | qi |
| jingzuo | `concerns` | zuowang-vs-jingzuo |
| qi | `concerns` | qi-belief-necessary |
| zuowang | `concerns` | zuowang-safety-without-teacher |
| zuowang-lun | `derived_from` | neiguan-jing |
| zuowang-lun | `derived_from` | qingjing-jing |
| daodejing | `described_in` | guodian-daodejing |
| jingzuo | `described_in` | cheng-men-li-xue |
| jingzuo | `described_in` | zhuzi-yulei-jingzuo |
| laozi | `described_in` | shiji-biographies |
| qi | `described_in` | daodejing |
| qi | `described_in` | zhuangzi |
| shouyi | `described_in` | baopuzi-shouyi |
| shouyi | `described_in` | daodejing |
| sima-chengzhen | `described_in` | zuowang-lun-composition |
| taiping-jing | `described_in` | taiping-jing-shouyi |
| wuwei | `described_in` | daodejing |
| xinzhai | `described_in` | zhuangzi |
| zuowang | `described_in` | reading-order |
| zuowang | `described_in` | sitting-protocol |
| zuowang | `described_in` | zhuangzi |
| zuowang | `described_in` | zuowang-lun |
| sima-chengzhen | `discusses` | zuowang-lun |
| jingzuo | `investigates` | mindfulness-meta-analysis-2014 |
| jingzuo | `related_to` | shouyi |
| jingzuo | `related_to` | xinzhai |
| jingzuo | `related_to` | zuowang |
| neiguan-jing | `related_to` | qingjing-jing |
| shouyi | `related_to` | neiguan-jing |
| shouyi | `related_to` | wuwei |
| shouyi | `related_to` | zuowang |
| wuwei | `related_to` | zuowang |
| xinzhai | `related_to` | qingjing-jing |
| zuowang | `related_to` | mindfulness |
| zuowang | `related_to` | wuwei |
| zuowang | `related_to` | xinzhai |
| qingjing-jing | `translated_as` | qingjing-jing-opening |
| shouyi | `translated_as` | daodejing-10-shouyi |
| wuwei | `translated_as` | daodejing-48 |
| xinzhai | `translated_as` | xinzhai-passage |
| zuowang | `translated_as` | zuowang-passage |
