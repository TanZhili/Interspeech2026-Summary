# Geometrically Constrained Decentralized Independent Vector Analysis for Distributed Microphone Arrays

- 论文编号：1037
- 报告人：Changda Chen
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26h_interspeech.pdf

## 问题
分布式麦阵上 Dec-IVA 只交换功率统计，但常因跨阵排列不一致、源模型跨阵耦合过强，相对本地 IVA 几乎无增益，噪声下更差。

## 方法
提出 GC-Dec-IVA：MAP 代价在辅助函数上加 DOA 几何约束，使各阵第 n 路 demixing 对同一目标/干扰方向增强或置零，促进跨阵源对齐；另提出按阵分带子频带的源模型 φ，弱化全局共享活动度耦合。VCD 迭代更新 V 与 W；通信仍只交换功率相关统计。

## 实验与结果
仿真 2 讲者、2–8 个双麦阵、无噪与 SNR∈[15,25] dB。噪声下 GC-Dec-IVA II（新源模型）SDRi/SIRi 约 3.3–3.4 / 8.1–8.3 dB，优于 Loc-IVA、原 Dec-IVA I 与 GC-Loc-IVA。排列准确率与一致性近乎完美；部分阵缺 DOA 时 GC-Dec-IVA II 仍保持 Acc≈95–99%。

## 结论
DOA 约束 + 弱化跨阵依赖的源模型可同时提升分离与跨阵排列一致性；实验为同步阵、已知/可推断 DOA 的仿真设定。

## 点评
抓住 Dec-IVA 的核心失败模式（排列错位被全局 rn,t 放大），用几何先验与分阵源模型对症下药。通信开销不增是实用点；真实时钟偏移、DOA 误差与非确定场景仍待测。
