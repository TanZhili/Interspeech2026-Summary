# Robust and Real-World ASR Systems

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral（Area 10 - Oral 2）
- Area：10
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。不编造摘要外指标。

## 技术趋势

本场从“真实部署约束”审视 ASR：云级联字幕的延迟—稳定权衡、联邦多语 SpeechLLM、智能眼镜佩戴者识别、可扩展基础模型基础设施、诊断式印度语言评测，以及长周期增量后处理纠错。

级联实时字幕工作揭示激进端点会把系统推入积压雪崩（中位 RTF>1），需区分首字延迟与稳定文本延迟，并指出 Whisper 提示条件可能伤害短块流式 ASR。联邦学习在英意双语非 IID 下用语言感知梯度聚合与采样聚类缓解失衡。穿戴侧用多前端差分输入对抗侧向干扰说话。

工程与评测层，ESPnet3 以配置驱动数据组织与分片服务大规模预训练；SCRIBE 用类别化错误分解与 sandhi 容忍对齐挑战纯 WER；Audio-KWS 门控检索则让纠错日志在上下文窗口内按音频关键词增量复用。

## 技术内容

### 实时级联、联邦与穿戴鲁棒识别

**Decoding the Trade-off: A Large-Scale Analysis of Latency and Stability in LLM-based Speech Translation Cascades**（论文 1821；presenter：Shinyoung Sun）  
可复现 KO→EN 字幕流水线 RST 区分 latency_first 与 latency_stable。全量 FLEURS 上显示激进端点使级联进入积压区（中位 RTF>1），latency_stable 随时间增长；Whisper 提示条件使短块流式 ASR CER 恶化约 14–17 个百分点并可泄漏指令。将操作阈值定义为中位 RTF≤1 的最激进设置，强调吞吐稳定对低延迟 LLM 级联的必要性。

**Fed-SpeechLLM: Federated Learning Speech Language Models for Multilingual ASR**（论文 689；presenter：Daniele Giuseppe Falavigna）  
在英意双语设定研究联邦 SpeechLLM-ASR，面对声学与跨语异构叠加的非 IID。标准 FL 在语言偏斜客户端上退化；提出语言感知梯度聚合与基于采样聚类的方法，选择性聚合语音编码器与投影层并冻结 LLM 骨干，结果相对集中式训练具竞争力。

**Multi-Channel Differential ASR for Robust Wearer Speech Recognition on Smart Glasses**（论文 127；presenter：Yiteng Huang）  
智能眼镜佩戴者识别受侧向说话干扰。系统融合波束形成、麦克风选择与轻量侧向说话检测等互补前端的差分输入。仿真与真实数据上相对传统方法，WER 相对降幅可达 18.0%。

### 基础设施、诊断评测与增量后处理

**ESPnet3: Infrastructure for Scalable Speech and Audio Research in the Foundation Model Era**（论文 2698；presenter：Masao Someki）  
模块化架构、配置驱动数据集合成与统一 Python 工作流；DataOrganizer 与数据集分片支持大规模训练，并允许轻量 stage 覆盖。OWSM 预训练相对 ESPnet2 每 epoch 缩短 21.1 分钟，多节点 GPU 利用率>80%；微调实验显示约 46 行额外代码即可接入新模型与数据。将公开模型检查点与训练日志。

**SCRIBE: Diagnostic Evaluation and Rich Transcription Models for Indic ASR**（论文 3436；presenter：Kavya Manohar）  
主张纠错成本取决于错误类型而非计数；WER 混淆类别且对黏着语 sandhi 合并结构性惩罚。SCRIBE 经 sandhi 容忍对齐与领域词表注入，分解词汇、标点、数字与领域实体错误率；人工验证与专家判断更一致。发布框架、LLM 策展流水线、基准及印地/马拉雅拉姆/卡纳达富转写开源权重模型。

**Audio-KWS-Gated Error Memory Retrieval for Incremental ASR Post-Correction**（论文 363；presenter：Taira Ashikawa）  
增量后处理：LLM 错误分析提取纠错对更新关键词库；Audio-KWS 从音频检测 Top-N 关键词并检索纠错记录（日语用读音作关键词）；LLM 再按记录编辑。Earnings-21 与 CSJ 上约减少 70% 提示量（英 Top-20；日 Top-10），同时改进 WER/CER 与 Bias-F1。

## 本场要点

- 低延迟级联必须监控稳定文本延迟与 RTF，避免“更快端点反而更慢”的积压区。
- 联邦 SpeechLLM 需语言感知聚合以应对跨语客户端失衡。
- 智能眼镜 WSR 受益于多前端差分输入与侧向说话检测。
- ESPnet3 降低基础模型时代大规模实验的工程门槛。
- 印度语 ASR 需要类别化诊断指标，而非单一 WER。
- 音频门控纠错记忆使长周期后处理可在有限上下文内复用历史。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 1821 | Decoding the Trade-off: A Large-Scale Analysis of Latency and Stability in LLM-based Speech Translation Cascades |
| 689 | Fed-SpeechLLM: Federated Learning Speech Language Models for Multilingual ASR |
| 127 | Multi-Channel Differential ASR for Robust Wearer Speech Recognition on Smart Glasses |
| 2698 | ESPnet3: Infrastructure for Scalable Speech and Audio Research in the Foundation Model Era |
| 3436 | SCRIBE: Diagnostic Evaluation and Rich Transcription Models for Indic ASR |
| 363 | Audio-KWS-Gated Error Memory Retrieval for Incremental ASR Post-Correction |
