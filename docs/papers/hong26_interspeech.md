# Convolutional Dynamic Rotary Positional Encoding

- 论文编号：1312
- 报告人：Euijin Hong
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hong26_interspeech.pdf

## 问题
RoPE/RelPos 等位置编码依赖均匀离散时间索引，与语音特征连续、信息密度不均的特性错位；纯 RoPE 在 ASR 训练中还可能发散。Branchformer 的注意力支路缺少中间卷积，局部时序建模不足。

## 方法
提出 **CD-RoPE**：用轻量 depthwise-separable 1D 卷积从输入特征预测连续时间偏移 \(\Delta t\in[-1,1]\)（tanh + ReZero 式可学习 \(\alpha\)），加到基索引后再乘逆频率，得到 \(\hat{\Theta}_{t,i}=(t+\Delta t)\cdot\theta_i\)。在全维特征上算偏移再分头，保留 RoPE 谐波结构；故意调制时间索引而非直接调频率，以避免早期训练不稳定。嵌入 Branchformer 注意力支路。

## 实验与结果
SpeechBrain 上从零训练 Branchformer（18 编码器 + 6 解码器），LibriSpeech 960h；对比 RelPos（109.8M）与 CD-RoPE（107.6M）。
- WER：dev-clean 2.02→1.96；test-clean 2.17→2.13；test-other 5.07→4.95；少 2.2M 参数。
- McNemar 在 test-other 上显著（p≈0.043）。
- Speech Robust Bench：中等强度下 9 类扰动中 7 类更好，时序扰动优势最大（如 severity 4 的 tempo↑：10.73→8.63）。
- 核大小在 100h 子集上对 WER 不敏感（k=7/9/11 约为 5.44–5.47）。

## 结论
CD-RoPE 在 Branchformer 上全面优于 RelPos 且参数更少；鲁棒性增益主要落在时序扰动上，支持“时间轴弯曲”假设。作者刻意只评 Branchformer，向 Conformer 等带卷积结构迁移留作未来工作。

## 点评
把动态性放在“时间索引”而非旋转频率上，是兼顾稳定性与相对归纳偏置的合理设计；对 Branchformer 尤其对口，因为注意力支路本来缺局部卷积。增益幅度不大，且单数据集单 seed、无组件消融，推广性仍需更多证据。
