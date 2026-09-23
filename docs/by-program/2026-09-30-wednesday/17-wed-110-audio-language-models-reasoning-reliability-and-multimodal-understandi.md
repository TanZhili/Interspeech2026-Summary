# Audio Language Models: Reasoning, Reliability, and Multimodal Understanding

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：12
- 论文数：10
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场审视音频语言模型的推理、可靠性与多模态理解：位置偏差、训练无关隐状态转向、多音频理解瓶颈、噪声下的工具检索、语音–文本检索重排、口语指令数据集、基准中的文本先验泄露、唤醒词半监督难负例、跨模态不稳定性，以及决策级可靠性融合是否真正被使用。共同警示是：高分不一定等于真正“听见”。

评测诊断显示选项顺序可造成高达约 24% 的性能波动；无音频输入仍可保留满分的约 60–72%；多音频输入随并发数急剧下降。缓解手段包括排列自洽、隐状态转向、LLM 合成查询嵌入转向、语音文本重排器，以及口语提示基准 DOWIS。可靠性还延伸到唤醒词自适应难负例生成与跨语/跨模态三元组不稳定性度量。

## 技术内容

### 偏差、转向与多音频理解

**Hearing the Order: Investigating Position Bias in Large Audio-Language Models**（论文 1025；Yu-Xiang Lin）  
六模型、三基准及其口语版本显示位置偏差普遍存在；打乱选项顺序性能波动最高约 24% 并可改变模型排名。排列策略在多数情形可缓解偏差。

**Nudging Hidden States: Training-Free Model Steering for Chain-of-Thought Reasoning in Large Audio-Language Models**（论文 554；Chih-Kai Yang）  
三种推理时转向策略跨四模型四基准相对 CoT 最高准确率增益约 4.4%；文本少样本导出的转向向量可有效引导语音推理，显示高数据效率。

**MUGEN: Evaluating and Improving Multi-audio Understanding of Large Audio-Language Models**（论文 530；Chih-Kai Yang）  
覆盖语音、通用音频与音乐的多音频基准。性能随并发音频数急剧下降。Audio-Permutational Self-Consistency 最高约 +6.28% 准确率，结合 CoT 约 +6.74%。

### 检索编排、口语指令与评测诊断

**From Noisy Speech to Accurate APIs: LLM-driven Embedding Steering for Resilient Tool Retrieval**（论文 3291；Rama Doddipatla）  
训练无关离线方法：LLM 为每工具生成多样用户风格合成查询/任务/场景并平均（转向）嵌入。在混响与加性噪声再 ASR 的条件下，多嵌入模型与工具集上提升检索可靠性且无需重训。

**A Reranker for Orchestrating Heterogeneous Speech and Text Retrievers**（论文 2154；Inho Kim）  
STEREO 重排异构语音与文本检索结果；先构建含查询、混合模态证据与相关性排序的数据集再训练。单模态与混合模态场景下摘要称能选出最相关证据并显著改善下游问答。

**Do What I Say: A Spoken Prompt Dataset for Instruction-Following**（论文 685；Maike Züfle）  
DOWIS：9 任务、11 语言的真人录制口/书面提示，每任务–语言五风格共 10 变体，可与既有基准配对。摘要称文本提示总体优于口语，低资源与跨语差距更大；仅当任务输出为语音时口语提示缩小差距。

**All That Glitters Is Not Audio: Rethinking Text Priors and Audio Reliance in Audio-Language Evaluation**（论文 913；Chih-Kai Yang）  
双轴诊断：文本先验（仅文本与常识可答性）与音频依赖。八模型三基准无音频仍保留满分约 60–72%；需音频的题目中仅约 3.0–4.2% 需要完整片段，多数局部片段即可。

### 唤醒词、跨模态稳定与融合诊断

**ADALA: A Wake-up Word Detection Framework Based on Adaptive Semi-supervised learning and Large Language Model**（论文 493；Nianhang Tang）  
RL 微调 LLM 动态生成难负例，并与真实数据半监督增强 WUW。音近词集上摘要称误激活率 3.19%、唤醒率 90.43%，取得更优均衡。

**Said Aloud, Read Different: Cross-Modal Instability in Multimodal Models**（论文 1980；Nadir Durrani）  
语音增强视觉对比三元组基准：10,150 张来自 18 个 MENA 国家的文化扎根图像。对比不稳定性度量显示模态（文/语音）与语言（英/阿）切换引入显著三元组级不一致，语音放大部分失败，且不完全被总体准确率捕捉。

**When Does Quality-Aware Multimodal Fusion Matter? A Leakage-Safe Diagnostic for Decision-Level Dependence**（论文 2989；Jaden Moon）  
训练后固定模型与输入，置换测试样本的可靠性分数：若决策依赖这些分数则性能应下降。StressID 与 CMU-MOSEI 上置换后性能不变，尽管每例选最佳模态有潜在增益；正对照中同一冻结融合规则可显著改进，表明仅当可靠性信号可靠预测单模态正确性时才影响融合决策。

## 本场要点

- LALM 普遍存在位置偏差，可动摇排行榜可靠性。
- 训练无关隐状态转向可小幅提升 CoT 推理，并存在跨模态迁移。
- 多音频理解随输入规模急剧变差，排列自洽有帮助。
- 基准常被文本先验主导，无音频仍可得高分。
- DOWIS 推动用口语指令而非仅文本提示评测 SLLM。
- 工具检索嵌入转向、唤醒词难负例与融合诊断共同强调部署可靠性。

## 覆盖核对

| id | title |
|---|---|
| 1025 | Hearing the Order: Investigating Position Bias in Large Audio-Language Models |
| 554 | Nudging Hidden States: Training-Free Model Steering for Chain-of-Thought Reasoning in Large Audio-Language Models |
| 530 | MUGEN: Evaluating and Improving Multi-audio Understanding of Large Audio-Language Models |
| 3291 | From Noisy Speech to Accurate APIs: LLM-driven Embedding Steering for Resilient Tool Retrieval |
| 2154 | A Reranker for Orchestrating Heterogeneous Speech and Text Retrievers |
| 685 | Do What I Say: A Spoken Prompt Dataset for Instruction-Following |
| 913 | All That Glitters Is Not Audio: Rethinking Text Priors and Audio Reliance in Audio-Language Evaluation |
| 493 | ADALA: A Wake-up Word Detection Framework Based on Adaptive Semi-supervised learning and Large Language Model |
| 1980 | Said Aloud, Read Different: Cross-Modal Instability in Multimodal Models |
| 2989 | When Does Quality-Aware Multimodal Fusion Matter? A Leakage-Safe Diagnostic for Decision-Level Dependence |
