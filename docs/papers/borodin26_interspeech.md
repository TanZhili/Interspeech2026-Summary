# Balalaika: Data-Centric, Prosody-Aware Annotation Pipeline for Russian Speech

- 论文编号：83
- 报告人：Vasiliy Kudryavtsev
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/borodin26_interspeech.pdf

## 问题
俄语网络语音难规模化标注：元音弱化、腭化、移动重音影响韵律与意义，现有管线多依赖人工或有声书、忽视韵律/音素细节，限制去噪与 TTS 等生成式语音任务。

## 方法
Balalaika 开源管线：SmartTurnV3.1 语义 VAD 切分（语音占比≥70%、内部静音≤1 s，块长约 5–15 s）；过滤短于 3 s、CREST>10、NISQA-S MOS<4.2、以及 pyannote 检出重叠/多说话人段落；五路 ASR（GigaAM-CTC±LM、GigaAM-RNNT、Vosk、T-one）经 ROVER 融合，保留 CTC+LM 词级时间戳；再以 RuPunctBig 补标点、RuAccent 加重音与 ё 归一、自训轻量 Transformer G2P 出 IPA。用该管线从多源俄语资源得到约 5,078 小时多层标注语料。在等预算下用 SEMamba 训去噪、VITS 训 TTS，并做重音/标点/MOS 阈值消融。

## 实验与结果
相对 11 个公开俄语语料，Balalaika 在 NISQA 各维、UTMOS、人工 MOS（约 4.601）与 TMR 上整体最优。等预算去噪中，在 Balalaika 上训练的 SEMamba 多数指标（含 CSIG/CBAK/COVL/PESQ/STOI/SI-SDR 等）领先。等预算 TTS 中客观质量与人工 MOS（约 3.618）最高、CER 约 0.1062，IntMOS 次于单说话人 RUSLAN；消融显示重音+标点联合最好，且 MOS>4.2 严过滤优于更松阈值。

## 结论
作者认为数据中心、韵律感知标注可产出更高质俄语语料并提升等预算下的去噪与 TTS；管线模块化但当前依赖俄语专用组件。局限包括等预算未训满收敛、TTS 测试集与部分源域部分重叠。

## 点评
抓的是“标注层（标点/重音/音素/时间戳）+ 质量过滤”如何改变下游生成质量，而不是新模型结构。等预算对比设计清楚，消融能支撑重音与标点的互补；脆弱点在语言相关工具链与测试域对齐，跨语种直接复用成本高。
