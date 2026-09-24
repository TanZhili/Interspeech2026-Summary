# Hidden Priors in Speech LLMs: Speaker Identity Shapes Emotional Perception

- 论文编号：1238
- 报告人：Hsing-Hang Chou
- 程序：Wednesday 30 September 2026 / Speaker Identity, States, and Traits in Paralinguistics
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chou26_interspeech.pdf

## 问题
Speech LLM 做情感识别时，提示中的说话人身份描述（口音/国家/语言）可能引入隐藏先验，即使音频不变也会改变判断；需量化、解释并削弱该敏感性。

## 方法
固定音频，仅替换身份语句（12 种描述 × 口音/国家/语言），在 MSP-Podcast 与 BIIC-Podcast（各四类情感、每类 2000 条评测）上测 Qwen2-Audio、Qwen3-Omni、Phi-4、DeSTA2.5-Audio。用 F1 gap（各情感最优–最差身份差的 RMS）+ 置换检验；用音频 token 显著性 CDF 差检验预测跳变是否伴随声学关注转移。以 LoRA（base / mix 身份提示）微调 Qwen2-Audio 降敏。

## 实验与结果
预训练模型 F1 gap 均显著大于零；语言条件往往 gap 最大。标签跳变组显著性偏移更大，支持 H2。LoRA（尤其 mix）把 MSP 语言 gap 从约 0.12 压到约 0.0025，多数设置与置换零假设无显著差异；同时 macro-F1 升至约 0.67。

## 结论
文本身份线索 alone 即可系统偏移 Speech LLM 情感预测；轻量 LoRA 可大幅降低该敏感性。局限：真实身份属性更复杂、多线索组合未充分探索。

## 点评
固定音频的提示扰动实验设计干净，把“偏见”从数据分布问题变成可控因果探针。语言条件最强暗示模型把“说什么语”当成强情境先验；mix 训练使身份与标签解耦，是实用缓解路径。
