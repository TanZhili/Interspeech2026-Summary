# Two-stage semi-supervised learning with pseudo-labels: A case study on Northern Sámi ASR

- 论文编号：2497
- 报告人：Priyanshi Pal
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pal26_interspeech.pdf

## 问题
北萨米语标注稀缺；同量监督下小模型弱于大模型。如何用伪标签半监督让轻量 wav2vec2 学生逼近大教师，且兼顾域外泛化。

## 方法
约 75h 未标注议会语音；20h 人工转写监督。教师/学生为 wav2vec2-large/base-sami-22k（22.4k 小时萨米预训练）。伪标签：全量教师输出，或师生 WER<10% 一致过滤得约 28h。策略含 PL-Full、PL-Filtered、等量 capped，及人工+伪标签混合 vs 两阶段微调（先 PL 后 HL 或相反）。单轮伪标签、不用 LM。评议会验证、282utt、YLE 播客、UIT-SME。

## 实验与结果
PL-Full 优于过滤；等量 capped 无增益。混合训练劣于基线；两阶段且先全量伪标签再人工最好（如 282utt CER 6.73 vs 基线 10.09；播客 CER 8.89 vs 11.40）。相对 CER 改进约 3.8–33.3%（摘要）。过滤偏删、全量偏插；伪标签强化常见字符、稀有/借词字符仍弱。

## 结论
单轮伪标签即可提升小模型；顺序关键，宜先伪标签再金标；过滤牺牲多样性未必更好。

## 点评
把“伪标签怎么喂、喂多少、喂顺序”在濒危语上跑清楚，实用。强在域外播客与错误类型分析；弱在未试迭代 PL/增广，且教师系统错误会灌给学生。
