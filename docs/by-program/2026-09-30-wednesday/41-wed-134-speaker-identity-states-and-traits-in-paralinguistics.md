# Speaker Identity, States, and Traits in Paralinguistics

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：3
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场连接说话人身份、人格特质、情绪状态与副语言感知：从有声书叙述吸引力、人格语料升级，到对话熟悉化对声音识别偏差的影响，再到隐私约束下的多模态对话情绪识别，以及 Speech LLM 中身份先验与可控 TTS 挖苦韵律线索。

共性是：副语言判断不仅取决于声学，还取决于体裁/标题、语言理解、对话语境，以及提示中注入的身份描述。方法上同时出现语料发布、图网络隐私过滤、prompt 控制评测与因果韵律操控实验。

## 论文技术总结

# Audio-Based Understanding of Audiobook Narration Appeal

- 论文编号：453
- 报告人：Shahar Elisha
- 程序：Wednesday 30 September 2026 / Speaker Identity, States, and Traits in Paralinguistics
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/elisha26_interspeech.pdf

## 问题
有声书吸引力受叙述风格影响，但大规模计算研究少；同一书目多版本、体裁差异与稀疏消费数据使“哪些声学特征驱动吸引力”难解。

## 方法
LibriVox 单叙述者英语有声书 8,854 本（1,206 叙述者、65 体裁）；每本最多采样约 10 分钟音频。特征：eGeMAPS、YAMNet 事件、whisper-tiny 语速等共 129 维汇总。以 view-rate（浏览量/上线天数）为公开代理；GLM / 分体裁 GLM / 书目随机截距 LME；四分位分类与同书目内排序；并用 Spotify 子集的 return-rate 复核。

## 实验与结果
全局 GLM 伪 R²≈0.09，31 个特征显著但效应小；同书不同叙述变异（0.52）接近跨书目变异（0.54）。LME 相对 GLM 大幅降 AIC。分类：声学 alone 准确率约 0.29–0.32（随机 0.25），结合体裁可达 0.35。排序在 view-rate 上弱，改用 return-rate 后 Kendall’s τ 升至约 0.26–0.28。

## 结论
在控制书目后，叙述声学仍与消费相关且体裁依赖；声学信息可用于分类/排序，但粗代理指标限制强度。属首批系统连接叙述声学与大规模真实消费的研究。

## 点评
把推荐/选角问题落到可解释声学特征与同书对照，工程价值清楚。view-rate 噪声大、对短书有偏，Spotify return-rate 补强是关键；效应分散提示“组合风格”比单特征更重要。


# The SSPNet Speaker Personality Corpus Version 2: Investigating the Role of Language Understanding in Automatic Personality Perception

- 论文编号：383
- 报告人：Alessandro Vinciarelli
- 程序：Wednesday 30 September 2026 / Speaker Identity, States, and Traits in Paralinguistics
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/alshubaily26_interspeech.pdf

## 问题
原 SSPNet SPC 是 APP 常用基准，但评测者听不懂法语，只能依赖副语言；且 9 点量表偏粗、无转写、无标准协议，妨碍多模态与“语言理解是否改变人格印象”的研究。

## 方法
发布 SPC V2：仍用原 640 条 10 秒法语新闻片段（322 说话人）。新增 ASR 转写；两组评测者各约 100 人（懂法语 vs 仅英语）用 BFI-10 的 0–100 分评 Big Five，每条 10 人平均，并可中位数二值化。提供特征、说话人独立五折协议与 6 套基线（Whisper 副语言 / Word2Vec 语言，分类与回归，中/晚融合）。

## 实验与结果
表 1：多数配置显著优于随机/均值基线。懂法语组在 Conscientiousness、Extraversion 等上准确率更高（如多模态尽责性 Acc 67.1%）；不懂法语组 Agreeableness 副语言 Acc 达 61.2%。回归 MAE 约 5.9–8.4（百分制）。

## 结论
SPC V2 使语言理解对照、回归与可复现多模态 APP 成为可能，并附带统一基准协议，意在替代原 SPC。

## 点评
核心贡献是实验设计而非新模型：同音频、异语言理解能力，直接拆开词汇与副语言对第一印象的贡献。转写来自在线 ASR，误差会抬高语言通道噪声；基线 LSTM 偏旧，但协议清晰便于后人替换更强编码器。


# Learning speaker identities in dialogue: Conversational familiarisation modulates response bias and confidence in voice recognition

- 论文编号：1174
- 报告人：Tianze Xu
- 程序：Wednesday 30 September 2026 / Speaker Identity, States, and Traits in Paralinguistics
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26m_interspeech.pdf

## 问题
日常声音学习多在对话中偶发发生，而实验室常用孤立句刻意记忆；对话连贯性与注意焦点如何影响随后的说话人再认仍不清楚。

## 方法
200 名北美英语母语者，2×3 被试间设计：熟悉化材料为四人连贯对话 vs 打乱版；注意指令为身份 / 内容 / 无定向。材料由 VibeVoice 基于 UCLA 库参考音合成，保证身份可控。随后 yes/no 旧/新声音再认并评 9 点信心；用 GLMM/LMM、贝叶斯模型与 SDT（d′、c、AUC）分析。

## 实验与结果
无刺激类型或焦点主效应。刺激×真值交互显著（BF≈297）：对话熟悉化提高旧说话人命中，但降低对新说话人的拒识。信心模式被对话放大；d′ 不变而偏差 c 在对话条件下更自由（更倾向答“旧”）。注意焦点主效应不显著。

## 结论
对话语境主要改变反应偏差与信心依赖，而非整体辨别力；熟悉化结构系统性调制声音再认决策。

## 点评
用 SDT 把“对话学得更好”拆成偏差而非灵敏度，结论更干净。合成语音保留身份但可能减弱自然变异；焦点无效提示偶发学习在此任务中已足够，或指令操纵偏弱。


# Speaker-Filtered Heterogeneous Graph Network: Toward Privacy-Preserving Multimodal Emotion Recognition

- 论文编号：2282
- 报告人：heying song
- 程序：Wednesday 30 September 2026 / Speaker Identity, States, and Traits in Paralinguistics
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/song26e_interspeech.pdf

## 问题
多模态对话情感识别（MDER）常用全局图聚合，易混入非目标说话人表征（隐私风险），并可能泄漏未来信息；跨模态噪声也导致负迁移。

## 方法
提出 SF-HGN：CAGI 在因果窗内用分模态 Top-K 注意力抽取跨说话人线索并注入目标话轮（含冲突/情感动态特征）；随后仅在单说话人异质子图（SS-HG）上做内外模态关系传播，从结构上隔离其他说话人节点。特征：RoBERTa 文本、DenseNet 视觉、openSMILE IS10 声学。

## 实验与结果
IEMOCAP：WA 68.76%、WF1 68.73%，总体优于所列基线。MELD：WA 66.40%、WF1 65.65%，在 Fear/Disgust/Anger/Surprise 等少数类上更强。消融去掉残差、事件注入或说话人过滤均掉点。参数约 1.19M，推理约 51.3 ms，低于 DialogueGCN/DialogueRNN。

## 结论
先因果注入上下文、再单说话人图传播，可在保护说话人级隐私边界的同时保持竞争力，并降低计算开销。

## 点评
“隐私”主要靠图拓扑隔离而非差分隐私等形式化保证，但对部署场景仍有工程意义。Angry 在 IEMOCAP 上偏弱、MELD 中性类偏大，说明隔离策略在低唤醒冲突与类别不平衡下仍需加强。


# Hidden Priors in Speech LLMs: Speaker Identity Shapes Emotional Perception

- 论文编号：1238
- 报告人：Hsing-Hang Chou
- 程序：Wednesday 30 September 2026 / Speaker Identity, States, and Traits in Paralinguistics
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chou26_interspeech.pdf

## 问题
Speech LLM 做情感识别时，提示中的说话人身份描述（口音/国家/语言）可能引入隐藏先验，即使音频不变也会改变判断；需量化、解释并削弱该敏感性。

## 方法
固定音频，仅替换身份语句（12 种描述 × 口音/国家/语言），在 MSP-Podcast 与 BIIC-Podcast（各四类情感、每类 2000 条评测）上测 Qwen2-Audio、Qwen3-Omni、Phi-4、DeSTA2.5-Audio。用 F1 gap（各情感最优–最差身份差的 RMS）+ 置换检验；用音频 token 显著性 CDF 差检验预测跳变是否伴随声学关注转移。以 LoRA（base / mix 身份提示）微调 Qwen2-Audio 降敏。

## 实验与结果
预训练模型 F1 gap 均显著大于零；语言条件往往 gap 最大。标签跳变组显著性偏移更大，支持 H2。LoRA（尤其 mix）把 MSP 语言 gap 从约 0.12 压到约 0.0025，多数设置与置换零假设无显著差异；同时 macro-F1 升至约 0.67。

## 结论
文本身份线索 alone 即可系统偏移 Speech LLM 情感预测；轻量 LoRA 可大幅降低该敏感性。局限：真实身份属性更复杂、多线索组合未充分探索。

## 点评
固定音频的提示扰动实验设计干净，把“偏见”从数据分布问题变成可控因果探针。语言条件最强暗示模型把“说什么语”当成强情境先验；mix 训练使身份与标签解耦，是实用缓解路径。


# What Makes Synthetic Speech Sound Sarcastic? A Prosody-Controlled Perception Study

- 论文编号：1487
- 报告人：Shekhar Nayak
- 程序：Wednesday 30 September 2026 / Speaker Identity, States, and Traits in Paralinguistics
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26x_interspeech.pdf

## 问题
讽刺感知依赖韵律，但自然语料中音高、语速、响度共变，难分离各维度因果贡献；需可控合成刺激做因果检验，并对照模型是否与人类权重一致。

## 方法
用 Qwen3-TTS 单说话人生成，对语速（快/慢）× 音高变化（动态/平坦）× 响度（响/轻）做 2×2×2 全交叉；经 Cohen’s d 正交筛选得 192 刺激（24 句×8 条件）。66 名英语近母语者评 5 点讽刺与自然度；同刺激喂给 Qwen3-Omni（多 seed 平均）。LME 分析主效应与交互。

## 实验与结果
正交验证：目标维度 d 大（音高 1.14、响度 0.81、时长 1.76），非目标 |d|<0.25。人类：响度主效应显著（更响更讽刺），语速与音高主效应不显著。模型：讽刺评分更由语速驱动（更慢更高分），与人类权重不一致。自然度方面人类偏好更快、更轻；模型更偏好动态音高。

## 结论
可控神经 TTS 可构造正交韵律刺激；人类主要靠响度听讽刺，而该基础模型更偏重语速，行为对齐有限。

## 点评
方法贡献大于单一“响度重要”结论：用生成+效应量筛选逼近因果独立。无语境的最小设置抬高韵律权重；模型用同一家族 TTS/Omni，对齐差距可能部分来自训练目标差异，不宜外推到所有系统。

