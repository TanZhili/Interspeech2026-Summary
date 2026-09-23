# Target Speaker Extraction, Speech Separation and Audio Understanding

- 日期：2026年9月29日（周二）
- 时间：09:00-11:00
- 形式：Poster
- Area：6
- 论文数：9
- 材料说明：依据官方节目单与 ISCA 条目中的标题、作者、报告人、时间与摘要撰写；不补写摘要未给出的数字、数据集或方法细节。

## 技术趋势

本场主线是目标说话人提取（TSE）与分离在“线索多样化、场景真实化、生成式增强”上的扩展。单声道分离侧，时频 Transformer 通过内容感知滑窗注意力联合建模局部与全局；生成式路径则把说话人日记化与潜空间 flow matching 结合，并以对抗说话人引导缓解说话人混淆。线索侧从传统注册音、DOA 扩展到唤醒词注册、HRTF 空间先验、耳 EEG 神经引导，以及唇动语义 token、多视角唇部与波束域声噪交互。

音视频 TSE 强调超越正面唇同步：有工作把唇动先变为粗粒度语义 token 再引导提取，也有用多视角张量融合在训练期学习跨视角相关、推理期支持单/多视角；多通道方案则结合掩码波束形成与跨波束注意力，在真实录音与远场仿真上报告 WER 改善。与此同时，通用音频理解编码器 USAD 2.0 通过域感知蒸馏、音乐域覆盖与深度扩展到十亿参数，服务于下游探测与音频 LLM。

整体上，本场从“谁说话”的线索工程走向空间、视觉与神经多线索，并在判别式分离与生成式高保真之间形成互补；交互场景则关注无预注册、短噪唤醒词等可用性瓶颈，辅以 LLM-TTS 注册增强。

## 技术内容

### 时频分离、生成式分离与通用音频编码器

**TF-MossFormer: Integrating Convolution Gated Local-Global Attentions for Enhanced Time-Frequency Domain Monaural Speech Separation**（论文 218；Shengkui Zhao）提出结合局部与全局注意力的时频 Transformer，以内容感知滑窗注意力动态调整感受野，并在注意力层间加入卷积门控。摘要报告在 WSJ0-2Mix 上，参数量 5.9M/16.9M/25.4M 时 SI-SDRi 分别为 22.6、24.0、24.4 dB。

**Latent Flow Matching Based Speech Separation Using Speaker Diarization**（论文 1401；Sharon Gannot）将说话人日记化表示与潜空间 Flow Matching 结合，仅需训练潜空间生成式 U-Net；并提出 Adversarial Speaker Guidance（ASG），以混合信号导出的说话人吸引子替代传统注册音，缓解说话人混淆并提升可懂度相关表现。

**USAD 2.0: Scaling Representation Distillation for Universal Audio Understanding**（论文 1296；Heng-Jui Chang）融合 SSL 与有监督基础模型知识，引入域感知蒸馏以应对教师不匹配，扩展音乐域并加入二阶段有监督蒸馏；通过深度扩展将模型扩至约十亿参数，并在探测与基于 LLM 的评测中报告强或当时最优表现。

### 注册、空间与神经引导的目标说话人提取

**Enroll-on-Wakeup: A First Comparative Study of Target Speech Extraction for Seamless Interaction in Real Noisy Human-Machine Dialogue Scenarios**（论文 259；Yiming Yang）提出 Enroll-on-Wakeup，将人机交互中自然捕获的唤醒词段作为注册参考，系统比较判别式与生成式 TSE；针对短噪唤醒词研究 LLM-TTS 注册增强，报告现有 TSE 在 EoW 设定性能下降，TTS 辅助可改善听感但仍存在识别精度差距。

**HRTF-guided Binaural Target Speaker Extraction with Real-World Validation**（论文 807；Yoav Ellinson）以听者 HRTF 为显式空间先验做双耳 TSE，基于多通道深度盲源分离骨干并在多样实测 HRTF 上训练以跨听者泛化；在仿真与混响环境 HATS 真实录音上验证，强调相对 DOA/注册方法更利于保留双耳线索。

**NeuroMultiSpEx: Neuro-Guided Target Speaker Extraction for Multi-Speaker Scenarios**（论文 1120；Siqi Cai）面向 4 说话人场景，用可穿戴耳 EEG 融合包络同步（when）与说话人身份（who）两类神经线索，经门控融合端到端训练；摘要称在耳 EEG 数据上显著优于对比系统，并定位为可穿戴耳 EEG 多说话人神经引导提取的首项研究。

### 视觉与波束域音视频目标说话人提取

**TGTSE: Token-Guided Target Speaker Extraction with Visual Cue**（论文 1710；Zhong-Qiu Wang）先从目标唇动提取粗粒度语义 token，再将其作为时间对齐语义线索引导 AVTSE；在 VoxCeleb2-2Mix 与 LRS2-2Mix 上相对常规 AVTSE 持续更优。

**Multi-View Based Audio Visual Target Speaker Extraction**（论文 2035；Peijun Yang）提出 Multi-View Tensor Fusion（MVTF），训练期用同步多视角唇视频经成对外积建模跨视角乘性交互，推理支持单/多视角；摘要称单视角亦可受益于多视角知识，多视角模式进一步提升鲁棒性。

**AV-SNINet: A multi-channel audio-visual speech-noise interaction network for Target Speaker Extraction with cross-beam attention**（论文 3227；Yanhui Tu）第一阶段用 AV-DPCRN 引导的 GEVD 波束形成得到目标/干扰波束，第二阶段双分支交互估计语音与噪声掩码，并以跨波束注意力建模帧级互斥抑制。摘要报告真实录音集相对第一阶段基线平均 WER 从 28.40% 降至 20.38%（相对降幅 28.23%），远场 LRS2 仿真平均 WER 为 17.20%。

## 本场要点

- 单声道分离并行推进局部—全局时频注意力（TF-MossFormer）与日记化条件潜空间 flow matching。
- TSE 线索从预录注册扩展到唤醒词、HRTF、耳 EEG，以及唇动 token / 多视角 / 波束域交互。
- 生成式与对抗说话人引导用于缓解混淆并追求感知质量；USAD 2.0 服务通用音频理解与音频 LLM。
- 真实交互与真实录音评测（EoW、HATS、自建真实集）成为重要议程。
- 音视频方法不再局限于正面唇同步，强调语义 token、多视角迁移与波束域声噪建模。
- 摘要给出的 SI-SDRi、WER 等数字仅转述官方摘要。

## 覆盖核对

| paper_id | title |
|---|---|
| 218 | TF-MossFormer: Integrating Convolution Gated Local-Global Attentions for Enhanced Time-Frequency Domain Monaural Speech Separation |
| 259 | Enroll-on-Wakeup: A First Comparative Study of Target Speech Extraction for Seamless Interaction in Real Noisy Human-Machine Dialogue Scenarios |
| 807 | HRTF-guided Binaural Target Speaker Extraction with Real-World Validation |
| 1120 | NeuroMultiSpEx: Neuro-Guided Target Speaker Extraction for Multi-Speaker Scenarios |
| 1296 | USAD 2.0: Scaling Representation Distillation for Universal Audio Understanding |
| 1401 | Latent Flow Matching Based Speech Separation Using Speaker Diarization |
| 1710 | TGTSE: Token-Guided Target Speaker Extraction with Visual Cue |
| 2035 | Multi-View Based Audio Visual Target Speaker Extraction |
| 3227 | AV-SNINet: A multi-channel audio-visual speech-noise interaction network for Target Speaker Extraction with cross-beam attention |
