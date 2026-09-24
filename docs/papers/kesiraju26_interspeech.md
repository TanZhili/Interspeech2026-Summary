# FLiP: Towards understanding and interpreting multimodal multilingual sentence embeddings

- 论文编号：3315
- 报告人：Santosh Kesiraju
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kesiraju26_interspeech.pdf

## 问题
多语/多模态句向量压缩为单向量后难解释“装了什么”；现有线性探测多为非分解或英语中心，缺系统跨语跨模态诊断。

## 方法
FLiP：将嵌入映到词表分布的 log-linear 模型，\(W=AB\) 因式分解（隐含正则，可低秩）；目标最大化 bag-of-words 似然，可混合同句语音/文本或双语文本（\(\alpha\)）。推理取 top-k 词作关键词。训于 SONAR / LaBSE / Gemini 嵌入；MCV 英德法语音–文本，Europarl/Samanantar 平行文本。

## 实验与结果
SONAR 英：因式化全秩文本准确约 77%（非因式约 59%）；r=512 接近全秩。同语内语音–文本对齐较好；跨语呈英语偏置，远距离语（如 TA、TE）线性可恢复性下降。同设置下 SONAR 优于 LaBSE/Gemini。相对 SpLiCE，span-aware 准确约翻倍（文本 61.45% vs 29.58%）。去 bias 可提高命名实体召回。

## 结论
良对齐嵌入空间中多数词汇内容可线性恢复；FLiP 可作为不依赖下游榜单的内在诊断工具，揭示模态对齐与英语偏置。

## 点评
把解释落成可量化的关键词召回，比单点 MTEB 分数更细。线性假设与词袋忽略语序；“诊断工具”定位清楚，但高召回不等于语义忠实。
