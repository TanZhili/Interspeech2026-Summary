# Spoofing and Deepfake Detection 2

- 日期：Tuesday 29 September 2026；时间：14:00-16:00；形式：Poster；Area：4；论文数：11
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场从“二分类是否够用”转向泛化、可解释、可追溯与主动防御。SSL 前端检测器仍占主导，但工作重点转向域不变/攻击特异特征解相关、任务感知剪枝蒸馏、自蒸馏预训练与证据子空间量化，以应对未见攻击与资源受限部署。

音视频联合检测强调局部伪造痕迹、参考身份锚点与物理一致性（说话距离—能量耦合），补足单纯唇同步在动态场景的脆弱性。唱歌声伪造与局部篡改则暴露“语音检测器直接迁移”的失败模式。

基准与推理框架（FakeSound2、HIR-SDD）推动 localization / traceability / generalization 与类人推理解释；自嵌入隐写则给出无训练的主动防御路径，与被动检测形成互补。

## 技术内容

### 泛化、压缩、预训练与证据解释

**Improving Generalization in Speech Deepfake Detection via Orthogonality-Constrained Common-Specific Feature Decorrelation**（论文 1483；Donghee Kim）在 SSL-AASIST 上学习域不变共性特征与攻击特异特征，并以正交正则最小化二者相关。摘要报告在未见语料（如 21DF、ASV5、ITW）上相对基线更低的 EER。

**Task-Aware Joint Pruning and Distillation for Efficient Audio Deepfake Detection**（论文 1766；Miao He）联合跨域知识蒸馏与 movement-guided 结构化剪枝，压缩至 31.9M 参数、FLOPs 降约 6.3×，多数据集平均性能相对未压缩基线仅降约 1.30%。

**ADD-DINO: A Two-Stage Self-Distillation Framework for Audio Deepfake Detection**（论文 1847；Zhaorui Sun）先在约 100 万无标注音频上做非对比师生自蒸馏（全局长段教师 vs. 噪声增强局部短段学生），再微调检测。摘要称在 ASVspoof 2019 LA 上用 20% 标注可接近全监督，并在 In-the-Wild、DFADD 及未见合成方法上改善 EER/准确率。

**FakeSound2: A Benchmark for Explainable, Traceable, and Generalizable Deepfake Sound Detection**（论文 1157；Zeyu Xie）从定位、追溯与泛化三维度评测，覆盖 6 类操纵与 12 个来源；实验显示现有模型在伪造模式识别、解释与泛化上仍不足。

**Evidence Subspace Projection: Measuring How Much Evidence Explains Deepfake Detection in Self-Supervised Speech Models**（论文 3210；Yixuan Xiao）把攻击类别、编解码、性别、传输等证据与真伪标签投影到由神经元激活构建的共享空间，用决策向量在各证据子空间的投影比值量化解释力，并在 raw / fine-tuned / post-trained 设定下验证。

**Towards Robust Speech Deepfake Detection via Human-Inspired Reasoning**（论文 1289；Dmitrii Korzh）提出 HIR-SDD，结合大音频语言模型与基于人工标注数据的思维链推理，强调对真伪归因给出可感知理由。

### 音视频、歌声与主动防御

**Physics-Aware Deepfake Detection via Distance–Speech Consistency**（论文 1541；Kyeongrae Kim）利用真实录音中语音能量随说话人—相机距离可预期变化这一声学约束；结合视频距离估计与语音距离相关声学量，并报告与唇同步检测器集成可获一致增益。

**MS-GNN: Multi-Scale Graph Neural Network for Detecting Local Audio-Visual Forgery Traces**（论文 416；Ju Zhang）将音视频流分窗建多尺度图，自下而上聚合语义、自上而下回传全局以精炼局部证据，辅以窗级与视频级监督；摘要强调对局部伪造痕迹更敏感（LAV-DF、FakeAVCeleb）。

**Referee: Reference-aware Audiovisual Deepfake Detection**（论文 1246；Hyemin Boo）用单次参考作为生物识别锚点，经身份瓶颈与匹配模块建模说话人特异线索一致性；在 FakeAVCeleb、FaceForensics++、KoDF 的跨数据集/跨语言协议上报告强结果。

**OPERA-Net: Octave-aware Phase-sensitive Enhanced Recognition Architecture for Singing Voice Deepfake Detection**（论文 3341；Fengwei Ye）用 Phase-Consistent CQT 捕捉相位异常，并以 WavLM 语义先验门控隔离人声伪造痕迹与背景音乐干扰；在 CtrSVDD、SingFake 跨语料评测中报告优于语音伪造基线的泛化。

**A Training-Free Proactive Defense Against Partial Speech Manipulation via Self-Embedding Steganography**（论文 1822；Yigitcan Özer）把干净语音的压缩自表示嵌入自身，事后提取作参考，并借助编解码式恢复支持局部 deepfake 检测；方法无需训练，作为被动防御的补充。

## 本场要点

- 泛化主线：共性—特异特征解相关、自蒸馏与证据子空间，针对未见域/攻击。
- 部署主线：任务感知剪枝蒸馏把 SSL 检测器压到可上设备规模。
- FakeSound2 / HIR-SDD 把评测从二分类推向定位、追溯、解释与类人推理。
- 音视频检测强调局部痕迹、参考身份与物理距离一致性，而非仅唇同步。
- 歌声伪造需相位敏感表征与背景音乐抑制；局部篡改适合主动隐写式自嵌入防御。

## 覆盖核对

| id | title |
|---|---|
| 1483 | Improving Generalization in Speech Deepfake Detection via Orthogonality-Constrained Common-Specific Feature Decorrelation |
| 1766 | Task-Aware Joint Pruning and Distillation for Efficient Audio Deepfake Detection |
| 1847 | ADD-DINO: A Two-Stage Self-Distillation Framework for Audio Deepfake Detection |
| 1157 | FakeSound2: A Benchmark for Explainable, Traceable, and Generalizable Deepfake Sound Detection |
| 3210 | Evidence Subspace Projection: Measuring How Much Evidence Explains Deepfake Detection in Self-Supervised Speech Models |
| 1289 | Towards Robust Speech Deepfake Detection via Human-Inspired Reasoning |
| 1541 | Physics-Aware Deepfake Detection via Distance–Speech Consistency |
| 416 | MS-GNN: Multi-Scale Graph Neural Network for Detecting Local Audio-Visual Forgery Traces |
| 1246 | Referee: Reference-aware Audiovisual Deepfake Detection |
| 3341 | OPERA-Net: Octave-aware Phase-sensitive Enhanced Recognition Architecture for Singing Voice Deepfake Detection |
| 1822 | A Training-Free Proactive Defense Against Partial Speech Manipulation via Self-Embedding Steganography |
