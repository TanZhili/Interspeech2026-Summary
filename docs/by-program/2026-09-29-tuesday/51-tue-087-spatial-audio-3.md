# Spatial Audio 3

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Poster
- **Area**：5
- **论文数**：10
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场集中于双耳合成、个性化 HRTF、分布式声学场景理解与车载个人声区。单声道/文本到双耳生成强调几何或空间提示条件化、时频域耳间关系建模，以及粗估计后再生成精炼的两阶段流程。HRTF 个性化从网格离散预测走向连续算子学习与物理可微渲染，并用双耳声学信息辅助稀疏测量重建。

理解侧把多房间遮挡下的分布式麦克风图网络与 LLM 叙事结合，并把空间音频语言对齐推进到多事件时空细粒度对比学习。应用侧引入心理声学加权的车载 MU-MIMO 预编码，以及矢状面定位中生态声源先验与空间先验的贝叶斯评估。整体上，可控空间提示、物理约束与感知加权成为共同关键词。

## 技术内容

### 单声道/文本到双耳合成

**AURA: Audio-Geometry Conditioned U-Net Refinement with Flow Matching for High-Fidelity Monaural-to-Binaural Synthesis**（论文 87；Wenjie Zhang）  
从单声道推断空间线索同时保持音色细节仍难。AURA 两阶段显式建模单声道与声源方向关系：第一阶段全局语境与局部纹理得到粗双耳估计，第二阶段生成机制精炼空间线索与频谱细节。摘要称在主客观指标上优于 SOTA，并给出 Wave-L2 对比数值。

**TTBA: Spatial Prompted Text to Binaural Audio Generation Using Transformer**（论文 602；Changjun He）  
文本音频模型难生成方向可控、空间感知准确的双耳信号。TTBA 结合交叉排列离散表征与 Transformer 自回归骨干联合建模语义与空间线索，并用空间提示编码器把显式空间提示融入文本条件。以单声道生成模型为指导，强调内容准确与耳间差异；在 BEWO-1M 上摘要称可生成具空间意识与可控方向性的双耳音频。

**Spec2Spatial: A Time-Frequency Spatial Attention Network for Binaural Audio Synthesis**（论文 607；Changjun He）  
提出时频空间注意网络：耳间空间注意捕捉频域左右关系，条件融合残差网络用声源位置调节时频特征。在 Binaural Speech 数据上摘要给出 DILD、DITD、MRSTFT 等 SOTA 数值。

### HRTF 个性化与物理/声学辅助

**GISNO: Neural Operator-based HRTF Personalization from 3D Meshes via Differentiable Helmholtz Rendering**（论文 366；Liming Shi）  
将 HRTF 预测重述为连续算子学习：几何知情球面神经算子结合可微 Helmholtz 积分渲染，从 3D 头几何映射到连续边界压力场。在 HUTUBS 上摘要称对数谱失真优于代表基线，并支持未见空间密度、距离与频率上的多维零样本泛化。

**SA-HRTF: A Sound-Assisted Approach to Personalized HRTF Modeling**（论文 1995；Qingyin Zhao）  
稀疏测量下个性化 HRTF 难。双分支：主分支用既有库结构特征给初估，辅分支从声音信号提取感知线索作补充预测，融合得到更准个性化 HRTF。摘要称实验验证有效。

### 场景理解、ASC、车载 PSZ 与定位先验

**Geometry-Informed Distributed Acoustic Scene Understanding**（论文 821；Yiyuan Yang）  
多房间环境中墙门遮挡使集中式阵列失效。用分布式麦克风，经音频谱图 Transformer 与拓扑感知图网络融合时空特征，解码为离散语义三元组，再由冻结 LLM 结合环境几何做空间理解、推断缺失转移并生成物理一致叙事。自定义多房间仿真上优于集中式基线并改善遮挡下空间一致性。

**Branch-wise Complementary Attention for Acoustic Scene Classification**（论文 865；Seung-Gyu Han）  
多分支卷积常简单聚合而未显式建模互补关系。BCA 按感受野特性跨分支分配通道、时间、频率与联合时频注意图，集成到 Rep-Mobile 后在 TAU Urban Acoustic Scenes 2020/2022 Mobile 上持续优于既有注意机制。

**CoSTALA: Compositional Spatio-Temporal Audio-Language Alignment via Multi-Grain Hierarchical Contrastive Learning**（论文 1110；Peiwei Ren）  
日常空间场景中多事件序列难以靠全局粗粒度对比对齐。CoSTALA 用多粒度层次损失显式建模时间依赖并锚定单事件语义纯度，服务时空音频理解。

**Perceptually Weighted Minimum Mean Square Error Precoding for Acoustic Multi-User MIMO in Vehicular Personal Sound Zones**（论文 1191；Huihui Wei）  
将心理声学掩蔽模型纳入 WMMSE，对感知敏感时频区加重失真惩罚、在目标语音强掩蔽区放宽约束，协调预编码以平衡用户间干扰与目标失真。用实测车舱冲激响应验证，摘要称客观语音质量相对基线有改进。

**Bayesian Model-Based Assessment of Spatial and Source Priors in Sagittal-Plane Sound Localization**（论文 3494；Yunda Chen）  
矢状面极向定位不适定。用带生态声源先验与五种空间先验的贝叶斯观察者，在 CI 样频谱分辨率降低条件下对照人类响应。摘要称模型捕捉分辨率改善时误差下降；生态声源先验额外收益有限，预测对空间先验配置更敏感，非对称变体总体更吻合人类数据。

## 本场要点

- 双耳合成走“几何/空间条件 + 时频耳间建模 + 精炼”路线。
- 文本到双耳需显式空间提示与耳间差异目标。
- HRTF 个性化结合连续神经算子、可微物理渲染或声音辅助分支。
- 分布式麦克风 + 几何条件 LLM 叙事应对多房间遮挡场景理解。
- 车载个人声区预编码引入心理声学加权；矢状面定位依赖空间先验配置。

## 覆盖核对

| id | title |
|---|---|
| 87 | AURA: Audio-Geometry Conditioned U-Net Refinement with Flow Matching for High-Fidelity Monaural-to-Binaural Synthesis |
| 366 | GISNO: Neural Operator-based HRTF Personalization from 3D Meshes via Differentiable Helmholtz Rendering |
| 602 | TTBA: Spatial Prompted Text to Binaural Audio Generation Using Transformer |
| 607 | Spec2Spatial: A Time-Frequency Spatial Attention Network for Binaural Audio Synthesis |
| 821 | Geometry-Informed Distributed Acoustic Scene Understanding |
| 865 | Branch-wise Complementary Attention for Acoustic Scene Classification |
| 1110 | CoSTALA: Compositional Spatio-Temporal Audio-Language Alignment via Multi-Grain Hierarchical Contrastive Learning |
| 1191 | Perceptually Weighted Minimum Mean Square Error Precoding for Acoustic Multi-User MIMO in Vehicular Personal Sound Zones |
| 1995 | SA-HRTF: A Sound-Assisted Approach to Personalized HRTF Modeling |
| 3494 | Bayesian Model-Based Assessment of Spatial and Source Priors in Sagittal-Plane Sound Localization |
