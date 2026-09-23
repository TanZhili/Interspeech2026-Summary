# Spoken Dialogue Systems

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Poster
- **Area**：11
- **论文数**：8
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场覆盖口语对话系统的交互质量建模、反馈通道时机、呼叫中心上下文 ASR、全双工视听生成，以及主动语音代理评测与噪声下系统输出语言复杂度。系统无关交互质量特征在端到端微调后可逼近系统依赖日志特征，提升跨系统可扩展评测。

反馈通道预测强调停顿邻近介入与语义适宜性：声学 alone 易过预测，需融合部分 ASR 假设；双路径模型则按快/慢功能类别分离时机。上下文侧区分“内部已感知历史”与“解码是否遵循”，并用上下文感知解码放大关键历史轮次；呼叫中心则用紧凑上下文投影器替代原始历史拼接。

## 技术内容

### 交互质量、反馈通道与呼叫中心上下文

**A System-Agnostic Approach to Modelling Interaction Quality in Spoken Dialogue Systems**（论文 1152；Paul Gering）  
用声学、文本与时间特征建模交互质量，对比系统依赖与系统无关特征。摘要称静态管线中 SD 更优，但端到端微调后 SA 可达可比表现，作为跨系统可扩展替代。

**Considerate Listener Modeling for Korean Streaming Backchannel Prediction**（论文 1854；Yong-Seok Choi）  
体贴倾听者在停顿邻近区域介入，但并非所有停顿适合反馈通道。零前瞻流式预测结合停顿感知软缩放与 Q-Former 融合部分 ASR 假设，并引入 Semantic FDR。在韩语咨询语料上摘要称显著降低 Semantic FDR 并提升 Macro-F1。

**DP-BCT: A Dual-Path model for predicting BackChannel Timing**（论文 3216；Jin Yea Jang）  
用 Cox 分析确认不同功能类别相对 BOP 的时延分布差异，据此将快/慢组合入双路径做帧级起始与功能类别预测。在 K-MIND 上摘要称 Macro-F1 相对单路径基线提升。

**Context Projector: Complementary Keyword and Dialogue Context Embeddings for LLM-based ASR**（论文 3326；Sergio Burdisso）  
把历史轮次编码为紧凑上下文 token，并辅以自动关键词；骨干冻结仅训投影模块。在真实多域呼叫中心数据上摘要称相对朴素原始上下文提示，总体与偏置词错误率均有相对下降。

### 上下文遵循、主动性、视听全双工与噪声可懂度

**From Awareness to Adherence: Bridging the Context Gap in Spoken Dialogue Systems via Context-Aware Decoding**（论文 1589；Che Hyun Lee）  
指出潜在上下文感知与主动遵循之间的鸿沟：参数先验在解码时掩盖历史信号。音频适配 CAD 用内部注意隔离关键历史轮次，对比有无关键上下文的输出分布以放大多模态上下文。在 Audio MultiChallenge 上摘要称语义记忆与自我连贯子任务显著改进。

**From Reactive to Proactive: Assessing the Proactivity of Voice Agents via ProVoice-Bench**（论文 1160；Yuhao Wang）  
提出面向主动语音代理的 ProVoice-Bench（四项新任务，1182 样本）。对 SOTA 多模态 LLM 评估显示过触发与推理能力存在明显差距。

**Integrating Facial Generation into Full-Duplex Spoken Dialogue Systems**（论文 3114；Jingjing Jiang）  
Moshi-Face 用 VQ-VAE 脸部编解码把 3D 头网格编为离散 face tokens，再以 Face Transformer 非自回归生成，实现用户音视频输入下的实时语音与面部运动联合生成。摘要称低延迟视听对齐并保持原音频模型对话质量。

**Optimal Linguistic Complexity for Dialogue System Speech in Noise: Convergent Evidence from Automatic and Human Transcription**（论文 2799；Lubos Marcinek）  
大规模合成话语 ASR 与人类听写试点均呈 U 形：自然语法句（约 9–16 词）优于电报式简化；语法优势在条件改善时反而增大。摘要据此拒绝自适应过度简化，并给出系统输出词数建议区间。

## 本场要点

- 系统无关交互质量特征经微调可接近系统依赖方案。
- 反馈通道需停顿时机 + 语义适宜性；快/慢功能路径可分建模。
- 呼叫中心 LLM-ASR 宜用紧凑上下文投影与关键词，而非原始历史拼接。
- 上下文感知解码弥合“知道历史”与“遵循历史”的差距。
- ProVoice-Bench 暴露主动代理过触发与推理短板。
- 全双工可扩展到同步面部；噪声下系统输出宜保持自然语法复杂度。

## 覆盖核对

| id | title |
|---|---|
| 1152 | A System-Agnostic Approach to Modelling Interaction Quality in Spoken Dialogue Systems |
| 1854 | Considerate Listener Modeling for Korean Streaming Backchannel Prediction |
| 3326 | Context Projector: Complementary Keyword and Dialogue Context Embeddings for LLM-based ASR |
| 3216 | DP-BCT: A Dual-Path model for predicting BackChannel Timing |
| 1589 | From Awareness to Adherence: Bridging the Context Gap in Spoken Dialogue Systems via Context-Aware Decoding |
| 1160 | From Reactive to Proactive: Assessing the Proactivity of Voice Agents via ProVoice-Bench |
| 3114 | Integrating Facial Generation into Full-Duplex Spoken Dialogue Systems |
| 2799 | Optimal Linguistic Complexity for Dialogue System Speech in Noise: Convergent Evidence from Automatic and Human Transcription |
