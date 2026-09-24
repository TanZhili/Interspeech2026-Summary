# A light weight Continuous Speaker Verification System for Real time Monitoring

- 论文编号：3584
- 报告人：Harish Rajamani
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/keetha26b_interspeech.pdf

## 问题
电话客服、银行与医保等场景需要在通话全程持续核验客户身份，防止交接、冒充或盗用设备后泄露敏感信息。传统系统多为通话开头一次性认证，无法实时监测说话人变化；同时需满足低延迟、抗噪声混响与跨语言/语码转换的稳健性。

## 方法
演示级连续说话人验证（CSV）系统：客户侧按用户名取注册声纹或短段现场注册，开头验证失败三次则回退密码；通过后转座席，座席界面持续显示验证状态。流式处理用 1 s 窗、0.5 s 跳，经 VAD、嵌入提取与对注册声纹的余弦相似度打分，约每 500 ms 更新决策；不匹配持续约 3 s 则告警并可终止通话。模型为两阶段：Stage 1 用 ReDimNet-B1 在 log-mel 上做多语说话人分类（margin loss，含噪声/混响/变速增强）；Stage 2 冻结骨干，用轻量卷积投影网络与含同语/跨语对的 triplet 采样，得到更可分、语言不变的 256 维嵌入。

## 实验与结果
在 TidyVoice（约 457 小时多语）上训练增强（SNR 5–20 dB，RT60 0.2–0.8 s，速度 0.9/1.1）。系统在 Intel Core i7-8650U 上处理 1 s 音频约 50 ms，RTF=0.05；总约 2.5M 参数、318 M MAC/s（骨干 2.2M / 290 M MAC/s，投影约 256K / 27.36 M MAC/s）。在 TidyVoice 评估/开发集上 EER=2.08%。

## 结论
作者认为该两阶段轻量模型可学习稳健、语言不变的说话人表征，在实时 RTF 与低算力下完成连续验证与座席告警，适用于电话类安全场景并可扩展到其他应用。

## 点评
工作偏系统演示：把 CSV 接到座席告警闭环，并用两阶段（分类预训练 + 跨语 triplet 投影）压低算力。指标与效率数字清楚，但正文对公开基准对比、误报/漏报业务代价及更复杂噪声信道的系统评测着墨有限，EER 主要来自自有 TidyVoice，跨域泛化仍需外部验证。
