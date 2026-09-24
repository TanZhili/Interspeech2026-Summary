# Empathetic Dialogue and Interaction Dynamics

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：11
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕共情式口语对话与互动动态展开：一方面用语音大模型（speech LLM）生成情感对齐的回复，另一方面从双人协作对话中估计认知负荷等交互状态。共同点是强调“听到什么情绪/状态”与“如何以合适韵律与语义回应”的闭环，而不仅是文本层面的礼貌或共情措辞。

在生成侧，工作从“会不会识别情绪”推进到“回复情绪方向是否正确”（情绪共识），以及在有限数据、可控计算预算下仍能理解用户语音中的情感线索。多代理框架则把感知、推理与合成解耦，并用韵律到语言的桥接稳住大模型推理，同时按需调用外部知识。

在交互分析侧，研究从受控实验室转向自然协作对话，关注轮替、重叠、参与不平衡等交互动力学特征与时间压力、心理负荷等主观维度的关联。整体趋势是：共情能力的评测与训练目标更细（方向正确性、韵律适宜性），系统架构更模块化（对比式思维链、多代理、数据管线），并对真实对话中的认知状态建模提出需求。

Survey Talk 时段（40 分钟）题目尚未公布，本摘要不对其内容作推测。

## 论文技术总结

# To be announced (Survey Talk, 40 mins)

- 论文编号：
- 报告人：
- 程序：Tuesday 29 September 2026 / Empathetic Dialogue and Interaction Dynamics
- 技术分类键：dialogue
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
官方程序未提供摘要。仅能从标题与会场信息判断主题方向：「To be announced (Survey Talk, 40 mins)」，安排在「Tuesday 29 September 2026 / Empathetic Dialogue and Interaction Dynamics」。

## 方法
官方程序无摘要，无法概括具体方法、模型结构或训练流程；此处不作推断。

## 实验与结果
官方程序无摘要，未给出数据集、对比设置或定量结果。

## 结论
官方程序无摘要，无法归纳作者结论与适用边界。

## 点评
该条目目前只有标题与程序位置可参考，后续若有讲义、幻灯片或正式论文，再据此补充问题设定、方法细节与可核验结果。


# CE-CoT: A Contrastive Empathetic Chain-of-Thought Training Strategy for Improving Emotion Consensus in Empathetic Speech LLMs

- 论文编号：1271
- 报告人：Jing-Han Chen
- 程序：Tuesday 29 September 2026 / Empathetic Dialogue and Interaction Dynamics
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/chen26o_interspeech.pdf

## 问题
共情语音 LLM 常用 SER 准确率、Emotional Reaction（ER）、Exploration（Ex）等指标，但它们不保证回复情绪方向与用户一致。Emotion Consensus（EC）衡量这种方向正确性，在语音 LLM 中仍少被显式建模；仅靠识别正确情绪并不能保证回复共情对齐。

## 方法
提出 Contrastive Empathetic Chain-of-Thought（CE-CoT）：把目标回复拆成情绪识别 e、忽略情绪的中性回复 r_neu、再经情感反应与探索性提问修订的 r_rev，形成隐式对比（r−=r_neu，r+=r_rev）。训练两步：(1) 用文本 LLM（Qwen-7B-Chat）结合转写与含真值情绪的 CE-CoT prompt 生成期望 CoT 回复 R；(2) 语音 LLM 仅见语音与不含真值情绪的同一 prompt，用 KL 散度对齐到 R。推理沿用同一结构。EC 由 LLM 裁判（Gemini Flash 2.0）判断 r_rev 主情绪是否匹配标签。

## 实验与结果
在 IEMOCAP、ESD（英）、MSP-Podcast 子集、MESC 上评估 BLSP-Emo、RE-LLM、Qwen2Audio。预训练通用模型多数 EC 低于 0.5；vanilla 行为对齐增益有限或不稳。CE-CoT 对齐相对预训练/vanilla 在多数据集显著提升，例如 BLSP-Emo 在 MSP-Podcast 上相对 vanilla 约 +19.1%，在 MESC 上相对预训练约 +35.2%。条件评估中，CE-CoT 使因 EC 失败而清零的 ER/Ex 掉幅约减半。案例显示 vanilla 易把开心用户回成悲伤，CE-CoT 可对齐。局限：单轮、未深挖内部推理与 EC 度量变体。

## 结论
结构化对比式 CoT 对齐可提升共情语音 LLM 的情绪一致性，超越表面模仿式微调；作者认为这为多轮与更细 EC 度量奠定基础。

## 点评
把“识别对了却回错情绪”拆成可监督的中性 vs 修订对比链，训练目标直接对准 EC，比只追 ER/Ex 更对准部署风险。依赖文本 LLM 造监督与 LLM 裁判 EC，增益对裁判与 prompt 敏感；单轮设定下尚未检验多轮情绪漂移时对比结构是否仍稳。


# Empathy Omni: Enabling Empathetic Speech Response Generation Through Large Language Models

- 论文编号：984
- 报告人：Guangyan Zhang
- 程序：Tuesday 29 September 2026 / Empathetic Dialogue and Interaction Dynamics
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/wang26q_interspeech.pdf

## 问题
端到端语音 LLM 常把回复内容再合成语音，对用户副语言情绪利用不足；同类共情系统又依赖海量情绪对话与大规模训练。需要在数据与算力受限下显式感知情绪并生成共情口语回复。

## 方法
Empathy Omni 为双塔结构：冻结 Whisper large-v3（语义）与 emotion2vec（情绪）编码，经帧堆叠 MLP 下采样到 10 Hz 后融合送入 LLM（Qwen2.5-7B-Instruct + LoRA）。LLM 同步输出文本 token 与 token 级情绪轨迹；用 DTW 将目标波形的帧级情绪特征对齐到 token，联合 CE + MSE/余弦损失监督。语音解码器（6 层因果 Transformer）用门控融合 token 嵌入与 LLM 隐状态，经 AdaLN 注入情绪轨迹，预测 CosyVoice2 声学 token 再流式合成。两阶段训练：先对齐理解与文本共情，再训解码器。配套构建 EmotionalQA-200k（合成+ESD 改写+真实录音，约 135k/15k/50k），并与 VoiceAssistant-400k 联训。

## 实验与结果
VoiceBench 上综合竞争力强：CommonEval 3.47、IFEval 27.89 最佳，UTMOS 4.41 最高；Alpaca/WildVoice 接近 GLM-4-Voice。自建 1k 情绪查询集上 Emotion GPT Score 3.97、Speech Emotion MOS 4.23、ASR-WER 表中为 4.61，优于 OpenS2S 等。消融去掉融合模块后 GPT 分 3.97→3.15、MOS 4.23→3.85、WER 升至 6.42。作者称对悲伤/恐惧等需持续韵律塑造的情绪较有效，细微/混合情绪仍偏泛化。

## 结论
显式 token 同步情绪规划加可扩展合成数据管线，可在无需大规模共情预训练的情况下同时提升指令跟随、音质与共情表达；细粒度情绪与强度控制仍是开放问题。

## 点评
把语义生成与情感轨迹解耦，再用 AdaLN 条件合成，比“隐式从数据学共情”更可控，也解释了音质与共情分同升。DTW 对齐避开非言语发声上的强制对齐失败，设计贴合情绪语音。评测依赖 GPT-4o 与 ASR-WER，且 EmotionalQA 大量合成，真实分布外的细微情绪仍可能是短板。


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


# Predicting Cognitive Load from Speech and Interaction Dynamics in Dyadic Conversations

- 论文编号：3052
- 报告人：Tahiya Chowdhury
- 程序：Tuesday 29 September 2026 / Empathetic Dialogue and Interaction Dynamics
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/chowdhury26_interspeech.pdf

## 问题
语音认知负荷研究多在受控单任务、离散分类设定下进行，随机划分易高估泛化；双人协作中轮换、重叠等交互动态与连续 NASA-TLX 负荷的关系仍不清楚。

## 方法
基于 AVCAffe 远程协作数据（53 对、最多 9 任务、106 人），按任务切 30s 窗，Silero VAD 过滤弱语音窗。特征分三组：OpenSMILE eGeMAPSv02 静态声学（88 维）、一阶差分时间动态（88 维）、仅用计时的交互特征（说话占比、重叠/静音窗比例、话轮切换等）。以共享 GRU 编码双人序列、均值池化后双回归头预测个体 NASA-TLX（0–21），联合 MSE；对照为任务级聚合特征上的 Random Forest。评估用 Leave-One-Dyad-Out，主指标 CCC，辅以 PCC、RMSE。

## 实验与结果
静态声学 GRU：时间需求 dyad CCC 0.42 最稳；心理需求个体不对称（A 约 0.31，B 约 0.13）；努力/绩效有弱信号；挫折/体力接近无效。GRU 对时间需求优于 RF（约 0.41 vs 0.33），但 Wilcoxon 校正后与 RF 差异不显著。交互特征 alone 将时间需求 CCC 提至 0.51；A+I 使四维负荷均提升（心理 0.22→0.32 等）。置换重要性：时间需求关联重叠与话轮切换；心理需求关联说话时间不平衡。对间 CCC 异质性大（部分 0.6–0.9，亦有负相关）。

## 结论
双人对话语音可对时间/心理等负荷做适度、可跨对泛化的回归；交互动态提供互补信号，但可能混入任务结构效应，且样本量限制了带注意力序列模型收益。

## 点评
把问题从“分类高/低负荷”改成跨对回归，并显式拆开声学 vs 交互，方向对自然协作场景更诚实。最强信号来自 10 维交互特征，说明“测的是负荷还是任务诱发的轮替模式”仍需拆解；小样本 LODO 下 GRU 未显著碾压 RF，模型复杂度应服务于可解释特征而非堆砌。

