# Multimodal Spoken Dialogue Systems

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral（Area 11）
- 论文数：6
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

本场多模态口语对话系统覆盖会话情感识别、机器人在线动作生成、音视频问答、自我中心“是否在对我说话”，以及 Speech LLM 与文本 LLM 的能力对齐。情感侧从不确定度感知融合（EmoEUS）到图结构多模态融合与情绪惯性/传染 GNN（MF-EDM），强调冲突线索、噪声与缺失模态下的动态加权，以及说话人内持久与跨说话人交互。

交互与具身场景要求流式处理：Plan and Double-Check 把 Q-Former 动作生成扩展到短时块音视频特征与左上下文 query，并增量生成动作与确认消息；VividAC 用视觉智能体生成查询相关视频描述，再引导听觉智能体产出视觉情境化音频描述，免音视频联合训练即可提升 AVQA。Ego4D TTM 工作则联合说话人感知对话上下文与 Looking-at-Me 视觉骨干。

系统层，X-OPD 以跨模态 on-policy 蒸馏让 Speech LLM 在自身分布上 rollout，由文本教师给 token 级反馈，缩小相对文本模型的能力落差。瓶颈包括模态不确定度、情绪动态、流式延迟、朴素音频描述损害 AVQA，以及 E2E Speech LLM 相对级联/文本模型的性能缺口。

## 技术内容

### 会话情感：不确定度与图动力学

**EmoEUS: Uncertainty Supervision for Multimodal Emotion Recognition in Conversation**（论文 1996；Zilong Huang）
指出 MERC 既有融合常忽略话语级模态特异不确定度。EmoEUS 用学到的方差估计动态加权模态，并以显式监督损失把预测方差与话语分布表示到情绪—模态簇中心距离对齐。在 IEMOCAP 与 MELD 上持续优于当时先进方法。

**MF-EDM: Graph-based Multimodal Fusion and Emotional Dynamics Modeling for Emotion Recognition in Conversation**（论文 1875；Sooyeon Hwang）
两阶段框架：Intra-Utterance Graph 以早融合多模态锚点节点做结构化跨模态消息传递；再以 Emotional Inertia GNN 建模说话人内情绪持久，Emotional Contagion GNN 建模跨说话人交互。摘要报告在 IEMOCAP、MELD、K-MIND、M3ED 上达到当时最优加权 F1/准确率数值。

### 流式具身交互与音视频问答

**Plan and Double-Check: Streaming Multimodal Q-Former for Online Robot Action Generation**（论文 2999；Chiori Hori）
将基于 Q-Former 的机器人动作生成扩展到未切分多模态流：从短时块提取音视频特征，把左上下文纳入 query embedding，由 LLM 增量生成动作序列与确认消息；通过注意力掩码设计可并行训练。实验称流式方案低延迟，相对离线准确率下降不到 10%。

**VividAC: Visually Informed and Visually Interacted Audio Captioning for Enhancing Audio-Visual Question Answering**（论文 3442；Mingi Kim）
发现朴素音频描述常因缺少任务相关细节且与视觉场景不一致而损害 AVQA。VividAC 让 Visual Agent 生成查询相关视频描述，再引导 Audial Agent 产生视觉情境化音频描述，全程自然语言通信、无需音视频联合训练。在 MUSIC-AVQA 上超过最强端到端 Audio-Visual LLM 7.0%p，并在 11/12 组 LLM-VLM 组合上一致增益。

**Who is Talking to Me? Addressing Egocentric TTM with Speaker-aware Conversational Context**（论文 2358；Fukun Chen）
针对自我中心 Talking-to-Me 任务中多说话人长程语义依赖，提出联合说话人感知多轮对话语义依赖与注视感知视觉线索的框架：说话人感知语音嵌入 + 对话上下文建模，并辅以 LAM 导向视觉骨干。在 Ego4D TTM 基准上显著优于既有基线。

### Speech LLM 能力对齐

**X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLMs**（论文 861；Di Cao）
指出 E2E Speech LLM 相对文本模型常有显著性能落差，且标准 SFT/RL 难以弥合。X-OPD 让 Speech LLM on-policy rollout，由文本教师评估轨迹并提供 token 级反馈，将教师能力蒸馏进学生多模态表示。多基准实验称在复杂任务上显著缩小差距并保留固有能力。

## 本场要点

- 会话情感识别正同时处理模态不确定度加权与情绪惯性/传染等交互动力学。
- 具身对话要求流式 Q-Former/LLM 动作生成，并接受小幅准确率换低延迟。
- AVQA 可受益于“视觉引导的音频描述”，而非无条件音频 caption。
- 自我中心 TTM 需要说话人身份化对话上下文与注视线索联合建模。
- Speech LLM 与文本 LLM 的缺口可用跨模态 on-policy 蒸馏系统对齐。
- 免联合训练的智能体自然语言协作成为多模态系统集成的 pragmatic 路径。

## 覆盖核对

- 1996 | EmoEUS: Uncertainty Supervision for Multimodal Emotion Recognition in Conversation
- 1875 | MF-EDM: Graph-based Multimodal Fusion and Emotional Dynamics Modeling for Emotion Recognition in Conversation
- 2999 | Plan and Double-Check: Streaming Multimodal Q-Former for Online Robot Action Generation
- 3442 | VividAC: Visually Informed and Visually Interacted Audio Captioning for Enhancing Audio-Visual Question Answering
- 2358 | Who is Talking to Me? Addressing Egocentric TTM with Speaker-aware Conversational Context
- 861 | X-OPD: Cross-Modal On-Policy Distillation for Capability Alignment in Speech LLMs
