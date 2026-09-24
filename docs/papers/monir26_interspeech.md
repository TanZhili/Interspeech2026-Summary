# Time–Frequency Weighted Losses for Phoneme Reconstruction in DNN-Based Speech Enhancement

- 论文编号：3416
- 报告人：Nasser-Eddine Monir
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/monir26_interspeech.pdf

## 问题
基于 SDR 的增强训练对时频均匀加权，忽视辅音爆发、摩擦等高可懂度线索及强语音–噪声竞争区；既有频率加权 SDR 未统一结合语音存在、局部 SIR 与瞬态动态。

## 方法
在 Mel 域定义 TF 加权 SDR \(L_w\)。提出：(1) \(L_{SIR\cdot SP}\)：sigmoid 门控低 SIR 与语音存在；(2) \(L_{SIR\cdot SP\cdot SF}\)：再乘光谱通量（spectral flux）放大瞬态；(3) \(L_{learn}\)：可学习频带权重（ANSI 1997 初始化）。在 FaSNet（4 通道助听器阵列）上相对时域 \(L_T\) 与先前 \(L_{logSIR}\) 比较。

## 实验与结果
白噪（WN）与语音整形噪（SSN）、SIR −8～8 dB。\(L_{SIR\cdot SP\cdot SF}\) 在 WN 上 FW-SIR/FW-SDR 与辅音/元音音素准确率（PA）更稳；塞音 PA 在中高 SIR 显著高于基线；谱分析显示中频结构在 0/8 dB 更接近干净参考。SSN 下 STOI/部分失真指标有代价，但干扰抑制与高 SIR 识别更一致。

## 结论
把 SIR、语音存在与光谱通量并入可微 SDR 权重，可改善干扰抑制与音素级重建，尤其利于辅音/塞音；适合助听器式场景中对瞬态线索的强调。

## 点评
训练目标直接对准“竞争 TF + 瞬态”，比全局 SDR 更贴可懂度。SSN 与极低 SIR 上收益变弱，且未做听音试验，与真实感知仍隔一层。
