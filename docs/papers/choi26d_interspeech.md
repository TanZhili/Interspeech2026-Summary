# ProsoCodec: Prosody-Oriented Speech Codec for Voice Conversion

- 论文编号：2146
- 报告人：Jeongsoo Choi
- 程序：Tuesday 29 September 2026 / Controllable and Expressive Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26d_interspeech.pdf

## 问题
神经语音 codec 常把内容、说话人、韵律缠在一起，利于零样本克隆但不利于变声：变声需改音色、严保源内容与韵律。把韵律当独立可交换流往往丢掉说话人相关韵律细节。

## 方法
ProsoCodec：将韵律建模为条件残差——编码器/解码器以 ASR 文本与 SV 说话人嵌入作前缀，BSQ 离散瓶颈迫使 token 编码内容/说话人之外的韵律变化；编码器仅用低频 mel，解码器用全频 prompt。扩散 DiT 解码器 + 条件流匹配；训练交替随机 span mask 与同说话人双话语策略（prompt 与源不同句），减轻 prompt 风格泄漏。推理：源 token + 源文本 + 参考说话人/prompt。LibriTTS 585 h 训练，Vocos 合成。

## 实验与结果
合并 LibriTTS test + VCTK：ProsoCodec WER 4.451、SIMr 0.565、SIMs 0.167、f0 RMSE 0.428、P-MOS 3.852，整体优于 DDDM-VC、UniAudio、HierSpeech++、FACodec、Seed-VC、Vevo。消融：去掉双话语抬 RMSE；去文本条件 WER 暴涨；去说话人条件泄漏加重；全频 mel 略差。瓶颈约 12.5 Hz、4096 码本（150 bps）权衡较好；无 codec token 则退化为跟 prompt 韵律的零样本 TTS。

## 结论
文本/说话人前缀 + 离散瓶颈可学韵律残差，双话语与低频输入抑制风格泄漏，变声在内容、音色、韵律与自然度上更均衡。

## 点评
不走对抗解耦，而用“先验吃掉内容/音色、瓶颈只剩残差”的信息论思路，对变声更贴切。双话语训练直接打 prompt 抄袭；脆弱点是依赖外部 ASR/SV 质量，且码率过低会伤内容、过高又泄漏源音色。
