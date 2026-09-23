# Explainability for Compliance and Trust in Speech AI

- 日期：2026年9月30日（星期三）
- 时间：16:30-18:30
- 形式：Special Session
- Area：14
- 论文数：16
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本专场围绕语音 AI 的可解释性、合规与信任：深伪检测证据定位、说话人嵌入可听分解、情感描述符校正、多模态句嵌入诊断，以及分离/编解码/空间 SSL 内部机制探测；同时覆盖 SLM 越狱攻防、LALM 音文融合因果追踪、临床语音中的人群差异审计，与交叉注意力作为解释代理的限度。

方法谱从归因与因果干预（Integrated Gradients、因果掩码、causal tracing、影响函数样本级解释），到稀疏自编码器、因子化线性投影、可听组件分解，再到将 XAI 证据接入免训练多模态 LLM 生成自然语言说明。共同诉求是：解释须与决策因果相关、可被人核验，且不能用全局平均掩盖人口学/语言差异。

安全线与可解释线交织：多模态联合越狱远强于单模态；统一安全子空间跨模态转移拒绝向量。工程上，对稳定层注意力缓存等“解释驱动加速”开始出现。对从业者而言，本场强调：分数不够，必须说明“听了什么、在何处融合、对谁可靠”。

## 技术内容

### 深伪、说话人与情感的可听/可验解释

**What Do Deepfake Speech Detectors Actually Hear?**（论文 123；Vojtěch Staněk）  
对时间对齐 SSL 表示做 Integrated Gradients，定位决策证据并人工标注高归因区语义。ASVspoof 5 上三款 WavLM 检测器虽性能相近但线索不同：AASIST 偏非语音/环境，CA-MHFA 偏局部音素伪影，SLS 偏词边界与谱完整性；因果掩码主线索后性能下降，支持解释语义。

**LISE : Listenable Interpretable Speaker Embeddings**（论文 537；Xiaoliang Wu）  
无标签框架将预训练说话人嵌入分解为少量组件，保持 x-vector/ECAPA-TDNN 上 EER 几乎不降；听音实验中被试凭组件区分说话人准确率 83.9%，验证组件对人类可听可解释。

**Explainable and Trustworthy Speech Emotion Recognition Using Confidence Score and Reinforcement Learning Rectified Speech Emotion Descriptors**（论文 1683；Youjun Chen）  
对自动标注的情感描述符用置信度筛选与 RL 在线校正，服务可解释 SER。IEMOCAP/MELD 上相对无选择与无校正基线绝对提升 2.9%/3.3%（相对 3.7%/5.4%）。

**XAI-Grounded Explanation Generation for Speech Deepfake Detection with Training-Free Multimodal Large Language Models**（论文 161；Yupei Li）  
免训练框架把 XAI 证据接入多模态 LLM，生成 grounded 自然语言解释；基于 PartialSpoof 构建接地解释数据，含 XAI 的方法 inside accuracy 提升逾 45%，经人工与忠实性核验。

**Towards Dys-XAI: Influence-Based Explanations for Dysarthria Severity Assessment**（论文 538；Xiaoliang Wu）  
用梯度影响近似为每条预测找出支持性与竞争性训练样本，提供可审计的实例级解释；删除 5–20% 高影响样本会系统改变预测，验证解释有效。

### 嵌入诊断、融合机制与空间相位

**FLiP: Towards understanding and interpreting multimodal multilingual sentence embeddings**（论文 3315；Santosh Kesiraju）  
用因子化线性投影从 LaBSE、SONAR、Gemini 等嵌入恢复词汇内容，召回逾 75%，显著优于非因子化基线，并揭示模态与语言偏置，无需下游任务即可做内在诊断。

**Inside the Latent Flow: Causal Deciphering of Attention Dynamics in Audio Separation Foundation Models**（论文 2684；Yuxuan Chen）  
对 SAM Audio 做推理时确定性因果探测：加性注入控语义身份，交叉注意力细化声学结构；稳定层早建时间骨架，快速层继续消伪影。据此提出免训练 LSAC，缓存稳定层注意力，自注意力计算约减 25%，质量保留显著优于朴素减步。

**Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information**（论文 811；Shih-Heng Wang）  
用 SAE 分解 NAC 稠密表示并量化口音相关可解释性；DAC 与 SpeechTokenizer 最高。声学导向 NAC 口音信息主要在稀疏激活幅度，语音导向更依赖激活位置；低码率 EnCodec 变体可解释性更高。

**Spectro-Temporal Interference Confounds Phase Encoding in Spatial Audio Foundation Models**（论文 2873；Yuxuan Chen）  
基于双耳掩蔽电平差评测相位精细结构编码。通用双耳 SSL 相位敏感极弱，专用空间 SSL 有可观但未达上限的 BMLD；渐进消融显示通用模型依赖谱—时干扰纹理而非跨通道相位，语音高检出率常混淆于宽带包络。

**What Do Neural Networks Learn for TDOA Estimation? A Cross-Architecture Probing Study**（论文 3246；Yaozhong Kang）  
把 GCC-PHAT 数学步骤作诊断目标探测 MLP/CNN/Transformer：跨功率一致涌现，PHAT 白化未涌现，网络学到保留逐频可靠性的幅度感知加权。噪声下从经典与神经管线去掉 PHAT 反而更好；混响真实数据上端到端自适应加权误差更低。

**Cross-Attention is Half Explanation in Speech-to-Text Models**（论文 40；Luisa Bentivogli）  
比较交叉注意力与特征归因显著性：中等对齐，聚合头/层更好，但交叉注意力仅捕获约 50% 输入相关性，至多 52–75% 编码器显著性，不宜单独作为 S2T 行为代理。

**Causal Tracing of Audio-Text Fusion in Large Audio Language Models**（论文 1118；Wei-Chih Chen）  
对 DeSTA、Qwen、Voxtral 做层/token 因果追踪：融合策略从渐进到晚期突变不等；末 token 成信息瓶颈检索音频；中间位置存在类注意力查询机制拉取任务相关音频上下文。

### 安全子空间、越狱与临床公平审计

**On Optimizing Multimodal Jailbreaks for Spoken Language Models**（论文 309；Aravind Krishnan）  
提出 JAMA，联合 GCG 与 PGD 同时扰动音文两模态；四款 SOTA SLM 上越狱率相对单模态高 1.5×–20×；顺序攻击可快 4×–6×。结论：单模态安全不足以保护稳健 SLM。

**A Unified Safety Subspace Exists in Speech Language Models**（论文 2797；Nurdaulet Mukhituly）  
发现跨模态共享安全子空间，PCA 显现拒绝与越狱遵从边界；沿边界因果干预可无训练切换行为。音频拒绝向量使文本越狱成功率 76.5%→2.2%，文本拒绝向量使音频 79.0%→3.1%；在 Qwen2-Audio 与 GLM-4-Voice 及五种攻击上可转移。

**Do Learned Layer Weights Reflect Pretrained Information Structure in Self-Supervised Speech Models?**（论文 566；Yaroslav Getman）  
用层表示聚类与音素/词标签的调整互信息度量预训练信息结构，在 13 个 SSL 模型上与可学习层权重显著相关；10 分钟监督下相关高于 1 小时；对比式模型相关可达 0.98，聚类式较弱。

**Disentangling Acoustic Cues in Alzheimer’s Pathology and Perception: The Roles of Language and Gender**（论文 1149；Liu He）  
分别预测临床 AD 与人类感知分数，用 SHAP 比较特征重要性。病理—感知对齐在普通话与女性显著，在希腊语与男性消失且病理模型未超机会水平；全局 XAI 会掩盖人口学分歧，需人群特异性审计。

## 本场要点

- 深伪检测器“听什么”可用时域归因 + 因果掩码验证，且模型间线索不同。
- 说话人嵌入可分解为可听组件；情感描述符可用置信度与 RL 校正。
- 交叉注意力只是半解释；LALM 融合位置与策略因模型而异。
- NAC/分离/TDOA 内部机制探测揭示编码偏置与可加速稳定层。
- SLM 需多模态安全；统一安全子空间支持跨模态拒绝向量迁移。
- 临床语音解释必须按语言与性别做人群审计，避免全局解释假象。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 40 | Cross-Attention is Half Explanation in Speech-to-Text Models |
| 123 | What Do Deepfake Speech Detectors Actually Hear? |
| 161 | XAI-Grounded Explanation Generation for Speech Deepfake Detection with Training-Free Multimodal Large Language Models |
| 309 | On Optimizing Multimodal Jailbreaks for Spoken Language Models |
| 537 | LISE : Listenable Interpretable Speaker Embeddings |
| 538 | Towards Dys-XAI: Influence-Based Explanations for Dysarthria Severity Assessment |
| 566 | Do Learned Layer Weights Reflect Pretrained Information Structure in Self-Supervised Speech Models? |
| 811 | Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information |
| 1118 | Causal Tracing of Audio-Text Fusion in Large Audio Language Models |
| 1149 | Disentangling Acoustic Cues in Alzheimer’s Pathology and Perception: The Roles of Language and Gender |
| 1683 | Explainable and Trustworthy Speech Emotion Recognition Using Confidence Score and Reinforcement Learning Rectified Speech Emotion Descriptors |
| 2684 | Inside the Latent Flow: Causal Deciphering of Attention Dynamics in Audio Separation Foundation Models |
| 2797 | A Unified Safety Subspace Exists in Speech Language Models |
| 2873 | Spectro-Temporal Interference Confounds Phase Encoding in Spatial Audio Foundation Models |
| 3246 | What Do Neural Networks Learn for TDOA Estimation? A Cross-Architecture Probing Study |
| 3315 | FLiP: Towards understanding and interpreting multimodal multilingual sentence embeddings |
