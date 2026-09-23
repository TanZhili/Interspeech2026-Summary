# FastWave: Optimized Diffusion Model for Audio Super-Resolution

- 论文编号：2721
- 报告人：Nikita Kuznetsov
- 程序：Wednesday 30 September 2026 / Dereverberation, Bandwidth Extension and Restoration
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/kuznetsov26_interspeech.pdf

## 问题
音频超分辨率需要从低采样率（如 8 kHz）估计缺失的高频成分并重建到更高采样率（如 48 kHz）。现有深度方法中，扩散与流模型往往参数量大、推理慢；GAN 虽更快，但仍多为高参数网络。面向消费级低资源/端侧场景时，训练与推理成本都偏高。

## 方法
FastWave 基于 NU-Wave 2，做任意输入采样率到 48 kHz 的超分。核心改动有两类：
1. **EDM 风格扩散**：将噪声预测改为去噪器 \(D_\theta(x+n;\sigma)\approx x\)，采用输入–输出 preconditioning、加权 L2 去噪损失，并从数据估计 \(\sigma_{\mathrm{data}}\)；噪声水平按 log-normal 采样。推理用概率流 ODE 的一阶 Euler 求解与 EDM 连续噪声日程，可用较少 NFE（如 4/8）。
2. **结构压缩**：在 STFC/BSFT 等局部块中用深度可分离卷积替代标准 Conv1d，并加入 Global Response Normalization（GRN），参数量约 1.3M、约 50 GFLOPs 量级复杂度。

## 实验与结果
在 VCTK（100 说话人训练 / 8 测试，目标 48 kHz）上评估从 8/12/16/24 kHz 上采样。有限算力设定下（单卡 V100、约 30 小时量级），EDM 相对原 NU-Wave 2 baseline 收敛更好；FastWave 与 EDM 接近。与预训练/大容量模型对比（Table 2）：FastWave 4 NFE 在 8→48 上 SNR≈18.75、LSD≈1.18；24→48 上 SNR≈27.09、LSD≈0.93。相对 AudioSR 明显更优；相对 FlowHigh 在 LSD 上略逊但 SNR 往往更好。复杂度：1.3M 参数、12.87 GFLOPs/次函数评估，4 NFE 的 RTF≈0.16。

## 结论
作者给出一套可在中等算力下训练的轻量扩散超分管线，参数少、NFE 可减半，并具备面向消费设备流式/低资源部署的潜力。

## 点评
这篇工作的抓手是「扩散超分如何在质量可接受时把参数、NFE 和训练成本一起压下来」，而不是再堆更大生成器。强项是把 EDM 训练/采样配方直接迁到 NU-Wave 2，并用 ConvNeXtV2 式深度可分卷积+GRN 做结构性减参，路线清晰、可复现性强。脆弱点在于：与单步 FlowHigh 相比仍是多步 ODE、LSD 不占优；主要评测在干净 VCTK 说话人超分，对噪声/音乐等域外鲁棒性正文未深入验证。
