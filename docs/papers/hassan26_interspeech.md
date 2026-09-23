# SCANS: Supervised Contrastive Temporal Alignment of Neural Responses and Speech Stimuli

- 论文编号：2651
- 报告人：K M Naimul Hassan
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hassan26_interspeech.pdf

## 问题
EEG 与言语刺激的时间对齐常被形式化为 match–mismatch 分类，但多数模型晚融合、自监督对比又受正负样本稀缺与跨被试噪声限制，难桥接模态差距。

## 方法
SCANS 将任务定义为：给定 EEG 片段与同一语音中的 N 个非重叠候选，找出唯一时间对齐的匹配段。两侧同构编码器：Dilated Convolutional Frontend（EEG 64 通道→128 维空间滤波；语音包络→128；三层膨胀卷积 dilations 1/2/4）+ 对称 Cross-Modal Attention（4 头，互相以对方为 K/V）。全局平均池化得 L2 归一化嵌入；候选与 EEG 拼接后经 MLP 分类。损失 `L = L_CE + λ L_align`（λ=0.5），其中对齐损失为 batch 内严格一一对应的对称 InfoNCE（可学习温度 τ）。

## 实验与结果
SParrKULee / ICASSP Auditory-EEG Challenge：EEG 0.5 Hz 高通、Wiener、平均参考、64 Hz；gammatone 包络 + x^0.6，64 Hz。窗长 t∈{3,5}s，候选 N∈{2,5}。N=2,t=3：Within MSA 87.09、Held-out 84.12，Total Score 86.1（2023 榜首 Thornton 等为 82.13）。N=5,t=5 Held-out MSA 69.33（HSSTD 4.60），高于 Wang/Thornton 等（约 60–62.8）。更长窗普遍提升准确率并压低被试方差。

## 结论
作者认为扩张卷积前端 + 全程跨模态注意力 + 监督对比多任务目标，可在有限样本下学到更稳的 EEG–言语共享空间，并在 2023/2024 挑战设定上达到新 SOTA，对未见被试泛化更好。

## 点评
相对晚融合余弦匹配，SCANS 把“标签可用的严格时间同步”写进对称对比矩阵，比纯 InfoNCE 自监督更贴合该任务；跨模态注意力直接打通特征提取中的模态缺口。代价是对 challenge 划分与硬负采样依赖强，N=5 held-out 方差仍可能被窗长掩盖个体差异。
