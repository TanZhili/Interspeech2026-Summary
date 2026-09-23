# Structured Prompting vs. Self-Training for Audio Reasoning Under Limited Data and Compute: Lessons from Interspeech Audio Reasoning Challenge 2026

- 论文编号：2880
- 报告人：Steven Au
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/noronha26_interspeech.pdf

## 问题
在高质量音频推理轨迹稀缺、算力有限时，应优先提示工程、自动提示搜索，还是自训练改权重？需在同一强底座上比较资源—收益折中。

## 方法
底座 Qwen3-Omni 30B，三路线：(1) Reinforced Self-Training：每题采 16 条轨迹，仅保留成功率 26–75% 的 learning-zone 正确轨迹，qLoRA 三轮迭代；(2) DSPy MIPROv2 自动提示优化；(3) 基于错误分析的结构化提示迭代（Expert Analyst → Category-Aware → Targeted Hints → Structured Reasoning：HEARD→ANALYSIS→ANSWER，禁止 Wait/Actually 式自我推翻）。vLLM 推理，提示实验 bfloat16，ReST 为 4-bit。

## 实验与结果
MMAR 1000 题：基线 67.1%；Structured Reasoning 72.6%（+5.5），16 子类中 13 类提升；MIPROv2 63.3%；ReST 64.7%（低于 4-bit 基线 65.7%）。learning-zone 仅约 21.4% 题、4361 训练样本，对 30B 模型过稀；辅助 CountingQA/MusicBench 迁移不佳（如 Music Theory −15.4%）。

## 结论
资源受限时，系统错误分析+结构化推理格式优于自动提示搜索与稀疏自训练；先激活既有能力再考虑微调。

## 点评
结论实用：对已很强的 Omni 模型，格式约束比再喂少量自生成轨迹更划算。局限是单模型单基准、部分子类样本极少，且 16-bit vs 4-bit 比较仍有精度混杂；ReST 失败更像数据与域失配，不否定大规模高质量 RL/SFT。
