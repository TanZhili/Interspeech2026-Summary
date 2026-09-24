# K-DIALECT : Korean Dialect-Aware Face-Based Speech Synthesis

- 论文编号：616
- 报告人：Seongyeon Yang
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/yang26d_interspeech.pdf

## 问题
韩语方言韵律差异大且资源少；多数 TTS 面向标准语，依赖参考音频在低资源方言上不现实；人脸条件 TTS 尚未系统建模方言韵律。

## 方法
K-DIALECT：双分支人脸编码器（ArcFace 身份 + CLIP 风格，拼接后融合 ℓ2 归一化）；方言条件 pitch predictor 输出与音素对齐的半音相对 f0 轨迹；FiLM 将 pitch 嵌入调制到声学隐状态。推理只需文本、人脸图与方言 ID；T5 Dialect Translator（42GB 韩语预训练 + 标准–方言并行微调）做词汇/语尾转换。多任务损失含 Ltxt、Lmel、对比/MSE/蒸馏/正交与 Lpitch。

## 实验与结果
AI Hub 韩语方言数据：六方言约 1511.55 分钟、2749 说话人；仅首尔子集有人脸，人脸编码器只在首尔训。对比 XTTS-v2：配对图声上 SECS 0.70（基线 0.79）、WER 0.25、MCD 14.66（优于基线）；方言韵律指标平均 F0-DTW-RMSE/G-SHAPE/MOD 等优于 XTTS。主观 30 人：Full 平均 MOS-F/N 3.96/3.90，显著高于无 pitch 与 XTTS；模态匹配 Rank-M 亦更好。

## 结论
人脸身份/风格解耦 + 方言 pitch 预测可在无参考音频下提升六种韩语方言的流利度与自然度；未来可建模方言内部变异。

## 点评
把「方言韵律」显式做成 f0 轨迹而非只靠方言 ID，对韩语句末边界调尤其对症。人脸只用首尔子集是硬约束，跨方言身份–方言组合的泛化仍依赖视觉条件可迁移这一假设。
