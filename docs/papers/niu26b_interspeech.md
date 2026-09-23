# MCA-DCF-DS: An Adaptive Framework for Unified Diarization and Separation with Spatial Information

- 论文编号：1539
- 报告人：Shutong Niu
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/niu26b_interspeech.pdf

## 问题
DCF-DS 级联 diarization 与分离主要靠频谱线索，高重叠易崩；CHiME-8 空间管线中 GSS 重聚类降 confusion 却抬 miss，NSD 反向，存在 MI–CF 权衡。

## 方法
MC-DCF-DS：在 DCF-DS 分离输入拼接 IPD，并用 mask-MVDR 波束形成，通道级活动概率融合。MCA-DCF-DS：用 SI-SSD（长窗空间聚类）得低 CF 先验，以 NSD-MS2S 重叠检测滤除非重叠单说话人段，仿真保留空间关系的多通道适应数据；教师软标签 KL 蒸馏微调 NSD-MS2S。Whisper-large-v3 作 ASR 后端。

## 实验与结果
NOTSOFAR-1 多通道评测：MC-DCF-DS tcpWER 可至 20.17%（基线 28.28%；无 IPD/MVDR 更差；单通道 DCF-DS 31.72%）。SI-SSD 低 CF 高 MI，NSD 降 MI 抬 CF。Eval-Sim+KD：DER 13.83%，tcpWER 17.86%，优于同 Whisper 后端下的 CHiME-8 Task 2 冠军（18.74%）。

## 结论
系统级空间特征与数据级空间适应互补，可改善分离质量并缓解 diarization 的 MI–CF 权衡，同后端下超过挑战赛冠军。

## 点评
把冠军管线里暴露的 miss/confusion 跷跷板转成“用低 CF 空间先验造适应数据 + KD 控噪声标签”，工程针对性强。依赖多麦空间聚类质量与会话级适应算力；跨会议泛化与实时性仍是边界。
