# SETEAB: Multiscale approach with Squeeze-and-Excitation Temporal Enhanced Aware Block for Speech Emotion Recognition

- 论文编号：1208
- 报告人：Kiet Anh Hoang
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/vo26_interspeech.pdf

## 问题
轻量 SER（如 TIM-Net 的 TAB）存在归一化不足、特征冗余与前后向等权相加等问题；大 SSL 模型精度高但 FLOPs 大，难上边缘设备，跨语料泛化也仍弱。

## 方法
SETEAB：Mel 频谱经 depthwise 卷积下采样（R=2/4）→ SE-Res2Block 做多尺度通道重标定 → 双向 TEAB 栈（LN、点扩、depthwise 时序、门控残差，膨胀 2^{i−1}，n=8）→ 全局可学方向权重 a/b 的加权双向融合 + 层级 λ_i 聚合。训练用 EmoBox 协议、Adam、label smoothing 与 SpecAugment 等增强。

## 实验与结果
语内：SETEAB(R=2) 平均 UA 47.69%，R=4 平均 F1 45.23%，均优于 TIM-Net/MS-SENet；参数约 0.4–0.5M、0.06–0.12 GFLOPs，远低于 wav2vec 2.0 base（95M/33.53G）。跨语料：12 组中 7 组最优，平均 WA 37.53%（高于 MS-SENet 34.31% 等）。消融显示 BiF、SE-Res2、DW-Sub、TEAB 均有贡献。

## 结论
作者认为 SETEAB 在精度、算力与跨语料稳健性间取得平衡，适合实用 SER。

## 点评
在 TIM-Net 族上做系统小改（门控残差+可学双向权重+深度可分下采样），工程收益清晰。跨语料方差偏大（±8.20），说明仍对某些训测对敏感；相对大 SSL 绝对精度未必全面领先，但效率优势突出。
