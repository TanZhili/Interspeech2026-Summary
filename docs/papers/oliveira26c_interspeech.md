# The TinyExplorer Ecosystem: Open tools for studying infants’ auditory and visual experiences

- 论文编号：3597
- 报告人：Cátia M Oliveira
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/oliveira26c_interspeech.pdf

## 问题
婴儿日常视听学习环境需 egocentric 头戴摄像，但缺轻量安全硬件，且人工标注视听耗时；长时音频工具难捕捉具身社交交互。

## 方法
开源 TinyExplorer：Gear 用 Insta360 GO 3（1080p/50 fps，水平约 80°、垂直约 116° 视场）采第一人称视频；Detection App 本地跑 AI 标注（敏感数据不上云）。已集成人脸检测（评测 13 种 DeepFace 算法，YOLOv11Face/RetinaFace 优）；手检测（100DOH 等）与 CDI 具体名词关键词 spotting（BabyHuBERT+Whisper）在扩展中。

## 实验与结果
关键词流水线相对人工标注 recall 78%、precision 77%，接近标注者间一致（均值约 82%）。人脸/手检测基准结果指向既有研究 [5,7]；完整多模态一体化仍在推进。

## 结论
硬件+本地 AI 生态旨在可扩展、可复现地研究儿童真实多模态输入；下一步融合姿态/物体与音频，形成“谁在说、做什么、说什么”的整合刻画。

## 点评
把头戴视场（尤其垂直）与本地隐私标注绑成生态，对语言习得具身研究很实用。强在开放与关键词近人类一致；弱在部分模块尚未完全集成进 App，工程成熟度仍演进中。
