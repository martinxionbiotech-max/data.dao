# Concepts

Structured concept records from `data/concepts.json` — 6 records.

| id | name | 中文 | tradition | evidence | related |
|---|---|---|---|---|---|
| zuowang | Zuowang | 坐忘 | Daoist | PRIMARY SOURCE | zhuangzi, xinzhai, wuwei, qi, jingzuo |
| xinzhai | Xinzhai | 心斋 | Daoist | PRIMARY SOURCE | zhuangzi, zuowang, qi, wuwei |
| wuwei | Wuwei | 无为 | Daoist | PRIMARY SOURCE | daodejing, zuowang, xinzhai, qi |
| jingzuo | Jingzuo | 静坐 | Neo-Confucian | PRIMARY SOURCE | zuowang, shouyi, xinzhai |
| shouyi | Shouyi | 守一 | Daoist | PRIMARY SOURCE | daodejing, wuwei, qi, zuowang, jingzuo |
| xu | 虚 emptiness | the working state: mind emptied, Dao gathers; xinzhai=its fasting |
| qi | Qi | 气 | Pan-Chinese | PRIMARY SOURCE | zhuangzi, daodejing, xinzhai, zuowang, shouyi, wuwei |

## Schema

```json
{ "id": "zuowang", "name": "Zuowang", "chinese": "坐忘",
  "pinyin": "zuòwàng", "tradition": "Daoist",
  "page": "/concepts/zuowang/", "evidence": "PRIMARY SOURCE",
  "related": ["zhuangzi", "xinzhai"] }
```

Each concept has a full authored page on the main site at `page`.
| ziran | so-of-itself; the Dao models on it (DDJ 25) |
