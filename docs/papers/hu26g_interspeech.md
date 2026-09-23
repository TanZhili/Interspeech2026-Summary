# Singing Voice Conversion via Shared Speaker Space and Min-Pooling Adversarially Enhanced Flow Matching

- 论文编号：2090
- 报告人：Hao Huang
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hu26g_interspeech.pdf

## 问题
SVC 中内容–音色解耦与重建质量常冲突：VQ 等显式解耦易丢细节或漏源音色；KNN 映射到共享歌手空间可去音色，但帧级拼接不连续，且 flow matching 易糊高次谐波。

## 方法
MinFlow-SVC：WavLM 特征经 content encoder，用指定共享歌手特征池做 KNN 对齐训练（Lknn）；对 encoder 输出做 min-pooling 对抗（盯最差连续性格子）平滑不连续。目标 Mel 由 OT-CFM 在内容、目标音色、F0 条件下生成；再以动态谐波掩码（DHM）+ min-pooling 对抗强化谐波区。先训 encoder 再冻住训向量场，HiFi-GAN 声码。

## 实验与结果
M4Singer 训练，OpenSinger 6 人零样本评测。说话人分类：原 WavLM 95%，转共享空间后 98%（表明源音色被抹掉）。MinFlow-SVC-10：NMOS 3.83、SMOS 2.65、F0CORR 0.948、MOSNet 4.26，整体优于 So-Vits-SVC、DiffSVC、NeuCoSVC；消融去 content encoder 损 SMOS，去 Lmin-pooling/Ladv-harm/DHM 均降自然度或 F0 相关。

## 结论
共享空间 KNN 去音色 + 双阶段 min-pooling 对抗（特征连续与谐波感知）可缓解解耦–质量权衡，零样本转换主观/客观更优。

## 点评
用共享说话人空间替代码本，解耦更“硬”；min-pooling 专门打最差局部，贴合歌声瞬态/谐波瑕疵。依赖选定共享歌手与 KNN 匹配质量，共享池覆盖不足时可能引入内容失真。
