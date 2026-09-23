# Bridging Self-Supervised Learning and Speech Enhancement: A Wav2Vec2-Conditioned Framework

- 论文编号：964
- 报告人：Shuubham Ojha
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/ojha26_interspeech.pdf

## 问题
扩散式语音增强感知质量较好，但缺少语言学引导，对未见噪声/声学条件泛化弱。常见条件方式为拼接或独立条件网络；SSL 特征虽含噪声下仍可用的音素信息，如何低开销注入扩散 U-Net 仍不明确。

## 方法
在 StoRM（复 STFT 域 OUVE 分数匹配）上，用冻结 wav2vec 2.0 base 从噪声波形提最终 Transformer 层特征（768 维）。经三层 MLP 投影为 FiLM 的 \(\gamma,\beta\)，仅在 U-Net bottleneck 做仿射调制。时序聚合采用由线性–高斯状态空间稳态卡尔曼滤波导出的指数平滑（EMA），\(\alpha=1\) 用于主实验。对比 128/32 通道配置，反向采样 30 步。

## 实验与结果
VoiceBank-DEMAND：相对同宽 StoRM，OURS-128 PESQ 从 2.4862 提到 2.8742（约 +0.4），STOI 亦升；SI-SDR 略降（作者归因于更激进抑噪）。DNSMOS 上 OURS-32 OVRL 3.359 略优于 StoRM-32 的 3.347。LibriMix（32 通道）上相对 StoRM-32 全面更好（PESQ 2.01 vs 1.64 等）。消融：仅 bottleneck FiLM 优于 encoder/decoder 多处调制；EMA 在侵入/非侵入指标间比 mean pool 更均衡。OURS-32 RTF 0.55，可快于实时。

## 结论
作者认为用时序平滑的 wav2vec 2.0 FiLM 条件能以极小算力开销提升扩散增强的 PESQ/STOI/DNSMOS；bottleneck-only 最有效。未来拟扩大评测、主观听音并尝试 WavLM/HuBERT。

## 点评
贡献在于“在何处、如何压缩”注入 SSL：bottleneck + EMA 有理论动机且算力占比极低，工程可落地。相对改表示域的大改方案，这是轻量插件。脆弱点是 SI-SDR 回落与谱上更强抑噪可能伤保真；\(\alpha=1\) 接近极端平滑，条件几乎成全局向量，细粒度音素时序可能被抹掉。
