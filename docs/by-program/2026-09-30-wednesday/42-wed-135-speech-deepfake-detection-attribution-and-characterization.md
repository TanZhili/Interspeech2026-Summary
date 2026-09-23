# Speech Deepfake Detection, Attribution and Characterization

- 日期：2026年9月30日（周三）
- 时间：16:30-18:30
- 形式：Oral
- Area：4
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场聚焦语音深度伪造检测的泛化：老年合成语音缺口、域泛化元学习中的梯度冲突、强化学习微调、域自适应双门控 MoE、质量感知多中心一类学习，以及时长变化下的自注意力偏置校正。

共同挑战是未见攻击、声学条件与说话人群体（尤其老年）上的域移。方法上从“单一真伪中心”扩展到质量子空间多中心，从监督微调扩展到 GRPO 类 RL，并从固定长度训练扩展到显式时长嵌入。

## 技术内容

### 老年 CodecFake、元学习与 RL 微调

**Bridging the Age Gap: Towards Detecting Neural Audio Codec Synthesized Elderly Speech Deepfake**（论文 2283；Orchid Chetia Phukan）  
提出 Elderly CodecFake Detection 任务并发布英中 Elderly-CodecFake 数据集。摘要称既往 CF 检测器泛化到老年语音很差；多模态基础模型因跨模态预训练接触老年内容更有效；BONSAI 以 JS 散度融合 LanguageBind 与 ImageBind，平均 EER 1.66%，优于单模型与竞争性基线。

**DGS-MLDG: Domain Gradient Surgery Guided Meta-Learning for Domain Generalization in Speech Deepfake Detection**（论文 1042；Youzhi TU）  
针对 MLDG 中 meta-train 与 meta-test 梯度冲突，提出域梯度手术（DGS）非对称投影，以及仅干预冲突层的 LW-DGS。摘要称相对平均 EER 分别降低约 5.29% 与 4.04%。

**Does Fine-tuning by Reinforcement Learning Improve Generalization in Binary Speech Deepfake Detection?**（论文 589；Xin Wang）  
探究 GRPO 强化学习微调相对监督微调的作用。摘要称纯 GRPO 在域外测试集提升表现并保持目标域，优于仅 SFT 与混合设定；消融提示负奖励可能是关键因素。

### MoE 门控、质量感知一类学习与时长感知注意力

**Domain-Adaptive Dual-Gating Mixture of Experts for Generalizable Speech Deepfake Detection**（论文 1778；Zhe LI）  
DADG-MoE 用基于 Sinc 的滤波器同时处理原始波形与 SSL 高层表征，并以域原型引导专家路由。摘要称在挑战性域外基准上相对基线 EER 相对最多降低 40.8%。

**QAMO: Quality-aware Multi-centroid One-class Learning For Speech Deepfake Detection**（论文 1098；Eng Siong Chng）  
在一类学习中引入多个质量感知中心，刻画真实语音按 MOS 质量分子空间的类内变异，并支持推理时无需质量标签的多中心集成打分。摘要称 In-the-Wild 上 EER 5.21%，优于先前 OCL 与质量感知系统。

**Duration-aware self-attention for speech deepfake detection**（论文 2200；Youzhi Tu）  
把由音频时长与片段偏移计算的时间嵌入写入自注意力，校正注意力偏置图。摘要称在 ASVspoof21、In-the-Wild 与 CodecFake 上，基于相对位置编码的 DASA 有效，有助于缓解时长变化。

## 本场要点

- 老年 CodecFake 暴露既有检测器群体盲区，多模态基础模型融合是一条有效路径。
- 域泛化元学习需处理梯度冲突；RL（GRPO）微调可改善域外泛化。
- 双门控 MoE 把低层声学与 SSL 表征及域原型路由结合。
- 一类学习从单中心走向质量感知多中心。
- 显式时长信息有助于纠正固定长度训练带来的注意力偏置。

## 覆盖核对

- 2283 | Bridging the Age Gap: Towards Detecting Neural Audio Codec Synthesized Elderly Speech Deepfake
- 1042 | DGS-MLDG: Domain Gradient Surgery Guided Meta-Learning for Domain Generalization in Speech Deepfake Detection
- 589 | Does Fine-tuning by Reinforcement Learning Improve Generalization in Binary Speech Deepfake Detection?
- 1778 | Domain-Adaptive Dual-Gating Mixture of Experts for Generalizable Speech Deepfake Detection
- 1098 | QAMO: Quality-aware Multi-centroid One-class Learning For Speech Deepfake Detection
- 2200 | Duration-aware self-attention for speech deepfake detection
