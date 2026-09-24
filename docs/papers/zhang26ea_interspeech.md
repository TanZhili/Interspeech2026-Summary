# AcoustEmo: An Utterance-Aware Acoustic Q-Former for Open-Vocabulary Emotion Reasoning

- 论文编号：2364
- 报告人：Liyun Zhang
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26ea_interspeech.pdf

## 问题
面向开放词汇情感推理的 MLLM 常把整段音频压成全局 token，难以捕捉单句内部的微韵律、突变语调等局部时序线索，限制了 EMER 等需细粒度声学证据的任务。

## 方法
提出 AcoustEmo：视觉仍用 ViT + Global Visual Q-Former；声学用时间戳同步滑动窗按转写句边界切分帧级特征（如 ImageBind），每句经 Utterance-Aware Acoustic Q-Former（K=32 可学习 query 交叉注意）得到局部 token，并与全局 Acoustic Q-Former token 拼接；再与指令（含时间戳）一起送入 LLaMA-2（7B）+ LoRA 做因果语言建模。

## 实验与结果
在 EMER-Fine 测试集上，AcoustEmo Avg/Acc/Recall 为 67.55/65.40/70.15，超过 MicroEmo（66.21）与 AffectGPT（61.75）等。消融：去掉 Utterance-Aware A-QF 降至 61.20；固定 2s 窗降至 62.85；去掉全局声学 Q-Former 降至 64.10。定性例子中能抓住句末短暂声颤并预测 anxious/concerned，而全局基线判为 calm/neutral。

## 结论
句级对齐的局部声学建模可增强开放词汇情感推理；全局上下文仍有补充价值。未来拟做连续效价–唤醒追踪并降低动态切分开销以支持端侧实时应用。

## 点评
把 MicroEmo 一类“局部视觉动态”思路迁到声学，并用转写时间戳做软对齐，问题定位准确。相对全局池化的增益与消融一致，说明边界对齐比单纯加窗更重要。讽刺（声学与语义冲突）与低 SNR 叠音仍会出错，提示局部 token 质量仍受前端分离与噪声制约。
