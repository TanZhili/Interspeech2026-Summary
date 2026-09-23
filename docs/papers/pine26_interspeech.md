# Two Lessons Learned from the SGILE project: Efficient Building and Evaluation of TTS Voices

- 论文编号：3596
- 报告人：Korin Richmond
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pine26_interspeech.pdf

## 问题
绝大多数语言属低资源，难以按高资源范式用海量数据与大模型建 TTS；听者稀缺时传统 MOS 评测代价高。SGILE 项目需同时解决高效建声与高效评测。

## 方法
展示开源 EveryVoice TTS Toolkit：面向有限算力与少量音频（常仅数小时）从零建高质量音色，带向导降低非专家门槛。评测侧推广 Best-Worst Scaling（BWS）等相对选择范式，对比 AB：四刺激选最好/最差可等价约五对成对判断。演示为网页听测：盲评样本后揭示所用音色与数据量，并与其他用户跨语言偏好对照。

## 实验与结果
本文为 Show & Tell，不报告新的定量 TTS 分数；强调演示样本覆盖不同数据量与多语言，并引用项目前期工作称 BWS 更高效稳健。

## 结论
低资源 TTS 可用适度数据与工具链实现；BWS 等范式可在听者稀缺时提高评测信息量。后续 Own Your Voice 项目将把 EveryVoice 部署到强调数据主权的云环境。

## 点评
价值在社区工具与评测方法论的可体验展示，而非新声学模型。强项是把“少数据可建声”与“少听者可评测”绑在同一交互界面；局限是本文本身缺少对照实验数字，说服力依赖现场听感与已发表配套论文。
