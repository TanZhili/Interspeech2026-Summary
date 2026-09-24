# Spectro-Temporal Interference Confounds Phase Encoding in Spatial Audio Foundation Models

- 论文编号：2873
- 报告人：Yuxuan Chen
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/chen26da_interspeech.pdf

## 问题
空间自监督音频模型在定位等宏观任务上表现好，但未必真正编码微秒级耳间相位（IPD）；下游成功可能来自捷径，现有几何/房间声学基准无法检验这一点。

## 方法
提出基于 binaural masking level difference（BMLD）的心理声学表征基准：在冻结模型嵌入上用特征距离比 ΔBMLD 度量 SπN0 相对 S0N0 的空间释掩。对照 Durlach EC 解析基线与 GCC-PHAT 正对照；评估双耳 SSL（WavJEPA、GRAM-T、Spatial-AST、DSpAST）、单耳负对照（HuBERT-L/WavLM-L/Wav2Vec2-L、DAC）与编解码器（EnCodec）。用高通、Mel 带能量均衡、50 Hz envelope vocoder 等逐步物理消融隔离机制；并在 AIR BRIR+LibriSpeech 上做生态评测。

## 实验与结果
500 Hz、−14 dB SNR：EC 为 +15.7 dB；WavJEPA +0.5、GRAM-T +2.1（远低于天花板）；Spatial-AST/DSpAST/EnCodec 约 +6.8–7.0 dB；四类单耳对照恒为 0。GRAM-T 对 ILD 敏感（峰 18.2）远强于 ITD（~2.6），Spatial-AST 相反（ITD 152 > ILD 85）。高通与能量均衡几乎不伤 GRAM-T/EnCodec 检出；vocoder 摧毁 TFS 后 GRAM-T 100%→75%、EnCodec 100%→20%、Spatial-AST 100%→60%。语音生态条件下双耳模型显著率很高，但机制上仍可能是宽带包络干扰纹理而非真相位计算。

## 结论
通用双耳 SSL 主要依赖每通道 spectro-temporal interference / 包络纹理，而非跨通道相位；专用 IPD 架构可达实质但亚天花板的相位敏感。未来预训练需显式相位约束。

## 点评
把经典 BMLD 做成冻结表征探针，再用物理消融 falsify“相位编码”叙事，对空间音频可解释性很有力。注意 ΔBMLD 是嵌入距离比而非人类听阈；结论对预训练目标（MAE 重建谱 vs IPD 特征）的归因合理，但未覆盖全部空间模型族。
