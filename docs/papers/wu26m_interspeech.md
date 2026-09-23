# SEA-Spoof: Bridging the Gap in Multilingual Audio Deepfake Detection for South-East Asia

- 论文编号：3019
- 报告人：Jinyang Wu
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/wu26m_interspeech.pdf

## 问题

SEA 数字经济发展放大音频深度伪造风险，但主流反欺骗数据以英语等高资源语为主；MLAAD/SpeechFake 等对 SEA 覆盖稀疏或不成对，难做系统语言/系统级评测。泰语、越南语等声调语言与印地/泰米尔/马来/印尼等非声调语言的韵律差异，使高资源训练模型跨语迁移脆弱。

## 方法

发布 SEA-Spoof：覆盖 Tamil、Hindi、Thai、Indonesian、Malay、Vietnamese 六语，总约 711 小时，真假近 1:1，转录对齐配对。假语音来自 10 个开源（VITS-MMS、Edge-TTS、XTTS-v2、FastSpeech2、Indic-TTS、F5-TTS、Tacotron2 等）与 4 个闭源（HeyGen、ElevenLabs、MiniMax、ChatGPT-4o-mini-TTS）TTS/VC；真实来自 Common Voice、Indic、GigaSpeech2、马来会话与 YouTube、Thai Dialect、VIVOS 等。按语种与系统划分子集；8:1:1 分层切分。基准 AASIST、AASIST3、MoLEx，并在 SEA-Spoof 上微调 MoLEx。

## 实验与结果

高资源训练模型在 SEA-Spoof 上严重失配：如 MoLEx 在 ASVspoof5 EER 1.25% 但在 SEA-Spoof 达 43.8%。微调后 SEA-Spoof EER 降至 0.2%（ASVspoof5 略升，存在遗忘）。闭源假音比开源更难；语言上越南语相对易检，泰米尔/马来更难；系统上 ElevenLabs、ChatGPT-4o-mini-TTS 等更具挑战，HeyGen 相对易检。

## 结论

SEA-Spoof 填补区域语言空白，既作诊断基准暴露跨语/跨源失效，也可作微调资源显著恢复检测性能。未来拟扩方言与低资源语、接入新合成技术，并探索跨源适应与语言感知对策。

## 点评

典型“缺数据就建数据”贡献：用成对真假与开闭源并置，使跨语失败可归因到语言与合成源而非协议混乱。结果清楚表明英语基准高分不可外推到 SEA。脆弱点是微调后对原基准遗忘、部分语种开源模型覆盖不均，以及闭源系统随时间演进会使基准老化，需持续更新。
