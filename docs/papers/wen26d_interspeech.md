# Towards Robust Ultrasound-based Silent Speech Recognition Learning Physics-Aware and Context-Rich Representations

- 论文编号：2646
- 报告人：Qisheng Xu
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/wen26d_interspeech.pdf

## 问题
基于 Ultrasound Tongue Imaging（UTI）的 Silent Speech Recognition 面临两类瓶颈：探头位移与散斑噪声等成像物理变异使同一发音在表示空间不稳定；协同发音带来的长程时序依赖又难被逐帧独立建模抓住。

## 方法
提出物理感知与上下文丰富表示学习框架：用 k-means 对高帧率 UTI 序列做时序聚类下采样，得到紧凑且保留关键调音上下文的定长序列；训练时施加物理启发增强——空间平移模拟探头位移、高斯噪声模拟散斑、时序掩码强迫依赖长程上下文；前端用 3D-CNN 提局部时空特征，再经双向 GRU 建模全局时序，以 CTC 端到端解码。

## 实验与结果
在 UXTD 儿童词级数据上比较 ST-GRU、ST-LSTM、ST-Transformer。Overlap 设置下 Ours 的 WER/CER 为 0.1595/0.1009，相对最佳基线 WER 降约 36.5%；Unseen 设置下为 0.0597/0.0227，相对最佳基线 WER/CER 分别降约 50.4%/69.1%。消融表明 3D-CNN 与数据增强均必要；物理增强使同内容不同采集条件的表示余弦相似度由 0.7697 升至 0.9630。

## 结论
一致性（物理增强）与完备性（聚类下采样 + 3D-CNN/BiGRU）共同提升 UTI-SSR 鲁棒性与跨说话人泛化；低资源下时空归纳偏置优于大容量 Transformer。未来拟探索自监督预训练与更大规模数据。

## 点评
把超声成像的物理伪影直接做成增强先验，比单纯堆更深网络更贴 UTI 特性。聚类下采样在压缩冗余的同时保留调音关键帧，对长序列与小数据场景合理。ST-Transformer 崩溃也提示：UTI-SSR 更吃局部运动与噪声抑制，而非全局注意力容量。局限是目前主要在 UXTD Type-A 词级设定，句子级与更强探头变异仍待验证。
