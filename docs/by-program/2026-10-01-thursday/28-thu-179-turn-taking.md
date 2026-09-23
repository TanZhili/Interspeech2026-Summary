# Turn-taking

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：11
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场把话轮转换从“静音超时/二元边界检测”推进到角色条件、前瞻预测、双通道生成预训练、以及模态消融下的信号贡献分析。生产级 ASR–LLM–TTS 流水线虽具备工具调用与推理能力，却常因静音启发式导致不自然打断；端到端语音模型更自然但工具链受限——多篇工作试图弥合这一鸿沟。

趋势一是把话轮建模为结构化决策或多动作输出（含基准 CoDeTT），覆盖场景与上下文变化。趋势二是前瞻：提前数秒预测终点或话轮边界，以投机执行 LLM/TTS 换延迟。趋势三是从运动学预发言线索与声学–韵律–语义消融理解“何为驱动因素”，摘要侧证据偏向韵律与静音胜过语义完备性。

## 技术内容

### 多方角色与决策基准

**Adaptive Turn-Taking for Real-time Multi-Party Voice Agents**（论文 2493；Soumyajit Mitra）提出 ModeratorLM：在多方设定中按显式角色条件话轮行为，基于分块流式语音大模型，并有结合上下文与角色的思维链式推理变体。构建含多样助手角色的合成多方口语数据 RolePlayConv。摘要称在真实会议与 RolePlayConv 上，相对非角色条件基线，话轮精度提升逾 40%、召回逾 70%，并显著降低假阳性打断。

**CoDeTT: A Context-Aware Decision Benchmark for Turn-Taking Evaluation**（论文 974；Huan Shen）认为现有评测碎片化且常限于狭窄设定下的二元边界检测。CoDeTT 将话轮转为结构化决策问题，构建含细粒度决策类别与受控上下文变化的多场景数据，在统一协议下评估代表性模型。摘要称不同决策类型与交互场景间存在显著性能差距，提供标准化、上下文感知的评测基准。

### 前瞻、双通道预训练与模态贡献

**Before the Turn: Investigating Motion Cues Preceding Speech in Dyadic Interaction**（论文 1243；Ying-Hsuan Huang）系统分析连续运动学对预测前置时间（lead time）的影响。在 InterAct 三维骨骼上用 Transformer，变化观察窗与 lead time。摘要称意图在独立时间线上运作：上身信号可在发言前至多 3.0 s 稳定预测；争抢话轮约 1.5 s 预备累积，而保持话轮则呈爆发式。强调异步多模态协调是主动话轮协商的核心原则。

**DualTurn: Learning Turn-Taking from Dual-Channel Generative Speech Pretraining**（论文 2424；Shangeth Rajaa）在双通道对话音频上生成式预训练：自回归生成双方未来音频、无标签学习对话动态，再微调为可映射到智能体动作的可解释话轮信号，持续监测双通道并输出五种动作。摘要称 0.5B 的 DualTurn 在智能体动作预测上 wF1 0.633 vs VAP 0.389，词级预测 AUC 0.930 vs 3.1B 音文模型 0.880，更早预判、更少打断，并可在 CPU 实时运行。

**Endpoint Anticipation for Low-Latency Spoken Dialogue**（论文 2196；Sathvik Udupa）将终点检测从反应式改为前瞻预测，语音模型可提前至多 2.56 s 预期终点，从而在部分上下文上投机执行 LLM 与 TTS。引入度量量化延迟收益与计算冗余权衡。摘要称跨会话与任务导向数据优于竞争性 VAP 基线；接入 Unmute 平均降延迟 505 ms，投机计算增 28.4%。

**Less can be More: What Aspects of Speech Drive End-of-Turn Detection**（论文 1705；Rini Sharon）用轻量三模态分类器对声学、韵律与语义做受控消融。相同训练条件下，声学–韵律组合在精度与延迟上最佳：utterance F1 0.93，400 ms 中位延迟下假警 7.8%；加入文本增加过早检测且无性能增益。特征空间分析显示韵律可分性最强、文本表征重叠大。摘要认为话轮主要由语调与静音模式传达，而非语义完备性。

## 本场要点

- 多方场景需要角色条件与流式语音 LLM，并可结合思维链推理。
- CoDeTT 推动从二元边界到结构化、多场景决策评测。
- 预发言运动学与 Endpoint Anticipation/DualTurn 共同指向“提前预测换延迟”。
- 双通道生成预训练可无标签学习对话动态后再映射智能体动作。
- 模态消融证据支持韵律+声学优于叠加文本做终点检测。
- 延迟–投机计算权衡成为可量化的系统指标。

## 覆盖核对

| id | title |
|---|---|
| 2493 | Adaptive Turn-Taking for Real-time Multi-Party Voice Agents |
| 1243 | Before the Turn: Investigating Motion Cues Preceding Speech in Dyadic Interaction |
| 974 | CoDeTT: A Context-Aware Decision Benchmark for Turn-Taking Evaluation |
| 2424 | DualTurn: Learning Turn-Taking from Dual-Channel Generative Speech Pretraining |
| 2196 | Endpoint Anticipation for Low-Latency Spoken Dialogue |
| 1705 | Less can be More: What Aspects of Speech Drive End-of-Turn Detection |
