# GitHub 书源二次深挖报告（2026-11-15）

## 扫描范围与方法

- 仓库：`dujiu1024-dotcom/shudan`
- 书目范围：读取当前 `catalog/booklist.csv`，严格限定 BK001–BK205；不纳入《传习录》《毛泽东选集》。
- 对照：`sources/github-search-round-001.md` 至 `-004.md`、`notes/index.md`、`excerpts/index.md`、`metadata/index.md`；检查现有已入库状态，避免把既有全文或已登记材料重复计数。
- 方法：针对此前未检索、结果稀疏或版本信息缺失的条目，使用书名、作者、别名和文件名组合进行 GitHub 精确检索；对候选文件调用 GitHub 文件读取，确认文件可访问、内容类型与书目对应关系。
- 本轮属于针对遗漏/低覆盖条目的深挖，不将其表述为重新逐条穷尽 205 本所有可能拼写和 ISBN 的全量搜索。

## 新增完整全文

**0 本。**

本轮没有发现同时满足“全文完整、版本匹配、许可明确允许再分发”的新文件。未将第三方电子书仓库、无许可说明的 PDF 或分析报告复制进 `books/`。

## 新增读书笔记

| ID | 书名 | 新发现内容 | 来源 |
|---|---|---|---|
| BK044 | The Elements of Style | Strunk Jr. 与 E. B. White 版本的分章节读书笔记；来源明确称为第四版相关笔记。注意这与仓库现有早期 Strunk 单作者公版文本不是同一版本 | https://github.com/mgp/book-notes/blob/2f9287690310dd9801fec6105acaf274d76b6678/elements-of-style.markdown |
| BK130 | Getting to Yes: Negotiating Agreement Without Giving In | Roger Fisher、William Ury 分章节读书笔记，含谈判原则与章节要点 | https://github.com/mgp/book-notes/blob/2f9287690310dd9801fec6105acaf274d76b6678/getting-to-yes-negotiating-agreement-without-giving-in.markdown |
| BK131 | Never Split the Difference | Chris Voss 分章节读书笔记 | https://github.com/mgp/book-notes/blob/2f9287690310dd9801fec6105acaf274d76b6678/never-split-the-difference.markdown |
| BK195 | The Mythical Man-Month | Frederick P. Brooks Jr. 分章节读书笔记，含页码标记 | https://github.com/mgp/book-notes/blob/2f9287690310dd9801fec6105acaf274d76b6678/the-mythical-man-month.markdown |

以上均为笔记，不是原书全文；只登记索引，不复制第三方笔记正文。

## 新增书目元数据线索

| ID | 书名 | 新发现信息 | 核验状态 |
|---|---|---|---|
| BK020 | La Distinction: Critique sociale du jugement | 法文版 1979；英译本由 Richard Nice 翻译，Harvard University Press 1984；ISBN 0-674-21277-0 | 来自 GitHub 深度分析报告，属于二手书目线索；需出版社/图书馆目录复核 |
| BK034 | Amusing Ourselves to Death | Neil Postman；Penguin 2005 版；250 页；ISBN 9780143036531 | 已读取 GitHub 书籍条目元数据；这是后续版线索，不可误作 1985 初版 |

## 其他检索结果的排除说明

- BK017《Essai sur le don》：命中 Marcel Mauss 的人物介绍、句子数据集及理论笔记，未发现可确认的原书全文或可独立归档的新增书评/读书笔记。
- BK021《Emotional Contagion》：命中概念条目和书目引用，非原书全文。
- BK020《La Distinction》：除元数据报告外，其他命中多为无关法语内容；未发现可确认授权全文。
- BK028、BK029：命中教材/人物/实验介绍与书目资料，未确认与书目版本匹配的全文。
- BK031《Understanding Media》、BK034《Amusing Ourselves to Death》、BK038《The Hero with a Thousand Faces》、BK041《Морфология сказки》、BK048《Reality in Advertising》、BK049《How Brands Grow》：命中内容主要是人物资料、二手分析、方法卡或理论介绍；不计为新增原书全文。BK034 的既有笔记不重复登记。
- BK130、BK131、BK195：确认了可访问的分章节笔记文件，已纳入 notes 索引。
- 本轮其余候选命中没有足够证据证明是目标书籍全文、匹配版本或许可允许再分发，均不下载。

## 本轮计数

- 扫描范围：原始 205 本中的未检索/低覆盖条目深挖；不是 205 本全部关键词组合的穷尽式重跑。
- 新增合法完整全文：**0**
- 新增读书笔记：**4**
- 新增摘录/章节材料：**0**
- 新增元数据线索：**2**
- 新增待核实的未授权全文来源：**0**
- 版本/许可待核实：BK020 元数据需权威目录复核；BK034 需确认用户书单所指版次。

## 仓库变更

- 更新：`notes/index.md`
- 更新：`metadata/index.md`
- 更新：`README.md`
- 新增：本报告
- `books/` 未新增文件；本轮没有满足入库门槛的全文。

所有登记均使用 catalog 中的书目 ID；未改变原始 205 本范围。
