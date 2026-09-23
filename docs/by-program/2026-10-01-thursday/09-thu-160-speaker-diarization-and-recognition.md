# Speaker Diarization and Recognition

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Long Oral
- Area：跨领域长文口头报告（Cross-area）
- 论文数：5（含 1 场 Survey Talk）
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场聚焦说话人日志与识别（SDR）及说话人中心建模：从“单一嵌入难以通吃多任务”的综述视角，到 Speech-LLM 端到端联合预测说话人、文本与时间戳，再到边界紧致化、重叠语音的 shuffle 建模，以及语音语言模型流水线中的后门传播分析。

统一表示与任务自适应之间的张力贯穿综述与系统论文：嵌入在验证、日志、目标说话人提取与个性化交互中被不同方式利用，声学、内容、时长与域变化共同塑造鲁棒性。工程上，级联系统的误差累积与许多 E2E 模型缺乏细粒度时间对齐，推动 FIFO 式自回归输出与合成—微调两阶段数据策略。

日志边界与重叠处理是另一主线：对话 ASR 标注偏“松”导致模型复现松散边界；因果—反因果一致性可从松标注逼近紧边界。重叠方面，shuffle 积与偏序有限状态自动机在子词/词/短语层边缘化所有串行化，并直接建模（token, speaker）元组，支持单遍对齐。安全侧则提醒：SLM 作为异质组件系统，后门可跨组件传播，且毒化样本在共享多任务嵌入中未必可分。

## 技术内容

### 说话人表示鲁棒性与端到端 SDR

**One Embedding Doesn't Fit All: Rethinking Speaker Modeling Robustness Across Speaker-Centric Tasks**（Survey Talk；Shuai Wang）  
综述从任务导向视角重新审视说话人建模鲁棒性：回顾在声学、内容、时长与域变化下学习说话人表示的进展，并讨论下游任务如何差异化利用说话人信息。重点权衡任务无关表示与任务自适应建模，并展望更可泛化、可迁移且任务感知的说话人建模与多模态系统。

**SDR-LLM: Speech-LLM Based End-to-End Speaker Diarization and Recognition with Sentence-Level Temporal Modeling**（论文 2854；Renjie Yu）  
提出统一 Speech-LLM，同时预测说话人身份、文本与毫秒级时间戳；以 FIFO 输出序列将声纹 ID 与时间边界纳入自回归生成。针对标注稀缺，先用合成数据模拟说话人轮次与时序，再用少量真实数据微调。在 AISHELL-4、AliMeeting、OleSpeech 上转录精度优于对比 E2E，日志性能与级联相当，兼顾转写精度与时间对齐。

### 边界紧致、重叠建模与模型安全

**Tight Boundary Prediction in Speaker Diarization Using Causal-Anticausal Consistency**（论文 45；Shota Horiguchi）  
针对多说话人对话 ASR 标注因语义连续而包含停顿与边界裕量、模型易学到“松”边界的问题，用因果与反因果模型生成更紧的伪标签（二者天然难以学松散化行为），并迭代协同训练逐步收紧。摘要称可恢复理想紧标注训练约 70% 的收紧效果，并改善下游表现。

**Modeling Overlapped Speech with Shuffles**（论文 2462；Matthew Wiesner）  
用 shuffle 积与偏序 FSA 对齐并做说话人归属转写；以 FSA 总分为损失，在子词、词、短语层边际化重叠序列的所有串行化，并用偏序约束缩小图规模；直接建模（token, speaker）元组，Viterbi 实现单遍对齐。在合成 LibriSpeech 重叠上评估，算法基于 k2/Icefall，摘要称此为多说话人录音单遍对齐的首类算法。

**Where Do Backdoors Live? A Component-Level Analysis of Backdoor Propagation in Speech Language Models**（论文 2813；Alexandrine Fortier）  
从后门攻击视角分析 SLM 流水线：后门可贯穿传播使各任务高度脆弱；组件级分析表明后门存留或擦除高度依赖被攻击组件；共享多任务嵌入中毒化与良性样本未必可分，挑战过滤防御的可分性假设。强调应将多模态流水线视为具独特脆弱性的系统，而非单模态简单延伸。

## 本场要点

- 说话人嵌入需按任务与条件审视鲁棒性，任务无关与任务自适应存在权衡。
- Speech-LLM 可将说话人、文本与毫秒级时间戳统一自回归生成，并依赖合成—微调缓解标注稀缺。
- 松标注下可通过因果—反因果伪标签逼近紧边界预测。
- Shuffle/偏序 FSA 为重叠语音提供可边缘化、可单遍对齐的说话人归属转写框架。
- SLM 后门可跨组件传播，且毒化样本在共享嵌入中未必可分离。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| Survey | One Embedding Doesn't Fit All: Rethinking Speaker Modeling Robustness Across Speaker-Centric Tasks |
| 2854 | SDR-LLM: Speech-LLM Based End-to-End Speaker Diarization and Recognition with Sentence-Level Temporal Modeling |
| 2813 | Where Do Backdoors Live? A Component-Level Analysis of Backdoor Propagation in Speech Language Models |
| 45 | Tight Boundary Prediction in Speaker Diarization Using Causal-Anticausal Consistency |
| 2462 | Modeling Overlapped Speech with Shuffles |
