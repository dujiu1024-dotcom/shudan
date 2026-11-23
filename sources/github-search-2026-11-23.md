# GitHub 书源周度扫描报告（2026-11-23）

## 范围与方法
- 仓库：`dujiu1024-dotcom/shudan`。
- 书目范围：原始 `catalog/booklist.csv` 的 BK001–BK205，共205个 ID；排除《传习录》《毛泽东选集》，不扩展书目。
- 扫描前读取 `catalog/booklist.csv`、全部现有 `sources/` 检索报告、`notes/index.md`、`excerpts/index.md`、`metadata/index.md`、`books/` 目录，并检查三个历史 GitHub 命中索引，避免重复登记。
- 对205个书目逐项执行 GitHub 精确书名检索，尽可能附作者；其中24条因目录行解析异常先出现空标题，随后按原始 CSV 行重新查询，完成205个有效书名查询。另对已获得 ISBN 的条目及重点候选补充12次 ISBN/作者/PDF/EPUB/MOBI 查询。
- 对候选逐一读取 GitHub 文件，核对内容类型、路径、commit、版本字段和仓库根目录许可文件；二进制 PDF 仅核对 GitHub API 文件元数据，不将未读取二进制的文件认定为完整全文。

## 本轮结果

| 类别 | 新增/补充 | 说明 |
|---|---:|---|
| 可确认合法再分发的完整全文 | **0** | 没有文件同时满足完整性、版本匹配和明确再分发授权；`books/` 未改动 |
| 新增/补充读书笔记来源 | **7条** | BK043、BK058、BK061、BK094、BK100、BK199、BK201；其中BK043、BK199、BK201为既有书目补充独立来源 |
| 既有笔记的新增独立来源 | **1** | BK199《Give and Take》增加 rwieruch 的独立读书总结；原有 Ibrahim0814 来源保留 |
| 新增摘录/方法蒸馏来源 | **3** | BK037、BK043、BK101；均不是原书全文 |
| 新增书目元数据记录 | **12个书目ID** | BK024、BK043、BK076、BK090、BK094、BK096、BK111、BK112、BK116、BK124、BK143、BK189 |
| 既有元数据补充 | **1** | BK191 增加作者官方简体中文版信息；BK128 已有元数据，不重复计数 |

### 新增笔记与方法材料
- BK043《金字塔原理》：新增 wenfujie/document-library 笔记，含二手评论引文及金字塔/MECE要点；不是原书，仓库根目录未见 LICENSE。
- BK058 *The Science of Storytelling*：新增 aneurokumar 阅读笔记，只有两条核心想法；仓库 MIT License。
- BK061 *Film Directing Shot by Shot*：新增 camera-blocking 深读原理笔记，覆盖镜头关系、景别、180°轴线、场面调度；仓库根目录未见 LICENSE。
- BK094《丰田生产方式》：新增微信读书导入笔记，显示大野耐一、中信出版集团、2024-04-01、ISBN 9787521764192，记录373条高亮/笔记；仓库根目录未见 LICENSE。
- BK100《设计调研》：新增读书笔记与全书目录结构；仓库根目录未见 LICENSE。
- BK201 *The Go-Giver*：新增约1KB内容简介与五大成功法则摘要；仓库根目录未见 LICENSE。
- BK199 *Give and Take*：增加 rwieruch 的独立读书总结；仓库根目录未见 LICENSE。BK169《一本书读懂财报》本轮再次核对，但其笔记已在现有索引中，不重复登记。
- BK037 *Story*：新增 RAEA 的 McKee 叙事结构方法卡；仓库使用 FSL-1.1-ALv2，内容为方法蒸馏而非原书。
- BK101 *Competing Against Luck*：新增 Wondelai JTBD Skill；文件声明 MIT，属于方法框架，不是逐章读书笔记或原书。

### 新发现的待核实版权来源（均未下载、未复制）

1. **BK016 — Exchange and Power in Social Life**：`DeSociologue/Sociology-of-Emotions-Reading-List` 的 `21 emotions in exchange theory/Exchange and Power in Social Life.pdf` 在 commit `9a08660cca83e6fce5cbfd7ba315f176f9f8336b` 确实存在，GitHub API 返回大小 21,517,095 bytes、blob `f84267d180e2a9ef36913d41d6db904a45dd9174`。README 书目行写作“Balu, P.”、Wiley、1964，作者拼写与通行书目不一致；PDF 二进制未读取，内容完整性和版本未验证。仓库根目录未见 LICENSE/COPYING，版权及再分发许可不明。
2. **BK024 — The Presentation of Self in Everyday Life**：`aarnphm/aarnphm.github.io` commit `bf260f41e04113eef55bd80ad4331ce5054bdfc8` 的 `content/library/The Presentation of Self in Everyday Life.md` 存在，记录作者 Erving Goffman、年份1956，并链接 Monoskop PDF。该仓库有 Apache-2.0 LICENSE，但仅为仓库许可，不能推定外链 PDF 获得授权；外链访问、PDF完整性和再分发权均未验证。与既有书目引用的1959年存在年份/版本冲突。
3. **BK111 — 营销的本质**：`jbiaojerry/ebook-treasure-chest` commit `93cf3ffcf5a2e6814644d1747a101272557d7eac` 的 `md/营销.md` 列出包政著普通版及珍藏版 CTFile 链接。页面明确声明版权归作者/权利人，下载链接仅供宽带测试并要求24小时删除；这不是授权，未下载。
4. **BK124 — 阿里铁军销售课**：同仓库同 commit 的 `md/创业.md` 列出李立恒著作及 CTFile 链接；适用同一版权声明，无再分发授权，未下载。
5. **BK128 — 增长黑客：如何低成本实现爆发式成长**：同仓库 `md/营销.md` 列出 Sean Ellis 的 CTFile 链接。该书元数据已在旧索引登记，本轮只补充下载线索和版权状态，不重复登记元数据；未下载。
6. **BK143 — 合同法研究**：`p0dsphbe/processorc` commit `af24ff84a2baa9d67ada89bbcf59e76ee9720cb2` 中读取到两份下载聚合 HTML：第一卷第三版（2015，中国人民大学出版社，746页，ISBN 9787300216478，blob `4b5231017b514ace4358837e390ea93c16662bc3`）及第三卷第二版（2015，789页，ISBN 9787300131825，blob `4391170bc5cae22efb56dd71e69b1bcae5855a64`）。它们不是 PDF 文件，只指向外部下载页；仓库根目录未见 LICENSE，版权状态不明。

### 元数据补充与待消歧
- BK024：1956 与 1959 年份线索冲突；需以具体版次版权页核对。
- BK043：确认作者 Barbara Minto；出版社、年份、版次、ISBN仍待权威目录核对。
- BK076：Joshua D. Angrist、Jörn-Steffen Pischke；Princeton University Press，2008。
- BK090：William Albert、Thomas Tullis；Newnes，2013。
- BK094：大野耐一；中信出版集团，2024-04-01；ISBN 9787521764192（来自阅读导入记录，非版权页）。
- BK096：Rob Fitzpatrick；条目标注2013-09-10；ISBN 1492180742。
- BK111：包政；版本、出版社、年份、ISBN未核。
- BK112：Geary A. Rummler、Alan P. Brache；第3版；Jossey-Bass，2013。
- BK116：同名候选冲突：Edward F. McQuarrie / SAGE / 2006 / 228页；另有 Jie Xu / iUniverse / 2005 / 204页。原始书目未给作者，暂不判定哪个版本匹配。
- BK124：李立恒；版本、出版社、年份、ISBN未核。
- BK143：第一卷第三版与第三卷第二版的书目字段见上，不能据此确定原始书单意图的卷次。
- BK189：W. Timothy Coombs；第6版；SAGE Publications，2021；ISBN 9781071816646。
- BK191：作者官方翻译页补充简体中文版《机器学习系统设计》，中国电力出版社，2024-04-30，ISBN 9787519886288。

## 许可与排除说明
- 本轮没有复制任何受版权保护的全文，也没有把网盘索引、书目页、阅读笔记、方法卡或单条摘录计为全文。
- `DeSociologue`、`jbiaojerry`、`p0dsphbe` 等版权来源仓库未见根目录 LICENSE；`aarnphm` 的 Apache-2.0 不涵盖外链 Monoskop PDF。
- `jbiaojerry` 的页面本身明确声明版权归权利人，链接仅供测试；不构成授权。
- `shinyobjectz/raea` 声明 FSL-1.1-ALv2；`wondelai/skills` 声明 MIT；`aneurokumar/website` 为 MIT。上述许可证仅说明对应仓库文件许可，不改变所引用书籍的版权状态。
- `digoal/blog` 使用 GPL-2.0，但 BK169 笔记已登记，本轮不重复新增。
- `books/` 中已有文件未改动；没有新下载文件。

## 本轮仓库改动
- 更新 `catalog/booklist.csv`、`notes/index.md`、`excerpts/index.md`、`metadata/index.md`。
- 更新历史汇总索引 `catalog/github-reading-notes.md`、`catalog/github-excerpts.md`、`catalog/github-book-metadata.md`。
- 更新 `README.md` 进度。
- 新增本报告。

本轮覆盖原始205个书目 ID；对无有效命中或版本不明的书目不作“GitHub不存在”结论。下周继续使用作者、ISBN、译者、版次和扩展名组合补漏。