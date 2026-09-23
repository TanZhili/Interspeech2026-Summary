# Controllable and Expressive Speech Synthesis
- 日期：Tuesday 29 September 2026 / 时间：09:00-11:00 / 形式：Oral（Area 7）/ 论文数：6
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本场围绕可控、表情化 TTS/VC：改进 Classifier-free Guidance 的无条件嵌入、Lombard/清晰度多级控制、跨语口音强度、粗到细韵律控制、韵律导向 codec，以及公开嗓音印象语料与防泄漏训练。共同瓶颈是细粒度表情/口音/印象控制常与说话人音色、文本语义纠缠，导致泄漏或不可解释的强度调节。

控制接口多样化：可学习 null embedding 与分模态无条件嵌入；声乐用力与清晰度伪标签 + 词级强调；口音子空间加权语言嵌入；音素对齐的音高/响度/时长；把韵律建模为相对文本与说话人条件的残差；以及数值嗓音印象（VI）的双话语解耦或无参考控制。公开 LibriTTS-VI 直接回应“无公开语料”障碍。

评价维度在说话人相似度、稳定性、表情、口音相似度、可懂度（含噪声中）与 VI 均方误差之间权衡；摘要强调更大 guidance scale 下的鲁棒性与数值控制相对提示式 TTS 的精确性。

## 技术内容

### 引导、清晰度/用力与口音强度控制

**Learnable Classifier-Free Guidance Null Embeddings for Enhanced Controllable Speech Synthesis**（论文 803；presenter：Biel Tura-Vecino）
CFG 常用固定 null 向量作无条件。改为可学习无条件嵌入，并可为各 TTS 条件模态学习不同无条件嵌入。主客观评价称在说话人相似度、稳定性与表情上优于固定 null，对更大 guidance scale 更稳，并展示说话人/文本引导的细粒度权衡。

**Synthesizing the Lombard Effect: Multi-Level Control of Speech Clarity and Vocal Effort in TTS**（论文 1159；presenter：Seymanur Akti）
用 flow-matching TTS 与声乐用力、清晰度伪标签，实现二者连续解耦控制，并支持词级强调。摘要称可改善清晰度相关声学特征，且噪声中言语实验显示可模拟人类清晰语音的可懂度增益。

**CrossAccent-TTS: Cross-Lingual Accent-Intensity Controllable Text-to-Speech via Disentangled Speaker and Accent Representations**（论文 1744；presenter：Nirmesh J. Shah）
面向跨语尤其 Indic 低资源场景的口音控制不足。Accent Intensity Controller 向口音子空间注入加权语言嵌入，推理时可插值口音并调节强度。摘要称在 Indic Multilingual 与 L2-arctic 上口音相似度与可控性优于强基线，并保持说话人相似与自然度。

### 细粒度韵律、韵律 codec 与嗓音印象语料

**CtrlSpeech: Coarse-to-Fine Control for Expressive Speech Synthesis**（论文 1760；presenter：David Harwath）
基于 DiTAR，结合全局说话人条件与音素对齐的音高、响度、时长，实现局部韵律控制并保音色。摘要称零样本 TTS 有竞争力，表情属性可控性提升。

**ProsoCodec: Prosody-Oriented Speech Codec for Voice Conversion**（论文 2146；presenter：Jeongsoo Choi）
整体 codec 纠缠内容、说话人与韵律，不利韵律保留/迁移。ProsoCodec 将韵律建模为条件残差：编解码以文本与说话人嵌入为前缀 token，离散瓶颈捕获二者无法解释的韵律变化，并用低频 mel 与同说话人成对话语训练。VC 实验称改善韵律保留并减少源音色泄漏。

**LibriTTS-VI: A Public Corpus and Novel Methods for Efficient Voice Impression Control**（论文 2231；presenter：Junki Ohmura）
发布基于 LibriTTSR 的公开 VI 语料 LibriTTS-VI；并提出双话语解耦训练（同说话人一句管说话人、一句管 VI）与仅靠目标 VI 的无参考控制，以减轻单参考导致的印象泄漏。摘要报告 11 维 VI 误差主客观下降，并对比提示式 TTS 的不精确数值控制与语义纠缠。

## 本场要点
- 可学习 CFG null（含分模态）提升可控合成对大 guidance 的稳健性。
- Lombard/清晰度控制把环境可懂度需求写入连续控制接口。
- 跨语口音强度控制依赖说话人–口音解耦与可插值子空间。
- 粗到细韵律信号使词/音素级表情调节更可行。
- 韵律导向 codec 用条件残差视角服务 VC 中的韵律保留。
- 公开 VI 语料与防泄漏训练直接针对数值印象控制的数据与纠缠问题。

## 覆盖核对
`803 | Learnable Classifier-Free Guidance Null Embeddings for Enhanced Controllable Speech Synthesis`
`1159 | Synthesizing the Lombard Effect: Multi-Level Control of Speech Clarity and Vocal Effort in TTS`
`1744 | CrossAccent-TTS: Cross-Lingual Accent-Intensity Controllable Text-to-Speech via Disentangled Speaker and Accent Representations`
`1760 | CtrlSpeech: Coarse-to-Fine Control for Expressive Speech Synthesis`
`2146 | ProsoCodec: Prosody-Oriented Speech Codec for Voice Conversion`
`2231 | LibriTTS-VI: A Public Corpus and Novel Methods for Efficient Voice Impression Control`
