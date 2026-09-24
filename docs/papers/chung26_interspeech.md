# Localizing and Editing Knowledge in Large Audio-Language Models

- 论文编号：2066
- 报告人：Jiaheng Dong
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/chung26_interspeech.pdf

## 问题
LALM 在语音理解上表现强，但训练语料静态，可能编码过时或错误事实。文本 LLM 的 locate–then–edit（如 ROME、MEMIT、AlphaEdit）依赖离散 token 腐蚀，无法直接处理连续语音，也不清楚事实知识在音频编码器与 LLM backbone 中如何分布，以及编辑是否会破坏音频–文本对齐。

## 方法
构建面向 LALM 的语音事实定位与编辑基准，并提出语音驱动的 locate–then–edit 框架。事实表示为三元组 (s, r, o_c)，用口语 prompt 探测。定位阶段用 speech-aware causal tracing：clean / corrupted / corrupted-with-restoration 三轮前向；借 WhisperX 对齐定位主语跨度，对音频编码器首层输入加高斯噪声腐蚀，再按层窗（±4）恢复 clean 隐状态，用 Indirect Effect / AIE 标定关键层与 MLP、attention 模块。编辑阶段基于线性 key–value 假设做参数扰动，比较单层 / 多层编辑，以及仅音频、仅文本与顺序跨模态（先改音频再改 LLM）策略；多层编辑对受保护 key 做零空间投影以降低干扰。骨干为 Qwen2-Audio-7B-Instruct。

## 实验与结果
数据基于 CounterFact 与 Known-1000，经 Gemini 2.5 Flash TTS 转语音；定位分别保留 250 / 100 条模型预编辑正确样本，编辑用 500 条 CounterFact 子集。指标为 Efficacy / Paraphrase / Neighbor Score 及均值 S。因果追踪显示事实联合编码于音频编码器与 LLM，CounterFact 上音频中后层（约 25–31）与主语首词 AIE 更强，MLP 在文本中层贡献大。编辑上跨模态单层整体最优（S=77.60，ES=95.20，PS=78.70，NS=64.72），优于单模态编辑与微调；带参数重置的多层跨模态可达 79.67。层与词位选择上，AIE 更高的位置编辑效果更好。

## 结论
作者认为语音感知因果追踪能定位口语事实存储位点，并指导更有效、更特异的参数更新；跨模态协同编辑优于标准微调。工作为语音 AI 中细粒度事实控制提供初步可行路径。

## 点评
这篇工作把文本模型编辑里的因果追踪迁到连续语音上，关键在于用对齐框定主语帧并在音频路径注入噪声，从而回答“事实藏在编码器还是语言骨干”。结果强调音频层是口语事实的锚点、跨模态编辑更稳，这与 LALM 的双塔结构一致。脆弱点在于依赖 TTS 合成的事实基准与单一骨干（Qwen2-Audio），以及单层编辑需样本间重置参数，多层累积更新仍易伤 Neighbor Score，真实噪声语音与开放域事实外推仍待验证。
