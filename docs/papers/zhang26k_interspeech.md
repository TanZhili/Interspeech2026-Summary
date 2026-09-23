# WeSep: A Modular and Cue-Composable Framework for Target Speaker Extraction

- 论文编号：784
- 报告人：Ke Zhang
- 程序：Tuesday 29 September 2026 / Source Separation 1
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26k_interspeech.pdf

## 问题
Target Speaker Extraction（TSE）依赖注册语音、空间、视觉或文本等辅助线索，但现有系统多为单线索、架构与训练管道紧耦合，难以在线索可用性动态变化时做系统组合与对比。作者要把 TSE 重述为异构线索条件学习，并给出可配置的模块化框架 WeSep。

## 方法
WeSep 将数据抽象、线索 frontend、分离 backbone 与 Top Model 组合解耦：mix–target 对从模态仓库按 ID 取线索，batch 内可有不同线索子集；frontend 覆盖 speaker（USEF、TF-Map、Contextual、speaker emb 等）、spatial（IPD/ΔSTFT/SDF/CDF、embedding）、visual（MuSE 风格 viseme）、textual（DAE-TSE 式关键词音素编码）；backbone 可选 Conv-TasNet、DPCCN、BSRNN、TF-GridNet、NBC2 等，经标准化接口注入。默认以 BSRNN 在 3 s 段上训 150 epoch，目标为负 SI-SNR，指标 SI-SDRi；并支持因果化与缺失线索零填充的异构训练。

## 实验与结果
Libri2Mix-100：speaker 特征中 USEF+Context 达 16.56 dB SI-SDRi / 98.05% accuracy（SI-SDRi>1 dB），优于纯 speaker emb（13.17 / 92.08）；因果版同配置 14.15 / 95.93，理论延迟 32 ms。多通道混响数据上，handcraft 空间特征（CDF+SDF+IPD+ΔSTFT）在 BSRNN/NBC2 上分别 14.24 / 17.49 dB，优于 embedding 式空间先验。文本关键词（DAE-TSE）16.45 dB，接近最佳音频注册。VoxCeleb2-mix 上 BSRNN+视觉 12.81 dB，高于原 MuSE 的 11.67。注册+空间联合 14.67 dB，优于单线索；异构缺失训练下 Spatial+Speaker / Spatial / Speaker 分别为 13.51 / 12.61 / 10.01 dB，无崩溃。

## 结论
贡献不在新分离网络，而在把线索粒度、跨模态组合与缺失可用性放进同一优化框架，使 TSE 可系统研究并更接近真实选择性收听。工具已开源。

## 点评
这是基础设施向论文：用统一接口把“换线索=换整条管线”变成配置问题，实验表格也因此能在同 backbone 下公平扫特征族。强项是 intra-modal 组合与 missing-cue 零填充都能跑通；若要推到真实部署，还需看异构训练对“全线索最优”是否有代价，以及视觉/文本设定与注册设定在数据分布上的可比性边界。
