# SEMamba++: A General Speech Restoration Framework Leveraging Global, Local, and Periodic Spectral Patterns

- 论文编号：665
- 报告人：Yongjoon Lee
- 程序：Wednesday 30 September 2026 / Speech Enhancement and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/lee26f_interspeech.pdf

## 问题
通用语音恢复（噪声、混响、带限、削波等）中，时–频双路径常对时间与频率用同构模块，频率侧缺少全局/局部选择性与谐波周期性建模；单分辨率处理难兼顾多尺度谱模式与效率。

## 方法
提出 SEMamba++：Frequency GLP 并行连接 FAN 直作用于频率轴的全局–周期（GP）支路与卷积局部（L）支路，再点卷积选择融合；多分辨率并行 TFDP（仅频率下采样，时间分辨率保留），各分辨率独立 Time Mamba + Frequency GLP 后自底向上融合；幅度解码用按频带可学习 softplus 映射。训练用 LSGAN（MS-SB-CQTD+MRD）及 mag/相位/一致性/RI/mel/特征匹配等重建损失。

## 实验与结果
在 VCTK-GSR（噪声/混响/带限/削波仿真）上训练，并用 URGENT 2025、DNS 2020、CCF-AATC 等做域外评测；指标含 SCOREQ、UTMOS、DNSMOS 等。正文报告相对 MP-SENet、SEMamba、MaskSR、Universe++、VoiceFixer、USE-Mamba 等多基线，SEMamba++ 在计算效率可接受下取得最佳总体表现；消融支持 GLP、并行多分辨率与 LSGAN 相对纯 MetricGAN 的贡献。

## 结论
为频率轴显式注入全局–局部–周期归纳偏置，并以并行多分辨率 TFDP 捕获多样谱模式，可提升通用语音恢复质量。

## 点评
相对「时间 Mamba + 朴素频率模块」的 SEMamba，GLP 与并行多分辨率直接对准 GSR 的异构失真（尤其带限需全局、谐波需周期）。LSGAN  vocoder 式目标减轻只刷 PESQ 的偏置。全文末段抽取不完整处不影响方法主线；具体数值以论文表格为准。
