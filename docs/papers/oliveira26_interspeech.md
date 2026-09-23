# DIALOG DeID: Role and Privacy Aware Transcription for Clinical Interviews Beyond WER

- 论文编号：1489
- 报告人：Dominic Dwyer
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/oliveira26_interspeech.pdf

## 问题
精神病学等双人临床访谈里，“谁说了什么”以及否定、情态/不确定、时间锚点等词面线索直接影响评分；传统 WER/DER 无法刻画误归属与意义关键线索丢失，且需在 IRB 约束下做转写去标识。现有工具分散，缺少统一、可审计流水线。

## 方法
DIALOG-DeID：可配置段级表示上串联 ASR（WhisperX/Amazon/Azure/Google）、diarization（如 pyannote）、LLM 角色映射（clinician vs interviewee）、文本 DeID（Presidio / LLM span / 云 API），并可选下游 PSYCHS 严重度回归。评测除 WER、DER 外提出：(i) 置换不变流对齐的 speaker/role-attributed sWER；(ii) Qualifier/Temporal Preservation F1（QTP-F1），用固定词表检查否定/情态/时间线索类型是否在对应流中保留。另做 1.5× 变速相对 WER、语义审计（线索丢失与硬否定翻转）、DeID span F1，以及在去标识角色标注转写上用词数与线索密度的 ridge 回归拟合 PSYCHS 复合分（LOSO）。

## 实验与结果
PSYCHS-Bench：25 段英文学术访谈 10 分钟片段；AMI 作重叠压力测试。固定 pyannote 时 Amazon 最佳：WER 13.3±1.4、sWER 33.1±6.7、QTP-F1 0.88；其他后端 WER 相近但 sWER 可高至 40+。WER 与 sWER 中等相关（ρ=0.55），与 QTP-F1 弱相关。审计：Amazon/WhisperX 线索丢失 20%/24%，硬否定翻转 2%/4%。1.5× 时 WhisperX RTF 0.06 但 WERrel 20.0，Amazon RTF 0.18、WERrel 12.29。DeID 上 Presidio 在姓名/日期等类别 F1 较强。11 会话子集回归：RMSE=3.84、CCC=0.44、Spearman ρ=0.53。

## 结论
聚合 WER 会掩盖归属错误与线索丢失；角色感知保真与 QTP 监控应作为一等指标。隐私处理后的转写仍可保留一定临床可评分信号。局限：临床样本量小、无声学匿名、QTP-F1 仅为词面代理、未充分分解 diarization/角色映射误差。

## 点评
工作把临床转写评测从“字对不对”推到“归属与否定/时间线索是否还在”，指标设计可审计、与访谈评分逻辑对齐。弱点是 QTP 不建模辖域与改写，sWER 仍受 diarization 瓶颈主导；小样本可行性回归不能外推为可靠自动评分。
