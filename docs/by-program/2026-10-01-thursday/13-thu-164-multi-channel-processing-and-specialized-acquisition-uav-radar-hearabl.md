# Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：6
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场面向可穿戴听戴设备、穿墙/毫米波雷达与无人机极低信噪比听觉，以及多通道相对传递与云边协同增强。共同约束是功耗、时延与极端噪声结构；技术回应包括亚奈奎斯特采样后重建、气导/骨导一致性剪枝、相位几何约束、注意力谱扩展，以及把自噪声或雷达先验写进波束形成/生成模型。

听戴与多模态侧，CAPS 主动降采样/降比特并做带宽扩展以省电；CCAP 按跨模态一致性保留融合关键通道。相位方面 MSGLA 用 STFT 一致性消解几何相位符号歧义。雷达路径上 CAF-Former 与 RAD-GAN 分别攻克穿墙带限与低 SNR 带宽扩展。无人机侧则利用自噪声时相关、频变组成与幅度平稳性做 DoA/NCM/后滤波，或用轻量频带融合 Transformer 做实时单麦增强。多通道与部署上，深度学习估计 ReTM，以及延迟服务器输出 + 层间特征提升 + 协同多通道维纳滤波的云边协作。

## 论文技术总结

# CAPS: A Cascaded Reconstruction Model to Power Saving in Hearables Using Sub-Nyquist Sampling with Bandwidth Extension

- 论文编号：506
- 报告人：Sajid F. Dipto
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/islam26_interspeech.pdf

## 问题
耳机端 ACM/BCM 常以高采样率与高位宽 ADC 采集再压缩传输，未系统利用降采样/降位宽省电；现有多模态 SE 或 BWE 也难同时覆盖多模态、流式与低功耗约束。

## 方法
CAPS 级联：耳端将 ACM/BCM 采到约 4 kHz、8-bit；手机端 Spectral Enhancement Network（U-Net+Mamba）提频谱分辨率，HiFi-GAN 风格 Upsampling Network 波形上采样（256×），Amplitude-Phase Enhancement Network 融合 BCM 做幅相增强。损失含 multi-period、反 wrapping 相位/群时延与多尺度 MAE。自建 20 人同步 ACM+双 BCM 数据（8/10/12-bit）。

## 实验与结果
桌面 4→16 kHz：CAPS 约 2.85 M / 11.04 MB，推理 1.36 ms，LSD/PESQ/STOI 等优于 TFiLM、VibVoice、AERO、EBEN、HiFi++、SEANet。Pixel7 上 55.11 ms（<150 ms 流式阈值）。{24 kHz,12-bit}→{4 kHz,8-bit} 耳端省电约 3.31×；手机跑 CAPS 约 1.15 W，相对耳机电芯可忽略。

## 结论
耳端亚奈奎斯特+低位宽与手机端级联重建可平衡省电与可懂度/质量；文中亦报告低位宽时性能下降趋势。

## 点评
把 ADC 功耗公式与重建网络绑成端到端系统论证，工程闭环完整。模型体积极小适合手机；质量依赖 BCM 条件与自采数据分布，跨设备/极端噪声外推需谨慎。


# An Investigation on Combining Geometry and Consistency Constraints into Phase Estimation for Speech Enhancement

- 论文编号：621
- 报告人：Chun-Wei Ho
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ho26_interspeech.pdf

## 问题
加性噪声 SE 中几何相位估计可把问题化成相位差符号二分类，但符号难估且错分代价大；直接相位回归与 DNN 符号预测也常不稳定。

## 方法
提出 multi-source Griffin-Lim（MSGLA）：在语音与噪声谱之间交替做 GLA 式一致性投影，并强制加性几何。NM-MSGLA 用估计语音/噪声幅度，经几次迭代隐式落到 ±|ΔP| 候选；NP-MSGLA 首次用正弦定理，由语音幅度与噪声相位得到两候选并迭代消歧。骨干 TF-GridNet（约 1.3 M）。

## 实验与结果
Oracle 实验显示噪声幅度/相位对重建很关键。VB-DMD：NP-MSGLA PESQ 3.46、SI-SNR 19.61、CBAK 3.18，匹敌或略优于直接相位估计与符号预测。WSJ0-CHiME3 上两变体与 GLA/基线接近，背景抑制（CBAK）更稳。

## 结论
几何约束与多源一致性结合可无监督消解符号歧义；NP 路径表明噪声相位在低能区可作为互补线索。

## 点评
用一致性迭代替代脆弱的符号分类器，动机扎实。Oracle 与盲测落差说明幅度/噪声估计仍是瓶颈；相对直接回归增益多为边际，价值更在可控几何框架与 CBAK。


# Through-Wall Radar Speech Acquisition via Cascaded Attention Fusion

- 论文编号：1034
- 报告人：Ruotong Ding
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ding26c_interspeech.pdf

## 问题
穿墙 FMCW 雷达语音严重带限、杂波与高频衰减，常规卷积难抓长程依赖，标准 MHSA 在低 SNR 高频易碎片化、跨频交互不足。

## 方法
CAF-Former：从可靠低频（约前 50 bin）经 K=10 层渐进扩到全带。每层 Temporal Multi-Query Attention（共享 K/V、多独立 Q）再经 Frequency Attention Fusion 沿频轴融合；保留输入噪声相位、优化 log-spectral 幅度距离。5.31 GHz、15 cm 混凝土墙采集；仿真约 312 h 训练。

## 实验与结果
相对 RANet、Wave-Voice、TF-Locoformer、EBENet：仿真/实录上 STOI、DNSMOS、CS-MFCC 最优（如实录 STOI 0.617、DNSMOS 2.423），PESQ 略低于个别强基线但更均衡。消融显示 TMQA+FAF 优于 MHSA、仅 LP 融合或单 query。

## 结论
级联时频注意力与渐进扩带利于穿障雷达语音的高频谐波恢复；未来将评真人发声场景。

## 点评
针对雷达“低频可靠、高频噪声主导”的传感退化设计渐进与共享 KV 多 query，问题匹配度高。PESQ 非全面第一但可懂度/感知更稳；仍用激励器隔墙而非真人，迁移需再验。


# Ego-Noise-Aware Spatial Filtering for Reliable UAV Audition in Extreme Low-SNR Conditions

- 论文编号：1530
- 报告人：Chanhong Jeon
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jeon26b_interspeech.pdf

## 问题
无人机自噪声强时域相关、频变组成与幅度平稳，分别破坏 DoA、噪声协方差与波束后残差抑制，极端低 SNR 下常规波束成形不可靠。

## 方法
无预训练、约 0.021 GMAC/s 的信号处理管线：相位一致性引导 TF bin 选择（偏离时域相关参考的 bin）估 DoA；按交叉频率 ν（文中 3 kHz）混合 closeness/directional 掩码估 NCM 并做 MVDR；用最小似然方向作 null 参考，方差调制 Wiener 后滤波压残差自噪声。圆形 4 麦阵、实测 Syma 自噪声 + TIMIT 仿真。

## 实验与结果
−25 dB 下 DoA 准确率达 98.12%，优于 MUSIC、SRP-PHAT、wHisK。消声/混响（T60=0.3 s）多 SNR 上 SI-SDR、PESQ、ESTOI、DNSMOS 整体优于 MPDR、directional/closeness MVDR、MMSE；后滤波贡献显著（如消声 −25 dB SI-SDR −2.45 vs 无后滤 −9.17）。

## 结论
围绕自噪声结构性质联合设计 DoA–NCM–后滤，可在极低 SNR 提升无人机听觉；实验主为悬停与固定阵几何。

## 点评
把 DoA 当全管线共享空间锚点而非仅导向向量，工程思路清楚、算力极低。强依赖悬停相关与固定 ν/σ；机动、非平稳自噪声与真实远场对话场景仍具挑战。


# Cross-Modal Consistency-Aware Structured Pruning for Efficient Speech Enhancement with Air- and Bone-Conduction Microphones

- 论文编号：1548
- 报告人：Yeeun Kim
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26n_interspeech.pdf

## 问题
ACM+BCM 多模态 SE 算力大，难上可穿戴；幅度/梯度剪枝与跨模态激活对比对融合关键通道不友好，噪声与模态失配更易误剪。

## 方法
CCAP：对预训练卷积 SE 模型做结构化通道剪枝。分别零掩 ACM 或 BCM，相对多模态响应算归一化灵敏度，平均得重要性后剪低分通道并微调。在 DCCRN、MMINet、LAU-Net 上检 0–80% 剪枝比；TAPS 配对语料 + DNS 噪声（SNR −5–10 dB）。

## 实验与结果
各架构上 PESQ/STOI 优于 PP、TP、BN、MANU；80% 时相对最强基线 PESQ 约 +0.10/+0.20/+0.10。同延迟下质量更高；MMINet 相关层冗余降更多、CKA 漂移更小。MCU 上 LAU-Net 50% 剪枝：Flash/RAM 降约 48%/27%，304 ms 段推理 87 ms（RTF 0.29）。

## 结论
以模态零掩下的响应保持评估通道，可压缩 MMSE 同时保住融合信息，适合嵌入式部署。

## 点评
剪枝准则直接对准“去掉一模态后谁还活着”，比纯权重范数更贴多模态。一次性估计+微调流程实用；是否推广到非卷积融合块与更强非平稳噪声仍待看。


# DroFiT: A Lightweight Band-Fused Frequency Attention Toward Real-Time UAV Speech Enhancement

- 论文编号：1620
- 报告人：Jeongmin Lee
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26n_interspeech.pdf

## 问题
单麦无人机听觉被宽带准平稳桨叶/电机自噪声淹没；现有 SE 模型过大或 chunk 激活用量过高，难在机载内存与能耗预算内做帧级流式。

## 方法
DroFiT：全带/子带（Mel 式五组）编解码压缩频谱；Pre-TCN 抓准平稳谐波自噪声；频率轴 Transformer 在拼接的全带/子带 token 上做 MHSA 融合；Post-TCN 时域细化后预测复掩码。约 168k 参数，支持增量推理；另有 Linear Attention 的 Lite 与量化变体。VB-DEMAND×实测 DJI Flip 噪声，SNR 至 −30 dB。

## 实验与结果
相对 DCU-net、SMoLnet-T、DTLN、DCCRN，DroFiT 在多 SNR 上 SI-SDR/PESQ/ESTOI 最优或接近最优，算力较 DCU-net、SMoLnet-T 降约 15–26× 与 9–15×。消融去 Pre-TCN/子带/Post-TCN 均掉点；亦含真实外放近机录音评测。

## 结论
时频解耦 + 全/子带频注意力可在极轻量下做无人机 SE 与流式部署。

## 点评
针对桨叶谐波的 Pre-TCN 与“内存友好帧流”约束设计清晰。主结果来自仿真混合；真实机载麦克风与风噪/机动噪声分布可能更难，需看补充真实集表现。


# mmWave Radar Aware Dual-Conditioned GAN for Speech Reconstruction of Signals With Low SNR

- 论文编号：2330
- 报告人：JASH KARANI
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/karani26_interspeech.pdf

## 问题
玻璃墙后 mmWave FMCW 语音捕获带限且 SNR 极低（约 −5 至 −1 dB），难重建可懂全带语音；许多方法依赖大数据、预训练模块或偏乐观 SNR。

## 方法
RAD-GAN 两阶段：Stage-1 在带限（≤1 kHz）干净 mel 上用 mel + MR-STFT 预训练 HiFi-GAN 生成器；Stage-2 用 Residual Fusion Gate 融合噪声 mel 与 WaveVoiceNet 增强 mel，对抗微调，判别器含 MPD、MSD 与提出的双分支 Multi-Mel Discriminator。RASE 2026 数据：直接膈肌振动与铝箔二次表面两任务，约 42 h 配对。

## 实验与结果
加权分 0.333（Task1 0.387 / Task2 0.297）优于 WaveVoiceNet、HiFi-GAN、DCCTN、AP-BWE、DiffWave、CDiffuSE；DNSMOS 2.688 等更均衡。消融显示 MMD/MR-STFT、预训练、WVN 条件逐步抬分。无数据增强、无外部预训练骨干。

## 结论
双条件融合 + 两阶段训练可在小数据、极低 SNR mmWave 设定下提升带宽扩展重建；Task2 更难但加权更看重。

## 点评
先稳住低带到全带映射再引入对抗与多 mel 判别，适合噪声相位不可靠场景。指标靠加权综合而非单一 PESQ；数据规模相对小、场景特定，跨雷达硬件泛化未知。


# Deep Learning Based Relative Transfer Matrix Estimation for Multiple Sources and Multiple Microphones

- 论文编号：2524
- 报告人：Oshan A. B. Yalegama
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/yalegama26_interspeech.pdf

## 问题
多声源同时活跃时，相对传递函数（ReTF）依赖的 W-disjoint orthogonality 不成立；相对传递矩阵（ReTM）可刻画两组麦克风间对多声源的空间映射，但既有估计几乎只靠协方差矩阵，深度学习路线尚未系统探索。

## 方法
在静止声源假设下，提出三种有监督 ReTM 估计框架：SCoNet 在 STFT 域对实虚部堆叠通道做 depthwise 卷积；FuSNet 用 QA×QB 个可学习 1D 卷积滤波器对应时域卷积核并求和；LAeNet 对每频点共享 BiLSTM 后经层归一化与全连接估计 ReTM 系数再重建 A 组信号。训练目标为时域负 SDR 与 STFT 域 RSE 的加权和（α=1, β=10）。

## 实验与结果
在 6×7×3 m、T60=500 ms 房间用工具箱仿真（QA=3/QB=4 或 QA=5/QB=7），场景含 WGN、空调/音乐噪声与含语音的多声源，麦克风加 40 dB SNR。相对协方差基线，FuSNet 在多数场景估计精度最高（如 A1 平均 SDR 28.46 dB），SCoNet/LAeNet 也常优于基线；麦克风增多时各法均改善。语音去噪（用噪声段估 ReTM）上 LAeNet 最好（B/C 的 SDR 8.67/7.03 dB，STOI 0.92/0.91），FuSNet 虽估计准但去噪差且残留回声。FuSNet 参数与延迟最低，LAeNet 延迟最高。

## 结论
深度学习可明显提升 ReTM 估计精度，STFT 域模型在去噪中更稳；未来拟扩展到分离、去混响与麦克风分组策略。

## 点评
把 ReTM 从协方差估计拉到端到端空间映射，并用去噪闭环验证“估计准≠任务好”——时域 FuSNet 与时频模型的反差很有信息量。局限是仿真、静止声源与固定分组；真实移动场景与热噪声不可忽略时还需再验。


# Cloud-Boosted Low-Compute Multi-Channel Speech Enhancement

- 论文编号：2774
- 报告人：Buye Xu
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/fan26d_interspeech.pdf

## 问题
可穿戴端侧增强受算力与延迟约束，轻量模型场景建模弱；Knowledge Boosting 用服务器模型帮忙，但对一般语音增强增益有限，且未充分利用中间表征与混合波束成形中的空间统计。

## 方法
服务器为冻结的因果 SpatialNet；端侧为 TinyGRU+MCWF。三点协作：(a) 将延迟后的服务器增强谱拼到多通道输入；(b) 从 SpatialNet 第 0/4/8/12 层抽特征，经 1×1 压缩与延迟后用 FiLM 分层调制 TinyGRU；(c) Collaborative MCWF：边端各自估目标后算交叉协方差，用网络预测的 α(t) 融合延迟服务器统计与当前边端统计，再经可学习时变平滑求 MCWF。

## 实验与结果
DNS-Challenge 语音/噪声 + 8 通道圆阵 Pyroomacoustics 仿真；Standard SNR∈[−5,10] dB，Challenging ∈[−10,−5] dB。64 ms 延迟下，完整 (a)(b)(c) 相对 TinyGRU+MCWF：Standard SI-SDR 1.97→5.74 dB，Challenging −1.16→2.33 dB；边端仅多约 1.5% 参数、2.4% MMACs。放大 TinyGRU-Large（+198% 参数）仍远不及协作。延迟 96/128 ms 时 SI-SDR 降至约 4.39/4.26 dB，仍高于基线。

## 结论
在冻结大模型与可接受通信延迟下，延迟输出、分层特征与协方差融合可显著缩小端云差距，且边端开销很小。

## 点评
核心洞见是空间统计比谱细节更耐延迟，因而把 boosting 做到 MCWF 统计层而非只拼输出。α(t) 自适应权衡“准但旧”与“新但弱”，在突变噪声时是否足够灵敏仍依赖仿真设定；服务器仍需在线可达。

