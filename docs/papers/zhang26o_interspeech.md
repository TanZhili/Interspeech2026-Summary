# Rubric-Aligned Disentangled Evaluation of Human Simultaneous Interpreting

- 论文编号：1105
- 报告人：Ziyu Zhang
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26o_interspeech.pdf

## 问题
人工同传（SI）专业评测用分析性量规分开意义传递、表达与时延，但缺少面向量规、句段级的自动指标。MT 标量指标与 LLM 提示评分易把多维坍成单一质量信号。

## 方法
构建 1,101 段专业双评注 SI 语料（LQ/EXP/LAT，0–3；talk 级划分，En↔Zh）。焦点为文本侧 LQ 与 EXP。在 COMET-KIWI 上用 LoRA + 双独立回归头，残差预测与 MSE+方差正则；对比冻结 COMET-KIWI、单头标量微调、结构化 LLM 零/少样本提示等。LAT 留待多模态。

## 实验与结果
人评者间绝对一致偏低（LQ/EXP Pearson 约 0.21/0.27），一致性 ICC(3,1) 约 0.34/0.43。Dev 上 LLM 提示与人相关近零，且 LQ–EXP 耦合 corr≈0.90（人约 0.56）；标量微调亦近零。Test：双头模型 Pearson LQ 0.388、EXP 0.301，显著优于冻结 COMET-KIWI（0.219/0.175）；预测维间相关 0.529，接近人类耦合。错误多在多步骤程序性内容的步骤完整性。

## 结论
监督结构（而非仅骨干容量）是瓶颈：提示与标量监督坍缩量规维度，双头结构化监督可恢复相对人类一致性范围内的稳定排序信号，服务形成性反馈而非替代认证。

## 点评
把问题从“换更大 LLM”转到“量规监督是否可分”，并用相同骨干隔离监督结构，实验设计干净。绝对相关不高但对照人–人天花板后解读合理。文本-only 对 EXP 是下界；LAT 与客观时延几乎无关，说明“感知同步”本就不是简单 onset 差，多模态是自然下一步。数据集规模与中英双向限制外推，但对 SI 自动评测方向很清晰。
