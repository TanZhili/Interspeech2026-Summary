# BEST-RQ-2: Contextualize-Then-Predict, a Two-Step Approach for Self-Supervised Audio Representations

- 论文编号：2488
- 报告人：Ludovic Tuncay
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：https://www.isca-archive.org/interspeech_2026/tuncay26_interspeech.pdf

## 问题
BEST-RQ 用冻结随机投影离散目标做掩码预测很稳，但原 Conformer 与“掩码原位输入”难支持 JEPA 式“先上下文、再预测”；通用音频域（语音/环境/音乐）需要更好的架构分解。

## 方法
**BEST-RQ-2**：ViT 上下文编码器只看未掩码 mel 块；轻量 ViT 预测器在预训练时对掩码块预测 8192 码目标，推理丢弃。对照 BEST-RQ（Conformer）与 BEST-RQ (ViT)（同 tokenizer/目标但单阶段原位掩码）。AudioSet 约 1.9M×10s，200k 步。

## 实验与结果
X-ARES 线性探测：BEST-RQ-2 MoM/Overall 0.50/0.49，优于 BEST-RQ 0.43/0.45 与 BEST-RQ (ViT) 0.44/0.43；语音略换环境/音乐增益。kNN 上同样领先同类。文称 XARES-LLM 上两步分解带来一致迁移增益，推理算力不变。

## 结论
跨域平均提升主要来自 contextualize–then–predict 分解，而非仅换 ViT；ViT 本身更重分配域内表现。

## 点评
干净消融把“编码器换骨”和“预测分解”拆开，对挑战赛式通用编码器很实用。冻结随机目标保持简单；语音域相对 Whisper 等仍可能偏弱，需按下游权衡。
