# Rethinking Entropy Minimization in Test-Time Adaptation for Autoregressive Models

- 论文编号：944
- 报告人：Chee-En Yu
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/huang26c_interspeech.pdf

## 问题
分类任务上熵最小化（EM）是成熟的测试时适应（TTA）手段，但用于自回归生成时，既有做法分裂为伪标签 teacher-forcing 与策略梯度 RL 启发式，缺统一、数学正确的 EM 梯度。

## 方法
推导自回归模型上精确 EM 目标，自然分解为：
- **token 级策略梯度项**；
- **token 级熵项**。
据此将先前方法解释为该统一目标的部分实现。在 Whisper ASR 上实施 episodic TTA（单样本适应后复位），比较 Greedy-EM、序列级与 token 级变体及 beam 扩展（如 EM-tok-b）。

## 实验与结果
- 加性噪声：源模型平均 WER 22.53%；Greedy-EM 21.91%；EM-seq 21.34%；EM-tok 20.77%；**EM-tok-b 平均 19.15%**，在十种噪声上最低。
- 口音迁移等亦有表（摘要称覆盖噪声、口音、多语等 **>20 域** 持续改进；自称首次对 Whisper 做 TTA）。

## 结论
正确 EM 为自回归 TTA 提供统一理论；完整 token 级目标（可加 beam）优于不完整启发式，提升 Whisper 在分布偏移下的稳健性。

## 点评
贡献首先是理论澄清：把“伪标签熵”与“RL 熵奖励”收束到同一分解。强在 Whisper 多域实证；脆弱在 episodic 单样本适应的算力与稳定性，以及伪标签质量差时策略梯度方差——噪声表显示完整目标更有效，但极端失配时仍可能放大错误。
