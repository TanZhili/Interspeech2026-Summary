# Robust and Real-World ASR Systems

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：10
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从“真实部署约束”审视 ASR：云级联字幕的延迟—稳定权衡、联邦多语 SpeechLLM、智能眼镜佩戴者识别、可扩展基础模型基础设施、诊断式印度语言评测，以及长周期增量后处理纠错。

级联实时字幕工作揭示激进端点会把系统推入积压雪崩（中位 RTF>1），需区分首字延迟与稳定文本延迟，并指出 Whisper 提示条件可能伤害短块流式 ASR。联邦学习在英意双语非 IID 下用语言感知梯度聚合与采样聚类缓解失衡。穿戴侧用多前端差分输入对抗侧向干扰说话。

工程与评测层，ESPnet3 以配置驱动数据组织与分片服务大规模预训练；SCRIBE 用类别化错误分解与 sandhi 容忍对齐挑战纯 WER；Audio-KWS 门控检索则让纠错日志在上下文窗口内按音频关键词增量复用。

## 论文技术总结

# Decoding the Trade-off: A Large-Scale Analysis of Latency and Stability in LLM-based Speech Translation Cascades

- 论文编号：1821
- 报告人：Shinyoung Sun
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sun26f_interspeech.pdf

## 问题
实时字幕需低延迟与稳定译文。段级云端级联中，激进端点检测抬高请求率，可超出服务容量形成 backlog avalanche——排队延迟主导，使“更快”设置在稳态下更慢。系统评测常只报单一端到端延迟，混淆首字延迟与稳定字幕延迟。

## 方法
提出 RST：可复现 KO→EN 字幕流水线，区分 time-to-first-text（latency first）与 time-to-stable-text（latency stable）。在完整 FLEURS KO→EN（2851 clips）上回放评测；2×2 级联（whisper-1 / gpt-4o-transcribe × gpt-4.1-mini / grok-4-fast）；对比 fast vs stable 端点预设并扫 hangover/min 时长；定义运营阈值为 median RTF≤1 的最激进设置。另做 Whisper 提示消融。

## 实验与结果
fast 预设 median RTF≫1（如约 24–52），latency stable 可数十秒并随时间累积；stable 预设 RTF 可 ≤1，首字/稳定延迟约 1–3 s 量级且质量更高（BLEU/chrF）。Whisper 滚动/静态提示在短块流式下 CER +14–17 pp，并可泄漏指令。吞吐稳定是低延迟 LLM 级联的必要条件。

## 结论
端点粒度–吞吐稳定–上下文完整构成三难；应优先保证 median RTF≤1 的稳定区，再追求激进延迟。提示条件在短块流式 ASR 上可能有害。

## 点评
把“快设置变慢”量化成 backlog 机制，并拆分 first/stable 延迟，对工程运维直接可用。评测绑定特定云 API 与 KO→EN，外推需重标定阈值。


# Fed-SpeechLLM: Federated Learning Speech Language Models for Multilingual ASR

- 论文编号：689
- 报告人：Daniele Giuseppe Falavigna
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ali26_interspeech.pdf

## 问题
SpeechLLM 适于多语 ASR，但集中训练与隐私约束冲突；联邦学习面临声学与跨语双重 non-IID。语言偏斜客户端会使标准 FL 退化。

## 方法
Fed-SpeechLLM：在双语英/意设置评测联邦 SpeechLLM。选择性聚合语音编码器与投影层，LLM 骨干冻结（LoRA 可适配）。提出语言感知梯度聚合与基于采样聚类的客户端选择，缓解多语不平衡。Flower + FedAvg，每轮约 30% 客户端、本地 10 epoch、共 100 轮。数据：LibriSpeech-100 与 MLS 意大利语。

## 实验与结果
单语 FL 接近中心化（LS 约 6–7% vs 中心约 6%；MLS 约 22% vs 约 20%）。双语全客户端：LS/MLS 约 16.8/19.7，相对中心仍有差距。客户端平衡、服务端微调与早/晚语言偏置显著影响收敛；早期英语偏置可将 LS 联邦–中心差距缩至约 5 点。Whisper 作编码器的消融验证编码器选择影响。

## 结论
在复合非 IID 下，语言感知聚合与客户端采样策略可使联邦 SpeechLLM 收敛并接近中心化性能，为隐私约束多语 ASR 提供可行路径。

## 点评
首次系统分析 SpeechLLM 联邦适配，抓住“语言偏斜”这一新轴。仍偏双语音读语料；真实设备异构与通信预算未充分展开。


# Multi-Channel Differential ASR for Robust Wearer Speech Recognition on Smart Glasses

- 论文编号：127
- 报告人：Yiteng Huang
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yang26_interspeech.pdf

## 问题
智能眼镜佩戴者语音识别（WSR）在开放场易受旁人 side-talk 干扰；仅靠波束成形难完全抑制，且增强/分离/抽取前端常引入不可接受延迟或隐私敏感说话人建模。

## 方法
多通道 differential ASR：并行融合互补前端——朝向嘴部的 MVDR 波束成形、最低延迟的麦克风选择（高 SNR 通道）、轻量流式 side-talk detection（区分佩戴者/旁人、不建模身份）。不同帧率前端嵌入对齐后送入低延迟流式 RNN-T。在 Ray-Ban Meta 实测 RIR 模拟与 HATS 实采数据上评测。

## 实验与结果
模拟与真实 LibriSpeech 多通道集：相对仅波束成形基线，组合系统一致更优；真实噪声侧谈上相对 WERR 最高约 18.0%（平均约 14.4%）。实采覆盖 72 个旁人位置（角度/高度/距离）；50% 重叠时角度依赖性更明显。干净条件亦保持竞争力。

## 结论
多前端差分输入能量著提升眼镜 WSR 对 side-talk 的鲁棒性，且兼顾流式延迟与隐私约束。

## 点评
问题定义贴产品：延迟与隐私排除重前端，改用轻量互补线索喂 ASR。实采角度网格使评测可信。仍偏 LibriSpeech 读音；极强旁人主导或多人侧谈场景未充分覆盖。


# ESPnet3: Infrastructure for Scalable Speech and Audio Research in the Foundation Model Era

- 论文编号：2698
- 报告人：Masao Someki
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/someki26_interspeech.pdf

## 问题
基础模型时代语料达百万小时、模型达十亿参，实验工作流复杂；既有工具链在多数据集组合、大规模迭代、多节点训练与 PEFT 集成上工程开销大。

## 方法
ESPnet3：模块化架构 + 配置驱动数据集组合 + 统一 Python 工作流。引入 DataOrganizer 灵活拼数据，dataset sharding 控制内存；允许轻量 stage override 写配方逻辑。默认 BaseSystem 即可跑大规模预训练，并支持接入非原生 ESPnet 模型（如 Whisper）与 HuggingFace PEFT。

## 实验与结果
OWSM-V4 base（约 320k 小时）预训练：相对 ESPnet2，每 epoch 从 95.3→74.2 分钟（约 −21.1 分钟），多节点 GPU 利用率 >80%；RAM 与数据刷新开销大幅下降（约 35.9GB→73.1MB，刷新 311.5s→13.1s）。增强经 DataOrganizer 接入后 CHiME-4 WER 略降。WhisperLv3 在 FalAR 微调可用约 46 行接入新 HF 数据集（ESPnet2 手工约 374 行）；全参/LoRA 均可。

## 结论
ESPnet3 以更低工程成本支撑大规模语音基础模型训练与定制微调，并将公开释放与 checkpoint/日志。

## 点评
贡献在基础设施而非新识别算法：把“能跑大、好扩展”做成可测指标（epoch 时间、利用率、代码行数）。对社区复现大模型实验价值高；具体任务 SOTA 非本文重点。


# SCRIBE: Diagnostic Evaluation and Rich Transcription Models for Indic ASR

- 论文编号：3436
- 报告人：Kavya Manohar
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/manohar26_interspeech.pdf

## 问题
ASR 作为听写工具时，纠错成本取决于错误类型而非计数；WER 把词法/标点/数字/实体混成标量，并对黏着语 sandhi 合法合并施加结构性惩罚（可相对抬高约 30%）。印地语系富文本转写缺乏可操作诊断。

## 方法
SCRIBE：输出诊断向量 [ERlex, ERpunc, ERnum, ERent]，经 sandhi 容忍对齐与领域词表注入；聚合为 SCRIBE-WER。配套 LLM（Gemini）策展管线把 verbatim 转富文本，并发布 FLEURS-RO、IN22-Legal 基准与 Hindi/Malayalam/Kannada 开源富转写模型（Whisper 三阶段微调）。

## 实验与结果
相对 IndicWhisper/IndicConformer，SCRIBE-ASR 在 FLEURS-RO 与法律 OOD 上 WER/WERS 更低；数字错误近饱和（ERnum 常 <1%）。马来alam 法律集 WER 44.52% 而 ERlex 仅 15.96%，显示约 30% 相对膨胀来自形态对齐。人工评分：SCRIBE 分项与专家 Spearman |ρ| 约 0.36–0.92，WER 在多维（尤其马来alam）不显著。标点仍是主瓶颈。

## 结论
分类诊断 + sandhi 对齐使评测对齐专家纠错成本；富转写模型与开源工具为印地 ASR 提供可行动反馈回路。

## 点评
把“听写可用性”从 WER 单标量拆开，对黏着语尤其关键。人评验证强。策展依赖 LLM，残留幻觉需人工把关；标点仍难，说明诊断清楚后下一步应攻韵律/边界。


# Audio-KWS-Gated Error Memory Retrieval for Incremental ASR Post-Correction

- 论文编号：363
- 报告人：Taira Ashikawa
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ashikawa26_interspeech.pdf

## 问题
端到端 ASR 对稀有词与领域专有名词仍易错；LLM 二遍纠错可复用历史纠错记录，但全历史进 prompt 会撞上下文窗口，且仅靠噪声 ASR 假设做文本检索时，触发词被误识就会漏检相关记录。

## 方法
提出增量式 LLM ASR 后纠错框架：人类参考可用时，用 LLM 做错误分析，抽取 hypothesis–reference 短语对写入 error memory，并更新关键词库存与倒排索引（英语索引正误两侧；日语用 LLM 估计的读音作检索键）。对新音频段，用开词汇 Audio-KWS（AdaKWS，Whisper-medium 编码器冻结）在库存上打分，经阈值与 Top-N 得到关键词集合，再检索并按时效截断至最多 M=200 条记录，交给 LLM 做记录约束的保守编辑。

## 实验与结果
在 Earnings-21（英语，公开 ASR 假设）与 CSJ（日语，Whisper-large-v3）含至少一词的 20 个 bias-word 子集上评测。相对无 KWS 的近期历史基线，Top-20 英语约减 prompt 70.9%/65.1%（micro/macro），WER 28.92 vs 29.06，Bias-F1 0.856 vs 0.836；Top-10 日语约减 71.7%/66.7%，CER 14.62 vs 14.86，Bias-F1 0.673 vs 0.648。Top-30 精度最好但压缩更少；仅索引参考侧在日语上损害 Bias-F1。纠错 LLM 为 gpt-oss-20b。

## 结论
Audio-KWS 门控检索可在约 70% prompt 压缩下保持或提升 WER/CER 与 Bias-F1；未来需处理 KWS 漏检并加速分析/纠错推理。

## 点评
核心抓的是「纠错记忆膨胀」与「文本检索依赖错误假设」的耦合问题：用音频侧关键词门控历史，比单纯截断近期记录更贴合当前内容。日语读音键与表面编辑分离的设计合理，但系统依赖人类参考才能扩库存，且强过滤（Top-1）会明显伤 Bias-F1，SLA 上需在压缩与召回间折中。

