# Lung-SRAD: Spectral-Aware Regularized Audio DASS with Dual-Axis Patch-Mix Contrastive Learning for Respiratory Sound Classification

- 论文编号：550
- 报告人：June-Woo Kim
- 程序：Tuesday 29 September 2026 / Acoustic Event Detection 1
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shridhar26_interspeech.pdf

## 问题
呼吸音分类（RSC）中 crackle/wheeze 等异常是短时局部谱–时结构；AST 等 CLS 自注意力理论与实证上可能呈低通，削弱高频空间变异，且二次复杂度高。

## 方法
以 AudioSet 蒸馏的 DASS（状态空间）为骨干；用谱响应曲线分析中间层，对选定层施高斯卷积谱感知正则。提出 Dual-Axis Patch-Mix 监督对比学习：沿时间与频率轴混合谱图块，适配 SSM 扫描。ICBHI 官方 60/40 病人无关划分，8 s/16 kHz，SpecAugment，Adam 5e-5，五随机种子。

## 实验与结果
四类 Score：(Se+Sp)/2。纯微调 DASS 61.06%；加谱正则与 Dual-Axis Patch-Mix 的 Lung-SRAD 达 64.48%±0.25（Sp 79.53%、Se 49.42%），相对 AST 基线约 +5%。二分类可达 72.57%。消融显示双轴混合优于单轴；高斯核大小与 σ 过大会降分。

## 结论
SSM 更保中高频空间成分，配合谱正则与双轴混合对比可提升 ICBHI RSC；开源代码公开。

## 点评
把“局部异常=空间高频”接到骨干频谱行为分析，动机强于单纯换模型。Score 仍略低于部分 BEATs SOTA（如 64.84%），敏感性仍偏低；正则层选择依赖响应曲线，跨设备泛化待验。
