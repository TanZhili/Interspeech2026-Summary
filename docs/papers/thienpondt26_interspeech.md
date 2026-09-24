# Multi-Speaker Embeddings With Weakly Supervised Speaker Activity Detection For Granular Speaker Diarization

- 论文编号：2471
- 报告人：Jenthe Thienpondt
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/thienpondt26_interspeech.pdf

## 问题
级联日志依赖外部 VAD/切分且窗重叠启发式边界粗糙；端到端需帧级标注且场景受限。希望在弱监督下同时出多说话人嵌入与帧级活动。

## 方法
先单说话人预训练带注意力的嵌入器（注意力标量作 VAD logit）；再冻结编码器与 VAD，加 BLSTM SAD 头，用仅话语级说话人标签的置换不变 AAM-Softmax 弱监督训练，使每窗最多两人可得说话人特异嵌入与帧级活动。下游级联日志不再依赖外部 VAD/切分模型。

## 实验与结果
在 AMI、VoxConverse、DIHARD III 上，相对作者先前系统平均相对降低 confusion error rate 13.7%。示例显示弱监督 SAD 可检出基线窗启发式漏掉的说话人活动。

## 结论
弱监督多说话人嵌入可简化流水线并提供更细粒度边界，无需帧级活动金标即可接近混合端到端的粒度优势。

## 点评
用注意力把 VAD/SAD 嵌进嵌入器，弱监督路径实用。强在去外部切分依赖与跨基准相对增益；弱在窗内限两人、极端重叠/多人窗仍需分治。
