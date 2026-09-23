# Leveraging Discriminative Capabilities of Self-Supervised Neural Audio Fingerprinting for Efficient Speech Data Annotation

- 论文编号：1436
- 报告人：Kemal Altwlkany
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/altwlkany26_interspeech.pdf

## 问题
行业语音（如语音信箱）需内部标注、不可众包，重复样本浪费昂贵标注时间；若只能标子集，随机抽样会偏向高频重复条。

## 方法
用仅在音乐上训练的预训练 Conformer 神经指纹（PTC）做：(1) 去重；(2) 在嵌入空间 farthest-point sampling 选多样子集。在 Infobip 5 万语音信箱与公开 robocalls 上去重；用 VCTK 合成增强副本验证；线性探针比较 PTC 与 WavLM 对性别/口音/说话人区分。

## 实验与结果
语音信箱中 24,983/50,000 为重复，可标量减半；robocalls 近重复约 64.8%。合成集上 PTC 检出唯一数略偏高（2158 vs 2000）。探针：说话人 F1 PTC 96.36 vs WavLM 82.28（大效应）；性别两者均高；口音 WavLM 略优。FPS 相对随机抽样在嵌入空间更分散。

## 结论
音乐指纹嵌入可迁移到语音去重与多样性子采样，帮助隐私受限场景把有限标注时间花在不重复、更分散的样本上。

## 点评
把工业重复分布与指纹检索对接，实用性强。强在真实重复率与探针量化；弱在指纹非为语音任务训练、口音上不如 WavLM，且去重阈值需业务侧复核假阳。
