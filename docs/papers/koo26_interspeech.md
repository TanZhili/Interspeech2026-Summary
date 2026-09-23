# VeRe-Flow: Guiding Flow Matching toward Clean Speech via Velocity Contrastive Regularization and Representation Alignment for Noise-Robust Bandwidth Expansion

- 论文编号：712
- 报告人：Sujin Koo
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/koo26_interspeech.pdf

## 问题
噪声鲁棒带宽扩展（NR-BWE）需同时补全高频并抑噪。标准 flow matching 只单向监督速度场，噪声下速度估计模糊，轨迹易偏离干净语音流形；现有方法在高频重建与抑噪之间仍难兼顾。

## 方法
VeRe-Flow 在 flow matching 上引入多层干净监督。源分布为高斯，目标为干净高分辨率 Mel；以噪声低分辨率 Mel 与冻结 XEUS 的 SSL 特征为条件。骨干在 FLowHigh 上加入 DiC 风格 Conv ResBlock（卷积–Transformer–卷积三明治）。损失：(1) VeCoR：吸引预测速度靠近干净速度、排斥噪声扰动高分辨率对应的噪声速度；(2) REPA 式表示对齐：将第一层 Transformer 隐状态经 MLP 与干净 XEUS 表示做余弦对齐。总损失为两者加权和。波形用 BigVGAN 重建。

## 实验与结果
数据为 Valentini-Botinhao（合并 84 说话人训练），评测官方测试集，输入经低通后下采样至 8 kHz，输出 16 kHz。主配置：高斯先验 + Euler，NFE=2。相对非生成与生成基线（含重训的 FLowHigh、NU-Wave2），提出方法 LSD 最低（1.10）、DNSMOS OVRL 最高（3.12），生成基线中 MOS 最高（4.14±0.65）。消融显示 XEUS 优于 WavLM / Wav2Vec 2.0；Conv ResBlock、XEUS、REPA、VeCoR 逐步带来增益。

## 结论
作者认为在速度与表示两层做干净导向正则，可有效引导 NR-BWE 的生成轨迹；在 Valentini-Botinhao 上全面优于对比的生成基线。据称是首次将速度对比正则用于语音生成。

## 点评
针对“噪声条件下流匹配速度歧义”这一具体失败模式，用干净/噪声速度对比 + 干净 SSL 对齐双向拉回流形，问题定位清晰。与纯条件 CFM 相比，额外监督直接约束轨迹方向。脆弱点在于依赖成对干净高分辨率与语义一致的噪声版本构造 \(u^{\mathrm{noisy}}\)，以及冻结 XEUS 的域匹配；消融也显示各模块对 LSD 与 DNSMOS 的贡献分工不同。
