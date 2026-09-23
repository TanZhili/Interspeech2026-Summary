# Acoustic Biomarkers of Sleep Deprivation on French Read Speech: Interpretable and Frugal Modeling of Sleep Deprivation and Its Symptoms

- 论文编号：777
- 报告人：Vincent P. Martin
- 程序：Tuesday 29 September 2026 / Clinically Useful Speech Representations 2
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/martin26_interspeech.pdf

## 问题
睡眠剥夺及其后果（困倦、疲劳、表现下降）是重要公卫问题，临床需要可在自然场景下反复测量的工具。现有语音研究多聚焦主观困倦或疲劳等副作用，且近年健康语音常依赖大模型，难解释、耗能高，也少系统报告性别/年龄偏差。本文问：仅用可解释声学特征与简单分类器，能否估计睡眠剥夺及其相关症状，并同时评估偏差、能耗与分类器学到的构念特异性。

## 方法
数据为 SOMVOICE：28 名被试（16 女）随机顺序经历正常夜与全睡眠剥夺后做 MSLT；每次朗读前朗读约 150 词法语文本，共 336 段录音，经 rVAD 切成≥20 s 的 818 段。标签包括睡眠剥夺状态、MSLT 潜伏期（≤8 min）、KSS（>5）、疲劳 VAS（>50）、PVT 中位速度与 RTD。特征为 88 维 eGeMAPS、27 维 Snack，及二者早期融合。分类器为 SVC、Random Forest、HistGradientBoosting；嵌套分层分组 10×5 折，按说话人分组并平衡正负类、性别与年龄，段级训练、录音级多数投票，以 UAR 为主指标。用 McNemar 比较特征集，用 logistic 回归评估误分类相对年龄×性别的偏差，用 SHAP 解释特征贡献，用 codecarbon 估计能耗与碳足迹；并用症状网络与跨任务预测检验分类器是否学到更泛化的构念。

## 实验与结果
最佳聚合 UAR：KSS 0.628 最低，PVT-RTD 0.852 最高；睡眠剥夺 0.744、MSLT 0.706、疲劳约 0.65–0.68，PVT Speed/RTD 约 0.80–0.86。除睡眠剥夺任务上融合显著优于单特征集外，特征集间多数无显著差异。部分睡眠剥夺、KSS、疲劳系统存在年龄或年龄–性别交互偏差。SHAP 显示多任务与更低平均能量等相关，不同任务有特异描述符（如 MSLT 更高 F1 mean）。训练+解释合计约 0.450 kWh、8.55 g CO₂。跨任务上，剥夺/MSLT/KSS 较特异；两个 PVT 指标几乎可互换；疲劳与 KSS 易混淆（疲劳模型预测 KSS 的 UAR 甚至高于专训 KSS 模型）。

## 结论
作者认为可用节俭、可解释管线估计睡眠剥夺相关症状，并应同时报告偏差与学到的临床构念特异性。后续拟用贝叶斯推断联合症状网络与分类器估计做联合建模。

## 点评
工作刻意避开 foundation model，把重点放在可解释性、偏差审计与“分类器到底泛化了什么”三件事上，和健康语音里常见的刷分路线形成对照。弱点是样本量小（28 人）、朗读任务场景受限，且疲劳/KSS 混淆提示主观标签边界本身就不清，声学可分性可能部分来自相关构念而非单一症状。
