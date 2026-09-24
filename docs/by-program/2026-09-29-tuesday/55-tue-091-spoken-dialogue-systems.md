# Spoken Dialogue Systems

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：11
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖口语对话系统的交互质量建模、反馈通道时机、呼叫中心上下文 ASR、全双工视听生成，以及主动语音代理评测与噪声下系统输出语言复杂度。系统无关交互质量特征在端到端微调后可逼近系统依赖日志特征，提升跨系统可扩展评测。

反馈通道预测强调停顿邻近介入与语义适宜性：声学 alone 易过预测，需融合部分 ASR 假设；双路径模型则按快/慢功能类别分离时机。上下文侧区分“内部已感知历史”与“解码是否遵循”，并用上下文感知解码放大关键历史轮次；呼叫中心则用紧凑上下文投影器替代原始历史拼接。

## 论文技术总结

# A System-Agnostic Approach to Modelling Interaction Quality in Spoken Dialogue Systems

- 论文编号：1152
- 报告人：Paul Gering
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gering26_interspeech.pdf

## 问题
交互质量（IQ）分类以往多用系统日志等系统依赖（SD）特征，难以跨系统泛化。系统无关（SA）路线缺少声学线索验证；能否用声学+文本+时间特征替代日志特征。

## 方法
在 LEGO（公交电话对话，229 对话/5477 exchange，中位 IQ 1–5）上对比 SD 与 SA。SA：Silero VAD + Whisper 转写（人工校正）、eGeMAPS、HuBERT/WavLM/Wav2Vec2 池化、RoBERTa/SBERT/TOD-BERT 文本嵌入及话轮时长/延迟/重叠等。两阶段：静态冻结编码器 + LSTM；端到端微调编码器与后端。

## 实验与结果
调参 Macro-F1：静态 SD 0.557 vs SA 0.498；微调后 SD 0.593 vs SA 0.530。测试集最终：微调 SA MF1/UAR 0.454/0.453，接近 SD 0.462/0.471，优于多数类；相对 Ultes UAR 0.540，微调 SD UAR 0.471、SA 0.453。微调提升 SA 但计算与延迟更高。

## 结论
端到端微调时，声学–文本–时间 SA 特征可接近 SD 日志特征，成为可跨系统的 IQ 建模替代；静态管道下 SD 仍更优。

## 点评
把“可迁移评估”落到有音频的 LEGO 上，填补了先前纯文本 SA 工作。标签偏斜与电话噪声削弱声学嵌入；半自动转写校正使 SA 并非完全自动，作者也指出需更新语料与全自动流水线。


# Considerate Listener Modeling for Korean Streaming Backchannel Prediction

- 论文编号：1854
- 报告人：Yong-Seok Choi
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26c_interspeech.pdf

## 问题
流式附和（backchannel）若时机不当会打断说话；仅声学易在“需要回答的停顿”（问题/指令后）上过预测。需零 look-ahead、兼顾停顿邻近与语用合适性。

## 方法
Considerate Listener：块级共享声学编码器 + 停顿检测器对声学做 pause-aware soft scaling；ASR 部分假设经 Q-Former 交叉注意力融合；L_look-ahead=0。引入 Semantic FDR（预测 BC 落在 NOBC-PauseFP 的比例）。韩语咨询语料约 99h，块级 BC 仅 3.6%。

## 实验与结果
相对声学基线 (A) Macro-F1 66.77%：文本融合 (C) 69.14%、完整 (D) 68.93%（约 +2.16pp）。Semantic FDR：5.76%→(D) 3.07%，Semantic FP 相对降 53.8%。完整系统精度最高但召回略降，抑制集中在语用不当停顿。

## 结论
停顿软缩放 + 部分 ASR 文本融合可在零前瞻流式设定下提升 Macro-F1，并显著降低语用不当附和；Semantic FDR 比 Macro-F1 更能反映非打断目标。

## 点评
把“能不能插话”从声学停顿推进到话语行为约束，指标设计贴产品体验。私有咨询语料与人工 NOBC 标注限制复现；双条件联合时略过抑制，需在精度与召回间权衡。


# Context Projector: Complementary Keyword and Dialogue Context Embeddings for LLM-based ASR

- 论文编号：3326
- 报告人：Sergio Burdisso
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/villatorotello26_interspeech.pdf

## 问题
联络中心 ASR 既要整体 WER，也要业务实体（BWER）。把原始多轮上下文塞进 LLM-ASR 提示易变差且昂贵；需参数高效地注入压缩对话上下文与关键词。

## 方法
在冻结 SLAM-ASR（WavLM-Large + Llama 3.2 3B）上增加 context projector：Dialog2Flow 句嵌入经与 speech projector 同构的 MLP 变成紧凑上下文 token；Gemma3-27B 从历史抽关键词。只训 projector。DefinedAI 多域联络数据约 246h、约 3.8 万实体。

## 实验与结果
原始长上下文常抬高 WER；关键词 alone 改善 BWER 但可能伤 WER。keywords + context projector 改善 WER–BWER 权衡：相对基线平均相对降 WER 最高约 2.5%、BWER 约 7.2%，并提升实体 F1。近期短窗上下文通常足够。

## 结论
压缩动作感知上下文 + 关键词互补，是 LLM-ASR 在联络中心场景下实用的上下文增强，避免原始长提示退化。

## 点评
把“实体敏感”明确成 BWER，比只报 WER 更贴业务。冻结骨干只训投影器工程友好；关键词依赖大模型抽取，部署成本与错误会传导到 ASR。


# DP-BCT: A Dual-Path model for predicting BackChannel Timing

- 论文编号：3216
- 报告人：Jin Yea Jang
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jang26b_interspeech.pdf

## 问题
附和时机相对 Backchannel Opportunity Point（BOP）延迟因功能类别而异；单路径多任务可能因快/慢响应分布冲突而互相干扰。

## 方法
在 K-MIND（115h 韩语双人对话）上按 MUMIN 映射 CP/CPU/A/E，并用双过程理论把 CP 归为 fast、其余为 slow。BOP 定义为主说话人持续静音约 200ms。Cox PH 检验类别间 BOP-relative latency。DP-BCT 将 fast/slow 分到双路径做帧级 onset 与类别预测，对比单路径 SP-BCT。

## 实验与结果
Cox：slow 相对 CP 的 HR 0.71–0.85（均 p<.001）；均值延迟 CP 145ms，CPU/A/E 约 295–376ms。DP-BCT Macro-F1 0.6254 vs SP-BCT 0.4862（+0.1392，相对约 +28.6%）。

## 结论
功能类别确有不同 BOP 相对延迟；结构上拆开快/慢路径可显著提升附和时机与类别预测。

## 点评
用生存分析把“何时插话”量化，再把归纳偏置写进双路径，动机清晰。DPT 分组是解释性代理而非认知测量；静音定义的 BOP 可能漏掉非停顿型附和机会。


# From Awareness to Adherence: Bridging the Context Gap in Spoken Dialogue Systems via Context-Aware Decoding

- 论文编号：1589
- 报告人：Che Hyun Lee
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26m_interspeech.pdf

## 问题
多轮口语对话系统失败常被归因于“忘记历史”；作者指出还存在潜在上下文觉察与生成时主动遵从之间的鸿沟——内部认出关键历史，解码却被参数先验压过。

## 方法
音频适配的 Context-Aware Decoding（CAD）：用内部注意力定位关键历史轮次，推理时对比有/无该关键上下文的输出分布，放大上下文信号（无需额外训练或检索）。在层选择、token–turn–round 聚合与上下文范围上做消融。评测 Audio MultiChallenge 的 Semantic Memory 与 Self Coherence。

## 实验与结果
相对无 CAD：MiMo-Audio 平均 APR 26.01→34.11；Qwen3-Omni 25.78→39.08（Semantic Memory 22.67→39.33，绝对 +13.30pp）；Kimi-Audio 16.19→22.89。整段历史当 key 的 Whole History CAD 反而降至 21.04%，说明需精确选轮。

## 结论
多轮口语对话的上下文失败常是解码遵从问题；基于注意力的 CAD 可在推理期强制上下文忠实，显著提升记忆与自洽子任务。

## 点评
把“记得但没用上”形式化为 awareness–adherence 间隙，干预点放在解码而非再训，部署成本低。依赖注意力作为觉察代理、法官模型与公开榜不一致，绝对分需谨慎解读。


# From Reactive to Proactive: Assessing the Proactivity of Voice Agents via ProVoice-Bench

- 论文编号：1160
- 报告人：Yuhao Wang
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26k_interspeech.pdf

## 问题
现有语音智能体评测偏反应式问答，缺少对主动介入、条件触发与环境监测的系统基准。

## 方法
提出 ProVoice-Bench（1182 样本）：PIC 隐式意图并工具调用；LTM 潜伏话题监控；CFC 口头与数字上下文矛盾时纠错；ESS 用户定义环境声触发。多阶段 LLM+TTS+声学仿真合成，含数字应用状态。用 Rec/FPR/Acc 与 Response Accuracy 评开源 MLLM。

## 实验与结果
模型普遍过触发（尤其 LTM）；CoT/thinking 在 CFC/LTM/PIC 上明显提升。例：Qwen3-Omni(T) 总体 Acc 0.787、R_acc 0.759；Step-Audio-R1(T) Acc 0.793、R_acc 0.734。去掉数字上下文会显著伤害 CFC 召回与 PIC 准确率。决策是否说话与执行什么任务之间仍有落差。

## 结论
ProVoice-Bench 暴露当前 MLLM 在主动语音交互上的过触发与推理短板，并为数字上下文+音频的主动范式提供评测路线图。

## 点评
把“该不该插话、何时插话”拆成四类可测任务，填补反应式基准空白。合成数据与 TTS 场景可能低估真实噪声与多说话人复杂性；过触发现象本身说明校准比单纯放大模型更急迫。


# Integrating Facial Generation into Full-Duplex Spoken Dialogue Systems

- 论文编号：3114
- 报告人：Jingjing Jiang
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26g_interspeech.pdf

## 问题
全双工口语对话（如 Moshi）已支持低延迟重叠说话，但仍缺面部表情与头动；既有带脸系统多为轮替架构，无法同时处理/生成语音与面部。

## 方法
Moshi-Face：VQ-VAE face codec 把 VHAP 提取的 3D 头网格编成与音频同帧率（12.5 Hz）的离散 face tokens；Face Transformer 非自回归生成 N=8 face tokens，条件于 RQ-Transformer 隐状态与文本/音频嵌入。在 Seamless Interaction 约 180h 对话上两阶段训练（先冻 RQ 训 Face Transformer，再联合微调）。

## 实验与结果
Codec（K=256,C=128）重建较好。教师强制下 LSE-D/C 接近重建上界；自由双模型对话仍可流式。Moshi-Face free-run：UTMOS 1.75，LLM-as-Judge 总体约 3.76，与 Moshi/Moshi-ft 对话质量同量级；消融显示 Face Transformer 预训练与联合微调、以及 t−1 face 条件对同步与质量重要。

## 结论
首次把面部 token 生成接入全双工对话，实现低延迟音画对齐且不明显牺牲原音频对话质量。

## 点评
把脸做成与 Mimi 音频同构的离散流，是全双工多模态的自然扩展。自由运行下 LSE 与 UTMOS 仍有差距；依赖单目 3D 重建质量，真实摄像头噪声与遮挡未充分覆盖。


# Optimal Linguistic Complexity for Dialogue System Speech in Noise: Convergent Evidence from Automatic and Human Transcription

- 论文编号：2799
- 报告人：Lubos Marcinek
- 程序：Tuesday 29 September 2026 / Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/marcinek26b_interspeech.pdf

## 问题
嘈杂环境下对话系统合成回复应否“自适应简化”？对 ASR 与人类听者，最优语言复杂度仍缺系统证据。

## 方法
Study 1：250 句五级复杂度（电报式 L1 到复杂 L5），两 TTS×性别×12 DEMAND 噪声×7 SNR×两 ASR，共 168k 转写。Study 2 试点（N=15）：人类转写 L1/L3/L5×四噪声×三 SNR。控制词长、困惑度与韵律混淆。

## 实验与结果
ASR 与人类均呈 U 型：自然语法句（L3，约 9–16 词）优于电报式 L1——ASR WER 约优 43%，人类转录错误约优 45%；条件越好，语法优势反而更大。建议系统输出落在约 9–19 词的语法完整区间，拒绝“噪声越大越简化”。

## 结论
噪声下对话系统输出应保持自然语法完整句，而非电报式简化；ASR 与人类证据收敛。

## 点评
用大规模因子交叉把“该不该简化”钉成可检验结论，对 Listening Speaker 输出策略直接有用。人类侧仅 N=15 试点；复杂度由 LLM 改写+人工检查，真实交互中的语用简化未覆盖。

