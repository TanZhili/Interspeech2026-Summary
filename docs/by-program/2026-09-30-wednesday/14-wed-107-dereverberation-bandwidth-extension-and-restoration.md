# Dereverberation, Bandwidth Extension and Restoration

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：6
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦去混响、带宽扩展与波形恢复：在保真与实时性之间平衡谐波一致性、瞬态清晰度与相位重建。超分辨与 BWE 出现 MDCT 域谱上下文建模、辅音/元音分建模轻量方案、高效扩散与 Vocos 骨干任意上采样比；去混响则结合迁移学习跨房间几何、无监督神经模型蒸馏信号处理结果，以及把 U-Net 中间表示解读为 RIR 编码器并用对比 RIR 嵌入条件化训练。

低延迟声码从幅度谱或 Mel 重建宽带/全带波形成为实用焦点；扩散超分被重审训练技术以压缩到约百万参数与数十 GFLOPs。共同趋势是：用物理/稀疏先验与跨域迁移减少对匹配数据依赖，并明确追求可实时部署的高质量恢复。

## 论文技术总结

# STSR: High-Fidelity Speech Super-Resolution via Spectral-Transient Context Modeling

- 论文编号：27
- 报告人：Jiajun Yuan
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yuan26_interspeech.pdf

## 问题
语音超分需恢复至 48 kHz 的谐波与瞬态细节；级联或特征不匹配方案易糊高频；需端到端 MDCT 域高保真重建。

## 方法
STSR：有符号 MDCT 域端到端框架，建模频谱–瞬态上下文以对齐谐波；复合目标含频域对抗等。训练时随机截止频率 r∈[4,32] kHz 再上采样至 48 kHz。约 66.2M 参数，无额外声码器。

## 实验与结果
VCTK：4/8/16/24→48 kHz 平均 LSD 0.79，ViSQOL 随带宽升高；主观 MOS 4.20±0.06。HiFi-TTS 跨库平均 LSD 1.05，优于 NVSR、mdct 等对比。消融显示频域对抗与瞬态建模有贡献。

## 结论
统一 MDCT 超分在客观与主观上超过文中所列 SOTA，跨数据集仍稳。

## 点评
有符号 MDCT 避免幅相拆分带来的级联失配，设计干净。参数量不小；对比系统是否同训练预算需留意。瞬态/谐波可视化支撑“更锐谐波”主张。


# A Novel Transfer Learning Approach for Room Impulse Response Estimation and Speech Dereverberation Across Geometrically Diverse and Data-Scarce Environments

- 论文编号：31
- 报告人：Christian Ritz
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pasha26_interspeech.pdf

## 问题
RIR 估计对回声消除与去混响关键，但跨房间形状（矩形→L 形/不规则）泛化差，目标几何标注稀缺。

## 方法
迁移学习：几何感知编码器提形状不变特征，物理信息解码器施加回声稀疏与能量衰减先验；LSTM 将房间参数映射为时域 RIR。微调时冻结编码器只更新解码器。源域 500 矩形房 25k 对；目标仅用 10 房微调、40 房测试。

## 实验与结果
未见目标几何上 MSE 降 56%、LSD 降 37%（相对未迁移设定）。下游去混响：PESQ 3.24 vs GAN 基线 2.78，STOI 0.89 vs 0.79。

## 结论
选择性冻结 + 物理正则可在极少目标房数据下完成跨几何 RIR 迁移，并改善去混响实用指标。

## 点评
“编码器冻、解码器适”把跨几何不变性与房间特异声学拆开，样本效率高。依赖仿真/参数化几何输入；真实测量噪声与不规则材料分布可能削弱物理先验假设。


# HWB-plus: A Lightweight Speech Bandwidth Extension Method with Separate Modeling for Consonants and Vowels

- 论文编号：1498
- 报告人：Xueliang Zhang
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26k_interspeech.pdf

## 问题
轻量 BWE（如 HWB-Net）参数少，但高频辅音重建弱：输入增强与辅音需求不匹配，单 WGMM 谱建模初始化不够感知化。

## 方法
HWB-plus：在 HWB-Net 上保持约 194K 参数、12.39M MACs/s；用 DualWGMM 分建模辅音/元音相关谱，配合带引导掩码与改进初始化。HR 采样率改为 22050 Hz 以覆盖辅音频段；VCTK 说话人无关划分，LR 由 2–3 kHz 低通产生。

## 实验与结果
相对 HWB：LSD 1.11→0.94，DNSMOS P.808 3.31→3.55，PESQ 3.35→3.83，VISQOL/NISQA 同步升。优于 BAE-Lite 等轻量对比，接近更大 BAE 的部分感知分而算力远低。

## 结论
分辅音/元音谱建模在不增复杂度下显著提升轻量 BWE，尤其听感与辅音相关质量。

## 点评
“同预算换结构”对照干净，适合端侧。DualWGMM 依赖辅音/元音路径分工正确；极端窄带或噪声 LR 未充分展开。指标全面（LSD+多听感）利于部署选型。


# USDnet++: Distilling Signal Processing Based Dereverberation for Unsupervised Neural Speech Dereverberation

- 论文编号：2044
- 报告人：Zhong-Qiu Wang
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pang26_interspeech.pdf

## 问题
无监督去混响 USDnet 仅靠线性滤波重建观测约束；WPE/WPD 等信号处理结果通常抬高目标 SNR，可作弱监督，但不宜直接当硬标签。

## 方法
USDnet++：在原有“DNN 输出经线性滤波重建混合”之外，增加使滤波后估计逼近 SPD（WPE/WPD）结果的损失；可多阶段交替 DNN 与 SPD 精炼；亦可把 SPD 结果作额外输入再训。骨干 TF-GridNet；DNN 估计直达声支撑 WPE/WPD。

## 实验与结果
WSJ0CAM-DEREVERB（8 麦）：混合 PESQ 1.64 / SI-SDR −3.6 dB；USDnet 2.64 / 3.1 dB；USDnet++ 用 USDnet-WPD 作 SPD 达 2.86 / 3.9 dB。Oracle-WPD 指导可达 2.95 / 4.9 dB。多阶段 refinement 进一步提升。

## 结论
把 SPD 当弱约束而非硬目标，可稳定改进无监督神经去混响，并与 WPE/WPD 形成互补闭环。

## 点评
保留 USDnet 物理重建思想，又吃到经典算法的 SNR 红利，折中合理。性能仍受 SPD 上限牵制（相对监督 Oracle）；真实远场噪声/多说话人是否同样有效需外推谨慎。


# EffVOC: Low-Delay Efficient Speech Waveform Reconstruction from Spectral Representations Without Phase

- 论文编号：2407
- 报告人：Renzheng Shi
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shi26f_interspeech.pdf

## 问题
从幅度/Mel 重建波形时，经典相位恢复算法延迟高或质量差；神经声码器质量高但常更复杂、延迟更大。需 20 ms 级低算法延迟的高效重建。

## 方法
EffVOC：基于低延迟 Encodec 式声码器改造，直接从幅度谱或 Mel 合成宽带/全带语音，无显式相位迭代。固定 20 ms 窗、5 ms 移；可配置通道宽度 F∈{64,32,16,8} 权衡算力与质量。

## 实验与结果
VCTK 16 kHz：F=64 幅度输入 PESQ-WB 4.31、MOS 4.17，延迟 20 ms，RTF≈0.65；F=32 仍 PESQ 4.24。优于同延迟 RTISI 变体；相对高延迟 GLA/DiffPhase 接近。Mel 输入 F=32 亦达 PESQ 4.21、MOS 4.15。更小 F 质量下降但算力大降。

## 结论
20 ms 低延迟神经重建在客观与 MOS 上达新 SOTA 区间，且可按 F 伸缩部署。

## 点评
把“算法延迟”定义钉死在帧长，便于与通信场景对齐。与高延迟相位法比质量优势明显；与大扩散模型比算力友好。全带与极小 F 时仍有可见质量折损。


# Your U-Net Dereverberation Model is Secretly an RIR Encoder

- 论文编号：2707
- 报告人：Sina Khanagha
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/khanagha26_interspeech.pdf

## 问题
NCSN++ U-Net 类去混响网络是否在隐式编码 RIR？若是，显式 RIR 条件化能否改善表示与收敛？

## 方法
分析：从去混响 U-Net 注意力特征提嵌入做 t-SNE，与对比学习训的 RIR 编码器（ResNet34 / Conformer）对照。训练：InfoNCE 式对比，使同 RIR 不同语句靠近。应用：将预训练 RIR 嵌入注入 SGMSE+/NCSN++ 各 BigGAN 残差块作条件。数据约 10k 真实 RIR 的 VCTK-Reverb。

## 实验与结果
t-SNE 显示判别/扩散去混响骨干深层特征按 RIR 成簇，形态接近专用 RIR 编码器。显式条件化：SGMSE+ PESQ 2.62→约 2.86–2.89（ResNet/Conformer 嵌入），并加速收敛；DNSMOS 同步改善。RIR 可分性与去混响分数相关。

## 结论
去混响 U-Net“暗中”学 RIR 编码；显式对比 RIR 条件可提升质量与训练效率，作为概念验证。

## 点评
分析性贡献强：把黑盒特征解释成退化算子编码。条件化增益中等但一致；真实未知 RIR 时需先估嵌入，级联误差是下一步。证明“秘密切 RIR”比单纯刷分更有启发。


# FastWave: Optimized Diffusion Model for Audio Super-Resolution

- 论文编号：2721
- 报告人：Nikita Kuznetsov
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/kuznetsov26_interspeech.pdf

## 问题
音频超分辨率需要从低采样率（如 8 kHz）估计缺失的高频成分并重建到更高采样率（如 48 kHz）。现有深度方法中，扩散与流模型往往参数量大、推理慢；GAN 虽更快，但仍多为高参数网络。面向消费级低资源/端侧场景时，训练与推理成本都偏高。

## 方法
FastWave 基于 NU-Wave 2，做任意输入采样率到 48 kHz 的超分。核心改动有两类：
1. **EDM 风格扩散**：将噪声预测改为去噪器 \(D_\theta(x+n;\sigma)\approx x\)，采用输入–输出 preconditioning、加权 L2 去噪损失，并从数据估计 \(\sigma_{\mathrm{data}}\)；噪声水平按 log-normal 采样。推理用概率流 ODE 的一阶 Euler 求解与 EDM 连续噪声日程，可用较少 NFE（如 4/8）。
2. **结构压缩**：在 STFC/BSFT 等局部块中用深度可分离卷积替代标准 Conv1d，并加入 Global Response Normalization（GRN），参数量约 1.3M、约 50 GFLOPs 量级复杂度。

## 实验与结果
在 VCTK（100 说话人训练 / 8 测试，目标 48 kHz）上评估从 8/12/16/24 kHz 上采样。有限算力设定下（单卡 V100、约 30 小时量级），EDM 相对原 NU-Wave 2 baseline 收敛更好；FastWave 与 EDM 接近。与预训练/大容量模型对比（Table 2）：FastWave 4 NFE 在 8→48 上 SNR≈18.75、LSD≈1.18；24→48 上 SNR≈27.09、LSD≈0.93。相对 AudioSR 明显更优；相对 FlowHigh 在 LSD 上略逊但 SNR 往往更好。复杂度：1.3M 参数、12.87 GFLOPs/次函数评估，4 NFE 的 RTF≈0.16。

## 结论
作者给出一套可在中等算力下训练的轻量扩散超分管线，参数少、NFE 可减半，并具备面向消费设备流式/低资源部署的潜力。

## 点评
这篇工作的抓手是「扩散超分如何在质量可接受时把参数、NFE 和训练成本一起压下来」，而不是再堆更大生成器。强项是把 EDM 训练/采样配方直接迁到 NU-Wave 2，并用 ConvNeXtV2 式深度可分卷积+GRN 做结构性减参，路线清晰、可复现性强。脆弱点在于：与单步 FlowHigh 相比仍是多步 ODE、LSD 不占优；主要评测在干净 VCTK 说话人超分，对噪声/音乐等域外鲁棒性正文未深入验证。


# LavaSR: Fast and Flexible Audio Bandwidth Extension via Vocos

- 论文编号：2839
- 报告人：Yatharth Sharma
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/sharma26c_interspeech.pdf

## 问题
带宽扩展（BWE）要补全低带宽录音缺失的高频。扩散类方法（如 AudioSR）质量高但迭代采样过慢；许多 GAN 方案虽快，却常绑定固定输入/输出采样率对，或引入复杂多尺度管线，难以用单一网络覆盖任意上采样比。

## 方法
LavaSR 基于 Vocos 风格傅里叶域神经声码器：
1. 任意 8–48 kHz 输入先经 sinc 重采样到 48 kHz，得到保低频但无真实高频的基带波形。
2. 从 80-bin mel（n_fft=2048, hop=512）经 8 个 ConvNeXt 残差块（维 512，7×1 深度卷积 + FFN）预测复 STFT，再 iSTFT 得到波形。
3. **Linkwitz-Riley 风格频域 refiner**：用平滑多项式 crossover 掩码把原低频锚点频谱与生成高频线性混合，保证 crossover 附近幅度平坦、减轻相位/幅度尖刺。
训练损失含多分辨率 STFT、mel L1、多分辨率判别器（MRD）对抗损失与特征匹配；AdamW，batch 16。

## 实验与结果
VCTK（约 44 小时）训练；干净 48 kHz 随机下采到 8/12/16 kHz（sinc/ZOH/linear，可加量化噪声）再回采到 48 kHz。相对 Sinc、AudioSR、NVSR、AP-BWE：
- LSD（8/12/16→48）：Proposed 0.85 / 0.80 / 0.74，与 AP-BWE 持平或略优，优于 AudioSR/NVSR。
- ViSQOL 与 AP-BWE 接近（如 8→48 均为 3.51）。
- SI-SDR：Proposed 18.02 dB，介于 NVSR(14.68) 与 AP-BWE(18.77)。
消融显示 LR-inspired refiner（LSD 0.850）优于无 refiner / 砖墙 / Butterworth。效率：约 15M 参数；8 核 CPU RTF 0.0053（约 190×）；A100 batch32 时 RTF≈0.0001（万倍实时吞吐）。OOD 采样率上 LSD 随输入带宽单调下降。

## 结论
作者给出单一网络覆盖任意输入采样率的 Vocos 式 BWE，在频谱/感知指标上接近强 GAN 基线，同时达到极高吞吐；未来工作提到音乐、噪声场景与自适应 refiner。

## 点评
做法本质是把「任意率 BWE」改写成固定 48 kHz 网格上的频谱补全，再靠 crossover 把可靠低频钉死——工程上很聪明，也解释了为何能避开 ratio-specific 架构。相对扩散方法，质量–速度权衡是明确卖点；相对 AP-BWE，用单流复 STFT 头换来巨大 CPU/GPU 加速，但 SI-SDR 仍略逊，说明相位/波形保真仍是单头简化的代价。脆弱点包括：主评测偏干净语音、训练锚点采样率有限，且 refiner 依赖正确的低频锚点——输入低频本身已失真时收益可能下降。

