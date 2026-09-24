# Do What I Say: A Spoken Prompt Dataset for Instruction-Following

- 论文编号：685
- 报告人：Maike Züfle
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/zufle26_interspeech.pdf

## 问题
SLLM 指令跟随评测多靠文本提示，难反映真实语音交互；现有口语指令基准多为 TTS、语种少、与任务输入绑死，难复用到任意下游集。

## 方法
发布 DOWIS：人工撰写并录音的平行文–语提示，与任务输入解耦，可挂任意基准。覆盖 9 任务（ASR、TTS、ST、MT、S2ST、语音/文本摘要、音频分章、SQA）、11 语种、每任务–语言 10 条提示（basic/formal/informal/detailed/short 各 2），总音频约 3h17m。在 Phi-4 Multimodal 与 Qwen2.5-Omni 上系统比较模态、风格与语言。

## 实验与结果
文本输出任务上文本提示显著优于口语提示；Phi 在口语 ASR 等上可出现灾难性失败。语音输出任务（TTS、S2ST）口语与文本接近甚至略优。低资源/跨语（如 cs、nl、sv 等）文语差距更大。非正式与短提示最难；男女说话人有任务依赖的小偏差。Whisper 转写显示提示可懂，差距主要来自模型跟口语指令能力。

## 结论
仅用文本提示会高估指令跟随；需多样口语提示评测。DOWIS 提供可复用的人工录音资源。

## 点评
把“提示模态”从任务数据中拆出，设计对社区很实用。当前仅两模型，且部分任务语言覆盖受限；录音设备杂但作者已用转写排除可懂度主因。
