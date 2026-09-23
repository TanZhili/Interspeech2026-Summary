# VoxEffects: A Speech-Oriented Audio Effects Dataset and Benchmark

- 论文编号：1621
- 报告人：Zhe Zhang
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26x_interspeech.pdf

## 问题

真实语音常经后期效果处理，但少有带精确效果链与参数标注的语音数据，难以系统研究“识别用了哪些效果、如何设置”。音乐侧效果研究多，语音广播式良性后期与采集/平台失真下的鲁棒评测不足。

## 方法

发布 VoxEffects：由 DAPS/EARS/TSP 等近无回声干净语音经固定链 DN→DRC→EQ→DS→RVB→LIM（Pedalboard）渲染，每效果含 bypass 与语音向预设，共 2520 种组合；支持离线与在线渲染。任务含效果存在多标签检测、预设分类、活跃效果数、整体/逐效果强度回归。鲁棒协议覆盖采集侧/平台侧退化（噪声、重采样、有损编码）的 None/Pre/Post/Either/Both。基线 AudioMAE-Fx；评测 ID 与 VCTK OOD，并分析时长与性别公平。

## 实验与结果

Both 训练增强在无退化测试上 ID Acc_macro 约 95.58%、EMR 76.48%、预设 Top-1 36.78%；OOD 明显下降（如 Acc_macro 86.15%、Top-1 12.19%）。平台侧/双侧重退化显著伤性能；匹配退化训练可大幅挽回。细粒度 2520 类预设分类仍难，尤其 OOD。

## 结论

VoxEffects 把语音后期效果识别做成多粒度可复现基准，揭示域偏移与捕获/平台失真是主要难点；资源与渲染器已公开以支持生产感知内容理解与取证相关分析。

## 点评

把“良性后期”从真假二分类中拆出做属性化监督，对内容理解与取证都很实用。固定链+预设库可控但也可能低估真实非线性/创意效果与未知插件；预设分类绝对准确率不高说明粒度过细时需层次化或参数回归替代。
