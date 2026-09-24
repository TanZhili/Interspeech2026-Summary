# STArK: Towards Synthesizing Articulatory Kinematics from Text

- 论文编号：2842
- 报告人：Xavier Yin
- 程序：Thursday 1 October 2026 / Modeling Articulation
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yin26b_interspeech.pdf

## 问题
从语音到 EMA 的反演已可行，但高质量发音数据稀缺；直接从文本合成发音运动（TTA）仍开放，限制发音表征在合成与下游任务中的规模化使用。

## 方法
STArK 为非自回归文本→发音管线：G2P + FFConformer 音素编码器；Temporal Regulator（One TTS Alignment 无监督对齐 + SepConv 时长预测）做时长扩展；Articulatory Decoder 预测 12 维 EMA、响度与对数归一化 pitch（不预测 SPARC 周期特征）。目标由冻结 SPARC 编码器从 LibriTTS-R 伪标注；推理用冻结 SPARC vocoder 与说话人嵌入做克隆，训练时不显式喂说话人嵌入。损失为 \(L_{art}+\alpha L_{align}+\beta L_{dur}\)。

## 实验与结果
LibriTTS-R train-clean-100，约 73.7M 参数、32k 步。语音：STArK DNSMOS 接近 GT；加 aligner/prosody 后部分指标贴近或超过 SPARC；相对 YourTTS 在 SECS 更强，WER 更高（test-clean 约 6.25 vs 4.58）。发音：对齐时长下 EMA PCC 0.905，pitch PCC 较低（0.533）；加 aligner 改善 EMA/响度 DTW，pitch 改善有限。

## 结论
文本可直接生成高质量发音运动并合成可懂语音，且无需训练期说话人嵌入即可多说话人克隆。未来需加强韵律/情感/口音与评估稳健性。

## 点评
把 NAR-TTS 骨架接到 SPARC 特征空间，用文本扩展伪 EMA 数据，路线清晰。性能高度依赖 SPARC 伪标签与时长对齐；基座设置下 pitch/韵律仍是短板，WER 相对 YourTTS 的差距也说明内容保真仍有空间。
