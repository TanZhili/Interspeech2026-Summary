# Neural Speech Enhancement: Survey, Diffusion and Flow Matching

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral（Area 6）
- 论文数：5
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场以综述串联单通道神经语音增强史，再聚焦离散扩散、Schrödinger Bridge 与“漂移”生成等少步/单步推理方案。主线是：增强从映射/掩蔽与时域回归，转向分布采样式生成，并借预训练表征与桥接轨迹压低迭代成本。

综述勾勒浅层网络→时频映射/掩蔽→时域建模→生成式→speech foundation model 重用，并反思评测、鲁棒性与“干净语音”定义。实证研究则分别在 codec 码空间做吸收离散扩散；用 SB+Mamba 单步联合去噪去混响；把去噪写成均衡问题的 DriftSE；以及可学习 SB 的单次扩散 EffDiffSE+。

共同瓶颈是多步扩散的推理复杂度；共同策略是单步/少步轨迹匹配、桥接初始化与架构协同（Mamba 相对 MHSA/LSTM 在 SB 下更强）。评测上既有非侵入客观指标，也有 PESQ/POLQA/NISQA 等综合榜。

## 技术内容

### 综述与离散扩散

**Monaural Speech Enhancement: From Shallow Networks to Speech Foundation Models**（论文 （无编号）；Sabato Marco Siniscalchi）
Survey Talk 回顾单通道神经增强：早期浅层方法、时频域映射/掩蔽与全连接网络相对经典统计估计器的优势、时域建模、将增强重铸为干净语音分布采样的生成范式，以及大规模预训练语音模型的再利用，并讨论评测、鲁棒性与“干净”概念变迁。

**Absorbing Discrete Diffusion for Speech Enhancement**（论文 659；Philippe Gonzalez）
用吸收离散扩散建模给定噪声码条件下的干净语音码分布（ADDSE），并提 RQDiT 以非自回归方式建模 RVQ 层级。两数据集上非侵入客观指标具竞争力，尤其低 SNR 与少采样步时；代码与样例公开。

### Schrödinger Bridge 与单步生成

**Schrödinger Bridge Mamba for One-Step Speech Enhancement**（论文 682；Jing Yang）
SBM 结合 Schrödinger Bridge 训练与 Mamba。联合去噪去混响实验称在多指标上优于强生成与判别方法，且仅一步推理并具可流式的实时因子。消融显示 SB 相对常规映射跨架构一致提升，且 Mamba 在 SB 下强于 MHSA 与 LSTM。

**Speech Enhancement Based on Drifting Models**（论文 833；Liang Xu）
DriftSE 将去噪写为均衡问题：用学习到的 Drifting Field 推动映射的 pushforward 分布匹配干净语音分布，原生单步推理，并因匹配分布而利于无配对数据。考察自噪声观测的直接映射与自高斯先验的随机条件生成。VoiceBank-DEMAND 上称单步高保真并优于多步扩散基线。

**Learnable Schrödinger Bridge and Activations for Efficient Diffusion-based Speech Enhancement**（论文 2465；Yihui Fu）
EffDiffSE+ 含条件 DNN、桥接 DNN 与可学习 SB：单次反过程高斯初始化、辅助网络自适应桥接初态、拓扑改进。摘要称在 PESQ、POLQA、NISQA、UTMOS、ESTOI、LPS、SBScore、SpkSim 与主观 MOS 上总体优于顶尖开源时/频域扩散基线。

## 本场要点

- 增强范式正从确定性映射转向生成式分布匹配，并与 foundation model 时代衔接。
- 离散扩散可在神经编解码码空间做非自回归增强，利好低 SNR 与少步采样。
- Schrödinger Bridge 支持高质量单步增强，并与 Mamba 等序列骨干协同。
- DriftSE 以漂移场做分布匹配，原生单步且可面向无配对训练。
- 可学习 SB 与激活/拓扑改进是压低扩散迭代成本的另一路径。

## 覆盖核对

- （无编号） | Monaural Speech Enhancement: From Shallow Networks to Speech Foundation Models
- 659 | Absorbing Discrete Diffusion for Speech Enhancement
- 682 | Schrödinger Bridge Mamba for One-Step Speech Enhancement
- 833 | Speech Enhancement Based on Drifting Models
- 2465 | Learnable Schrödinger Bridge and Activations for Efficient Diffusion-based Speech Enhancement
