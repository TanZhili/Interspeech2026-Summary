# Diffusion Bridge Learning Between Overfitted and Underfitted Representations for speech emotion recognition

- 论文编号：2996
- 报告人：Shi-wook Lee
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26w_interspeech.pdf

## 问题
SSL 编码器在 SER 上易过拟合语料特异线索，跨语/跨域退化；训练早期表征更稳健但可分性弱，晚期更可分却过专，单检查点难以兼得。

## 方法
Diffusion Bridge Learning：从同一 HuBERT Large 骨干取晚期（过拟合）与早期（欠拟合）表征 A/B，定义类原型 μ；用条件去噪扩散在表征空间学习样本↔原型双向桥，配合配对对齐、循环一致、分类 CE 与 logit-pair KL 正则。推理可对 sample→prototype 翻译后分类。

## 实验与结果
英（IEMOCAP+MSP-IMPROV）↔日（JTES）交叉评估，指标 WAR。异质桥 overfit–underfit(B) 增益最大：英→日高权重 (λ_pair,λ_cycle)=(10,1) 时 +6.42 pp（45.32→51.74，p=0.0011）；日→英 +4.00 pp（35.74→39.74，p=0.0015）。同阶段桥增益较小；过拟合侧分类器较难被平滑改善。

## 结论
作者认为原型引导的扩散桥可重塑类中心几何、缓解过专方向，提升跨语稳健性；未来拟做直接跨域桥与更高效扩散日程。

## 点评
把“早/晚检查点互补”做成可训练的随机桥，视角新颖，跨语数字也扎实。依赖同一骨干不同阶段表征，部署需存双端点；增益主要落在欠拟合侧分类器，过拟合侧收益有限。
