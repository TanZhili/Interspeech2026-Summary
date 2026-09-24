# Improving Stable Speech Synthesis Post-Training with ChatScorer and Margin-Based Preference Construction

- 论文编号：1881
- 报告人：Wenhuan Lu
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/niu26c_interspeech.pdf

## 问题
Codec TTS 后训练常把 CER/SIM 等异构指标融成标量奖励，候选分数分不开，偏好监督模糊，且难压制明显“机器感”对话输出。

## 方法
对每条提示采样多候选，用 CER+SIM+ChatScorer 融合排序；ChatScorer 为 WavLM+轻量 Transformer 的高斯打分头，并用 GRL 抗说话人泄漏。仅保留质量间隔足够大的组：正样本需满足 CER/SIM/Chat 阈值，负样本至少两项差，并按 margin 抽中间样本，构造 DPO / Rank3/5DPO 数据。对比 GRPO。对话式长文本提示约 2000 训 / 500 测。

## 实验与结果
Rank3DPO：CER 1.17%、SIM 失败率 0.10、BadRate 2.44%，优于 SFT/DPO/GRPO。Margin 构造优于直接按融合分选；加 ChatScore 对 CER 影响小但大幅降 BadRate 并抬高 MOS。ChatScorer 与人类 A/B 一致性高于 DNSMOS/UTMOSv2。

## 结论
辅助 ChatScorer + margin 偏好构造可把嘈杂多指标信号变成更可学监督，提升生成稳定性并抑制不良对话输出，同时保持可懂度与说话人相似。

## 点评
问题诊断（弱分离→模糊监督）清晰，稳定性指标（组失败率、BadRate）比只看均值 CER 更贴后训练目标。过滤丢弃大量提示（DPO~40%，RankDPO 更高）以换可学性；GRPO 未同用 margin 过滤，对比不完全对等。
