# ClinAware: Speech Enhancement Needs Clinical Awareness

- 论文编号：3611
- 报告人：Pramod H. Kachare
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kachare26_interspeech.pdf

## 问题
远程/居家神经语音评估常先做增强再提生物标志物，但增强为可懂度优化可能扭曲停顿、音高变异、jitter 等临床相关特征，影响下游解读。

## 方法
交互演示 ClinAware：同一噪声语音经保守谱门控、激进平滑、预训练 DEMUCS 等增强；提取 pause ratio、F0 均值/标准差、谱质心标准差、jitter、shimmer、语速等；加权归一化成可解释风险探针（非诊断）。浏览器对比频谱、标志物漂移与风险分变化。

## 实验与结果
示例显示方法依赖的漂移：基线风险升幅有限；激进平滑改变细尺度音高但抬高谱不稳定；DEMUCS 放大音高/能量动态并显著抬高风险分。作者称多条录音趋势类似；无临床诊断效度声明。

## 结论
可懂度提升≠生物标志物稳定；增强需临床感知评估，远程监测流水线应检验处理对标志物的副作用。

## 点评
把“增强副作用”做成可点可比的探针，对可信医疗 AI 很及时。强在多策略对照与透明风险公式；弱在风险分为启发式、非验证诊断，且标志物集较小。
