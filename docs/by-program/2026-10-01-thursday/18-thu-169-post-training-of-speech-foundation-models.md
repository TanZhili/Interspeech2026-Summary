# Post-Training of Speech Foundation Models

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Special Session
- Area：14
- 论文数：13
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本专题聚焦语音基础模型后训练：把通用 SSL/LLM 表征改造成任务特异、模态锚定、时间细粒度或计算高效的形式。手段包括帧级监督扰动、干预对比解耦、统一话语属性编码器、声学接地推理蒸馏、指令级偏好优化、对比音频感知蒸馏，以及文本侧 CTC 仿真与深度上扩。

安全与表示侧，混合帧后训练让 SSL 学局部伪造不一致；干预对比把纠缠空间分到内容/说话人子空间；统一框架联合学语义与说话人话语表示。音频 LLM 推理上，PolyBench 暴露复调组合推理瓶颈；Step-Audio-R1/MGRD 纠正“文本替身推理”；CAAD 把对比解码内化到学生权重以降时延。

生成与 ASR 侧，ALLM 细粒度反馈做 TTA 指令遵循 DPO；LLM 语义先验蒸馏进仅编码器多说话人 ASR；TASU2 可控 WER 的 CTC 仿真服务低资源对齐；深度上扩插入层保文本能力；知识定位编辑与音频侧时间提示强化事实与时序感知；交错堆叠加速蒸馏部署。

## 技术内容

### 监督/干预后训练与话语级多属性表示

**Supervised Post-training of Speech Foundation Models for Robust Adaptation in Speech Deepfake Detection**（论文 908；Zihan Pan）  
混合帧后训练制造局部伪造扰动，帧级监督促使 SSL 学局部不一致。ASVspoof5 单模型无增强 EER 4.50%（摘要称 SOTA）；ASVspoof2021 LA/DF 绝对 EER 差仅 0.16%。

**Learning task-specific subspaces via interventional post-training of speech foundation models**（论文 2542；Jack Cox）  
干预对比学习将基础模型纠缠表示变换为分离的内容与说话人子空间；说话人验证与关键词检出上改善域外验证，并显示信息跨子空间分离。

**Learning Multiple Utterance-Level Attribute Representations with a Unified Speech Encoder**（论文 3350；Maryem Bouziane）  
扩展 SAMU-XLSR/SONAR 式话语级对齐，统一后训练使单一编码器产出多种话语属性表示；联合学语义与说话人表示，并在多语检索与说话人识别上验证。

### 音频 LLM 推理、指令遵循与高效蒸馏

**PolyBench: A Benchmark for Compositional Reasoning in Polyphonic Audio**（论文 2466；Yang Xiao）  
复调音频组合推理基准含计数、分类、检测、并发与时长五子集。SOTA LALM 在复调上一致退化，暴露瓶颈。（注：与 Area 7 同名 PolyBench 主题不同。）

**Step-Audio-R1: Why Audio LLMs Fail at Reasoning — The Trap of Textual Surrogates**（论文 256；Xiangyu Zhang）  
将失败归因于文本替身推理；MGRD 经自蒸馏与多模态 RL 转向声学属性。跨语音/环境声/音乐基准优于 Gemini 2.5 Pro、可比 Gemini 3 Pro；声学接地可扭转“更长审议更差”现象。

**Improving Text-to-Audio Instruction Following via Fine-Grained Feedback from Audio-Aware Large Language Models**（论文 1111；Chun-Yi Kuan）  
ALLM 作细粒度裁判验证事件存在与时序关系，经人类核验后构偏好对做 DPO；提出叙事基准 S3Bench。提升事件完整性、时序与联合指令遵循且保持音质。

**CAAD: Contrastive Audio-Aware Distillation for Efficient Speech Language Models**（论文 645；Chun Wei Chen）  
将教师对比推理内化到学生权重；同步 teacher-forcing 与统一伪真值实现全序列对比分布蒸馏。Dynamic-SUPERB 相对标准蒸馏约 8% 相对增益，并降低 MCR-BENCH 语言偏置。

### ASR/对齐适应、知识编辑、时间感知与蒸馏加速

**Distilling LLM Semantic Priors into Encoder-Only Multi-Talker ASR with Talker-Count Routing**（论文 612；Hao Shi）  
训练时蒸馏适配 LLM 的多说话人语义指导，推理保留 CTC 式解码；后编码器分离 + 序列化 CTC，Talker-Count Head 动态选分支。LibriMix 两说话人可比 LLM 系统，三说话人显著提升且 RTF 很小。

**TASU2: Controllable CTC Simulation for Alignment and Low-Resource Adaptation of Speech LLMs**（论文 866；Jing Peng）  
在指定 WER 范围仿真 CTC 后验，使纯文本监督难度可控、无需 TTS。多源到目标适应上优于 TASU、纯文本微调与 TTS 增强，并缓解源域退化。

**Adapting Text LLMs to Speech via Multimodal Depth Up-Scaling**（论文 2099；Kazuki Yano）  
冻结文本 LLM，仅训练插入的新 Transformer/E-Branchformer 层。SmolLM2 在 48k 小时英语 ASR 上达可比全微调 ASR，文本退化远小于全微调与 LoRA；E-Branchformer 变体可匹配/超越大模型全微调 ASR，文本退化降超 75%、可训参数少 60%。

**Localizing and Editing Knowledge in Large Audio-Language Models**（论文 2066；Jiaheng Dong）  
首个 LALM 知识定位与编辑音频基准；语音感知因果追踪定位支撑事实检索的层再编辑。事实知识联合编码于音频编码器与语言骨干；音频侧编辑优于文本编辑或微调。

**Towards Fine-Grained Temporal Perception: Post-Training Large Audio-Language Models with Audio-Side Time Prompt**（论文 745；Yanfeng Shi）  
将时间戳嵌入交织进音频特征作时间坐标提示，SFT 后接 RL 优化时间对齐（TimePro-RL）。在音频定位、声音事件检测与稠密音频描述等任务显著提升。

**Fast Speech Foundation Model Distillation Using Interleaved Stacking**（论文 3071；Eungbeom Kim）  
交错堆叠在加深过程中保持层位置，避免既有堆叠伤性能；对依赖层特异知识的 SFM 尤为关键。SUPERB 上验证加速蒸馏部署有效。

## 本场要点

- 帧级伪造扰动与干预对比把通用 SSL 改造成防伪或解耦子空间。
- 音频 LLM 需声学接地推理与指令级 ALLM 反馈，而非文本替身或全局相似度。
- 对比蒸馏内化、深度上扩与可控 CTC 仿真分别服务效率、保文本能力与低资源对齐。
- 知识编辑与音频侧时间提示拓展事实与细粒度时序控制；交错堆叠加速学生训练。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 908 | Supervised Post-training of Speech Foundation Models for Robust Adaptation in Speech Deepfake Detection |
| 2542 | Learning task-specific subspaces via interventional post-training of speech foundation models |
| 3350 | Learning Multiple Utterance-Level Attribute Representations with a Unified Speech Encoder |
| 2466 | PolyBench: A Benchmark for Compositional Reasoning in Polyphonic Audio |
| 256 | Step-Audio-R1: Why Audio LLMs Fail at Reasoning — The Trap of Textual Surrogates |
| 1111 | Improving Text-to-Audio Instruction Following via Fine-Grained Feedback from Audio-Aware Large Language Models |
| 645 | CAAD: Contrastive Audio-Aware Distillation for Efficient Speech Language Models |
| 612 | Distilling LLM Semantic Priors into Encoder-Only Multi-Talker ASR with Talker-Count Routing |
| 866 | TASU2: Controllable CTC Simulation for Alignment and Low-Resource Adaptation of Speech LLMs |
| 2099 | Adapting Text LLMs to Speech via Multimodal Depth Up-Scaling |
| 2066 | Localizing and Editing Knowledge in Large Audio-Language Models |
| 745 | Towards Fine-Grained Temporal Perception: Post-Training Large Audio-Language Models with Audio-Side Time Prompt |
| 3071 | Fast Speech Foundation Model Distillation Using Interleaved Stacking |
