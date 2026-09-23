# Surgical-Robot Command Spotting: Safety-Aware Learning for Compositional Commands

- 论文编号：3372
- 报告人：Jaewon Lee
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26y_interspeech.pdf

## 问题
手术室语音控制助手机器人需在口罩与 OR 噪声下把短指令映射为结构化动作；误识可导致不安全运动。多数指令是“方向 × 步数(1–5)或连续运动”的组合，再加少量功能指令。把 51 类合成指令当独立分类会忽略组合结构，且 softmax 对“五步↔四步”与“五步↔一步”同等惩罚，不利于抑制灾难性大步误差。

## 方法
轻量共享编码器（2D conv stem + 1D depthwise-separable CNN，输出 24×128）上做头级时间注意力池化，分别预测方向、模式（function/step/continuous）与步幅。步幅用 CORAL 序次回归（阈值化二分类解码）；仅对 step 模式样本计步幅损失；训练期加 51 类辅助头稳定表示，推理去掉。英语 Google Speech Commands v2 预训练编码器后再在韩语 OR 指令上微调。输入 40-bin log-mel。

## 实验与结果
韩语 OR 指令集：5 说话人、7140 句、Clean/Noise×Mask/No-mask，LOSO。完整模型联合成功 95.36%，步指令 MAE 0.0338、灾难误差 CSE（|Δ|≥3）0.60%；优于 Flat-51（93.14%）、BC-ResNet-6（93.65%）及无 CORAL/无头级注意力变体。去掉预训练降至 88.97%。四条件下联合成功约 94.9–96.2%。模型约 181K 参数、5.99M MACs/2s。

## 结论
因子化+序次步幅学习在未见说话人与口罩/噪声条件下兼顾成功率与安全向步幅误差。局限：说话人少、评测为预切 2s 片段而非流式、噪声为回放重录，外推到真实 OR 流式闭环仍受限。

## 点评
把安全关键从“分类对不对”细化到“大步是否灾难”，CORAL 与 CSE/MAE 指标设计对齐手术控制风险。弱点是 5 人 LOSO 方差大（难说话人可拉低）、封闭词表与预切片段简化了真正始终在线检测与拒识问题。
