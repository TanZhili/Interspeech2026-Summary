# Teacher-Agnostic Temporal Knowledge Distillation for Resource-Efficient Sound Event Detection

- 论文编号：855
- 报告人：Gihun Son
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/son26_interspeech.pdf

## 问题
SED 需要帧级检测，但 SOTA 多依赖大容量模型，资源受限场景表现不足。异构教师—学生蒸馏不稳定，而面向 SED 的 KD 研究有限，直接套用图像侧 OFA-KD 又难以传递时序上下文。

## 方法
提出 TAT-KD：以教师 logits 为统一蒸馏空间，训练时在学生各编码阶段挂接 Temporal Context Projector（卷积对齐时间分辨率 + Conformer 建模时序 + MLP 投影到类别维），推理时去掉以保持轻量。提出 TCAD：对温度锐化后的教师软标签按 |ŷ−0.5| 归一化置信度加权 BCE（τ=0.5，γ=2），作用于中间投影与最终输出；最终仅用蒸馏损失、不加监督 CE。学生为 SE-CRNN 变体 SC32/16/8/4；教师含 ATST-SED、JiTTER、MDFD-SED 及用 TAT-KD 从 JiTTER 蒸馏得到的 MDFD-TAT。

## 实验与结果
在 DESED（DCASE 2023 Task 4）上以 PSDS1 评估。TAT-KD 在全部教师—学生对上优于 from-scratch、logit KD 与 feature KD；SC32←MDFD-TAT 达 PSDS 0.574（4.548M 参数、3.668G MACs）。TCP 优于 MLP/CNN/RNN 投影器；TCAD 优于普通 BCE。ATST-SED 教师 PSDS 最高但蒸馏增益较小，消融显示其对 median filtering 依赖更强（0.583→0.495）。

## 结论
TAT-KD 通过教师无关的 logits 接口、TCP 与 TCAD，在 DESED 上稳定提升轻量 SED 学生，并保持推理效率，优于训练自零与标准 KD。

## 点评
把 OFA-KD 改造成帧级时序蒸馏，并用置信度加权抑制模糊教师信号，切中 SED 边界定位需求。MDFD-TAT 与学生架构相近时蒸馏最强，说明“教师无关”仍受结构亲和影响；强依赖后处理的教师（如 ATST-SED）作软标签时增益有限，是部署时需甄别的点。
