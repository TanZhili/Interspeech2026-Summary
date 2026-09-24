# Scaling few-shot spoken word classification with generative meta-continual learning

- 论文编号：408
- 报告人：Batsirayi Mupamhi Ziki
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/beyers26_interspeech.pdf

## 问题
少样本口语词分类多在小类数设定；若要持续扩到约 1000 类且每类仅 5 条，需在精度、遗忘与适应速度上可扩展的元–持续学习方案。

## 方法
用 GeMCL：编码器 + 生成式分类器，每类嵌入用 Normal-Gamma 先验、观测后闭式更新高斯后验（类参数隔离，免疫灾难遗忘）；元训练优化编码器与先验 α0、β0，元测试冻结元参数、对新词只算类统计。实现为 12 层 12 头 Transformer、MFCC 输入（约 85M 参数），在 MSWC 英语约 8915 词上元训（25-way-5-shot，估计约 477 小时有效数据）。基线为 HuBERT base（LibriSpeech 约 960 h 预训练）全量微调，以及冻骨干只训投影+分类头；类数从 25 增至 1000，每阶段 5-shot 支持集后评查询集。

## 实验与结果
全量微调多数阶段准确率最高但不稳（词级波动均值约 24.55）；GeMCL 波动约 0.48，显著更稳。GeMCL 在 <450 类优于 CH，高类数略逊；1000 类时约落后 1000-way 微调 CH 约 2%。适应时间：GeMCL 少样本适应约 0.06 h vs CH 124 / 全微调 186（摘要称适应约快 2000×）；元训远少于 HuBERT 预训练等价算力。

## 结论
从零训练的 GeMCL 在千类 5-shot 持续设定下可达接近实用 HuBERT 分类头基线的精度，真正增量更新、词级表现稳定，适合持续扩词表部署。

## 点评
把“可扩展少样本 KWS”推到 1000 类并报告过程稳定性，问题设定贴近产品。对比混入数据量与算力不对称，结论更像策略选择（相关小数据元学习 vs 大 SSL 微调）而非纯算法胜负。仅英语 MSWC；跨语与其他持续学习算法仍待验证。
