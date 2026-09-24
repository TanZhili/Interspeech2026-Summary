# Privacy vs. Performance: Assessing Communication Utility of Anonymized Voice Features

- 论文编号：751
- 报告人：Shogo Okada
- 程序：Thursday 1 October 2026 / Speaker Privacy and Anonymization
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chan26_interspeech.pdf

## 问题
语音匿名保护身份，但可能扭曲评估沟通质量所需的声学/韵律特征；既往多看 WER/EER，较少直接量化特征保真及其对沟通构念评分的影响。

## 方法
在端到端评估管线最前端用轻量 PV-TSM 匿名（约 0.4 s/2 分钟），原始音频丢弃。比较内部 Kaldi ASR、Azure 发音评估基线，以及在 AMI（36 小时匿名 + 含 uh/um 的原始）上微调的 Azure 定制模型。评估 WER，并对语速、停顿、犹豫、填充比等低层特征与 confidence/persuasion/formality/proficiency 等高层构念做原音 vs 匿名的 Pearson r 与 MAE。

## 实验与结果
AMI 1.5 小时 hold-out：内部 45.13%→58.88%；Azure 基线 12.66%→15.01%；微调后 7.72%→7.89%。面试语料 1000 条上，微调模型原–匿相关普遍最高（如 repetitions r=0.97、hesitation r=0.99、speaking rate r=0.99）；高层中 confidence/proficiency 相关显著提升，persuasion 相关固定约 0.23 但 MAE 低且配对 t 检验不显著。

## 结论
PV-TSM 可大体保留沟通评估所需信息；对匿名数据微调 ASR 可将 WER 差距压到近乎持平，并改善低层/高层特征一致性。

## 点评
把评估从 WER/EER 推进到沟通构念特征保真，贴合就业评估落地约束。隐私数字主要引用先前 EER，本文重心在效用；persuasion 相关偏低提示部分声学构念对相位声码器变换更敏感。
