# Room Impulse Response Completion Using Signal-Prediction Diffusion Models Conditioned on Simulated Early Reflections

- 论文编号：531
- 报告人：Zeyu Xu
- 程序：Tuesday 29 September 2026 / Spatial Audio 2
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/xu26p_interspeech.pdf

## 问题
RIR 补全常要求固定时长（如 50–80 ms）的完整早期反射头；低阶 ISM 条件在窗口内不填满时，现有方法易在补全结果引入不连续。

## 方法
用 x-prediction 扩散（余弦调度，T=200）直接预测目标 RIR \(x_0\)，条件为任意最大反射阶的 ISM 早期响应 \(c\)（与噪声 \(x_t\) 通道拼接）。1D U-Net + 瓶颈膨胀卷积；损失 MSE 与可选 EDC 损失。Classifier-free guidance：训练时以 \(p_{CFG}=0.2\) 置零条件。构建配对 ISM（pyroomacoustics）与 Treble SDK 波场数据集（各 10k RIR，25 房间）。对比 Echo2Reverb。

## 实验与结果
Exp.1 纯 ISM：阶数变化时指标较稳，加 EDC 损失显著降 EDC MAE。Exp.2 混合训练（80% ISM + 20% Treble）测 Treble：低阶条件上早期残差能量比（RER）优于 Echo2Reverb；阶 5/7 时 EDC 更好；Echo2Reverb 在窗口未填满时可能出现不连续与后期虚假脉冲。扩散 200 步推理慢于基线单次前向。

## 结论
在不固定早期窗口填满的前提下，x-prediction + CFG 可用低阶 ISM 条件生成更现实的 RIR，并在混合数据上改善早期补全与 EDC；未来需加速推理并在实测 RIR 上验证。

## 点评
把“阶数受限 ISM”当作真实部署条件，并用 x-prediction 便于直接算 EDC，设计贴工程。CFG 用少量 Treble 样本撬动波效应是亮点。脆弱点是推理延迟与极低阶（如 order 1）时 EDC 仍可能差于基线。
