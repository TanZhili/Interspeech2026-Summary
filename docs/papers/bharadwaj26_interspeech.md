# An Empirical Recipe for Universal Phone Recognition

- 论文编号：1462
- 报告人：Shikhar Bharadwaj
- 程序：Tuesday 29 September 2026 / Low-Resource & Endangered Language Speech Processing
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bharadwaj26_interspeech.pdf

## 问题
英语音素识别模型跨语泛化差；多语音素识别又常未充分利用 SSL，且不清楚数据规模、架构与损失各自贡献。

## 方法
在统一 PRiSM 评测下做受控消融，确定配方：以 XEUS（大规模多语 SSL）为骨干，用 Self-Conditioned CTC 在 IPAPack++（约 17k 小时）上微调，得到 PhoneticXEUS。对比 Vanilla/Inter/Self/Hierarchical CTC 与 CTC-Attention；对比从零训练的 E-Branchformer 与 MMS/XEUS；并缩放多语训练句数（固定英语约 850k，多语 150k→600k）。进一步按语系、口音与发音特征分析错误。

## 实验与结果
PhoneticXEUS：口音英语平均 PFER 10.6，多语平均 17.7，均为表中 SOTA。SelfCTC 多语 17.7，优于 InterCTC 18.5 与 Vanilla 18.8；XEUS+SelfCTC 相对从零训练约改善英语 2.0、多语 5.4 点。增加多语数据改善多语表现且不伤英语。SSL 在 PR-vox 的 21 语系中 19 系更好；在 PR-saa 的 192 口音中 187 个更好。时域性强的特征（如 tenseness、delayed release）相对收益最小。

## 结论
SSL 初始化 + SelfCTC + 大规模多语 G2P 数据构成有效通用音素识别配方；SSL 利于跨语迁移与口音稳健，但部分发音特征与低质评测集仍是瓶颈。

## 点评
用同一评测协议把损失、骨干与数据规模拆开，给出可复现配方，比单点刷榜更有建设性。强在开源代码数据与错误剖面；弱在训练标签主要来自 G2P（偏典范音），对儿童/短音节等声学偏移仍脆弱，作者亦承认评测标注噪声。
