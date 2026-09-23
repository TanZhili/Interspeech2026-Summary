# Pruning as Regularization: Sensitivity-Aware One-Shot Pruning in ASR

- 论文编号：3411
- 报告人：Julian Irigoyen
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/irigoyen26_interspeech.pdf

## 问题
剪枝常被当作训后压缩；编码器–解码器 ASR Transformer 是否存在过参数冗余，使无微调的一次性幅度剪枝反而改善泛化，尚缺系统敏感度诊断。

## 方法
对 Whisper-small（244M）做训后梯度与对角 Fisher 敏感度诊断；按模块/层（早中晚）做无结构幅度剪枝，无微调。主评 LibriSpeech test-other（基线 WER 11.64%），掩码原样迁到 Common Voice、TED-LIUM。敏感度引导组件级稀疏度分配。

## 实验与结果
解码器整体更脆弱；全局剪枝 30–40% 崩溃。解码器自注意力 50% 剪枝：test-other 绝对降 2.38%；编码器末四层 50%：降 1.72%。解码器早层/FFN 极脆。40.8% 稀疏度下敏感度感知压缩近保基线，全局幅度剪枝则塌。跨语料增益可迁移。

## 结论
一次性幅度剪枝可作隐式正则；解码器自注意力与深层编码器冗余可剪，解码器早期与 FFN 需保护。方法模型无关但需按架构重验敏感度剖面。

## 点评
把“剪枝=压缩”翻成“剪枝=正则”，并用一/二阶诊断对齐实证，视角新鲜。强在无微调即增益与跨库迁移；弱在非结构化稀疏未加速实际推理，且相对某流水线基线报告，不宜与官方 Whisper 数字硬比。
