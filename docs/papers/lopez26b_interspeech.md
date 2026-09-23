# S-DiverSe: Spanish Diverse Speech

- 论文编号：2529
- 报告人：Fernando López
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/lopez26b_interspeech.pdf

## 问题
西语神经疾病语音（ALS、帕金森、卒中后构音障碍）公开野外基准稀缺，标准 ASR 在病理语音上仍脆弱，难以系统评估与适配。

## 方法
发布 S-DiverSe：22 名说话人、3.2 小时野外西语音频、444 段人工转写，含性别/病种/可懂度元数据（注释与视频链接公开）。评测 Whisper-large-v3、Voxtral-Mini、omniASR CTC 1B、ElevenLabs Scribe v2；并用 NeuroVoz/TORGO/Common Voice 做微调与启发式文本后处理（去重复幻觉）。

## 实验与结果
零样本总 WER：Scribe 20.69%、omniASR 33.56%、Whisper 36.43%、Voxtral 40.43%；WER 随可懂度下降而上升。启发式后处理显著降 WER（如 Whisper 36.43→22.01）。域外神经数据微调常损害 S-DiverSe（Whisper FFT 甚至 WER 飙升），作者认为后处理对域外神经西语更稳健。

## 结论
提供多病种野外西语 ASR 基准；对当前模型，规则后处理优于跨域微调。

## 点评
填补西语病理 ASR 数据空白，野外多样性是卖点。规模小、男性/ALS 偏斜、可懂度标注一致性仅 fair，且音频本身不直接分发，限制复现与训练用途。
