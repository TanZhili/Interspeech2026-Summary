# EchoLoc: Audio-Aware Object Grounding via Joint Heatmap and Box-Level Localization

- 论文编号：2320
- 报告人：Junghwa Shin
- 程序：Monday 28 September 2026 / Audio-Visual Grounding, Synchronization & Video Understanding
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/shin26b_interspeech.pdf

## 问题
音视频定位常只有模糊的相似度热图，难得到清晰目标框；带声源框标注的数据稀缺，而文本–图像 grounding 又对不完整/噪声文本敏感。需要在无显式框标注下，把音频线索接到目标级框预测并端到端训练。

## 方法
EchoLoc 基于 MDETR 式 query 检测器：ResNet-101 视觉 + 冻结 PANNs CNN14 音频。并行两支：(1) 热图支：像素级音视相似度，用空间/全局双向对比学习；(2) 框支：早期融合 Transformer 编解码器输出候选框。用热图 top-α 概率质量区域生成伪框，Hungarian 匹配后做音频条件分类 + L1/GIoU；总损失 L_spa+L_glob+L_box。不以伪框作硬唯一目标，而用多候选 + 最高音视相似度选择，缓解自举不稳定。

## 实验与结果
VGGSound→VGG-SS：cIoU 36.36、AUC 38.28。Flickr-SoundNet-144K→Test：固定阈值 cIoU 84.34；自适应指标 cIoU(adap) 88.22、AUC(adap) 79.99，相对 SOTA 相对提升约 +2.58% / +17.08%。消融：仅热图 cIoU 31.73，加框支升至 36.36。在多实例/模糊对应的 Flickr 上自适应收益更明显。

## 结论
作者认为热图软线索与 query 框预测联合训练，可在无框标注下实现更精细的声源目标定位，尤其利于模糊多目标场景。

## 点评
设计上正面处理“伪框自举悖论”：多候选 + 相似度选择而非硬回归伪框。固定阈值 AUC 不一定全面领先，说明标定敏感；强项在自适应评测与模糊场景。依赖热图质量与 α 阈值，音频编码器冻结也限制声学自适应上限。
