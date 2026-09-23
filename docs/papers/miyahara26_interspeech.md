# Evaluating Zero-Shot Cross-Lingual Stuttering Detection Based on Self-Attention Weights of Temporal Acoustic Vector Sequence

- 论文编号：1886
- 报告人：Genzo Miyahara
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/miyahara26_interspeech.pdf

## 问题
口吃事件检测（SED）依赖大规模标注语料，低资源语言难以直接训练；跨语种迁移时，音素/词汇层面的重复与语言相关，而“相似声学模式的重复/延长”结构可能更跨语。需检验何种表征能在零样本跨语设定下保持检测能力。

## 方法
SAWF：对冻结的时序声学向量序列 S 计算 X=SS^T/√d_S（可多层堆叠），将自注意力权重矩阵当“图像”，用改过的 VGG-19（全局平均池化以支持变长）做多标签 SED。骨干对比：源语 ASR 微调 wav2vec2、xlsr-53、Whisper-medium encoder。零样本：英（SEP-28k）、汉（AS-70）、德（KSoF）互训互测，含 Cmn+En→De 多源。

## 实验与结果
单语上 SAWF 与基线互有胜负（英多类更强，汉基线常更强）。零样本多数设定 SAWF 优于 Bayerl 风格基线；Whisper 骨干总体最强，xlsr 在部分重复类较弱。摘要称跨语 F1 可达单语设定的 77–98%。对德：Cmn+En→De 的 Whisper 在词重复 F1 0.40，优于 StutterFuse 的 0.20；在 block/prolongation/sound 等声学主导类仍落后 StutterFuse 约 10–23 点。多源优于单源；En→De 常优于 Cmn→De。

## 结论
SAWF 能降低对语言特定声学细节的依赖，尤其利于词重复等结构类；SOTA StutterFuse 在部分声学类仍领先。多语联合训练可进一步弥补语言距离。

## 点评
把“重复/延长”显式做成时间–时间相似图，归纳偏置清晰，适合跨语零样本。弱点是插话类受 Whisper 训练去 filler 影响、block 仍难，且相对检索增强 SOTA 在声学主导症状上仍有差距——说明结构特征与声学细节需要互补而非替代。
