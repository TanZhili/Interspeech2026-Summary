# AuDirector: A Self-Reflective Closed-Loop Framework for Immersive Audio Storytelling

- 论文编号：1180
- 报告人：Wen Wu
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ren26d_interspeech.pdf

## 问题
长篇音频叙事需整合语音、音效与配乐，现有智能体系统常出现角色设定与声线不匹配、缺乏缺陷自纠、以及用户难用自然语言局部改稿。

## 方法
AuDirector 闭环多智能体：(1) 身份感知前期：Director 解析剧本与角色档案，Casting 用 EmbeddingGemma 粗检索 + Director 精选（320 条多样声库），并为每句生成 7 维情感指令；(2) 协同合成与校正：Acoustic 用 IndexTTS2 / TangoFlux / MusicGen 分层生成语音与非语音，Critic（MiMo-Audio、CLAP）打分，低于阈值则改情感指令/提示/种子并最多 \(N_{\max}\) 次重生成，Mix 混合；(3) 人机精修：Interaction 解析自然语言反馈，只对受影响脚本片段做定向再生。主 LLM 为 Gemini-3-Pro。

## 实验与结果
100 场景（40 播客 + 60 广播剧）对比 WavJourney、PodAgent 及无 Critic 变体。客观上 AuDirector 在 PQ、CE、VRM 领先（VRM 4.23）；主观 MOS-M/Emo/Ali/Aes 等整体最优或接近最优，Critic 带来除 MOS-Q/M 外的普遍增益。交互指令执行准确率平均 90%（增益控制 96%，结构编辑 84%）。作者指出非语音细粒度（如呼吸紧张度）仍受限。

## 结论
作者认为身份感知选角、闭环自纠与自然语言精修共同提升长篇音频故事的结构连贯、情感表现与声学保真，并支持人机协作。

## 点评
把“编排质量”与“单模型生成质量”拆开，在后端统一时用选角 + Critic 闭环解释 MOS-M/Emo 优势，评测设计较干净。系统工程性强，依赖外部 LLM/TTS/SFX 栈。脆弱点在重叠音效时的定位歧义（结构编辑 IEA 较低），以及环境声多样性不足仍会破坏沉浸感。
