# Enhancing EMG-to-Speech via Silent-Voiced Representation Alignment

- 论文编号：2931
- 报告人：Jiwon Lee
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/lee26v_interspeech.pdf

## 问题
Silent EMG 无对齐声学监督且数据远少于 voiced；现有 target-transfer 只搬声学目标，忽略平行 silent–voiced EMG 的表征一致性；ETS 结果跨随机种子波动大却少被报告。

## 方法
提出 Silent-Voiced Alignment（SVA）损失：对平行对在输出层（声学表征 + 音素分布，DTW）与各 Transformer 隐层（复用输出对齐路径，余弦距离）对齐 silent 与 voiced 编码器表示；soft scheduling ω=σ(τ−Lout_SVA)。总损失在 silent 上为 α(声学+音素)+SVA。两阶段：先仅 voiced 预训练，再 voiced+silent 微调。可插到 Gaddy（mel）与 SU-ETS（HuBERT-Soft）管线。

## 实验与结果
Gaddy & Klein：1289 平行对 + 5477 非平行 voiced；98 测试句。10 种子协议：Ours(Mel) CER/WER 12.88%/25.14% vs Gaddy 14.16%/26.75%（相对 WER −6.0%，p=0.002）；Ours(SU) WER 26.55% vs 27.78%（p=0.009）。Mel 设定 FSD 显著更好。消融：输出+隐层全 SVA 最优；仅隐层弱于仅输出。

## 结论
显式 silent–voiced 表征对齐可稳定提升不同声学目标下的 ETS 可懂度，且易集成；多种子报告暴露了该领域以往均值不可靠的问题。

## 点评
把平行 EMG 当「中间教师」而非只对声学目标 DTW，监督更近、更稳。增益幅度不大但统计显著且方差更小，对小数据噪声模态很有说服力；协议本身可能比百分点更有长期价值。
