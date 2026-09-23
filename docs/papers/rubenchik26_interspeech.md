# Latent Flow Matching Based Speech Separation Using Speaker Diarization

- 论文编号：1401
- 报告人：Sharon Gannot
- 程序：Tuesday 29 September 2026 / Target Speaker Extraction, Speech Separation and Audio Understanding
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rubenchik26_interspeech.pdf

## 问题
判别式分离易过平滑；生成式虽保真，但条件弱时易 speaker confusion（忽略条件、反复抽同一人）。希望用 diarization 从混合物自取说话人线索，且尽量只训练轻量生成模块。

## 方法
冻结 EEND-EDA、mel-VAE、vocoder：由 EEND 得说话人 attractor 与活动概率，按活动池化后拼接为条件，经 FiLM 注入潜空间 Flow Matching U-Net；输入为混合物潜变量与中间噪声潜变量拼接。训练用 PIT 选排列；推理引入训练无关的 Adversarial Speaker Guidance（ASG），用干扰说话人速度场作负条件并与 CFG 组合。另做 ECAPA enrollment 变体作对照。

## 实验与结果
LibriSpeech 动态混合训练（SIR [−5,5] dB），LibriMix 16 kHz min 测试。Ours：OVRL 3.20、DNSMOS 3.76、WER 13.26、SIM 0.81、TSIM 0.08%；无指导时 TSIM 0.14%。ECAPAv TSIM 高达 9.7–12.7%，SoloSpeech TSIM 0.8%。ASG 降低混淆并略提质量。相对 SoloSpeech（OVRL/DNSMOS/WER 更优），本文在无 enrollment 分离设定下混淆率显著更低、可懂度更好。

## 结论
仅训潜空间 FM U-Net，用混合物衍生 EEND attractor 条件化即可达可比感知质量，并大幅降低 speaker confusion；ASG 对 enrollment 与 diarization 条件均有益。

## 点评
关键是把 diarization attractor 当作“从混合物即时得到的说话人条件”，比通用验证嵌入更贴分离歧义；TSIM 指标直接量化“两路输出几乎同一内容”的失败模式。脆弱点在于依赖预训练 EEND 质量，且作者也指出更关键的是 attractor 可分性而非 DER，鲁棒分析留待后续。
