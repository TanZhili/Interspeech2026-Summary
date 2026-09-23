# Online Predictive Coding for Dual-Mode Self-Supervised Speech Models

- 论文编号：1997
- 报告人：Keita Goto
- 程序：Monday 28 September 2026 / From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/goto26_interspeech.pdf

## 问题
双模（online/offline）自监督语音模型在同一套参数下同时服务流式与非流式，但两侧自注意力可见上下文范围不同，优化困难；流式缺少未来帧时常明显变差。作者此前引入 online registers 补偿缺失未来上下文，收益仍有限。

## 方法
编码器基于 wav2vec 2.0，双模预训练：offline 看整句；online 按 chunk（可选 lookahead）加注意力掩码，并为每个 chunk 追加共享的可学习 online registers。核心改进有两点：
1. **Online Predictive Coding (OPC)**：将各 chunk 的 register 表征拼接后，经线性投影对后续多步 offline 表征做余弦距离预测（停梯度到 offline 目标），与 online/offline 的 wav2vec 2.0 损失及 codebook diversity 损失联合优化，迫使 registers 编码对未见未来有用的信息。
2. **Dual-mode Layer Normalization**：online/offline 各用一套 LayerNorm 仿射参数，其余权重共享，缓解模式间统计差异。

推断时 online 按 chunk 提取表征，registers 不增加算法延迟。预训练用 LibriSpeech 960h；ASR 微调在 LibriSpeech 与 WSJ，CTC，配合 Dynamic Chunk Training。

## 实验与结果
LibriSpeech 160 ms（\(N_c=8\)，无 lookahead）下，相对纯双模基线，OPC 将 online WER 从 3.65%/10.15% 降到 3.40%/9.65%（test-clean/other），offline 从 2.73%/6.63% 到 2.64%/6.41%。640 ms 设定下 online 优于 UFO2（如 test-other 8.3 vs 9.4），offline 接近 wav2vec 2.0。跨域 WSJ 上 OPC 仍优于双模基线，但 eval93 offline 略差于仅加 registers。消融显示 \(N_f=4\) 最好；小 chunk、零 lookahead 时增益更明显。

## 结论
OPC 让 online registers 主动编码未来信息，配合双模 LayerNorm，可缩小 online–offline 差距并改善低延迟 ASR，且不增加算法延迟。跨域时辅助未来预测可能引入分布偏置。

## 点评
切入点是双模共享参数下的注意力可见域不匹配，用“可学习槽 + 未来表征预测”把流式侧补成接近双向上下文，比单纯蒸馏流式学生更干净。脆弱处在于：OPC 依赖 offline 目标，跨域可能拖累 offline；\(N_f\) 过大过小都伤性能；与 UFO2 等对比解码器/LM 设定不完全对齐。
