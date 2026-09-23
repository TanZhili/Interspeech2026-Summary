# StuPASE: Towards Low-Hallucination Studio-Quality Generative Speech Enhancement

- 论文编号：837
- 报告人：Xiaobin Rong
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rong26_interspeech.pdf

## 问题
生成式 SE 易幻觉；PASE 靠语义增强压幻觉，但在强噪声/混响下感知质量有限，且训练目标常保留仿真早反射，可能使目标本身听感混响、谱细节模糊，从而偏置生成分布。

## 方法
StuPASE 在 PASE 上两步改进：(1) dry-target 微调得 PASE-R——先用 DRD 把 DeWavLM 微调到 dry 干净语音的 phonetic 表示（DeWavLM-R），再微调 DualVocoder-R 重建 dry 波形；(2) 用 DiT flow-matching 生成干净 Mel，再经 Mel vocoder（改进 Vocos）合成波形，替代 GAN DualVocoder。条件为 DeWavLM-R 投影后的增强 phonetic 表示与噪声 Mel；训练采用 SenSE 式 speech-infilling（遮罩干净/噪声 Mel 区域，预测速度场 MSE）。工作室质量子集约 1000 小时（UTMOS≥4.0）。

## 实验与结果
DNS1 with-reverb 消融：PASE→PASE-R 的 UTMOS 1.61→3.23、dWER 9.78%→8.01%；StuPASE 达 UTMOS 4.01、dWER 7.89%。去语义或用噪声语义显著抬升 dWER（至 19.79%/36.36%）。DNS1 与 1000 条仿真测试上相对 TF-GridNet、FlowSE、PASE、SenSE、Adobe Enhance Speech V2，StuPASE 在混响与难例上 UTMOS/内容指标领先或并列，with-reverb dWER 最低（7.89%）。主观：Q-MOS 约 4.19（文末截断处给出最佳质量）。

## 结论
dry 目标提升去混响与语义保真；flow-matching 声学模块把质量推到工作室级，同时保留低幻觉。相对 SenSE 框架更简（无额外语义 LM）且内容指标更好。

## 点评
问题定位准：生成 SE 的目标定义与生成容量同等重要。dry-target 与 infilling 共同降低对噪声声学线索的依赖。脆弱点包括依赖 DeWavLM 语义质量、多模块分阶段训练，以及文末主观结果抽取略有截断；SpkSim 在换评测骨干后与原 PASE 论文不可直接比。
