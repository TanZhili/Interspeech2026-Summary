# Data Filtering Trade-offs in Self-Supervised Speech Representation Learning: A Study on Unconstrained Broadcast Audio

- 论文编号：50
- 报告人：Yaroslav Getman
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/getman26_interspeech.pdf

## 问题
用原始广播音做 SSL 预训练时，是否只留语音、是否只留目标语，常凭启发式决定；能量 VAD 等廉价过滤对表示质量的影响缺少受控比较。

## 方法
在约 20,400 小时芬兰 AlfaTV 存档上固定 wav2vec 2.0 Base，比较四种过滤：Raw（30 s 切分）、能量 VAD（Auditok）、神经 VAD（pyannote）、神经 VAD+音频 LID（ECAPA）。保留量约 100%/86.5%/58.4%/42.3%。在 Common Voice、FLEURS、VoxPopuli 上微调 ASR；ML-SUPERB 冻结探测 CER；ARCH 评非语音事件与音乐分类。

## 实验与结果
E-VAD 全面劣化 ASR（如 CV test WER 39.4 vs Raw 34.2）；N-VAD+LID 最佳（CV test 21.5，相对 Raw 绝对降最多约 12.7 点），N-VAD 次之。冻结探测趋势一致。ARCH 上 Raw 在 8 任务中 6 项最优，选择性过滤可降最多约 9 个百分点；N-VAD 在 ASR 与通用音频间较均衡。神经过滤 RTF 远高于能量法。

## 结论
无普适最优过滤：神经 VAD（±LID）利于目标语 ASR，但牺牲通用音频理解并增加预处理成本；能量 VAD 看似省事却常伤 SSL。应按下游目标权衡。

## 点评
把广播 SSL 过滤做成四档对照并同时测 ASR 与 ARCH，直接打穿“多滤一点总更好”的直觉。强在同架构同步数；弱在领域偏芬兰电视、LID 无域内金标，跨语广播上 LID 收益可能更大。
