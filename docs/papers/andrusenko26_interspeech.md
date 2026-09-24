# Reducing the Offline-Streaming Gap for Unified ASR Transducer with Consistency Regularization

- 论文编号：1195
- 报告人：Andrei Andrusenko
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/andrusenko26_interspeech.pdf

## 问题
同一 ASR 模型同时做好离线高精度与低延迟流式仍难；Conformer 的 MHA/卷积在 chunk 解码下存在训练–推理失配，低延迟（<0.5 s）时离线/流式模式冲突加剧，大规模数据下的统一训练也欠研究。

## 方法
统一 RNNT：chunk-limited attention（左/当前/右上下文 L,C,R，训练时从预定义集合采样）+ Dynamic Chunk Convolution（DCConv，卷积按 chunk 与核半宽重排，离线共享参数）。训练可用单模式（每步随机 offline/streaming）或双模式（同 batch 两边 RNNT 损失加权）。进一步提出 MCR-RNNT：对离线与流式 joint logits 做对称 KL，用 Triton 融合核在线算 log-softmax/KLD，避免物化巨大 [T,U+1,V] 张量。最终目标 α L_off + (1−α) L_str + λ L_MCR。曾尝试 CR-CTC 扩展，对流式 RNNT 有害，故改为对 Transducer 输出一致性。

## 实验与结果
L-size FastConformer RNNT（~128M）在 Granary ~120k 小时归一化英文上训；Open ASR Leaderboard 平均 WER。Unified DM + MCR-RNNT：离线 6.63，流式在 0.24 s 仍 9.04，显著优于无 MCR 的 SM/DM（低延迟急剧恶化）。XL ~0.6B + 280k 小时含标点大小写：较大右上下文配置离线 AVG WER 5.76（SOTA Unified RNNT），平衡配置低延迟更稳。消融：对称 KL、λ≈0.3、α≈0.5 较优；固定总延迟下增大右上下文降 WER。

## 结论
chunk 限制注意力 + DCConv + MCR-RNNT 可把离线/流式差距压到更低延迟区间，并随模型与数据放大仍有效；框架与英文 checkpoint 开源。

## 点评
关键不是再叠一套编码器，而是在 RNNT joint 输出上显式拉齐两种上下文制度；相对 CTC 一致性，更贴合 Transducer 的对齐灵活性。工程上 Triton 全格点一致性使方法可训练。当前推理仍每步重算左上下文，作者承认速度未充分优化；极低 0.16 s 仍略逊纯流式基线。
