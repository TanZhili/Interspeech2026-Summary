# ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Poster
- Area：8
- 论文数：10
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场围绕真实约束下的流式 ASR/KWS、持续学习与参数高效适应，以及脉冲网络早退能效。关键词是：开放可复现的流式日语模型、分离前端与干净后端解耦、严格虚警预算下的边缘关键词、无回放持续 ASR，以及口音/说话人流上的 LoRA 变体。

流式与鲁棒性上，CER 分层数据策展对欠表示域有益但多域微调时可能伤性能；在线分离 + 仅干净语音训练的流式 ASR 避免 MCT 对干净语音的损害。KWS 用间隔感知对比正则压低相似伪触发 FRR，并用因果时间关系蒸馏消解非因果教师的因果失配。

持续学习侧从保留方向梯度投影、奇异值尾子空间旋转 LoRA、模块化诊断数据集，到相似度条件有符号正交 LoRA 与按发音方式组织专家的 MoPE-LoRA，共同对抗灾难性遗忘并促进相似说话人/音类迁移。能效方面 First-to-Spike 以输出首峰本身作为决策信号。

## 技术内容

### 流式 ASR、解耦前端与边缘关键词

**A Compact Fully-Open Cache-Aware Streaming Model for Japanese ASR**（论文 3380；Yinchang Yang）  
123M 混合 RNNT/CTC、全开源流式日语 ASR。35K 小时预训练上 CER 分层策展惠及欠表示域，但高解码容量多域微调时可能受损；五域共 507 小时渐进微调后五测集平均 CER 12.4%（RNNT），优于更大 OWSM/ReazonSpeech 模型，RTFx 批量 1220、流式 446。

**Robust Streaming ASR with Decoupled Separation and Recognition**（论文 1503；DeLiang Wang）  
在线分离前端 + 仅干净语音训练的流式 ASR 后端；LibriSpeech、CHiME-4、LibriCSS 上持续优于 MCT 基线，并可模块化接到大型预训练语音模型而无需任务特化重训与 MCT。

**Margin-Aware Contrastive Regularization for Robust Streaming Keyword Spotting under Strict False-Alarm Constraints**（论文 3545；Hanwen Zhang）  
MACR 仅对目标关键词做类内吸引，并对离线挖掘的难负样本做间隔排斥，避免全局簇聚异构 Unknown。GSCV2 事件级流式协议下，在 0.5–0.2 FA/h 相对 CE 降 FRR >40%，部署零增参/时延。

**Mitigating Causality Mismatch with Causal Temporal Relation Distillation for Streaming Keyword Spotting**（论文 3546；Hanwen Zhang）  
蒸馏样本内时间拓扑而非逐点特征，下三角掩码保证历史可实现锚点；双向变体用教师全拓扑作辅助先验但不改零前瞻推理图。因果 1D-CNN 准确率 95.12%→96.91%，1.0 FA/h 时 FRR 约减半。

### 持续学习、口音/说话人适应与脉冲早退

**Retention-Preserving Gradient Projection with Entropy-Guided Token-Level Distillation for Rehearsal-Free Continual ASR**（论文 2309；Seunghee Ma）  
用上一模型蒸馏定义保留方向，熵引导 token 蒸馏；监督与蒸馏梯度冲突时投影衰减对立监督分量；冻结编码器只适应解码器。相对 LwF，四域顺序适应后平均 WER 相对降 7.2%，Common Voice 多语退化平均降 51.5%。

**Parameter-Efficient Continual Learning for Automatic Speech Recognition**（论文 3169；Steven Vander Eeckt）  
按奇异值划分头/尾子空间，仅在低能量尾子空间做近似旋转适应，后续任务旋转经权重平均以保保持；两基准上遗忘更少、总体更优。

**MoDiCoL: A Modular Diagnostic Continual Learning Dataset for Robust Speech Recognition**（论文 2111；Theresa Pekarek Rosin）  
模块化诊断持续学习数据集，可控组合语言内容、说话人与声学环境，并给出贴近现实的持续课程；评测三种持续学习策略以分析鲁棒性获取、迁移与遗忘。

**SCOLoRA: Similarity Conditioned Signed Orthogonal LoRA for Continual Speaker Adaptation**（论文 3243；Ye-Eun Ko）  
用说话人嵌入相似度经有符号系数动态平衡子空间对齐与正交分离，避免任务无关正交抑制相似说话人迁移；相对 LoRA 类持续学习基线提升新说话人适应并减遗忘。

**Mixture of Phonetic Experts Based Low-Rank Adaptation of Conformer Models for Accented English Speech Recognition**（论文 322；Anmol Guragain）  
六个按发音方式类别组织的低秩专家，帧级音素监督 + 声学门控路由，专家跨口音共享。L2-ARCTIC 优于单 LoRA 与全微调；留一口音零样本相对单 LoRA 相对改进 12.3%。

**First-to-Spike: An Early-Exit Framework for Rapid and Energy-Efficient Spiking Neural Networks**（论文 1858；Siqi Cai）  
竞争输出层首次发放即终止推理，配合 Winner-Take-All 与混合时间训练目标；语音与神经生理数据上更高精度且显著降时延与能耗，验证尖峰本身可作为决策信号。

## 本场要点

- 全开源流式日语小模型与分离—识别解耦提供可部署鲁棒路径。
- 严格 FA 预算下对比间隔与因果关系蒸馏显著改善流式 KWS。
- 无回放持续 ASR 依赖保留方向投影、尾子空间旋转与说话人相似度条件 LoRA。
- 音素类别 MoE-LoRA 比口音专用专家更具零样本可扩展性；脉冲首峰早退服务能效。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 3380 | A Compact Fully-Open Cache-Aware Streaming Model for Japanese ASR |
| 1503 | Robust Streaming ASR with Decoupled Separation and Recognition |
| 3545 | Margin-Aware Contrastive Regularization for Robust Streaming Keyword Spotting under Strict False-Alarm Constraints |
| 3546 | Mitigating Causality Mismatch with Causal Temporal Relation Distillation for Streaming Keyword Spotting |
| 2309 | Retention-Preserving Gradient Projection with Entropy-Guided Token-Level Distillation for Rehearsal-Free Continual ASR |
| 3169 | Parameter-Efficient Continual Learning for Automatic Speech Recognition |
| 2111 | MoDiCoL: A Modular Diagnostic Continual Learning Dataset for Robust Speech Recognition |
| 3243 | SCOLoRA: Similarity Conditioned Signed Orthogonal LoRA for Continual Speaker Adaptation |
| 322 | Mixture of Phonetic Experts Based Low-Rank Adaptation of Conformer Models for Accented English Speech Recognition |
| 1858 | First-to-Spike: An Early-Exit Framework for Rapid and Energy-Efficient Spiking Neural Networks |
