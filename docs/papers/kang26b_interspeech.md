# What Do Neural Networks Learn for TDOA Estimation? A Cross-Architecture Probing Study

- 论文编号：3246
- 报告人：Yaozhong Kang
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/kang26b_interspeech.pdf

## 问题
神经网络在噪声/混响下常优于 GCC-PHAT 做 TDOA，但其内部是否复现 GCC-PHAT 的交叉功率与 PHAT 白化步骤尚不清楚，影响混合管线设计。

## 方法
以双麦 STFT 窄带观测为输入，训练 MLP-per-bin、1D-CNN、Transformer 回归延迟。用线性（及非线性对照）probe 解码各层是否含 cross-power、PHAT 相位与 τ；辅以梯度频率归因与单频 bin 掩蔽因果检验。在合成噪声、混响、LibriSpeech 仿真通道与 LOCATA 真实阵列上评测。

## 实验与结果
各架构均能高 R² 解码 cross-power（如 Transformer 0.94），而理论 PHAT 相位持续低（≤0.21）；网络另编码 |G12|（R²=0.82）。学习权重与 |G12| 正相关（r=+0.53）、与 1/|G12| 反相关；掩蔽 ΔMAE 与归因高度一致（r=+0.94）。经典与神经 GCC 在加性噪声下去掉 PHAT（Flat）多数条件更优；LOCATA 上 PHAT 仍是最佳经典加权，但端到端 Transformer MAE 5.75，约为经典机会水平的约 2.4× 更低误差。

## 结论
跨架构共享的是交叉功率计算，而非 PHAT 白化；网络学到保留频带可靠性的幅度感知加权。PHAT 对神经管线常是信息瓶颈，但在真实混响经典设定下仍有价值。

## 点评
把经典算法步骤变成可探针靶标，再辅因果掩蔽，解释力强、对 NGCC 设计有直接建议。局限是单声源假设与频谱输入；波形端模型与更强混响下是否转向去混响类特征，正文留作开放问题。
