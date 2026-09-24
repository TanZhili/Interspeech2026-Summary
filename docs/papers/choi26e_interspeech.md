# SISER: Speaker-Invariant Speech Emotion Recognition with Entropy-Based Adversarial Training

- 论文编号：2186
- 报告人：Eunseo Choi
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26e_interspeech.pdf

## 问题
SER 受说话人变异与标注稀缺双重制约；对抗式去说话人常配浅层判别器，对抗压力不足，且 GRL 不约束失败后的目标分布形状。

## 方法
SISER：wav2vec 2.0（微调时仅解冻最后两层 Transformer）作编码器，ECAPA-TDNN 作说话人分类器，情感头为多层 FC。交替训练：先更新 SC 的说话人 CE；再固定 SC，用情感 CE + 最大化说话人后验熵联合更新 ENC/EC（λ=0.5）。无增强以隔离模块贡献。

## 实验与结果
IEMOCAP 四类（happy 含 excitement），10-fold leave-one-session。测试 UA/WA：基线（CNN+GRU+熵，无增强）51.15/50.14；wav2vec vanilla 56.46/54.45；GRL+ECAPA 56.95/56.01；SISER 60.63/58.53，接近原方法有增强版本（59.91 UA）。消融：换 ECAPA 相对浅层 FC 提升约 6–7 UA；t-SNE 显示情感簇更分离。

## 结论
作者认为强说话人判别器+熵最大化是说话人不变表示的关键；简单分类头已够用，更复杂头可再涨点。

## 点评
把“判别器容量”当作一等公民，消融说服力强。无增强设定公平但绝对分可能偏低；熵最大化在说话人极少的折上是否过度抹平情感仍需警惕。
