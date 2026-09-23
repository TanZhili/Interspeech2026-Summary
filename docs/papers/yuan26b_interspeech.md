# DelayGSE: A Generative Speech Enhancement Framework with Delayed Text-Aware Conditioning

- 论文编号：232
- 报告人：Xin Yuan
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yuan26b_interspeech.pdf

## 问题
基于 LM/扩散的生成式语音增强感知质量强，但在低 SNR 与瞬态噪声下易出现类语音幻觉，语义准确率（WER）常劣于判别式甚至劣于噪声输入。需要在统一框架内同时做去噪、去混响与超分，并抑制幻觉。

## 方法
DelayGSE：16 kHz 噪声语音经 STFT+4 层 Conformer 得声学条件，Whisper-large-v3 编码器得语义条件；AR Transformer（由 Qwen2.5-0.5B 初始化）预测 44.1 kHz DAC 的多码本 RVQ token。两层 delay：(1) MusicGen 式码本级 stride-1 delay；(2) Moshi 式 text-first：先预测文本 token，语音 token 延迟 k=5 步。训练目标为 λtext Ltext + Σ wℓ Lspeech；wℓ 由对 10 万片段逐层保留真值码本测 STOI/Sim/MOS 增量归一得到。可选推理时用真值文本进一步约束。

## 实验与结果
仿真清洁 >3 万小时、噪声约 600 小时。对比 GAN、StoRM、FlowSE、LLaSE-G1 与内部变体。DGSE-IW（重要性加权）在多数据集上 MOS/SIM 最优或近最优且 WER 竞争力强；+T 延迟文本监督相对 WER 降 15.8%；+TG（真值文本）相对降约 33.1%。内部集上 DGSE-IW MOS 4.043、WER 0.099、SIM 0.344；URGENT 英文 WER 可到 0.153（+TG）。随机文本实验表明高失真时才更依赖文本。

## 结论
延迟文本感知与重要性码本加权在抑制幻觉、提升可懂度的同时保持感知质量，并统一增强与超分。未来方向为降延迟与多语扩展。

## 点评
抓住生成 SE 的“语义先于声学”约束，把幻觉问题从后验修补前移到生成顺序与损失权重。强度在消融清楚、码本重要性可复现；脆弱点是依赖 ASR/文本质量与仿真分布，真值文本推理是上界而非部署常态，低延迟场景需再压复杂度。
