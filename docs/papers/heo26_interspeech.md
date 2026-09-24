# Leveraging Diarization Labels for Robust Score Calibration in Target Speaker Tagging via Gaussian Mixture Modeling

- 论文编号：896
- 报告人：Hee-Soo Heo
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/heo26_interspeech.pdf

## 问题
Target speaker tagging（TST）需在日志化后给片段贴注册说话人身份；对话片段长短不一导致验证分数方差大，同标签平均可聚合会话信息，但欠聚类会把异说话人分数混在一起，朴素平均很脆。

## 方法
对每个日志标签下的验证分数集拟合两成分 GMM（EM）：一成分对应正确聚类片段，另一吸收误聚类；每片段取其后验最大成分的均值作校准分。对比 Label-level 全平均与同标签 Top-K 近邻平均。日志化用高分辨率嵌入 + 谱聚类；识别用 ECAPA/ResNet + AS-Norm。标签段数 <5 时不校准。

## 实验与结果
TST-Bench（合成，>204k 段）：ECAPA 上 GMM 在 FAR=0.5% 时 DIR 93.64%，相对 Baseline 88.79%、Label-level 81.82%；ResNet293 等同趋势。ICSI 真实会议：GMM 多数工作点最优或并列最优。C=2 在严格 FAR 最优；C=1 几乎无校准，C≥3 放宽 FAR 略有收益但严格点不稳。方法跨嵌入架构有效。

## 结论
用会话内分数分布的混合建模，可在利用日志标签聚合的同时显式抗欠聚类；两成分是容量与估计稳定性的较好折中。信道/设备多峰留待未来。

## 点评
问题诊断清楚：短段方差 + 欠聚类不对称伤害。GMM 校准几乎零训练成本、嵌入无关，工程可插拔。严格 FAR 上相对 Label-level 的巨大反差是核心卖点；对极短簇或分数近单峰时收益有限属预期 graceful degradation。
