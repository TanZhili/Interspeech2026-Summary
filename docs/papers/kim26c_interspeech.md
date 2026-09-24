# Mixture Consistency Learning for Robust Speaker Verification in Noisy Environments

- 论文编号：364
- 报告人：Seung-bin Kim
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26c_interspeech.pdf

## 问题
噪声鲁棒 SV 常加 SE 前端，但用“干净”参考做重建会连带恢复通道等非判别因素，反而伤说话人区分。

## 方法
提出 MCL-SV：双解码 SE（说话人路径 + 背景路径），用 mixture consistency 约束两路输出之和重建原始混合输入（自监督、无干净参考）；SV 目标仅耦合说话人路径。后端对接说话人网络（文中与 ReDimNet-B2 等对比），在 VoxCeleb + MUSAN 等噪声条件评测。

## 实验与结果
Vox1 训练时平均 EER 3.03%，低 SNR（如 0 dB）更稳。Vox2 上平均 EER 1.19%，相对复现 ReDimNet-B2 与带 SE 基线分别约改善 16.2%/12.5%，干净条件亦优于基线约 14.4%。消融显示含 MC、弱化目标 SE/NE 的配置优于纯目标重建。

## 结论
相对强制贴合“干净”参考，用输入自一致性分离说话人与干扰更利于噪声鲁棒 SV。

## 点评
把 MixIT/一致性思路接到 SV，直接挑战“SE 一定要有干净标签”的默认设定。干净高 SNR 上未必全面领先；优势集中在严苛噪声，部署需按场景权衡。
