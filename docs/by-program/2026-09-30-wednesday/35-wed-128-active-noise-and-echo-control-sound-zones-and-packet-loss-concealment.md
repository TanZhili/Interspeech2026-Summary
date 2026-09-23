# Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment

- 日期：2026年9月30日（周三）
- 时间：14:00-16:00
- 形式：Poster
- Area：6
- 论文数：10
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场聚焦主动噪声控制（ANC）、个人声区（PSZ/SZC）、声学回声消除（AEC）与分组丢失隐藏（PLC），共同点是把控制变量从“线性滤波器权重”扩展到载体、非线性、方向预测与相位—幅度解耦等新维度。

声区控制侧，参量阵扬声器开始把超声载体当作可控量；微型扬声器场景则用数据驱动网络补偿非线性失真，并以“锚点扬声器”稳住亮区声压。ANC 侧则同时处理脉冲噪声冗余基函数、移动声源方向跟踪、微扬声器低频过冲与“保语音”约束。

通信前端侧，端侧全双工 AEC+降噪强调多路径对齐与极轻量；扩散模型被引入非因果 VQE；PLC 则明确分离幅度与缠绕相位。另一条线提出“主动语音增强”（ASE），在抑制干扰的同时主动抬高语音相关频段。

整体上，摘要共同指向：在功耗、时延与硬件非线性约束下，把物理先验与轻量网络、预测控制结合起来，以提升对比度、可懂度与通话稳健性。

## 技术内容

### 声区控制与定向渲染

**Carrier-Aware Sound Zone Control for Parametric Array Loudspeakers**（论文 2170；Mengtong Li）  
参量阵扬声器依赖超声载体与非线性自解调生成定向语音/音频。既有工作多优化边带激励，载体本身较少作为控制变量。本文提出载体感知声区控制框架，对边带与载体权重交替优化。摘要称仿真与实验均优于仅边带控制，实验在相同功率约束下宽带声对比度提升 11.2 dB、目标区声压级提升 7.0 dB。

**NCPSZ: A Nonlinear Control Network for Miniature Loudspeakers in Personal Sound Zone Applications**（论文 182；Liming Shi）  
微型扬声器非线性失真使线性 PSZ 控制明显退化。NCPSZ 采用非对称双网络：离线高保真 ModelNet 刻画扬声器非线性，并监督因果轻量 CtrlNet 实时运行。锚点耳麦扬声器维持亮区目标声压，CtrlNet 优化辅助扬声器抑制暗区泄漏。摘要称在智能手机防泄漏任务上相对线性 VAST 提升声对比度 3.78 dB，相对参数匹配因果 CNN 提升 1.80 dB。

### 主动噪声控制与“保语音”控制

**A Sparsity-Aware Robust Nonlinear Active Noise Control for Impulsive Noise Environments**（论文 122；Liming Shi）  
FLN 类非线性 ANC 在扩基时引入冗余，影响自适应效率与稳态性能。作者把重加权零吸引（RZA）正则写入 MOV-FsLMP，作为在线特征选择以抑制冗余系数并保持对脉冲干扰的鲁棒性。摘要称在 α 稳态脉冲噪声仿真下相对常规 MOV-FsLMP 稳态 MSE 改善约 1–2 dB，并提高主动降噪量。

**Predictive Directional Selective Fixed-Filter Active Noise Control for Moving Sources via a Convolutional Recurrent Neural Network**（论文 271；Boxiang Wang）  
方向选择性固定滤波器 ANC（D-SFANC）按到达方向选取预训练控制滤波器，但难跟踪移动非平稳噪声。PD-SFANC 用 CRNN 捕捉运动噪声时序动态并预测未来控制滤波器。摘要称数值仿真在多种运动场景下优于若干代表性 ANC 基线，改善跟踪与动态降噪。

**Active Noise Control With a Gain Constraint for Micro-Loudspeakers**（论文 2202；Liming Shi）  
固定滤波器 ANC 常最小化误差麦均方声压，但对微扬声器易引发低频机械过冲；级联高通会增加电子时延。本文在控制滤波器频响上对低频与目标降噪频段施加增益约束。摘要称仿真与实验证实该方法在降噪性能上有效。

**A Causal Reference-Enhanced Keep-Speech Active Noise Control Method**（论文 1608；Li Rao）  
提出因果低时延、参考增强的保语音 ANC（KSANC）：用 DNN 增强参考信号，抑制其中语音而保留噪声，从而在控制后更好保留误差信号中的语音。摘要称基于实测耳机冲激响应的实验表明，相对全部基线在嘈杂对话场景提升可懂度与语音质量，并对不同语音/噪声方向与信噪比具有鲁棒性。

**Active Constructive Interference for Speech**（论文 222；Ofir Yaish）  
提出主动语音增强（ASE）范式：既衰减失真，又放大语音相关频率以提升可懂度与感知质量。方法采用 Transformer-Mamba 架构与兼顾抑制与增强的任务损失。摘要称在去噪、去混响与反削波等多任务上优于既有基线，并公开演示与代码。

### 回声消除、降噪与丢包隐藏

**LMPAN: A Lightweight Multi-Path Alignment Network for Joint Full-Duplex Acoustic Echo Cancellation and Noise Suppression**（论文 191；Chengwei Liu）  
面向端侧全双工对话，联合 AEC 与噪声抑制。核心包括：参考、线性 AEC 输出与麦克风信号的多路径时能对齐；注意力动态融合增强 LAEC 与麦信号特征；面向 ASR/VAD 的动态目标后滤波；以及利用自监督表征的两阶段训练。摘要称模型仅 480K 参数、126 MACs，性能可比轻量 SOTA DeepVQE-S 并支持实时推理。

**DiffVQE: Hybrid Diffusion Voice Quality Enhancement Under Acoustic Echo and Noise**（论文 2337；Haljan Lugo）  
面向免提与扬声电话场景的联合回声控制与降噪，提出可复现的（仍非因果）扩散式 AEC 模型 DiffVQE。摘要称在拓扑、数据与训练框架可复现前提下，用 Interspeech 2025 URGENT Challenge 数据训练后，在回声/噪声控制、计算复杂度与模型规模上均优于判别式 DeepVQE。

**DDSN: A Physics-Aware Decoupled Dual-Stream Network for Speech Packet Loss Concealment**（论文 1295；Hao Tian）  
针对频域 PLC 常联合建模实虚部、忽视缠绕相位与幅度差异的问题，DDSN 解耦幅度与相位双流，并以 SARG 用幅度先验引导相位重建，同时用流形约束三角表示保持相位拓扑一致性。摘要称相对既有基线表现良好，并在长突发丢包下保持稳定重建。

## 本场要点

- 声区控制从边带优化扩展到载体维度，并针对微型扬声器非线性提出双网络与锚点策略。
- ANC 同时覆盖稀疏鲁棒非线性、移动源方向预测、微扬声器增益约束与“保语音”参考增强。
- ASE 把主动控制从“消噪”推向“抑制+语音频段增强”。
- 端侧联合 AEC/NS 强调多路径对齐与极轻量；扩散模型进入 VQE，但摘要标明 DiffVQE 仍非因果。
- PLC 明确解耦幅度与缠绕相位，并以幅度引导相位重建。

## 覆盖核对

- 2170 | Carrier-Aware Sound Zone Control for Parametric Array Loudspeakers
- 122 | A Sparsity-Aware Robust Nonlinear Active Noise Control for Impulsive Noise Environments
- 182 | NCPSZ: A Nonlinear Control Network for Miniature Loudspeakers in Personal Sound Zone Applications
- 191 | LMPAN: A Lightweight Multi-Path Alignment Network for Joint Full-Duplex Acoustic Echo Cancellation and Noise Suppression
- 222 | Active Constructive Interference for Speech
- 271 | Predictive Directional Selective Fixed-Filter Active Noise Control for Moving Sources via a Convolutional Recurrent Neural Network
- 1295 | DDSN: A Physics-Aware Decoupled Dual-Stream Network for Speech Packet Loss Concealment
- 1608 | A Causal Reference-Enhanced Keep-Speech Active Noise Control Method
- 2202 | Active Noise Control With a Gain Constraint for Micro-Loudspeakers
- 2337 | DiffVQE: Hybrid Diffusion Voice Quality Enhancement Under Acoustic Echo and Noise
