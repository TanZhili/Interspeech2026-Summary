# First-to-Spike: An Early-Exit Framework for Rapid and Energy-Efficient Spiking Neural Networks

- 论文编号：1858
- 报告人：Siqi Cai
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26j_interspeech.pdf

## 问题
SNN 本具事件驱动低时延潜力，但常跑满整段序列；现有 early-exit 多用 softmax 置信阈值等非脉冲准则，偏离纯事件范式并增加部署复杂度。

## 方法
提出 First-to-Spike（F2S）：输出层每类一个 LIF 神经元，首个发放脉冲的类即为预测并立即停算；无脉冲则回退到最终膜电位 argmax。加入可学习侧向抑制 WTA 电路加速竞争。Hybrid Temporal Training（HTT）含加权 TET 分类损失、时间间隔 margin 损失与正确类发放时刻效率正则。

## 实验与结果
GSC V2：F2S Acc 92.89%、ADT 63.68、能耗 2.75 µJ，优于 ED-sKWS（90.14%/66.07/2.85 µJ）。SEED：79.35% Acc、ADT 3.06；SEED-IV：71.60%、ADT 5.45，均高于 Sparch 与 ED-sKWS 且更低时延。消融：仅 F2S 规则已有 early-exit；WTA 大幅提准，HTT 进一步降 ADT，二者合用最佳。

## 结论
脉冲本身可作为可靠决策信号；F2S+WTA+HTT 在语音指令与 EEG 情感识别上同时提升准确率并降低时延/能耗。未来需考察 SNR 鲁棒性及与异步神经形态传感器耦合。

## 点评
把 early-exit 内化为输出层“赛跑发脉冲”，比外挂置信阈值更贴 SNN 硬件。强项是跨语音与 EEG 一致；脆弱点包括无脉冲回退仍依赖满时序、以及能耗按 CMOS MAC/AC 估算，真实神经形态芯片开销可能不同。
