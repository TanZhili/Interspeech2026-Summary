# Can Large Language Models Reliably Correct Errors in Low-Resource ASR? A Contamination-Aware Case Study on West Frisian

- 论文编号：1659
- 报告人：Yun Hao
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hao26b_interspeech.pdf

## 问题

低资源 ASR 仍弱；LLM 生成式纠错（GER）在高资源语上有效，但低资源语覆盖不足，且公开评测可能污染导致虚高。需污染可控地检验是否真能纠错。

## 方法

以 XLS-R 为弗里斯兰 ASR；在 Common Voice 与新建非公开文本的 Offline 集（故事书+原创句，4 男声，1.5 h）上做 GER。比较生成式纠错与从 5-best 选择；模型含 Qwen3（±LoRA）、GPT-4o-mini、GPT-5.1；零样本到少样本。并做句级改进/退化统计与编辑级精度召回。

## 实验与结果

CV：基线 WER 13.5，oracle 9.6；GPT-5.1 生成式最低 8.9（超 oracle），选择式仅约 12.1。Offline：基线 21.1，GPT-5.1 最低 13.8（亦超 oracle 18.0），与公开集趋势一致，支持非污染解释。Qwen3 几乎不改。生成式比选择式更强；GPT-5.1 句级改进多但也可能退化；插入纠错召回高、精度偏低，删除相反。

## 结论

作者认为强 LLM 的 GER 在低资源弗里斯兰上有效且可超 N-best oracle；非公开集上的相近增益表明并非仅靠污染。开源小模型收益有限，效果高度依赖模型语言覆盖。

## 点评

用非公开文本听写集专门压污染假说，方法学贡献突出。生成式可跳出 N-best 是关键优势。强依赖闭源 GPT；开源侧几乎无效，部署可复现性受限。纠错会引入新插入错误，实际需配合置信度或过滤。
