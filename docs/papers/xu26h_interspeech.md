# Towards Data-free and Training-free Compression for Speech Foundation Models Using Parameter Clustering

- 论文编号：1010
- 报告人：Haoning Xu
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/xu26h_interspeech.pdf

## 问题
语音基础模型（HuBERT、Whisper 等）参数大，端侧难部署。结构化剪枝虽硬件友好，但常按孤立重要性丢弃可能功能冗余却重要的单元，且依赖数据校准/微调；非结构化稀疏又需专用算子。

## 方法
**参数聚类压缩**（数据无关、可训练免费）：
1. 对 MHSA/FFN（及 Whisper 交叉注意力）中结构化单元（注意力头、FFN 中间单元）做 k-means，把相似单元融合成 \(K=\mathrm{round}(N(1-sp))\) 个质心并写回权重，而非直接删除低幅度单元。
2. **混合稀疏**：按层内参数方差把模块分高/中/低三组，高方差层保留更多簇（\(s=0.2\)），全局平均稀疏度不变。
对比基线为同结构的幅度剪枝（MP）。

## 实验与结果
LibriSpeech 上评 HuBERT-large 与 Whisper-large-v3。无微调：HuBERT 50% 均匀稀疏相对 MP，test-clean/other 绝对 WER 降 27.73%/18.61%；Whisper 10% 混合稀疏相对 MP 降 2.86%/5.02%，且相对未压缩基线无显著恶化。HuBERT 聚类后仅 3 epoch 微调，相对 MP 仍有小幅优势。混合稀疏在多数稀疏度优于均匀；过高稀疏（如 Whisper≥30%、HuBERT 60%）会崩溃。

## 结论
作者主张用「合并相似结构」替代「丢弃低幅度结构」，实现可部署的粗粒度、数据/训练免费压缩，并可用方差分配稀疏预算。

## 点评
核心反直觉但合理：高幅度单元若彼此相似，剪枝会留下冗余；聚类融合保留集体信息。数据免费这一点对「训练数据不可得」的商用基础模型尤其实用。脆弱点：极端稀疏仍崩；主要评测在 LibriSpeech 英语 ASR；聚类本身有计算开销，且融合是否损害多语 Whisper 能力正文未深挖。
