# CAPS: A Cascaded Reconstruction Model to Power Saving in Hearables Using Sub-Nyquist Sampling with Bandwidth Extension

- 论文编号：506
- 报告人：Sajid F. Dipto
- 程序：Thursday 1 October 2026 / Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/islam26_interspeech.pdf

## 问题
耳机端 ACM/BCM 常以高采样率与高位宽 ADC 采集再压缩传输，未系统利用降采样/降位宽省电；现有多模态 SE 或 BWE 也难同时覆盖多模态、流式与低功耗约束。

## 方法
CAPS 级联：耳端将 ACM/BCM 采到约 4 kHz、8-bit；手机端 Spectral Enhancement Network（U-Net+Mamba）提频谱分辨率，HiFi-GAN 风格 Upsampling Network 波形上采样（256×），Amplitude-Phase Enhancement Network 融合 BCM 做幅相增强。损失含 multi-period、反 wrapping 相位/群时延与多尺度 MAE。自建 20 人同步 ACM+双 BCM 数据（8/10/12-bit）。

## 实验与结果
桌面 4→16 kHz：CAPS 约 2.85 M / 11.04 MB，推理 1.36 ms，LSD/PESQ/STOI 等优于 TFiLM、VibVoice、AERO、EBEN、HiFi++、SEANet。Pixel7 上 55.11 ms（<150 ms 流式阈值）。{24 kHz,12-bit}→{4 kHz,8-bit} 耳端省电约 3.31×；手机跑 CAPS 约 1.15 W，相对耳机电芯可忽略。

## 结论
耳端亚奈奎斯特+低位宽与手机端级联重建可平衡省电与可懂度/质量；文中亦报告低位宽时性能下降趋势。

## 点评
把 ADC 功耗公式与重建网络绑成端到端系统论证，工程闭环完整。模型体积极小适合手机；质量依赖 BCM 条件与自采数据分布，跨设备/极端噪声外推需谨慎。
