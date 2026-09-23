# Who is Speaking or Who is Depressed? A Controlled Study of Speaker Leakage in Speech-Based Depression Detection

- 论文编号：1394
- 报告人：Hsiang-Chen Yeh
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yeh26_interspeech.pdf

## 问题
语音抑郁检测在 DAIC-WOZ 等基准上常报极高准确率，但未见患者时近随机；疑因说话人泄漏使模型走身份捷径而非抑郁声学标志。需在训练规模固定下系统量化重叠说话人效应。

## 方法
DAIC-WOZ 189 人、PHQ-8≥10 为抑郁，切出 6545 段。规模匹配划分：控制组 151 人 / 目标组 38 人；测试固定为目标组一半片段，训练 A 无说话人重叠（5117 段）、训练 B 同等规模但含目标组另一半（重叠）。三族模型：Wav2Vec-Linear Probing、XLSR-eGeMAPS 拼接、Wav2Vec-SLS；编码器冻结/微调，并加 DANN（说话人作域）对抗。报告抑郁 Macro F1、准确率与说话人识别准确率。

## 实验与结果
重叠设定下微调 Wav2Vec 可至准确率 97.65%（SLS 约 98%），说话人识别常 >90%；严格独立时跌至约 58.74% 等，DANN 仅有限回升（如 62.36%）。XLSR-eGeMAPS 说话人识别近随机（约 6–10%），抑郁准确率中等（约 54–67%），重叠–独立差距较小。高抑郁性能总伴随强身份可分性。

## 结论
当前语音表示中抑郁信号与说话人身份高度纠缠；重叠划分会高估泛化与临床效用，应强制说话人独立评估。

## 点评
用“等规模、只动是否重叠”的对照把泄漏从模型复杂度里剥离，证据链清晰。强在跨架构一致、并同时报 Spk ID Acc；弱在 DANN 未能真正抹平差距，说明简单对抗不够，且结论主要锚定 DAIC-WOZ 一种切段协议。
