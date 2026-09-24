# Attentive Mamba: Channel-wise Local Attention for Speech Recognition

- 论文编号：1708
- 报告人：Jen-Tzung Chien
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/chien26_interspeech.pdf

## 问题
Transformer 自注意力全局建模强但 \(O(T^2)\) 且局部细粒度不足；Mamba 等 SSM 线性复杂度、擅长长程，但局部聚合依赖**静态**深度卷积，缺乏内容自适应。希望在保持 SSM 全局状态建模的同时，为局部特征引入动态注意力。

## 方法
提出 **Attentive Mamba (attMamba)**：用**通道维局部注意力**替换 Mamba2 中的静态因果卷积。
1. 对各通道用因果深度卷积上下文化生成 \(q,k,v\)（而非逐时刻线性投影）。
2. 在因果局部窗口 \(w\) 上做跨通道点积注意力，得到内容感知局部摘要 \(u_t\)。
3. 用 \(u_t\) 动态参数化 SSM 状态转移 \(A,B,C\)。
编码器为双向 attMamba；训练可联合 CTC 与 AED，并可加 4-gram LM 重打分。

## 实验与结果
LibriSpeech 960h：attMamba-CTC (S, 21.2M) test-clean/other 6.24/12.31，优于同配置 conformer-CTC (S, 30.0M) 的 6.59/12.57。TED-LIUM3：S/L 上均优于 conformer；attMamba+lm-CTC+AED (L) test 4.98。消融：双向相对单向 Mamba2 大幅降错；再换通道注意力进一步改善。进阶 CTC+AED+LM 下 attMamba+lm 达 test-clean/other 2.73/6.02，优于同设置 conformer 与若干自监督基线。特征图显示通道注意力使各通道时间轴更均匀，体现通道级动态调制。

## 结论
把静态卷积局部聚合换成卷积上下文化的通道维局部注意力，可增强 SSM 状态参数化，在更小参数量下于朗读与自发语音 ASR 上低于 conformer/Mamba2。

## 点评
抓的是 Mamba「时间混合强、局部聚合钝」的瓶颈，设计贴合频谱「通道内时域相干、再跨通道融合」的结构先验。强在参数更少且消融干净；脆弱点在窗口 \(w=4\) 等超参敏感、双向实现偏离严格因果流式，以及与更强预训练编码器对比时收益边界仍待更大尺度验证。
