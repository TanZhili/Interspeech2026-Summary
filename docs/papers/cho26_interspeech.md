# Acoustic Prompting via Stage-wise Modulation for Few-Shot Learning in Audio Language Models

- 论文编号：885
- 报告人：Hyebin Cho
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cho26_interspeech.pdf

## 问题
少样本音频分类的提示学习几乎只调文本侧，音频编码器冻结导致域移与类内声学变异难以对齐。

## 方法
ASPL：在 CLAP-HTSAT 音频管道三阶段做共享仿射调制（γ⊙X+β）——log-mel 频谱、patch embedding、早期 Swin block；参数与类别数无关。作为即插模块与 CoOp/CoCoOp/PALM 文本提示联用，编码器冻结。

## 实验与结果
11 数据集 16-shot：CoOp 平均 73.56→ASPL* 75.54；CoCoOp 76.45→ASPL 77.85；PALM 77.86→ASPL* 79.26。与动态文本提示搭配时较轻的 ASPL 常更优；与静态/类提示搭配时加结构调制的 ASPL* 更好。参数开销极小，单数据集偶有波动。

## 结论
显式调制音频表征空间可与文本提示互补，形成双侧对齐，提升少样本适应。

## 点评
把“提示”从文本 token 扩展到声学管道早期仿射，参数效率高、即插即用。增益约 1% 量级且依赖基线；CREMA-D 等上不稳定，说明频谱级调制对情感类任务未必总利。
