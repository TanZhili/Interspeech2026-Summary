# Towards Fine-Grained Temporal Perception: Post-Training Large Audio-Language Models with Audio-Side Time Prompt

- 论文编号：745
- 报告人：Yanfeng Shi
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/shi26b_interspeech.pdf

## 问题
LALM 在语义理解上较强，但对细粒度时间感知不足，难以精确推断声事件起止时间，限制了 audio grounding、sound event detection 等时序任务。现有时间标注数据或特殊时间 token 仍缺显式物理时间坐标，且 SFT 的 token 级交叉熵对边界小偏差惩罚过重，与对齐质量目标不一致。

## 方法
提出 TimePro-RL：先用 Audio-Side Time Prompt（ASTP），按音频编码器帧率把 Timestamp Token（如 `<0.04>`）交错插入音频特征序列，经 Timestamp Embedding 层映射；嵌入用对应数字子词嵌入均值做语义初始化，训练时冻结以防语义漂移。随后 SFT 教模型使用该 prompt，再以 GRPO 做 RL 后训练。奖励以 Event-based F1（Eb-F1）为主；当组内主奖励方差过低时，与辅助奖励（AG/SED 用 mIoU，DAC 用 METEOR）做逐元素乘积，形成 advantage-driven adaptive temporal reward。在 Qwen2-Audio 与 Qwen2.5-Omni 上用 LoRA（r=8, α=32）做参数高效微调。

## 实验与结果
任务包括 FTAR 上的 Audio Grounding 与 Dense Audio Captioning，以及 DESED 上的 Sound Event Detection。TimePro-RL 后训练的 Qwen2.5-Omni 在 AG 上达到 R@0.5=80.1、R@0.9=39.8、mIoU=74.4，SED Eb-F1=57.6，DAC METEOR=33.9、Eb-F1=40.7，优于同数据 SFT 的多种 LALM（含 TimeAudio、Kimi-Audio 等）。消融显示随机初始化 ASTP 会退步，语义初始化有效；再加自适应 RL 相对仅 Eb-F1 奖励更均衡，尤其挽回 DAC 的 METEOR。注意力可视化显示对 Timestamp Embedding 的关注集中在事件起止边界。

## 结论
作者认为 ASTP 与面向时间对齐的自适应 RL 协同，可显著提升 LALM 的细粒度时间感知；未来拟扩展到 CoT 等复杂推理场景。

## 点评
思路是给音频侧显式“时间坐标”，再用与评测指标对齐的 RL 修边界，直击 SFT 对时间偏差不友好的问题。语义初始化与主辅奖励自适应切换是务实设计。可能脆弱处在于强依赖帧率固定的时间 token 网格与较短时长覆盖（文中 0–30 s、0.04 s 步长），以及 RL 仅单 epoch、子集 10,200 样本——复杂重叠事件与更长音频上的外推仍需观察。
