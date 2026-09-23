# ETC-TTS: Emotion Trajectory Learning for Controllable Emotional Text-to-Speech

- 论文编号：3088
- 报告人：Gaeun Kim
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kim26u_interspeech.pdf

## 问题
情感强度控制常在推理时对情绪嵌入做缩放/插值，中间强度并未在训练中显式学习，导致强度单调性不稳、自然度下降。作者指出这造成训练–推理不匹配：模型只在离散端点上优化，却指望推理期潜空间操纵给出一致感知强度。

## 方法
**ETC-TTS** 把强度重写为潜在风格空间中的 **中性→目标情绪轨迹**：
1. **RVQ 情绪原型**（L=3）：每级码本大小=情绪类别数，与标签一一对应；k-means 初始化 + 级联 triplet 聚类损失，并周期性复活未使用码字。
2. **原型锚定 flow matching**：源为中性原型加噪、目标为情绪原型；学习条件于音素特征与风格标签的速度场；推理用轨迹参数 \(t\in[0,1]\) 调节强度，无需参考音频。
总损失含 FastSpeech2 重建、RVQ、聚类、flow（\(\lambda_f=30\)）与中性对齐项。三阶段训练：原型初始化 → 冻结 flow 先稳抽取器 → 联合训练。

## 实验与结果
数据：AIHub 韩语情感语音（约 80h，七情绪）与 ESD 英语。骨干统一 FastSpeech2 + HiFi-GAN。相对标签条件、RA、SF：
- ESD：Proposed N-MOS 3.14、E-MOS 3.78、EmoAcc 92.93%；AIHub 上 E-MOS/CER 等亦更优。
- 强度单调性 AB 错误率在多数情绪/强度对上低于 RA/SF；emotion2vec 概率随 \(t\) 更平滑单调。
- 跨强度 UTMOS/CER 更稳定；用 SER 嵌入或高斯先验替代中性锚定会伤 EmoAcc 或自然度。

## 结论
作者认为应在训练中学习中性–情绪轨迹，而非推理期启发式嵌入操纵；在韩/英数据上获得更稳的单调强度控制并保持竞争力音质。

## 点评
问题诊断很准：强度控制的失败往往不是「没标量」，而是「中间态从未被监督」。把 rectified flow 端点钉在 RVQ 原型上，把可控 \(t\) 变成真正学过的路径参数，比 SF/插值更有训练一致性。脆弱点：原型与类别数硬绑定，细粒度/复合情绪表达受限；flow 权重大（\(\lambda_f=30\)）需小心与声学重建权衡；主对比都在同一 FastSpeech2 骨干上，换现代零样本骨干时轨迹模块是否仍成立未验证。
