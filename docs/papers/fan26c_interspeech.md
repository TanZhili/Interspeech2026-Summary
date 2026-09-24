# Bayesian Generalized Additive Multilevel Models for Accurate ERP Latency Estimation under Moderate Downsampling

- 论文编号：2750
- 报告人：Zixia Fan
- 程序：Wednesday 30 September 2026 / Neurophysiology of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/fan26c_interspeech.pdf

## 问题
单试次 Bayesian GAMM 估 ERP 潜伏期计算昂贵，常靠降采样；不同分量潜伏期变异不同，中等/极端降采样对 onset/offset/持续时长的影响不清。

## 方法
普通话 Tone3 吱哑声被动 oddball（20 人，标准/偏差 /ia/）：在 1000/500/250/100 Hz 上拟合 Bayesian GAMM，估 MMN 与 LDN 的 onset、offset、持续；报告收敛诊断与组件特异变化。

## 实验与结果
1000–250 Hz 收敛良好（R-hat≈1.00、无发散）；100 Hz 不稳定（发散约 5%、ESS 低）。MMN 潜伏期从全分辨率到中等分辨率基本稳定、onset 位移小；LDN 随采样率下降出现更晚 onset、更短持续。极端 100 Hz 两分量仍可检出但时间精度下降、可信区间变宽。

## 结论
适度降采样可降算力且对低变异分量（如 MMN）较安全；应避免极端降采样，尤其对高变异晚期分量（LDN）。

## 点评
把“能算”与“估得准”拆开，并按分量变异解释为何同一降采样策略效果不等。强在收敛诊断与组件对照；弱在单范式/单语种，阈值选择仍偏经验。
