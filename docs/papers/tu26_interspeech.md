# Duration-aware self-attention for speech deepfake detection

- 论文编号：2200
- 报告人：Youzhi Tu
- 程序：Wednesday 30 September 2026 / Speech Deepfake Detection, Attribution and Characterization
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/tu26_interspeech.pdf

## 问题
深度伪造检测训练/评测常固定时长（填充或截断），与真实可变时长不符，易引入边界伪迹或丢掉关键片段。

## 方法
由整段时长与片段偏移构造 timing embedding，注入自注意力以修正注意力偏置图，称 Duration-aware Self-Attention (DASA)。三种实现：帧无关、帧相关、相对位置编码（RPE）相关。用于 ConFusionformer / Conformer，在 ASVspoof21、In-the-Wild、CodecFake 上评测。

## 实验与结果
RPE-dependent DASA 一致有益：ConFusionformer-9 上 ASVspoof21-LA 最佳/平均 EER 1.01/1.13，DF 1.53/1.71，优于标准注意力；另两种 DASA 常恶化。时长失配实验中，RPE-DASA 在 2/6s 与全长上更稳，标准 SA 在训练=评测时长时最好、失配时骤降。

## 结论
把全局时长语境写入 RPE 约束下的注意力偏置，可缓解时长变化带来的性能波动。

## 点评
问题真实且实现轻量；关键是“有界纠偏”（RPE）而非任意帧级调制。增益幅度中等，但对可变时长部署有直接工程意义。
