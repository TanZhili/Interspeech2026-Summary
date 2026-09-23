# Automatic generation of audio comic from manga images

- 论文编号：3577
- 报告人：Sota Koshino
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koshino26_interspeech.pdf

## 问题
有声漫画需为角色配适合剧情的表情语音，人工成本高；希望从漫画页图像（半）自动生成对应朗读/演技语音，兼顾制作降本与视障可及。

## 方法
流水线：检测分镜/文字/角色 → OCR → 阅读顺序 → 人脸与预存姓名–人脸库匹配并关联说话人，产出 XML；VLM（GPT-5.2）据文本上下文、脸与分镜图预测八类情绪，组成 “角色名's voice is Emotion with very clear audio” 提示；ParlerTTS 在约 9 小时 MangaVox 日语有声漫画数据上微调后按行合成。检测理解对比 Magiv2+Yomitoku（v1）与 Magiv3+MangaOCR（v2）。

## 实验与结果
约 700 页/8 部 Manga109+MangaVox 测试：v2 在面板/文本/角色检测、身份、说话人关联、TOER、CER 全面优于 v1，故采用 v2。主观：150 人、五分制整体印象；GT 真人约 4.0，v2+TTS 与 manual+TTS 均约 2.5，自动与半自动接近，但仍低于真人。

## 结论
自动检测–理解–提示 TTS 可生成一定质量的有声漫画，瓶颈更在 TTS 表现力而非理解流水线。未来改进提示设计与角色音色合成。

## 点评
把漫画理解与风格化 TTS 串成可演示闭环，客观任务齐全。主观上自动≈人工校正说明前端够用，差距主要在演技合成；情绪仅八类离散标签、依赖角色脸库，跨风格/无脸分镜时可能脆弱。
