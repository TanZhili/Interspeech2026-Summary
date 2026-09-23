# GLAD-CSpeech: A Dialectologically Comprehensive Benchmark for Genuine Chinese Dialect Speech

- 论文编号：1128
- 报告人：Ziyi Cheng
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26j_interspeech.pdf

## 问题
中文方言语音资源按行政地理标签易错分（省内多方言、跨省同方言），且真方言与带口音普通话常混杂，缺语言学根据地、覆盖完整、可支撑 ASR/TTS/DID 的统一评测基准。

## 方法
发布 GLAD-CSpeech：按《中国语言地图集》覆盖 16 方言区（8 官话亚区 + 8 非官话大区）、23 代表点；区分 Genuine Dialect 与 Accented Mandarin；>163 小时，ASR 用多样真实场景、TTS 用棚录；每点 6 说话人、ASR/TTS 任务量见表；三层标注含方言感知转写与普通话–方言平行文本。提供 ASR/TTS/DID 基线；非商用免费。

## 实验与结果
零样本 ASR（6 代表点、方言层转写 CER）：Whisper-large-v3 / Qwen3-ASR / Dolphin 总 CER 61.65% / 28.97% / 38.63%；温州、梅县最难，官话点明显易。同点 KeSpeech 上 CER 低得多。Xi’an TTS（GPT-SoVITS 微调 3.93 h）：MOS 3.78、IMOS 3.91、AMOS 3.65。DID：FireRedLID 零样本 Macro F1 72.29%；Dolphin-FT 达 99.08%。

## 结论
语言学分区 + 真方言/口音普通话对照的多任务基准，能暴露非官话方言上的脆性和行政标签 DID 的迁移差；高纯度标注可补偿数据量做方言 TTS 适配。

## 点评
贡献在数据与分类学：用方言学标签替代省界标签，并显式拆开“口音 vs 真方言”。ASR 用方言层转写评测避免与普通话归一化混淆，诊断更诚实；点位按人口/影响力抽样，未必覆盖最濒危变体。
