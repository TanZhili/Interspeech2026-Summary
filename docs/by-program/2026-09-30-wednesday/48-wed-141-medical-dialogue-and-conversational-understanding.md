# Medical Dialogue and Conversational Understanding

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：13
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场面向医疗音频与对话理解：联邦少样本临床音频诊断、心理危机热线分级、抑郁症严重度 LLM 行为剖析、环境临床抄写员的噪声安全压测、一线健康对话基准挑战，以及多部位听诊录音的患者级多模态问答。

共性关注标注稀缺、隐私与安全：伪标签情境学习、副语言注入文本证据、提示内容相关性重于 demonstration 数量，以及 WER 无法捕捉的临床不安全输出。评测侧则建设真实噪声重叠的多说话人医疗对话基准，并把听诊从孤立分类推向患者级问答。

## 论文技术总结

# Unlocking In-Context Learning in Audio-Language Models from Decentralized Medical Audio

- 论文编号：430
- 报告人：Ran Piao
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/piao26_interspeech.pdf

## 问题
临床音频诊断缺大规模中心化标注，机构数据隐私受限；闭集分类难覆盖开放临床概念。需要在联邦设定下让音频–语言模型获得上下文诊断能力。

## 方法
Federated Self-Contextualization (FSC)：无监督聚类伪标签（无语义的任意名称）构造 support–query 片段，训练抽象“声学→上下文标签”映射；三阶段——字幕式预训练对齐音频嵌入与医学 LLM、联邦 episodic ICL 适配、测试时用少量真实标签 support 诊断 query。在留出呼吸与心脏条件上评测。

## 实验与结果
2-way 2-shot 准确率 71.6%，相对最强音频–语言基线高约 9 个百分点（约 62.1%）。跨 shot/设置优势保持；异常心音等子条件亦有报告。消融支持完整流水线。

## 结论
可把 ICL 技能与医学语义知识分源获取：伪标签练推理技能，预训练 LLM 提供概念语义，适配少样本开放词汇临床音频诊断与联邦隐私约束。

## 点评
“无意义伪标签防记疾病–声音映射、只学上下文绑定”是巧妙解耦。联邦 + 少样本叙事贴合医院现实。性能仍依赖测试时真实 support 质量与聚类伪片段是否覆盖声学多样性；开放类别外推边界需更多罕见病验证。


# Speech-based Psychological Crisis Assessment using LLMs

- 论文编号：997
- 报告人：Terumi Chiba
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chiba26_interspeech.pdf

## 问题
心理支持热线危机分级依赖人工、一致性受培训与人力限制；纯转写文本丢失副语言线索，隐私与稀缺数据下难直接训 SpeechLLM。

## 方法
真实中文热线 154 通（约 100h），专家三分类：无危机/低/中高。SpeechLLM 抽取副语言线索写入 ASR 转写（paralinguistic injection），再由文本 LLM 分类；推理增强训练用 LLM 诊断理由作辅助监督；5 分钟分块增强 + 通话级多数投票；通话级 5 折。对比 OpenSMILE+SVM、零样本富文本 LLM、SpeechLLM 微调等。

## 实验与结果
系统 macro F1 0.802、准确率 0.805，优于声学、零样本 LLM 与 SpeechLLM 基线。作者定位为人工监督下的分流决策支持，非替代临床评估。

## 结论
显式副语言文本化在少数据隐私敏感场景下，可比直接微调 SpeechLLM 更有效；理由监督与分块增强有助于正则化。

## 点评
把副语言“写进文本”绕开稀缺语音端到端微调，务实。样本量仍小、分块多数票可能抹平局部危机信号；热线中文单中心，跨机构外推需验证。伦理上强调决策支持定位是必要边界。


# Investigating LLMs Behavior in Depression Severity Prediction

- 论文编号：456
- 报告人：Jiawei Yu
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yu26_interspeech.pdf

## 问题
LLM 少样本是否为抑郁严重度（PHQ-8）提供有效监督仍不清；示范数量增加是否单调变好、错误示范标签是否被利用、全文转写是否必要，均缺系统检验。

## 方法
E-DAIC（275 访谈，PHQ-8 0–24）；Whisper-Large-V3 重转写；五款 LLM，0–10-shot；矛盾标签干预测标签依赖；GPT-5.1 抽取症状聚焦摘要 vs 全文；多轮预测平均。主指标含 CCC 等。

## 实验与结果
增加 shot 收益有限且非单调；对损坏示范标签大多不敏感，暗示示范更像格式线索而非强监督。症状聚焦摘要一致提升 CCC，约省 80% token；弱模型增益更大。预测平均带来稳定提升且不改提示设计。

## 结论
上下文相关性重于示范数量；临床部署宜优先精炼症状相关文本并配合预测平均，而非堆 shot。

## 点评
矛盾标签与 shot 缩放实验直接拆穿“更多示范=更好临床监督”的假设，对 ICL 医疗应用很有价值。摘要抽取本身用强模型，可能引入抽取器偏置；仅文本通道，忽略声学抑郁线索。E-DAIC 音频质量不均限制外推。


# Beyond WER: A Paired Acoustic Stress Test for Ambient Clinical Scribes

- 论文编号：606
- 报告人：Xiao-Hang Jiang
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26c_interspeech.pdf

## 问题
环境临床 scribe（ASR→LLM）用 WER 评稳健性会掩盖安全风险：小词错误可翻转否定、剂量、分诊，而 WER 几乎不动。

## 方法
配对声学压力测试：同一对话注入平稳环境噪声（DEMAND）与非平稳语义干扰（MUSAN 人声）多 SNR，下游 LLM 配置冻结。将否定翻转、数字/单位、非语音污染等原因侧触发映射到分诊漂移、红旗遗漏、Unsafe Rate、SCER、ErrProp 等结果侧安全指标；并测轻量 agent 缓解（无需微调）。

## 实验与结果
干净参考 Unsafe 约 13.6%、WER 16.54%。平稳环境噪声 WER 仅小幅升（摘要称约 +0.71pp）即可使 Unsafe 近翻倍（如 15 dB 环境噪声 Unsafe 27.21%）。语义干扰下 WER 与 Unsafe 同步恶化（5 dB Unsafe 91.54%）。缓解策略在噪声下降低安全劣化。

## 结论
临床不变性应替代纯转写精确度；语义扭曲而非聚合 WER 是下游安全失败主因。轻量缓解可在不微调模型时部分止血。

## 点评
配对设计干净隔离声学因果，对“WER 好看就安全”是有力反例。依赖 LLM 裁判与 claim 抽取，指标本身有噪声；真实诊所噪声分布与合成注入可能有差。结果对部署 ambient scribe 的安全评测清单很实用。


# Benchmarking Speech Systems for Frontline Health Conversations: The DISPLACE-M Challenge

- 论文编号：3255
- 报告人：Dhanya E
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/e26_interspeech.pdf

## 问题
一线社区健康对话（印地语、自发、嘈杂、重叠、语码混合）与医院受控英语临床语料差异大，缺统一基准覆盖说话人日志、ASR、主题识别与摘要的端到端链路。

## 方法
DISPLACE-M Phase-I：发布约 40h 开发 + 15h 盲测印地语一线健康会话；四赛道——说话人日志（DER）、ASR（tcpWER 等）、主题识别、对话摘要（ROUGE-L）；提供基线（IndicConformer、ASR–LLM 主题/摘要等）。12 国际队参赛；参考 Gemini 2.5 Pro、Sarvam Saaras v3。

## 实验与结果
ASR：最佳队 CER/WER/tcpWER 10.59/18.15/18.63，优于微调 IndicConformer 基线（tcpWER 20.23）与 Gemini；日志赛道前四队超 Baseline-2。主题识别 ROUGE-1/L 最佳约 0.46/0.44（基线约 0.15/0.14）；摘要 ROUGE-L 最佳约 0.20（基线 0.18，Gemini 0.21）。域内微调与医学术语后处理是 ASR 关键。

## 结论
挑战建立了印地语一线健康会话的可复现基准与排行榜；Phase-I 显示 ASR/日志有明显提升空间，高层理解任务仍难。后续阶段将延续。

## 点评
把社区一线、语码混合与多任务串成统一评测，填补印度健康语音空白。摘要/主题绝对分仍低，反映上游 ASR 误差与任务定义难度；发布数据规模相对会议语料仍有限，但对催生域适配研究已够用。


# AuscuTSLM: Patient-Level Multimodal Question Answering from Multi-Site Auscultation Recordings

- 论文编号：2037
- 报告人：Fan Wu
- 程序：Wednesday 30 September 2026 / Medical Dialogue and Conversational Understanding
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wu26j_interspeech.pdf

## 问题
听诊主观性强；通用 ALM 不擅生理声学细微异常。既有方法多为孤立分类或短窗切分，难做多部位、患者级问答式综合评估。

## 方法
AuscuTSLM：用门控交叉注意力将多部位听诊录音对齐冻结 LLM 嵌入空间；比较轻量自训编码器（Raw/Mel）与 Wav2Vec2/Whisper/CLAP；支持更长上下文（至约 30s）与多部位聚合。在 CaReSound 上做患者级 QA（是否题 + 开放生成）。

## 实验与结果
1.4B 模型：Yes/No Acc 93.50%、F1-macro 0.865、Contains-Match 42.60%、ROUGE-L 0.673、METEOR 0.643、BERTScore 0.952，优于零样本 ALM 与微调 CaReAQA（F1 0.846）。Raw 编码器与大预训练前端相当或更好；上下文从 30s 缩到 10s 性能明显下降，多部位聚合可部分补偿截断。

## 结论
域专用轻量前端 + LLM 对齐可 rival 大规模 ALM；多部位空间冗余有助于患者级听诊 QA。

## 点评
把听诊从分类推向可问询的患者级理解，更贴近临床交互。生成指标提升大于二分类，说明对齐主要改善文本 grounding。依赖 CaReSound 与冻结 LLM 世界知识，罕见病理与噪声设备外推仍待验证。

