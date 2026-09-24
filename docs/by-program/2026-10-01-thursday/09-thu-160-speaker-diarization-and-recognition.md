# Speaker Diarization and Recognition

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Long Oral
- Area：
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦说话人日志与识别（SDR）及说话人中心建模：从“单一嵌入难以通吃多任务”的综述视角，到 Speech-LLM 端到端联合预测说话人、文本与时间戳，再到边界紧致化、重叠语音的 shuffle 建模，以及语音语言模型流水线中的后门传播分析。

统一表示与任务自适应之间的张力贯穿综述与系统论文：嵌入在验证、日志、目标说话人提取与个性化交互中被不同方式利用，声学、内容、时长与域变化共同塑造鲁棒性。工程上，级联系统的误差累积与许多 E2E 模型缺乏细粒度时间对齐，推动 FIFO 式自回归输出与合成—微调两阶段数据策略。

日志边界与重叠处理是另一主线：对话 ASR 标注偏“松”导致模型复现松散边界；因果—反因果一致性可从松标注逼近紧边界。重叠方面，shuffle 积与偏序有限状态自动机在子词/词/短语层边缘化所有串行化，并直接建模（token, speaker）元组，支持单遍对齐。安全侧则提醒：SLM 作为异质组件系统，后门可跨组件传播，且毒化样本在共享多任务嵌入中未必可分。

## 论文技术总结

# One Embedding Doesn't Fit All: Rethinking Speaker Modeling Robustness Across Speaker-Centric Tasks

- 论文编号：
- 报告人：Shuai Wang
- 程序：Thursday 1 October 2026 / Speaker Diarization and Recognition
- 技术分类键：diarization
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
说话人嵌入已成为验证、日志化（diarization）、目标说话人提取与个性化交互等任务的基础表征；但为某一任务或声学条件优化的表征，未必能良好泛化到其他任务。需要从更广的、任务导向视角重新审视说话人建模中的「鲁棒性」。

## 方法
回顾在声学、语音内容、时长与领域变化下学习说话人表征的进展，并讨论下游任务如何以不同方式利用说话人信息。特别关注任务无关说话人表征与任务自适应建模之间的权衡，以及迈向更可泛化、可迁移、任务感知说话人建模的挑战与机遇。

## 实验与结果
调研型摘要，未给出具体评测集或 EER 等数字。

## 结论
「一个嵌入打天下」并不成立；鲁棒性应相对任务与条件定义，未来需要更可迁移且任务感知的说话人建模。

## 点评
论点直接挑战通用说话人嵌入假设，对多任务系统很有针对性。无定量证据细节，强度取决于报告中的案例。


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


# Where Do Backdoors Live? A Component-Level Analysis of Backdoor Propagation in Speech Language Models

- 论文编号：2813
- 报告人：Alexandrine Fortier
- 程序：Thursday 1 October 2026 / Speaker Diarization and Recognition
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/fortier26_interspeech.pdf

## 问题
Speech LM 由音频编码器、连接器与 LM 拼装而成，常被视为黑盒；音频后门能否跨模态传播、各组件角色如何、多任务共享嵌入中后门是否可分离，尚不清楚。

## 方法
基于可互换的 SpeechLLM 变体：WavLM Large（微调顶 15 层）、三层 CNN 连接器、TinyLlama-1.1B+LoRA。脏标签后门：220ms 打字机点击（0 dB SNR）；ASR 目标句需全时重复触发，其他任务单次触发。攻击 ASR/情感/性别/年龄；基线 AER 跨 WavLM/HuBERT/wav2vec/Whisper。组件分析：单冻结、单训练、传播三类设定，隔离编码器/连接器/LM。另在多任务嵌入上检验后门样本可分离性假设。

## 实验与结果
全管线攻击跨任务高 AER（如 WavLM：ASR 99.2、情感 93.7、性别 94.4、年龄 94.2），良性性能基本保持。隐藏任一组件不足以防护；仅编码器可独自撑起双任务后门。传播攻击中，仅“毒编码器 + 情感”能传入洁净管线（AER 63.5%）。正文还报告：多任务嵌入中毒样与良性样不可直接分离，过滤型防御的可分假设受挑战（抽取后段截断，细节不全）。

## 结论
SLM 对音频后门高度脆弱；后门存续/擦除强烈依赖被攻击组件，编码器最关键；插件式复用预训练组件存在现实威胁。多模态管线应作为有独特脆弱性的系统来防护。

## 点评
组件级消融把“谁在背锅”说清楚，对供应链式预训练复用有直接安全含义。情感任务比 ASR 更易单组件维持，可能因全局标签对局部触发更敏感。全文后半（嵌入分析/结论）抽取截断，可分性结论以摘要与已读章节为准。


# Tight Boundary Prediction in Speaker Diarization Using Causal-Anticausal Consistency

- 论文编号：45
- 报告人：Shota Horiguchi
- 程序：Thursday 1 October 2026 / Speaker Diarization and Recognition
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/horiguchi26_interspeech.pdf

## 问题
用多说话人 ASR 语料训 diarization 时，标注常把停顿与边界 padding 算进语音段，模型学会“松边界”；下游 GSS、对话数据构建等有时更需要紧边界，而强制对齐紧标注又依赖分轨录音、成本高。

## 方法
把紧标签视为真值、松标注视为弱监督。因果/反因果单向模型在松标签下仍难学前向 padding 或后向 pause-filling；对其后验取平均再阈值，与松标注做掩码得紧伪标签 Ytight = Ỹ ⊙ ϕτ((⃗P+⃖P)/2)。多说话人扩展：Basic（说话人对齐后逐说话人）、VAD（用 powerset 静音类抗说话人混淆）、SC（后验重分配纠正漏检/虚警）。过紧时若删超 50% 则恢复松段。并提出因果–反因果协同训练：逐步用输出收紧标签并更新参数；最终用紧伪标签训非因果 EEND（powerset，S≤4，至多两人重叠）。

## 实验与结果
摘要报告：相对理想紧标签训练，所提方法可恢复约 70% 的收紧效果，并改善下游表现。正文实验表与 DER 等具体数字在抽取全文中截断未完整出现。

## 结论
无需分轨强制对齐，仅用松 ASR 标注即可通过因果–反因果一致性构造更紧伪标签，使非因果 diarization 输出更紧并惠及下游。

## 点评
核心洞见是“松边界依赖未来/过去上下文”，用单向模型结构性禁止 padding/filling，再合成紧伪标签——比置信度去噪更贴问题本质。多说话人混淆时的 VAD/SC 变体说明简单平均不够。因全文抽取在方法中后段截断，实验数字仅能引用摘要中的约 70% 收紧恢复率。


# Modeling Overlapped Speech with Shuffles

- 论文编号：2462
- 报告人：Matthew Wiesner
- 程序：Thursday 1 October 2026 / Speaker Diarization and Recognition
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/wiesner26_interspeech.pdf

## 问题
重叠语音的说话人归属转写中，跨说话人 token 交错顺序未知；PIT 扩展差、SOT/tSOT 对时间对齐假设强，缺少在单通道重叠上做一次通过对齐的统一框架。

## 方法
用 shuffle 积 FSA 表示保留各说话人内部顺序的所有合法交错；在 CTC 前向中对 shuffle 图边缘化（shuffle loss）。用近似 token 起始时间（utterance 起止线性插值）加 collar κ 做偏序剪枝，κ→0 退化为 tSOT，κ→∞ 为全 shuffle，SOT 为说话人级全序特例。说话人归属：输出 (token, speaker) 元组，可用因式分解（类 SD-CTC）或直接联合 softmax。解码：1-pass 贪心元组 CTC，或 N-pass 目标说话人掩码后接标准 TLG。采用 compact selfless CTC 拓扑以控图规模。实现基于 k2/Icefall。

## 实验与结果
在合成 LibriSpeech 重叠上评估训练、解码与对齐（摘要声明）。正文实验表与具体 WER/cpWER 数字在抽取全文中于方法段截断，未能完整读到。

## 结论
Shuffle + 偏序约束为重叠多说话人 ASR 提供可统一看待 SOT/tSOT/SD-CTC 的形式化；Viterbi 路径可做单遍对齐，并支持说话人标记元组建模。框架原则上可扩展到 transducer/HMM 及其他交错过程。

## 点评
把并发交错写成可组合 FSA，理论清晰，且指出 tSOT/SOT/SD-CTC 是偏序特例，贡献偏框架性。图规模对说话人数敏感，偏序 collar 是关键工程旋钮。因抽取截断未见实验表，定量结论仅能依据摘要“在合成 LibriSpeech 重叠上评估”，具体数字从略并在此说明。

