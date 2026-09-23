# Audio-Visual and Generative Target Speaker Extraction

- 日期：2026年9月30日（周三）
- 时间：16:30-18:30
- 形式：Oral
- Area：6
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场围绕目标说话人提取（TSE）与视听语音增强：一步均值流生成、视觉仅做选择的插拔式解耦、扩散 AVSE 的对比跨模态对齐、粗到细生成式语言模型 TSE、视位引导的在线轻量视觉分支，以及 LLM 可解释奖励的强化学习 AVSE。

核心张力是：生成式方法提升质量但常需多步采样；深度视听融合可能受野外数据噪声牵制；实时部署又要求因果与轻量视觉前端。场内答案分别是一步生成、冻结音频骨干+潜空间转向、对比对齐增强视觉利用，以及把视觉压缩为视位线索。

## 技术内容

### 一步生成与分离—选择解耦

**MeanFlow-TSE: One-Step Generative Target Speaker Extraction with Mean Flow**（论文 109；Riki Shimizu）  
在 AD-FlowTSE 范式上用均值流目标训练一步生成 TSE，在背景与目标源之间由混合比控制流。摘要称在 Libri2Mix 上分离质量与感知指标优于既有生成式 TSE，且仅需单次推理。

**Plug-and-Steer: Decoupling Separation and Selection in Audio-Visual Target Speaker Extraction**（论文 706；Doyeop Kwak）  
将高保真分离交给冻结音频骨干，视觉模态仅负责目标选择；用最小线性潜空间转向矩阵（LSM）把目标说话人锚定到指定通道。摘要称在四种代表性架构上有效保留声学先验，感知质量可比原骨干。

### 扩散 AVSE、生成式 LM-TSE 与轻量视觉

**Audio-visual Contrastive Alignment for Diffusion-based Visual-conditioned Speech Enhancement**（论文 766；Colombe Mboungou）  
在保持后验采样框架不变前提下，为视觉条件扩散 AVSE 训练目标加入对比视听损失。摘要称在匹配/失配测试上干扰抑制、信号重建与感知质量一致提升，低 SNR 收益最大。

**GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-Fine Generative Language Model**（论文 893；Haoyang Li）  
两阶段仅解码器生成 LM：先预测粗语义 token，再生成细声学 token；使用连续 SSL/编解码嵌入，并以 Frozen-LM Conditioning 与 DPO 缓解曝光偏差、对齐感知偏好。摘要称在 Libri2Mix 上语音质量、可懂度与说话人一致性优于先前 LM 系统。

**Online Audio-Visual Target Speaker Extraction with Viseme-Guided Lightweight Visual Pretraining**（论文 948；Zixuan Li）  
用视位作为视觉引导，相对常规 VSR 预训练表征更轻量、稳健、可解释，并提出在线视位引导 TSE。摘要称在最低计算预算下取得强性能。

**LLM-Guided Reinforcement Learning for Audio-Visual Speech Enhancement**（论文 1816；Chih-Ning Chen）  
用音频 LLM 对增强语音生成自然语言描述，再经情感分析转为 1–5 分作为 PPO 奖励微调预训练 AVSE。摘要称在 AVSEC-4 上优于监督基线与 DNSMOS 奖励 RL 基线，覆盖 PESQ、STOI、神经质量指标与主观听测。

## 本场要点

- 均值流使生成式 TSE 可一步推理，利于低时延。
- 视觉可用于“选择/转向”而非重学分离，以保留音频骨干保真度。
- 对比对齐可增强扩散 AVSE 对视觉信息的利用，尤在低 SNR。
- 粗到细 LM-TSE 与 DPO 提升生成式提取质量与说话人一致性。
- 视位预训练与 LLM 可解释奖励分别服务部署轻量化与感知对齐优化。

## 覆盖核对

- 109 | MeanFlow-TSE: One-Step Generative Target Speaker Extraction with Mean Flow
- 706 | Plug-and-Steer: Decoupling Separation and Selection in Audio-Visual Target Speaker Extraction
- 766 | Audio-visual Contrastive Alignment for Diffusion-based Visual-conditioned Speech Enhancement
- 893 | GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-Fine Generative Language Model
- 948 | Online Audio-Visual Target Speaker Extraction with Viseme-Guided Lightweight Visual Pretraining
- 1816 | LLM-Guided Reinforcement Learning for Audio-Visual Speech Enhancement
