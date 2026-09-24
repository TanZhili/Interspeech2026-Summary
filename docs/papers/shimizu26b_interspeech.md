# Auditory Contrast Network for Text-Free Prominence Detection

- 论文编号：250
- 报告人：Kosuke Shimizu
- 程序：Tuesday 29 September 2026 / Prominence, Stress and Focus
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shimizu26b_interspeech.pdf

## 问题
词级感知凸显依赖与邻词的相对对比，但主流 CNN/SSL 检测器无显式邻比机制，且常需文本，不利端侧无文本场景。

## 方法
Auditory Contrast Network（≤238 参数）：对时长、能量、频谱、F0 等线索分别用小 MLP 算与前/后词的非线性对比，softmax 注意融合方向，再聚合原始线索与可选 surprisal。编码成对对比、线索独立与前向主导等心理声学原则。Helsinki Prosody→Emphases 跨库迁移评测。

## 实验与结果
仅声学：r=0.412，匹敌冻结 wav2vec2（94.6M，r=0.409），延迟约低 120×；加文本 r=0.451。学得权重显示前向上下文 >96%、±1 词局部最优、线索序 duration>energy>spectral≫F0。

## 结论
极轻量、可解释的对比架构可在无文本时达到大模型级相关，适合助听器与实时发音监测。

## 点评
把心理声学直接写进结构，可解释性是卖点；相关仍中等，任务是连续凸显评分而非焦点检测，外延需谨慎。
