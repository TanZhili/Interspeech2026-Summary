# From Single to Multi-Label SER: Dataset and Mamba-Based Fusion Model

- 论文编号：3458
- 报告人：Thi Thu Trang Nguyen
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/tran26c_interspeech.pdf

## 问题
主流 SER 把众包投票压成单标签，抹掉共现与标注歧义；公开大规模多标签语音 SER 基准稀缺。Transformer/SSL 骨干对长音频又偏重。

## 方法
将 MSP-Podcast V2.0 转为多标签：丢弃评分 <3 或 OOS 比 ≥0.5 的样本；多数类必选，次要类需同时满足票数/相对比例/对多数比阈值，L_max=3；训练集上长尾组合剪枝。主基准 n_min=2_final：保留训练样本 ≥1000 的 18 种组合，并做 train-only 右移增强平衡。双分支 Mamba：MFCC（轻量 1D CNN 前缀）与 100 维 log-mel（patch+更深 Mamba）分别编码、masked mean pool，门控缩放后拼接瓶颈头，8 路 sigmoid；二元 focal loss。验证集全局阈值扫描选 checkpoint，测试固定 t=0.45。

## 实验与结果
Fusion-Gate（3.07M）Test1 miF1/maF1/HL/Jac 为 0.510/0.305/0.179/0.412；Test2 为 0.514/0.258/0.179/0.405，优于单模态 Mamba 与多数复现的韩语融合基线，并接近/超过部分 MulT、WavLM（94.3M）的集合指标。作者强调差异更多体现在 HL/Jaccard/ExactAcc；尾类 Fear/Disgust/Contempt 仍很难。抽取后部讨论略有延续但主表已完整。

## 结论
提供可复现的 MSP-Podcast 多标签构建协议与轻量 Mamba 融合基线，在统一协议下 micro-F1 约 0.50；长尾与稀有情绪仍是限制。代码与划分将公开。

## 点评
贡献重心在标签协议（确定性 multi-hot + 防泄漏剪枝）而非刷大模型。Mamba 线性时序适合长 podcast；脆弱处是固定阈值对尾类不友好、组合空间被压到 18 种牺牲了真实歧义覆盖，以及与 SSL 大模型比参数仍非最轻但准确–效率折中明确。
