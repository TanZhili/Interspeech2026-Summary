# Speech Emotion Recognition and Representation 2
- 日期：Tuesday 29 September 2026 / 时间：09:00-11:00 / 形式：Poster（Area 3）/ 论文数：11
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本海报场覆盖 SER / MER / MERC / CER 的表征与学习策略：高效注意力权衡、多标签基准与 Mamba 融合、混合增强与多损失、图注意力时序聚合、低资源语种轻量双流、对话情感惯性、模态特异标签分布、标注不确定性课程、连续情感时延补偿，以及性别公平迁移与冲突感知伪标签。瓶颈集中在标注歧义、类不平衡、长序列算力、跨模态不一致，以及说话人/评分者偏见与伪标签噪声。

相对“更大预训练编码器”，多篇强调结构与监督形式：分布标签 vs 硬标签、优势加权排序式思想在相关健康场已见、此处则用熵感知分析与对比学习；多任务细粒度对齐可从声学自举伪标签而少依赖转写。公平性工作明确双端（说话人侧与评分者侧）中立，并在属性部分观测下做任务向量式迁移。

效率与容量并存：标准自注意力识别最强但昂贵，RetNet 等高效变体换时延与显存；1.1M 参数双流在孟加拉语说话人无关评测上挑战更大预训练模型——摘要强调先前工作常缺 SI 评测。

## 技术内容

### 注意力效率、多标签基准与增强式学习

**How Attention Shapes Emotion: A Comparative Study of Attention Mechanisms for Speech Emotion Recognition**（论文 1907；presenter：Federico Costa）
系统基准 RetNet、LightNet、GSA、FoX、KDA 等优化注意力。MSP-Podcast 两版上标准自注意力识别最强，但高效变体可大幅降推理时延与显存，凸显精度–效率权衡。

**From Single to Multi-Label SER: Dataset and Mamba-Based Fusion Model**（论文 3458；presenter：Thi Thu Trang Nguyen）
由 MSP-Podcast V2.0 众包票构造可复现多标签基准（可靠性过滤、票到标签、时间平移增强）。紧凑 Mamba 融合 MFCC 与 log-mel，验证集阈值扫描选检查点。摘要称两测试分区 micro-F1 约 0.50，并开源划分与配方。

**Multi-Loss Learning for Speech Emotion Recognition with Energy-Adaptive Mixup and Frame-Level Attention**（论文 1219；presenter：Yizhong Geng）
EAM 基于 SNR 增强生成多样样本，FLAM 强化帧级线索；多损失含 KL、focal、center 与监督对比。在 IEMOCAP、MSP-IMPROV、RAVDESS、SAVEE 上摘要称达先进。

**Segment-wise Embedding based Graph Attention Network for Effective Speech Emotion Recognition**（论文 969；presenter：Haoyu Song）
Swin-Transformer 适配预训练表征；块掩码预测与话语对比缓解分布偏移；由多嵌入裁剪构图经 GAT 聚合变长话语，并用监督对比应对歧义标签。IEMOCAP 与 MER2023 上摘要称显著优于 SOTA。

### 低资源架构、对话/多模态与不确定性监督

**Dual-Stream DNN-KAN Networks with Bangla-Specific Features for Speech Emotion Recognition**（论文 3374；presenter：Kazi Reyazul Hasan）
MFCC 走 DNN、统计优化韵律特征走轻量 KAN（B-spline），约 1.1M 参数。说话人无关评测下报告 SUBESCO / BanglaSER 准确率，并强调多数先前 Bangla 工作缺 SI；特征选择管线迁到 EmoDB 亦高，且相对更大预训练模型有优势。

**EII-SCL: Harnessing Emotional Inertia for Multimodal Emotion Recognition in Conversation**（论文 3532；presenter：Zilong Huang）
MERC 常忽略情感惯性对情绪转换的影响。EII-SCL 在时窗内构造惯性影响样本以指导监督对比，无需额外数据即可接入既有模型。IEMOCAP 与 MELD 上摘要称持续优于先进方法。

**Leveraging Modality-Specific Label Distributions for Enhanced Multimodal Emotion Recognition**（论文 2076；presenter：Xiaohan Shi）
MoLD 显式建模模态特异标签分布，并加模态相似度损失促跨模态一致。对比基线与消融，并在单模态设置评估稳健性；摘要称各组件均有贡献且单模态仍有效。

**Learning from Annotation Uncertainty: Entropy-Aware Curriculum for Speech Emotion Recognition**（论文 2992；presenter：John Hansen）
在 MSP-Podcast 2.0 九类 SER 上比较硬共识标签与主/合并票分布监督。分布目标更好对齐人类票分布（JSD/KLD）；硬监督部分受益于把歧义句归入 Other，分布监督则把不确定性分到各类。熵分层显示高歧义句仍难，但分布监督更好刻画感知不确定性。

### 连续情感时延、公平迁移与声学伪标签

**Revisiting Delay Compensation via Feature-Level Temporal Accumulation in Continuous Emotion Recognition**（论文 3030；presenter：Jian Xiang）
相对显式平移截断的 shift-based delay compensation，提出特征级时间累积的 ADC，不改原始输入–标签对齐而引入内禀时延。RECOLA 上对时延参数更稳健；唤醒偏好更短积分窗，效价偏好更长窗。

**Two-Sided Fairness Transfer for Gender-Neutral Speech Emotion Recognition with Partially Observed Attributes**（论文 3201；presenter：Woan-Shiuan Chien）
公平需说话人侧与评分者侧同时中立，但目标集常只观测一端性别。两阶段：对抗去偏细调 CLAP 得单端公平模型；由源集说话人/评分者公平模型差定义 ATT2Fair 任务向量，推断目标集缺失端公平模型。摘要强调部分属性监督下的公平迁移可行性。

**Conflict-Aware Pseudo-Labeling via Acoustic Signals for Multi-Task Speech Emotion Recognition**（论文 2118；presenter：Shunfei Liang）
多任务细粒度对齐常依赖昂贵转写。方法仅从声学经协作推断划分共识/冲突区：共识帧给硬伪标签，冲突区用话语级标签全局回填降噪。IEMOCAP、EmoDB、MELD 上摘要称无辅助文本即达先进。

## 本场要点
- SER 注意力存在精度与吞吐的明确权衡。
- 多标签与分布标签监督更贴近标注歧义，硬标签会掩盖不确定性。
- 图聚合、多损失与帧级/混合增强仍是单话语 SER 主力。
- 对话 MER 开始显式建模情感惯性；模态特异标签分布成新杠杆。
- 连续情感时延补偿可用特征累积替代标签平移。
- 双端性别公平可在属性部分观测下经任务向量迁移；声学伪标签可减少对转写的依赖。

## 覆盖核对
`1907 | How Attention Shapes Emotion: A Comparative Study of Attention Mechanisms for Speech Emotion Recognition`
`3458 | From Single to Multi-Label SER: Dataset and Mamba-Based Fusion Model`
`1219 | Multi-Loss Learning for Speech Emotion Recognition with Energy-Adaptive Mixup and Frame-Level Attention`
`969 | Segment-wise Embedding based Graph Attention Network for Effective Speech Emotion Recognition`
`3374 | Dual-Stream DNN-KAN Networks with Bangla-Specific Features for Speech Emotion Recognition`
`3532 | EII-SCL: Harnessing Emotional Inertia for Multimodal Emotion Recognition in Conversation`
`2076 | Leveraging Modality-Specific Label Distributions for Enhanced Multimodal Emotion Recognition`
`2992 | Learning from Annotation Uncertainty: Entropy-Aware Curriculum for Speech Emotion Recognition`
`3030 | Revisiting Delay Compensation via Feature-Level Temporal Accumulation in Continuous Emotion Recognition`
`3201 | Two-Sided Fairness Transfer for Gender-Neutral Speech Emotion Recognition with Partially Observed Attributes`
`2118 | Conflict-Aware Pseudo-Labeling via Acoustic Signals for Multi-Task Speech Emotion Recognition`
