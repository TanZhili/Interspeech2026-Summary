# CtrlSpeech: Coarse-to-Fine Control for Expressive Speech Synthesis

- 论文编号：1760
- 报告人：David Harwath
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zheng26c_interspeech.pdf

## 问题
零样本 TTS 自然度与音色克隆已强，但词/音素级细粒度表现力控制仍难：说话人、韵律、风格常纠缠，现有控制多在句级提示，无法对齐到局部音高、响度或时长并保持目标音色。

## 方法
CTRLSPEECH 基于 DiTAR：VAE 将 16 kHz 波形压成 40 Hz、64 维连续潜 token；按 patch（4 token）做因果 AR + 局部扩散（flow-matching）生成。粗控制：CampPlus 说话人嵌入与/或 prompt 语音；细控制：音素对齐的量化 pitch（WORLD→Mel→128 bins）、A 加权响度（64 bins）、强制对齐音素时长帧数，叠加到音素嵌入。约 2 万小时英文（Emilia+GigaSpeech）训 0.1B/0.6B；推理 CFG 32 步、scale 1.5。支持先粗生成再迭代改局部控制。

## 实验与结果
零样本：0.6B 在 LibriSpeech-PC WER 2.46%、SIM-o 0.65，Seed-TTS WER 2.58%、SIM-o 0.63，优于复现 DiTAR；SMOS 亦更好。说话人消融：嵌入+prompt 最佳。有控制信号时 LJSpeech 上 pitch RMSE 67.86→38.39 Hz、loudness 6.35→4.56 dB；音素时长 MAE 28.08→11.86。

## 结论
全局音色 + 音素对齐韵律信号可实现粗到细的可编辑表达合成，同时保持有竞争力的零样本质量。局限：主英文；依赖 pitch/对齐质量；纯文本仍难预测精确局部韵律；未显式建模情感等。

## 点评
抓住“可编辑局部韵律”而非再堆提示词，连续潜空间比离散 codec 更利于细微起伏。控制信号显式、可测（RMSE/MAE）是强项；工程上依赖对齐与提取器误差，且 UI 迭代流程对标注成本敏感。
