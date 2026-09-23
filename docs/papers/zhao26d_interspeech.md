# Speech-Worthy Alignment for Japanese SpeechLLMs via Direct Preference Optimization

- 论文编号：976
- 报告人：Mengjie Zhao
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zhao26d_interspeech.pdf

## 问题

SpeechLLM 常继承书面体输出（markdown、列表、冗长复杂句），日语口语与书面在敬体、句末助词、句法复杂度上差距大，不利于 TTS 与听懂。尚无可靠日语 speech-worthy 评测资源。

## 方法

在 Whisper 编码器 + Sarashina-7B 架构上，预训练对齐模态后，用 DPO+SFT 偏好对齐：偏好口语化、不偏好书面体。偏好数据来自翻译后的 SpeechPref、InstructS2S-200K 滚动采样 + DeepDialogue。构建 SpokenElyza：过滤 ELYZA 中不适口语任务，风格改写并经母语者听测校验。评测用 LLM-as-judge 与词数/依存深度/不可发音字符比例。

## 实验与结果

SpokenElyza：预训练 2.91 → DPO+SFT+口语系统提示 3.44（约 +18%）；Elyza 书面评测从 3.97 微降至 3.78。表面形式：词数约 326→78，NV% 13.46%→3.24%，依存深度降至约 4.97。单独提示可大幅缩短，与偏好训练互补。

## 结论

作者认为偏好对齐可显著提升日语 SpeechLLM 的可听合成友好度，同时大体保留书面指令跟随；SpokenElyza 开源以支持后续研究。

## 点评

把“能听懂的回复”从文本 LLM 对齐迁到 SpeechLLM，并补日语基准，针对语体落差。依赖 LLM 改写与 LLM-as-judge，可能与真实听感不完全一致；书面分略降是风格权衡。偏好数据经翻译，日语特有礼貌策略是否充分覆盖仍待验证。
