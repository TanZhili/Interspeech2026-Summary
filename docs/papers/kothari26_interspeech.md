# Multilingual Multi-Speaker Unit Vocoders: A Systematic Analysis of Discrete Speech Representations

- 论文编号：3330
- 报告人：Naman Kothari
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/kothari26_interspeech.pdf

## 问题
SSL+k-means 离散单元纠缠音素、说话人与语言信息，多语多说话人生成易出现说话人混叠与跨语干扰；单元声码器常被当作附属模块，簇大小与条件策略缺乏系统分析。

## 方法
以 BigVGAN 为骨干，输入改为离散单元 embedding；可选拼接 ECAPA-TDNN 说话人嵌入与语言嵌入，并加基于 mel 的辅助 LID（真实与生成 mel 的 CE，λ=1）。单元来自 Data2Vec-AQC 第 21 层，在 22 种印度语 1200h 上训 k-means（500/1k/2k/5k/10k）；声码器在孟加拉语、印地语、泰米尔语、泰卢固语四语 IndicVoices-R 上训练（约 71–134h/语）。对比：仅单元、+说话人、+语言+LID、说话人+语言+LID。

## 实验与结果
未见说话人测试：簇越大 WER 越低（如孟加拉语仅单元 500→10k：60.42→25.13）。无说话人条件时 SIM 约 0.16–0.21 且句内音色混乱；加 ECAPA 后 SIM 升约 4–5×（10k 时约 0.67–0.77）。语言条件在小簇上降 WER 更明显，大簇增益减弱甚至略伤（如印地 10k：说话人 23.99 vs 联合 24.84）。音素纯度/PNMI 随簇增大上升，簇纯度下降；500 簇时跨语同音素常共享簇 ID，10k 时趋于分语分离。

## 结论
簇大小主要通过音素可分性决定可懂度；显式说话人条件对防身份崩塌必不可少；语言监督主要在小簇、单元歧义大时有用。

## 点评
把声码器从流水线里拆出来做受控消融，结论可直接指导 Audio LLM/S2ST 的单元库存与条件设计。跨语共享表把“小库存混语、大库存分语”说清楚了。脆弱处是评测语仅四种、UTMOSv2 无趋势可报，且大簇带来更长离散序列与建模成本，正文未讨论下游 LM 负担。
