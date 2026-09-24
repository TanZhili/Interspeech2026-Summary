# The Illusion of Balanced Multimodal Sentiment Analysis: Beyond the Limits of Optimization-Based Methods

- 论文编号：2556
- 报告人：Alexandros Potamianos
- 程序：Tuesday 29 September 2026 / Audio-Visual and Multimodal Perception
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/kaffeza26_interspeech.pdf

## 问题
多模态情感分析常因模态失衡（文本主导）而弱于单模态；社区依赖梯度/损失再加权（OGM、AGM、PMR、ReconBoost 等）试图「平衡」，但可能混淆拟合速度与判别贡献。

## 方法
统一评测框架：在 CMU-MOSI/MOSEI 上用简单 LSTM 晚融合隔离单模态优化动态；对比梯度类与损失类平衡法；诊断「loss≠utility、gradient≠importance」；探索优化器、batch、调制时长与专用校准集。主张转向留出集上的判别式模态效用估计。

## 实验与结果
Late Concatenation 在多数设定不可被可靠超越（如 MOSI A-V 54.93，T-V 74.35；各平衡法常小幅波动或更差）。结果对超参敏感；比例校准亦无稳定增益。训练曲线显示文本损失迅速下降并牵引多模态曲线，音视频损失近乎平坦。

## 结论
优化期再加权测错了信号，无法真正解决模态失衡；应改用基于留出性能的模态效用估计。

## 点评
批判性工作：用受控简单架构暴露「平衡算法」的幻觉，理论类比 1990s AVSR 似然比失败史很有力。强在统一对比；脆弱点在简化融合可能低估复杂注意力融合中再加权的作用，外推需谨慎。
