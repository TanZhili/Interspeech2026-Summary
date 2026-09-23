# Joint Fullband-Subband Modeling for High-Resolution SingFake Detection

- 论文编号：1614
- 报告人：Chia-Yu Hu
- 程序：Tuesday 29 September 2026 / Spoofing, Deepfake Detection and Watermarking
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/hu26e_interspeech.pdf

## 问题
歌声合成（SingFake/SVDD）比语音含更丰富谐波与气息等高频细节；多数检测沿用 16 kHz（Nyquist 8 kHz），丢弃 8–22.05 kHz 线索。简单子带融合又常打不过专职全带专家，且伪影在频谱上非均匀分布。

## 方法
Sing-HiResNet：以 44.1 kHz log-power 频谱为输入。Phase 1：全带 ResNet18 专家 + 将 Nyquist 带均分为 N∈{1,2,4,8} 的子带专家，各产 32 维嵌入与 logit。Phase 2 四种融合——决策级平均、特征拼接+MLP、多头自注意力跨专家交互、跨专家蒸馏——系统比较全带全局与子带局部如何协同。

## 实验与结果
WildSVDD（约 97 歌手、3223 曲；训练 27879 句，深伪/真实约 15364/12515）；Test A 未见歌手同语言，Test B 未见波斯语歌手。摘要称显著优于 16 kHz 模型并在 WildSVDD 上达 SOTA，强调高频子带提供互补线索。全文在实验设置段截断，具体 EER/AUC 表未能读到。

## 结论
作者主张高分辨率全带–子带联合建模对野外歌声鉴伪关键；精确数字需回查 PDF。

## 点评
把「采样率天花板」与「子带伪影非均匀」同时问题化，融合策略对比设计清楚。强在相对 SSL-16kHz 路线的物理动机；脆弱点在重采数据带来分布偏移，以及 N 划分固定均匀未必最优。抽取截断已在结果中标明。
