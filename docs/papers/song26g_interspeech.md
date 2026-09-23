# Real-Time Speech Enhancement on Edge Devices Guided by Harmonic and Voice-Activity Cues Utilizing Skin-Attachable Accelerometer

- 论文编号：3119
- 报告人：Yonghun Song
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/song26g_interspeech.pdf

## 问题
极低 SNR 下仅靠声学麦的轻量增强能力不足；皮肤贴附加速度计（ACC）抗噪但高频糊。既有多模态融合用并行编码器或注意力，体积大难上 MCU。需要廉价地把 ACC 线索注入轻量 U-Net。

## 方法
LAU-NetV2：从 ACC 提取帧级 VAD（功率阈值）与浊音谐波软掩码；经轻量 1D 卷积生成 FiLM 的 γ/β，分别在瓶颈 FGRU 前（谐波）与 TGRU 前（VAD）调制特征。骨干为三层下/上采样 U-Net，8 kHz，用噪声 AM 相位做 iSTFT。TAPS（60 名韩语说话人）+ DNS 噪声（SNR −20–20 dB）。部署到 STM32H753：40% 结构化剪枝后微调以满足实时预算。

## 实验与结果
全模型约 45.6k 参数、65.7M MACs/s；PESQ 从纯 U-Net 1.78 升到 2.78，低 SNR（−20–0 dB）优于 VibVoice、LAU-NetV1、FT-JNFS 及 FSPEN/LiSenNet。消融显示 ACC 拼接、VAD-FiLM、谐波-FiLM 逐步贡献；γ 置零比 β 置零伤害更大。剪枝后 PESQ 2.62，MCU 推理 48.66 ms（未剪枝 87.12 ms），端到端约 176 ms；Flash/RAM 约 154/151 KiB。真机 92.3 dBA 噪声下可抑宽带噪声并保谐波。

## 结论
用 ACC 导出的 VAD/谐波做 FiLM 调制，可在极小数参数下显著提升多模态增强，并经剪枝在可穿戴 MCU 上实时运行。

## 点评
把多模态从“重融合”改成“线索调制”，对边缘最实用。机制分析（γ 主导）增强了可解释性。局限是 8 kHz、依赖可靠 ACC 贴附与阈值 VAD；剪枝有可测质量代价。
