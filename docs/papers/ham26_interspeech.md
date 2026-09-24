# Continuous 2D Spectral—Temporal Transformer for Speaker Verification

- 论文编号：963
- 报告人：Seongwook Ham
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ham26_interspeech.pdf

## 问题
ReDimNet 等混合架构在全局依赖建模前常把频谱维并入通道，破坏显式时–频网格；全局建模应在坍缩后还是直接在 2D 谱–时网格上进行，尚不明确。

## 方法
提出 C2D-ST：骨干全程保持 X∈R^{B×C×F×T}；五阶段共 16 层 Transformer，每阶段先 Neighborhood Attention 做局部谱–时建模，再 Axial Attention 沿时间与频率轴做全局依赖；阶段输出加权聚合后才 1D 投影，末段 8 层时序注意力 + ASP 出嵌入。RoPE 用于轴向/全局注意力；Neighborhood Attention 含 RPB 与 value-side RPE。

## 实验与结果
VoxCeleb2-dev 训练、VoxCeleb1-O/E/H 评测；80-dim log Mel，SphereFace2，ESPnet-SPK。6.9M 参数下：无 LMFT/QMF 平均 EER 0.627；+LMFT 0.517；+LMFT+QMF 达 0.507/0.051（minDCF），优于 ReDimNet-B6（15.0M，0.633/0.059）与 ECAPA2（27.1M，0.617/0.062）。消融：去轴向→NA 平均 EER 升至 0.693；仅时间轴向 0.533；轴向改为坍缩后 1D Transformer 升至 0.557 且参数多 2.8M。

## 结论
作者认为全程保持谱–时网格并直接在网格上做全局建模，能以更少参数达到有竞争力的验证性能；局部用注意力、末段可用卷积等设计选择亦有消融支持。

## 点评
用结构回答“何时坍缩频谱维”，相对盲目加深更干净。强项在参数效率与对照消融；与更大模型的对比依赖引用结果与 AS-Norm/QMF 设定一致性，跨语料泛化未展开。
