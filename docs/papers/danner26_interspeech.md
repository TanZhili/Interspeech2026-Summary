# Vocal Tract Disparity and Potential Implications for Speaker Recognition

- 论文编号：2627
- 报告人：Valeriia Vyshnevetska
- 程序：Monday 28 September 2026 / Methods and data for vocal tract and articulation analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/danner26_interspeech.pdf

## 问题
人与机器对女性说话人识别常更差，即便训练数据性别平衡；原因不明。本文检验男性声道形态/发音形态差异（disparity）是否更大，从而可能产生更可分的声学签名。

## 方法
USC MRI 库：73 人静息态静态 MRI；子集 32 人 rtMRI 元音 /i,e,a,o,u/。几何形态计量（GPA+PCA），形态 disparity=组内 Procrustes 方差（控制质心大小等），置换检验性别差；按 landmark 可视化差异来源。

## 实验与结果
男性喉位更低、声道更长、质心大小约大 8.4%。合并发音数据上男性形状变异显著更大（\(p=0.006\)）；静息与单元音上趋势常同向但多不显著。男性在后元音等处发音幅度更大。差异热点多在舌根/咽等区域。

## 结论
男性更高形态/发音 disparity 可能贡献于识别优势；先天声道变异或可部分解释语音技术中的性别偏置。

## 点评
把“识别偏置”接到可量化的解剖变异，假说清晰。注意：未直接测声学/ASR 准确率与 disparity 的相关，仍是间接证据；样本与文化因素未控。
