# No-Shot Text-to-Speech: Limitations of Zero-Shot TTS and its Evaluation Methods in Representing Queer and Transgender Voices

- 论文编号：709
- 报告人：Juliana Francis
- 程序：Tuesday 29 September 2026 / Queer and Trans Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/francis26_interspeech.pdf

## 问题
性别扩展（GE）声音在训练数据中稀缺，零样本 TTS 克隆与自动评测是否对 GE 与非 GE（N-GE）表现不公，且自动指标是否与人听一致，尚不清楚。

## 方法
评测 CosyVoice2、E2TTS、F5TTS、XTTS、Zonos、LinaSpeech。N-GE 取 Globe（美式英语、男/女各半，共 14 人）；GE 取 MAGES（自我认同标签，14 人）。每人约 10 秒参考音，合成 15 句 Harvard sentences（16 kHz，-20 dB）。16 名听者做类 MUSHRA 相似度（0–100；每数据集 4 说话人×3 轮）。自动侧：ECAPA-TDNN / TitaNet-L / ReDimNet-M 说话人相似度、UTMOS 与微调 wav2vec2 的 AMOS、Whisper WER，并算 ICC。

## 实验与结果
人听：E2TTS、F5TTS、CosyVoice2 的 GE 相似度显著高于 N-GE；XTTS、LinaSpeech 则 GE 显著更差（效应量更大，如 LinaSpeech d=.704）；ZONOS 无显著差异。说话人相似度与 AMOS 在模型间常互相矛盾，且常与人听不一致（如 UTMOS 对所有模型都判 N-GE 更好；ZONOS 上三套嵌入结论互斥）。WER 仅 LinaSpeech 的 GE 显著更高。作者推测读语音训练与 spontaneity/EMILIA 类数据差异可能部分解释表现分裂。

## 结论
零样本 TTS 对 GE 的人听表现因模型而异，但自动评测管道存在盲区；需要更多代表数据与更贴合人听的指标，且建库须以社区参与、隐私与同意为先。

## 点评
同时打“合成偏置”和“评测器偏置”，对把嵌入相似度/AMOS 当 GE 公平性金标准的做法很有警示力。说话人仅各 14、人听子集更小，结论是方向性证据而非全面排行；Globe 的性别标签部分由分类器补全，也会污染 N-GE 对照。
