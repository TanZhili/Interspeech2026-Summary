# CrossPhon-Tonal: Streamlining Cross-language Modeling for Forced Alignment in Low-resource Tonal Languages

- 论文编号：1770
- 报告人：Hongchen Wu
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wu26e_interspeech.pdf

## 问题
跨语强制对齐（CLFA）对声调语常忽略声调或依赖专家手工映射；忽略声调损害边界，手工又慢且难复现。

## 方法
CrossPhon-Tonal：在 CrossPhon 发音特征坐标映射音段后，对 Chao 调号做自动声调映射——先同轮廓类，再最小化首末音高水平差，并列时取更近音高；凹/凸无同类则回退首半轮廓。输出中间词典供目标语声学模型对齐。评测普通话、粤语、泰语、越南语、豪萨语、克罗地亚语。

## 实验与结果
相对语言专属基线的边界一致率（0.025 s）上，自动映射与专家映射总体相当，部分对（如泰模型对齐普通话 0.772 vs 专家 0.726）更优。声调模型常优于 3600 h Global English（如泰→普通话 0.772 vs 英 0.638）。小数据映射目标（如克罗地亚）与家族差异大时效果不均。

## 结论
自动声调编码可去掉专家瓶颈，且声调特异性往往比单纯数据规模更关键。

## 点评
把声调当“类附加符号”接进既有音段管线，工程可扩展。质量依赖源/目标词典与目标模型小时数；非声调强模型在印欧对上仍可胜，说明音系相似度与声调并非唯一因素。
