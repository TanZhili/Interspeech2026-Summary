# Multi-Channel, Beamforming and Spatial Speech Enhancement

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：6
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场多通道/波束形成口头报告面向阵列几何可变、无线传感网分布式滤波、虚拟麦空间上采样、近距源歧义、自适应白噪增益 MVDR，以及方向信息压缩传输。核心问题是：固定阵列假设与边缘物理尺寸限制，如何在有限麦数、带宽与算力下保住空间滤波增益。

几何与分布侧，Geo-DConv 把麦坐标显式注入动态卷积使固定阵列模型阵列不变；ANDFilter 用端到端神经滤波替代 DANSE 迭代协方差优化。空间上采样与轻量双通道则通过虚拟麦条件下游增强，或以空间不变单通道教师动态仲裁蒸馏，降低对脆弱空间线索的过度依赖。经典 MVDR 经可微层联合学掩码与频变 WNG 阈值；NDC 仅压缩空间信息即可在接收端配置方向模式重建。

## 论文技术总结

# Towards Array-Invariant Speech Enhancement via Geometry-Aware Dynamic Convolution

- 论文编号：548
- 报告人：Zhenglong Liu
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26d_interspeech.pdf

## 问题
多通道语音增强依赖固定阵列几何，难跨设备复用数据与模型；现有 array-agnostic 方法可处理麦数与排列变化，但很少显式利用可用的麦克风坐标先验，空间滤波往往弱于固定阵列模型。

## 方法
提出 Geometry-Aware Dynamic Convolution（Geo-DConv）：用麦克风相对坐标的 Fourier 位置编码 + Topology-Aware Coordinate Transformer（TACT，MHSA）生成变换矩阵 M，将固定基卷积核线性组合成与输入通道数匹配的动态核，经 LN+PReLU 后接到下游固定阵列网络。TACT 对通道置换等变，保证卷积结果置换不变。将 SpatialNet、TF-GridNet 等首层卷积替换为 Geo-DConv，即可转为阵列不变系统。

## 实验与结果
在真实录制 RealMAN（32 麦子阵列、8 kHz、4 s 片段）上训练。几何不变设定下 SpatialNet-Geo-DConv：SDR/SI-SDR 9.72/4.22，优于 FaSNet-TAC 与 USES2-comp，参数约 1.3M、MACs 约 6.08 G/s。可变麦数训练进一步提升。1/2/5 麦与跨数据集 CHiME-4（未微调）上 DNSMOS OVRL 分别升至约 2.64、2.73（未处理 1.42）。

## 结论
作者认为显式几何先验可把强固定阵列算法改造成阵列不变 SE，并在真实数据上优于既有 array-agnostic 方法，为跨设备部署提供新路径。

## 点评
把“坐标→动态核”接到已有强骨干上，比纯 TAC/注意力式无几何方法更充分利用阵列结构，且置换等变性设计干净。局限是仍需设备提供坐标；训练主要在 RealMAN 子阵列抽取，极端不规则几何与仿真–真实差异下的表现需更多验证。


# An All-neural Distributed Filtering Algorithm for Speech Extraction in Wireless Acoustic Sensor Networks

- 论文编号：648
- 报告人：Jiawei Wang
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26l_interspeech.pdf

## 问题
无线声学传感器网络（WASN）可用分布式压缩交换（如 DANSE）避免集中式聚合，但基于协方差迭代的滤波在低 SNR、非平稳噪声下脆弱；现有深度方法多只做掩码前端，核心仍依赖线性滤波与矩阵求逆。

## 方法
提出 ANDFilter：端到端神经分布式滤波，通信协议与 DANSE 一致（每节点广播一个压缩标量）。三模块：SNFM（U²-Encoder + S-TCN + Decoder + LSTM 滤波器映射）由本地多通道观测量直接合成局部复滤波器并产生压缩信号；NSM 以本地为 query、远端压缩为 key/value，余弦注意力自适应加权；MNFM 结构同 SNFM，在本地观测与精炼压缩信号上合成全局滤波器。损失为 SNFM/MNFM 的 RI–幅度混合损失加 NSM 熵正则。

## 实验与结果
Pyroomacoustics 仿真 4 节点×4 麦十字阵，LibriSpeech 干净语音 + Freesound 噪声，16 kHz。消融：完整 ANDFilter PESQ/ESTOI 2.86/0.83，优于 SNFM+MNFM（2.80/0.82）与 DANSE（1.44/0.61）。相对 C-MWF、DANSE、C/D-PEVD、TANGO，在各 SNR 段均最优，平均 PESQ/ESTOI/DNSMOS 为 2.86/0.83/2.60。

## 结论
作者认为用结构化神经模块直接合成分布式滤波器，可在有限带宽下摆脱协方差迭代，于低 SNR 与非平稳条件更稳健。

## 点评
把 DANSE 两阶段结构“神经化”且保留可解释通信形式，相对掩码+传统滤波的混合系统更彻底。证据几乎全在仿真 WASN，真实无线同步/丢包/时钟偏差未覆盖；节点数固定为 4，规模扩展性仍待检验。


# Spatial-Magnifier: Spatial upsampling for multichannel speech enhancement

- 论文编号：1477
- 报告人：Dongheon Lee
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26k_interspeech.pdf

## 问题
边缘设备麦数受物理限制，多通道增强的空间自由度不足；已有 Neural-VME 多把增强网络挪用来估虚拟麦，且缺少把 VM 信号/特征系统接入下游 SE 与波束形成的通用框架。

## 方法
提出 Spatial-Magnifier（GAN，DBPN 风格）：频域把麦通道当卷积通道，交替 up/down block，加入 Selection Module（点卷积门控）与 Dynamic Channel Allocation（动态卷积通道注意力压缩）。并提出 SARL：SARL-S 将估计 VM 波形与真实麦拼接后送 MC-SE；SARL-F 将 VM 潜特征与编码器特征相加再分离–解码。可服务 VM-BF（MCWF/MVDR）与端到端 VM-SE；训练联合 Neural-VME、波束形成与对抗损失。

## 实验与结果
DNS 语料 + 六麦仿真（圆阵+高低麦），含 omni-SE 与 FoV-SE。2ch RM/4ch VM 上 SARL-S 的 VM-BF SI-SDR/PESQ/STOI 达 7.10/2.40/82.1，接近 6ch 物理阵 8.35/2.41/84.6；相对 MC Conv-TasNet 等基线更优且算力更低。换 MVDR、MC-RNN、智能眼镜 ATF/HRTF、2→8 VM 等设定仍有效；VM-SE 使 SpatialNet-small 质量超过更大的 2ch SpatialNet-large。

## 结论
作者认为专用空间上采样网络加 SARL 条件化，可在少物理麦下接近全阵 oracle，并跨波束形成与端到端增强通用。

## 点评
把“估虚拟麦”从复用 SE 骨干改为面向通道维超分，并用信号/特征双路径条件化下游，工程完整。VM 位置绑定训练阵列几何，任意点生成仍难；复杂 2RM/4–8VM 相对全物理阵仍有差距。


# A Dynamic Knowledge Distillation Framework for Mitigating Spatial Ambiguity in Lightweight Dual-Channel Speech Enhancement

- 论文编号：1524
- 报告人：Yifei Yang
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26i_interspeech.pdf

## 问题
轻量双通道 SE 靠空间线索优于单通道，但目标与干扰方位接近时空间信息失效， unconstrained 空间依赖会导致空间模糊，甚至不如单通道；既有缓解多需距离/DOA 辅助或额外模式切换开销。

## 方法
提出 Dynamic Spatial-aware Knowledge Distillation（D-SKD）：冻结单通道 SC-GTCRN 为教师，双通道 DC-GTCRN（幅度 + sin/cos IPD）为学生。Dynamic Arbitrator Module 按样本比较师生混合损失相对差距 ΔL，用 ReLU(tanh(γ·ΔL)) 得到动态蒸馏权重：仅当教师更好时蒸馏。总损失 = 任务损失 + μ·λ_dyn·蒸馏损失（均用 SI-SNR + 复谱混合损失）。推理仅保留学生，无额外参数。

## 实验与结果
DNS-3 仿真双麦 4 cm，分段角/平均角/角扫描测试。0°–15° 上 D-SKD 将 DC-GTCRN PESQ/STOI 从 1.742/71.80 提到 1.793/72.96，大角度基本保持；去掉 DAM 虽近角更好但大角度明显变差。h.size=16/32/64 及 LiSenNet、UL-UNAS 上趋势一致；h.size=32 时近角可追平单通道教师并提升其他区间。

## 结论
作者认为用空间不变单通道教师做动态仲裁蒸馏，可在无角度监督、无推理开销下缓解近角空间模糊，并适用于多种轻量双通道模型。

## 点评
把“空间不可靠时回退频谱”做成样本级门控蒸馏，比硬切换多任务更适合边缘部署。权衡是近角提升有限、强蒸馏可能伤空间能力（无 DAM 即见）；教师上限决定近角天花板。


# Joint Learning of Covariance Estimation and White Noise Gain for Robust MVDR Beamforming

- 论文编号：2212
- 报告人：yongyi deng
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/deng26d_interspeech.pdf

## 问题
MVDR 对麦克风自噪声与阵列失配敏感，常用固定 WNG 阈值或对角加载，在未知/时变声学与器件条件下次优；学习型波束形成多改进协方差估计，却很少把 WNG 本身纳入端到端优化。

## 方法
双分支网络（多线索融合 JNF 骨干）：一支预测复 T–F 掩码估计噪声协方差，一支预测逐频 WNG 阈值；嵌入可微的 QEP 形式 WNG 约束稳健 MVDR 层。训练用增强输出与 early-reference 波束形成信号的 MAE，无需显式 WNG 监督，由重建损失隐式驱动稳健性–指向性折中。

## 实验与结果
VCTK、8 麦 ULA（2 cm）、端射目标、多干扰与扩散/白噪声。相对 FullSubNet 掩码 + 最优固定 WNG（−6 dB）及提出模型的最优固定 WNG（−8 dB），自适应 WNG 在 SNR/STOI/SDR/PESQ 分布上更好。已见阵列（δ=2.0±ϵ cm）上提出方法 SNR gain/ΔSDR 为 11.940/11.474，高于最优固定 W0 的 10.543/9.510 与最优对角加载。未见阵列间距设定下亦有对比（正文表格后续行因抽取截断，定性结论为自适应仍更优）。

## 结论
作者认为把 WNG 当作可学习物理控制量并与掩码协方差联合优化，可在失配条件下稳定优于固定稳健性设定。

## 点评
把稳健性旋钮从经验超参拉进可微 MVDR，问题抓得准。实验以仿真 ULA 为主；正文部分图表抽取有乱码，未见阵列定量细节需对照 PDF。early-reference 目标与真实失配分布的匹配程度决定可迁移性。


# Neural Directional Coding: Joint Spatial Coding and Filtering with Configurable Directivity Patterns

- 论文编号：2234
- 报告人：Weilong Huang
- 程序：Thursday 1 October 2026 / Multi-Channel, Beamforming and Spatial Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26o_interspeech.pdf

## 问题
通信接收端常需可配置指向性空间处理，但传全阵列代价高；级联 SpatialCodec 重建全通道再做 UNDF 参数量大、码率高，不够高效。

## 方法
提出 Neural Directional Coding（NDC）：参考通道用 EVS（12.8 kbps）传输；阵列空间信息经 SpatialCodec 式编码器–RVQ–解码器压成低维侧信息。接收端 FiLM-JNF 估计模块结合可配置指向性向量 Λt，输出复掩码乘参考通道得到虚拟指向麦信号。两阶段训练：先用一阶 Cardioid 多样源–阵几何预训练编码，再冻结编码器/量化器、用多样 μ/θs/J 模式训解码与滤波。可选输入归一化仅保留通道间幅度/相位差。

## 实验与结果
4 麦（3 cm UCA+中心参考）、16 kHz、无回声仿真。0.25 kbps/1.4M 参数 NDC 在多种未见高阶指向性上 SDR/PESQ 优于同码率 SpatialCodec+UNDF，并多数超过 7.5 kbps/90.8M 级联基线与 oracle-DOA 参数滤波。归一化输入差距小，说明比特主要用于空间信息；无预训练变差。低混响动态场景中仍能抑制移动干扰。

## 结论
作者认为联合空间编码与可配置指向性滤波，可用极低侧信息码率与轻量模型近似虚拟指向麦，优于“全重建再滤波”管线。

## 点评
把 DirAC 思路神经化并与 UNDF 联合优化，码率–参数优势非常突出。主要在无回声、共面源设定训练，混响/移动仅为定性推广；参考通道仍占 12.8 kbps，总链路码率需一并考虑。

