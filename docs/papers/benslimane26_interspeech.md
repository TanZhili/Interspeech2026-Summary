# RT-Tango: Real-Time Distributed Binaural Speech Enhancement for Low-Power Hearing Aid Devices

- 论文编号：3301
- 报告人：Zahra Benslimane
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/benslimane26_interspeech.pdf

## 问题
双耳助听要实时、低功耗且设备间通信有限；既有高效方案多在单通道，分布式双耳在低延迟与低算力上仍缺统一框架。

## 方法
RT-Tango 改造 Tango 两阶段分布式架构：每耳 SN-DNN 估 mask → SDW-MWF 得压缩信号传对侧 → MN-DNN  Refine → 最终 SDW-MWF。效率手段：ERB 特征压缩、分组 RNN（SN 用 8 组、MN 用 2 组）、固定速率跳帧复用 mask（FRS）。低延迟用非对称 STFT（长分析/短综合窗）与在线 EMA 更新空间协方差；流式版称 RT-Tango-OS。在仿真双耳与 BinauRec 实测 RIR 子集上评估。

## 实验与结果
4 ms hop 下 RT-Tango 约 33.4 MMAC/s，接近保留 Tango-RNN 质量（PESQ/STOI 约 1.66–1.71 / 0.84），远低于同帧率 GTCRN（197.5）。RT-Tango-OS 算法延迟可至 8 ms，代价是 SI-SDR 等有所下降（如左耳 4.4→2.9），总约 35.1 MMAC/s。消融：SN 分组降本几乎无损，MN 过分组伤约 0.8–1 dB；FRS 优于部分学习 skip 方案。

## 结论
在分布式双耳框架内组合 ERB、分组 RNN、时域稀疏与非对称 STFT，可在超低延迟与低 MMAC 下保持有竞争力的增强与耳间平衡。

## 点评
少见地把“分布式双耳 + 助听级延迟/算力”一起做系统整合，而不是只压单通道网。两阶段 MWF 结构对压缩与耳间平衡友好。在线 SCM 适应期与跳帧对非平稳干扰的鲁棒性仍是部署关键风险。
