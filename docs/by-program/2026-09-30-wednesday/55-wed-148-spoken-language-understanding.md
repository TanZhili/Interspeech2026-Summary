# Spoken Language Understanding

- 日期：2026年9月30日（星期三）
- 时间：16:30-18:30
- 形式：Poster
- Area：11
- 论文数：12
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场覆盖口语理解（SLU）从数据与基准、SpeechLLM/LALM 适配，到对话状态跟踪、多意图与多说话人场景，以及能力遗忘与长时音频时间锚定。主线是：把语音侧线索与大模型推理能力接到意图/槽位/对话状态上，同时用新基准暴露单说话人、单意图设定下的盲区。

数据与评测上，DEBATE 用语音消歧文本歧义；MAC-SLU、MSU-Bench 分别加压汽车座舱多意图与会话多说话人；若干工作显示 ICL 远弱于 SFT，端到端 LALM 可接近管线并避免 ASR 级联错误。方法上，RG-FT 蒸馏结构化拒斥推理以拉开相邻意图边界；SPARE 用语义摘要寄存器缓解长 CoT 偏离音频；增量符号编辑 + GRPO、跨域语音—文本联合训练推动口语 DST。

鲁棒与治理方面，原型感知对比与粗到细注意力强化多模态意图；覆盖引导 RL 约束检索代理查询分解；语义帧级多任务自洽聚合多意图输出；Binding Subspace 在表示层削弱意图—槽位条件映射以实现选择性能力遗忘；GigaChat Audio 用周期时间标记支撑长达 120 分钟的时间锚定问答。

## 技术内容

### 数据、基准与消歧

**DEBATE: A Dataset for Disentangling Textual Ambiguity in Mandarin Through Speech**（论文 3146；Haotian Guo）  
针对语音消歧（DTS）数据缺失，发布含 1,001 条歧义话语、各由 10 名母语者录制的中文语音—文本公开集，刻画发音、停顿、重音、语调如何揭示真实意图。详述数据管线并对三款大型语音语言模型做基准，显示机器与人类意图理解差距显著。

**MAC-SLU: Multi-Intent Automotive Cabin Spoken Language Understanding Benchmark**（论文 1055；Yuezhang Peng）  
面向汽车座舱多意图真实复杂数据，对主流 LLM/LALM 做 ICL、SFT 及端到端/管线评测。摘要称 ICL 有潜力但显著落后 SFT；端到端 LALM 可比管线并避免 ASR 错误传播。

**MSU-Bench: Towards Understanding the Conversational Multi-Speaker Scenarios**（论文 3344；Zhaokai Sun）  
诊断性多说话人会话理解基准：16 项说话人中心任务、2,300 条 QA，两层框架从说话人接地到对话推理。Gemini 辅助标注与人工校验；闭源领先但复杂接地与多说话人推理仍普遍困难。

### SpeechLLM 适配、推理与 DST

**Distilling Structured Reasoning into SpeechLLMs for Spoken Language Understanding**（论文 1540；Toshihiro Tsukagoshi）  
提出 RG-FT：将 DeepSeek-R1 生成的候选枚举—拒斥推理—标签预测轨迹蒸馏为多任务目标，迫使模型显式说出拒斥理由以锐化类间边界；推理时仅直接预测标签、无额外开销。多基准与六款 SpeechLLM 上一致提升。

**Enhancing Audio Reasoning via Semantic Summary Prediction**（论文 1504；Francesco Bonzi）  
LALM 显式 CoT 常比直接作答更差，假说为长推理序列使注意力离开音频。SPARE 引入与最终结论用 Sentence-BERT 余弦对齐的寄存器 token，在推理前用目标语义条件化潜空间。MMAU/MMAR 上 SALMONN 零样本推理与早期音频注意力增强，无额外推理成本。

**Incremental End-to-End Spoken Dialogue State Tracking with a Multimodal LLM and Reinforcement Learning**（论文 592；Tomoya Higuchi）  
用 Qwen2.5-Omni-7B 从原始音频生成转写与相对上一状态的符号编辑，缩短输出并降低破坏未变槽位风险。SFT + GRPO 直接优化转写、DST 正确性与格式奖励。SpokenWOZ 上增量更新显著优于全状态预测，并报告该基准最佳结果。

**Joint Speech And Text Training For LLM-based End-To-End Spoken Dialogue State Tracking**（论文 2769；Katia Vendrame）  
针对口语 DST 标注稀缺与跨域难泛化，联合训练可用口语 DST 与其他域书面文本 DST，在无需目标域口语训练数据时获得良好跨域表现。

### 多意图、检索代理、遗忘与时间锚定

**MVCL-DAF++: Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion**（论文 267；Haofeng Huang）  
扩展 MVCL-DAF：原型感知对比对齐增强语义一致性；粗到细注意力融合全局模态摘要与 token 级特征。MIntRec/MIntRec2.0 达新 SOTA，稀有类 WF1 分别 +1.05%/+4.18%。

**PROGRESS: Coverage-guided RL to Train Search-augmented LLM Agent**（论文 2760；Aounon Kumar）  
用教师引导的覆盖奖励显式塑造策略模型对复杂查询的分解搜索；冻结教师分解出必要搜索查询并纳入 R1 风格训练，无需稠密过程监督。实验显示覆盖引导 RL 提升任务表现。

**SFL-MTSC: Leveraging Semantic Frame-Level Multi-Task Self-Consistency for Robust Multi-Intent Spoken Language Understanding**（论文 3369；Po-Yen Chen）  
在语义帧级分解意图专用帧，做域—意图分组与槽位聚类，用路径支持评分保留可靠帧再整合。MAC-SLU 零样本相对单路径提升槽 F1 与总体准确率，意图准确率大多稳定。

**Selective Capability Unlearning in End-to-End Spoken Language Understanding**（论文 3349；Akanksha Singh）  
指出仅抑制目标意图不能消除意图条件下的槽位生成（能力残留）。Binding Subspace 在表示层隔离并衰减该条件方向；显著降低强制前缀可恢复性并保持保留任务性能。

**GigaChat Audio: Time-aware Large Audio Language Model**（论文 2343；Aleksandr Kutsakov）  
在连续音频 token 中交织周期时间标记，用级联管线大规模合成监督，支持最长约 120 分钟输入的显式时间戳问答与时间锚定片段描述/摘要。消融考察时间表示、标记频率、分词与时长混合；权重与数据已发布。

## 本场要点

- 语音消歧与多意图/多说话人新基准暴露 SpeechLLM 与人类差距及接地瓶颈。
- 结构化拒斥推理蒸馏与语义摘要寄存器分别锐化意图边界、稳住音频注意力。
- 口语 DST 趋向增量符号编辑 + RL，以及跨域语音—文本联合训练。
- 多意图鲁棒依赖原型对齐、帧级自洽聚合与检索分解监督。
- 选择性遗忘需在表示层切断意图—槽位条件映射。
- 长录音理解需要显式时间标记与时间锚定能力。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 267 | MVCL-DAF++: Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion |
| 592 | Incremental End-to-End Spoken Dialogue State Tracking with a Multimodal LLM and Reinforcement Learning |
| 1055 | MAC-SLU: Multi-Intent Automotive Cabin Spoken Language Understanding Benchmark |
| 1504 | Enhancing Audio Reasoning via Semantic Summary Prediction |
| 1540 | Distilling Structured Reasoning into SpeechLLMs for Spoken Language Understanding |
| 2343 | GigaChat Audio: Time-aware Large Audio Language Model |
| 2760 | PROGRESS: Coverage-guided RL to Train Search-augmented LLM Agent |
| 2769 | Joint Speech And Text Training For LLM-based End-To-End Spoken Dialogue State Tracking |
| 3146 | DEBATE: A Dataset for Disentangling Textual Ambiguity in Mandarin Through Speech |
| 3344 | MSU-Bench: Towards Understanding the Conversational Multi-Speaker Scenarios |
| 3349 | Selective Capability Unlearning in End-to-End Spoken Language Understanding |
| 3369 | SFL-MTSC: Leveraging Semantic Frame-Level Multi-Task Self-Consistency for Robust Multi-Intent Spoken Language Understanding |
