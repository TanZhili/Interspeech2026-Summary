# Audio-Cogito: Towards Deep Audio Reasoning in Large Audio Language Models

- 论文编号：988
- 报告人：Longhao Li
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/li26o_interspeech.pdf

## 问题
现有 LARM 的 CoT 常僵硬、接地弱；公开音频数据多为短标签/字幕，高质量深度推理数据稀缺且多依赖闭源 API，格式与目标模型不匹配还会损害内在推理。

## 方法
开源方案 Audio-Cogito + Cogito-Pipe 四阶段：多域数据采集（声/语/乐及混合，约 545k）；Qwen3-Omni-Instruct 以约 500 条种子题 few-shot 构造 QA（含难负选项）；Qwen3-Omni-Thinking 自蒸馏自由格式 CoT（生成时不给金标答案，强制听音频）；QA 一致性 + Instruct 作 judge 滤幻觉。再对 Thinking 底座 LoRA SFT 一 epoch（ms-swift，lr 1e-5）。评测用 MMAR Acc、Rubrics、仅正确样本上的 CRS。

## 实验与结果
MMAR：Acc 71.70%、Rubrics 62.22%、CRS 0.87，开源 LARM/LALM/OLM 中领先，相对 Qwen3-Omni-Thinking Acc +约 5.44%（相对提升表述），混模态提升明显；部分指标接近或超过 Gemini 2.0/2.5 Flash、GPT-4o Audio 等。挑战赛中位列前列（与官方榜单第 3 档 Acc/Rubrics 一致量级）。

## 结论
全开源数据管线 + 自蒸馏可显著增强深度音频推理并缩小与部分闭源差距；释放 545k 数据集与代码。

## 点评
自蒸馏对齐“生成格式=训练格式”，并故意藏答案逼模型听声音，针对模板化/捷径 CoT。质量仍大体由同族 Omni 模型闭环决定，多样性上限与 judge 偏差需警惕；相对冠军级两阶段 RL，本文更偏高质量 SFT 路线。
