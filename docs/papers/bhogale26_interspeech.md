# Voice of India: A Large-Scale Benchmark for Real-World Speech Recognition in India

- 论文编号：3189
- 报告人：Kaushal Bhogale
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bhogale26_interspeech.pdf

## 问题
现有 Indic ASR 基准多为脚本化、较干净语音，公开榜易过拟合；单参考严格 WER 惩罚印度语言自然拼写与语码混合变体，且聚合指标掩盖地区差异，难反映真实电话对话表现。

## 方法
构建闭源评测集 Voice of India：非脚本电话双人对话，按人口比例从 139 区域簇采样，覆盖 15 种主要印度语言，306,230 句、536 小时、36,691 说话人。多轮人工交叉校验转写，并用 Gemini 等构建拼写/切分变体 lattice；用 Orthographically-Informed WER（OIWER）评测。评估 14 个系统（含 Sarvam、Gemini、IndicConformer、OmniASR 等），并按地区、音质、语速、时长、人口统计切片分析。

## 实验与结果
多数模型多语 WER 常超 20；SARVAM AUDIO 在 15 语中 13 语最低，但仍在 Bhojpuri（20.9）、Maithili（24.8）超阈值。地区 WER 约 4%（Nainital）至 44%（Mannarakkat），印地语带与都市偏低，南印与北比哈尔等偏高。公开 FLEURS 上强的模型在 VoI 上显著变差；音质差、过慢/过快、短句均抬高错误。人口统计差异较小（女性略好约 3.1–4.3%，年轻略差）。

## 结论
真实印度口语 ASR 仍有明显语言与地区鸿沟；多参考/ orthography-aware 评测更能反映识别质量。作者按失败模式给出分档改进建议（低资源方言、短句/噪声、语言检测失败等）。

## 点评
把“能上榜”与“能上线”拆开，用地理与条件切片暴露偏差，对 Indic ASR 很有针对性。强在规模、lattice/OIWER 与闭源防过拟合；弱在完整测试集需申请、部分 API 在个别语言上崩溃式失败需结合语言检测一起解读。
