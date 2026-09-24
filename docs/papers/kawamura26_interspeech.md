# PASQA: Pitch-Accent-Focused Speech Quality Assessment Model Trained on Synthetic Speech with Accent Errors

- 论文编号：1662
- 报告人：Masaya Kawamura
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kawamura26_interspeech.pdf

## 问题
常规 utterance 级自然度 MOS 预测对日语等语言的局部音高重音错误不敏感，而许多 TTS 又不暴露内部重音标签，难以专评重音正确性。

## 方法
用可控制重音的 TTS 生成受控日语重音错误语料，由错误率得到伪重音质量分。PASQA 基于 SSL，加入 mora 条件融合、排序损失、重音错误定位辅助任务与说话人不变训练。在见/未见说话人与人工主观评测上验证。

## 实验与结果
常规 MOS 模型排序准确率近随机、相关常近零或负；PASQA 在主观评测达 Order Acc 0.850、SRCC 0.828、KTAU 0.614。客观集上见/未见说话人均保持高排序准确；对 OOD TTS 输出亦有较好两两判别。

## 结论
显式建模重音错误可显著提升日语音高重音质量评估，并优于仅预测整体自然度的模型。

## 点评
把“听得懂重音”做成可训练目标，对日语 TTS 评测很切题。合成伪标签与真人口感可能仍有隙，但主观相关已明显拉开；思路可迁移到其他声调/重音语言。
