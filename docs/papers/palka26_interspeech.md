# SphereVBx: Spherical Variational Bayes Clustering for Simplified EEND-VC Diarization

- 论文编号：2224
- 报告人：Petr Pálka
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/palka26_interspeech.pdf

## 问题
现代说话人嵌入多在单位超球上、角间隔训练，VBx 仍用高斯 PLDA 后端；EEND-VC 第二阶段常依赖滤短嵌、滤后余弦重分配等启发式。需要与超球几何匹配、能简化聚类流程的贝叶斯方法。

## 方法
SphereVBx：保留 VBx 变分推断，将 PLDA 换成 T-PSDA（vMF 说话人/先验），在超球上做混合聚类；简化版用 GMM 替代 HMM。特殊设置 d=D、κ_b=0、κ_w=1 得无预训练参数的 SphereVBx-PF（相似度与余弦单调相关）。EEND-VC 中用时长可靠性权重替代丢弃短嵌；可选 Multi-Stream 变体在窗内联合分配以强制 cannot-link。

## 实验与结果
级联 VAD+VBx+OSD：SphereVBx 平均 DER 22.1 vs VBx 22.7，PF 22.2。EEND-VC（固定 DiariZen 局部模型）：Baseline 平均 12.65（MSCE 0.37）；SphereVBx 12.52；MS-SphereVBx-PF 12.48。多数集合持平或略优，同时去掉短嵌过滤与事后余弦重分配等启发式。

## 结论
超球贝叶斯聚类在级联管线提升聚类，在 EEND-VC 上性能相当或更好且第二阶段更简洁；PF 变体免后端预训练，便于部署。实现已开源。

## 点评
把“余弦常常胜过 PLDA”收进 VBx 概率框架，理论与工程对齐得好。EEND-VC 上绝对 DER 降幅不大，价值主要在简化与统一约束/可靠性加权。对嵌入几何假设强，非单位范数后端需另议。
