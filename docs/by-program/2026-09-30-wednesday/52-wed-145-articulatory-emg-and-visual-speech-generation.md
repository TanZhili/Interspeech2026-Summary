# Articulatory, EMG, and Visual Speech Generation

- 日期：2026年9月30日（星期三）
- 时间：16:30-18:30
- 形式：Poster
- Area：7
- 论文数：10
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场聚焦发音器官、肌电与视觉模态驱动的语音/人脸生成：从发音合成评估到 EMG 静默语音、从说话人脸到唇同步配音，再到 rtMRI 发音视频合成。核心问题是如何在缺少声学监督或部分模态缺失时，仍重建可懂、可编辑且身份一致的语音或面部运动。

视觉与人脸侧，工作从可编辑三维人脸重建、方言感知的人脸 TTS，到离散语音表征驱动的三维面部动画，再到用二值语音活动条件做唇同步配音。共同趋势是：用更轻、更可编辑的条件（几何—纹理解耦、方言音高、VAD、离散 token）替代或补充视频唇部轨迹。

肌电与发音侧，GETS 用静默语音识别语义引导扩散式 EMG→语音；SVA 用静默—有声平行 EMG 的多层次对齐缓解无真实语音标签；另有研究追问从舌超声等发音数据预测 f0 的信息来源，以及 rtMRI 说话人无关波形合成。特征设计与生成式建模在“补回反演丢失信息”与“合成结果是否仍代表估计的发音”之间形成方法论张力。

迁移学习角度上，音素添加研究表明：预训练更利于自然度，对新音素 PER 未必节省数据。整体上，本场把跨模态对齐、语义纠错与发音可解释性并列为静默/视觉语音系统的关键能力。

## 技术内容

### 语音合成迁移与人脸/方言条件生成

**Exploring Pre-training Benefits on Phoneme Addition through Fine-tuning in Speech Synthesis**（论文 208；Masato Murata）  
低资源 TTS 微调时常需“音素添加”。用 LLM 生成音素可控语料做仿真，并以英→日真实跨语种迁移验证。两设置均显示：微调自然度高于从头训练，但新音素达到可比 PER 所需数据并不更少。结论：预训练主要提升自然度，对音素添加帮助有限。

**ES-3DF: Editable Speech-Driven 3D Face Reconstruction via Geometry Texture Disentanglement**（论文 433；Ju Zhang）  
提出据称首个直接从语音重建可编辑带纹理三维人脸的框架。Disentangle 模块解耦 3DMM 几何与 UV 纹理；Dual-Branch Alignment 配合 Class-Aware Multi-Slot Memory Bank 与 Multi-Slot InfoNCE，动态对齐语音嵌入与说话人原型。实验称几何精度、身份保持与视觉质量优于 SOTA。

**K-DIALECT : Korean Dialect-Aware Face-Based Speech Synthesis**（论文 616；Seongyeon Yang）  
韩语多方言韵律与文化身份重要，但 TTS 多面向标准语；人脸 TTS 在参考音频稀缺时可用，方言韵律建模仍少。K-DIALECT 融合人脸编码器、方言条件音高预测器与 FiLM 融合。六种韩语方言实验称改进方言流利度、自然度与模态对齐。

**Not Quite My Tempo: Voice Activity-aware Speech Synthesis for Lip-Synchronous Dubbing**（论文 1407；Alejandro Pérez-González-de-Martos）  
唇同步配音需目标语语音/静音时序精确匹配源片。本文用二值语音活动信号条件化合成（表征轻、可多源生成），称能高精度跟随 VAD，同时保持自然韵律与句内合理停顿；训练时随机掩码使该条件在推理时可选用或放宽。

### 离散表征、发音合成与 MRI

**From Tokens to Faces: Investigating Discrete Speech Representations for 3D Facial Animation**（论文 1397；Pedro R. Corrêa）  
比较 SSL、神经 codec、ASR 式标签空间等四类语音表征在两种面部解码器上的重建与感知质量，并探测 token 与音素类、发音形变关系。发现编码音素类对准确面部动画有益；并引入以离散表征为共享空间的 AVTTS 管线，同时解码语音与三维面部运动。

**Feature Design and Generative Modelling in Deep Articulatory Synthesis**（论文 694；Charles McGhee）  
深度发音合成用于评估发音反演时，需补回反演丢失信息（显式特征或隐式生成）。但补回后合成语音可能不再代表估计的发音。工作系统比较不同特征输入与建模类型对输出的影响，强调若要通过合成结果对发音下结论，需审慎设计。

**Speaker-Independent Speech Synthesis from Real-time MRI Articulatory Data**（论文 3379；Yuto Otani）  
用 EfficientNetV2 逐帧特征、E-Branchformer 时序建模与 BigVGAN-v2，从 rtMRI 视频合成波形；经说话人嵌入跨模态训练实现仅依赖 rtMRI 的说话人无关合成。USC 75 人库上朗读语言准确度较好；F0 相关显示相对韵律可部分捕获，绝对 F0 仍难；说话人相似度在性别内区分困难但身份有一定再现。

**Automatic pitch prediction from speech articulation: Where does the f0 information come from?**（论文 1288；Beliz Ozkan）  
静默语音接口常从发音数据预测 f0，与源—滤波独立性假设冲突。多说话人数据表明仅舌超声即可部分预测 f0。四项假设检验：未见依赖舌/唇外特定结构或更长时上下文；孤立句训练难泛化到自发语音；对显著词的局部 f0—发音相关预测更准。感知实验支持：需真实会话数据，并侧重局部韵律功能而非全局 f0 轨迹。

### EMG 静默语音合成

**GETS: Guiding EMG-to-Speech Synthesis via Silent Speech Recognition**（论文 1938；Jiwon Lee）  
传统 ETS 语义可懂度不足。GETS 以 EMG 条件扩散生成，并用 SSR 语义引导；摘要称静默 EMG 测试集 WER 达 11.89% 的新 SOTA，在消歧不足指定 EMG 的同时保留时序对齐与能量等韵律特征。

**Enhancing EMG-to-Speech via Silent-Voiced Representation Alignment**（论文 2931；Jiwon Lee）  
静默 EMG 无真实语音标签且数据稀缺。提出 Silent-Voiced Alignment（SVA）损失，对语句平行的静默/有声 EMG 做多层次表征对齐。实验称显著增强内容重建，可嵌入现有 ETS 框架，并在统一评测协议下提升可懂度与稳健性。

## 本场要点

- 预训练对 TTS“音素添加”主要增益自然度，对新音素数据效率帮助有限。
- 语音驱动三维人脸趋向几何—纹理解耦与可编辑身份对齐。
- 低资源方言可用人脸 + 方言条件音高等轻量条件建模。
- EMG→语音靠 SSR 语义引导与静默—有声对齐补监督缺口。
- 从发音预测 f0 更宜关注局部韵律功能与会话数据，而非全局轨迹复制。
- 用合成评估发音反演时，特征与生成式补信息方式会改变“合成是否代表发音”的结论效度。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 208 | Exploring Pre-training Benefits on Phoneme Addition through Fine-tuning in Speech Synthesis |
| 433 | ES-3DF: Editable Speech-Driven 3D Face Reconstruction via Geometry Texture Disentanglement |
| 616 | K-DIALECT : Korean Dialect-Aware Face-Based Speech Synthesis |
| 694 | Feature Design and Generative Modelling in Deep Articulatory Synthesis |
| 1288 | Automatic pitch prediction from speech articulation: Where does the f0 information come from? |
| 1397 | From Tokens to Faces: Investigating Discrete Speech Representations for 3D Facial Animation |
| 1407 | Not Quite My Tempo: Voice Activity-aware Speech Synthesis for Lip-Synchronous Dubbing |
| 1938 | GETS: Guiding EMG-to-Speech Synthesis via Silent Speech Recognition |
| 2931 | Enhancing EMG-to-Speech via Silent-Voiced Representation Alignment |
| 3379 | Speaker-Independent Speech Synthesis from Real-time MRI Articulatory Data |
