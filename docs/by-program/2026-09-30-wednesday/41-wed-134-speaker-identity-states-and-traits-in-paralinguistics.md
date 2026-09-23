# Speaker Identity, States, and Traits in Paralinguistics

- 日期：2026年9月30日（周三）
- 时间：16:30-18:30
- 形式：Oral
- Area：3
- 论文数：6
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。仅依据摘要表述，不补写未给出的实验细节。

## 技术趋势

本场连接说话人身份、人格特质、情绪状态与副语言感知：从有声书叙述吸引力、人格语料升级，到对话熟悉化对声音识别偏差的影响，再到隐私约束下的多模态对话情绪识别，以及 Speech LLM 中身份先验与可控 TTS 挖苦韵律线索。

共性是：副语言判断不仅取决于声学，还取决于体裁/标题、语言理解、对话语境，以及提示中注入的身份描述。方法上同时出现语料发布、图网络隐私过滤、prompt 控制评测与因果韵律操控实验。

## 技术内容

### 叙述吸引力、人格语料与对话熟悉化

**Audio-Based Understanding of Audiobook Narration Appeal**（论文 453；Shahar Elisha）  
从 LibriVox 提取音色、语速、响度等特征，分析其与消费数据（浏览率）及体裁、书名的关系。摘要称在控制书名效应后，声学信息仍与吸引力稳健相关，并用更细粒度专有参与度指标进一步验证；据称是首次系统计算研究叙述质量、体裁、书名与有声书消费的关联。

**The SSPNet Speaker Personality Corpus Version 2: Investigating the Role of Language Understanding in Automatic Personality Perception**（论文 383；Alessandro Vinciarelli）  
发布 SSPNet Speaker Personality Corpus V2：全量转写、100 分制标注，并分懂/不懂录音语言的两组评分者。摘要称支持多模态方法、回归设定，以及语言理解对人格感知影响的研究，并提供可复现单模态/多模态基线。

**Learning speaker identities in dialogue: Conversational familiarisation modulates response bias and confidence in voice recognition**（论文 1174；Tianze Xu）  
200 名英语被试听连贯四说话人对话或打乱版，并被指示关注身份、内容或无特定焦点，随后做旧/新声音识别。摘要称无主效应，但熟悉化刺激与真值交互：对话熟悉化提高对旧说话人的识别与信心，同时也提高把新说话人误判为旧的倾向，显示响应偏差变化。

### 隐私情绪识别、LLM 身份先验与挖苦韵律

**Speaker-Filtered Heterogeneous Graph Network: Toward Privacy-Preserving Multimodal Emotion Recognition**（论文 2282；heying song）  
SF-HGN 将图传播限制在单说话人诱导子图以维护说话人级隐私，并用 CAGI 在严格因果窗口内以三模态注意力提取跨说话人情绪线索。摘要称在 IEMOCAP 与 MELD 上验证有效，避免暴露非目标说话人特征与未来信息泄漏。

**Hidden Priors in Speech LLMs: Speaker Identity Shapes Emotional Perception**（论文 1238；Hsing-Hang Chou）  
固定话语仅改变提示中注入的口音/国家/语言描述，在 MSP-Podcast 与 BIIC-Podcast 上观察多种 Speech LLM。摘要称身份文本 alone 即可造成统计可靠的情绪预测差距；显著性分析显示身份驱动预测转变常伴随音频 token 段声学关注变化；并用轻量 LoRA 与两种提示策略降低敏感性。

**What Makes Synthetic Speech Sound Sarcastic? A Prosody-Controlled Perception Study**（论文 1487；Shekhar Nayak）  
用可提示韵律条件的神经 TTS 正交操控语速、音高变化与响度，比较人类与基础模型对挖苦的判断。摘要称人类挖苦感知主要由响度驱动，而模型更看重语速，行为对齐有限；展示可控 TTS 用于因果检验韵律线索权重的价值。

## 本场要点

- 有声书吸引力可部分由叙述声学解释，且与体裁/书名交织。
- 人格语料升级使语言理解效应与多模态回归成为可检验问题。
- 对话语境熟悉化会系统性改变声音识别偏差与信心。
- 多模态情绪识别开始显式加入说话人过滤与因果隐私约束。
- Speech LLM 情绪判断受提示身份先验影响；挖苦感知的人类—模型韵律权重并不一致。

## 覆盖核对

- 453 | Audio-Based Understanding of Audiobook Narration Appeal
- 383 | The SSPNet Speaker Personality Corpus Version 2: Investigating the Role of Language Understanding in Automatic Personality Perception
- 1174 | Learning speaker identities in dialogue: Conversational familiarisation modulates response bias and confidence in voice recognition
- 2282 | Speaker-Filtered Heterogeneous Graph Network: Toward Privacy-Preserving Multimodal Emotion Recognition
- 1238 | Hidden Priors in Speech LLMs: Speaker Identity Shapes Emotional Perception
- 1487 | What Makes Synthetic Speech Sound Sarcastic? A Prosody-Controlled Perception Study
