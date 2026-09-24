# Distilling Structured Reasoning into SpeechLLMs for Spoken Language Understanding

- 论文编号：1540
- 报告人：Toshihiro Tsukagoshi
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/tsukagoshi26_interspeech.pdf

## 问题
SpeechLLM 微调做意图分类/槽填充时，语义相近意图仍易混淆；纯标签监督难拉开边界，收集近边界样本成本高。文本侧推理蒸馏有效，但能否迁移到语音输入的 SLU 尚不清楚。

## 方法
提出 **RG-FT**：用 DeepSeek-R1 在转写、金标与意图/槽定义上生成结构化轨迹 \(T=(C,R,L)\)——候选枚举、对错误候选的拒斥理由、最终标签；94% 样本格式合格。训练对比 Direct-FT（只预测 L）、Reasoning-FT（只学完整轨迹，推理时也生成 C/R）、RG-FT（多任务 \(\alpha L_{\mathrm{reasoning}}+(1-\alpha)L_{\mathrm{label}}\)，推理仅直接出标签）。在六个 SpeechLLM 上全参微调，语音+金标转写联合训练，\(\alpha=0.5\)。

## 实验与结果
SLURP 与 Speech-MASSIVE-FR：RG-FT 全面优于 Direct-FT；意图准确率最高约 +2.4%，SLU-F1 最高约 +2.8（如 Music-Flamingo）。Reasoning-FT 普遍差于 Direct-FT。潜空间：Silhouette、Fisher ratio、centroid margin 均上升。消融显示 C→R→L 逐步增益；\(\alpha\) 呈钟形，0.5 附近稳健。

## 结论
把拒斥式结构化推理作辅助正则，可 sharpen 意图边界且推理零额外开销。纯推理监督不稳定；开放问题包括轨迹质量、教师选择、噪声条件下声学如何进入推理。

## 点评
关键设计是“对比拒斥”而非只肯定正确标签，直接针对近义意图混淆。多任务把推理压成训练期表征塑造、推理期仍直出标签，工程上务实。教师依赖文本转写与金标，对纯语音噪声/ASR 错误的鲁棒性正文未充分验证。
