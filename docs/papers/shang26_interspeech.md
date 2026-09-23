# Seed-Enh: Generative Speech Enhancement in Decoupled Semantic and Timbre Spaces

- 论文编号：200
- 报告人：Zengqiang Shang
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/shang26_interspeech.pdf

## 问题
多数增强方法直接在声学域（STFT/Mel/波形）操作，噪声与语音纠缠，易学捷径，出现过抑制、高频衰减与背景空洞，并损害说话人音色。解耦语义–音色在合成/变声中有效，但在增强中应用仍有限。

## 方法
Seed-Enh 在解耦语义与音色空间做生成式增强，分三阶段：(1) 语义：将输入后半段（训练时加低复杂度音色扰动）送入冻结 Whisper-Large-v2 编码器，取最后一层 1024 维语义表示；(2) 音色：前半段用 CAM++ 提 192 维全局说话人嵌入，并与对应 Mel 与语义做上下文学习；(3) 融合：以标准高斯为源、语义与音色为条件的 DiT flow matching 生成干净 Mel，经 BigVGAN 合成波形。训练两阶段：先用干净音频学变声/重建，再在 SNR −5~15 dB 的噪声–干净对上微调。推理用 Euler 求解器 25 步；有干净参考时可提更好音色，也可做零样本变声。

## 实验与结果
干净数据为 Emilia（约 101k 小时多语），噪声为 DNS Challenge 库；评测 DNS blindtest 与 LibriTTS+wham，指标含 DNSMOS（OVRL/SIG/BAK）、SIM、CER。Seed-Enh 在两测试集 OVRL 最高（3.095 / 3.193），优于 FullSubNet、TFGridNet、SGMSE、StoRM、SB、AnyEnhance、FlowSE 等。LibriTTS+wham 上 SIM 0.890、CER 0.167。零样本变声在嘈杂参考下明显优于 Seed-VC（OVRL 3.225 vs 2.461，SIM 0.823 vs 0.726）。谱图显示更能抑制噪声并恢复谐波与高频细节。

## 结论
作者认为在解耦语义–音色空间增强可避免声学域纠缠干扰，在抑制噪声的同时恢复高频细节，并支持嘈杂输入下的零样本变声。

## 点评
做法抓住“声学缠绕导致语义/音色互相拖累”这一类问题，把 Whisper 的噪声鲁棒语义与 CAM++/上下文音色分开优化，再 flow matching 融合，比直接在 Mel 上 flow matching（如 FlowSE）更结构化。代价是依赖半段切分与冻结大编码器，且 CER 仍高于判别式模型；生成式路线偏感知质量而非波形保真。
