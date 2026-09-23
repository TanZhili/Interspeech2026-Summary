# Better Late Than Never: Meta-Evaluation of Latency Metrics for Simultaneous Speech-to-Text Translation

- 论文编号：575
- 报告人：Peter Polák
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/polak26_interspeech.pdf

## 问题
同声语音翻译（SimulST）需权衡质量与延迟，但现有延迟指标（AP、AL、LAAL、DAL、ATD 等）常给出不一致系统排序（如 IWSLT 2023）；短音频人为预切分与尾词（tail words）处理引入结构性偏差，长音频无切分时对齐工具又不可靠，导致评测难支持公平比较。

## 方法
对 IWSLT 等共享任务系统做跨语对、短/长形式的指标元评估。分析指出短形式模拟器在段结束后瞬时吐出剩余译文，使含尾词的指标（AP/DAL/ATD）与用 cutoff τ 的 AL/LAAL 均偏。提出 YAAL：cutoff 改为 τ_YAAL=max{i|d_i<|X|}，只计入严格早于源段结束的词。长形式提出 SOFTSEGMENTER（小写分词、禁止对齐到未来段、标点约束、字符相似软对齐，并保留延迟）与 LongYAAL（计入跨段但排除整条流结束后的尾词）。另定义对齐源词时间戳的 True Latency 作参照，并给出检测“大部分译文在输入结束后才出”的退化行为诊断。工具收入 OmniSTEval。

## 实验与结果
短形式覆盖 IWSLT 22/23 与 MuST-C tst-COMMON 多语对（EN→DE/JA/ZH 等）；长形式用 IWSLT 2025 日志与 ACL 60/60 等（含 CS→EN）。表 1 给出过滤退化系统前后的系统数。正文强调 YAAL/LongYAAL + SOFTSEGMENTER 相对常用指标与 MWERSegmenter 更可靠；抽取文本在成对 Score Difference 元评设定处截断，具体相关/排序一致率数字未见。

## 结论
延迟指标不一致主因是切分与尾词带来的结构性偏差而非仅均匀词长等假设；YAAL/LongYAAL 与更好的重切分可更稳健评估短/长同声系统，并应用退化诊断避免误导性低延迟。

## 点评
工作做的是评测基建而非新翻译模型：把“段结束瞬间免费吐尾词”标成偏差源，再改 cutoff 定义。强处是与 True Latency 对齐的元评思路和长音频软对齐；脆弱处是 True Latency 本身依赖优质转写与词对齐，低资源语难用，且全文截断使定量优势证据不完整。
