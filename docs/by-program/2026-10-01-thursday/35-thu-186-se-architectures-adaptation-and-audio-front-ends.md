# SE Architectures, Adaptation and Audio Front-Ends

- 日期：Thursday 1 October 2026
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

本场语音增强（SE）与前端覆盖双编码器融合、可调重建–抑噪损失、增强与响度联合、复合退化条件注入、脉冲神经网络、并行时–频混洗前端、无字典离散注意力、音素敏感 TF 加权损失，以及真实远场分布对齐与无监督去混响。目标从“干净波形”扩展到 ASR 友好、会议响度达标与低功耗神经形态实现。

关键设计议题包括：条件应注入各层而非仅输入层；前后端模块联合优化（SE+AGC）；前端要并行高效并对 ASR 伪影可控；真实远场需轻量潜空间对齐弥合仿真–真实鸿沟。

## 论文技术总结

# Dual-Encoder Fusion with Explicit and Implicit Injection for the Interspeech 2026 Audio Encoder Capability Challenge

- 论文编号：463
- 报告人：Ming Li
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26d_interspeech.pdf

## 问题
LALM 管线里单一音频编码器难以在分类与理解任务上全面最优；Whisper（弱监督转写）与 Dasheng（掩码声学建模）表征互补，但如何注入、保留非冗余信息并控制冗余，在 AECC 统一评测下缺乏系统研究。

## 方法
融合 Whisper-Base 与 Dasheng-Base，投影到 512 维后输出 \(Z\in\mathbb{R}^{T\times512}\)。比较 concat、MoE-concat/MoE-proj 与 token 级 softmax 门控残差融合；并加轻量 STFT 对数幅度残差支路（可学习 \(\gamma\)）。注入两种：(1) 隐式——LoRA 适配 Dasheng 后冻结双编码器，只训融合；(2) 显式——从 Whisper 线性预测 Dasheng 得残差 \(R_d=H_d-\hat H_d\)，再门控融合，并加残差能量与交叉协方差去相关正则。训练跟 XARES-LLM 官方 “all” 配方。

## 实验与结果
softmax 门控 + STFT 相对 MoE 更稳：Track A overall 0.701、Track B 0.442。隐式注入 Track A 最高（0.712±0.001），在 CREMA-D、ESC-50、GTZAN 等声学分类上更强；显式注入更多子任务最佳、Track B 略优（0.446±0.002）。MoE 可在个别任务冲高但不抬总体分。

## 结论
token 级 softmax 门控残差 + STFT 支路是稳定骨干；显式残差注入任务互补更强、可扩展多编码器，隐式 LoRA 适配整体更稳健。

## 点评
在挑战统一接口下把“怎么融”和“怎么注”拆开消融，结论可操作。未改数据采样比，部分说话人/指令类任务仍可能被融合冲淡；显式残差目前线性预测偏简，作者也提示可换更强残差预测器。


# Balancing Speech Reconstruction and Noise Suppression Using Dual-Asymmetric Loss

- 论文编号：794
- 报告人：Merlin Carson
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/carson26_interspeech.pdf

## 问题
SE 中语音质量与噪声抑制常此消彼长；资源受限模型更易偏一端。现有加权或 max 式 speech/noise 损失多不对齐相位、或不在每步同时优化两端，难用单一可调参数稳定地偏置训练目标。

## 方法
提出 Dual-Asymmetric Loss：由 \(L_{speech}\) 与 \(L_{noise}\) 线性组合 \(L=\lambda L_{speech}+(1-\lambda)L_{noise}\)。两项均含压缩复域与幅度（\(\alpha\)、\(c\) 沿用 CCMSE）；幅度用 ReLU 不对称差，复域用指示函数只在“过抑语音”或“残留噪声”的时频点计罚。\(\lambda\) 低偏抑噪、高偏保语音；\(\lambda=0.5\) 退化为缩放 CCMSE。在 LiSenNet、DPCRN、SEMamba、MP-SENet 上、VoiceBank-DEMAND 训练，并加 STFT consistency。

## 实验与结果
DNS5 Blind 与 VoiceBank-DEMAND 上，\(\lambda=0.35/0.5/0.65\) 分别抬高 BAK、平衡、抬高 SIG；\(\lambda=0.5\) 常得最高 SI-SDR。LiSenNet 扫 13 个 \(\lambda\)：与 SIG/BAK 的 PCC 为 0.95 / −0.96。\(\lambda\le0.25\) 过抑语音、\(\ge0.7\) 噪声泄漏。相对官方 SEMamba/MP-SENet 权重，在 DNS5 上 SIG/BAK/SI-SDR 有提升；WER 相对 noisy 降约 32–45%。

## 结论
单一 \(\lambda\) 可在多种因果/非因果架构上可控地权衡重建与抑噪，并与 DNSMOS 指标强相关；推荐大致落在 0.3–0.65。

## 点评
把不对称惩罚对称地扩到“残留噪声”一侧，并同时做复域，比只罚过抑更完整。依赖 DNSMOS 作调参读出；极端 \(\lambda\) 会明显失真，部署仍需按场景标定。


# SE-AGCNet: An End-to-End Framework for Joint Speech Enhancement and Loudness Control in Meeting Scenarios

- 论文编号：1023
- 报告人：Eng Siong Chng
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26n_interspeech.pdf

## 问题
会议场景音量差异大时，SE 与 AGC 级联会互相拖累：AGC 在前放大噪声，AGC 在后依赖 SE 质量且易放大残噪；SE 又易过抑远场/小声。公开 AGC 数据与标准化响度评测也不足。

## 方法
SE-AGCNet：STFT 后先 SE（MP-SENet 骨干，对过抑 bin 将 SE 损失加权 \(\times10\)），目标为干净但音量不平衡；再对 RMS 归一化幅度做 AGC（Conv2D→BiLSTM→转置卷积），目标为干净且音量平衡；ISTFT 用 AGC 幅度 + SE 相位。AGC 损失对“目标静音却预测有能”再 \(\times10\)；\(L_{total}=L_{MP\text{-}SENet}+\lambda_{AGC}L_{AGC}\)（\(\lambda_{AGC}=0.9\)），先预训 SE 5 epoch 再联合。配套 SE-AGC-DataGen 从 LibriTTS 构造 LibriAGC（音量扰动 + DNS 噪声）；响度用 LUFS / St LUFS / LRA，目标约 −23 LUFS、LRA 约 3–6。

## 实验与结果
LibriAGC：SE-AGCNet PESQ 3.00，LUFS/St LUFS ≈ −23.7/−23.9，LRA 3.86，Whisper WER 6.88，优于 MP-SENet (SE)+pyagc 等。真实 MMCSG / AliMeeting-far：响度回到约 −23，MMCSG WER 13.86/30.36，AliMeeting CER 34.43，优于级联与单模型同时学 SE+AGC。

## 结论
联合优化使 SE 保小声、AGC 调响度，比级联或单网络硬学两任务更稳，并改善下游 ASR；模块可挂接其他 SE 骨干。

## 点评
把会议“远近音量”与增强绑在同一端到端目标里，并引入 ITU/EBU 响度指标，评测比只看 PESQ 更贴场景。依赖自建仿真与固定 −23 LUFS；多通道只取第一路，复杂声学仍待扩展。


# SLICE: Speech Enhancement via Layer-wise Injection of Conditioning Embeddings

- 论文编号：1715
- 报告人：Seokhoon Moon
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/moon26_interspeech.pdf

## 问题
真实语音常同时受加性噪声、混响与非线性失真；扩散 SE 在单退化上强，但噪声感知条件若只加在输入层，在复合退化上甚至不如无条件模型，且条件信号在深层残差块中被稀释。

## 方法
在 SGMSE+ / NCSN++ 上提出 SLICE：冻结 WavLM-Base 提特征，经投影得共享 \(h\)，再分三头（噪声 11 类 CE、\(T_{60}\) MSE、失真强度 MSE）监督；三路投影拼接后 MLP 得 \(c_{extra}\)，加到 timestep embedding，从而经全部残差块传播，无需改骨干。训练损失 \(L_{score}+\lambda\sum L_{aux}\)（\(\lambda=0.3\)），并做分支 CFG dropout。数据在 VoiceBank-DEMAND 上叠加合成混响与 soft-clip 失真。

## 实验与结果
同数据消融：layer-wise 在多退化上 ESTOI 0.80、SI-SDR 3.7、UTMOS 3.71；输入级 addition 仅 0.73 / 1.4 / 3.62，弱于无编码器（0.77 / 2.3 / 3.70）。相对仅噪声训练的 SGMSE+/NASE 等，多退化提升明显。噪声-only 上 UTMOS 最高（3.93）。野数据（VOiCES/DAPS/URGENT）上多退化训练是主因，编码器增益不如受控集显著。

## 结论
条件“怎么注入”与“有没有条件”同样关键：经 timestep 的逐层注入优于浅层输入相加，配合多任务退化表征可联合处理噪声/混响/失真。

## 点评
用受控对照把“注入深度”钉死，对条件扩散 SE 很有启发。混响仍拖累 SI-SDR；野数据上与无编码器差距缩小，说明编码器标定与域偏移仍是短板。


# Neuromorphic Speech Enhancement with Dual-Branch Spiking Neural Networks

- 论文编号：1797
- 报告人：Wenbin Jiang
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/meng26d_interspeech.pdf

## 问题
SNN 增强参数少、适合神经形态硬件，但二值脉冲与单分支谱建模使质量仍落后主流 ANN；现有工作少在双路径框架里系统利用幅度与复谱的互补性。

## 方法
GSU-DBNet：STFT 实部/虚部/幅度三通道经带 CBAM 的卷积编码器 → 两层双路径 GSU（频向 BiGSU、时向因果 GSU）→ 双分支转置卷积解码器：复分支 tanh 输出作 DeepFilter 系数，幅度分支 sigmoid 掩码乘噪声幅度，再加权融合。GSU 仅单遗忘门更新膜电位并以 Heaviside 发脉冲（三角 surrogate）。损失为压缩谱 MSE + SI-SNR。

## 实验与结果
VoiceBank+DEMAND：394K 参数下 PESQ 3.04、CSIG 4.28、CBAK 3.57、COVL 3.68、SSNR 9.94，优于 DPSNN（PESQ 2.20）与 Spiking-FSN（2.66），并超过若干更大 ANN（如 DCCRN/FullSubNet+/GaGNet）。消融显示双分支、双路径均必要；多门 SLSTM 参数升而 PESQ 不升反降；平均放电率约 37%。

## 结论
单门 GSU + 双路径双分支可在极少参数下拉近与 ANN 的 PESQ 差距；二值输出瓶颈下加门无益，适合稀疏事件驱动部署方向。

## 点评
把 ANN 里成熟的双路径/双谱思想迁到 spiking 单元，参数效率叙事清晰。评测主要在合成 VoiceBank；真正神经形态芯片上的能耗/时延未实证，CSIG 仍略逊 TSTNN。


# Parallel Time-Band Mixing with Learned Observation-Adding for Robust ASR Front-Ends

- 论文编号：1972
- 报告人：Xingyu Shen
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/shen26c_interspeech.pdf

## 问题
SE 作 ASR 前端时常引入伪影伤识别；BSRNN 类 band-split 前端依赖时序/跨带 RNN，块内串行、并行效率差，且 Observation-Adding（OA）系数常需开发集手调。

## 方法
并行 Time–Band Mixer（PTBM）：子带嵌入后堆叠 \(L\) 块，每块并行做 (1) Temporal ConvMixer——门控膨胀深度卷积做带内时间混合；(2) Cross-Band Attention——每帧对 \(K\) 子带自注意力；门控融合 + 残差。重建为 mask-plus-residual \(\hat S=M\odot X+R\)。Learned OA（LOA）：用能量比与对数幅度差统计量经小 MLP 预测 \(\omega\)，\(s_{LOA}=\omega x+(1-\omega)\hat s\)；先训 SE（MR-STFT+SI-SNR），再冻 SE、用网格搜索 oracle \(\omega^*\) 回归训 LOA。V4 子带划分（\(K=23\)），默认 \(L=12\)。

## 实验与结果
DNS Challenge 与 CHiME-4、冻结 Whisper Tiny/Medium/Large：相对 BSRNN 与 Zhao 等轻量 band-split，WER 全面更低，前端仅 0.96 M / 0.58 GMAC/s。消融：去 TCM 或 CBA 均升 WER；无 OA 差于固定 OA，LOA 最好且免开发集调 \(\omega\)；\(L=12\) 性价比优于 6/9，相对 15 增益收益有限。

## 结论
并行时–带混合可替代块内 RNN 做高效 ASR 前端，LOA 自适应混合观测与增强以抑制伪影，在合成与真实噪声上稳定降 WER。

## 点评
目标对准“下游 ASR 而非听感”，LOA 把人工 OA 自动化很实用。LOA 为 utterance 级、非全流式；训练仍无 ASR 梯度，极端失配时可能不如适配器式前端。


# Dictionary-Free Discrete Key-Value Attention for Improving Speech Enhancement

- 论文编号：2881
- 报告人：Zihao Cui
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/cui26b_interspeech.pdf

## 问题
Harmonic Attention（HAtt）用手工谐波字典改善浊音谱重建，但对清音/无声段弱；依赖先验的固定字典限制了更全面的 key–value 结构化表征。

## 方法
提出 Dictionary-Free Discrete Attention（DFDA）：用 Finite Scalar Quantization（FSQ）在注意力前离散化 key 与 value（轻量 encoder–quantizer–decoder，无需显式可学习 codebook），形成信息瓶颈以稳住语音相关模式、抑制噪声随机波动。嵌到 TFGridNet：前两层注意力换成 DFDA；并与前端 HAtt 组合。损失为压缩幅度/复谱 + SI-SNR。

## 实验与结果
约 25k 小时语音 + DNS 噪声 + RIR 训练；seen 与 Emilia/LibriSpeech unseen 评测。TFGridNet+HAtt+DFDA 在 Emilia 上 PESQ 2.89、ESTOI 90.7、SISNR 16.55，优于基线与单用 DFDA/HAtt；UV SSNR 最高（seen 8.84），验证清音恢复。DFDA 仅增约 0.48 GMACs。

## 结论
数据驱动的离散 key–value 与谐波先验互补，联合使用可同时加强谐波与清音结构，提升质量与可懂度。

## 点评
把神经编解码里的 FSQ 瓶颈搬进 SE 注意力，避开手工字典，与 HAtt 的互补叙事清楚。对比主要相对 TFGridNet 变体，生成式 SE 骨干上的迁移仍待验证。


# Time–Frequency Weighted Losses for Phoneme Reconstruction in DNN-Based Speech Enhancement

- 论文编号：3416
- 报告人：Nasser-Eddine Monir
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/monir26_interspeech.pdf

## 问题
基于 SDR 的增强训练对时频均匀加权，忽视辅音爆发、摩擦等高可懂度线索及强语音–噪声竞争区；既有频率加权 SDR 未统一结合语音存在、局部 SIR 与瞬态动态。

## 方法
在 Mel 域定义 TF 加权 SDR \(L_w\)。提出：(1) \(L_{SIR\cdot SP}\)：sigmoid 门控低 SIR 与语音存在；(2) \(L_{SIR\cdot SP\cdot SF}\)：再乘光谱通量（spectral flux）放大瞬态；(3) \(L_{learn}\)：可学习频带权重（ANSI 1997 初始化）。在 FaSNet（4 通道助听器阵列）上相对时域 \(L_T\) 与先前 \(L_{logSIR}\) 比较。

## 实验与结果
白噪（WN）与语音整形噪（SSN）、SIR −8～8 dB。\(L_{SIR\cdot SP\cdot SF}\) 在 WN 上 FW-SIR/FW-SDR 与辅音/元音音素准确率（PA）更稳；塞音 PA 在中高 SIR 显著高于基线；谱分析显示中频结构在 0/8 dB 更接近干净参考。SSN 下 STOI/部分失真指标有代价，但干扰抑制与高 SIR 识别更一致。

## 结论
把 SIR、语音存在与光谱通量并入可微 SDR 权重，可改善干扰抑制与音素级重建，尤其利于辅音/塞音；适合助听器式场景中对瞬态线索的强调。

## 点评
训练目标直接对准“竞争 TF + 瞬态”，比全局 SDR 更贴可懂度。SSN 与极低 SIR 上收益变弱，且未做听音试验，与真实感知仍隔一层。


# Bridging the Distribution Gap in Real-World Far-Field Speech Enhancement via Lightweight Latent Representation Alignment

- 论文编号：3478
- 报告人：Biao Liu
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/liu26s_interspeech.pdf

## 问题
真实远场相对近场干净语音存在严重中高频衰减与传播特性差异，仿真 RIR 训练易失配；轻量单阶段网络直接学复杂映射往往不足，大模型又算力过高。

## 方法
采集约 70 小时同步近场–远场配对（AISHELL-3 内容，10 场景，4/6/8 m）。两阶段轻量框架：冻结预训练 GTCRN 做粗去噪/去混响；DAC 式编码器学干净近场潜空间，轻量 ConvNeXt 映射网络把粗增强信号投到该潜空间，再解码重建。分阶段训练：先联合训 AE+映射，再冻编码器微调映射与解码器。对齐损失为潜空间 MSE，AE 用多尺度 Mel + 对抗。

## 实验与结果
真实远场测试集：Proposed 约 10.38 M / 0.8 GMAC/s，P.835 OVRL 2.94、SIG 3.23、BAK 4.01、P.808 3.35，优于在仿真或真实数据上训的 GTCRN、LiSenNet、因果 TF-GridNet。轻量基线直接用真实数据训练未必提升，说明难映射问题需对齐分解。

## 结论
粗增强 + 干净潜空间对齐可在低算力下缩小仿真–真实远场分布差，提升感知质量。

## 点评
把难题拆成“先抑噪再对齐近场流形”，对设备端远场很务实；自建配对数据是关键资产。映射依赖近场参考训练，无配对场景需另寻无监督对齐。


# ARTT: Augmented Reverberant-Target Training for Unsupervised Monaural Speech Dereverberation

- 论文编号：1857
- 报告人：Wei-Qiang Zhang
- 程序：Thursday 1 October 2026 / SE Architectures, Adaptation and Audio Front-Ends
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/song26d_interspeech.pdf

## 问题
单通道无监督去混响缺少干净参考与空间线索，属病态逆问题；WPE 难用深度先验，USDnet 等常依赖多通道约束，生成式方法算力重；Noise2Noise 式 NyTT 因混响相关卷积而难以直接套用。

## 方法
ARTT 两阶段：(1) Reverberant-Target Training（RTT）——观测混响混合再与随机统计 RTF（指数衰减扩散尾）卷积，判别式训练 DNN 重建原观测，因卷积交换律倾向同时削弱合成与真实混响；(2) mean-teacher 自蒸馏——教师吃轻噪观测，学生吃相对 RIR 卷积 + 噪声的加重腐化输入，蒸馏损失对齐教师伪标签并辅以重建观测的 \(L_{aux}\)。骨干 TF-GridNet，损失 SI-SDR-SE + 幅度 L1。

## 实验与结果
WSJ0CAM-DEREVERB 单通道：RTT 阶段 SI-SDR 3.3 / PESQ 2.18；完整 ARTT 达 7.3 / 2.61 / eSTOI 0.832，超过 WPE、单通道 USDnet、BUDDy 及监督 DNN-WPE。消融显示 \(L_{aux}\) 与噪声注入对稳定与抑噪关键；Stage II 在低 SNR 更稳。

## 结论
用“再混响→重建观测”构造监督信号，再加非对称自蒸馏，可在无干净参考下实现强单通道去混响。

## 点评
把 NyTT 思路改成相关混响增广，物理直觉清楚；Stage II 显著抬升说明仅 RTT 不够稳。评测仍在仿真基准，真实房间泛化与作者未强调的多通道潜力留待验证。

