# SEA-MDD: Self-adapting Mispronunciation Detection and Diagnosis Models via Test-Time Training

- 论文编号：856
- 报告人：Minglin Wu
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wu26c_interspeech.pdf

## 问题
L2 发音检测与诊断（MDD）面对学习者水平与错误类型多样，固定训练集难覆盖分布外样本；大规模标注昂贵。已有 MAML 适应仍需目标说话人较多标注数据，形成二次数据稀缺。

## 方法
SEA-MDD：在 wav2vec 2.0 Transformer 块的自注意力与 FFN 之间插入 TTT 模块（默认两层 MLP + LN + 残差 + tanh 门控；另有 Linear 变体）。内外环：内环在训练与测试时对每个输入用自监督重构更新 MLP 权重 W（θ_K x 输入、θ_V x 目标，也可时间维 mini-batch b=32）；外环用 CTC 微调其余参数。测试时仅做内环、单句适应。

## 实验与结果
CU-CHLOE（34.6 h，粤/普通话学习者）。相对 wav2vec2-CTC 与需约 2 h 适应数据的 wav2vec2-MAML：SEA-MDD-MLP（全块）PER 8.03%、F1 81.54%、DIAA 94.06 等全面更优。适应成本：1 句、延迟约 5–52 ms、参数约 3.0–35.5M，远低于 MAML（94.4M、约 30 min、2 h 数据）。浅层插入效果更好；MLP 略优于 Linear；全块略优于仅第 1 块。

## 结论
单句级 Test-Time Training 可在无额外标注下自适应当前发音样本，兼顾 MDD 精度与实时效率，为 L2 数据稀缺提供新适应范式。

## 点评
把长上下文 TTT 思路迁到 MDD，用“测试时自监督更新局部 MLP”换掉“再采目标人数据”，对课堂实时反馈很贴切。浅层更有效符合底层声学变异更大的直觉。局限是仅 CU-CHLOE 一种 L1 背景；内环学习率与插入层需调；相对 MAML 的评测设置对其更苛刻（MAML 用测试集一部分适应）。
