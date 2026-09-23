# ML-KD-DRI-GAN: Teacher-Guided Denoising and Triplet-Adversarial Training for Robust Spoken Language Understanding

- 论文编号：670
- 报告人：Ankit Kumar
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26b_interspeech.pdf

## 问题
模块化 SLU 依赖 ASR 转写，替换/插入/删除错误会扭曲语义表示，造成干净训练分布与噪声推理分布的失配。对比学习与一致性方法多做确定性表征对齐，GAN-BERT 等对抗框架也未显式利用 clean–noisy 对应或教师决策边界，难以在严重 ASR 噪声下稳定做意图分类。

## 方法
提出 ML-KD-DRI-GAN：先在干净转写上训练教师（生成器为 768→512→256→512→768 的编码器–解码器瓶颈，判别器用 GAN-BERT 目标），冻结后指导学生。学生生成器对噪声嵌入做多层潜空间对齐（输出级与瓶颈级余弦对齐）；学生判别器经 Bi-DCD 对齐教师瓶颈特征与意图 logits（含温度 KL）；合成生成器产生硬负样本，并在判别器上施加 clean / denoised / synthetic 的 triplet 分离。BERT 编码，分阶段：教师独立训练 → 学生仅对抗预热 10 epoch → 再引入对齐、蒸馏与度量学习。

## 实验与结果
在 SLURP 意图检测（60 类）上，用 SpokenCSE 提供的 Google Web API / Wav2Vec 2.0 噪声假设（中位 WER 约 25% / 60%）。相对 GAN-BERT，N0.25 / N0.60 上绝对提升 4.49% / 6.46%；ML-KD 达 86.99% / 73.56%。消融显示：仅学生 DRI-GAN → 加生成器对齐 → 加判别器 KD → 加 triplet，性能逐步上升。t-SNE 显示类内更紧、类间更清；α/β/γ 在适中区间最优，高噪声下增益更大。

## 结论
多层蒸馏、对抗去噪与 triplet 度量联合，可把噪声嵌入拉回干净语义流形并改善决策边界；作者计划扩展到更多真实声学条件与 ASR 系统。

## 点评
抓的是「嵌入空间去噪 + 教师决策边界迁移」这一类 noisy SLU 问题，比纯对比一致性多了显式生成器去噪与双判别器蒸馏。强在组件可逐步消融、与 DRI-GAN/GAN-BERT 路线衔接清晰；脆弱点在依赖 clean–noisy 配对与两阶段训练超参（α/β/γ），且主结果集中在意图分类与合成噪声假设，对槽位填充与真实部署 ASR 分布的外推仍待验证。
