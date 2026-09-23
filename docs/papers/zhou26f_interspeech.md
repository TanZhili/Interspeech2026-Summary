# Conflict-Aware Pseudo-Labeling via Acoustic Signals for Multi-Task Speech Emotion Recognition

- 论文编号：2118
- 报告人：Shunfei Liang
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhou26f_interspeech.pdf

## 问题
话语级 SER 标签抹掉帧内情绪动态；用 ASR 转写做细粒度对齐成本高。朴素伪标签在模糊帧上噪声大。

## 方法
冲突感知伪标签：训练数据分 K 折训 K 个冻结 emotion2vec 子模型；去掉池化后对帧做协同推断。多数票（>K/2）帧赋硬伪标签（共识区）；无共识帧用话语级真值回填（冲突区）。下游共享 HuBERT 编码器，话语分支 attention pooling + CE，帧分支对共识/回填分别 CE，L_total=L_utt+λ(L_cons+α L_rect)。推理丢弃帧头。

## 实验与结果
IEMOCAP（4 类 LOSO）、EmoDB（7 类）、MELD 官方划分。作者称三集均达 SOTA 且无需辅助文本；抽取文本在实现细节处截断，完整 WA/UA 对比表未见。

## 结论
仅用声学协同共识与全局回填即可构造帧级辅监督，提升表示而不增加推理开销。边界是伪标签仍依赖话语级真值先验与子模型多样性。

## 点评
用“多视角共识 vs 冲突回填”处理伪标签噪声，比单纯稠密伪标更稳，并避开 ASR 依赖。强处是训练期多粒度、推理零附加；脆弱处是 emotion2vec→HuBERT 骨干切换与 K 折成本，以及截断导致 SOTA 数字不可核对。
