# Speech and Language Technologies for Health Applications 1

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：13
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场面向健康应用：咳嗽结核筛查、青少年自杀风险语音检测、抑郁检测的联邦隐私、言语治疗感知训练、神经疾病西班牙语 ASR 语料，以及德文焦虑抑郁语音数据集。共同线索是非侵入、可扩展的语音生物标志，同时强调隐私、范式泛化与真实临床/众包数据质量。

方法上出现基础模型表示与谱描述符的融合（双曲原型 + bandit 加权）、跨诱发范式的 Speech LLM + MoDE 专家、以及联邦多模态原型对齐并引入隐私–性能分数。教育与包容侧则用深度学习嗓音编辑生成锚点样本训练学生感知，并发布神经受损西班牙语与德文 GAD/抑郁开源标注资源。

趋势是：从单任务单范式检测走向跨范式统一模型、隐私可量化的联邦学习，以及面向低资源病理语音与心理健康的基准数据集建设。

## 技术内容

### 筛查、风险检测与联邦隐私

**From Signals to Patterns: Non-Invasive Tuberculosis Detection from Cough Audio using Bandit Weighted Hyperbolic Prototypes**（论文 2704；Muskaan Singh）  
提出 COBALT：码本对齐双曲原型与 bandit 式可靠性加权，融合语音/音频基础表示与谱描述符。在 CODA TB DREAM Challenge 上摘要称持续优于单表示与拼接基线，MFCC 与 PaSST 融合取得最佳整体表现并刷新该基准。

**Towards Paradigm-General Suicide Risk Detection via Speech LLM**（论文 666；Wen Wu）  
首次研究跨诱发范式统一模型：Speech LLM 骨干 + DoRA 专家混合（MoDE），在 1,223 名参与者、十种诱发范式上动态捕捉互补线索。摘要称 MoDE 优于单范式与常规联合学习，可泛化到未见范式并改善置信校准。

**FedMPA: A Novel Privacy-Performance Optimization Approach for Multimodal Speech-Based Depression Detection**（论文 586；Dushanthi Madhushika Manamalage）  
联邦多模态原型对齐框架：模态特异原型、EMA 稳定全局原型库、原型引导损失与 softmax–原型混合推理，并引入任务特异 Privacy-Performance Score（PPS）。在 E-DAIC 上摘要称优于 FedAvg/FedProx/FedProto/FedGPD，PPS 达 0.92。

### 治疗训练与临床语料资源

**Can deep learning based voice editing enhance voice quality perception skills in speech therapy students?**（论文 2475；Jana Wiechmann）  
20 名参与者对 16 个嗓音在解释前后沿 creaky/breathy/rough 评分；对照组听自然锚点，实验组听合成样本。摘要称合成解释提高感知灵敏度与与金标准一致性，对照组无此效应；“rough” 仅在合成条件下从低于机会水平升至高于机会水平。

**S-DiverSe: Spanish Diverse Speech**（论文 2529；Fernando López）  
3.2 小时野外西班牙语，22 名 ALS、帕金森与中风说话人，444 段人工转写及性别、疾病类型、可懂度元数据。基线与适配实验摘要称对域外神经受损西语，启发式文本后处理比微调更稳健，凸显专用野外基准需求。

**GADVOX: The German Anxiety and Depression Voice Examination Dataset**（论文 3523；Robert P. Spang）  
首个开源可及的德文抑郁与焦虑自动检测/严重度估计语音集：1,004 名成人众包，十个结构化自由说提示随机呈现，人均约 18.4 分钟自发语音；附 PHQ-9 与 GAD-7（Cronbach’s α 分别为 .85、.86）。多阶段质控自 1,420 候选排除 29.3%；元数据公开，完整音频按合理请求提供。

## 本场要点

- COBALT 融合谱特征与基础嵌入，刷新咳嗽结核筛查基准。
- MoDE 统一十种诱发范式的自杀风险语音检测并改善校准。
- FedMPA 量化隐私–性能权衡，服务去中心化抑郁检测。
- 合成嗓音锚点可提升言语治疗学生的感知训练效果。
- S-DiverSe 提供神经受损西班牙语野外 ASR 评测资源。
- GADVOX 以大规模德文自由说 + 量表分支持回归式严重度建模。

## 覆盖核对

| id | title |
|---|---|
| 2704 | From Signals to Patterns: Non-Invasive Tuberculosis Detection from Cough Audio using Bandit Weighted Hyperbolic Prototypes |
| 666 | Towards Paradigm-General Suicide Risk Detection via Speech LLM |
| 586 | FedMPA: A Novel Privacy-Performance Optimization Approach for Multimodal Speech-Based Depression Detection |
| 2475 | Can deep learning based voice editing enhance voice quality perception skills in speech therapy students? |
| 2529 | S-DiverSe: Spanish Diverse Speech |
| 3523 | GADVOX: The German Anxiety and Depression Voice Examination Dataset |
