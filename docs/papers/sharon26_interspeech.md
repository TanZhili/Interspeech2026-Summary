# Less can be More: What Aspects of Speech Drive End-of-Turn Detection

- 论文编号：1705
- 报告人：Rini Sharon
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sharon26_interspeech.pdf

## 问题
流式 end-of-turn（EOT）检测常融合声学、韵律与语义，但各模态相对贡献不清；多加文本是否一定更好仍缺在相同容量与训练条件下的系统消融。

## 方法
设计轻量三模态 APT：冻结 Zipformer2 声学编码器（80D FBank→25 Hz）、5 维手工韵律（归一化 F0、ΔF0、voiced、speech、log 静音累计）与 MiniLM 句向量（来自 RNN-T 贪心解码，blank 帧缓存）。各流经投影与 7 帧因果 depthwise 卷积后拼接，~261K 参数分类头输出帧级 EOT 概率。禁用模态用零向量占位并阻断梯度，在相同超参下从零训练全部 7 种非空子集。检测需连续 8 帧超阈（320 ms），容忍提前 50 ms。

## 实验与结果
专有英语电话对话 10K/2K/5K 句（约 33 h 训练）。A+P 最优：utterance F1 0.930，FA% 7.8，中位延迟 400 ms；纯声学 F1 0.927；APT 加文本后 F1 降至 0.909、FA% 升至 10.7。文本单模态 F1 仅 0.292、平均每句逾 5 次误触发。特征空间上韵律原始 silhouette 最高（0.301，主因 silence dur），文本类重叠大（0.108）。仅 A+P 与 APT 同时满足 FA<10% 与延迟<500 ms 部署预算；加文本的延迟优势部分被 ASR/BERT 开销抵消。

## 结论
在所研究的对话电话域，声学提供主检测信号、韵律补精度；连续帧级文本融合系统性抬高误触发，A+P 已足以达到部署级 EOT，不必为文本支付额外推理成本。

## 点评
零掩码 + 全子集消融把“能不能加模态”问成“该不该加”，证据扎实。文本在长 turn（中位 10–11 s）上对句法完整单元过敏，是场景效应而非单纯编码器弱；作者也承认噪声/低资源语言上文本或许更有用，且可改成边界抑制而非逐帧融合。
