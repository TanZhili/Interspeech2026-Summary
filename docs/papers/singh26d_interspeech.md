# Selective Capability Unlearning in End-to-End Spoken Language Understanding

- 论文编号：3349
- 报告人：Akanksha Singh
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/singh26d_interspeech.pdf

## 问题
端到端自回归 SLU 中，功能是“意图 + 条件槽生成”。只压低目标意图边缘概率时，强制意图前缀仍可恢复槽结构，即 capability persistence；需选择性擦除条件映射并保留其余意图。

## 方法
Binding Subspace Unlearning (BSU) 两阶段：(1) 在槽位上 teacher-force 抽 decoder 隐状态，用 forget vs retain 协方差差 \(M^{(\ell)}=\mathrm{Cov}_{D_F}-\mathrm{Cov}_{D_R}\)，取正特征方向得绑定子空间 \(U^{(\ell)}\)；(2) 对条件 log-likelihood 相对隐状态的梯度投影到该子空间并惩罚 \(\mathcal{L}_{bind}\)。总目标：\(-\mathcal{L}_F+\lambda_{ret}\mathcal{L}_R+\lambda_{kl}\mathcal{L}_{kl}+\lambda_{bind}\mathcal{L}_{bind}\)。无推理开销。

## 实验与结果
SLURP 与 SpeechMASSIVE（法语子集）；Conformer 编码器 + Transformer 解码器，ASR 初始化与 SSL 初始化两套。相对 GA/NPO/RL 等，BSU 大幅降低 forget 集 BRR@10 与语义相似度（如 SLURP NeMo：BRR@10 92.64→22.10，Sim 90.14→24.80），retain 性能大体保持。Random Space 消融与 \(\lambda_{bind}\) 扫描支持子空间对齐的必要性。

## 结论
需在表示空间削弱意图–槽绑定，而非仅抑制意图分类；BSU 显著降低 forced-prefix 可恢复性并保留其余能力。未来拟扩展到更广生成任务。

## 点评
把 unlearning 问题从“别说出意图”改成“别还能按该意图填槽”，评估协议（BRR@10）直接对准失败模式。协方差对比假设 forget/retain 方差差能定位绑定方向，对纠缠强或小样本意图可能脆弱；表格数字密集，但主结论与图示一致。
