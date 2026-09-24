# Eliminating Stability Hallucinations in LLM-based TTS models via Attention Guidance

- 论文编号：1345
- 报告人：Shiming Wang
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wang26x_interspeech.pdf

## 问题
LLM-based TTS 缺少显式 text–speech 对齐，在长文本/难文本上易出现稳定性幻觉（重复、无尽生成、漏读）。早期 cross-attention 单调约束不适配 decoder-only；硬单调注意力又伤自然度；强制对齐标签在大规模数据上难以获得。

## 方法
在 CosyVoice2（Qwen-0.5B，24 层×14 头）上分析自注意力，发现中层存在类似 cross-attention 的“alignment heads”。提出 Optimal Alignment Score（OAS）：对 speech→text 注意力子矩阵用 Viterbi 求最优对齐路径，再取路径概率占比；OAS 与 WER 相关系数约 −0.638。将第 8、9 层半数头指定为对齐头并 mask 到对齐区域，用可微 OAS 正则 LOAS 监督。进一步做 attention-guided CoT 学生训练：用教师最高 OAS 头路径作伪强制对齐；学生预测稀疏重复文本 token（非整段重复）与 progress bar 位置值（L1 + 一阶差分非负约束），且预测文本不回灌输入，减轻伪标签误差累积。

## 实验与结果
WenetSpeech4TTS 从头训 LLM；Seed-TTS-Eval 与 CV3-Eval 上评 hard/common。相对 CV2，CV2 OAS 在 hard 上 WER 分别降约 2.1%/1.6%（Seed hard 13.568%→11.472%；CV3 hard 10.239%→8.657%），SIM/UTMOS 不降。CV2 AG（sparse text + progress bar）进一步到 Seed hard WER 9.984%、CV3 hard 6.660%。稀疏文本监督的 token 准确率明显高于 full text（train 97.10% vs 90.44%）。common 场景 MOS 略升或持平。

## 结论
用 OAS 损失与注意力引导训练，可在难文本上减少 CosyVoice2 的稳定性幻觉，且不明显损害自然度与相似度，且无需真实强制对齐标签。

## 点评
做法抓住的是 decoder-only TTS 里“对齐头可学、可监督”这一结构：先度量再约束，再用伪对齐做 CoT，比硬单调推理更贴合语音连续性。稀疏重复 + progress bar 是对伪标签不准与重复句式的务实修补。潜在脆弱处是对齐头层位与头选择依赖该 backbone 的统计（文中锁定 8–9 层），换模型需重标定；伪对齐质量上限仍受教师稳定性约束。
