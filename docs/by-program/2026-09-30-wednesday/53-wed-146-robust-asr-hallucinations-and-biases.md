# Robust ASR: Hallucinations and Biases

- 日期：2026年9月30日（星期三）
- 时间：16:30-18:30
- 形式：Poster
- Area：8
- 论文数：9
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场主题是稳健 ASR：幻觉检测与缓解、群体偏见、儿童/老年等困难域，以及多说话人场景下的识别与说话人归属。共同背景是大模型 ASR（尤其 Whisper 系）在静音、非语音与长尾实体上仍会“流利地错”，且微调数据配比未必能纠正预训练已固化的偏差。

幻觉研究从内部谱动力学理论（分散→吸引子相变）、解码器中间层探测，到无需改模型的音频锚输入技巧，形成“理论—检测—推理时缓解”链条。专有名词则走 ASR 后处理多视角音素—语义检索接地。偏见与域方面，性别组成实验强调预训练掩盖微调配比效应；儿童零样本 SSL 层误差结构显示问题在声学表征而非可恢复语言不一致；WildElder 提供野外中文老年语料基准。

多说话人侧，端到端 LLM 需在有限真实数据下平衡 ASR 与 diarization；另一工作用说话人切换 token 掩码，使性能不随训练中未见的切换次数崩塌。整体趋势是：稳健性越来越多地被当作可诊断、可接地、可与说话人建模联合优化的系统问题。

## 技术内容

### 幻觉机理、检测与缓解

**From Dispersion to Attraction: Spectral Dynamics of Hallucination Across Whisper Model Scales**（论文 1420；Ivan Viakhirev）  
提出 Spectral Sensitivity Theorem，预测深层网络由分散区（信号衰减）到吸引子区（秩-1 坍缩）的相变。对 Whisper Tiny 至 Large-v3-Turbo 在对抗压力下做激活图特征谱分析：中等规模呈结构解体（交叉注意力秩坍缩约 13.4%），大模型进入压缩吸引态（自注意力秩约 −2.34%），谱斜率硬化并与声学证据解耦。

**From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection**（论文 338；Jan Jasiński）  
在真实语音人工标注上比较文本指标、LLM 与解码器内部状态探测。文本分类高召回但无参考会退化；领域提示 LLM 提精但不敌轻量文本法；无参考探测 Whisper 解码器表示效果最强，显示幻觉特质编码于中间解码层；文本+内部状态晚融合最佳。

**Grounding Whisper: An Audio Anchor-Based Approach for Hallucination Mitigation and Throughput-Efficient ASR**（论文 1314；Saurabh Kumar）  
对静音/非语音幻觉，在输入前拼接近零域出现的短“锚音频”，无需改模型即可检测幻觉。评估单次增强到批拼接自动回退等五种推理策略；批策略利用固定 30 秒窗拼接短句并由锚校验。摘要称整体 WER 从 32.18% 降至 13.23%，非语音幻觉错误率 0.14%，时延可比基线 VAD 管线。

### 偏见、困难域与实体接地

**Gender Bias in ASR: A Controlled Study of Gender Composition Across Training Paradigms**（论文 3047；Seshan S）  
在三套预训练模型与 0–100% 女性占比的 11 组划分上微调，男女 WER 波动无一致方向；对照从头训练系统则随组成呈方向性差距变化。结论：效应真实，但被大规模预训练表征掩盖；仅平衡微调数据不足以缓预训练 ASR 的性别差距。

**Error Diversity and Performance Variability in Zero-Shot Children's Speech Recognition**（论文 2666；Abhijit Sinha）  
严格成人→儿童零样本下，评估 Wav2Vec2/HuBERT/Data2Vec 各层混合 ASR。最佳 WER 相近但表征间变异大；误差结构依赖数据集；LLM 后纠几乎无助；oracle 显示层间互补尤其在强域失配时。结论：错误主要由声学表征局限驱动，而非可恢复语言不一致。

**WildElder: A Chinese Elderly Speech Dataset from the Wild with Fine-Grained Manual Annotations**（论文 102；Hui Wang）  
发布自在线视频采集、含转写/年龄/性别/口音强度细粒度标注的普通话老年语料，兼顾野外真实性与专家整理，服务 ASR 与说话人画像。实验揭示老年识别难点并定位为具挑战基准；数据与代码已开源。

**Post-ASR Proper Noun Grounding via Multi-View Phonetic and Semantic Retrieval**（论文 907；Pranshu Nema）  
不重训 ASR，将噪声专有名词提及链接到预定义词表候选：细粒度 G2P、粗粒度 Soundex 与上下文语义嵌入，归一化分数融合。相对精确匹配，Whisper-large-v3 与 Qwen3-ASR-1.7B 的 Recall@1 分别提升 36.4 与 23.6 个百分点，达 74.67% 与 59.82%，最强配置 Recall@10 达 87.36%。

### 多说话人 ASR 与归属

**Balancing ASR and diarization in end-to-end LLMs for multi-talker speech recognition**（论文 1124；Naijun Zheng）  
有限真实数据下训练 LLM 多说话人系统：双编码器抽语义与说话人特征、特征交错送入 LLM、长度感知说话人 ID 损失、重叠区 ASR 损失自适应阈值以抑幻觉。相对开源基线，AliMeeting / Aishell4 相对提升约 18% / 24%。

**Multi-Talker ASR Unaffected by Speaker Change Count**（论文 1582；Naoki Makishima）  
自回归多说话人 ASR 依赖含切换 token 的拼接转写，训练中未见更多切换时易退化。引入自注意力中的说话人切换 token 掩码，将切换 token 及随机被其他查询引用的 token 值置零，使模型无法从上下文推断切换次数。实验验证该方法有效。

## 本场要点

- Whisper 幻觉与尺度相关的谱相变、解码器中间层可探测性相关。
- 输入级音频锚可在不改模型下抑制非语音幻觉并兼顾吞吐。
- 预训练 ASR 的性别差距难以靠微调数据配比单独纠正。
- 儿童零样本误差更偏声学表征；老年野外语料补中文困难域缺口。
- 专有名词可用多视角音素—语义后处理接地。
- 多说话人 LLM 需显式平衡 ASR/diarization；切换次数鲁棒需掩码等结构干预。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 102 | WildElder: A Chinese Elderly Speech Dataset from the Wild with Fine-Grained Manual Annotations |
| 338 | From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection |
| 907 | Post-ASR Proper Noun Grounding via Multi-View Phonetic and Semantic Retrieval |
| 1124 | Balancing ASR and diarization in end-to-end LLMs for multi-talker speech recognition |
| 1314 | Grounding Whisper: An Audio Anchor-Based Approach for Hallucination Mitigation and Throughput-Efficient ASR |
| 1420 | From Dispersion to Attraction: Spectral Dynamics of Hallucination Across Whisper Model Scales |
| 1582 | Multi-Talker ASR Unaffected by Speaker Change Count |
| 2666 | Error Diversity and Performance Variability in Zero-Shot Children's Speech Recognition |
| 3047 | Gender Bias in ASR: A Controlled Study of Gender Composition Across Training Paradigms |
