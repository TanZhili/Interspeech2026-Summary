# Enhancing Temporal Prediction Consistency for Short-Duration Acoustic Scene Classification via Semantic Adversarial Training

- 论文编号：1955
- 报告人：Yiqiang Cai
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 2
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cai26b_interspeech.pdf

## 问题
短窗（如 1 s）声学场景分类相对满时长严重掉点。作者归因于时间预测不一致：短窗预测与长时场景语境错位。需迫使特征丢掉“时长依赖语义方差”、保留场景判别信息。

## 方法
提出 Semantic Adversarial Training（SAT）：辅助对抗目标与场景分类竞争，事件判别器（527 类，伪标签来自冻结 BEATs/AudioSet）经 GRL 对抗；用 Local–Global Prediction Discrepancy（LGPD）分层稳定/不稳定测试子集。在 TAU20 上以 10 s 为全局、1 s 为短窗评测。

## 实验与结果
基线随 LGPD 升高准确率由约 95.8% 掉到 34.7%。Table 显示 +SAT 达 76.2 / 50.9（对应分列指标）优于 Mixup、Freq-MixStyle、MTL、KD、JTL 等；不稳定集上缓解掉点更明显。

## 结论
作者认为时间预测一致性与短窗 ASC 精度直接相关，SAT 可提升高差异样本上的稳健性与时序一致性。

## 点评
把短窗崩塌诊断为“与全局语境不一致”而非单纯信息不足，并用事件级对抗去掉时长相关捷径，思路清晰。事件伪标签噪声与对抗权重敏感；LGPD 分层本身依赖满时长语境，部署时短窗系统未必总能拿到 10 s 参考。
