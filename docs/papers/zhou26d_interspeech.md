# BiSASV: Bidirectional Feature Modulation with Dual-Granularity Fusion for Spoofing-Robust ASV

- 论文编号：1532
- 报告人：Ji Liu
- 程序：Tuesday 29 September 2026 / Speaker Verification and Anti-Spoofing
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhou26d_interspeech.pdf

## 问题
SASV 特征融合多把 CM 分数单向门控 ASV，忽略说话人全局上下文对伪迹标定的帮助，且 ASV/CM 特征需求冲突使端到端难平衡。

## 方法
BiSASV：预训练 ECAPA-TDNN（ASV）与 AASIST（CM）。双向调制——用注册/测试 ASV 均值方差与余弦相似度拼成 z_stat，经 FiLM（γ,β）仿射调节 CM 特征；增强后的 CM 再经 sigmoid 通道门控 ASV。双粒度融合：粗粒度把 CM 特征与余弦相似度映射；细粒度对 ASV 交互向量（拼接差与积）做通道重加权后与粗特征拼接。联合训练，无需交替更新。

## 实验与结果
ASVspoof 2019 LA：SASV-EER 0.73%、min a-DCF 0.0153（95% CI 见文），显著优于单向 ATMM-SAGA（约 2.18%/0.048）及多种分数/嵌入融合基线；SV-EER 1.02%、SPF-EER 0.47%。

## 结论
ASV↔CM 互惠调制加粗–细双路径可提升欺骗稳健说话人验证，超越单向门控范式。

## 点评
把说话人统计显式注入 CM 再回控 ASV，闭合了单向设计缺口。强依赖强预训练专家；在更新攻击/域移上的稳定性未在本文充分展开。
