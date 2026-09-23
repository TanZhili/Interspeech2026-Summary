# Rethinking Speaker Embeddings for Speech Generation: Sub-Center Modeling for Capturing Intra-Speaker Diversity

- 论文编号：942
- 报告人：Ismail Rasim Ulgen
- 程序：Monday 28 September 2026 / Speaker Verification: Advances in Speaker Embeddings
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ulgen26_interspeech.pdf

## 问题
说话人嵌入多为识别目标训练，压缩类内方差、强化类间分离；用作 TTS/VC 条件时会丢掉韵律、风格等生成所需的说话人内变化。如何在判别目标下保留结构化类内多样性。

## 方法
在 ECAPA-TDNN + AAM-Softmax 上，每说话人学 C 个子中心；对各类子中心相似度做温度 softmax 聚合后再算角间隔损失。嵌入（192 维）接入 Polyak 式语音重合成 VC：HuBERT 单元 + VQ-VAE 离散 F0 + HiFi-GAN，源提供内容/基频、参考提供说话人嵌入。嵌入在 VoxCeleb2 训练；VC 用 VCTK（90 训/20 零样本）。评测：类内/类间方差比、EER（VCTK 试次与 Vox1-E）、转换语音 F0 std/range、WER/CER、d-vector SECS、MOS/SMOS/ABX 韵律。

## 实验与结果
C=10/20 且 T=1 时类内方差升且 EER 不降反升（如 Vox1-E：基线 1.46%→C=10 的 1.15%）；T=0.1 使方差更低、更偏识别。VC 上 C=20：F0 std 8.03→10.25，WER 14.84→13.93，CER 6.82→6.41；低方差配置 SECS 最高（65.86%）。主观：C=20 MOS 3.18、SMOS 2.88，优于基线 2.94/2.65，ABX 韵律偏好更高方差嵌入。

## 结论
子中心建模可在保持辨别力的同时增加类内变化，改善零样本 VC 的自然度与韵律表达；温度控制子中心利用率。嵌入设计应按下游生成目标重新权衡紧凑性。

## 点评
把“类内方差当噪声”翻转为生成设计维度，子中心聚合是轻改 AAM 头的干净实现。证据链从方差比→F0→可懂度→听感较完整；局限是仅在一种重合成 VC 上验证，且高方差与最高说话人相似度仍有权衡。
