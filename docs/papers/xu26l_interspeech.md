# Audio-Language Prompt Learning for Few-Shot Audio Classification

- 论文编号：1173
- 报告人：Qisheng Xu
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26l_interspeech.pdf

## 问题
少样本 ALM 适应以文本提示为主，音频侧欠适应，声学相近类别（如吉他/贝斯）可分性不足。

## 方法
MALP（PENGI 骨干）：音频/文本特异提示做残差适配 `(1−λ)f+λP`，再经共享提示拼接融合加强跨模态对齐；先模态特化再共享对齐。仅训提示，编码器冻结。

## 实验与结果
11 数据集 16-shot 平均准确率 78.35%，相对 CoOp/CoCoOp/PALM 分别 +7.21/+4.88/+1.77。CREMA-D、RAVDESS、NS-Instruments 等细粒度集增益更明显。消融：仅音频提示 77.33、仅共享 76.89，二者合用最佳。随 shot 数增加稳步上升。

## 结论
音频特异 + 共享提示的多模态提示学习可平衡模态内判别与跨模态对齐，改善少样本音频分类。

## 点评
与 ASPL 同类问题，但用嵌入残差+共享拼接而非声学早期调制；在 PALM 同套评测上平均更高。λ 与模板固定，跨骨干/零样本设定外推未充分展开。
