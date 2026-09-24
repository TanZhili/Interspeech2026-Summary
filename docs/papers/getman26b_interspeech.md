# Do Learned Layer Weights Reflect Pretrained Information Structure in Self-Supervised Speech Models?

- 论文编号：566
- 报告人：Yaroslav Getman
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/getman26b_interspeech.pdf

## 问题
先验认为 SUPERB 类可学习层权重与单层下游性能相关弱（ρ 约 0.39–0.71），“不可靠”。作者改问：这些权重分布是否反映预训练模型的层间信息结构？

## 方法
在冻结 SSL 上按层提取 phone/word 段表征，k-means 聚类后算与标签的 adjusted mutual information（AMI）。层权重取自 ML-SUPERB 英语 ASR（softmax 加权和 + CTC），比较 10 min 与 1 h 有标签监督；对每层输出做 layer norm 再聚合。用 Spearman ρ + 置换检验关联权重与 AMI。覆盖对比学习（wav2vec 2.0 族）、聚类（HuBERT）、聚类+去噪（WavLM）共 13 个 Base/Large/XLarge 模型。

## 实验与结果
52 个模型-条件组合中 49 个显著正相关。对比模型在 10 min 上最强（phone/word AMI 均值 ρ=0.86/0.91，个体可达 0.98）；1 h 降至 0.65/0.70。HuBERT/WavLM 更弱且更易变。额外监督使权重更集中于较深层、熵更低，偏离宽峰 AMI 曲线。权重虽仍接近均匀（归一化熵>0.996），但排序系统且与 AMI 对齐。

## 结论
层权重并非无信息：它们系统反映预训练层间音素/词信息结构，尤其在对比目标与低资源监督下；弱“权重–单层性能”相关更可能是参照不当，而非权重本身无用。

## 点评
把评价参照从下游单层分数换成预训练 AMI，直接回应“权重不可靠”叙事，结论清晰可复现。边界是仅 ASR + phone/word AMI；非 ASR 任务可能需要别的信息度量。
