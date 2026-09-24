# Disentangling Speaker Traits for Deepfake Source Verification via Chebyshev Polynomial and Riemannian Metric Learning

- 论文编号：36
- 报告人：Xi Xuan
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/xuan26_interspeech.pdf

## 问题
深度伪造源验证判断两段合成语音是否来自同一生成器，常默认源嵌入与说话人特质无关；试点显示说话人/源嵌入跨任务仍可互推，说明存在纠缠与捷径学习。需在源验证中显式剥离说话人信息。

## 方法
SDML 双分支：可训练源编码器提 f_src，冻结 ReDimNet-B6 提 f_spk。两套说话人解耦损失：
- ChebySD-AAM：在 ChebyAAM（用 Chebyshev 多项式逼近 cos(arccos(x)+m) 以稳定梯度）上，对非目标 logit 加上阈值化说话人边距 λ·max(0, |f_src·f_spk|−τ)，惩罚源–说话人对齐。
- RiemannSD-AAM：将源/说话人嵌入与原型经指数映射投到 Poincaré 球，用双曲距离做 AAM 式分类，并以 max(0, γ−d_H(f̃_src,f̃_spk)) 抬高非目标 logit，抑制身份泄漏。
前端 80 维 filterbank；源编码器对比 ECAPA-TDNN、ResNet34、AASIST、Mamba；训练用 MUSAN+RIR 增广。

## 实验与结果
数据：MLAAD v8。因无说话人标签，用说话人嵌入余弦阈值≈0.5 构造伪说话人键，形成四协议：Seen/Unseen 源 × Same/Diff 说话人（P-I–P-IV）。指标 EER/AUC（bootstrap）。相对 AAM-Softmax 基线，两种损失在各编码器上均更好；ResNet34+RiemannSD-AAM 平均最优（EER 3.27%、AUC 0.988），未见源同说话人（P-III）EER 4.08%、异说话人（P-IV）7.13%。消融确认说话人解耦项必要；K、λ、曲率 c 在开发集网格搜索。

## 结论
结合多项式逼近与双曲度量的说话人解耦度量学习可减轻源验证对说话人捷径的依赖，并在未见源协议上提升；代码与协议已公开。

## 点评
把“源验证是否在偷用说话人”从假设变成可测协议与可优化损失，贡献扎实。伪说话人键依赖阈值划分，合成语音本身未必有清晰说话人身份，协议噪声可能影响结论；双曲空间与 Chebyshev 边距的增益是否可迁移到更新 TTS 架构仍需验证。
