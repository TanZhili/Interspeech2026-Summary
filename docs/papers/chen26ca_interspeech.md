# Inside the Latent Flow: Causal Deciphering of Attention Dynamics in Audio Separation Foundation Models

- 论文编号：2684
- 报告人：Yuxuan Chen
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/chen26ca_interspeech.pdf

## 问题
Flow-matching transformer（如 SAM Audio）分离效果强，但多模态条件如何注入、注意力如何沿 ODE 轨迹演化仍不透明；直接把视觉扩散中“cross-attention=语义锚定”的假设搬到音频可能误导。

## 方法
在推理期对 SAM Audio 做确定性因果探针（不改权重）：(1) Orthogonal probing 分别清零 additive text injection、cross-attention 或强制均匀注意力；(2) Causal freezing 按注意力熵变化率划分 stable/fast 层并中途冻结；(3) Gate hijacking 强行打开 span gate（γ=+5.0）检验时序分段几何能力。据此提出训练无关的 Layer-Selective Attention Caching（LSAC）：对已收敛的 stable 层缓存注意力矩阵（V 仍每步重算），设 SAFE/BALANCED/AGGRESSIVE 冻结步配置。

## 实验与结果
在 SAM Audio Small（12 层、16 步 Euler）与 3B（22 层）上，Clean/Noisy/Env 三档共逾万次 ODE 运行。Additive 消融对语义轴冲击最大（STOI Δ=−0.219，d=−0.89）；清零 CA 对声学轴冲击大（SAR −9.85 dB）。Stable 层可早至 Step 4 冻结（SI-SNR 仅劣 0.05 dB）；Fast 层 Step 8 冻结劣 0.66 dB。Gate 劫持使 L06 Block Ratio 5.76→9.55，同时 SI-SNR 崩约 14.6 dB。LSAC 约省 25% self-attention 计算，质量保持明显优于 naive 减步（Noisy 档可达约 6.7× 相对优势）。

## 结论
文本条件呈非对称双通路：additive 管语义身份，cross-attention 管声学结构；层间异步“搭脚手架再雕细节”；模型会主动抑制离散时序边界先验以保连续流稳定。LSAC 把该洞察转成可扩展加速。

## 点评
用因果干预而非被动看注意力图，直接挑战“CA=语义 grounding”的常见迁移假设，并落到可部署缓存策略。结论依赖 SAM Audio 一类 flow DiT；gate 与冻结阈值阈值模型特定，推广到其他分离骨干需再验证。PDF 抽取中部分图表数字有乱码，正文表格与叙述仍可读。
