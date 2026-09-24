# Steps toward a wearable-informed model of real-world listening effort and fatigue among adults with hearing loss

- 论文编号：2022
- 报告人：David Meng
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/meng26e_interspeech.pdf

## 问题
听力损失者常有听努力与听相关疲劳，助听器算法多只适应声学、不适应用户当下状态；实验室生理指标难反映日常复杂性。

## 方法
46 名轻–中度感音神经性听力损失成人（助听器使用者与非使用者各 23）完成 7–10 天实地研究：Apple Watch 自发起 EMA（不存原始音频，仅提声级、过零率、谱/混响等特征）+ 被动心率/HRV，以及早晚手机问卷（睡眠、日疲劳等）。用可穿戴与声学特征做二分类：高听努力 vs 非高；日疲劳（≥6）vs 非疲劳。

## 实验与结果
无定时提示下日均约 3 次打卡，与既往手机 EMA 相当。听努力：RUSBoost 在 70/30 划分上 recall 92.6%、F1 84.6%；LOPOCV 中 13/25 合格被试 F1>70%。疲劳：Random Forest 准确率 76.2%（显著高于随机）；重要特征含打卡平均 A 计权声级、日最高心率、REM+深睡时长等。LOPOCV 疲劳准确率均值约 63.5%。助听与非助听组疲劳等多数指标无显著组间差。

## 结论
消费级可穿戴结合 EMA 可在真实生活中可行地刻画听努力与疲劳，有望支持未来自适应助听与纵向监测；全文 5 级刻度回归仍难，需二值化才达可用分类性能。

## 点评
把“用户状态感知助听”落到可落地的手表 EMA+隐私友好声学特征，接受度证据有价值。二值化与被试间变异大说明日常标签噪声与个体基线是瓶颈；助听组打卡声级略高的趋势提示策略差异，尚需更大样本验证。
