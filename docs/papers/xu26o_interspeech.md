# BACON: Boundary-Aware Convolution for Streaming Conformer Models

- 论文编号：1455
- 报告人：Hainan Xu
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/xu26o_interspeech.pdf

## 问题
Chunk-based 流式 Conformer 常把深度卷积改成因果卷积以防未来泄漏；但 chunk 内帧已全部可用，纯因果卷积过度限制右上下文，丢掉安全可用的局部未来信息。

## 方法
提出 BACON：深度卷积通道对半拆分——因果组保留完整历史（仅句首左 pad）；边界感知双向组左上下文可跨 chunk，右上下文用 chunk 末 pad，严格限制在当前 chunk 内。核大小 k 时有效感受野约 [−(k−1),(k−1)/2]，宽于因果 [−(k−1),0]，参数量不变。作为因果卷积的 drop-in 替换。

## 实验与结果
NeMo FastConformer（17 层，d=512，k=9，chunk C=14≈1120 ms）上对比因果 vs BACON，架构含 RNN-T 与 CHAT。LibriSpeech：CHAT test-other WER 8.47→7.68（相对约 9.3%，p<0.001）；test-clean 也有显著改善。En→De AST：两族模型在 MuST-C/CoVoST 上 BLEU 均显著提升（如 CHAT CoVoST 36.40→37.72）。双说话人 Fisher cpWER 27.41→27.14（方向一致，p=0.19）。消融：全通道 boundary-aware（all-bidir）常弱于 BACON，甚至在 RNN-T test-other 上差于因果；因果组起边界稳定作用。全注意力设定下非因果卷积仍比因果低 0.93 WER，说明卷积右上下文与注意力互补。平均发射 chunk 索引略降，未增延迟。

## 结论
在 chunk 流式约束下用通道拆分安全引入 chunk 内右上下文，可在多任务、多架构上提准且不增加参数与延迟。

## 点评
洞察很具体：流式约束是“不看未来 chunk”，不是“永远不看未来帧”。双组设计避免 chunk 右缘全通道有效感受野同时塌缩。收益在困难集与翻译上更明显；多说话人增益较小，可能被重叠/说话人归因噪声淹没。
