# Target Speaker Extraction, Speech Separation and Audio Understanding

- 日期：Tuesday 29 September 2026
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

本场主线是目标说话人提取（TSE）与分离在“线索多样化、场景真实化、生成式增强”上的扩展。单声道分离侧，时频 Transformer 通过内容感知滑窗注意力联合建模局部与全局；生成式路径则把说话人日记化与潜空间 flow matching 结合，并以对抗说话人引导缓解说话人混淆。线索侧从传统注册音、DOA 扩展到唤醒词注册、HRTF 空间先验、耳 EEG 神经引导，以及唇动语义 token、多视角唇部与波束域声噪交互。

音视频 TSE 强调超越正面唇同步：有工作把唇动先变为粗粒度语义 token 再引导提取，也有用多视角张量融合在训练期学习跨视角相关、推理期支持单/多视角；多通道方案则结合掩码波束形成与跨波束注意力，在真实录音与远场仿真上报告 WER 改善。与此同时，通用音频理解编码器 USAD 2.0 通过域感知蒸馏、音乐域覆盖与深度扩展到十亿参数，服务于下游探测与音频 LLM。

整体上，本场从“谁说话”的线索工程走向空间、视觉与神经多线索，并在判别式分离与生成式高保真之间形成互补；交互场景则关注无预注册、短噪唤醒词等可用性瓶颈，辅以 LLM-TTS 注册增强。

## 论文技术总结

# TF-MossFormer: Integrating Convolution Gated Local-Global Attentions for Enhanced Time-Frequency Domain Monaural Speech Separation

- 论文编号：218
- 报告人：Shengkui Zhao
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhao26_interspeech.pdf

## 问题
单声道分离既需短时谱连续性（谐波、音素过渡），也需长程说话人一致性。全局 Transformer 注意力易忽略局部细节，静态卷积感受野又不够灵活；时域分块方法未能充分利用二维频谱的时–频几何结构。

## 方法
TF-MossFormer 在 STFT 域预测复谱实部/虚部：Conv2D+gLN 编码后，堆叠 B 个交替频率/时间建模块，每块含 Conv-SwiGLU、RMSGroupNorm 与卷积门控的局部–全局 MHSA。局部注意力为滑动窗（时间窗 wT、频率窗 wF），全局为标准 MHSA；门控为 Conv1D+Swish。消融比较三种布局（V1：局部→全局最优；V2 反向；V3 并行）及去掉门控的 V4。S/M/L 三档：D∈{96,128,128}，B∈{4,6,9}，参数约 6.0/16.9/25.4M。训练用 SI-SDR、AdamW、4 s 片段、16 ms 窗 / 8 ms hop。

## 实验与结果
在 WSJ0-2Mix（8 kHz）上，窗口 (wT,wF)=(31,7) 最佳，S 模型 SI-SDRi 22.61 dB。V1 优于 V2/V3/V4。与同规模对比：S 为 22.6 SI-SDRi（优于 TF-Locoformer(S*) 22.2、SPMamba 22.5）；M 为 24.0（优于 TF-GridNet 23.5、TF-Locoformer(M) 23.6）；L 为 24.4（优于 TF-Locoformer(L) 24.2、MossFormer2(L)+DM 24.1）。

## 结论
内容感知滑动窗局部注意力、局部先于全局的布局，以及卷积门控，共同带来多尺度上的 SOTA 分离表现，并保持相对有利的参数与算力。

## 点评
工作把“局部连续性 + 全局分组”落到 TF 双路径上，用可调窗替代固定卷积局部建模，门控再做特征筛选。强项是尺度扩展一致且相对 TF-GridNet 更省算力；评测仍集中在两说话人完全重叠的 WSJ0-2Mix，对更复杂噪声/混响场景的外推需另证。


# Enroll-on-Wakeup: A First Comparative Study of Target Speech Extraction for Seamless Interaction in Real Noisy Human-Machine Dialogue Scenarios

- 论文编号：259
- 报告人：Yiming Yang
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26b_interspeech.pdf

## 问题
传统 TSE 依赖预录高质量 enrollment，打断自发人机对话；希望仅用唤醒词片段做“Enroll-on-Wakeup”（EoW），但约 1 s、含噪声与干扰的参考线索稀缺且被污染，现有模型在真实场景下的表现与 ASR 友好性尚缺系统评估。

## 方法
定义 EoW-TSE：KWS 切出 xwake 与后续 xquery，以 xwake 为条件抽取目标。评测四类模型——判别式 SEF-PNet、LExt、CIE-mDPTNet 与生成式 SoloSpeech；判别式在 Libri2Mix train-100（mix both）训练，SoloSpeech 用作者预训练。针对短噪 enrollment，用 IndexTTS2、xTTS、CosyVoice3 做 Clean Re-synthesis（CR）与 Extended Concatenation（EC）增强。测试为 Unisound 五场景真实录音（Close/Far Noise±Reverb，SNR 10/5 dB，中文唤醒词“Hi, Pandora/Hello, Cube”），指标含 SI-SDR、PESQ、STOI、DNSMOS、WER（Fun-ASR）。

## 实验与结果
Libri2Mix 2spk+noise 上 SoloSpeech SI-SDR 11.12、LExt 10.47 等，建立基线。EoW 五场景：SoloSpeech OVRL 最高，但远场/混响下 WER 急剧恶化；CIE-mDPTNet WER 最稳，然各模型均未优于直接对噪声混合物做 ASR。TTS 增强中 IndexTTS2 更常降低 enrollment 侧 WER；对 CIE-mDPTNet，CR/EC 提升 DNSMOS，却未能降低提取后 WER，EC 相对 CR 感知略好、识别相当。

## 结论
首次系统评估 EoW-TSE：生成式偏感知、判别式偏 ASR，整体存在感知–识别鸿沟；约 1 s 唤醒参考下模型远非理想，TTS 可减轻线索污染但无法自动修好可懂度与 ASR。

## 点评
问题设定贴近产品链路（唤醒即注册），价值在真实五场景对比与 TTS 增强诊断，而非提出新分离骨干。脆弱点在于线索极短且与查询同场景污染，以及生成式修谱易引入音素失真——后续更需 ASR-aware 目标或保留更多声学细节的约束，而不是只刷 DNSMOS。


# HRTF-guided Binaural Target Speaker Extraction with Real-World Validation

- 论文编号：807
- 报告人：Yoav Ellinson
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ellinson26_interspeech.pdf

## 问题
双耳 TSE 若仅用 DOA 或 enrollment，常破坏 ILD/ITD，造成视听位置不一致；基于个体 HRTF 的条件化若只针对单听者又难泛化。需要跨听者、以 HRTF 为显式空间先验、并做去混响的双耳提取。

## 方法
目标为提取直达路径 BRIR 调制的双耳目标语（M=0），以直达 HRTF hhrtf(θ,ϕ) 为线索。骨干为 NBSS：对混合物与 HRTF 分编码后在潜空间逐元素相乘调制，再经 P=8 个 NBC2 块，线性解码复谱。损失为双通道平均 SI-SDR + STFT MAE，末段仅 SI-SDR 微调。训练用 WSJ0 + SofaMyRoom 仿真 BRIR（T60∈[0.2,0.8] s，SIR∈[−5,5] dB），789 个实测 HRTF（ARI、SONICOM 等）训练/验证，7 个未见受试测；对比同骨干的 DOA-BDE。

## 实验与结果
仿真 2000 样本：Proposed SI-SDRi 15.770、PESQ 3.03、ΔITD 0.044 ms、ΔILD 0.349 dB，全面优于 DOA-BDE（13.881 / 2.74 / 0.982 / 0.479）。HATS 真实录音（T60=0.37 s，角距 20°–90°）：平均 NISQA Proposed 3.22 vs DOA-BDE 3.14，角距越大分数越高；即便 HRTF 库角分辨率导致最近邻失配仍保持优势。

## 结论
在多样实测 HRTF 上训练、推理用目标方向 HRTF 条件化，可跨听者保持双耳线索并提升感知质量；真实 HATS 验证有效，角量化误差下仍稳健。

## 点评
核心是把“方向线索”从 DOA 标量升级为完整双耳滤波形状，使提取与空间重建耦合，天然利于 ITD/ILD。代价是依赖可用 HRTF 库分辨率与目标方位已知；对近距离或与库几何不符的场景，最近邻条件可能成瓶颈。


# NeuroMultiSpEx: Neuro-Guided Target Speaker Extraction for Multi-Speaker Scenarios

- 论文编号：1120
- 报告人：Siqi Cai
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/silva26_interspeech.pdf

## 问题
神经引导说话人提取多用 scalp-EEG、且几乎只做 2 说话人；真实鸡尾酒会常 ≥3 人，排列歧义更大，仅 envelope 或仅身份线索不足，可穿戴 ear-EEG（cEEGrid，20 通道）信息量也更受限。

## 方法
NeuroMultiSpEx 输入 4 说话人混合物 + 20 通道 ear-EEG：EEG-Envelope Encoder（Pre-Conv + 4×SA/TCN）重建目标 envelope 并输出时序线索；EEG-Speaker Encoder（XAGnet：双耳 GCN + 跨耳 CA，MHA Adapter）输出 4 类身份与时序身份特征；Gated Fusion 自适应加权“何时/何人”得 HRef；Conv-TasNet 式提取网络用交叉注意力以 HRef 为 Query 调制混合编码并生成 mask。联合损失 SI-SDR + λ1 CE + λ2 PCC。

## 实验与结果
PKU Ear-EEG（16 人，±30°/±90°，0 dB SNR，trial 独立 80/10/10）：NeuroMultiSpEx SI-SDRi 9.613、PESQ 2.08、STOI 0.708、AAD 82.4%、envelope PCC 0.023，显著优于 NeuroSpEx+（8.904 / 1.84 / 0.683）等基线。说话人编码器消融：XAGnet 优于 FC/CNN/STAnet/XAnet；去掉身份编码器降幅最大（−0.407 dB），去掉门控改拼接亦降约 0.2 dB。

## 结论
在可穿戴 ear-EEG 上首次将神经引导提取扩展到 4 说话人；时序与身份双线索加学习门控优于单线索，朝脑控助听更近一步。局限含跨被试、混响与听障用户未评。

## 点评
抓住多说话人下“错抽干扰”的排列风险，用 AAD 式身份显式消歧，再靠 envelope 补帧级“何时”。强在双编码器与门控设计贴合场景；评测说话人依赖、PCC 绝对值低反映 ear-EEG 空间分辨率限制，跨被试泛化仍是落地关键。


# USAD 2.0: Scaling Representation Distillation for Universal Audio Understanding

- 论文编号：1296
- 报告人：Heng-Jui Chang
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chang26c_interspeech.pdf

## 问题
SSL 编码器多偏单域；USAD/SPEAR 等跨域蒸馏覆盖与评测仍有限，且监督式编码器往往更适合作音频 LLM 前端。需要同时吸收 SSL 与监督教师、覆盖 speech/audio/music，并在可控算力下扩到约 10 亿参数。

## 方法
USAD 2.0：域感知蒸馏——输入域与教师匹配时提高权重（ω=10，软权重仍保留错配教师）；教师为 WavLM、ATST-Frame、MuQ，数据含多语语音约 116K h、通用音 21K h、音乐 13K h。USAD 2.0+：以 SSL 学生初始化，二阶段蒸馏 Whisper Large-v3 与 Audio Flamingo 3 编码器末层。扩容：帧率 50→25 Hz，并用 depth up-scaling 将 XLarge（32 层）扩到 XXLarge+（48 层，约 1036M）。

## 实验与结果
HEAR 上 USAD 2.0+ XLarge+/XXLarge+ Avg 84.4，优于先前单编码器 SOTA；MARBLE 上无监督 Large 75.8，有监督变体保持竞争力；XARES-LLM Track B 上 XXLarge+ 达 0.624。消融：去域感知蒸馏 PR PER 升至 13.3；无音乐教师 NSynth Acc 从 70.3 掉到 49.1；二阶段从 SSL 初始化优于从头；depth up-scaling 优于均匀复制/新顶层。25 Hz XXLarge 推理快于 50 Hz Large，峰值显存约 2.4 GB。

## 结论
域感知三域 SSL 蒸馏 + 监督二阶段 + 高效深度扩展，得到跨域均衡且适合作 LLM 前端的通用编码器，并在学术预算内扩到 1B。

## 点评
路线是“多专家蒸馏成单前端”，域权重与音乐教师补齐先前 USAD 短板，监督二阶段对准 LLM 语义对齐。强在 HEAR/LLM 评测一致抬升；MARBLE 上有监督变体略低于部分无监督分数，说明对齐 LLM 与保留细粒度音乐表征之间仍有张力。


# Latent Flow Matching Based Speech Separation Using Speaker Diarization

- 论文编号：1401
- 报告人：Sharon Gannot
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rubenchik26_interspeech.pdf

## 问题
判别式分离易过平滑；生成式虽保真，但条件弱时易 speaker confusion（忽略条件、反复抽同一人）。希望用 diarization 从混合物自取说话人线索，且尽量只训练轻量生成模块。

## 方法
冻结 EEND-EDA、mel-VAE、vocoder：由 EEND 得说话人 attractor 与活动概率，按活动池化后拼接为条件，经 FiLM 注入潜空间 Flow Matching U-Net；输入为混合物潜变量与中间噪声潜变量拼接。训练用 PIT 选排列；推理引入训练无关的 Adversarial Speaker Guidance（ASG），用干扰说话人速度场作负条件并与 CFG 组合。另做 ECAPA enrollment 变体作对照。

## 实验与结果
LibriSpeech 动态混合训练（SIR [−5,5] dB），LibriMix 16 kHz min 测试。Ours：OVRL 3.20、DNSMOS 3.76、WER 13.26、SIM 0.81、TSIM 0.08%；无指导时 TSIM 0.14%。ECAPAv TSIM 高达 9.7–12.7%，SoloSpeech TSIM 0.8%。ASG 降低混淆并略提质量。相对 SoloSpeech（OVRL/DNSMOS/WER 更优），本文在无 enrollment 分离设定下混淆率显著更低、可懂度更好。

## 结论
仅训潜空间 FM U-Net，用混合物衍生 EEND attractor 条件化即可达可比感知质量，并大幅降低 speaker confusion；ASG 对 enrollment 与 diarization 条件均有益。

## 点评
关键是把 diarization attractor 当作“从混合物即时得到的说话人条件”，比通用验证嵌入更贴分离歧义；TSIM 指标直接量化“两路输出几乎同一内容”的失败模式。脆弱点在于依赖预训练 EEND 质量，且作者也指出更关键的是 attractor 可分性而非 DER，鲁棒分析留待后续。


# TGTSE: Token-Guided Target Speaker Extraction with Visual Cue

- 论文编号：1710
- 报告人：Zhong-Qiu Wang
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ling26_interspeech.pdf

## 问题
音视 TSE 常用唇部连续嵌入条件化，但视觉与声学模态异构、对齐不稳，嵌入只是相关特征而非生成必要变量；希望用与语音生成更紧耦合的离散语义 token 作时序对齐线索。

## 方法
TGTSE 两阶段：token predictor（DNN1）以冻结 3D-ResNet18 唇特征 + 混合物 STFT 幅度，经 Transformer 预测 WavLM-KM 伪标签（WavLM-Large，K-means）；再将预测 token 经可训练码本嵌入，条件化 extractor（DNN2）——TF-GridNet 或 MossFormer2，损失为负 SI-SDR。伪标签用 LibriSpeech 子集重做；提取网络与码本端到端训练。

## 实验与结果
VoxCeleb2-2Mix / LRS2-2Mix（SNR −10–10 dB）。Oracle token 消融：K=128 最佳；token 准确率约 60% 已有合理提取。TGTSE(MossFormer2) 在两集上 SDR 15.2/16.2、SI-SDR 14.8/15.7；相对 AV-TFGridNet，TGTSE(TFGridNet) SDR/SI-SDR 分别提升约 0.7/0.9 dB。跨域 LRS3、TCD-TIMIT、Grid 上亦全面优于同骨干 AV 基线。

## 结论
将唇动映射为离散语义 token 再引导提取，可缩小跨模态鸿沟，在基准与跨域集上持续优于常规 AV-TSE。

## 点评
做法把 AV 条件从“相关视觉嵌入”换成“语音侧离散语义”，对齐与监督都更像 ASR/生成式序列问题。强在对 backbone 可插拔且跨域仍涨；弱点是依赖伪标签质量与 token 预测准确率——K 增大预测变难，而真实噪声视觉下 token 错误会直接传导到提取。


# Multi-View Based Audio Visual Target Speaker Extraction

- 论文编号：2035
- 报告人：Peijun Yang
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26m_interspeech.pdf

## 问题
多数 AV-TSE 默认正面脸视频，真实场景常为侧脸/俯仰视角，正面化可能丢信息；多视角同步数据若只在训练时可用，如何把跨视角相关转成单视角测试增益仍不明确。

## 方法
MVTF-GridNet：唇编码器提各视角嵌入，线性插值对齐音频帧，LSTM 后做成对外积（带常数 1）建模乘性交互，再 Flatten+LayerNorm+Linear 并平均得融合视觉上下文，送入 TF-GridNet。训练可用随机三视角；推理缺视角则复制现有视角填满。损失 SI-SDR。

## 实验与结果
MEAD 中性情感、7 视角、两说话人混合（SNR −10–10 dB）。随机三视角训练的 MVTF 单视角平均 SI-SDR 15.718，优于仅正面 MVTF（14.102）与随机单视角 GridNet（15.089）；混合视角旋转测试上 MVTF 15.834，正面 GridNet 仅 10.425。多视角推理组合 SI-SDR 约 15.85。外积融合优于投影相加与注意力融合；相对 PIAVE 平均 SDR 约 10.81 vs 8.18（设定不完全严格可比）。

## 结论
训练期显式建模多视角乘性交互，可在单视角甚至头部转动混合视角测试下提升鲁棒性，且参数/算力增幅很小。

## 点评
把“姿态变化”从要矫正的噪声改成可学习的互补发音信息，外积融合比简单加和更贴合跨视角相关。强在训练–测试视角不对称仍有效；数据限于 MEAD 中性情感与固定相机几何，开放场景姿态连续变化需再验证。


# AV-SNINet: A multi-channel audio-visual speech-noise interaction network for Target Speaker Extraction with cross-beam attention

- 论文编号：3227
- 报告人：Yanhui Tu
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/tu26c_interspeech.pdf

## 问题
远场多通道 AV 提取多靠唇音同步增强目标，较少在波束域显式做目标–干扰互斥抑制；低 SNR 下 mask 波束成形残差仍拖累 ASR。

## 方法
两阶段：① AV-DPCRN 用 LPS+IPD+唇特征估 IRM，经 GEVD 得目标/干扰波束；② AV-SNINet 双分支 DPCRN 分别吃 Concat(Gs/Gn, LPS, Lip)，瓶颈插入 cross-beam attention——帧级交叉注意后从对方分支减去“像对方”的成分，联合估言语/噪声 IRM（λs=λn=1）。视觉编码器冻结于 LRW 预训练。

## 实验与结果
自建环形阵真实录音与匹配设定的 LRS2 远场仿真（SNR −10–+10 dB，距离 0.5–2 m）。真实集平均 WER：Baseline 28.40 → AV-SNINet 20.38（相对降 28.23%）；双塔 interactor（v3）优于共享注意矩阵变体。LRS2 仿真平均 WER 17.20，优于 USEV+GEVD（19.37）与 RTFS-Net+GEVD（20.47）。

## 结论
波束先验加双分支交叉注意可进一步压低残差干扰，低 SNR 与远场下 ASR 收益明显。

## 点评
抓住的是“目标波束与干扰波束应互相排斥”这一空间–谱结构，比单纯 AV 融合更直接。指标以黑盒 ASR WER 为主，贴落地；代价是依赖第一阶段 mask 质量，且大量结果来自自建场景，公开可比性主要靠 LRS2 仿真补充。

