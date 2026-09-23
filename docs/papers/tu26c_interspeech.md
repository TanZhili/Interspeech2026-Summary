# AV-SNINet: A multi-channel audio-visual speech-noise interaction network for Target Speaker Extraction with cross-beam attention

- 论文编号：3227
- 报告人：Yanhui Tu
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/tu26c_interspeech.pdf

## 问题
远场多通道 AV 提取多靠唇音同步增强目标，较少在波束域显式做目标–干扰互斥抑制；低 SNR 下 mask 波束成形残差仍拖累 ASR。

## 方法
两阶段：① AV-DPCRN 用 LPS+IPD+唇特征估 IRM，经 GEVD 得目标/干扰波束；② AV-SNINet 双分支 DPCRN 分别吃 Concat(Gs/Gn, LPS, Lip)，瓶颈插入 cross-beam attention——帧级交叉注意后从对方分支减去“像对方”的成分，联合估言语/噪声 IRM（λs=λn=1）。视觉编码器冻结于 LRW 预训练。

## 实验与结果
自建环形阵真实录音与匹配设定的 LRS2 远场仿真（SNR −10–+10 dB，距离 0.5–2 m）。真实集平均 WER：Baseline 28.40 → AV-SNINet 20.38（相对降 28.23%）；双塔 interactor（v3）优于共享注意矩阵变体。LRS2 仿真平均 WER 17.20，优于 USEV+GEVD（19.37）与 RTFS-Net+GEVD（20.47）。

## 结论
波束先验加双分支交叉注意可进一步压低残差干扰，低 SNR 与远场下 ASR 收益明显。

## 点评
抓住的是“目标波束与干扰波束应互相排斥”这一空间–谱结构，比单纯 AV 融合更直接。指标以黑盒 ASR WER 为主，贴落地；代价是依赖第一阶段 mask 质量，且大量结果来自自建场景，公开可比性主要靠 LRS2 仿真补充。
