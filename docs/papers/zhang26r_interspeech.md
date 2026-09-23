# PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken Dialogue

- 论文编号：1214
- 报告人：Wen Zhang
- 程序：Tuesday 29 September 2026 / Empathetic Dialogue and Interaction Dynamics
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26r_interspeech.pdf

## 问题
级联 ASR→文本对话→TTS 会丢掉韵律共情线索；端到端语音模型又把情绪当隐式特征，可解释控制与外部知识接入不灵活。共情口语对话需要同时处理韵律感知、情绪推理、知识增强与语音生成。

## 方法
PRISM 拆成四智能体：Perceiver（Whisper 转写 + emotion2vec 情绪，并提取语速、停顿比、能量、填充词率与启发式确信分）；Manager 将数值韵律经规则标签再 few-shot 写成自然语言韵律描述，并对 Responder 输出做情绪/强度/策略一致性校验；Responder（在 TOOL-ED 上微调的 Qwen2.5-7B-Instruct 或 Llama-3.1-8B-Instruct）据转写、韵律描述与历史按需调用 COMET-BART 常识工具，生成回复文本及目标情绪 e 与强度 λ；Vocalizer 用 StyleTTS2，按 (e,λ) 与用户副语言属性两阶段设定音色相似度、韵律强度、扩散步数与表达缩放，并做文本侧停顿/标点与速率能量后处理。

## 实验与结果
在 AvaMERG 音频子集上，PRISM（Qwen/Llama）在 ROUGE、BERTScore、BLEU、Dist 上优于 ASR+LLM、SpeechGPT、SALMONN、OSUM-EChat、Qwen2.5-Omni-7B、LLaMA-Omni2、OpenS2S 等；如 PRISM (Qwen) ROUGE-1/2/L 为 0.2254/0.0745/0.1872。人工 6 维 Likert（ICC 0.81）与 GPT-4o A/B 评测也多优于 LLaMA-Omni2、OpenS2S。消融 Always Kno / w/o Kno / w/o Prosody-Desc 均下降，验证按需知识与韵律描述有效。

## 结论
多智能体解耦感知–推理–合成，配合韵律到语言翻译与可插拔知识工具，可提升共情、韵律适切与文本质量，且无需整网重训即可更新知识源。

## 点评
把韵律先“翻译成自然语言”再交给 LLM，是兼顾可解释性与工具调用的务实折中，避开端到端隐式情绪黑箱。代价是级联误差与规则/启发式确信分的脆弱性；优势主要体现在文本自动指标与主观维度，合成侧控制参数的可复现性依赖 StyleTTS2 调参细节。
