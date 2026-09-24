# Bridging the Age Gap: Towards Detecting Neural Audio Codec Synthesized Elderly Speech Deepfake

- 论文编号：2283
- 报告人：Orchid Chetia Phukan
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/phukan26_interspeech.pdf

## 问题
CodecFake（CF）检测基准多基于年轻成人，老年语音声学差异大；现有 CF 检测器跨年龄泛化差，老年人群更易受害。

## 方法
提出 ECFD 任务与 Elderly-CodecFake（ECF）数据：真实老年语音来自 SeniorTalk（汉语）与 TIS（英语老年子集），用 14 种 NAC（DAC、EnCodec、SoundStream 等）编解码生成伪样本（约 6 万真实、85 万 CF）。评测既有 CF 检测器的零样本迁移；比较语音 FM（Wav2vec2/WavLM/Whisper）与多模态 FM（LanguageBind、ImageBind）；提出 BONSAI，用 Jensen–Shannon Divergence 对齐融合两路 FM 表征。

## 实验与结果
在 Lu et al. CF 数据上训练再测 ECF：老年 EER 约翻倍于年轻子集（如 Wav2vec2-AASIST 年轻 12.89 vs 老年 25.76）。域内：多模态 FM+CNN 优于语音 FM（LB 平均 EER 4.56）。BONSAI 融合 LB+IB 平均 EER 1.66，优于拼接与单模型。

## 结论
老年 CodecFake 是独立且更难的检测场景；多模态预训练先验与 JSD 对齐融合可显著提升 ECFD。

## 点评
把年龄缺口做成公开任务与数据，填补 CF 检测人口盲区。多模态 FM 优势被解释为预训练接触老年视觉语境，属合理假设但仍间接；跨 codec 测试划分有助于测泛化，后续需更严的未见 codec/未见录音条件评估。
