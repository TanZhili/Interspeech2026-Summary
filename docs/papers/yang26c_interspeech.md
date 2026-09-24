# MUGEN: Evaluating and Improving Multi-audio Understanding of Large Audio-Language Models

- 论文编号：530
- 报告人：Chih-Kai Yang
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/yang26c_interspeech.pdf

## 问题
实用 LALM 常需同时理解多段音频，但现有评测多为单音频、维度窄、输入规模小，多音频比较与随候选数扩展的能力未系统刻画。

## 方法
提出 MUGEN：35 任务、1750 实例、7 维（语义、说话人、情感副语言、时序、场景事件、音乐、组合推理）；每题 5 个音频候选（部分另加参考音频），文本约束选最佳，强制跨音频比较。基准开源模型与 Gemini-3-pro，以及 Whisper+Gemini 级联。改进：CoT、Self-Consistency，以及 Audio-Permutational Self-Consistency（打乱候选顺序再多数投票，可与 CoT 组合）。

## 实验与结果
开源整体准确率约 17–29%，接近级联；Gemini High 约 69.6%，仍远未饱和。语义维明显高于非语义，时序等更难。候选从 2 增至 5 时准确率明显下降（如 Qwen 五候选仅保留约 66%/48% 的两候选水平，有无参考音频）。APSC 增益最大：Gemini Low 最高约 +6.28%，APSC+CoT 约 +6.74%；CoT 单独近乎无效或略伤。

## 结论
多音频理解是当前 LALM 短板，且随输入数扩展恶化；音频排列自洽优于单纯 CoT，暴露位置敏感与感知瓶颈。

## 点评
用 audio-as-option 堵住转写捷径，对非语义与扩展性诊断很有力。Gemini 与开源鸿沟大；APSC 算力贵。部分数据含 TTS，真实嘈杂多源场景仍待验证。
