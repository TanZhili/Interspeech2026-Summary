# GRIDS: Dimensionality-Aware Anomaly Detection in Learned Representations of Self-Supervised Speech Models

- 论文编号：2719
- 报告人：Sandra Arcos-Holzinger
- 程序：Monday 28 September 2026 / Speech Representations and Alignment
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/arcosholzinger26_interspeech.pdf

## 问题
S3M（WavLM、wav2vec 2.0）下游强，但对自然与对抗扰动下局部几何如何形变、是否与 ASR 退化同向，既有相似度/全局维数分析可见性不足。LID 在视觉/文本中可标出对抗样本高维邻域，但在变长帧级语音表示上尚未系统应用。

## 方法
GRIDS（Geometric Robustness via Intrinsic Dimensionality in Speech）：
- 在 LibriSpeech test-clean 配对子集（918 句，5–10 s）上，对清洁与扰动（匹配目标 SNR 0–40 dB）过 WavLM / wav2vec 2.0 BASE；
- 扰动：Gaussian / babble / speech 良性噪声；\(\ell_2\)-PGD（MSE 或 CTC 目标，300 iter）；
- 每层用 Levina–Bickel MLE（\(k\) 近邻）估帧级 LID，跨句池化后谐波平均得 12 维层轨迹；报告 \(\Delta\mathrm{LID}\) 与 WER 关联；
- 用 12 维 LID 特征做对抗 vs 良性异常检测。

## 实验与结果
（抽取在实验配置末截断；定量结论取自摘要。）
- 低 SNR 下各类扰动 LID 均升高；高 SNR 时良性噪声 LID 趋近清洁轨迹，**对抗样本仍保留浅层 LID 抬升**。
- LID 抬升与 WER 升高共现；层间 LID 特征异常检测 **AUROC 0.78–1.00**，支持无转写监控。

## 结论
局部本征维可作为 S3M 层几何诊断：刻画扰动形变、关联 ASR 退化，并实现转录无关的异常监测。框架不绑定特定下游标签。

## 点评
把 LID 从图像对抗检测迁到语音 SSL 的层轨迹，并强制匹配 SNR 对照良性/对抗，问题设定清楚。强在“几何–WER–检测”三条线；**结果表未出现在抽取文本中**，AUROC 区间与层曲线细节需回原文核对。
