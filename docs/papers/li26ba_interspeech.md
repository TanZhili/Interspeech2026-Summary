# Resonate: Reinforcing Text-to-Audio Generation via Online Feedback from Large Audio Language Models

- 论文编号：1823
- 报告人：Xiquan Li
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/li26ba_interspeech.pdf

## 问题
TTA 上已有 RL 多采用离线 DPO，并以 CLAP 作奖励：偏好数据与策略脱节易分布漂移，CLAP 有 bag-of-words 倾向，奖励偏粗、与人对齐不足。在线 RL 与更细粒度奖励在 TTA 中仍少见。

## 方法
Resonate：MeanAudio 风格 Flux Transformer（16 MMDiT + 36 DiT，470M），FLAN-T5 条件，先在约 3.7M 对/1 万小时语料上 Conditional Flow Matching 预训练。再将去噪建成 MDP，用 Flow-GRPO：对每条 prompt 采 G 条轨迹，组内标准化优势，裁剪策略比 + KL 到参考策略；确定性 ODE 改为等价边缘的 SDE 采样以引入探索。奖励用 LALM（训练期 Qwen2.5-Omni）对 AQA 问题“音频是否包含文本描述事件？”的 Yes/No 归一化概率（AQAScore）；评测用另一模型 Qwen3-Omni-Instruct 降奖励黑客风险。后训练：AudioCaps 训练 prompt，G=24，a=0.7，β=0.04，1000 步。

## 实验与结果
TTA-Bench Accuracy（1500 prompt）：Resonate-GRPO 相对预训练全面提升（AQAScore 0.651→0.737，PQ 5.923→6.064，CLAP 0.476），并在多项上达 SOTA；主观 OVL 3.86、REL 3.83。消融：DPO/SFT 增益有限或降质量；直接 GRPO 优于 SFT+GRPO；AQAScore 奖励总体优于 CLAPScore；噪声 a=0.7、更大 G 更稳。25 NFE 推理。

## 结论
在线 Flow-GRPO + LALM 细粒度奖励可同时提升 TTA 音质与语义对齐；Resonate（470M）在 TTA-Bench 上达到新 SOTA。

## 点评
把“离线偏好 + CLAP”两条瓶颈一起拆：在线组相对优势缓解分布漂移，LALM-AQA 奖励补时间/组合推理。与图像 Flow-GRPO 同构迁移到音频较自然。需警惕奖励模型与评测模型虽不同仍属同类 LALM 家族；SDE 噪声与 G 需调，噪声过大可奖励黑客；SFT 在嘈杂 AudioCaps 上伤音质，说明后训练数据质量仍关键。
