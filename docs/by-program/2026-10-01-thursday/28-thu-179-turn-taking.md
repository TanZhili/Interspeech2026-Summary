# Turn-taking

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：11
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场把话轮转换从“静音超时/二元边界检测”推进到角色条件、前瞻预测、双通道生成预训练、以及模态消融下的信号贡献分析。生产级 ASR–LLM–TTS 流水线虽具备工具调用与推理能力，却常因静音启发式导致不自然打断；端到端语音模型更自然但工具链受限——多篇工作试图弥合这一鸿沟。

趋势一是把话轮建模为结构化决策或多动作输出（含基准 CoDeTT），覆盖场景与上下文变化。趋势二是前瞻：提前数秒预测终点或话轮边界，以投机执行 LLM/TTS 换延迟。趋势三是从运动学预发言线索与声学–韵律–语义消融理解“何为驱动因素”，摘要侧证据偏向韵律与静音胜过语义完备性。

## 论文技术总结

# Adaptive Turn-Taking for Real-time Multi-Party Voice Agents

- 论文编号：2493
- 报告人：Soumyajit Mitra
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/mitra26_interspeech.pdf

## 问题
多人语音对话中轮次竞争、重叠与动态 floor 分配使二元静音/句末启发式失效；用户对代理期望从被动听者到主动主持各异，但角色对实时 turn-taking 的影响少被建模。

## 方法
提出 **ModeratorLM**：语音编码器 + LLM，块式流式追加声学嵌入与带说话人标注转写；每块输出「抢轮+回复」控制 token 或空序列（不抢）。**ModeratorLM-Think** 在决策前加 chain-of-thought。构建合成口语多人语料 **RolePlayConv**（约 75k 对话、125 种助手角色，Nova Pro 生成文本 + Zonos TTS）。三阶段训练：ASR 对齐投影 → AMI/Fisher 对话预训练（轮换助手）→ RolePlayConv 角色条件微调（LoRA）。

## 实验与结果
真实会议 NOTSOFAR-1 与 RolePlayConv 零样本角色测试。相对 Moshi、无角色 MP-Baseline：ModeratorLM-Think 在 NSF-1 上 P/R/F1 达 0.81/0.74/0.76，FP 仅 0.01；RolePlayConv F1 0.79。文称相对非角色基线 precision 提升超 40%、recall 超 70%，并大幅降误打断。LLM-as-judge 角色保真更高。消融：无转写性能崩；ASR 假设仅轻微下降；Think 变体对切块策略更稳健，但固定切块评估有伪增益风险。

## 结论
显式角色条件可显著改善多人语音代理的 turn-taking 与回复一致性；推理轨迹进一步抬升召回并降低反应性漏接。

## 点评
把「何时开口」绑到角色义务，切中多人代理与二元对话代理的差异。强在真实会议+合成角色双评与 Think 消融；脆弱点在大量合成数据、评测依赖 teacher-force 与动态切块，以及 NSF-1 助手角色由 LLM/人工事后指定，与真实助手行为仍有差距。


# Before the Turn: Investigating Motion Cues Preceding Speech in Dyadic Interaction

- 论文编号：1243
- 报告人：Ying-Hsuan Huang
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/huang26d_interspeech.pdf

## 问题
计算 turn-taking 多作反应式声学边界检测，滞后于人类意图；已有视觉特征多是离散标签或统计量，未量化全身连续运动学，也未考察不同身体部位是否具有不同的预言语运动起始时间线。

## 方法
在 InterAct 3D 骨架（8.3h、241 二元场景）上定义 Shift/Hold 与有无停顿四类情形；提取部位角速度与运动多样性（FullBody/UpperBody/Hands/Head），说话人 Z-score 归一化，在上下文有界窗口内检测 \(\hat{V}_t>2\) 的最早 onset。用 Transformer 系统变化观察窗 \(W_L\) 与预测超前 \(\tau\in\{0,0.5,1.0,1.5\}\)s，比较各部位对 Shift vs Hold 的预测力。

## 实验与结果
约 30–35% 转换有明显预备动作；远端（手/头）常在发声前 0.5–0.6s 激活，UpperBody 峰值可早至约 2.9s。UpperBody 在 \(W_{0.5}\) 上 F1-Shift 达 76.81%，长窗仍稳；Head 随窗加长因点头等倾听噪声而崩。超前 \(\tau=1.5\) 时 Shift 预测可优于 \(\tau=0\)；Floor-claiming（尤其重叠 Case C）体现约 1.5s 运动多样性累积，Floor-holding 则在发声碰撞点爆发。静默间隙（Case B）头部位有短时协商信号。

## 结论
交际意图在发声前就以异步多模态运动编码：上半身提供最长稳定超前，远端给短窗同步；抢轮与守轮的运动时间线本质不同，支持「主动 turn-taking 协商」视角。

## 点评
把问题从「加视觉特征」转到「量化部位特异的预言语时间学」，证据链（onset 统计→观察窗→超前预测→运动学验证）清晰。强在生物力学可读性；局限是二元、半结构化、被试少，且预测器非端到端部署系统，外推到多人/实时代理需谨慎。


# CoDeTT: A Context-Aware Decision Benchmark for Turn-Taking Evaluation

- 论文编号：974
- 报告人：Huan Shen
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/shen26_interspeech.pdf

## 问题
Turn-taking 评测常停留在二元句末/是否开口，交互场景窄，难以比较模型或诊断「动作对了但意图错了」的失败；现有全双工基准多把决策当黑盒。

## 方法
提出 **CoDeTT** 上下文感知决策基准：在系统状态（Speaking/Idle）下映射到四类宏观动作（Maintain、Stop & Listen、Takeover、Dismiss），再细分为 14 种场景（backchannel、打断、未完成犹豫、旁听、第三方协作等）。约 300 小时中英多轮数据、18k 标注实例，每条含五轮历史；合成（Gemini/Qwen-TTS）+ 真实（Candor、MagicData-RAMC）混合，经 ASR 校验与声景仿真。两阶段漏斗评测：先统一四动作，再对 Omni-SLM 做 14 类意图；引入 **Semantic Misalignment Rate (SMR)** 量化「动作正确但意图错误」。

## 实验与结果
专用控制器在 Takeover 高、Maintain/Dismiss 弱。Omni-SLM（Qwen3-Omni、MiniCPM-o、GPT-4o-audio、Gemini3-Pro）动作更均衡，但 SMR 暴露差距：Gemini3-Pro SMR 约 15–25% 最低；MiniCPM 在部分策略 SMR 常 >40%（「幸运猜对」）。历史长度非单调：适度历史降 Incomplete/Completion 的 SMR，过长（H=5）在打断类易过承诺、损敏捷性。说话人角色归因（Collaboration/Exclusion）仍是瓶颈。

## 结论
CoDeTT 把 turn-taking 评测从计时任务升级为可诊断决策问题；SMR 显示功能成功常掩盖弱语用 grounding，并揭示上下文连贯性与交互敏捷性的权衡。

## 点评
贡献是评测协议与诊断指标，而非新模型。SMR 和 14 类分层对全双工系统很有用。需注意大量合成数据与自动标注链路可能引入分布偏置；专用控制器因无意图输出无法报 SMR，跨范式对比仍主要在动作层。


# DualTurn: Learning Turn-Taking from Dual-Channel Generative Speech Pretraining

- 论文编号：2424
- 报告人：Shangeth Rajaa
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rajaa26_interspeech.pdf

## 问题
生产级 ASR–LLM–TTS 流水线有工具调用与推理能力，但轮次切换仍依赖静音超时，延迟高且易打断；语音到语音（S2S）模型能隐式学到轮次动态，却难把能力迁移到模块化流水线。现有端点/VAP 多为单通道或把现象坍缩成二值语音活动，无法区分 backchannel、打断与真正 turn end。

## 方法
DualTurn 用冻结 Mimi codec 编码双通道 24 kHz 音频（连续 512 维嵌入，12.5 Hz），经通道 MLP 拼接后接入 Qwen2.5-0.5B。Stage-1 在约 453 h 对话音频上做双通道下一帧生成式预训练（深度预测器随后丢弃）；Stage-2 在每通道挂 6 个分类头，自监督从 VAD 对齐得到 EOT、HOLD、BOT、BC、VAD、FVAD 标签（4 s 前瞻），稀疏信号用 focal loss。信号可用启发式或多项式 logistic regression 映射为五类 agent action（ST/CL/SL/CT/BC）。推理步长 240 ms，CPU 约 78 ms。

## 实验与结果
预训练数据含 otoSpeech（289 h）与 Switchboard（220 h，138 session 测试集留出）。Switchboard 上 DualTurn（LoRA）agent action wF1 0.633，高于 VAP（LR-6）的 0.389；BC F1 0.349 vs VAP 的 0.000。词级 turn 预测 AUC 平均 0.930（启发式）/0.963（LR），高于 3.1B 音文模型的 0.880。相对 VAP 提前约 220 ms 预判 turn 边界，中位相对 turn end −360 ms vs −140 ms。消融表明 Stage-1 预训练是 BC 能力主因；连续 Mimi 优于离散码本；Stage-2 保留生成损失或加入 ASR 目标会伤稀疏信号。

## 结论
双通道生成式预训练 + 显式 turn-taking 信号微调，可在无人工标注下缩小静音端点与 S2S 级轮次动态的差距，并支持 CPU 实时运行；作者指出当前约 453 h 仅为英语双人对话，多语/多方扩展是自然下一步。

## 点评
把 S2S 式“预测对方下一帧”当作表征学习，再接到可解释的 agent action，路径清晰，也解释了为何无预训练时 0.5B LLM 几乎不比 8M LSTM 强。BC 召回提升大但精度仍低（0.282），作者也提醒不宜单独作触发；4 s 标签定义与生产策略如何对齐仍需实测。


# Endpoint Anticipation for Low-Latency Spoken Dialogue

- 论文编号：2196
- 报告人：Sathvik Udupa
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/udupa26_interspeech.pdf

## 问题
级联口语对话系统（如 Unmute）依赖反应式 endpointer，ASR→LLM→TTS 串行导致 TTFA 常达 1–2 s，难以接入推理/工具等重计算。需要在用户话轮结束前主动预判终点，以便投机执行下游流水线，并量化延迟收益与无效计算的折中。

## 方法
提出 Endpoint Anticipation（EPA）：双流 Transformer 分别编码 User/System 音频（Mimi 前 8 码本特征，12.5 Hz，骨干冻结），拼接后对多个固定前瞻窗口 h∈{320,…,2560} ms 做二值分类（若 t_EOT−t∈[0,h] 则为正）。EPA-S 每窗口独立模型；EPA-M 共享骨干、多头多任务。阈值用 Silero VAD 精修，短于 2 s 的 turn/backchannel 掩码。部署时首次超过阈值 θ 触发投机：fork LLM 短前缀并预合成 TTS 缓存；若在 h 内真实终点确认则释放缓存并续写，否则丢弃。引入 MRA、PAR、ERC、HEA 等指标刻画“实现的前瞻”与“过早触发”。

## 实验与结果
在 SpokenWOZ 与 Switchboard 上相对适配后的 VAP 基线，EPA-M 在 MRA–PAR、HEA–ERC 曲线上更优。约 33% ERC 工作点、h=640 ms 时 EPA-M 的 MRA 达 640 ms（VAP 160 ms）；约 15% ERC 时仍有 480 ms MRA。任务型 SpokenWOZ 整体优于开放对话 Switchboard。接入 Unmute（Gemma 3 4B，h=960 ms）平均延迟从 1195 ms 降至 690 ms（降 505 ms），ERC 28.4%。EPA-S 与 EPA-M 指标接近，后者可一模型覆盖多 h。

## 结论
固定视界的语音端点预判可使级联系统投机掩蔽串行瓶颈；EPA-M 持续优于 VAP 式基线，并在 Unmute 上验证约半秒级平均延迟下降。未来关注中途改口、晚到关键信息等语义边界情况。

## 点评
把“能提前多久”与“浪费多少算力”拆成可调阈值曲线，比单一 precision/recall 更贴近系统工程。强项在任务型对话；开放对话更难，说明声学预判对结构松散话轮仍脆弱。投机策略依赖原有语义 VAD 做最终确认，预判模块本身不处理打断等其它全双工能力。


# Less can be More: What Aspects of Speech Drive End-of-Turn Detection

- 论文编号：1705
- 报告人：Rini Sharon
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sharon26_interspeech.pdf

## 问题
流式 end-of-turn（EOT）检测常融合声学、韵律与语义，但各模态相对贡献不清；多加文本是否一定更好仍缺在相同容量与训练条件下的系统消融。

## 方法
设计轻量三模态 APT：冻结 Zipformer2 声学编码器（80D FBank→25 Hz）、5 维手工韵律（归一化 F0、ΔF0、voiced、speech、log 静音累计）与 MiniLM 句向量（来自 RNN-T 贪心解码，blank 帧缓存）。各流经投影与 7 帧因果 depthwise 卷积后拼接，~261K 参数分类头输出帧级 EOT 概率。禁用模态用零向量占位并阻断梯度，在相同超参下从零训练全部 7 种非空子集。检测需连续 8 帧超阈（320 ms），容忍提前 50 ms。

## 实验与结果
专有英语电话对话 10K/2K/5K 句（约 33 h 训练）。A+P 最优：utterance F1 0.930，FA% 7.8，中位延迟 400 ms；纯声学 F1 0.927；APT 加文本后 F1 降至 0.909、FA% 升至 10.7。文本单模态 F1 仅 0.292、平均每句逾 5 次误触发。特征空间上韵律原始 silhouette 最高（0.301，主因 silence dur），文本类重叠大（0.108）。仅 A+P 与 APT 同时满足 FA<10% 与延迟<500 ms 部署预算；加文本的延迟优势部分被 ASR/BERT 开销抵消。

## 结论
在所研究的对话电话域，声学提供主检测信号、韵律补精度；连续帧级文本融合系统性抬高误触发，A+P 已足以达到部署级 EOT，不必为文本支付额外推理成本。

## 点评
零掩码 + 全子集消融把“能不能加模态”问成“该不该加”，证据扎实。文本在长 turn（中位 10–11 s）上对句法完整单元过敏，是场景效应而非单纯编码器弱；作者也承认噪声/低资源语言上文本或许更有用，且可改成边界抑制而非逐帧融合。

