# ECAPA-TDNN-based Speaker Embedding Framework for Voice Mimicry Assessment

- 论文编号：1535
- 报告人：Bhasi K.C.
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kc26_interspeech.pdf

## 问题
如何客观评估模仿语音与目标说话人的接近度；需融合谱与韵律线索，并使自动排序与听感 MOS 一致。

## 方法
在 MIMICz（20 名人）上：从谱特征（MFCC、chroma、tonnetz、滚降/带宽/通量/质心等）与韵律（响度、音高、语速、shimmer、tempogram 等）提取说话人嵌入；比较 x-vector、ECAPA（E-vector）、d-vector；稀疏自编码器增强；分数级融合；DNN 预测与感知测试最优模仿艺人是否一致（top-1 hit）。

## 实验与结果
融合谱+韵律一致优于单通道。增强 ECAPA 融合 top-1 hit 75%，高于 x-vector 55%、d-vector 65%，并优于作者所列先前方法（如 60%/50%/41%/72%）。t-SNE 显示增强后簇更紧、边界更清。

## 结论
注意力增强的 ECAPA 嵌入 + 谱–韵律融合更适合模仿质量排序，更能对齐人工 MOS 最优艺人。

## 点评
把“hit MOS 冠军”当作任务定义，比单纯说话人验证更贴模仿评测。数据集规模与名人集合有限；分数融合权重敏感（文中有 α 曲线）。未强调跨性别/跨语言模仿等更难设定。
