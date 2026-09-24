# Bagpiper-TTS: Natural Language Guided Universal Speech Synthesis

- 论文编号：873
- 报告人：Haoran Wang
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tian26_interspeech.pdf

## 问题
传统 TTS 依赖固定槽位式输入（文本+预定义元数据），与真实用户自然语言请求不匹配；多说话人对话、角色扮演、歌声等任务又难以在单一管线中灵活统一。

## 方法
Bagpiper-TTS 以 Bagpiper-Base（Qwen3-8B-Base + 50 Hz 多流 X-Codec，8 codes/帧，600B token 预训练）为骨干，采用 Planning–Caption–Generation：先文本规划理解意图，再生成长达数百 token 的 rich caption（转写+副语言/声学蓝图），最后据此合成语音。微调数据用六步仿真：音频精选→自动 caption→WER 过滤→LLM 反推用户请求→规划过程仿真→LLM 一致性校验（均分>3.5）。覆盖 classical / multi-talker / intent-to-speech / role-play / SVS / general-purpose，共约 738k 样本。推理对文本与语音用解耦 Top-k，语音侧 CFG λ=3。

## 实验与结果
SFT 2 epoch。Seed-TTS-Eval (En) classical WER 1.7%（Qwen3-TTS 1.5%，CosyVoice 2 2.6%）。四类进阶任务：LLM-as-a-judge 均分约 4.09，人工 MOS 均约 3.69；如 Multi-Talker WER 4.2 / TF 4.23，SVS WER 7.2 / TF 4.60（相对 YuE WER 11.0）。定性显示能处理倒序计数、委婉批评等需推理的请求。系统不接受参考音频，故未测 speaker similarity。

## 结论
以自然语言与 rich caption 为统一接口，单一模型可覆盖多种合成应用，classical TTS 可懂度接近前沿专用系统，进阶任务在裁判与主观评价上整体可用。

## 点评
核心是把“槽位控制”换成“可扩写的文本蓝图”，让预训练 caption↔speech 对齐直接承接任意用户话术。数据仿真与严格校验决定上限；general-purpose 子集试图覆盖未定义场景。脆弱点包括 caption 幻觉需 WER/多模态校验兜底、相对专用模型在部分主观分上仍有差距，以及无参考音色克隆能力。
