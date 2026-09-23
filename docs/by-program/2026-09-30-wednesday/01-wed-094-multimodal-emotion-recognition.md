# Multimodal Emotion Recognition

- **日期**：Wednesday 30 September 2026
- **时间**：09:00-11:00
- **形式**：Oral
- **Area**：3
- **论文数**：6
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场从类别/维度情感识别扩展到比较推理、风格语言—音频预训练、纵向日志情感推断，以及视觉副语言与时间变化的模态门控。LALM 被训练做成对话语上的唤醒/效价/支配比较，并用语义描述与 GeMAPS 声学证据生成可解释推理轨迹。合成爱尔兰盖语嗓音实验则检验视听通道在情感感知中的相对作用。

表征侧 ParaSpeechCLAP 用双编码器覆盖更丰富的内禀与情境风格描述，并可用于风格提示 TTS 的推理时奖励。纵向语音日记显示群体层面语言学模型远强于声学，但个体日常监测仍需个性化。视觉微姿态通过运动引导空间去噪提升信噪比；情感识别中模态重要性被显式建模为随时间与类别变化的动态过程。

## 技术内容

### 比较情感推理与视听感知

**Comparative Reasoning: Making an Audio Language Model Better at Comparing Emotions**（论文 2935；Abinay Reddy Naini）  
研究 LALM 能否在成对语音上沿情感等维度做比较判断。提出推理引导序数 SER：以成对语音为条件，用语义音频描述与 GeMAPS 声学证据生成推理轨迹，并用 DPO 鼓励情绪差异分离。摘要称偏好预测改进，且仅用传统序数 SER 约 5% 训练数据。

**Exploring the effect of the visual channel in vocal expression of affect in an Irish (Gaelic) synthetic voice**（论文 1363；Ailbhe Ní Chasaide）  
声源修改合成愤怒/快乐/悲伤/无聊/放松等目标情感，与匹配/对立/无视觉脸部表情组合做感知实验。摘要称“一致视觉增强目标情感”假设支持有限，提示嗓音通道主导；但对立刺激凸显视觉重要性；视觉有助于高/低激活状态间更好分辨的假设大体成立。

### 风格对齐预训练与纵向情感推断

**ParaSpeechCLAP: A Dual-Encoder Speech-Text Model for Rich Stylistic Language-Audio Pretraining**（论文 1437；Anuj Diwan）  
双编码器将语音与文本风格字幕映射到共享嵌入，覆盖音高、质感、情绪等内禀与情境描述。训练专用 Intrinsic/Situational 与统一 Combined 模型；摘要称专用模型在单维更强、统一模型在组合评测更优，并可作风格提示 TTS 推理时奖励，多数指标优于基线。

**Daily Affect Inference from Longitudinal Speech-based Journals: A Comparison of Acoustic and Linguistic Models**（论文 2383；Michelle D Schlicher）  
61 说话人、769 段日常录音，标注多维心情与知觉压力。比较 eGeMAPS、wav2vec2 与 GBERT、零样本 Mistral。摘要称群体层面语言学明显占优，声学近零；Mistral 更偏特质差异而非日常个体变化；说话人层面停顿变异与效价有关。结论是当前模型个体监测能力有限，需要个性化。

### 视觉副语言与时间动态融合

**Enhancing Visual Paralinguistics: Motion-Guided Spatial Denoising for Non-Verbal Interaction Analysis**（论文 868；Junjie Wan）  
MG-SRM 用多阶时间差分过滤姿态热图静态背景伪影，CLF 按动作语义自适应模态权重。在 MA-52 上摘要称达 SOTA，直接提升微运动信噪比，服务多模态会话系统视觉前端。

**Modality Importance is Not Static: Temporal Dynamics via Gating in Multimodal Emotion Recognition**（论文 1399；Jiyeon Ryu）  
将模态重要性建模为时间变化、类别条件分布，用 GRU 情绪查询门控随对话语境调节权重。在 6 类 IEMOCAP LOSO 上摘要称时间建模优于静态融合，门控再进一步提升，并以扰动遮挡与 AOPC 证明模态重要性非平稳。

## 本场要点

- LALM 可通过推理轨迹与偏好优化学习成对情感比较。
- 合成嗓音情感感知中嗓音常主导，但对立视听条件凸显视觉作用。
- ParaSpeechCLAP 扩展风格字幕对齐，服务检索、属性分类与 TTS 奖励。
- 纵向日记情感推断在群体层依赖语言学，个体监测仍需个性化。
- 运动引导去噪提升微姿态视觉副语言；模态重要性应作时间动态过程建模。

## 覆盖核对

| id | title |
|---|---|
| 2935 | Comparative Reasoning: Making an Audio Language Model Better at Comparing Emotions |
| 1363 | Exploring the effect of the visual channel in vocal expression of affect in an Irish (Gaelic) synthetic voice |
| 1437 | ParaSpeechCLAP: A Dual-Encoder Speech-Text Model for Rich Stylistic Language-Audio Pretraining |
| 2383 | Daily Affect Inference from Longitudinal Speech-based Journals: A Comparison of Acoustic and Linguistic Models |
| 868 | Enhancing Visual Paralinguistics: Motion-Guided Spatial Denoising for Non-Verbal Interaction Analysis |
| 1399 | Modality Importance is Not Static: Temporal Dynamics via Gating in Multimodal Emotion Recognition |
