# SDR-LLM: Speech-LLM Based End-to-End Speaker Diarization and Recognition with Sentence-Level Temporal Modeling

- 论文编号：2854
- 报告人：Renjie Yu
- 程序：Thursday 1 October 2026 / Speaker Diarization and Recognition
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/yu26g_interspeech.pdf

## 问题
级联 SDR 易误差累积；许多端到端方案只能粗粒度“谁说了什么”，缺毫秒级时间戳，且高精度标注对话数据稀缺。

## 方法
以 FireRedASR-LLM-L（Conformer + Qwen2-7B，约 8.3B）为骨干，并联 WavLM-Large（经 Seed-TTS-Eval 说话人下游初始化）并在时间维拼接。输出按 FIFO 序列化：`<|spk|>` + 起止时间戳 token（80ms 量化）+ 文本，重叠时先写完先开始的整句。两阶段训练：Stage1 用 AISHELL-1/3、LibriSpeech 构造三类模拟任务（时间感知、说话人区分、对话仿真，允许最多 1s 重叠）；Stage2 在 AISHELL-4、AliMeeting、OleSpeech 真实会议/播客上微调。说话人数上限 4。

## 实验与结果
AISHELL-4：CER/cpCER/DER = 12.78%/22.11%/11.83%，优于 SpeakerLM 与 Gemini-2.5-pro 转写，DER 接近 Pyannote 级联。AliMeeting：12.35%/29.51%/23.26%。OleSpeech：WER/cpWER/DER = 14.12%/28.14%/14.11%。消融显示 Stage1 对 DER/cp 指标有帮助。

## 结论
Speech-LLM 可在统一自回归格式下联合输出说话人、文本与句级时间戳；合成多任务预训练再少量真实微调可缓解标注稀缺，在转写精度上优于多数 E2E，分离性能接近级联。

## 点评
FIFO + 时间戳特殊 token 把重叠适配进 LLM 序列范式，工程上可复现。AliMeeting DER（23.26%）仍高于级联 Pyannote（约 20%），说明重叠与噪声会议仍是短板；抽取文本在训练细节处截断，硬件与步数仅见 Stage1 约 120k steps。
