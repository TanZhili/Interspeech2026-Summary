# 语音合成、声音转换与歌唱生成

> Interspeech 2026 主题综述（依据 `topics_assigned.json` 中 **tts / voice-conversion / singing / generation** 相关会场摘要整理）。
>
> 会程：<https://interspeech2026.org/en-AU/pages/program/program>  
> ISCA Archive：<https://www.isca-archive.org/interspeech_2026/index.html>  
> 本文仅依据上述 JSON 中的摘要表述技术内容，不补充摘要未给出的数字或方法细节。

## 技术趋势

本届与语音合成、声音转换、歌唱与音频生成相关的工作，不再把“能听懂、像某人”当作唯一目标，而是沿着可扩展条件、生成范式、可控韵律、长音频与低延迟部署、低资源前端，以及评测可信度几条轴线并行推进；声音转换与歌唱/音乐生成则把同一套离散表示、流匹配与扩散工具迁移到音色解耦、旋律保持与多轨音频编辑场景。

### 零样本与规模化

零样本克隆与跨语覆盖仍是主线：从短参考或脸像等非语音身份线索推断说话人，到面向数百种语言的大规模多语零样本系统，共同依赖开源整理的大规模多语语音与更稳的离散声学建模。与此同时，规模化也带来效率压力——自回归解码的注意力与 KV cache 随长度二次增长，促使窗口注意力、蒸馏与测试时自适应等方法，在保持音质的前提下降低内存与非常见风格失败率。合成数据增强个性化微调时，还需用域条件等方式抑制“真伪混训”造成的说话人相似度下滑。

### 流匹配、扩散与 LLM-TTS

生成骨干明显三分：连续/离散流匹配（含对开源 FM 模型的在线强化学习）、扩散式离散语言模型或 DiT，以及基于 codec token 的自回归/LLM 式 TTS。离散流匹配试图在连续空间优化难度与自回归高延迟之间取折中；FM 路线上出现把 ODE 轨迹转为可采样 SDE、再配合多目标奖励的后训练；LLM/AR 路线则更强调韵律动态预测、指令跟随与前缀/前缀式测试时优化。声码器与潜空间一侧，对抗训练目标、语义对齐 VAE 与一步 Token2Wav 等，服务于“表征更紧、解码更快”的共同需求。

### 可控与情感韵律

控制粒度从全局风格（口音强度、情感、印象向量）下沉到词级/音素级的重音、力度、音高—响度—时长，以及指令文本中的细粒度属性。技术路径常见为：显式控制编码器 + 偏好对齐（DPO/GRPO）+ 韵律工具或感知奖励；以及内容—风格/韵律残差解耦（信息瓶颈、脸声对齐、伪标签）。情感与口音纠缠、指令改写语义漂移等问题被单独拿出，说明“可控”已进入需要诊断与数据治理的阶段，而不只是再加一个条件嵌入。

### 长文本与篇章级合成

长音频关注点从单句 MOS 转向篇章一致性：跨句块状态与历史文本编码、软对齐先验、潜空间压缩以支撑分钟级对话单次生成，以及面向有声书/叙事的上下文情感控制与多智能体闭环修正。评测侧也开始用韵律—音段解离分析指出：整体指标可能掩盖 F0 协调与元音空间等结构性偏差。

### 流式与低延迟

流式不仅出现在 TTS，也出现在听端语音转换与风格转换：非自回归 + 强解耦以换取秒级端到端延迟；电话域增强与多教师蒸馏应对信道损伤；窗口注意力与一步潜空间解码则针对 AR/多步扩散的逐步时延。低延迟与零样本质量仍是成对约束，摘要中多以恒定逐步延迟、峰值显存或 RTF 作为对照维度。

### 低资源与文本前端

低资源议程同时包含综述判断与系统实证：跨语迁移、无配对/无监督单元与基础模型降低对转写语音的依赖，但真正低资源语言仍受语言多样性、质量与可靠评测制约。实证工作覆盖印度诸语、埃塞俄比亚语、曼尼普尔拉丁字母部族语等，常见路径是从高资源 FM/SSL 检查点适配、质控过滤的克隆数据微调，以及 IPA/罗马化/规则 G2P 等前端统一。文本前端专场强调词典增强 G2P、多语罗马化编码、语域可听性、话语条件重音基准与口语化改写，把“读对字”重新放到合成链路前端。

### 评测

评测会场密集，问题意识很明确：主观贵且难复现，客观指标易饱和；需要迭代再合成放大系统差距、成对偏好排行榜、情境/域适宜性、非语言发声与口音—情感诊断等协议。偏见与社会属性提示、印象控制误差、以及指令 TTS 中改写漂移的量化，表明评测对象已从“好不好听”扩展到“是否可控、是否可信、是否适合场景”。

### 声音转换

声音转换与 TTS 共享流匹配/扩散与解耦工具，但任务重心在内容—音色—风格分离、流式听端部署、设计化/非人嗓音资源，以及词级嗓音质量编辑。退化鲁棒与实时切换成为演示与系统论文的共同卖点。

### 歌唱与音乐/音频生成

歌唱侧覆盖歌词编辑、歌声转换与美化、说话人克隆歌曲与伴奏共生成、地方戏曲基准与歌唱深度伪造语料；音乐/音频侧则从文本到音乐、视频到可编辑分轨音频、综艺音效智能体，延伸到音频基础模型与生成会场中的指令遵循与层级精炼。控制、主体性与评测（含特邀综述）被明确为“越过纯 text-to-music”后的下一议题。

## 技术内容

下列按会场（日期、时段、标题）列出全部论文；每篇为 **标题**（论文 id；presenter），其后 1–3 句据摘要改写。


### 周一（9月28日） 11:00-13:00｜Scaling and Zero-Shot Speech Synthesis（Oral；topic: tts）

**Learning to Rescale: On-the-Fly Sequence Length Adaptation in Non-Autoregressive Speech Synthesis**（1069；Jiawei Jin）  
提出可变长度非自回归 TTS 模型 ElasticDLM，通过功能 token、DLTS 训练与 HCGI 推理减轻对精确时长预测的依赖，可从任意长度输入生成高保真自然语音。

**OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models**（3256；Han Zhu）  
OmniVoice 是面向 600 余种语言的大规模多语零样本 TTS，采用扩散语言模型式离散非自回归架构，直接将文本映射到多码本声学 token；在开源整理的 581k 小时多语数据上训练，并在中英及多语基准上取得领先表现。

**WAND: Windowed Attention and Knowledge Distillation for Efficient Autoregressive Text-to-Speech Models**（943；Hanna Lee）  
WAND 将预训练自回归 TTS 改造为常量计算与内存复杂度：对条件 token 保持全局注意力、对生成 token 使用滑动窗口，并以课程学习收紧窗口、用全注意力教师蒸馏恢复音质；在三种 AR-TTS 上最高可降低约 66.2% KV cache，且逐步延迟近乎恒定。

**VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation**（1757；Li Liu）  
VoiceTTA 是面向预训练零样本 TTS 的强化学习测试时自适应方法，用 F0/能量变异系数风格奖励、说话人相似度与 Whisper WER，经 GRPO 优化可学习前缀，显著改善相声、方言等非常见风格模仿。

**ZeSTA: Zero-Shot TTS Augmentation with Domain-Conditioned Training for Data-Efficient Personalized Speech Synthesis**（1269；Youngwon Choi）  
ZeSTA 将零样本 TTS 合成语音用于低资源个性化合成增强，以轻量域嵌入区分真实与合成语音并结合真实数据过采样，在不改动基座结构的前提下，于 LibriTTS 与内部数据上提升说话人相似度并保持可懂度与感知质量。

**Dual-Space Constrained Face-Based Zero-Shot Text-to-Speech Synthesis**（409；Ju Zhang）  
DSC-TTS 在声学模型训练阶段同时在说话人嵌入空间与脸声对齐共享身份空间施加约束，缓解模块化脸基零样本 TTS 推理时引入脸特征导致的身份漂移，提升说话人相似度与身份一致性。


### 周一（9月28日） 11:00-13:00｜Long-Form Speech Synthesis（Poster；topic: tts）

**audiobook-cc: Controllable Long-context Speech Generation for Multicast Audiobook**（2125；Min Liu）  
面向多播有声书提出上下文感知、情感可控长上下文合成框架，含上下文一致性机制、风格与提示解耦及自蒸馏；章节级生成达 4.25 M-MOS（相对最强基线约 14%），对话 4.11 S-MOS，高强度情感判别提升 31 个百分点。

**MagpieTTS-LF: Inference-Time Long-Form Speech Generation Without Training on Long-Form data**（1461；Jing Yao Li）  
MagpieTTS-LF 在推理阶段使 MagpieTTS 无需长文本重训即可生成连贯长语音，引入软注意力先验、跨句块状态推理与历史感知文本编码，改善长程可懂度、韵律连贯、说话人一致与边界自然度。

**AuDirector: A Self-Reflective Closed-Loop Framework for Immersive Audio Storytelling**（1180；Wen Wu）  
AuDirector 是用于沉浸式音频叙事的自反思闭环多智能体框架，经身份感知前期制作、协作合成与缺陷音频闭环修正，以及自然语言反馈交互改稿，在结构连贯、情感表达与声学保真上优于既有基线。

**Designed Vocalizations Dataset: Sound-Designed Human and Animal Voices for Non-human Voice Conversion**（932；Seolhee Lee）  
提出 Designed Vocalizations Dataset，对语音与动物发声等原始素材施加专业效果得到设计化嗓音变体，并提供按音色组与预设风格划分的 seen/unseen 测试集及基线结果，面向非人声转换研究。

**ZipL-Dialog: Memory-Efficient Long-Form Spoken Dialog Synthesis via Latent Flow Matching**（185；Jihwan Kim）  
ZipL-Dialog 将条件流匹配移至 4 倍时域压缩（25 Hz）潜空间，配合确定性 mel 自编码器与 ZipFormer 下采样调度，相对基线峰值 GPU 显存降低 11.22 倍、推理加速 2.23 倍，支持单次多分钟对话合成并保持感知自然度。

**Not Flat, But Dissociated: Prosodic and Segmental Divergence in Neural TTS**（2730；Rong Wang）  
在 13,100 条匹配 LJ-TTS 上分析四种神经 TTS，发现全局 F0 变异被压缩而局部音高反转增多，元音空间缩至人类基线的 9–30%，韵律与音段偏差基本不相关，说明标准整体指标混淆了不同质量维度。

**Refining Emphasis Control in Flow-Matching TTS via Preference Alignment and Reinforcement Learning**（2284；Jiangnan Ye）  
在 F5-TTS 上增加 Emphasis Encoder，经人工标注 SFT、基于 WPT 排序的 DPO，以及适配 Flow-CPS 的在线强化学习三阶段优化，增强重音强度与可控性并保持自然韵律。

**CraftTTS: Fine-Grained Prosody Control for Text-to-Speech**（2018；Qihang Lu）  
CraftTTS 以三阶段实现稳定词级韵律控制：自动构建偏好对、联合 SFT 与 DPO，以及多维韵律奖励的 GRPO，在保持零样本能力的同时提升细粒度表现力。

**Dynamic Prosody Prediction in LLM-based TTS for Improving Speaker Similarity**（2312；Zhenwei Mou）  
针对 LLM 基 TTS 忽视风格相关韵律、限制说话人相似度的问题，提出基于已生成语音条件预测当前音节韵律的动态韵律预测，在三个数据集上提升韵律学习与说话人相似度。


### 周一（9月28日） 14:30-16:30｜Text-to-Speech Synthesis（Long Oral；topic: tts）

**FlowTTS-GRPO: Online Reinforcement Learning with Multi-Objective Reward Optimization for Flow-Matching Based Text-to-Speech**（1102；Haoxu Wang）  
FlowTTS-GRPO 将 ODE 轨迹转为 SDE 路径，对开源流匹配 TTS 做无需辅助模型的在线多目标强化学习微调；在 CosyVoice 3.0 与 F5-TTS 上提升说话人相似度与感知质量，F5-TTS 可懂度亦有改善。

**DiFlow-TTS: Compact and Low-Latency Zero-Shot Text-to-Speech with Discrete Flow Matching**（1043；Son Nguyen）  
DiFlow-TTS 基于离散流匹配，由确定性 Phoneme-Content Mapper 与同时生成韵律与声学 token 流的 Factorized Discrete Flow Denoiser 组成，在多项指标上验证零样本 TTS 的紧凑低延迟生成效果。

**RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis**（646；Yongjoon Lee）  
RAF 为 GAN 声码器提出相对论对抗反馈目标，借助语音自监督模型辅助判别并以相对论配对建模分布；多数据集上提升主客观指标，且仅用 12% 参数的 RAF 训练 BigVGAN-base 在感知质量上优于 LSGAN 训练的 BigVGAN。

**Iterate to Differentiate: Enhancing Discriminability and Reliability in Zero-Shot TTS Evaluation**（2414；Shengfan Shen）  
I2D 通过将模型先前合成结果迭代作为参考再合成，利用强弱系统衰减差异放大区分度；聚合迭代客观指标后，UTMOSv2 系统级 SRCC 由 0.118 提升至 0.464，在 11 个模型与中英及情感数据上更可靠评估零样本 TTS。

**Improving Text-to-Audio Instruction Following via Fine-Grained Feedback from Audio-Aware Large Language Models**（1111；Chun-Yi Kuan）  
利用音频感知大语言模型作细粒度评判，核验生成音频中目标事件与时序关系，并据此构建偏好对做 DPO；同时提出叙事基准 S3Bench，提升多事件时序指令遵循并保持音频质量。

**StyleStream: Real-Time Zero-Shot Voice Style Conversion**（404；Yisi Liu）  
StyleStream 是可流式零样本语音风格转换系统，由去风格化 Destylizer 与基于参考再注入风格的 DiT Stylizer 组成，经文本监督与强信息瓶颈实现内容-风格解耦，端到端延迟约 1 秒。


### 周一（9月28日） 14:30-16:30｜Speech Synthesis, Voice Conversion and Audio Generation（Show And Tell；topic: tts）

**Coco-VC: Degradation-Robust Streaming Voice Conversion System on the Listener Side**（3571；Ryo Kato）  
听端实时流式转换系统 Coco-VC 结合电话数据增强与多教师蒸馏提取鲁棒表示，在标准笔记本上低延迟演示，对受损电话语音相对现有流式 VC 仍保持较高质量。

**Listening to Motion in Space: Vision-Grounded Event-wise Video-to-Audio Generation and Rendering**（3574；Dayeon Ku）  
VisionSFX 是无需训练的视觉 grounding 视频到音频流程：用视觉语言模型分解声事件，分别生成各事件与环境音并事后双耳空间化渲染，支持按源编辑、重定位与提示改写。

**Automatic generation of audio comic from manga images**（3577；Sota Koshino）  
介绍从漫画图像（半）自动生成配音音频漫画的系统处理流水线，并报告对生成结果的客观与主观评价。

**Programmable Speech Synthesis without Computers**（3578；Takayuki Arai）  
展示基于人类声道动态物理模型的机械语音合成装置，主声道由六块滑块控制，并以可更换凸轮轮廓板实现可编程短语合成。

**VoiceQualityGUI: A Tool for Word-Level Voice Quality Modifications**（3579；Harm Lameris）  
VoiceQualityGUI 基于改进的 VoiceQualityVC，支持在词级调节吱嘎、气声与鼻音等嗓音质量，便于探索局部调制对会话语用感知的影响。

**DsNA(Digital sigNature for Audios): A Unique Method to Fingerprint Audio Files Generated by Text to Speech**（3590；Vishal Gourav）  
DsNA 在 TTS 生成后将由音频与元数据派生的密码学签名分片并与分块音频交错嵌入，作为轻量事后指纹；初步评估显示原音频与加指纹音频 SNR 无明显下降。

**Two Lessons Learned from the SGILE project: Efficient Building and Evaluation of TTS Voices**（3596；Korin Richmond）  
展示 SGILE 项目两项成果：开源 EveryVoice TTS Toolkit 可在低资源音频量下建声，以及尽量减少听者负担的评测方法；演示以网页整合试听与少见听力测试设计。

**Scalable Audio Scene Generation with the Treble SDK**（3609；Georg Götz）  
Treble SDK 的 Scene Generator 以轻量配方表示从房间声学仿真与干净音源构建可交互音频场景，按需渲染，支持手工设计与批量随机生成多说话人会话场景。


### 周二（9月29日） 09:00-11:00｜Controllable and Expressive Speech Synthesis（Oral；topic: tts）

**Learnable Classifier-Free Guidance Null Embeddings for Enhanced Controllable Speech Synthesis**（803；Biel Tura-Vecino）  
提出用可学习无条件嵌入替代 CFG 中固定空向量，并可为各条件模态学习独立无条件嵌入；在说话人相似度、稳定性与表现力上优于固定空嵌入，且对较大引导尺度更稳健。

**Synthesizing the Lombard Effect: Multi-Level Control of Speech Clarity and Vocal Effort in TTS**（1159；Seymanur Akti）  
基于流匹配的 TTS 以发声力度与清晰度伪标签训练，实现连续解耦的力度与发音控制及词级强调，可改善清晰度相关声学特征，并在噪声中模拟人类清晰语的可懂度增益。

**CrossAccent-TTS: Cross-Lingual Accent-Intensity Controllable Text-to-Speech via Disentangled Speaker and Accent Representations**（1744；Nirmesh J. Shah）  
CrossAccent-TTS 通过 Accent Intensity Controller 向口音子空间注入加权语言嵌入，实现口音强度插值与细粒度控制，在 Indic Multilingual 与 L2-arctic 上提升口音相似度与可控性并保持说话人相似度与自然度。

**CtrlSpeech: Coarse-to-Fine Control for Expressive Speech Synthesis**（1760；David Harwath）  
CTRLsPEECH 基于 DiTAR，结合全局说话人条件与音素对齐的音高、响度、时长信号，在保持目标音色下实现词/音素级粗到细表现力控制，零样本性能具竞争力且可控性提升。

**ProsoCodec: Prosody-Oriented Speech Codec for Voice Conversion**（2146；Jeongsoo Choi）  
ProsoCodec 将韵律建模为条件残差：编码器解码器以文本与说话人嵌入为前缀条件，使离散瓶颈捕获内容与说话人无法解释的韵律变化，并在同说话人对与低频 mel 监督下改善转换中的韵律保持、降低源音色泄漏。

**LibriTTS-VI: A Public Corpus and Novel Methods for Efficient Voice Impression Control**（2231；Junki Ohmura）  
发布基于 LibriTTSR 的公开印象控制语料 LibriTTS-VI，并提出双参考解耦训练与无参考数值印象控制，使 11 维印象均方误差客观由 0.61 降至 0.41、主观由 1.15 降至 0.92。


### 周二（9月29日） 09:00-11:00｜Singing Voice and Music Generation（Poster；topic: singing）

**MeloDISinger: Melody-Aware & Duration-Preserving Singing Voice Editing with Audio Infilling**（3285；Yoonjeong Park）  
MeloDISinger 以流匹配歌唱编辑模型 MeloDRP 预测固定预算时长比并融合伪 MIDI 旋律上下文，用流匹配 mel 解码器做音频填充，在保持旋律、总时长与未编辑区的同时实现歌词修订，主客观达领先水平。

**SingFox: A Multi-Lingual Singfake Detection Corpus**（2573；Arth J. Shah）  
SingFox 是面向歌唱深度伪造检测与溯源的大规模语料，含 T1–T6 六轨、20 种语言、超 1,13,802 条片段、逾 126.32 小时与 1150 种歌手；跨数据集交叉测试最高准确率 77.84%。

**Singing Voice Conversion via Shared Speaker Space and Min-Pooling Adversarially Enhanced Flow Matching**（2090；Hao Huang）  
MinFlow-SVC 用 KNN 将源歌手特征映射到共享歌手空间以去除音色，并以最小池化对抗训练校正不一致、增强带谐波感知的条件流匹配，在自然度、可懂度、音色相似度与演唱稳定性上优于现有 SVC 基线。

**YingMusic-Singer: Controllable Singing Voice Synthesis with Flexible Lyric Manipulation and Annotation-free Melody Guidance**（1547；Chunbo Hao）  
YingMusic-Singer 为全扩散歌唱合成模型，可选音色参考、旋律片段与修改歌词无需人工对齐即可控旋律改词；经课程学习与 GRPO，旋律保持与歌词遵循优于 Vevo2，并发布 LyricEditBench。

**CTMusic: A Traditional Chinese Instrumental Music Dataset Towards Text-to-Music Generation**（882；Haotian Guo）  
CTMusic 含 741 对精标文本-音乐与逾 42 小时传统中国器乐音频，用于文本到音乐；在其上微调 Stable Audio Open 并给出更贴合中国传统音乐的改进模型。

**SRF-SVB: Style-Consistent Singing Voice Beautifying via Rectified Flow**（615；Wenhui Li）  
SRF-SVB 以整流流实现风格一致的歌声美化，覆盖音高与节奏校正，并用上下文引导的掩码 mel 填充保留业余歌手音色与表达模式，在英中测试集多数主客观指标上优于基线。

**Towards Unified Song Generation and Singing Voice Conversion with Accompaniment Co-Generation**（481；Ziyu Zhang）  
UniSinger 首次端到端统一说话人克隆歌曲生成与伴奏共生成 SVC，基于多模态扩散 Transformer 构建统一说话人嵌入空间，并以任务模态掩码课程学习缓解多任务冲突，两任务均达领先并形成互补。

**Towards Chinese Yue Opera Singing Voice Synthesis: A Benchmark with Dataset, Data Augmentation and Baseline Model**（131；Peng Bai）  
建立粤剧（吴方言）歌声合成首个综合基准：YOAT 语料含 565 条工作室录音与音素级对齐、面向发音与音高的数据增强，以及条件流匹配基线 YueOpera-Singer（主观 MOS 3.92）。

**Back to Ear: Perceptually Driven High Fidelity Music Reconstruction**（219；Kangdi Wang）  
ear-VAE 以 K 加权感知滤波、相位感知相关损失与分组件幅度/相位谱监督优化音乐重建 VAE，在多项指标上明显优于主流开源模型，尤其高频谐波与空间特性。


### 周二（9月29日） 14:00-16:00｜Low-Resource Speech Synthesis（Oral；topic: tts）

**Low-Resource Speech Synthesis: What Have We Solved, and What Remains?**（特邀；Sakriani Sakti）  
综述演讲梳理低资源语音合成进展：多语跨语迁移、无配对数据、无监督单元发现与基础模型大幅降低对转写语音的需求；并讨论真正低资源语言在语言多样性、合成质量与可靠评测上的剩余挑战，以及与濒危语言社区需求的衔接。

**Lightweight Cross-Lingual Speaker Adaptation for Indic TTS**（2050；Tarun Kumar）  
提出仅需 10 秒参考的轻量说话人自适应管线：用四阶段质控过滤克隆合成语音微调 FastSpeech2，经 CLS 音素统一可在印地、马拉地、泰米尔、泰卢固跨语合成，较基线快 53 倍并改善可懂度与自然度。

**Scalable Neural TTS for Latin-Script Low-Resource Languages of Manipur**（2304；Hoomexsun Pangsatabam）  
为曼尼普尔拉丁字母低资源语 Tangkhul（9.58 小时）与 Maring（10.79 小时）构建工作室朗读语料与预处理管线，并用 Tacotron 2、FastSpeech 2 训练单语字符级 TTS，经主客观评测支持后续开发。

**High-Quality Speech Synthesis for Under-Resourced Ethiopian Languages**（2658；Rahel Mekonen Tamiru）  
用 SpeechT5 为阿姆哈拉语与阿方奥罗莫语构建高质量 TTS：每语约 100 小时工作室数据，阿姆哈拉因叠音等复杂性扩展至 113 小时；主观 MOS 分别为 4.65 与 4.43。

**IN-F5: Adapting an English TTS Foundation Model for Multilingual and Zero-Resource Indian Speech Synthesis**（3366；Praveen Srinivasa Varadhan）  
从英语预训练 F5-TTS 以不足原预训练规模 2% 的数据适配 11 种印度语言得到 IN-F5；对照显示仅在印度数据上直接微调效果最好，并展现多语转写、语码混合与表现力控制及对 Bhojpuri、Tulu 的零资源跨语迁移。


### 周二（9月29日） 14:00-16:00｜Speech Synthesis Evaluation 1（Oral；topic: tts）

**Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages**（3357；Ashwin Sankar）  
在 10 种印度语言、5K+ 句与 7 个 TTS 系统上收集逾 120K 成对比较（1900+ 母语听者），覆盖可懂度等 6 维感知，并用 Bradley-Terry 与 SHAP 构建多语排行榜并分析偏好与可靠性。

**Application context in speech synthesis evaluation: A problem and a solution**（747；Fritz Seebauer）  
实证比较四种合成系统在四种应用情境下的评分，发现情境显著改变系统评分且影响因系统而异；数字孪生环境与物理场景评分统计等价，提示仿真测试有助于提高生态效度。

**Is Natural Always Appropriate? Investigating Naturalness and Appropriateness Across Different Domains for TTS Evaluation**（3392；Dominika Woszczyk）  
在 AI 助手、朗读、表演、动画角色与自发说话五域评测五种 SOTA TTS 的适宜性与类人度，发现适宜性独立于自然度变化，表现力域仍难，且自然度易惩罚风格化、奖励自发性。

**NV-Bench: Benchmark of Nonverbal Vocalization Synthesis for Expressive Text-to-Speech Generation**（2211；Qinke Ni）  
NV-Bench 按交际功能分类法构建 1,651 条多语野外非语言发声样本、14 类并配人类参考，以 PCER 指令对齐与声学保真双维协议评测 TTS，客观指标与人类感知强相关。

**Phonetically Grounded Vowel Space Metrics for Evaluating Synthetic Speech During TTS Model Training**（1579；Pasindu Udawatta）  
提出音素学依据的元音空间重叠与 Procrustes 归一化差异指标，在微调训练步上量化合成与真值元音空间相似度，并与口音感知测试显著相关，可作为训练过程中可解释的损失曲线补充。

**The Binding Effect: Analysis of How Multi-Dimensional Cues Form Gender Bias in Instruction TTS**（66；Kuan-Yu Chen）  
将指令 TTS 提示建模为社会地位、职业刻板与人格描述符组合，分析开源模型发现多维线索交互形成复杂性别偏见，且与文本编码器语义先验及训练数据偏斜相关，通用多样性提示难以覆盖。


### 周二（9月29日） 14:00-16:00｜Text Processing for Speech Synthesis（Poster；topic: tts）

**Deterministic Prompting for Speaker-Stable Low-Resource Greek TTS**（2481；Alexandros Potamianos）  
以 WhisperX 对齐过滤有声书得到现代希腊语 TTS 数据，微调 Parler-TTS（880M），用确定性风格提示替代易漂移的 LLM 提示，并在 3.5 小时单说话人数据上用约 5% 参数的 LoRA 锚定身份；WER 10.7%，MOS-I 4.00，MOS-C 4.24。

**DiaMoE-TTS: A Unified IPA-Based Dialect TTS Framework with Parameter-Efficient Adaptation and Reward-Driven Optimization**（2447；Ziqi Chen）  
DiaMoE-TTS 基于 DiT/F5-TTS，采用统一 IPA 前端与方言感知 MoE 文本编码器，并用 PEFT 以数小时数据扩展低资源方言；实验显示 GRPO 强化学习可降低目标方言及相关方言 WER。

**SALT: Selective Allophone-Level Tokenization for Korean Text-to-Speech Synthesis**（2055；Kwangsung Kim）  
SALT 将选定音位变体现象写入韩语 TTS 输入而非依赖隐式学习；在 12.75 小时数据上 SALT-N 的 CER 为 3.30% 且 NMOS 最高（字素输入 CER 4.74%），在 1 小时极低资源下为唯一 CER 低于 10%（8.19%）的方法。

**G2PO: A Lightweight Lexicon-enhanced Framework for Open-Vocabulary Mandarin Polyphone Disambiguation**（1064；Feifan Chen）  
g2pO 以小型 BERT 编码器与词典适配器融合外部词典知识，经混合池化动态构图表示；仅 3.99M 参数（约 BERT 方法 1/27），在 CPP 上准确率 99.15%，未见读音零样本准确率 70.79%。

**UR-BERT: Scaling Text Encoders for Massively Multilingual TTS Through Universal Romanization and Speech Token Prediction**（909；Sangmin Lee）  
UR-BERT 以通用罗马化将书写系统统一，服务 495 种语言的多语 TTS 文本编码，并以语音 token 预测目标增强音位保真与文本-语音对齐，跨语言与资源条件优于近期文本编码器基线。

**Listenability of Synthetic Speech: On the Effect of Linguistic Registers in Text-to-Speech Input**（894；Maja Jønck Hjuler）  
初步研究会话、正式书面、简化书面与 LLM 生成语域在合成播报下的可听性；47 名被试显示书面来源合成可听性高于电台转写，且 LLM 生成文本可听性与维基来源相当。

**Uncovering the Impact of G2P Precision on Korean TTS: A Large-Scale Statistical Validation via a Novel Morphological Engine**（887；Heejo You）  
提出面向对象、音节-语素连通与递归重估的规则韩语 G2P，速度 3.14 ms 对 g2pk 的 14.98 ms、准确率 85.7% 对 27.2%；96 个 VITS 模型统计验证可显著提升可懂度与训练效率。

**Phonikud: Overcoming Phonetic Underspecification for Hebrew Text-To-Speech**（604；Morris Alper）  
Phonikud 框架含开源希伯来 G2P（输出完整 IPA）、ILSpeech 语料、G2P 基准与音频到 IPA 模型；结果显示 Phonikud 音素预测更准，带音标输入的小型本地 TTS 可接近大型专有系统。

**Speech-Worthy Alignment for Japanese SpeechLLMs via Direct Preference Optimization**（976；Mengjie Zhao）  
用偏好对齐使日语 SpeechLLM 输出更适于合成的口语化文本，并提出经母语专家听感核验的 SpokenElyza 基准；方法在该基准大幅提升同时大体保持书面风格原评测表现。

**Knowing What to Stress: A Discourse-Conditioned Text-to-Speech Benchmark**（2743；Avihu Dekel）  
CAST 基准以对比性上下文对评测话语条件词级重音：文本 LLM 能从上下文恢复目标重音，而 TTS 常无法在语音中实现；并发布基准、评测框架、构建管线与合成语料。


### 周二（9月29日） 16:30-18:30｜Instruction-following and Controllable Speech Synthesis（Poster；topic: tts）

**ARCHES: An Agent-Based Refinement Cycle for Hierarchical Synthesis of Sound Effects for Variety Shows**（561；Li Liu）  
ARCHES 以多智能体与检索增强自动为综艺节目生成音效，含 AURA、AXIS 与 CEB 模块及规划-生成- refinement 迭代；在新建 VSSE-Bench 上主客观显著优于 SOTA。

**Scalable Direction-Following TTS via Voice Impression-Guided Pseudo Triplet Construction**（919；Kenichi Fujita）  
提出可扩展伪三元组管线：用印象可控 TTS 生成风格变体，再由 LLM 据印象差写自然语言指示，训练指示跟随 TTS；伪三元组即可稳定保说话人修改，结合录制数据进一步提升指示对齐。

**Poly-InstructTTS: Learning In-the-Wild Expressive Speech Synthesis from Open-Ended Instructions**（930；Junhui Zhang）  
Poly-InstructTTS 从野外视听数据构建约 1,000 小时、覆盖 1,000+ 细粒度情感风格的指令标注语料，以无提示 GPT 与属性 thinking token 及流匹配注入音色，并支持说话人微调迁移指令控制。

**Spiking Vocos: An Energy-Efficient Neural Vocoder**（1086；Yukun Chen）  
Spiking Vocos 为超低能耗脉冲神经声码器，含降 MAC 的 Spiking ConvNeXt、幅度捷径、自架构蒸馏与 Temporal Shift Module；性能接近 ANN 对应体而能耗仅约 14.7%。

**Stabilizing Instruction Supervision for Instruct-TTS via Controllable Diversification and Drift Filtering**（1227；Yizhong Geng）  
针对 Instruct-TTS 中超 40% 无约束 LLM 改写存在语义漂移，提出可控指令多样化、漂移过滤与属性对齐监督的数据中心稳定化方案；中文 InstructTTSEval 指令遵循升至 56.4%，漂移由 40.4% 降至 15.4%。

**Improving Stable Speech Synthesis Post-Training with ChatScorer and Margin-Based Preference Construction**（1881；Wenhuan Lu）  
提出 ChatScorer 辅助奖励与基于间隔的偏好构造用于编解码器 TTS 后训练，缓解异构指标融为标量奖励时候选分不开的问题，减少不良输出并提升生成稳定性，同时保持可懂度与说话人相似度竞争力。

**Accent-Emotion Entanglement in LM-Based Text-to-Speech Systems**（2749；Matthew Hayden）  
以两套说话人相似度相近的零样本 TTS 案例揭示口音-情感纠缠：情感条件可无意改变口音却不被高相似度分数反映；口音 SMOS 与嵌入分析显示一套系统口音变异大（SMOS 1.17–4.13），另一套稳定。

**How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech**（2805；Nityanand Mathur）  
首次将 DAAM 式交叉注意力归因用于语音扩散模型 CapSpeechTTS，在 25 层与 24 个 ODE 步上分析 3,600 组风格说明与文本组合，揭示风格 token 全局条件、与 F0/能量相关及早期深层峰值等模式。

**Beyond Two-stage Diffusion TTS: Joint Structure and Content Refinement via Jump Diffusion**（2875；Jiabao Ai）  
提出跳跃扩散框架，在同一过程中用离散跳跃建模时间结构、连续扩散细化频谱；单次退化形式在 LJSpeech 上 WER 3.37% 对 Grad-TTS 的 4.38% 且 UTMOSv2 更优，完整 UDD 可在分布外慢语中自适应插入停顿。

**PhonemeCVAE: Contrastive Latent Clustering with Class-Conditioned Priors for Controllable Phoneme Interpolation**（2277；Nina Goes）  
PhonemeCVAE 以音素条件高斯先验与对比目标学习结构化连续潜空间，支持推理时音素插值与音系类平滑过渡，并在英语语音数据集上保持合成质量下实现一致插值。

**TAP-ETS: Time Aligned Phoneme Guiding for EMG-to-Speech Synthesis**（3485；Dongyub Han）  
TAP-ETS 以帧级音素序列经交叉注意力条件化 mel 生成，并将对齐音素嵌入直接注入解码器；在 Gaddy 静默 EMG 基准上将 WER 从 25.12% 降至 19.77%，达领先水平。


### 周三（9月30日） 09:00-11:00｜Speech Synthesis: Speech Features, Codec and Representations（Oral；topic: tts）

**Semantic-VAE: Semantic-Alignment Latent Representation for Better Speech Synthesis**（533；Zhikang Niu）  
Semantic-VAE 在潜空间加入语义对齐正则，缓解高维潜变量重建与可懂度权衡；接入 F5-TTS 后在 LibriSpeech-PC 上 WER 2.10%、说话人相似度 0.64，优于 mel 与普通声学 VAE 基线。

**One-Step Token-to-Waveform Generation with MeanFlow in Latent Space**（791；Zheqi Dai）  
在高度压缩潜空间应用 MeanFlow，以平均速度场实现真正一步 Token2Wav；相对多步基线 RTF 最高提升约 17 倍且质量下降可忽略，并给出缓解潜空间失配的精炼策略。

**CycleCodec: Distillation-Free Factorized Neural Speech Codec via Cycle-Consistent Speaker Swapping**（806；Yang Ai）  
CycleCodec 为无蒸馏因子化神经语音编解码器，以循环一致说话人交换作内部自监督，并限制时间容量、用查询式 Transformer 聚合与说话人对比损失；在英语及未见的普通话、越南语上解耦更稳健。

**Low-Framerate Speech Tokenization via Two-Stage Latent Patch Modeling**（2863；Théodor Lemerle）  
Z-CODEC 两阶段潜空间语音编解码：先高帧率对抗 VAE 再潜空间流匹配压缩并加入语义监督；低比特率离散与连续设定重建质量领先或持平，且可在单块 RTX 4070 上训练。

**Transcript-Free Flow-Matching Text-to-Speech via Speech Feature Conditioning**（3190；SooHwan Eom）  
RTFree-F5 用连续自监督语音表示经轻量适配器映射到 F5-TTS 文本条件空间以替代参考转写；在构音障碍语音上将 WER 从 24.6% 降至 10.4%，优于真值转写基线，并在标准基准上保持竞争力。

**Unified Prosody Restoration Using Diffusion Models for Controllable Text-to-Speech Synthesis**（2942；Yuki Ito）  
将韵律恢复统一为从简化易指定的韵律输入恢复帧级韵律，覆盖共五类任务；提出监督与无监督两类扩散韵律恢复器，五任务上均比非扩散基线更准确并保持语言学上合理的韵律结构。


### 周三（9月30日） 09:00-11:00｜Generative Audio and Music（Long Oral；topic: singing）

**Beyond Text-to-Music: Control, Agency, and Evaluation in Generative Audio**（特邀；Lauri Juvela）  
综述演讲面向语音社区梳理生成音频从语音合成到音乐、歌唱、环境声与制作的扩展，强调可控性超越文本提示，并讨论评测为何不能仅靠感知质量与 Fréchet 距离。

**Negation in Audio Generation Models**（1756；Bikash Dutta）  
提出含百万否定提示的 Audio Negation Benchmark（四类否定与三种作用域），并以 AQA 协议评测；AudioGen、AudioLDM2、TangoFlux 对否定音频的 AQA 召回均低于 0.05，否定提示常退化为肯定声景。

**DiffRhythm 2: Efficient and High Fidelity Song Generation via Block Flow Matching**（128；Yuepeng Jiang）  
DiffRhythm 2 以半自回归块流匹配实现忠实歌词-人声对齐且无需时长标签，5 Hz 音乐 VAE 支持长达 210 秒歌曲；提出跨对偏好优化与随机块表示对齐损失，主客观优于开源模型并保持高效。

**Scaling Properties of Continuous Diffusion Spoken Language Models**（2980；Eeshan Gunesh Dhekane）  
分析连续扩散口语语言模型的缩放性质，提出音素 Jensen-Shannon 散度（pJSD）；CD SLM 在验证损失与 pJSD 上呈缩放律，扩至 16B 参数与数千万小时会话数据可生成情感多说话人多语语音，但长程连贯仍难。

**FoleyGenEx: Unified Video-to-Audio Generation with Multi-Modal Control, Temporal Alignment, and Semantic Precision**（112；Shiyao Wang）  
FoleyGenEx 统一视频到音频，含多模态条件注入、保持训练同步的动态掩码与基于副词的数据增强；在 AudioCaps、VGGSound、Greatest Hits 上展现有竞争力的可控 VTA 性能。


### 周三（9月30日） 09:00-11:00｜Emotional Speech Synthesis（Poster；topic: tts）

**Adaptive Oscillatory Inductive Bias for Modeling Sharp Prosodic Dynamics in Diffusion-Based TTS**（1655；Nirmesh J. Shah）  
OscillaTTS 在扩散 TTS 解码器中引入自适应振荡非线性，以可控周期调制与线性旁路稳定信号；在 LJSpeech 与情感语音数据上主客观一致提升，改善尖锐韵律动态建模。

**Word-level Emotional Intensity Control in TTS via Emotion Residual Vectors**（3079；Ji-Hyun Park）  
用词对齐自监督嵌入中的中性到情感偏差作为无标注局部韵律线索（ERV），经低维瓶颈与 RoBERTa 预测器注入中性条件 TTS，实现连续词级情感强度控制并保持自然度。

**Continuous Time-Varying Emotion Control Zero-Shot Text-To-Speech With Emotion Orthogonal LoRA**（1798；Chenchen Wan）  
Emotion Orthogonal LoRA 以三个低秩分支对齐效价、唤醒与支配，并用正交正则鼓励分离效果；结合面向流匹配的 Flow-DGPO 强化学习，在有限数据下改善连续时变情感控制并保持可懂度与说话人相似度。

**ETC-TTS: Emotion Trajectory Learning for Controllable Emotional Text-to-Speech**（3088；Gaeun Kim）  
ETC-TTS 在潜在风格空间将情感强度建模为连续轨迹，以 RVQ 风格提取器与流匹配学习中性到目标情感轨迹，在韩英数据上提升可控性并保持语音质量，情感表达较基线更稳定。

**Beyond One-Size-Fits-All: Personalized and Culturally Adaptive Emotional TTS via Interactive Optimization of Individual Emotion Perception Spaces**（1696；Wangzixi Zhou）  
提出用交互式遗传算法优化个体唤醒-效价感知空间的个性化与文化自适应情感 TTS；日、中、印尼被试评估显示相较平均 A-V 模型，个性化能产生更符合感知的情感表达。

**Cross-modal Consistency Guidance for Robust Emotion Control in Auto-Regressive TTS Models**（1986；Yizhou Peng）  
CCG-CFG 按文本情感与显式语音情感不一致程度动态调节引导尺度，并以困难样本挖掘蒸馏引导信号；在 CosyVoice2 上情感识别准确率最高绝对提升 12%，主观分数相对提升 10%。

**A Large-Scale Dataset of Listener Impressions of Emotional TTS**（1521；Erica Cooper）  
发布情感合成语音质量评估大规模数据集：13 个系统与自然语音共 18,208 样本、五种情感风格，262 名听者对质量与情感类别、匹配度、VAD 等评分，供自动质量评估模型研究公开使用。

**DECRA: Dynamic Emotion Control for Real-time Speech Anonymization**（2927；Ghady Nasrallah）  
DECRA 为实时流式 VC，以因果 SER 在线预测的连续效价-唤醒轨迹闭环控制韵律并解耦说话人与情感，端到端 GPU 延迟小于 80 ms，情感转向优于 SOTA 基线。

**Emo-BPO: Emotion Bidirectional Preference Optimization for Diffusion-based Emotional TTS**（1613；Jiacheng Shi）  
Emo-BPO 从重排的同文情感对联合学习情感对齐与情感对比分数函数，无需辅助奖励模型或额外标注，可无缝接入扩散 TTS 以提升情感可控性与表现力。

**DeSRPA: Decoupled Speech Role-Playing Agent via Inference-Time Intervention**（1627；Wenqiu Tang）  
DeSRPA 在冻结骨干上以推理时干预进行角色扮演，用双层控制向量同步认知转向与外在表达渲染；在 SpeechRole 与 OmniCharacter 上人格与情感一致性显著优于端到端微调，自然度接近专有模型。

**EmoInstruct-TTS: Dual-Path Instruction-Guided Emotional Speech Synthesis**（1834；Ganjun Liu）  
EmoInstruct-TTS 含覆盖 48 种情绪状态的 Emotion2embed 与从自由指令生成声学 grounding 情感表示的 ICE-Flow，并接入 LLM 合成管线，相对强基线提升情感可控性与自然度。


### 周三（9月30日） 14:00-16:00｜Audio Foundation Models and Generation（Oral；topic: generation）

**SAM: A Mamba-2 State-Space Audio-Language Model**（639；Taehan Lee）  
SAM 将音频编码器与 Mamba-2 骨干结合，SAM-2.7B 在 AudioSet 上 21.1 mAP、AudioCaps 上 17.6 SPICE，匹配或超越更大 7B Transformer；分析给出联合微调、紧凑 token 与指令监督等设计原则。

**Samsone: A Family of Open Small Audio Language Models for On-Device Inference**（763；Michal K. Grzeszczyk）  
Samsone 是面向端侧的开源小型音频语言模型家族，核心 Samsone-134M 在同级基准达新 SOTA，并探索 99M 与 356M 缩放；在公开数据上训练并发布代码、权重与 Android 实时演示。

**FreeSonic: Training-Free Temporal-Aware Decoupled Attention for Precise Audio Editing**（1121；Yuxuan Jiang）  
FreeSonic 基于 TangoFlux 的无训练音频编辑框架，用优化反演-反向与联合文本-音频注意力提取目标段，并以调度注意力解耦与任务向噪声注入实现高保真一致编辑。

**Resonate: Reinforcing Text-to-Audio Generation via Online Feedback from Large Audio Language Models**（1823；Xiquan Li）  
Resonate 将在线 GRPO 适配流匹配文本到音频，并以大音频语言模型提供细粒度奖励；仅 470M 参数在 TTA-Bench 音频质量与语义对齐上达新 SOTA，优于离线 DPO/CLAP 奖励方案。

**GACA-DiT: Diffusion-based Dance-to-Music Generation with Genre-Adaptive Rhythm and Context-Aware Alignment**（2348；Jinting Wang）  
GACA-DiT 含体裁自适应多尺度时空节奏提取与上下文感知可学习查询时序对齐，在 AIST++ 与 TikTok 上客观与人类评估均优于现有舞蹈到音乐方法。

**Rethinking Speech Foundation Model Fine-tuning: Better SFT or Better Match?**（2436；Wangjin Zhou）  
在 SUPERB 三分类任务上对 wav2vec 2.0、HuBERT、WavLM 共九个预训练检查点系统比较八种 SFT 变体，发现统计不可区分的最优配方常依赖具体检查点，许多增益更像实例/种子匹配而非普适天花板提升。


### 周三（9月30日） 14:00-16:00｜Voice Editing（Oral；topic: tts）

**FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS**（2764；Nityanand Mathur）  
FlowEdit 为冻结流匹配 TTS 的终身发音适应框架：将纠正反馈优化为文本嵌入扰动并存入 Modern Hopfield 情景记忆；在 312 个跨 18 语系专有名词上目标词 PER 相对零样本基线降 92.7%，约 15 秒/GPU 完成纠正。

**Privacy and quality trade-off in real-time speaker anonymization via editing of age and sex attributes**（2741；Waris Quamer）  
在流式合成中隔离年龄与性别属性编辑，用说话人余弦相似度与 DNS-MOS 及听感验证隐私-质量权衡；隐私随修改增大下降快于质量，存在中等修改即可抑身份且自然度损失较小的最优匿名区。

**RIVET: Robust Idempotent Voice Attribute Editing**（395；Dareen Alharthi）  
RIVET 将幂等性目标引入嗓音属性编辑训练，作为对噪声标签的隐式正则；在可控标签噪声与 GLOBE 自然噪声标注上提升编辑成功率并更好保持说话人身份。

**FineCombo-TTS: Collaborative and Precise Controllable Speech Synthesis Using Text Descriptions and Reference Speech**（2280；Zhiyong Wu）  
FineCombo-TTS 以参考语音与文本描述共同指导，用统一声学表示与 CFM 语音方差预测器建模细粒度变换，并构建编码源到目标属性变化的 FineEdit 成对数据，实现灵活精确可控合成。

**Edit Content, Preserve Acoustics: Imperceptible Text-Based Speech Editing via Self-Consistency Rewards**（1186；Yong Ren）  
在稳定语义空间做基于文本的语音编辑，由流匹配解码器实现声学，并以 Self-Consistency Rewards GRPO（预训练 TTS 作隐式评判）加可懂度与时长约束，相对自回归与非自回归基线提升可懂度、稳健性与感知质量。

**Bagpiper-Edit: Zero-Shot Open-Ended Audio Editing via Rich-Caption**（631；William Chen）  
Bagpiper-Edit 将开放式音频编辑重述为富字幕改写：用户请求译为编辑后字幕，再以原音频为声学锚生成目标；无需成对编辑训练数据即可零样本编辑，跨语音与音频多数情形接近专家模型。


### 周三（9月30日） 14:00-16:00｜Streaming Speech Synthesis（Poster；topic: tts）

**HybridCodec: Fast Dual-Stream, Semantically Enhanced Neural Audio Codec**（3393；Arjun Gangwar）  
HybridCodec 结合双流语义/声学分支并将 SSL 蒸馏入语义流，推理无需 SSL；域内 RVQ-1 语义特化更强、RVQ-all 重建具竞争力，跨域与零样本跨语稳健，较现有双流模型约快 3 倍。

**WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation**（2803；Luca Della Libera）  
WavSLM 将 WavLM 表示量化蒸馏为单一码本并以自回归下一块预测训练，无文本监督在单 token 流中联合建模语义与声学，参数与数据更少且支持流式，一致性与语音生成具竞争力。

**VOSSA: Voiceprint Optimization for Streaming Speech Architectures**（2763；Mu-Ruei Tseng）  
VOSSA 从内容编码器中间层提取说话人信息并以注意力统计池化聚合，与 VC 目标联合训练无需独立说话人编码器；六数据集上改善 F0 动态与元音区分线索，听感自然度与相似度等亦有提升。

**MeanVC 2: Robust Low-Latency Streaming Zero-Shot Voice Conversion**（1961；Guobin Ma）  
MeanVC 2 引入跨 DiT 层调度过去/未来感受野的 FRC 并取消干净块教师强制，支持 40 ms 块稳定转换；通用音色 token 编码器提升对低质参考稳健性，延迟由 211 ms 降至 110 ms 且显著优于 MeanVC。

**FlashTTS: Fast Streaming TTS with MTP Acceleration and X-pred Mean Flow Distillation**（1692；Hanke Xie）  
FlashTTS 以滞后多轨架构原生处理流式文本与语音，并结合并行 MTP 与 X-pred 均值流匹配解码器在恰 2-NFE 完成 token 到 mel；首包延迟降至 325 ms，同时保持强零样本克隆与跨语可懂度。

**Prosodic Boundary-Aware Streaming Generation for LLM-Based TTS with Streaming Text Input**（1192；Changsong Liu）  
对预训练 LLM-TTS 做韵律边界感知后训练：在有限未来文本下学习在指定内容边界早停，推理用滑动窗口提示传递前文语音 token；长文本 WER 由 71.0% 绝对降至 4.8%，说话人与情感相似度相对提升 16.1% 与 1.5%。

**CTC-TTS: LLM-Based Dual-Streaming Text-to-Speech with CTC Alignment**（653；Zhijian Ou）  
CTC-TTS 用 CTC 对齐器替代 MFA，并提出双词交错策略；CTC-TTS-L（序列拼接）偏质量、CTC-TTS-F（特征维堆叠）偏低延迟，在流式合成与零样本任务上优于固定比例交错与 MFA 基线。

**PF-D2M: A Pose-free Diffusion Model for Universal Dance-to-Music Generation**（248；Jaekwon Im）  
PF-D2M 为无姿态依赖的通用扩散舞蹈到音乐模型，从舞蹈视频提取视觉特征，并以渐进训练缓解数据稀缺与泛化问题；主客观在舞蹈-音乐对齐与音乐质量上达领先。

**Streaming T5-based Text-to-Speech Synthesis with Limited Lookahead**（235；Muyang Du）  
S5-TTS 为流式 T5-TTS，经编码器-解码器与单调对齐在收到首几词后即开生成；lookahead-causal 掩码与卷积辅助注意力及交错多源蒸馏在有限前瞻下保持可懂度与说话人相似度，显著降低端到端延迟。


### 周三（9月30日） 16:30-18:30｜Speech Synthesis Evaluation 2（Oral；topic: tts）

**MOS-Bias: From Hidden Gender Bias to Gender-Aware Speech Quality Assessment**（67；Wenze Ren）  
首次系统分析 MOS 中的性别偏见：男性听者评分整体高于女性，低质量语音差距最大；聚合标签训练的自动 MOS 模型偏向男性感知标准，并提出性别感知模型学习组别评分模式以改善总体与分性别预测。

**TDScore: Learning Synthetic Speech Quality Predictors from TTS Training Dynamics without Human annotation**（449；Natacha Miniconi）  
TDScore 利用多 TTS 不同训练检查点的合成语音及迭代/损失等训练元数据作伪标注，在无人主观标注下学习合成质量预测器；多语基准显示迭代标注与人类标注相关。

**Exploring Active Sampling Strategies for Pairwise Comparisons in Speech Synthesis Evaluation**（446；Korin Richmond）  
比较 AB 与 BWS 成对评测中的随机选对与两种主动采样（排序与基于信息增益的 ASAP）；ASAP 揭示更多显著差异，且同等测验时长下 BWS 比 AB 更有效，ASAP 进一步放大该优势。

**Decoding the Ear (DeEAR): A Framework for Objectifying Expressiveness from Human Preference Through Efficient Alignment**（2408；Zhiyu Lin）  
DeEAR 沿情感、韵律与自发性三维将人类表达力感知映射为客观分数，少于 500 条标注即可与专家评分 SRCC=0.85；据此筛选 14K 表达性话语构建双语 ExpressiveSpeech 并微调 S2S，听感表达力提升。

**CodecMOS-Accent: A MOS Benchmark of Resynthesized and TTS Speech from Neural Codecs Across English Accents**（1273；Wen-Chin Huang）  
CodecMOS-Accent 含 24 系统、32 说话人、十种口音共 4,000 条重合成与 TTS 样本，25 名听者提供 19,600 条自然度、说话人与口音相似度标注，揭示说话人-口音相似度关系及同口音听者偏置等。

**MMGenre: Benchmarking Singing Voice Synthesis across Multiple Musical Genres**（137；Wenhao Feng）  
MMGenre 跨 10 主类与 26 子类评测多体裁歌声合成，配自动构建体裁对齐乐谱管线；代表 SVS 跨体裁区分弱，零样本适应增益有限，而轻量体裁特定继续训练有明显提升。


### 周四（10月1日） 09:00-11:00｜LLM Based Speech Synthesis（Oral；topic: tts）

**Decoding Order Matters in Autoregressive Speech Synthesis**（1339；Minghui Zhao）  
在标量量化 mel 上用掩码扩散研究任意解码顺序，发现从左到右并非最优，从右到左更优，自适应置信 top1 在模型输出中 MOS 最高；有效顺序常保持局部连续帧簇。

**Decoupling Search and Evaluation: Efficient Beam Decoding for Language Model-Based Text-to-Speech Synthesis**（1531；Chenlin Liu）  
SaVE-Beam 将假设扩展与序列打分解耦：轻量学生做块级束构建、教师 LM 保留精确评估，并加硬重复约束；相对常规束搜索最高加速 5.1 倍且不降质，相对采样 WER 最高降约 50%。

**Eliminating Stability Hallucinations in LLM-based TTS models via Attention Guidance**（1345；Shiming Wang）  
提出用 Viterbi 的 Optimal Alignment Score（OAS）评估文本-语音对齐，并融入 CosyVoice2 训练；再用预训练注意力经思维链引导学生模型，在 Seed-TTS-Eval 与 CV3-Eval 上减少稳定性幻觉且无额外负效应。

**MamTra: A Hybrid Mamba-Transformer Backbone for Speech Synthesis**（1031；Tan Dat Nguyen）  
MamTra 交织 Mamba 与 Transformer，并以知识迁移从预训练 Transformer 蒸馏，避免从头训练；最优混合配置下推理显存最高降约 34% 且不损保真，即便仅用原训练数据的 2%。

**DLLM-TTS: Block Discrete Diffusion Language Model for Text-to-Speech Synthesis**（788；Wasim Madha）  
DLLM-TTS 将 TTS 表述为对 X-Codec2 token 的条件块离散扩散，块内并行、块间顺序；0.6B 模型在 20K 小时数据上 RTF 0.15，Seed-TTS-eval 表现具竞争力。

**Bagpiper-TTS: Natural Language Guided Universal Speech Synthesis**（873；Haoran Wang）  
Bagpiper-TTS 先由自然语言请求推理出含转写与元数据的富字幕再合成，支持多说话人、意图到语音、角色扮演与歌声等；Seed-TTS-Eval 上 WER 1.7%，多应用主观与 LLM 评判接近专用模型。


### 周四（10月1日） 09:00-11:00｜Speech Synthesis Evaluation and Benchmarking（Poster；topic: tts）

**PolyBench: Benchmarking LLM-based TTS Systems for Chinese Polyphone Disambiguation**（998；Feifan Chen）  
PolyBench 含覆盖 494 个多音字与 88 个多音词的三套测试集，并探索 LALM 自动注音；评测 17 个开源 LLM-TTS，最佳系统多音字发音准确率仅 82.02%，方言/口语/文学类差距显著。

**Towards a Phonology-Informed Evaluation of Multilingual TTS**（3311；Neeraj Kumar Sharma）  
提出基于分类器的音系审计框架，以人类语音为基准检验 TTS 是否保持对立；对阿萨姆语 ATR 元音和谐与 Meta MMS TTS 显示约 1/3 的 [+ATR] 中元音实现为 [-ATR]，而人类语音无此偏置。

**An Evaluation Framework for Text-to-Speech Voice Reconstruction**（2600；Ariadna Sanchez）  
为言语障碍者的 TTS 嗓音重建提出主客观评测框架：主观用情境化 BWS 评可懂度与身份，客观用双参考分布度量权衡；在 193 说话人、17 个零样本 TTS 上验证任务对齐可靠性。

**Evaluating Automatic Laughter Phone Annotation for Socially-Situated Laughter Synthesis**（2141；Hiroki Mori）  
用新标注的十一说话人数据改进笑声音素识别器，并分别以人工与自动标签构建 SPSS 与音频 LLM 笑声合成器；听感显示音频 LLM 更自然、SPSS 更再现笑法，自动标签系统仍不及人工标签。

**Benchmarking Large Language Models for Grapheme-to-Phoneme Conversion: A Japanese Case Study**（1800；Tomoki Koriyama）  
在 3000 句人工标注日语上对 30 余个 LLM 做 G2P 基准：解析模式多数优于直接预测，最佳 LLM 假名 CER 低于 0.52%（传统工具最佳 1.03%），且将 LLM 假名送入假名输入 TTS 发音优于端到端 TTS。

**The False Resonance: A Critical Examination of Emotion Embedding Similarity for Speech Generation Evaluation**（39；Yun-Shao Tsai）  
通过可控对抗任务与人类对齐测试质疑情感嵌入余弦相似度作情感表达客观指标：尽管分类准确，零样本相似度易受语言与说话人干扰，与人类感知错位并奖励声学模仿而非真正情感合成。

**LLM-Based Multi-Reference Evaluation for Efficient and Robust Assessment of Phrase Break Annotations**（2225；Hoyeon Lee）  
提出 LLM 多参考评测（LMRE）为短语停顿标注生成多种合法切分；在 1,356 条韩语五策略标注上，接受行为与分数相关均比单参考更贴近人类判断。

**Investigating the Relationship between Objective AI-driven Metrics and Subjective MOS for In-the-Wild Speech**（2203；Shekhar Nayak）  
在连续干净 TTS、离散野外 MQTTS、加性噪声对照与真值录音上收集 768 条自然度评分：UTMOSv2 与人类相关从连续干净的 r=0.51 崩至离散野外的 r=-0.01；DNSMOS 对加噪惩罚重于生成伪影，与听感矛盾。

**SongBench: A Fine-Grained Multi-Aspect Benchmark for Song Quality Assessment**（1985；Dapeng Wu）  
SongBench 沿人声、乐器、旋律、结构、编曲、混音与乐感七维细粒度评歌，含 11,717 条专家标注样本，与专家评分高相关，用作诊断文本到歌曲生成差距的基准。

**GRATS : A Natural Multi-Speed Mandarin Dataset for Speech Time-Scale Modification Benchmarking**（1842；Yu Tsao）  
GRATS 为自然录制的多说话人普通话多语速平行语料（25 人，0.5x–1.5x 五档），用于语音时域伸缩评测；基准显示极端语速下可懂度与感知质量权衡及时间、音高一致性下降。

**On the Effect of Segmentation Width and Cluster Size on Speech Resynthesis and Continuation in Generative Spoken Language Models**（999；Shunsuke Kando）  
在 GSLM 中变化固定分段宽度与 K-means 簇数形成多种比特率，显示低于基线比特率仍可合成清晰自然语音，且续写质量在多指标上保持稳定，提示常规设定对有效生成可能冗余。

**ConformalMOS: Uncertainty-Aware MOS Prediction with Conformal Intervals and Ordinal Modeling**（572；Tashfain Ahmed）  
ConformalMOS 在 MOS 点估计外用共形预测给出有覆盖保证的区间，训练上将 one-hot 转为高斯平滑序数分布；在 BVCC 上 MSE=0.08 且覆盖经验有效，提升 TTS/VC 部署可靠性。


### 周四（10月1日） 14:00-16:00｜Flow Matching for Speech Synthesis（Oral；topic: tts）

**Hierarchical Conditional Continuous Normalizing Flows for Creaky Voice Editing under Speaker Identity Preservation**（1341；Petra Wagner）  
提出分层条件连续归一化流，分阶段注入条件以结构化解耦高层说话人属性与低层副语言嗓音质量；以吱嘎声操控为例，对音高与性别等高层属性影响显著更小，更好保持感知说话人身份。

**TC-DBI: A Plug-and-Play Trajectory Confidence-Guided Dynamic Block Inference Strategy for Speech Synthesis with Continuous Block Flow Matching**（1242；Ren Wang）  
提出由 ODE 轨迹平直度导出的轨迹置信度（TC），并给出即插即用的 TC-DBI：截断并重生不可靠区域以动态调整块大小；TC 与生成误差强相关，在相近效率下提升稳健性与感知质量。

**Bridging the Gap: A Hierarchical Framework for Cross-Modal Style Modeling in Expressive TTS**（1513；Jiale Chen）  
OTAFlow 以最优传输对齐、对比学习与多任务监督构建统一风格空间，再用条件流匹配建模残差模态缺口以从单提示生成多样声学风格嵌入；接入下游 TTS 后细粒度风格检索与合成风格准确度显著优于基线。

**RobustSpeechFlow: Learning Robust Text-to-Speech Trajectories via Augmentation-based Contrastive Flow Matching**（3086；Jinhyeok Yang）  
RobustSpeechFlow 将对比流匹配扩展为长度保持的重复/跳过潜变量增强，无需外部对齐器或偏好数据即可惩罚真实失败模式；Seed-TTS-eval 上 WER 由 1.44 降至 1.38（仅 0.06B 参数），ZERO500 上英韩 CER 亦降。

**Improving Flow Matching based Text-to-Speech with Dual-Model Preference Optimization and Classifier-Free Guidance**（2412；Minchuan Chen）  
提出用两个独立模型分别建模偏好与非偏好信息的偏好优化，并改进 CFG 以增强对文本与参考音频的遵循；实验显示可懂度、说话人相似度与自然度显著优于基线流匹配 TTS。

**Enhancing Flow Matching with A Unified Guidance Framework for Efficient and Robust Speech Synthesis**（1015；Zuda Yu）  
统一引导框架含异构增强的数据引导与轨迹整流加内在引导目标的模型引导，将条件知识蒸馏入权重并拉直推理轨迹以去掉 CFG 开销；推理近加速三倍并有效提升说话人相似度。


### 周四（10月1日） 14:00-16:00｜Voice Conversion（Poster；topic: voice-conversion）

**SSL-GMMVC: Interpretable Voice Conversion via Locally Linear GMM Transforms in Self-Supervised Representation Space**（1688；Tomoya Tanabu）  
SSL-GMMVC 在自监督特征空间用 GMM 对源-目标配对建模，以仿射变换的后验加权和完成转换；主客观显示说话人相似度提升，且随混合分量增多，受限协方差变体亦可超过深度学习基线。

**From A to B to A: Palindromic Zero-Shot Voice Conversion with Non-Parallel Data**（1663；Moshe Mandel）  
用 WavLM 上的 KNN 检索对齐非平行源目标语音以构造合成到真实训练对，并加入预训练说话人验证损失；仅英语训练即可跨多语达到高自然度与强说话人相似度，优于竞争 VC 基线。

**MeanVoiceFlow2: Joint Optimization of Mean Flow and Content Encoder for Fast One-Step Zero-Shot Voice Conversion**（1596；Takuhiro Kaneko）  
MeanVoiceFlow2 联合优化流转换模块与高效内容编码器，经 MeanVoiceFlow 转换蒸馏、真实重建及扩散-GAN 与教师引导条件增强训练；零样本 VC 感知质量更高，推理约快 9 倍且说话人相似度相当。

**Zero-VC: Zero-Lookahead Streaming Voice Conversion via Speaker Anonymization**（1340；Yudong Li）  
Zero-VC 将说话人匿名化用作扰动机制以抑制音色泄漏同时保留韵律效用，使生成器显著降低对未来上下文依赖，从而实现严格因果、零前瞻的流式零样本语音转换。

**Improving Model Expressivity and Speaker Matching in Low-Latency Voice Conversion**（796；Anders R. Bargum）  
面向低延迟实时 VC，通过激励信号显式补回丢失韵律，并将互补信息融合进全局说话人嵌入，训练时采用编码器特定信息扰动；在因果与低延迟约束下相对 SOTA 实时基线提升说话人匹配指标。

**Universal Speech Content Factorization**（198；Matthew Wiesner）  
USCF 以可逆线性最小二乘学习通用语音到内容映射并抑制音色，仅需数秒目标语音即可得说话人特定变换；作零样本 VC 具竞争力，并可作为音色提示 TTS 的声学表示。

**CFLOW-VC: An unsupervised cycle training strategy based on normalizing flows for Voice Conversion**（48；FeiBao Song）  
CFLOW-VC 在 VITS 上基于归一化流的无监督循环训练缓解非平行设定下的训练-测试失配，引入 mel 风格编码器与数据增强；主客观优于 SOTA 基线。

**WhispEar: A Bidirectional Framework for Scaling Whispered Speech Conversion via Pseudo-Parallel Whisper Generation**（1827；Yingda Shen）  
WhispEar 基于统一语义表示构建耳语到正常与正常到耳语双向框架，后者可从丰富正常语音零样本生成伪平行耳语以扩增 W2N；并发布迄今最大中英耳语-正常平行语料，性能优于强基线。

**Imitation Learning for Elder-Facing Speech Synthesis**（2107；Dongrui Han）  
提出面向老年人听觉理解需求的模仿学习 TTS 框架，并以两阶段同策略奖励学习改进 GRPO 以在有限专家示范下缓解奖励黑客；主客观优于 GRPO 与监督基线。


## 跨会场判断

- **条件与规模在“同一套离散/流式骨干”上合流**：零样本多语、指令可控、长篇章与流式部署，大量工作共享 codec/声学 token、流匹配或扩散解码；差异更多在条件接口（参考语音、脸、指令、历史文本）与训练后对齐，而非另起一套声学模型。
- **后训练（偏好/RL）从 LLM-TTS 扩到流匹配**：DPO、GRPO、测试时前缀自适应等被用来抠说话人相似度、重音、指令遵循与细节音质；奖励设计（韵律工具、WER、风格统计量）本身成为方法的一部分。
- **解耦是跨 TTS / VC / 歌唱的共同工程问题**：内容—风格、韵律残差、口音强度、音色与旋律/伴奏，普遍依赖信息瓶颈、伪标签或显式控制塔；失败模式则表现为身份漂移、源音色泄漏或口音—情感纠缠。
- **长音频与低延迟把“上下文状态”和“计算图形状”推到前台**：跨块状态、历史文本、潜空间时间压缩与窗口注意力，说明篇章级自然度已无法只靠加长训练句解决。
- **低资源进展与评测缺口同时被点名**：基础模型适配与前端统一能快速铺开语种，但特邀综述与多语偏好评测都强调：质量、可信评测与社区需求仍未随覆盖率同步解决。
- **评测专场与生成专场形成闭环**：一边用迭代再合成、情境适宜性、非语言发声等协议拉大系统区分度，一边用 ALLM 评判、成对偏好与诊断案例分析反哺训练目标——评测不再只是会后表格。
- **歌唱/音乐生成把编辑与多轨工作流写进任务定义**：歌词修订、分轨 V2A、音效智能体与克隆+伴奏共生成，表明生成式音频正在从“一条波形”转向可局部修改的制作管线。
- **Show-and-Tell 与系统演示补上部署与治理切口**：听端流式 VC、TTS 指纹、嗓音质量 GUI、机械声道与场景仿真等，提示学术议程已并行触及实时性、可解释操控与合成音频溯源。
