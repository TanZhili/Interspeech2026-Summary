# On Optimizing Multimodal Jailbreaks for Spoken Language Models

- 论文编号：309
- 报告人：Aravind Krishnan
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/krishnan26_interspeech.pdf

## 问题
Spoken Language Models 同时接受语音与文本，现有越狱多只优化单一模态；仅凭单模态鲁棒性可能高估多模态系统安全性。

## 方法
提出 JAMA：白盒联合优化文本后缀（GCG）与音频扰动（PGD），每步对同一联合损失同时更新 δ 与离散 suffix。评估 Audio Flamingo 3、Qwen2 Audio、Gemma 3N、Qwen2.5 Omni；PGD 初始化用朗读/对话/音乐等四类基音频。据梯度能量分析提出 SAMA：先纯文本 GCG 再固定后缀做 PGD，作为更便宜的序列近似。数据为 AdvBench（8 训 / 480 测，5 seed），成功判据含 LLaMA Guard 3。

## 实验与结果
JAMA 相对单模态 GCG/PGD 越狱率提升约 1.5×–20×；Gemma 3N 对纯 GCG 很硬（长后缀仍约 3%），但联合优化（尤其音乐+较长 PGD）明显打开缺口。PGD 单独通常弱于 GCG；音乐初始化与更长音频往往更强。t-SNE 显示成功多模态攻击落在远离 benign 的独立子空间。SAMA 在足够长的 GCG/PGD 配置下接近 JAMA，平均差距约 10%，计算约快 4×–6×（同配置 H100）。

## 结论
多模态同时扰动暴露单模态评测看不见的脆弱面；序列近似可作强基线。作者主张发布前需在复合攻击空间加强护栏。

## 点评
把 GCG 与 PGD 真正“同时”接到同一损失上，比“一模态优化、另一模态旁观”更贴近对手。结果依赖可微特征提取器改写与白盒设定；对不可微/闭源 SLM 的迁移性正文未覆盖。
