# Generative and Self-Supervised Speech Enhancement

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster（Area 6）
- 论文数：12
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

本场生成式与自监督语音增强高度集中于 flow matching / 扩散，并把条件信息从浅层噪声特征推向语义、谐波、SSL 与说话人先验。Seed-Enh 在解耦语义（冻结 Whisper）与音色（CAM++）空间做 flow matching 融合；HFMSE 显式提取基频定位与谐波掩码作强条件；PhASE-Flow 直接在 SSL 潜空间对“音素条件声学表示”做流匹配；另有工作用 wav2vec 2.0 + FiLM 锚定扩散反向过程。

噪声鲁棒带宽扩展 VeRe-Flow 用速度对比正则与干净 SSL 表示对齐提供多层干净监督。条件说话人嵌入方面，G-MaP-SE 以 GMM 干净嵌入先验匹配噪声条件嵌入，免注册音频。无监督线则分析 GAN 先验泄漏（对齐噪声先验可减泄漏），并提出多判别器 UFL-GAN 结合自监督辅助。

训练动力学与简化建模同样受关注：SGCM 从连续时间扩散梯度冲突的理论下界导出自适应更新方向；Autonomous Rectified Flow 论证线性插值目标向量场本征时不变，从而去掉显式时间步条件。边缘部署侧 WaveNorm 以因果时域神经 AGC 满足 ITU 响度规范。瓶颈是噪声下条件不可靠、合成—真实域隙、先验泄漏与扩散训练冲突。

## 技术内容

### 解耦空间、谐波与 SSL 条件生成

**Seed-Enh: Generative Speech Enhancement in Decoupled Semantic and Timbre Spaces**（论文 200；Zengqiang Shang）
指出声学空间中噪声与语音纠缠导致伪影。Seed-Enh 三阶段：冻结 Whisper 提噪声鲁棒语义、CAM++ 与上下文处理音色、flow matching 融合。摘要称整体质量分高于先进基线，并可在噪声输入上做零样本音色转换且优于 Seed-VC。

**VeRe-Flow: Guiding Flow Matching toward Clean Speech via Velocity Contrastive Regularization and Representation Alignment for Noise-Robust Bandwidth Expansion**（论文 712；Sujin Koo）
为噪声鲁棒带宽扩展引入速度对比正则（吸引干净轨迹、排斥噪声轨迹）与中间特征对齐干净 SSL 表示。结果在所列基线中 LSD 最低、DNSMOS OVRL 最高，生成基线中 MOS 最高。

**HFMSE: Harmonic-Guided Speech Enhancement with Flow Matching**（论文 722；Xinhong Li）
设计高效谐波编码器：基频定位 + 谐波掩码生成，将谐波结构特征作为 flow matching 强条件。DNS Challenge 2020 上称达先进性能。

**PhASE-Flow: Phonetic-Conditioned Acoustic Flow Matching in SSL Representation Domain for Speech Enhancement**（论文 916；Jun Gao）
在 SSL 空间建模干净声学表示在音素表示条件下的分布，再经神经声码器重建。感知质量与可懂度超先进基线，且仅四采样步即可具竞争力。

**Bridging Self-Supervised Learning and Speech Enhancement: A Wav2Vec2-Conditioned Framework**（论文 964；Shuubham Ojha）
用噪声输入的 wav2vec 2.0 特征经 FiLM 注入 U-Net 瓶颈，并以指数平滑聚合 FiLM 系数。VoiceBank-DEMAND 与 LibriMix 上相对无条件基线 PESQ 等指标有提升（摘要称 PESQ 持续改进约 0.4）。

### 目标域无干净数据、说话人先验与无监督 GAN

**Text-Annotated Noisy Speech as Supervision: A Dual-Learning Framework for Target-Domain Clean-Free Speech Enhancement**（论文 1259；Xueliang Zhang）
SwitchSE 利用转写—噪声语音对，以开关控制机制在真实环境无干净目标语音时微调预训练 SE。仅 2.9 小时 CHiME-3 真实噪声即可显著提升目标域并保持原合成域性能。

**G-MaP-SE: Guided Speech Enhancement via GMM-Based Prior Matching**（论文 2148；Yike Zhu）
用 GMM 建干净语音嵌入先验，将噪声条件嵌入匹配到该先验，再经门控融合注入时频增强主干，推理无需注册音频。在 VoiceBank+DEMAND 与 DNS 2020 上持续优于噪声条件，并大幅逼近干净条件上界。

**Analysing Adversarial Priors for Data-driven Unsupervised Speech Enhancement**（论文 2511；Dominik Klement）
分析无监督 GAN 增强中先验数据：失配先验增加源泄漏；采用易采集的对齐噪声先验可显著减轻语音—噪声泄漏、防止过抑制并改善感知质量。双分支框架显式建模干净语音与噪声。

**UFL-GAN: A Multi-Discriminator GAN for Unsupervised Speech Enhancement**（论文 2565；Satvik Bejugam）
无配对数据的多判别器 GAN，分别刻画话语级与帧级特性，并引入预训练自监督表示辅助生成器。VoiceBank+DEMAND 上侵入/非侵入质量指标可比或优于对比方法。

### 扩散训练稳定、无时间条件流与实时 AGC

**Self-adaptive Gradient Conflict Mitigator for Continuous-Time Diffusion Models**（论文 3059；Takumi Hirose）
提出 DELLBO 作为积分训练损失下降的可处理下界，导出最优更新方向，并据此提出 SGCM 在训练中调整参数更新方向；结果与理论一致，并验证对语音增强有效。

**Time-Unconditional Generative Speech Enhancement via Autonomous Rectified Flow**（论文 1679；Wen Zhang）
论证线性插值路径下目标向量场本征时不变，提出无显式时间步的网络，仅从当前状态与噪声观测的空间关系推断去噪方向。称可改善生成质量、鲁棒与推理效率。

**WaveNorm: A Low-Complexity Time-Domain Neural Adaptive Gain Control for Real-Time Speech Applications**（论文 2115；Harish Rajamani）
因果端到端从原始波形学习时变增益，满足 ITU-T P.56/P.79，约 49M MACs、55 KB 内存，适边缘实时；作预处理时可一致改善 VAD 与噪声抑制。

## 本场要点

- Flow matching 增强正把条件从浅层噪声特征转向语义、谐波与 SSL 潜空间。
- 多层“干净监督”（速度对比、表示对齐、GMM 先验匹配）是噪声输入下的关键稳定器。
- 目标域可在无干净语音时用转写—噪声对做高效微调（SwitchSE）。
- 无监督 GAN 的噪声先验是否对齐，直接决定源泄漏与过抑制。
- 连续时间扩散的梯度冲突可用理论指导的自适应更新缓解。
- 去掉显式时间条件的 rectified flow，以及超轻量神经 AGC，分别指向简化生成与边缘部署。

## 覆盖核对

- 200 | Seed-Enh: Generative Speech Enhancement in Decoupled Semantic and Timbre Spaces
- 712 | VeRe-Flow: Guiding Flow Matching toward Clean Speech via Velocity Contrastive Regularization and Representation Alignment for Noise-Robust Bandwidth Expansion
- 722 | HFMSE: Harmonic-Guided Speech Enhancement with Flow Matching
- 916 | PhASE-Flow: Phonetic-Conditioned Acoustic Flow Matching in SSL Representation Domain for Speech Enhancement
- 964 | Bridging Self-Supervised Learning and Speech Enhancement: A Wav2Vec2-Conditioned Framework
- 1259 | Text-Annotated Noisy Speech as Supervision: A Dual-Learning Framework for Target-Domain Clean-Free Speech Enhancement
- 2148 | G-MaP-SE: Guided Speech Enhancement via GMM-Based Prior Matching
- 2511 | Analysing Adversarial Priors for Data-driven Unsupervised Speech Enhancement
- 2565 | UFL-GAN: A Multi-Discriminator GAN for Unsupervised Speech Enhancement
- 3059 | Self-adaptive Gradient Conflict Mitigator for Continuous-Time Diffusion Models
- 1679 | Time-Unconditional Generative Speech Enhancement via Autonomous Rectified Flow
- 2115 | WaveNorm: A Low-Complexity Time-Domain Neural Adaptive Gain Control for Real-Time Speech Applications
