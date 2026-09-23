# Alignment-Aware Continued Pre-training for Multilingual Speech Representation Learning

- 论文编号：1185
- 报告人：Xuyang Wang
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lu26b_interspeech.pdf

## 问题
多语 SSL 基座常直接监督微调做 ASR，声学–符号对齐全压到微调阶段；异质文字与长尾语种下跨语泛化受限。

## 方法
在 MMS 300M 上插入对齐感知继续预训练：联合 SSL（对比+多样性）与 CTC，并对上下文/量化表示做随机替换使 CTC 梯度可进量化路径。比较建模单元 Char / IPA / Uroman；提出语言感知双码本（全局+语种特异，加性融合）缓解离散空间竞争。其后仍 CTC 微调。

## 实验与结果
FLEURS：Direct FT 47.2 WER → Continual SSL 43.4 → Joint(Uroman) 36.6；双码本再降至 35.5。Uroman 优于 Char 的 WER，Char CER 略优；IPA 因 G2P 覆盖/噪声在跨语上更差。MLS→FLEURS 未见语上 Uroman 更稳。

## 结论
对齐感知联合 SSL–CTC 继续预训练显著优于直接微调或纯 SSL 继续预训练；统一罗马化与双码本有助跨文书共享与长尾公平。

## 点评
把“符号对齐”前移到表示塑造阶段，比只换微调配方更治本。Uroman 实用折中 IPA 的资源依赖；双码本设计贴合长尾竞争，但语种码本规模与维护成本在更大规模上仍待验证。
