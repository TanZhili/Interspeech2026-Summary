# High-Quality Speech Synthesis for Under-Resourced Ethiopian Languages

- 论文编号：2658
- 报告人：Rahel Mekonen Tamiru
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tamiru26_interspeech.pdf

## 问题
阿姆哈拉语与阿凡奥罗莫语虽使用广泛，但缺少面向 TTS 的棚录语料；早期拼接/HMM 系统数据小、难处理非标准词与阿姆哈拉语叠音/同形异读。

## 方法
构建多说话人棚录语料：两语各约 100 h（各一男一女），阿姆哈拉另加 13 h 针对叠音与同形异读的句子，合计 113 h。文本清洗、数字展开、阿姆哈拉 Ge’ez→拉丁转写；微调 SpeechT5（英 LibriTTS 起点），用 512 维 x-vector 条件化多说话人。

## 实验与结果
数据从 50→100 h 降验证损失；阿姆哈拉加 13 h 后总体 MOS 由 4.12 升至 4.65。阿姆哈拉/奥罗莫总体 MOS 4.65 / 4.43（自然度、可懂度、发音分项见文内表）。推理依赖标准化输入，同形异读自动消歧留待前端。

## 结论
语言知情的大规模棚录数据 + SpeechT5/x-vector 可为低资源埃塞语言带来高自然度 TTS；语料拟在政策允许下公开。

## 点评
把“更多数据”具体化为同形异读/叠音靶向增广，对阿姆哈拉语收益直观。与早期系统对比主要靠 MOS 叙事；缺与 VITS/FastSpeech2 等同语料对照，跨模型结论仍待补。
