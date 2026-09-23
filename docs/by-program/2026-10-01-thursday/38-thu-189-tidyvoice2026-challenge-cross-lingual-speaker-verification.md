# TidyVoice2026 Challenge: Cross-Lingual Speaker Verification

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Challenge
- Area：14
- 论文数：8
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

TidyVoice2026 跨语说话人确认挑战的核心是说话人身份与语言线索纠缠：同说话人跨语接受、同语不同说话人拒绝最难。参赛系统普遍在预训练骨干上叠加语言不变训练——情节原型、对抗/梯度反转、正交投影、层选潜交叉注意力适配器、双 LoRA 语言锚定对抗，以及嵌入/后端/分数级语言补偿。

后端上出现流形约束神经 PLDA 与动态难样本挖掘；数据侧用多语噪声混响增强与零样本 TTS 合成扩语种。排名靠前系统报告约 1.4% 量级 EER，并强调前端去语言后强后端优势可能缩小。

## 技术内容

### 情节原型、渐进学习与正交–PLDA

**L-Proto: Language-Aware Episodic Prototypical Training for Multilingual Speaker Verification**（论文 410；Hyung-Seok Oh）每情节从单一语言采样说话人，降低训练中语言驱动变异，促使嵌入聚焦身份。TidyVoice 上相对常规微调与随机情节采样，多骨干一致提升。

**Progressive Learning for Robust Speaker Representation**（论文 2097；Harish Rajamani）基于 ReDimNet，在大规模多语语料上强噪声/混响增强，并以三元组损失训练后网络解耦身份与语言内容。匹配/失配语言场景 EER 1.58%。

**Orthogonal Feature Projection and Manifold-Constrained Neural PLDA for the TidyVoice2026 Cross-Lingual Speaker Verification Challenge**（论文 3003；Yuxuan Du）正交投影解耦冗余自监督特征并动态融入语言无关分量；流形约束神经 PLDA 做判别优化且遵守概率生成约束，辅以多语动态难样本挖掘。融合系统两赛道 EER 1.39%/1.95%，42 队中第 1。

### 适配器、对抗解耦与 SSL 前端

**LaS-LCA: Layer-Selected Latent Cross-Attention Adapters and Margin-Mixup for Robust Cross-Lingual Speaker Verification**（论文 1255；Xu Shen）层选择适配器隔离说话人特质与语言噪声，共享潜交叉注意力与卷积将多层特征蒸馏到语言无关潜空间，并以嵌入级 margin-mixup 减轻过拟合。TidyVoiceX 上 EER 1.40%。

**Dual-LoRA: Parameter-Efficient Adversarial Disentanglement for Cross-Lingual Speaker Verification**（论文 2274；Qituan Shangguan）向冻结骨干注入任务因子化 LoRA；Language-Anchored Adversary 用显式语言支锚定判别器，使对抗梯度瞄准真实语言线索而非任意相关。验证 EER 0.91%，挑战官方排名第 3。

**Cross-Lingual Speaker Verification with Self-Supervised Pre-Trained Models**（论文 1799；Jinghan Peng）以大规模自监督 PTM 为前端，再训下游说话人嵌入网络解耦身份与语言。tv26_eval-A / -U 上 EER 2.21%/2.99%（队名 T02）。

**Language-Invariant Multilingual Speaker Verification for the TidyVoice 2026 Challenge**（论文 2437；Xiaoxiao Miao）以 w2v-BERT 2.0 为骨干，加 Layer Adapters 与多尺度特征聚合，梯度反转语言对抗，并用多语零样本 TTS 合成扩语种。摘要称微调大预训练模型具竞争力，对抗与合成增强均有额外收益。

**Effectiveness of Language Variability Compensation in Speaker Verification**（论文 3367；Oldřich Plchot）系统比较嵌入、后端与分数级语言补偿；各路径独立带来一致可比增益。PSVM/SG-TPSDA 等强后端在语言纠缠嵌入上表现强，但前端经对抗去语言后优势减弱。提交系统 tv26_eval-A EER 2.53%。

## 本场要点

- 跨语 SV 关键是抑制语言簇化、保留说话人判别力。
- 情节单语采样、正交投影与语言锚定对抗从不同角度解耦。
- 适配器+margin-mixup 适合冻结大模型上的跨语有限数据。
- 神经 PLDA/难样本挖掘与分数级补偿构成完整流水线杠杆。
- TTS 合成与噪声混响增强补充跨语训练多样性。
- 前端已去语言时，强后端相对优势可能减小。

## 覆盖核对

| id | title |
|---|---|
| 410 | L-Proto: Language-Aware Episodic Prototypical Training for Multilingual Speaker Verification |
| 2097 | Progressive Learning for Robust Speaker Representation |
| 3003 | Orthogonal Feature Projection and Manifold-Constrained Neural PLDA for the TidyVoice2026 Cross-Lingual Speaker Verification Challenge |
| 1255 | LaS-LCA: Layer-Selected Latent Cross-Attention Adapters and Margin-Mixup for Robust Cross-Lingual Speaker Verification |
| 2274 | Dual-LoRA: Parameter-Efficient Adversarial Disentanglement for Cross-Lingual Speaker Verification |
| 1799 | Cross-Lingual Speaker Verification with Self-Supervised Pre-Trained Models |
| 2437 | Language-Invariant Multilingual Speaker Verification for the TidyVoice 2026 Challenge |
| 3367 | Effectiveness of Language Variability Compensation in Speaker Verification |
