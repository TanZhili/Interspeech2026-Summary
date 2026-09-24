# Modeling Articulation

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：1
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本 Oral 场以生物启发语音处理综述开场，随后聚焦发音建模：用大规模语音—网格数据增强稀缺 EMA 反演、从文本直接合成发音运动学、物理信息神经算子求解声道波动方程，以及动态神经场与任务动态的音系规划仿真工具包。主线是在真实 EMA 昂贵稀缺的前提下，扩展发音监督来源，并把物理与神经动力学引入可计算发音管线。

数据侧，ArtBoost 从面向三维人脸动画的 speech-mesh 抽取伪发音轨迹做预训练；STArK 用预训练语音→发音模型伪标 LibriTTS-R，实现文本→EMA 量级运动学并支持说话人克隆。物理侧，PINO 无需预计算监督即可学习一维波动方程，GPU 并行加速静态元音分析。工具侧，PyPhonPlan 把耦合动态神经场与任务动态做成可复现开源仿真栈。

整体上，发音研究正从“仅有少量 EMA”转向“伪标签规模化 + 物理/神经动力学仿真并存”的生态。

## 论文技术总结

# Bio-Informed Speech Processing, Modeling, and Generation

- 论文编号：
- 报告人：
- 程序：Thursday 1 October 2026 / Modeling Articulation
- 技术分类键：phonetics
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
该条目为 Modeling Articulation 口头会场开场的 survey talk。导出程序表保留了标题，但未提供完整官方摘要；主题方向是生物启发（bio-informed）的语音处理、发音建模与生成。

## 方法
官方完整摘要缺失。现有说明仅要求将其视为对生物启发语音处理、发音建模与生成路径的综述，并明确不要虚构具体主张、数据集或结果。因此此处不概括任何具体模型或流程。

## 实验与结果
无可用官方摘要细节，未报告实验与结果。

## 结论
无可用官方摘要细节，无法归纳结论。

## 点评
标题与会场（Modeling Articulation）表明其定位是发音建模综述开场，但当前材料不足以支撑技术细节层面的笔记。


# ArtBoost: Synthetic Articulatory Data Augmentation for Acoustic-to-Articulatory Inversion

- 论文编号：664
- 报告人：Hyung Kyu Kim
- 程序：Thursday 1 October 2026 / Modeling Articulation
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26f_interspeech.pdf

## 问题
学习式 AAI 依赖昂贵稀缺的 EMA 配对数据，规模与说话人/语音多样性不足，制约数据驱动反演的扩展性。

## 方法
ArtBoost 把大规模 speech–mesh 数据（TFHP，FLAME 网格）转为伪发音监督：ASR 切分为 utterance；在网格上跟踪 UL/LL/LI 锚点均值，取突出与开口方向构成与 EMA 兼容的 12 通道目标（不可见通道置零并重采样）；先以通道掩码 MSE 在伪轨迹上预训练，再在真实 EMA 上全通道微调。可接入既有 AAI 架构，无需改模型结构。

## 实验与结果
预训练用 TFHP；微调与评估用 HPRC、USC-TIMIT，leave-one-speaker-out。相对无增强：HPRC 上 PCC 0.678→0.698、RMSE 0.736→0.717；USC-TIMIT 上 PCC 0.351→0.510、RMSE 0.864→0.792（文中亦称基线上 PCC 约 +2.9% / +45.3%）。SSL-AAI 与 SI-AAI 两架构均稳定增益；伪监督虽仅可见锚点，多发音器通道 PCC 仍提升。

## 结论
speech–mesh 可作为可扩展的发音监督来源：伪轨迹预训练加 EMA 微调可稳定提升 PCC/RMSE，并跨架构可用。

## 点评
绕开改架构，用面部网格补 EMA 稀缺，对小数据 USC-TIMIT 增益更明显。伪标签只覆盖嘴唇/下切牙，舌等不可见通道靠表征迁移，物理保真与跨说话人网格质量仍是脆弱点。


# STArK: Towards Synthesizing Articulatory Kinematics from Text

- 论文编号：2842
- 报告人：Xavier Yin
- 程序：Thursday 1 October 2026 / Modeling Articulation
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yin26b_interspeech.pdf

## 问题
从语音到 EMA 的反演已可行，但高质量发音数据稀缺；直接从文本合成发音运动（TTA）仍开放，限制发音表征在合成与下游任务中的规模化使用。

## 方法
STArK 为非自回归文本→发音管线：G2P + FFConformer 音素编码器；Temporal Regulator（One TTS Alignment 无监督对齐 + SepConv 时长预测）做时长扩展；Articulatory Decoder 预测 12 维 EMA、响度与对数归一化 pitch（不预测 SPARC 周期特征）。目标由冻结 SPARC 编码器从 LibriTTS-R 伪标注；推理用冻结 SPARC vocoder 与说话人嵌入做克隆，训练时不显式喂说话人嵌入。损失为 \(L_{art}+\alpha L_{align}+\beta L_{dur}\)。

## 实验与结果
LibriTTS-R train-clean-100，约 73.7M 参数、32k 步。语音：STArK DNSMOS 接近 GT；加 aligner/prosody 后部分指标贴近或超过 SPARC；相对 YourTTS 在 SECS 更强，WER 更高（test-clean 约 6.25 vs 4.58）。发音：对齐时长下 EMA PCC 0.905，pitch PCC 较低（0.533）；加 aligner 改善 EMA/响度 DTW，pitch 改善有限。

## 结论
文本可直接生成高质量发音运动并合成可懂语音，且无需训练期说话人嵌入即可多说话人克隆。未来需加强韵律/情感/口音与评估稳健性。

## 点评
把 NAR-TTS 骨架接到 SPARC 特征空间，用文本扩展伪 EMA 数据，路线清晰。性能高度依赖 SPARC 伪标签与时长对齐；基座设置下 pitch/韵律仍是短板，WER 相对 YourTTS 的差距也说明内容保真仍有空间。


# Physics-Informed Neural Operator for Speech Production Analysis

- 论文编号：2023
- 报告人：Kazuya Yokota
- 程序：Thursday 1 October 2026 / Modeling Articulation
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yokota26_interspeech.pdf

## 问题
声带–声道耦合物理仿真对嗓音研究重要，但传统数值求解计算贵、逆问题需专用算法；经典 PINN 换条件需重训，难做多样声道形状的快速前向仿真。

## 方法
提出面向言语产生的 PINO（PI-DeepONet）：branch 网络输入归一化声道截面面积并输出稳态 \(f_0\)；trunk 输入时空配点。输出声带位移、声压与经硬约束耦合的体积速度（两质量模型 + 一维声道方程 + 唇辐射）。损失为声带/声道/辐射 PDE 残差加权和，无需监督仿真数据；Fourier 特征强制单周期稳态分析。

## 实验与结果
Arai 五元音 /a,i,u,e,o/ 截面，单网训练；对照 RK4-FDM。\(f_0\) 相对误差约 0.1–0.2%；声门体积流 range-normalized RMSE 约 0.36–1.23%，唇压约 1.01–5.98%（摘要称流约 0.8%、波形约 3.2%）。五元音训练约 80 小时，每元音推理均值 0.0389 s，可 GPU 并行。

## 结论
PINO 可在多种声道形状下快速输出 \(f_0\)、声门流与唇压波形。当前仅覆盖已训练形状与稳态；未来需泛化、非稳态、三维与辅音等。

## 点评
把算子学习做到耦合言语产生、用硬约束保证声门–声道耦合，避免为条件换网重训。唇压误差高于声门流，符合谱偏置对高共振峰的困难；训练成本高、仅稳态已训形状，是走向实用逆问题前的主要边界。


# PyPhonPlan: Simulating phonetic planning with dynamic neural fields and task dynamics

- 论文编号：1804
- 报告人：Sam Kirkham
- 程序：Thursday 1 October 2026 / Modeling Articulation
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kirkham26_interspeech.pdf

## 问题
任务动力学把发音目标当作固定吸引子，缺少学习、记忆与感知对产出的内在机制；DNF 与任务动力学的整合研究增多，但缺少面向言语社区、把两者直接打通的现代开源工具。

## 方法
开源 Python 工具包 PyPhonPlan：一维动态神经场（输入、墨西哥帽交互核、阈值门控）、Hebbian 记忆场、跨场耦合与可选 latched gate（防止感知耦合误触发产出）；用规划场峰位置作为临界阻尼谐振子的时变目标，求解 tract variable 轨迹。模块化支持多层场、手势输入与可视化。

## 实验与结果
以三层感知–规划–记忆模型仿真简化 shadowing：1 基线 + 10 阴影 + 1 washout。基线峰在响应位置 x=3；阴影期被感知输入拉向 x≈1.56；washout 仍偏基线约 −0.29（x=2.71），记忆痕迹驱动收敛，并体现在 tract variable 轨迹上。作者强调为示意性人工例。

## 结论
提供可复现、可扩展的 DNF+任务动力学规划到产出框架。讨论指出输入定时仍手动、缺少完整 articulator–tract 映射、高维扩展受限；展望接 TADA、状态反馈与说话人–听者耦合。

## 点评
把理论组件工程化，降低发音规划动力学入门成本。示例能展示交互收敛的涌现机制，但定时与 1D 人工参数空间限制定量拟合人类数据的力度；价值主要在工具与可复现实验脚手架。

