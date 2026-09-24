# A Sensitivity Analysis of Multi-Event Audio Grounding in Audio LLMs

- 论文编号：1684
- 报告人：Taehan Lee
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/lee26o_interspeech.pdf

## 问题
Audio LLM 在复杂声学场景中的事件定位与幻觉可靠性研究不足：既有幻觉评测规模小或标签本体不一致，主流基准也未隔离“场景事件数”对 grounding/假阳的影响。

## 方法
从 AudioCapsV2（约 71K 片段）用 LLM 抽取并人工规范化 (source, attribute) 事件，得约 145K 事件、578 类常见事件；约 74% 样本含多事件。对 present-event 做存在性检测；absent-event 用 ReCLAP 音频对齐文本嵌入按相似度过滤（α=0.3）后采样，避免近义声学事件被误判为幻觉，共约 356K 负查询。评测 Qwen3-Omni-30B、Qwen2.5-Omni-7B/3B、Audio-Flamingo 3-7B，12 种提示（4 问句 × 3 回答约束），每模型约 50 万 yes/no 查询；并分析输出 token 置信度与 prompt 敏感性（Kendall τ_bias、复杂度间隙相关）。

## 实验与结果
事件数从 1 增到 5 时，present TPR 约降 29 pp，absent FPR 约升 8 pp。提示在高 TPR 与低 FPR 间强权衡（τ_bias 为负，约 −0.66 至 −0.90）。条件 FPR（正确识别 ≥75% present 时）仅比整体 FPR 低 ≤0.3 pp。正确回答置信度随事件数上升而下降；错误回答置信度趋势不一。SSL 音频嵌入的 erank 亦随事件数升高，支持复杂度代理合理。

## 结论
当前 SOTA Audio LLM 在多事件场景中区分“在场/不在场”仍困难；提示会诱导 Yes/No 偏差并与复杂度敏感性耦合；复杂度升高时模型更不确定。作者希望该评测推动忠实音频 grounding 研究。

## 点评
贡献主要在大规模、可控的多事件评测协议（规范化事件 + 声学对齐负采样），而非新模型。强在把复杂度、提示偏差与置信度串成证据链；事件来自 caption 抽取，可能遗漏未写入字幕的声学事件，且 absent 过滤依赖 ReCLAP 相似度阈值，负例难度分布仍受阈值影响。
