# One-Step Token-to-Waveform Generation with MeanFlow in Latent Space

- 论文编号：791
- 报告人：Zheqi Dai
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/dai26c_interspeech.pdf

## 问题
LLM 式 TTS 依赖语义 token 时，Token2Wav 解码器既要恢复韵律/音色，又要满足低延迟。主流 flow-matching 解码器质量高，但推理需多步 ODE 积分，延迟大；直接在波形空间做一步 MeanFlow 又因序列过长而不稳、吃显存。

## 方法
两阶段流水线：先用轻量波形 VAE 把 24 kHz 语音压到与语义 token 对齐的 25 Hz 潜变量 `z`（潜维 `D∈{8,16,24}`），再用条件 1D DiT 在潜空间做 MeanFlow，学区间平均速度场，推理时一次前向从噪声得到 `z_gen`，再由确定性 VAE 解码器还原波形。条件为 CosyVoice2 风格语义 token（25 Hz、单码本）与 CAM++ 说话人嵌入。为缓解生成潜变量与 VAE 训练分布不一致，在不改变推理路径的前提下做两类精炼：冻结生成器只微调解码器，或端到端联合微调（波形域 MR-STFT + 对抗 + feature matching）。

## 实验与结果
在 LibriTTS 训练、LibriSpeech test-clean 评测。最佳配置为 140M DiT、`D=24`、Joint-FT：相对 CosyVoice2 的 10-step Token2Wav（RTF 0.0775），端到端 RTF 降至 0.0046（约 17×）；WER 3.41%、SpkSim 0.932、UTMOS 3.64、MOS 3.85（基线 WER 3.18、MOS 4.05）。消融显示潜维增大改善质量；140M 略优于 600M；No-FT→Decoder-FT→Joint-FT 感知质量逐步提升。

## 结论
潜空间 MeanFlow 可在固定一次生成器+一次 VAE 解码的代价下实现近似多步 Token2Wav 的可懂度与感知质量，并显著降低 RTF；剩余差距主要来自 token→潜变量生成而非波形解码。

## 点评
核心是把一步生成放到短、低维潜序列上，用 MeanFlow 的平均速度回避多步积分，再用 decoder/joint 精炼吃掉分布 mismatch。路线对实时/端侧 Token2Wav 很务实；脆弱点在于一步大跨度对平均速度估计敏感（更大 DiT 未必更好），且条件仍绑定 CosyVoice2 tokenizer 与说话人编码器，跨 token 体系可迁移性未在正文验证。
