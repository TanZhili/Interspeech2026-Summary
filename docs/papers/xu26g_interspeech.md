# Whisper-Aware LLM: Self-Supervised Uncertainty Learning for Robust Whispered Speech Recognition

- 论文编号：879
- 报告人：Gaopeng Xu
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26g_interspeech.pdf

## 问题
耳语缺少基频与谐波结构，声学不确定度高，导致常规 ASR 陷入准确率–可靠性权衡：要么对耳语识别差，要么为提高灵敏度而更容易把噪声幻听成语音。现有伪耳语数据增强存在分布差距，静态投影适配又难以随耳语变化动态调节。

## 方法
在 Qwen2-Audio 上增加轻量 Uncertainty Perception Module（UPM）与 Confidence-Fused Decoding。UPM 用两个自监督任务感知信号质量：F0 轮廓预测（MSE，由预测误差得到帧级置信度）与掩码频谱重建（时间平均得到全局不确定性向量）。解码时，全局向量经 MLP 变成 instruction embedding 作为系统提示；帧级置信度作为可学习标量加权的加性偏置调制 LLM 对声学帧的注意力。训练分三阶段：仅训 UPM 自监督 → 编码器/适配器/UPM/接口联合、LLM 冻结 → 端到端（ASR + 辅助损失，LLM 用 LoRA）。

## 实验与结果
基座为 Qwen2-Audio（Qwen-7B）。UPM 预训练混合 WenetSpeech/GigaSpeech 子集、AISHELL-1、LibriSpeech、wTIMIT、AISHELL6-Whisper 与噪声；微调用上述数据子集。AISHELL6-Whisper 耳语 CER 1.31%（相对此前最佳 Seed-ASR 的 1.58% 降约 17%），正常语音 CER 0.63%。英文 wTIMIT 多口音正常/耳语条件均优于对比系统。AISHELL-1 CER 1.34%、LibriSpeech-clean WER 1.91%。自建 Noise Hallucination Set 上幻觉率 4.5%（强基线多在 25% 以上）。消融：仅注意力调制 3.45%、仅全局指令 1.84%、完整模型 1.31%（基线微调 3.98%）。

## 结论
通过自监督感知信号不确定性并用置信度融合解码，模型在耳语 ASR 上达到文中报告的 SOTA，同时显著降低噪声幻觉，且不明显牺牲通用 ASR 能力。

## 点评
核心不是“把耳语学得更像正常语音”，而是先量化声学证据可靠度再约束生成，直接打在耳语场景的准确率–幻觉权衡上。全局指令对 CER 与幻觉率贡献更大，帧级注意力起补充作用；依赖 F0/频谱自监督与三阶段训练是否在其他 Audio-LLM 上同样稳定，正文未充分展开。
