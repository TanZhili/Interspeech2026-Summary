# The silence of the weights: a structural pruning strategy for Attention-based audio signal architectures with second-order metrics

- 论文编号：2026
- 报告人：Mathieu Fontaine
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/diecidue26_interspeech.pdf

## 问题
Transformer 注意力层参数与算力开销大；音频侧结构化剪枝多整头或 token 删除，对 Q/K/V 通道级细粒度剪枝探索不足。幅度剪枝还会因层间尺度差异偏向剪早期层。

## 方法
提出面向注意力块的通道级结构化剪枝：在满足 Q/K 同维、V/O 同维约束下，对每个头独立选择待删通道（per-head，PH），用贪心预算分配达到目标稀疏度；并与整头剪枝（EH）对比。重要性用 Fisher information（参数梯度平方期望）评分，对比 L 范数幅度；阈值策略分全局（G）与逐层局部（L）。在 AST（AudioSet、SpeechCommands）与 Whisper-medium（转录/翻译）上迭代剪枝：每步剪注意力块 10% 参数，共 10 步，剪后用 LoRA（AST）或大规模多语料（Whisper）微调。

## 实验与结果
Fisher 优于幅度，且全局阈值更合适；幅度宜用局部阈值。PH+FI 与 EH+FI 性能接近：60% 稀疏度下 SpeechCommands 准确率约 97.71%、AudioSet mAP 约 30.86%。整头剪枝推理略快 1–2 ms。Whisper 英文/意/法转录 WER 在 50% 稀疏附近仍接近原模型（约 1% 内）；翻译（CoVoST DE→EN BLEU）下降更大，作者归因于该语向微调数据较少。

## 结论
结合 Fisher 的通道级剪枝可与整头剪枝相当，注意力参数减半时分类/转录性能基本保持。未来可探索 CV/NLP、头与通道联合剪枝，以及放宽同层各头通道数一致的约束。

## 点评
把 NLP 侧 QKV 通道剪枝思想落到 AST/Whisper，并用 Fisher 缓解幅度偏置，工程上完整。PH 在精度上能追平 EH，但速度收益略逊；翻译任务掉点更明显，说明任务与微调数据量会限制“剪半无损”叙事。标题写 structural，正文亦称 structured，与实现一致。
