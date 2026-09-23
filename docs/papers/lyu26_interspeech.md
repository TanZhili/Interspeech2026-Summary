# TriA Pipeline: A Large-Scale Automatic Audio Annotation Pipeline For Audio Classification In Specific Scenarios

- 论文编号：995
- 报告人：Hong Lyu
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 1
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lyu26_interspeech.pdf

## 问题
面向家庭等特定场景的音频分类（AC）标注数据稀缺：通用集（AudioSet、FSD50K、ESC-50）对特定声学场景覆盖不足，专用集（DESED、Kitchen20、CHiMe-Home 等）规模有限。已有自动标注流水线（Emilia-Pipe、NVSpeech-Pipe、NonVerbalSpeech-Pipe）依赖 ASR 或只做副语言标注，难以覆盖广义音频事件。

## 方法
提出 TriA Pipeline 四阶段：Standardization（转 24 kHz 单声道 WAV、响度 -20 dBFS 等）、Audio Activity Detection（auditok 按能量切分，domestic 场景最小 ECT 1.2 s、最大 SCT 2.0 s）、Audio Event Detection（AS-2M 微调的 BEATs iter3+，本地窗 5 s/移 3 s、置信度阈 0.6，再全局检测并拼接）、Filtering（audiobox-aesthetics 的 PC/PQ 与 CLAP 相似度过滤）。用流水线从 Bilibili、Douyin 等构建 TriA（>2130 小时、431 类），并按场景先验切出 TriAGK 子集（TriADESED、TriAKitchen20、TriANonspeech7k）。下游用 BEATs 骨干 + 线性分类头，在人工标注、仅 TriAGK、先 TriAGK 再人工标注三种设定上微调，指标为 Accuracy 与 Macro-F1。

## 实验与结果
小批量验证：约 284.7 小时原始音频、RTX 3090 上约 10 小时、RTF 0.03；Filtering2 后剩 80.08 小时、258 类，主观听测标注准确率约 93.67%。TriA 的 PC/PQ 优于 DESEDreal、Kitchen20、Nonspeech7k。三任务结果（Table 4）：DESED AC 上 TriADESED+DESEDreal 达 Acc 0.8258 / F1 0.8256（相对仅人工约 +5.37% Acc、+3.94% F1）；Kitchen20 序贯微调到 0.9813 / 0.9812；Nonspeech7k 仅 TriA 子集弱于人工，但序贯仍略升。相对仅人工标注，平均相对提升 Acc 3.97%、Macro-F1 3.35%。

## 结论
TriA Pipeline 能把流媒体原始音频转成带事件标注的训练数据；TriAGK 在家庭 AC 任务上可与人工标注相当甚至更好，与人工序贯微调带来稳定增益。代码与数据已开源。

## 点评
核心是把“特定场景缺标注”转成可重复的 AED+美学/CLAP 过滤流水线，并用场景先验子集对接下游任务，而不是只堆大规模无平衡数据。强度在于流水线可扩展、且序贯微调把自动数据当预热。脆弱点在于标注依赖 BEATs 与 AudioSet 本体，对人工集未覆盖或分布偏移的类可能系统偏差；过滤阈值越高类多样性越低，质量与覆盖需权衡。
