# Low-Resource Speech Synthesis

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：7
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场由一篇综述性邀请报告与四篇低资源 TTS 系统/资源工作组成。邀请报告梳理多语跨语迁移、无配对数据、无监督语音单元发现与基础模型如何把“大量转写语音”门槛大幅降低，并讨论真正低资源语言仍面临的语言多样性、合成质量与可靠评测问题。论文侧则覆盖印度语族轻量跨语说话人适配、曼尼普尔拉丁字母部落语言神经 TTS 资源、埃塞俄比亚阿姆哈拉语/阿凡奥罗莫语高质量 SpeechT5 系统，以及把英语 F5-TTS 基础模型适配 11 种印度语言的 IN-F5。

方法共性包括：极短参考（如 10 秒）适配、合成数据质控再微调、音素/字符统一标签集跨语共享音色，以及“从零训练 vs 直接微调 vs 持续高资源暴露”的受控比较。IN-F5 摘要明确挑战“多语系统必须持续暴露高资源数据”的假设。整体上，低资源 TTS 已从“有没有系统”转向“适配策略、数据质控与评测是否可靠”。

## 论文技术总结

# Low-Resource Speech Synthesis: What Have We Solved, and What Remains?

- 论文编号：
- 报告人：Sakriani Sakti
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
传统语音合成依赖大量转写语音，导致仅少数语言可用。低资源语音合成已大幅降低数据门槛，但仍需厘清哪些问题已解决、哪些对真正低资源/濒危语言仍然困难。

## 方法
报告综述推动进展的关键技术路线：多语言与跨语言迁移、利用未配对数据学习、无监督语音单元发现，以及更近期的基础模型。摘要指出如今可合成成百上千种语言，有时目标语言几乎无需转写语音。随后讨论仍存挑战（尤其对真正低资源语言）：语言多样性、合成质量与可靠评估，并结合原住民与濒危语言技术经验，讨论如何把合成进展与语言社群需求对齐。

## 实验与结果
摘要给出「可合成数百甚至上千种语言」的定性规模描述，但未提供具体系统名、评测集或 MOS/客观指标数值。

## 结论
数据门槛已显著下降，但真正低资源场景下的多样性、质量与评估仍是核心缺口；未来需更好连接技术进展与社群优先事项。

## 点评
框架是「已解决 / 仍困难」二分，适合作为低资源 TTS 的现状图。「数百/上千语言」来自摘要表述，缺少可核验评测细节。


# Lightweight Cross-Lingual Speaker Adaptation for Indic TTS

- 论文编号：2050
- 报告人：Tarun Kumar
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26e_interspeech.pdf

## 问题
印度语 TTS/克隆多依赖大模型；IN-F5 等虽相似好，但易丢词、推理慢，难低资源部署，且跨语种需额外录音。

## 方法
三阶段： (1) FastSpeech2+HiFi-GAN 多说话人预训练（约 119 h，印地/马拉地/泰米尔/泰卢固），CLS 统一音素，双位点 ECAPA-TDNN 说话人条件（韵律前 + 声学解码前）与余弦一致性损失；(2) 用 10 s 参考经 IN-F5 合成约 2 h，经音素 CER、音高、时长、log-likelihood 四级过滤得 2088 句；(3) 在过滤合成数据上微调说话人条件层。推理仅用非自回归 FS2。

## 实验与结果
相对 IN-F5：印地 WER 11.8%→9.6%，跨语平均相对降约 21.8%；SECS 0.87–0.88（略低于 IN-F5 的 0.89–0.91）；输出完全确定（\(\sigma_{F0}=\sigma_{syl}=0\)）；单句推理约 53× 更快、参数约 4.7× 更少。主观 MOS 全语种最高（印地 4.14），SMOS 与 IN-F5 接近。过滤以 CER 阶段剔除最多（5.3%）。

## 结论
10 s 参考 + 质量控制合成数据即可得到轻量、确定、跨语（CLS）的说话人适应 TTS，在可懂度与速度上优于克隆基线，相似可竞争。局限：单说话人演示，多说话人验证仍待做。

## 点评
把“慢且不稳的克隆教师”蒸馏成非自回归学生，四级过滤是落地关键。双位点条件与 CLS 支撑跨语一致。当前证据绑定一名印地男声与合成教师质量上限；SECS 受合成语料相似度天花板约束。


# Scalable Neural TTS for Latin-Script Low-Resource Languages of Manipur

- 论文编号：2304
- 报告人：Hoomexsun Pangsatabam
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/pangsatabam26_interspeech.pdf

## 问题
曼尼普尔邦多数部落语言使用改编拉丁文正字法，方言与拼写不统一，缺乏可用 TTS 语料；既有 Indic 资源几乎不覆盖 Tangkhul、Maring 等藏缅语。

## 方法
工作室教材/故事/圣经译本文本，单说话人棚录（各一名标准方言女声），经 VAD 切分（2–8 s）、22.05 kHz 重采样与 LUFS 响度归一，得到 Tangkhul 9.58 h、Maring 10.79 h。字符级训练 Tacotron 2 与 FastSpeech 2（ESPnet），声码器用 Griffin–Lim 或 StyleMelGAN。开放预处理管线。

## 实验与结果
StyleMelGAN 相对 Griffin–Lim 显著降 MCD；FastSpeech2+SM 总体更优（如 Tangkhul Blind MOS 3.06、Maring 3.51）。Maring 听感受方言差异影响大；Tangkhul 变音符字符化易致短时不可懂。英语预训练模型因忽略声调等差异无法替代。

## 结论
约 10 h 棚录语料即可为拉丁文低资源声调语言建立可用基线；同脚本不保证跨语迁移。未来拟共享音素空间与实时部署。

## 点评
资源与管线贡献大于模型创新，对“无原生文字”情境务实。方言听感与变音符建模暴露了字符级正字法的脆弱点；单说话人限制表达多样性。


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


# IN-F5: Adapting an English TTS Foundation Model for Multilingual and Zero-Resource Indian Speech Synthesis

- 论文编号：3366
- 报告人：Praveen Srinivasa Varadhan
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/varadhan26_interspeech.pdf

## 问题
英语大模型 TTS 已近人类水平，印度多语低资源场景难以从零复现；是否可用英语 F5-TTS 作先验，在严格数据预算下获得克隆、多语、语码混合等涌现能力，尚缺受控证据。

## 方法
扩展字符词表至 685 token（11 语原生脚本），比较三种策略：从零训 IN11、直接 EN→IN 微调、EN→EN+IN 混合微调。IN11 约 1417 h（IndicTTS/LIMMITS/Rasa/众包/IndicVoices-R）。再做 1/10/100 h 每语缩放；对无资源 Bhojpuri、Tulu 用相关脚本说话人合成 + 母语核验。

## 实验与结果
直接 EN→IN 总体 MUSHRA 最高（73.4），优于混合与从零（43.2）；见说话人自然度可与真人持平或略高。涌现：零样本克隆、跨语族 polyglot、语码混合与 Rasa 风格表达均较强。10 h/语已接近 100 h 多数能力；零资源 Bhojpuri 可达约 86 MUSHRA。相对既有 Indic TTS，IN-F5 MUSHRA 80.5（表 5 设定）。

## 结论
英语基础 TTS 经直接微调即可成为低资源印度多语先验，并支撑零资源跨语启动；不必持续混入英语数据。

## 点评
受控对比直接挑战“继续混高资源语更好”的直觉，实用性强。合成音有时高于真人，可能部分来自更干净、少瑕疵的生成偏置。语码混合在不自然语对上仍弱；从零失败也强调预训练不可替代。

