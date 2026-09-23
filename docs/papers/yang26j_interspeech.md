# A Fusion-Aware Two-Stage Framework for Mispronunciation Detection and Diagnosis in Low-Resource Modern Standard Arabic

- 论文编号：1553
- 报告人：Gongping Huang
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26j_interspeech.pdf

## 问题
低资源 MSA 上 MDD 受数据稀缺与合成–真实域差距制约；Transformer/LSTM 易全局平滑，难以保留强调对立、重叠辅音等局部音位线索，简单混合合成与真实数据还可能加重域偏移。

## 方法
混合架构：wav2vec2-xls-r-300m 编码器 + 因果膨胀 TCN + CTC。两阶段训练——Stage1 在 Iqra train（~79h）与 Iqra TTS（~80h）学通用映射；Stage2 在真实学习者 Iqra Extra IS26（~2h）适应。推理：Stage1 最优 checkpoint + Stage2 多个 checkpoint（共 K=6）经混淆网络对齐投票，并用由融合假设自估计的 MKN 3-gram 重打分，λ=0.2 偏重声学以免过度纠正。

## 实验与结果
盲测 QuranMB.v2：系统 F1=0.7201，相对基线 0.4414 提升 63.1%，居 IqraEval.2 榜首。消融：两阶段单 checkpoint 0.6825；仅 Stage1 0.4629；仅 Stage2 0.6681；naive Mix 0.4305（低于基线）；Stage2 上 TCN 优于 LSTM（0.6467）与 Transformer（0.6000）。集成+LM 相对单 checkpoint 再相对提升约 5.5%。

## 结论
TCN 局部归纳偏置、两阶段域适应与多 checkpoint 集成共同缓解合成–真实差距与低资源过拟合，刷新低资源 MSA MDD 表现。作者认为该流程可推广到其他数据稀缺语言。

## 点评
把挑战里“真实误读虽少但关键”落成可消融的课程式训练，并用 TCN 显式对抗语义平滑，工程闭环完整。弱点是高度依赖 Extra IS26 与集成后处理，单模型上限与对其他测试域的迁移仍需验证；声学权重 λ=0.2 的设定也表明语言学先验仍是双刃剑。
