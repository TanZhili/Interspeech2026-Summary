# Learning Contextualized Tonal Contours from F0: A Core-Auxiliary Branched Transformer for Mandarin Tone Recognition

- 论文编号：1747
- 报告人：Yi-Fen Liu
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26n_interspeech.pdf

## 问题
普通话声调识别多依赖谱特征；为 CAPT/误发音诊断，希望仅用超音段 F0（及节奏）学上下文声调轮廓，并在推理时保持轻量。

## 方法
核心–辅助分支 Transformer：C-Net 对对数归一 F0 建音节/词/语块级嵌入与交替/内容标记，经多层自注意得轮廓表征；R-Net 用三段时长变异特征建模节奏。训练时辅助分支经 LSAP+交叉注意向核心回传梯度；推理丢弃辅助。损失为三分支交叉熵之和。数据 FCU-VOICE-360（360 说话人朗读）。

## 实验与结果
加词/语块粒度后核心 alone 准确率升至约 96%；辅以 C-Net 或 R-Net 可达 97.5%。v2-m3（Syl+Wrd+辅 R-Net）超单支 TNet-Full（97.2 vs 97.0），且推理延迟与参数更低。双辅助无额外增益。

## 结论
仅超音段信息即可高准确识别五声；可拆辅助分支提升训练稳健且不损推理效率，利于后续 L2 声调诊断迁移。

## 点评
用“训练加通路、推理减通路”把节奏上下文灌进 F0 轮廓学习，设计干净。数据为安静朗读，连读变调/自发语难度未充分覆盖；相对 MFCC 路线的优势在可解释超音段输入，而非绝对 SOTA 竞赛。
