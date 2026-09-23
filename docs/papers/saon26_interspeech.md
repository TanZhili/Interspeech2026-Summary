# Self-Speculative Decoding for LLM-based ASR with CTC Encoder Drafts

- 论文编号：2680
- 报告人：Avihu Dekel
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/saon26_interspeech.pdf

## 问题
Speech-aware LLM（SLM）ASR 精度领先，但自回归逐 token 前向限制吞吐。常规 speculative decoding 常需额外 draft 模型；联合 CTC/attention 虽可加速，但如何在不重训的前提下复用 SLM 自带 CTC 编码器做 draft，并兼顾准确率与 RTFx，仍不清晰。

## 方法
提出 self-speculative decoding（SSD），三步、无需额外 draft 模型：
1. **CTC decode + verify**：CTC greedy 假设；若所有帧级 CTC 输出熵低于 \(\tau_{\mathrm{CTC}}\)，直接接受；
2. **LLM verify**：否则用单次 LLM 前向，按松弛准则检查各 token 似然是否均大于 \(\tau_{\mathrm{SLM}}\)；通过则接受 CTC 假设；
3. **AR fallback**：失败则从最长已验证 CTC 前缀继续自回归解码。
架构为 Conformer CTC encoder + Q-Former adapter + LLM；要求 CTC encoder 在 projector/LoRA 微调时冻结。松弛接受（“plausible”而非精确匹配）用于提高接受率。

## 实验与结果
主模型 granite-speech-4.0-1b（约 1B LLM + 440M CTC encoder），在 HuggingFace Open ASR 及 MLS、CommonVoice 等多语料评测（1×H100，batched）。
- High accuracy（\(\tau_{\mathrm{CTC}}=0.7,\tau_{\mathrm{SLM}}=0.2\)）：Open ASR 平均 WER 5.58%，优于 full AR 的 5.75%，RTFx 相当（548 vs 564）；作者称创纪录 5.58% WER。
- High RTFx（\(\tau_{\mathrm{CTC}}=3.0,\tau_{\mathrm{SLM}}=0.1\)）：Open ASR 平均 WER 6.56%、RTFx 2491，相对 AR 约 4.4× 加速，相对 WER 增约 12%。
- 消融显示双阶段验证在多数 WER–RTFx 区间 Pareto 更优；LLM 验证相对纯 AR 常进一步降 WER，作者归因于 CTC 与 SLM 错误互补。

## 结论
复用冻结 CTC 编码器作 draft、LLM 做验证与回退，可在不重训、不引入独立 draft 模型的情况下同时提升准确率与吞吐。局限：需 CTC 训练的 SLM；仅适用于 ASR；验证失败时整句从失败点 AR，低接受率语料收益有限。

## 点评
核心是“声学接地的 CTC draft + 语言模型验证”：高置信 CTC 可跳过 LLM，而 LLM 接受 CTC 又能纠偏 AR 的语言先验偏差。强在自投机、可调 \(\tau\) 覆盖准确–速度谱；脆弱在依赖 CTC 头质量与 utterance 级接受失败时的整段 AR 回退，对长句与低接受率场景不友好。
