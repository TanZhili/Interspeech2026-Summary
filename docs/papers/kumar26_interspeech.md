# Listening with Attention: Entropy-Guided Explainability for Transformer-Based Audio Models

- 论文编号：593
- 报告人：Ravi Kumar
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26_interspeech.pdf

## 问题
Whisper 等 Transformer ASR 精度高但难解释；LIME/SHAP/IG 等事后解释对语音时序不友好，常不忠实且时间定位粗糙。需要与模型内部计算一致、并对齐到解码 token 的时域归因。

## 方法
LEAF-X：对每个解码 token 产生帧级归因。对 cross-attention（或 decoder-only 中指向音频伪 token 的注意力）算头熵，低熵头获更高权重并层内聚合；再用多层 attention rollout 累积证据；可用梯度调制压制对 token 概率影响小的注意力；可选按层消融 cross-attention 造成的 NLL 上升作因果重加权。输出归一化 token-to-frame 分布，映射回波形时间轴。适用于 Whisper 与 speech-augmented decoder-only（如 Canary-Qwen）。

## 实验与结果
模型：Whisper-large-v3（LibriSpeech）、Canary-Qwen-2.5B（TED-LIUM 3）。指标（归一化）：D-AOPC↓、TLoc↑、SPR↑、STAB↑、INF↓。Whisper：LEAF-X 为 0.45 / 0.72 / 0.70 / 0.78 / 0.45，全面优于多数基线，TLoc 略低于 SaCo（0.73）。Canary：0.48 / 0.70 / 0.68 / 0.76 / 0.47。消融显示去掉熵加权或 rollout 损害最大；insertion/deletion 曲线支持更高忠实度。作者强调指标为代理，非人类可信证明。

## 结论
LEAF-X 用熵引导头选择、多层 rollout 与轻量因果重加权，为 Transformer ASR 提供更忠实、稀疏且稳定的 token–时间归因，利于高风险场景下的可审计分析；局限含骨干/数据/语言覆盖、校准敏感、缺用户研究等。

## 点评
核心是把“哪些帧支持这个词”建成模型内禀流程，用低熵注意力过滤弥散头，比纯扰动或原注意力更贴计算路径。因果层消融有额外前向开销，可关掉；解释质量仍绑定注意力机制假设，对噪声域移与非注意力主导错误模式可能脆弱。
