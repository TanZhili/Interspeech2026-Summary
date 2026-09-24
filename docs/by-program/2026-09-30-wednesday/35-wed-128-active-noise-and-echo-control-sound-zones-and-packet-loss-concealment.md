# Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：6
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦主动噪声控制（ANC）、个人声区（PSZ/SZC）、声学回声消除（AEC）与分组丢失隐藏（PLC），共同点是把控制变量从“线性滤波器权重”扩展到载体、非线性、方向预测与相位—幅度解耦等新维度。

声区控制侧，参量阵扬声器开始把超声载体当作可控量；微型扬声器场景则用数据驱动网络补偿非线性失真，并以“锚点扬声器”稳住亮区声压。ANC 侧则同时处理脉冲噪声冗余基函数、移动声源方向跟踪、微扬声器低频过冲与“保语音”约束。

通信前端侧，端侧全双工 AEC+降噪强调多路径对齐与极轻量；扩散模型被引入非因果 VQE；PLC 则明确分离幅度与缠绕相位。另一条线提出“主动语音增强”（ASE），在抑制干扰的同时主动抬高语音相关频段。

整体上，摘要共同指向：在功耗、时延与硬件非线性约束下，把物理先验与轻量网络、预测控制结合起来，以提升对比度、可懂度与通话稳健性。

## 论文技术总结

# Carrier-Aware Sound Zone Control for Parametric Array Loudspeakers

- 论文编号：2170
- 报告人：Mengtong Li
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/li26da_interspeech.pdf

## 问题
参量阵扬声器（PAL）靠超声载波与边带非线性自解调产生可闻声；既有声区控制（SZC）多只优化边带激励，把载波当固定背景，自由度不足，声学对比度与解调效率受限。

## 方法
提出载波感知 SZC：对称调制结构下分别测量边带条件与载波条件有效传递函数 Gs(q)、Gc(w)，使解调场对边带权重 w 或载波权重 q 近似线性。采用有限阶段交替优化：初始载波全 1 → 测 Gs 优化边带 → 测 Gc 优化载波（映射为共轭）→ 再对齐边带。以 ACC 为验证；仿真用 k-space，实验 24×24 列 PAL（40 kHz 载波）、消声室扫描。

## 实验与结果
相对仅边带 ACC，载波感知在亮区更集中、暗区泄漏更少（仿真与实测一致）。宽带白噪声实验、相同功率约束下，总 AC 由 12.4 dB 升至 23.6 dB（+11.2 dB），亮区总 SPL +7.0 dB。超声场显示载波与边带空间对齐是增益来源。

## 结论
将载波作为主动控制维可显著提升 PAL 声区对比与解调效率，利于紧凑定向空间音频/私密语音渲染。

## 点评
抓住 PAL“解调∝载波×边带”的物理本质，把被忽视的载波纳入 ACC，比继续堆边带自由度更对症。有限交替避免反复重测成本，工程务实；载波优化在单音频点（1 kHz）完成再宽带对齐，宽带最优性仍可能受限。


# A Sparsity-Aware Robust Nonlinear Active Noise Control for Impulsive Noise Environments

- 论文编号：122
- 报告人：Liming Shi
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/xu26_interspeech.pdf

## 问题
FLN 非线性 ANC 扩展基函数冗余，抬高过量 MSE、收窄稳定步长；MOV-FsLMP 虽抗冲击并约束输出功率，仍缺乏在线特征选择。

## 方法
在 MOV-FsLMP 代价上加 RZA（对数和近似 L0）正则：Jprop = E[|e|^p]+λE[y²]+ρrza Σ log(1+ε|wi|)；更新含鲁棒 Lp 项、输出约束与逐元素零吸引。理论指出稀疏剪枝降低有效输入能量、扩大 μmax。仿真：α=1.6 SαS 冲击、非线性主路径、三角 FLN（P=3），对比 FxLMS/FsLMS/MOV-FsLMP。

## 实验与结果
最优步长下稳态 MSE 较基线约低 1–2 dB。大步长 μ=0.02 时基线边缘发散，所提方法仍收敛至约 −6.5～−3 dB。稳定性扫描显示可容忍更大 μ；摘要亦报告相同配置下更高 ANR。复杂度仍 O(L)。

## 结论
稀疏感知 MOV-FsLMP 可在冲击噪声与非线性下同时改善稳态误差与稳定域，适合实用非线性 ANC。

## 点评
把“FLN 过参数化”当作与冲击鲁棒同等重要的问题，用 RZA 做在线剪枝，设计简洁。结论主要来自合成路径仿真，真实扬声器饱和与声学二次路径的外推还需实测。


# NCPSZ: A Nonlinear Control Network for Miniature Loudspeakers in Personal Sound Zone Applications

- 论文编号：182
- 报告人：Liming Shi
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/gong26_interspeech.pdf

## 问题
个人声区（PSZ）线性方法在微型扬声器强非线性失真下失效；辅助扬声器高电平反相消漏易产生谐波，线性滤波器难以复现所需非线性分量。

## 方法
NCPSZ 非对称双网：大容量 ModelNet（约 32.71M）离线拟合扬声器–麦克风非线性；轻量因果 CtrlNet（约 0.18M）实时预补偿。锚点扬声器（主听筒）维持亮区目标，CtrlNet 驱动辅助扬声器抑制暗区非线性泄漏。损失为时频 BZ 保真与 DZ 能量最小化。在半消声室智能手机漏音场景采集（THD 3.2%@250 Hz），LibriSpeech 驱动 >1300 条高电压录音。

## 实验与结果
ModelNet 测试 MSE 约 1.6×10⁻⁹。200–2000 Hz 平均 AC 相对线性 VAST +3.78 dB，相对参数匹配因果 CNN +1.80 dB；亮区 SPL 接近目标，暗区更低。

## 结论
显式可微电声模型 + 锚点策略可在微型扬声器非线性体制下提升漏音抑制，并保持边缘可部署的因果控制。

## 点评
把 PSZ 从线性滤波器优化推进到“可微扬声器模型进环”，切中手机漏音实际。锚点扬声器降低对 BZ 损失的依赖，工程合理；收益相对线性天花板更可信，相对 CNN 的优势则指向 GRU 时序建模。


# LMPAN: A Lightweight Multi-Path Alignment Network for Joint Full-Duplex Acoustic Echo Cancellation and Noise Suppression

- 论文编号：191
- 报告人：Chengwei Liu
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/liu26b_interspeech.pdf

## 问题
全双工对话中硬件时延/能量失配与非线性回声使联合 AEC+NS 困难；端到端网络缺少显式多路径对齐，过抑制又伤下游 ASR/VAD。

## 方法
LMPAN：LAEC（子带 TDE+NLMS）+ 三条软时间对齐与能量补偿（ref–mic、mic–LAEC、ref–LAEC）+ GTCRN 精炼 + 注意力融合 LAEC/mic + 残差缩放后处理。动态目标按目标 SNR/SER 保留受控噪声/回声残差。两阶段训练：先对齐 WavLM 表征，再联合谱/回声/SI-SNR/PMSQE（SSL 作正则）。约 480K 参数、126M MACs。

## 实验与结果
AEC Challenge 2023：完整 STL 配置 MOS_avg 4.49（DT EMOS 4.63），可比 DeepVQE-S 且更轻。真实双讲下游：加 DTA 后低 SER 段 WER/DCF/TIR 显著改善（如 SER[−20,−15] WER 24.25→14.38）。消融显示对齐与注意力融合逐步抬升；SER_t=25 dB 对 ASR 最友好。

## 结论
显式多路径对齐、自适应融合与动态目标可在轻量预算下兼顾回声抑制与下游任务保真，适合端侧全双工对话。

## 点评
把“对齐/融合/不过抑”拆成可消融模块，并直接用 ASR/VAD/打断率衡量，比只报 AECMOS 更贴近产品。LAEC 仍作支路而非唯一依赖，设计稳健；最终 AECMOS 最优与下游最优配置略有分歧，需按任务选点。


# Active Constructive Interference for Speech

- 论文编号：222
- 报告人：Ofir Yaish
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/yaish26_interspeech.pdf

## 问题
传统 ANC 只做破坏性干扰消噪，被动语音增强则在麦克风后重建设；二者均未在声学域主动“塑造”语音。作者提出 Active Speech Enhancement（ASE）：同时衰减干扰并放大语音相关分量。

## 方法
ASE-TM：在前馈 ANC 设定下，误差麦作修改麦，使 eh=d+a 跟踪清洁目标 c。网络基于 SEmamba，用 Mamba2 的 TFMamba + 中间多头注意力，输出抵消信号 y 的复谱，经扬声器非线性与次级路径后与主路径叠加。损失含时域/幅值/复谱、防缠绕相位、度量对抗与一致性。任务覆盖加噪（VoiceBank-DEMAND）、去混响、去削波；仿真矩形房间与 SEF 扬声器非线性。

## 实验与结果
Table 1：去噪 PESQ 2.98 / STOI 0.99 / NMSE −21.76（优于 ARN 2.45、THF-FxLMS 2.37）；去混响 PESQ 2.43；去削波（η=0.25）PESQ 3.09。消融显示 Mamba2+损失改动贡献最大，注意力加速收敛。预测未来 500 样点以满足因果时 PESQ 仍约 2.96；约 22.3M 参数。

## 结论
主动建设性干扰可在消噪之外显式增强语音，在三类 ASE 任务上全面超过改编后的 ANC 基线。

## 点评
把 ANC 目标从“eh→0”翻转为“eh→c”，范式清晰。强结果部分来自与被动增强目标更对齐的损失与架构；基线本为消噪设计，在去混响/去削波上吃亏，对比解读需谨慎。仿真房间与固定几何下的实时部署仍待硬件验证。


# Predictive Directional Selective Fixed-Filter Active Noise Control for Moving Sources via a Convolutional Recurrent Neural Network

- 论文编号：271
- 报告人：Boxiang Wang
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/wang26e_interspeech.pdf

## 问题
定向选择性固定滤波 ANC（D-SFANC）按当前 DoA 选预训控制器，对移动源存在帧滞后，过渡期降噪变差。

## 方法
PD-SFANC：预训 36 个方位（10° 网格）宽带 FxLMS 控制器库；协处理器上 CRNN 用 K=4 帧多通道 STFT 幅相预测下一帧 DoA，提前切换滤波器；实时控制器按采样率输出抗噪。四面体 4 麦参考阵，16 kHz，帧长 0.5 s。数据含仿真白噪与 UrbanSound8K，多房间/SNR。

## 实验与结果
CRNN DoA 分类在 SNR≥20 dB 准确率 >90%，10 dB 约 87%。移动源仿真中，相对 FxLMS、SFANC、D-SFANC 等，PD-SFANC 能更稳地维持高噪声降低水平（NRL），多数时段 NRL 高于 15 dB，过渡更平滑。

## 结论
用时序预测消除滤波器切换滞后，可显著改善移动噪声场景的动态降噪，且参数端到端学习、无需手工调参。

## 点评
“预测下一帧再换滤波器”直接对准 D-SFANC 的滞后痛点，双速率架构也利于落地。当前限定单源与离散方位库；连续轨迹、多源与实物验证是自然延伸。


# DDSN: A Wrapped-Phase-Aware Decoupled Dual-Stream Network for Speech Packet Loss Concealment

- 论文编号：1295
- 报告人：Hao Tian
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/tian26b_interspeech.pdf

## 问题
频域 PLC 常联合建模实/虚部，忽略幅度与相位差异，导致相位错位与结构伪影；长突发丢包尤甚。批次元数据标题写作 Physics-Aware，正文为 Wrapped-Phase-Aware。

## 方法
DDSN：幅度与相位双流因果 U-Net（相位用 (cosθ,sinθ)），共享膨胀 TCN 抓全局上下文；SARG 用幅度先验作缩放残差引导相位（1+α·Mask），避免 sigmoid 门控在低能量区掐断相位；相位经 L2/SVD 投影回单位圆，幅度做 |A|^0.5 压缩。损失含流形约束、多分辨率 STFT、相位一致性与感知项。

## 实验与结果
VCTK 合成与 Interspeech 2022 PLC 盲测上，DDSN 在 PESQ/STOI/PLCMOS/DNSMOS 上优于 TFGAN、FRN 等；长突发下 PLCMOS 更稳。消融（40% PLR）支持解耦、SARG 与流形约束各自贡献。

## 结论
显式 wrapping 相位建模与非衰减式幅度→相位引导，可在因果约束下改善突发丢包重建稳定性。

## 点评
把“相位被幅度优化淹没”当作 PLC 核心失败模式，并用残差引导而非硬门控，设计针对性强。闭式 2×2 SVD 利于实时；与批次元标题不一致处，以正文为准。


# A Causal Reference-Enhanced Keep-Speech Active Noise Control Method

- 论文编号：1608
- 报告人：Li Rao
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/rao26_interspeech.pdf

## 问题
耳机 ANC 参考麦同时拾取噪声与语音，控制器会把语音一并抵消，损害对话可懂度；DeepANC 等端到端替换控制滤波会引入帧延迟，难满足因果余量。

## 方法
RSE-KSANC：用因果 WaveNet 变体增强参考信号（压语音、留噪声），FIR 控制滤波仍由 RLS 自适应；输入为原始参考与误差侧估计的含噪语音 ˆdv。训练目标对比 Lenh（误差域噪声抑制+保语音，代入 Wiener 最优 w）与 Lrefsep（参考端噪声提取 MSE）。约 9.53M 参数、零算法附加延迟。用实测耳机 IR（多方向/距离）与 LibriTTS+带限噪声及 DCASE 真实噪声评测。

## 实验与结果
Lenh 配置在 −5～15 dB SNR 上 STOI/DNSMOS 全面优于未处理、传统 ANC、DeepANC 与 Lrefsep；如 SNR=5 dB 时 STOI 88.67%、DNSMOS 2.36。真实风扇/引擎等噪声下同样领先。传统 ANC 在高 SNR 甚至因压语音而差于未处理。

## 结论
在参考支路做零延迟语音抑制、保留经典滤波器，可在严格因果下实现 keep-speech ANC，并泛化到未见方向、噪声与 SNR。

## 点评
把“智能”放在参考增强而非替换控制律，是兼顾因果与可部署性的好折中。Lenh 对齐最终误差目标，优于纯参考分离。模型仍偏大（约 9.5M），作者也指出需压缩以进耳机。


# Active Noise Control With a Gain Constraint for Micro-Loudspeakers

- 论文编号：2202
- 报告人：Liming Shi
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/cheng26b_interspeech.pdf

## 问题
微型扬声器低频复现能力弱，固定滤波 ANC 的 Wiener 解在低频增益过高易引起机械过冲；串高通虽限功率却增加群时延、降低降噪上限。

## 方法
在设计固定控制滤波时对频率响施加增益约束：先提 ANC-LF-FRC（仅低频约束）防过冲；因期望响应间断引发 Gibbs、损 NR，再加 ANC-FRC，对目标降噪带内其他频点也加约束。仿真与实测对比无约束 Wiener、高通级联、LF-FRC 与 FRC。

## 实验与结果
LF-FRC 可抑低频过冲但 NR 曲线出现起伏；FRC 在目标带更平滑。Table 1：FRC 在 100–500/500–1000/1000–2000 Hz 训练噪声上平均 NR 约 1.55/13.96/18.55 dB，优于高通与 LF-FRC，接近 Wiener 中高频表现且避免低频过冲。

## 结论
在滤波器预训练阶段施加频响增益约束，可在不增加电子延迟的前提下兼顾微型扬声器保护与有效降噪。

## 点评
把硬件能力直接写进固定滤波设计目标，比事后级联滤波更贴产品 ANC。Gibbs 分析解释了“只压低频不够”，FRC 是务实补丁。


# DiffVQE: Hybrid Diffusion Voice Quality Enhancement Under Acoustic Echo and Noise

- 论文编号：2337
- 报告人：Haljan Lugo
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/lugo26_interspeech.pdf

## 问题
免提场景需联合 AEC 与降噪；判别式 DeepVQE 强但生成式扩散 AEC 少见且先前工作难复现。作者要做可复现的混合扩散 VQE。

## 方法
DiffVQE：Cond DNN 用麦端与远端 STFT 判别估计 ˆScond 并提供条件 C；Score DNN 做方差爆炸 SDE 的去噪分数匹配，单步/少步 Langevin 采样生成近端语音。数据与合成管线基于公开框架，并加入 Interspeech 2025 URGENT 语音/噪声。仍允许非因果。对比同数据重训的 DeepVQE。

## 实验与结果
验证集：DiffVQE（5.13M，5.37G FLOPS，RTF 0.185）平均排名 1.3，多数 PESQ/LPS/ESTOI 与 ST 指标优于 DeepVQE（5.29M，42.24G，RTF 0.317）；DeepVQE 在 DT/ST Echo 上略领先且接近 clean。更小的 DiffVQE-S（3.43M，约 10% 算力）平均排名 2.0 仍优于 DeepVQE 的 2.5。AEC Challenge 测试集趋势一致（DiffVQE 平均排名 1.17）。

## 结论
可复现的混合扩散 AEC/NS 在多数质量指标与复杂度上超过 DeepVQE，但 Echo 指标仍略逊；单步变体利于部署研究。

## 点评
“可复现 + 公开数据”本身是对扩散 AEC 文献的贡献。混合 Cond/Score 把判别稳健与生成细节结合；非因果与 Echo 上的小劣势划清了与产品级低延迟 DeepVQE 的边界。

