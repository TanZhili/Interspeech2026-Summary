# Fast Multichannel Nonnegative Matrix Factorization with Directivity Regularization for DOA-Informed Speech Separation

- 论文编号：2139
- 报告人：Ryosuke Ono
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ono26_interspeech.pdf

## 问题
FastMNMF 联合对角化域里的伪分离滤波器对应虚拟分量而非物理源，本身不利用已知 DOA，难以稳定地选择性提取目标说话人（如智能眼镜场景）。

## 方法
在 FastMNMF 负对数似然上加 directivity 正则：对每个虚拟分量在角度网格上用 von Mises 权重鼓励对目标 DOA 附近响应≈1、对其他说话人方向响应≈0，以容忍 DOA/头动误差。源模型仍乘性更新；Qf 用含线性项 afm 的闭式 VCD。κ→∞ 时退化为点约束 GC。

## 实验与结果
5 麦弧阵、N=1–4、RT60=0.3 s、SNR=20 dB。DR-FastMNMF + von Mises 在 N=1/2 最优（如 N=1 SDR 18.2 vs FastMNMF 13.8；N=2 SDR 9.2），且方差更小。N=3/4 时 SR-FastMNMF（点权重先验）SDR 更高，但提出方法感知指标仍有竞争力。迭代早期收敛更快。

## 结论
全秩空间模型 + 连续角域概率指向正则可提升已知 DOA 下的分离，软权重优于硬点约束；未来需用估计 DOA 评估。

## 点评
把 GC 从“单点内积”推广到 von Mises 软束，贴合 DOA 不确定与混响展宽。N 大时约束变挤导致相对优势下降，说明 DOA 先验与源密度需匹配；真值 DOA 设定偏乐观。
