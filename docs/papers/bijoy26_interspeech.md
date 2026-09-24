# Mixture-of-Accent-Adapters for Robust ASR: Injecting Accent Cues into Pretrained Whisper

- 论文编号：1373
- 报告人：Mehedi Hasan Bijoy
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/bijoy26_interspeech.pdf

## 问题
带口音语音仍是包容性 ASR 瓶颈；全量微调预训练模型昂贵。既有适配器/多任务方案缺少口音专用适配器、可控编码器级口音线索注入，以及兼顾特化调节与性别信息泄漏抑制的监督设计。

## 方法
Mixture-of-Accent-Adapters（MoAA）作用于冻结 Whisper：池化状态控制瓶颈估计 accentedness；从可学习 soft accent codebook 加权检索注入口音线索并路由轻量口音专家适配器，再与骨干做门控混合。对抗性别头（GRL）抑制泄漏；reference-free hallucination suppression（DHF）抑制罕见解码伪影。默认口音弱时回退冻结骨干。

## 实验与结果
AESRC 上 Whisper-small：MoAA+DHF 达 WER 7.49%、CER 3.81%，约 0.51M 可训参数（约 1% 骨干）。优于全微调（15.50）、LoRA（15.83）与单适配器+DHF（10.25）；相对单适配器+DHF，WER 相对降约 26.9%。消融去掉线性投影或局部解冻编码器/解码器显著变差；GRL 使性别分类准确从约 98.6% 崩至约 29.8%。

## 结论
口音条件化路由 + codebook 注入在冻结 Whisper 上实现按需特化，配合 DHF 达到强口音鲁棒且参数极省。

## 点评
核心是“估计口音强度再决定是否/如何特化”，比一律加适配器更贴分布。DHF 与 MoAA 互补（前者稳解码、后者改编码器状态）。注意与带外置 LM/多阶段流水线的历史 SOTA 不完全可比；口音标签与 accentedness 估计误差会传导到路由。
