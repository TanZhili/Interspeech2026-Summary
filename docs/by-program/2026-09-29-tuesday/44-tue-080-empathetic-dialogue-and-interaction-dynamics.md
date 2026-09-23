# Empathetic Dialogue and Interaction Dynamics

- **日期**：Tuesday 29 September 2026
- **时间**：16:30-18:30
- **形式**：Oral（含 Survey Talk）
- **Area**：11
- **论文数**：4（另有 Survey Talk 1 场，题目待公布）
- **材料说明**：依据官方程序与 ISCA 归档中的题名、作者、报告人、时段与摘要整理；未补充摘要未给出的指标、数据或机制。来源：[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)、[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)。

## 技术趋势

本场围绕共情式口语对话与互动动态展开：一方面用语音大模型（speech LLM）生成情感对齐的回复，另一方面从双人协作对话中估计认知负荷等交互状态。共同点是强调“听到什么情绪/状态”与“如何以合适韵律与语义回应”的闭环，而不仅是文本层面的礼貌或共情措辞。

在生成侧，工作从“会不会识别情绪”推进到“回复情绪方向是否正确”（情绪共识），以及在有限数据、可控计算预算下仍能理解用户语音中的情感线索。多代理框架则把感知、推理与合成解耦，并用韵律到语言的桥接稳住大模型推理，同时按需调用外部知识。

在交互分析侧，研究从受控实验室转向自然协作对话，关注轮替、重叠、参与不平衡等交互动力学特征与时间压力、心理负荷等主观维度的关联。整体趋势是：共情能力的评测与训练目标更细（方向正确性、韵律适宜性），系统架构更模块化（对比式思维链、多代理、数据管线），并对真实对话中的认知状态建模提出需求。

Survey Talk 时段（40 分钟）题目尚未公布，本摘要不对其内容作推测。

## 技术内容

### 共情语音大模型：情绪共识与少资源生成

**CE-CoT: A Contrastive Empathetic Chain-of-Thought Training Strategy for Improving Emotion Consensus in Empathetic Speech LLMs**（论文 1271；Jing-Han Chen）  
面向对话代理中情绪对齐回复的需求，指出既有工作偏重识别与主动性，却忽视方向正确性，即情绪共识（EC）。提出 Contrastive Empathetic Chain of Thought（CE-CoT），将回复分解为情绪识别、中性回复与情绪对齐修订，以支持隐式对比训练。摘要称在四个数据集与多种 speech LLM 上 EC 一致提升，并给出相对基线的增益示例。

**Empathy Omni: Enabling Empathetic Speech Response Generation Through Large Language Models**（论文 984；Guangyan Zhang）  
指出多数模型只把回复内容转成语音，未充分捕捉用户语音中的情感线索，且共情 speech LLM 常依赖大规模数据与高算力。提出 Emotion Omni / Empathy Omni，理解用户语音情绪并生成共情回复，并构建约 200k 情感对话数据管线。摘要称在无大规模预训练条件下指令跟随能力可比，且在语音质量与共情上优于既有模型。

### 多代理韵律推理与双人交互中的认知负荷

**PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken Dialogue**（论文 1214；Wen Zhang）  
共情口语对话需要语义合适且韵律情感对齐；级联管线在 ASR 中丢失声学线索，端到端模型又缺乏可解释的情绪与知识控制。PRISM 将语音感知、回复生成与语音合成解耦为协调组件，引入韵律到语言的翻译机制稳定 LLM 推理，并支持按需调用外部知识工具。摘要称在共情、韵律适宜性与文本回复质量的主客观指标上均有一致改进。

**Predicting Cognitive Load from Speech and Interaction Dynamics in Dyadic Conversations**（论文 3052；Tahiya Chowdhury）  
认知负荷估计多在受控实验室，自然协作对话中的可靠性仍不足。分析 53 对双人、九项协作任务的音频，提取静态声学、动态与交互特征，用双头 GRU 编码器预测认知负荷分数。摘要称交互信号有助于预测时间压力、脑力工作、努力与任务表现相关负荷；时间需求与重叠、换说话人等轮替动态相关，心理需求与说话参与不平衡相关。

### Survey Talk（待公布）

**To be announced (Survey Talk, 40 mins)**（论文 id 未给出；presenter 未给出）  
程序安排 16:30–17:10 Survey Talk，题名与摘要尚未公布，此处不作技术推断。

## 本场要点

- 情绪共识（回复情绪方向与说话人状态是否匹配）成为共情 speech LLM 的显式训练与评测目标。
- 对比式思维链（识别—中性回复—情绪修订）用于隐式对比训练，以提升 EC。
- Empathy Omni 强调有限数据、免大规模预训练条件下的共情语音回复与配套情感对话数据管线。
- PRISM 用多代理解耦感知/生成/合成，并以韵律—语言桥接与按需知识调用强化可解释控制。
- 自然双人协作对话中，轮替与参与结构等交互动力学可预测多维认知负荷。
- Survey Talk 内容待官方更新后再补全。

## 覆盖核对

| id | title |
|---|---|
| （Survey Talk） | To be announced (Survey Talk, 40 mins) |
| 1271 | CE-CoT: A Contrastive Empathetic Chain-of-Thought Training Strategy for Improving Emotion Consensus in Empathetic Speech LLMs |
| 984 | Empathy Omni: Enabling Empathetic Speech Response Generation Through Large Language Models |
| 1214 | PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken Dialogue |
| 3052 | Predicting Cognitive Load from Speech and Interaction Dynamics in Dyadic Conversations |
