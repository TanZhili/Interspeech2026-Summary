# Spatially-Augmented Sequence-to-Sequence Neural Diarization for Meetings

- 论文编号：3473
- 报告人：Li Li
- 程序：Wednesday 30 September 2026 / Speaker Diarization 1
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26la_interspeech.pdf

## 问题
会议场景重叠、混响、说话人嵌入不可靠，多数神经说话人日志化仍只靠声学；空间方位是正交线索，但如何把稳健 DOA 注入可在线/离线的序列日志化模型仍缺清晰方案。

## 方法
SA-S2SND：用 SRP-DNN 估计多说话人 DOA（按帧 IDL 迭代峰检测，至多 2 源），将方位概率矩阵上采样后线性投影，残差加到 S2SND 编码器特征。骨干含 ResNet 提取器、Conformer 编码器与对称检测/表征解码器；多通道时再加交叉通道注意力。两阶段训练：Part A 单通道音频 + DOA（含仿真伪 DOA）；Part B 升级多通道 + DOA。损失 BCE + ArcFace。推理沿用 S2SND 滑窗，可在线后再离线重解码。

## 实验与结果
AliMeeting 远场阵列（NARA-WPE 去混响），无 oracle VAD、无 collar。Small 单通道加 DOA：总 DER 在线 16.03→15.35、离线 13.59→12.59（相对约 4.2%/7.4%）。8 通道 + DOA 相对仅声学基线进一步下降（如 Small E4 在线/离线 12.93/10.84）。Medium + 复合数据 + DOA 离线 DER 10.40，优于文中列出的若干对比系统（含 WavLM-Large 报告 10.80）。多说话人子集增益更大。

## 结论
显式 DOA 与交叉通道建模互补，统一支持单/多通道与在线/离线；仿真 DOA 减轻对匹配多通道语料依赖。未来需加强多说话人 DOA 稳健性。

## 点评
把 DOA 当“方位位置编码”注入，比盲通道融合更可解释；两阶段训练路径清晰。SRP-DNN 每帧最多 2 说话人与会议中 >2 重叠少见的统计相符，但极端重叠仍是盲区。SOTA 对比窗口/预训练条件不完全对齐，数字宜结合协议解读。
