# Enhancing Audio Reasoning via Semantic Summary Prediction

- 论文编号：1504
- 报告人：Francesco Bonzi
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/bonzi26_interspeech.pdf

## 问题
大音频语言模型（LALM）显式 Chain-of-Thought 常比直接作答更差：长推理易把注意力从音频拽向已生成文本，造成“reasoning gap”。现有缓解多依赖海量监督或昂贵 RL，缺少轻量训练期正则。

## 方法
提出 **SPARE**：在 SALMONN 13B 上，于音频/问题之后、CoT 之前插入 register 令牌 [REG]；用因果掩码使后续 token 看不到 [REG]，推理时丢弃该令牌与对齐头。训练时对 [REG] 末层隐状态与 Conclusion 的 Sentence-BERT 嵌入做余弦对齐损失，总损失 \(L_{\mathrm{CE}}+\lambda L_{\mathrm{align}}\)（\(\lambda=2\)）。数据为 YouTube8M 子集上 AF-Think 结构（summary/caption/reasoning/conclusion），约 16 万训 /4 万验。对比零样本、CoT、SFT、Audio MuToR。

## 实验与结果
MMAU / MMAR 零样本：SPARE 58.03% / 40.32%，高于 SFT（54.65 / 38.15）与 Audio MuToR（53.02 / 38.40）；零样本 CoT 则崩至 18.03 / 12.32。\(\lambda=1/2/3\) 均优于非 SPARE；多章节多 register 变差且不稳。注意力分析：首层 [REG] 对音频关注显著增强，答案 token 相对 SFT 也更听音频。

## 结论
用终局语义目标“播种”早期潜状态，可在不改推理流程、无额外开销下改善音频 grounding 与 CoT 推理。相对工业级大模型仍有绝对精度差距，但方法定位为可控设定下的正则策略。

## 点评
把 MuToR 式 register 从局部多 token 预测改成全局结论对齐，针对音频漂移问题更直接。因果掩码保证零推理成本是亮点。效果依赖 Conclusion 文本质量与 Sentence-BERT 空间；若结论本身短/歧义，对齐目标可能噪声较大。
