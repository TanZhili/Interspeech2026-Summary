# AdaptLingo: A Speech-to-Speech English Practice System with Fluency-Adaptive Responses

- 论文编号：3594
- 报告人：Zackary Rackauckas
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rackauckas26_interspeech.pdf

## 问题
静态英语口语练习对初学过难、对高阶过简；需按流利度调节词汇与语速。

## 方法
AdaptLingo：Praat 提发音率/语速 → 随机森林分初/中/高；CrisperWhisper 转写；按 EIKEN 词表检索并 logit 加权约束生成；gpt-4o-mini-tts 语速 0.8×/0.9×/1.0×。Gradio+FastAPI，含毒性过滤与学习日志。

## 实验与结果
标注集宏 F1 95%，用户研究噪声语音准确率仅 47%。被试内对比：日语母语者 19 项中 15 项偏爱 AdaptLingo；普通话与西班牙语母语者更多偏爱非自适应基线，但认可其“把我当英语学习者”。

## 结论
流利度自适应口语练习可行但非万能；需按母语背景与对话目标个性化。

## 点评
三件套（分类–词表–语速）演示完整；野外流利度估计是短板，且自适应有时牺牲自然度。
