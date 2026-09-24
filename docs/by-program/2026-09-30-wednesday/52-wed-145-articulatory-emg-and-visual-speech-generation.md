# Articulatory, EMG, and Visual Speech Generation

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：7
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦发音器官、肌电与视觉模态驱动的语音/人脸生成：从发音合成评估到 EMG 静默语音、从说话人脸到唇同步配音，再到 rtMRI 发音视频合成。核心问题是如何在缺少声学监督或部分模态缺失时，仍重建可懂、可编辑且身份一致的语音或面部运动。

视觉与人脸侧，工作从可编辑三维人脸重建、方言感知的人脸 TTS，到离散语音表征驱动的三维面部动画，再到用二值语音活动条件做唇同步配音。共同趋势是：用更轻、更可编辑的条件（几何—纹理解耦、方言音高、VAD、离散 token）替代或补充视频唇部轨迹。

肌电与发音侧，GETS 用静默语音识别语义引导扩散式 EMG→语音；SVA 用静默—有声平行 EMG 的多层次对齐缓解无真实语音标签；另有研究追问从舌超声等发音数据预测 f0 的信息来源，以及 rtMRI 说话人无关波形合成。特征设计与生成式建模在“补回反演丢失信息”与“合成结果是否仍代表估计的发音”之间形成方法论张力。

迁移学习角度上，音素添加研究表明：预训练更利于自然度，对新音素 PER 未必节省数据。整体上，本场把跨模态对齐、语义纠错与发音可解释性并列为静默/视觉语音系统的关键能力。

## 论文技术总结

# Exploring Pre-training Benefits on Phoneme Addition through Fine-tuning in Speech Synthesis

- 论文编号：208
- 报告人：Masato Murata
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/murata26_interspeech.pdf

## 问题
低资源 TTS 常先高资源预训练再微调；目标语含未见音素时需“音素添加”（扩展嵌入并随机初始化）。预训练已见音素能力是否真正帮助学会新音素，此前多只报整体自然度，证据不足。

## 方法
两设定：(1) 仿真——用 LLM 生成 Limited（排除目标音素）与 Full（含全部）语料，同一说话人/语言 TTS 合成，隔离语种与说话人混淆；目标组为爆破音或前元音。(2) 真实跨语——VCTK 英预训练 → JSUT 日微调，添加 20 个日语特有音素。Conformer-FastSpeech2，微调 vs 同数据从头训；数据量 100–2000 句。指标：目标音素 PER（wav2vec2 识别）与 UTMOS。

## 实验与结果
仿真与跨语一致：微调 UTMOS 优于或持平从头训（尤其低资源）；但达到相近 Target PER 所需数据量 ≥ 从头训，甚至更差。低资源下从头训爆破闭合模式更清晰；微调在保住已见音素时更难学新音素。

## 结论
预训练主要提升合成自然度，对音素添加本身帮助有限——与“预训练语言知识必然利于新音素”的常见假设相反。建议更广音素库存预训练或专为新音素设计辅助损失。

## 点评
用可控仿真拆开“自然度”与“新音素习得”，结论反直觉但证据链完整，对低资源跨语 TTS 实践有直接提醒：别指望随机扩嵌入就能自动借力预训练。仿真用合成语音，声学分布可能偏乐观；跨日语结果能部分对冲这一顾虑。


# ES-3DF: Editable Speech-Driven 3D Face Reconstruction via Geometry Texture Disentanglement

- 论文编号：433
- 报告人：Ju Zhang
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/wang26i_interspeech.pdf

## 问题
现有语音驱动人脸多为 2D 合成，缺显式 3D、跨视角几何不一致，也难精细编辑；级联「先 2D 再 3D」会误差累积。

## 方法
ES-3DF 直接从短语音重建可编辑带纹理 3D 脸。Disentangle：用 3DDFA V3 抽几何（3DMM 系数）与 StyleGAN2 式 UV 生成器分离纹理。Align：ECAPA-TDNN 提语音特征，ShapeMLP 回归 α_id，TexMLP 对齐纹理；用 Class-Aware Multi-Slot Memory Bank（每说话人 K=4 原型，EMA 更新）与 Multi-Slot InfoNCE 桥接语音–纹理模态差。可微渲染合成 3D 脸，3DMM 系数支持形状/表情/姿态/平移编辑。

## 实验与结果
VoxCeleb1∩VGGFace，1225 人（训练 F–Z 共 924，验证/测 301）。对比 CMP、VoiceStyle：Landmark L1/L2 1.33/19.65，α_id L1/L2 37.56/5.25，优于基线；面部部位 IoU（如 nose 84.55%、skin 87.94%）更高；FaceNet Feature Cos 31.04%（w/ GT α 达 47.15%）。消融显示去掉 3D 解耦或对比学习均下降。

## 结论
几何–纹理解耦 + 多槽对比对齐可直接从语音得到高保真、可编辑 3D 脸，几何与身份一致性优于级联/纯 2D 方法；未来拟加强高维身份特征的跨模态对齐。

## 点评
把「可编辑」落到显式 3DMM+UV，比潜空间粗控更可解释；多槽 Memory Bank 针对纹理高维、身份多原型的设定合理。嘴唇 IoU 仍偏低，作者也承认静态唇形从动态语音反推是病态问题。


# K-DIALECT : Korean Dialect-Aware Face-Based Speech Synthesis

- 论文编号：616
- 报告人：Seongyeon Yang
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/yang26d_interspeech.pdf

## 问题
韩语方言韵律差异大且资源少；多数 TTS 面向标准语，依赖参考音频在低资源方言上不现实；人脸条件 TTS 尚未系统建模方言韵律。

## 方法
K-DIALECT：双分支人脸编码器（ArcFace 身份 + CLIP 风格，拼接后融合 ℓ2 归一化）；方言条件 pitch predictor 输出与音素对齐的半音相对 f0 轨迹；FiLM 将 pitch 嵌入调制到声学隐状态。推理只需文本、人脸图与方言 ID；T5 Dialect Translator（42GB 韩语预训练 + 标准–方言并行微调）做词汇/语尾转换。多任务损失含 Ltxt、Lmel、对比/MSE/蒸馏/正交与 Lpitch。

## 实验与结果
AI Hub 韩语方言数据：六方言约 1511.55 分钟、2749 说话人；仅首尔子集有人脸，人脸编码器只在首尔训。对比 XTTS-v2：配对图声上 SECS 0.70（基线 0.79）、WER 0.25、MCD 14.66（优于基线）；方言韵律指标平均 F0-DTW-RMSE/G-SHAPE/MOD 等优于 XTTS。主观 30 人：Full 平均 MOS-F/N 3.96/3.90，显著高于无 pitch 与 XTTS；模态匹配 Rank-M 亦更好。

## 结论
人脸身份/风格解耦 + 方言 pitch 预测可在无参考音频下提升六种韩语方言的流利度与自然度；未来可建模方言内部变异。

## 点评
把「方言韵律」显式做成 f0 轨迹而非只靠方言 ID，对韩语句末边界调尤其对症。人脸只用首尔子集是硬约束，跨方言身份–方言组合的泛化仍依赖视觉条件可迁移这一假设。


# Feature Design and Generative Modelling in Deep Articulatory Synthesis

- 论文编号：694
- 报告人：Charles McGhee
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/mcghee26_interspeech.pdf

## 问题
用合成评估发音反演时，常把反演丢失的信息（F0/能量/说话人等）显式或隐式加回；结果可能不再代表反演得到的发音，却很少系统分析特征与建模类型对语音内容的影响。

## 方法
基于 ArtVVN（舌/唇/颌 6×2D + 鼻音/浊音 2D，共 14 维）训级联合成器（Conformer→mel→冻结 BigVGAN）。对比加 WavLM 说话人嵌入、F0+STE 源特征，以及 Conditional Flow Matching（DiT，Euler，主结果 NFE=2）。对照 SPARC 声码器与更大容量 Conformer（12 层、hidden 768）。

## 实验与结果
训于 LibriTTS-R clean-100（Large 另加 360）；测 test-clean 与平行 noisy/clean VCTK。源特征降低 in-domain PER，但 noisy 条件下 PER/MSE 恶化更明显，说明小模型会依赖源特征重建音素。Large+Spk 可接近「+Src」的音素一致性。FM 在低 NFE 与非生成模型音素一致性相近；提高 NFE 使 PER 升、UTMOS 升（约 NFE≥10 趋于平稳）。最小对特征替换：替换源特征显著伤辅音准确率（约 84.9%→75%），并引入大跨度混淆（如 /E/–/u/、/b/–/n/）。

## 结论
附加说话人尤其是源特征会扭曲发音合成的音素内容；CFM 可在低 NFE 保持一致性、用更高 NFE 换质量。用合成结果对反演下结论时必须谨慎设计输入与模型。

## 点评
把「评估用合成」本身当研究对象，直接挑战领域常见做法；特征替换实验把依赖关系做成可测证据。对想用 ASR-PER 闭环评估反演的工作，这是很实用的警示。


# From Tokens to Faces: Investigating Discrete Speech Representations for 3D Facial Animation

- 论文编号：1397
- 报告人：Pedro R. Corrêa
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/correa26_interspeech.pdf

## 问题
语音驱动 3D 面部动画常用 SSL 连续表征，但声学 codec、语义+声学混合、ASR 式 label-based 离散表征是否更合适尚不清楚；离散 token 对面部运动的信息内容也缺系统剖析。

## 方法
冻结比较四类编码器：HuBERT（semantic）、SpeechTokenizer（semantic+acoustic）、WavTokenizer（acoustic）、CosyVoice2（label-based），各接 GRU（扩散去噪，FaceDiffuser 复现为 Base）或 Transformer（L1+速度/加速度平滑）。在 BEAT2（约 27h，FLAME→51 维 ARKit blendshapes）上训解码器。指标：LVE、Jitter、自提 Bilabial Closure Score（BCS）；MUSHRA 式感知；对音素/viseme 做归一化条件熵探针与 Ridge 连续 blendshape R²。并给出 AVTTS 概念：CosyVoice2 TTS token 并行驱动语音与面部 Transformer。

## 实验与结果
LVE 上 HuBERT 最优（0.26），CV2+Transformer 接近（0.28）；Transformer 普遍降低 Jitter。BCS：Base 57.5%，CV2+T 47.0%，多数离散+GRU 接近 0。感知：CV2+T 与 Base 无显著差异，均优于 HB+T。探针：ST 音素熵最低（更好编码音素），但面部动画差；声学表征音素信息弱。AVTTS 可从文本共享 token 同步出语音与面部。

## 结论
semantic 与 label-based 表征均适合驱动 3D 面部动画且感知相近；编码音素类信息似必要但非充分，低结构声学信息可能有害。离散共享空间可支撑统一 AVTTS。

## 点评
把表征类型与「音素探针 vs 面部指标」对齐来看，比单纯刷 LVE 更有解释力；BCS 与感知更相关是有用的方法论提示。ST 音素好却动画差，说明「有音素信息」不等于「对面部解码友好」。


# Not Quite My Tempo: Voice Activity-aware Speech Synthesis for Lip-Synchronous Dubbing

- 论文编号：1407
- 报告人：Alejandro Pérez-González-de-Martos
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/perezgonzalezdemartos26_interspeech.pdf

## 问题
唇同步配音要求目标语语音–静音时间结构与片源严格对齐；现有方法多用唇动视频条件，依赖成对视频且面对卡通/多人场景脆弱。

## 方法
在类 F5-TTS 的 inpainting/流匹配 TTS 上加帧级二值 VAD 条件（Silero）：嵌入后加到编码器表示，约束 DiT 只在有声画布上生成。训练时随机 mask VAD，使推理可选开/关。架构含 ZipVoice 式平均上采样、显式说话人嵌入（FACodec、ERes2NetV2）与 GST，SoundStream 声码器。无视频，仅音频–文本。

## 实验与结果
English：LibriTTS-R；另训多语专有+公开数据。测 mTEDx（希/法/葡/俄→英，7–15s 且含 ≥500ms 停顿，291 句）。Silero VAD 帧准确率：无条件约 73%→有条件约 96%（LibriTTS 模型）；多语模型约 91.6%。静音起止偏差在条件开启时集中于 0。40 人主观：Placement/Prosody MOS 有无 VAD 差异不显著（约 3.7–3.8）。WER 略升（如 LibriTTS 8.5%→13.9%），与译文时长不适配有关；定性见省略/重复/重排以保住时间轴。

## 结论
轻量 VAD 条件即可高精度对齐配音时间结构且几乎不损韵律自然度；对未做等时适配的译文仍会牺牲可懂度。未来拟用更细粒度发音/唇动信息，并减少对等时 MT 的依赖。

## 点评
用二值活动掩码替代唇动视频，工程上很务实，且随机 mask 做成可选约束适合后期。边界情况清楚：模型优先保时间轴而非字面完整，说明系统假设「译文已大致等时」仍关键。


# GETS: Guiding EMG-to-Speech Synthesis via Silent Speech Recognition

- 论文编号：1938
- 报告人：Jiwon Lee
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/lee26r_interspeech.pdf

## 问题
Silent EMG→语音信息稀疏，仅最小化声学重建误差难保证语义可懂度；现有 ETS 在 silent 测试上 WER 常超 25%。

## 方法
GETS：DiffWave 骨干的 EMG 条件 mel 扩散生成器 + SSR 分类器引导。训练用 voiced EMG 与 DTW 对齐的 silent 特征条件去噪（classifier-free）；推理时 silent EMG 直接编码，并用 MONA-LISA SSR 预测文本 ˆt，以微调 ASR（AVEC 音频变体）的 ∇ log p(ˆt|xt) 做 classifier guidance（ω1=2.5，ω2=1.5，t≤270）。HiFi-GAN 声码。

## 实验与结果
Gaddy & Klein 单说话人：1285 平行对 + 5470 非平行 voiced。Silent 测试 Whisper WER 11.89%（vs Gaddy 25.74、SU-ETS 26.29、diff-ETS 32.1）；DeepSpeech 21.32%。词/停顿起止 MAE 与能量 RMSE 具竞争力；ω1=0 时时间对齐与 WER 明显变差，说明非纯 TTS。打乱实验：EMG-shuff 能量崩坏远重于 Text-shuff。消融：去 ω2 时 WER 升至 32.78%。

## 结论
SSR 语义引导可在不牺牲 EMG 固有韵律线索的前提下大幅提升 silent ETS 可懂度，达到新 SOTA。

## 点评
把 LipVoicer 式 ASR 引导迁到 EMG，直击「编码器容量不够」的旧瓶颈。依赖 SSR/LLM 精修文本质量，引导上限与 MONA-LISA（silent WER 8.93%）绑定；单说话人数据也限制泛化结论。


# Enhancing EMG-to-Speech via Silent-Voiced Representation Alignment

- 论文编号：2931
- 报告人：Jiwon Lee
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/lee26v_interspeech.pdf

## 问题
Silent EMG 无对齐声学监督且数据远少于 voiced；现有 target-transfer 只搬声学目标，忽略平行 silent–voiced EMG 的表征一致性；ETS 结果跨随机种子波动大却少被报告。

## 方法
提出 Silent-Voiced Alignment（SVA）损失：对平行对在输出层（声学表征 + 音素分布，DTW）与各 Transformer 隐层（复用输出对齐路径，余弦距离）对齐 silent 与 voiced 编码器表示；soft scheduling ω=σ(τ−Lout_SVA)。总损失在 silent 上为 α(声学+音素)+SVA。两阶段：先仅 voiced 预训练，再 voiced+silent 微调。可插到 Gaddy（mel）与 SU-ETS（HuBERT-Soft）管线。

## 实验与结果
Gaddy & Klein：1289 平行对 + 5477 非平行 voiced；98 测试句。10 种子协议：Ours(Mel) CER/WER 12.88%/25.14% vs Gaddy 14.16%/26.75%（相对 WER −6.0%，p=0.002）；Ours(SU) WER 26.55% vs 27.78%（p=0.009）。Mel 设定 FSD 显著更好。消融：输出+隐层全 SVA 最优；仅隐层弱于仅输出。

## 结论
显式 silent–voiced 表征对齐可稳定提升不同声学目标下的 ETS 可懂度，且易集成；多种子报告暴露了该领域以往均值不可靠的问题。

## 点评
把平行 EMG 当「中间教师」而非只对声学目标 DTW，监督更近、更稳。增益幅度不大但统计显著且方差更小，对小数据噪声模态很有说服力；协议本身可能比百分点更有长期价值。


# Automatic pitch prediction from speech articulation: Where does the f0 information come from?

- 论文编号：1288
- 报告人：Beliz Ozkan
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/ozkan26_interspeech.pdf

## 问题
源–滤波理论认为 f0 与声道独立，但 SSI 文献能从舌超声/唇等预测 f0，形成理论悖论；需弄清信息来自何处、何种条件下可泛化。

## 方法
在 TaL（UTI+唇+音频）上复现/扩展：CNN+FC 编码器（唇 L、舌 T、L+T；及 MFCC 子集 M0:2/M3:12/M0:12）+ 1D CNN 解码器（1/3/7/17 帧上下文）。用读白训练、自发测试；按 Continuous Wavelet Transform + k-means 分词级突显度 P0–P2。9 说话人（TaL1 + 8 TaL80 fine-tune）。用 Grad-CAM、相关/RMSE（八度）与 LPCNet 重合成主观可接受性检验四假设。

## 实验与结果
T/L+T 优于仅 L；舌相关约 0.63–0.68（TaL1），Grad-CAM 无稳定舌骨/喉源注意→拒 H1（图像泄露声门）。时间上下文对 T/L+T 几乎无显著影响→拒 H2。自发相关从读白约 0.65–0.70 跌至约 0.38–0.39→确认 H3 过拟合。P2 词预测显著更好→确认 H4。38 人强制选择：高 P2 比例时 L+T 与 M0:12 可接受率达约 87.5%，局部韵律功能比全局轨迹更重要。

## 结论
UTI 可部分预测 f0，主要抓突显处的局部发音–f0 耦合而非可见声门；读白模型难泛化到自发。SSI 应重视真实会话数据，并侧重局部韵律功能而非复制全局 f0。

## 点评
把「能预测」拆成可证伪假设，比继续刷 RMSE 更有科学价值。H3/H4 对工程含义清楚：训练域与突显结构决定可用性；主观实验把「局部够用」落到感知。


# Speaker-Independent Speech Synthesis from Real-time MRI Articulatory Data

- 论文编号：3379
- 报告人：Yuto Otani
- 程序：Wednesday 30 September 2026 / Articulatory, EMG, and Visual Speech Generation
- 技术分类键：multimodal
- 全文：https://www.isca-archive.org/interspeech_2026/otani26_interspeech.pdf

## 问题
rtMRI 语音合成多依赖说话人相关模型，未见说话人难以合成；TTS 式管线虽可泛化，但时长/韵律/音色不直接来自 rtMRI。

## 方法
EfficientNetV2-B0 抽帧特征 + E-Branchformer 时序建模，经 FiLM 注入说话人信息后回归 mel，BigVGAN-v2 声码。训练双路径：音频 X-vector 与 MRI 注意力池化说话人表征共享 FiLM；MRI 侧用 stop-grad 余弦损失对齐音频侧。另加 log-F0 Pearson 相关损失（高周期帧）以学习跨说话人相对韵律。推理仅用 rtMRI，无需参考语音。

## 实验与结果
USC 75-Speaker Speech MRI，质控后 51 人（训/验/测 43/4/4）。rtMRI 路径 dWER/dCER 与 audio 路径接近（如 sub20 8.2/3.5）；朗读最好（dWER 约 4.5–11.1%），自发与 nonce 更高。F0 相关约 0.38–0.57（高周期帧 0.62–0.76）；SECS 0.95–0.96，但同性别区分弱。

## 结论
跨模态说话人对齐可实现未见说话人的 rtMRI→语音；相对韵律可捕，绝对 F0 与同性别区分受限于中矢面分辨率与声门不可见。

## 点评
把「说话人信息必须来自 MRI」做成可训练对齐，比接 TTS 更忠实发音信号。同性别 SECS 对角塌缩说明身份仍偏粗；朗读–自发差距也提示自然会话仍是瓶颈。

