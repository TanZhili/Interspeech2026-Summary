# POP-SED: Prototype Orthogonal Projection for Robust Few-shot Sound Event Detection

- 论文编号：153
- 报告人：Takehiko Kagoshima
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kagoshima26_interspeech.pdf

## 问题
少样本声音事件检测中，支持集与查询中的目标事件常与背景重叠；现有做法多靠域级/支持集微调适应背景，计算重、灵活性差。

## 方法
POP-SED（无需微调）：用基础音频编码器提帧特征；对支持正例算目标原型；对背景与查询特征拟合 vMF 混合，再按稳健性支持集准则选背景均值向量；将目标原型正交投影到背景子空间的正交补，再与查询做相似度阈值检测。编码器可用 BEATs / CLAP，均不微调。

## 实验与结果
DCASE2024 Task 5 验证集：POP-SED + BEATs 平均 F-score 62.35%，相对 Full Background Model 基线 40.20% 大幅提升；接近需域级与支持集微调的顶尖系统。消融表明向量选择与 PDF 背景建模均有贡献。

## 结论
正交投影可在不微调编码器的前提下抑制背景，使通用基础模型达到接近微调系统的少样本 SED 表现，便于现场定制。

## 点评
把“背景适应”做成几何投影而非梯度更新，适合部署约束紧的场景。依赖背景向量估计质量与 vMF 假设；极端非平稳背景或目标与背景高度共线时投影可能过杀目标能量。
