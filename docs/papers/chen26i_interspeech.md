# G2PO: A Lightweight Lexicon-enhanced Framework for Open-Vocabulary Mandarin Polyphone Disambiguation

- 论文编号：1064
- 报告人：Feifan Chen
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26i_interspeech.pdf

## 问题

普通话多音字消歧是 TTS 前端关键环节。现有 BERT 类方法参数过大难上端，且闭集分类无法预测训练未见读音；词典增强方案常需存储稠密词向量，占存储。

## 方法

提出 g2pO：用 RoBERTa-tiny（约 3.2M）编码；词典融合模块用 Trie 匹配含目标字的词，对 span 隐状态做 mean+max mix-pooling，动态构造词表示并与拼音嵌入拼接，再经注意力聚合成 lexicon prior 与增强字符状态；辅以 POS 预测；最终用加权 softmax（结合 prior 与合法拼音 mask）输出。词典仅存字–拼音映射（约 100K 词约 3MB），无需预训练词向量。

## 实验与结果

CPP 测试准确率 99.15%（3.99M 参数），优于 g2pW 的 99.08%（约 108M）；RCPP/RCPP(S) 为 99.03%/98.51%。Hard 子集（词典冲突）准确率 93.62%（随机基线 54.26%）。未见读音零样本准确率 70.79%，闭集方法基本为 0。消融显示去 lexicon adapter 掉至 98.55%。

## 结论

作者认为轻量编码器 + 动态词典融合可在极小体积下达到 SOTA，并具备开放词表泛化，适于端侧部署。

## 点评

把“词典知识”从巨大 embedding 表改成隐状态上的 on-the-fly 池化，同时用 prior 打开输出空间，同时解决体积与开放词表。Hard 子集说明模型不是简单查表。未见音依赖词典覆盖与 prior 温度设定；极低频多音字仍可能弱。
