# Phonikud: Overcoming Phonetic Underspecification for Hebrew Text-To-Speech

- 论文编号：604
- 报告人：Morris Alper
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kolani26_interspeech.pdf

## 问题

现代希伯来文书写常省略元音与重音等语音细节，即便加 nikud 仍有重音、shva、不规则词等歧义；现有 TTS/评测用无标音 ASR，对元音与重音错误“看不见”。

## 方法

Phonikud：冻结 DictaBERT 标音器，加轻量头预测增强符号（非末音节重音、发声 shva、不规则词标记），再规则转全规格 IPA。训练用 IsraParlTweet 半自动伪标签 + 人工校正高频词。发布约 2 h 双说话人 ILSpeech（音频–文本–专家 IPA）；训 Whisper-small 作 audio-to-IPA 评测 ASR。下游用 Phonikud IPA 微调 Piper/StyleTTS2。

## 实验与结果

G2P（ILSpeech 子集）：WER 17.4%、CER 3.8%，优于实时标音器与多语 G2P，接近 Gemini。TTS：StyleTTS2 WER/CER 35.2%/8.9%，优于开源基线，接近专有系统；CMOS 相对 Robo-Shaul 自然度 +1.3。重音难例：全方法 WER 3.2%、EM 77.0%，显著优于去重音与 Robo-Shaul。消融：去增强标音或元音均伤性能。

## 结论

作者认为补全语音欠规格说明后，小本地模型可接近大专有系统；框架、数据与评测基准开源。局限继承基座标音器错误与书面对白语体差异。

## 点评

同时修“生成前端”和“评测盲区”：没有 audio-to-IPA，希伯来 TTS 改进难以量化。轻量 adaptor 保留原标音能力再补缺口，工程干净。伪标签+人工校正可扩展，但对口语变体与基座错误仍敏感。
