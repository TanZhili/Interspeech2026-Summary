# Whisper Hallucination Detection and Mitigation via Hidden Representation Steering and Sparse AutoEncoders

- 论文编号：1989
- 报告人：Georgii Aparin
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/aparin26_interspeech.pdf

## 问题
Whisper 常对非语音输入生成流畅但与声学无关的转写（幻觉）。既有缓解依赖前/后处理或微调特定神经元；是否可仅靠编码器内部表示检测并在推理时纠正，且少伤正常语音 WER，仍待验证。

## 方法
提取 Whisper 音频编码器激活，在两空间分析幻觉可分性：原始激活与 **AudioSAE** 稀疏潜变量（扩展×8，Top-k=50）。线性分类器显示判别力集中于稀疏特征子集、并随层加深增强。提出免微调干预：
1. **激活空间 steering**：沿分类方向加减扰动；
2. **SAE latent steering**：对 top-k 幻觉相关潜维做加性/乘性缩放，再经 SAE 解码注入残差流。
在 Whisper small / large-v3 上评测；非语音训测严格划分（MUSAN、WHAM!、FSD50k、UrbanSound8K 等）；语音侧用 LibriSpeech、FLEURS、AISHELL-1 监控 WER/CER。

## 实验与结果
- SAE steering 将完整非语音测试集幻觉率：small **72.63%→14.11%**；large-v3 **86.88%→27.33%**；
- 语音数据上 WER 仅小幅退化，接近微调类方法效果。
（抽取在数据集与 HR 表处截断，分数据集明细与 WER 表未全读到。）

## 结论
幻觉在编码器表示中线性可分；SAE 空间 steering 可不改模型参数大幅降非语音幻觉，并在多语言语音上保持可用识别质量。

## 点评
把可解释性工具（SAE + steering）接到 ASR 幻觉，避免重训整模，工程友好。强在双规模模型与非语音–语音分离评测；脆弱在依赖幻觉标签定义与 steering 强度 \(\alpha\)——过强可能伤真实语音。
