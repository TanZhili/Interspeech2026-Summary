# Collecting Prosody in the Wild: A Content-Controlled, Privacy-First Smartphone Protocol and Empirical Evaluation

- 论文编号：2417
- 报告人：Timo K. Koch
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koch26_interspeech.pdf

## 问题
野外采集韵律时，语义与韵律常纠缠；存原音频又有隐私与合规障碍。缺少可在手机上标准化词内容、仅上传特征的可落地协议。

## 方法
在 PhoneStudy EMA 中嵌入朗读模块：每日末次提示朗读正/中/负价脚本句；设备端 openSMILE 提特征后立即删除原音频，仅同步特征向量。德国配额样本 Android 用户两期各约两周；用特征过滤无效录音，并以随机森林做说话人性别与瞬时效价/唤醒预测作诊断。

## 实验与结果
提示发起率 67.8%，发起后三句完成率 96.9%；过滤后 9,877 条、560 人。条件对 F0 范围无显著差，HNR 与 voiced segments/s 有小幅条件效应；说话人 ICC 约 0.33–0.69。性别预测平衡准确率约 91.8–92.0%（eGeMAPS/ComParE）；效价/唤醒相关较弱（ρ 中位数约 0.02–0.13）。

## 结论
内容受控 + 端上删原音的协议可规模化采集可分析韵律特征；说话人信息保留强，瞬时情感自报预测弱，适合作为野外韵律基线模块而非情感金标准。

## 点评
同时解决“词内容控制”与“GDPR 友好”，工程完整且有大样本合规数据。强在隐私设计与合规率；弱在朗读≠自发韵律、情感预测弱说明特征对状态敏感度有限，且仅 Android。
