# CLEAR: Clinical LLM Embedding and Attention-based Reconstruction

- 论文编号：883
- 报告人：Eashita Wazed
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wazed26_interspeech.pdf

## 问题
临床心音受医院噪声、摩擦、呼吸等非平稳干扰，传统滤波与局部 CNN 难抓住心动周期长程结构，掩码分离又易产生波形断裂。

## 方法
CLEAR 三阶段：(1) 预训练 Whisper 编长序列生物声学嵌入；(2) Masked GAT 将嵌入建图并预测潜在掩码，抑制噪声；(3) Latent GAN 在嵌入空间修复生理结构并重建波形。相对直接回归干净嵌入，掩码路径约束更紧。

## 实验与结果
10 dB SNR 环境噪声下：输入 PESQ 1.03、SI-SDR −29.37 dB；增强后峰值 PESQ 4.64、SI-SDR 64.35 dB。作者报告自然、无明显伪影的听诊友好输出。

## 结论
LLM 嵌入 + 图注意力掩码 + 潜空间 GAN 可从严重降质输入恢复高保真心音，有助临床听诊与早期筛查。

## 点评
把语音大模型编码器挪到心音，强调长程周期，问题动机清楚。报告的 SI-SDR/PESQ 峰值极高，需注意是否含特定样本峰值、评价是否宽带模式等协议细节；临床诊断效用仍需下游疾病识别实验支撑（正文以增强指标为主）。
