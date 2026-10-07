# Sources Registry

Structured source records from `data/sources.json` — 21 sources
(primary texts: 10, scholarship: 9, research: 2).

| id | title | type | lang | url |
|---|---|---|---|---|
| zhuangzi | Zhuangzi (received text, Guo Xiang recension) | primary_text | zh | https://ctext.org/zhuangzi |
| daodejing | Daodejing (received Wang Bi text, 81 chapters) | primary_text | zh | https://ctext.org/dao-de-jing |
| zuowang-lun | Sima Chengzhen, Zuowang lun (Treatise on Sitting in Oblivion) | primary_text | zh | — |
| taiping-jing | Taiping Jing (Scripture of Great Peace) | primary_text | zh | — |
| zhuzi-yulei | Zhu Xi yulei (Classified Conversations of Master Zhu), juan 116 | primary_text | zh | — |
| er-cheng-waishu | Er Cheng waishu (Outer Collection of the Two Chengs), juan 12 | primary_text | zh | — |
| kohn-2010 | Kohn, Livia. Sitting in Oblivion: The Heart of Daoist Meditation. Three Pines Press, 2010 | scholarship | en | yes |
| slingerland-2003 | Slingerland, Edward. Effortless Action: Wu-wei as Conceptual Metaphor and Spiritual Ideal in Early China. Oxford University Press, 2003 | scholarship | en | — |
| robinet-1993 | Robinet, Isabelle. Taoist Meditation: The Mao-shan Tradition of Great Purity. SUNY Press, 1993 | scholarship | en | — |
| taylor-1988 | Taylor, Rodney L. The Confucian Way of Contemplation: Okada Takehiko and the Tradition of Quiet-Sitting. University of South Carolina Press, 1988 | scholarship | en | — |
| watson-1968 | Watson, Burton, trans. The Complete Works of Chuang Tzu. Columbia University Press, 1968 | scholarship | en | — |
| iep-zhuangzi | Internet Encyclopedia of Philosophy, 'Zhuangzi' | scholarship | en | https://iep.utm.edu/zhuangzi-chuang-tzu-chinese-philosopher |
| henricks-1989 | Henricks, Robert G., trans. Lao-Tzu Te-Tao Ching (Mawangdui text). Ballantine, 1989 | scholarship | en | — |
| cook-2012 | Cook, Scott. The Bamboo Texts of Guodian. Cornell East Asia Series, 2012 | scholarship | en | — |
| qingjing-jing | Qingjing Jing (Scripture of Constant Clarity and Stillness) | primary_text | zh | http://www.taoist.org.cn/showInfoContent.do?id=2549 |
| neiguan-jing | Neiguan Jing (Scripture of Inner Observation), Daozang; Yunji Qiqian juan 17 | primary_text | zh | yes |
| shiji-63 | Shiji (Records of the Grand Historian), ch. 63, 'Laozi Han Fei liezhuan' | primary_text | zh | yes |
| goyal-2014 | Goyal, M., et al. Meditation Programs for Psychological Stress and Well-being. JAMA Internal Medicine 174(3):357-368, 2014 | research | en | https://pubmed.ncbi.nlm.nih.gov/24395196 |
| kohn-1998 | Kohn, Livia. God of the Dao: Lord Lao in History and Myth. Center for Chinese Studies, University of Michigan, 1998 | scholarship | en | — |
| song-shi-yangshi | Song shi, 'Yang Shi zhuan' (ch. 428), Cheng Men Li Xue episode | primary_text | zh | yes |
| guodian-report | Jingmen City Museum, 'Jingmen Guodian yihao Chumu', Wenwu 1997.7 (Guodian tomb no. 1 excavation report) | research | zh | — |

## Types

- `primary_text` — classical text or original document
- `scholarship` — published academic work
- `research` — published scientific study or report
- `community` — practitioner community material

## Schema

```json
{ "id": "zhuangzi", "title": "Zhuangzi (received text)",
  "type": "primary_text", "language": "zh",
  "url": "https://ctext.org/zhuangzi",
  "pages_used_in": ["/concepts/zuowang/"] }
```

Every content page lists its sources; `pages_used_in` is the reverse index.
