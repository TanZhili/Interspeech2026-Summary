# AV-FlowSep: Audio-Visual Target Speaker Separation via Flow Matching

- 论文编号：1960
- 报告人：Pattara Tipaksorn
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/tipaksorn26_interspeech.pdf

## 问题
音视频目标说话人分离中，判别法可懂度强但谱过平滑；扩散生成法听感更好却需约 30 步迭代、推理慢。需要既少步高效又保持感知质量、并能跨数据集泛化的方案。

## 方法
AV-FlowSep 将分离建模为条件流匹配：源为混合 mel、目标为干净 mel，直线 OT 路径上向量场恒为 Mx1−My。DiT（DiT-S：12 层、隐维 384）估计向量场，时间步经 AdaLN 注入，TalkNet-ASD 视觉前端特征经跨注意力条件化；估计 mel 用 Vocos 声码器还原波形。推理 Euler，N_steps∈{1,5}。

## 实验与结果
VoxCeleb2 训练/域内，LRS2 零样本；speech–speech 与 speech–noise（AudioSet，SNR −5–5 dB）。对比 SepFormer、VisualVoice、AV-MossFormer2、AVDiffuSS（30 步）。单步 AV-FlowSep 在噪声场景 DNSMOS/MCD 常最优（如 VoxCeleb2-AudioSet MCD 4.400）；speech–speech 与更大数据训练的 AV-MossFormer2 接近。零样本 LRS2 退化较小。优势方/弱势方 PESQ 差距更小；全脸条件混淆率 12.60%（VisualVoice 唇区仅 0.11%，MossFormer2 33.90%）。

## 结论
条件流匹配 + DiT 可实现单步高质量音视频分离，数据效率与跨域稳定性较好；未来需缓解视觉身份捷径、扩展多说话人与下游 ASR。

## 点评
把“混合→干净”直接当直线流，天然适配少步甚至一步推理，相对扩散分离很务实。声码器路径会引入压缩/相位误差，故需同时看参考与无参考指标；全脸条件提升质量但带来混淆，说明视觉捷径仍是音视频分离的结构性风险。
