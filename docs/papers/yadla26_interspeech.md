# Extreme Few-Shot Phoneme Discovery for Indigenous Australian and Pacific Languages via Typological Transfer Learning

- 论文编号：284
- 报告人：Prasanth Yadla
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/yadla26_interspeech.pdf

## 问题
诸多原住民澳/太平洋语言转录极少（常不足 10 小时），常规声学单元发现假设远超 100 小时无标注音频；通用多语 SSL 又偏向印欧音系，在不足 1 小时的极端低资源设定下难以发现卷舌、元音长度等细微对立。

## 方法
提出 Typological Anchor Selection（TAS）：用 PHOIBLE 音位库存 Jaccard 重叠、谱系权重与源语言时长对数加权选源语（验证上偏好爪哇语、他加禄语）。在源语上预训练 VQ-VAE，再保留码本、降学习率适配目标语（≤60 分钟），并用自适应 commitment 权重缓解遗产录音噪声与码本坍塌；后处理做共现/时长/层次聚类映射到类音位单元。

## 实验与结果
目标语：Te Reo Māori、Pitjantjatjara、Nauruan。相对 XLS-R，平均 NMI 提升 18.8%、cluster purity 提升 15.6%（置换检验 p<0.01）。多源（Jav+Tag）优于单源；码本 K=40 对 Māori 最优；仅 15 分钟目标数据即可达到 XLS-R 用 60 分钟的水平（NMI 0.48，Purity 0.64）。

## 结论
类型学引导的迁移可为不足一小时音频的音位发现提供可复现路径，适配后的 VQ-VAE 对遗产录音更稳健；输出宜作需母语语言学家校验的初步假设。

## 点评
用 PIO 选锚点语种而非盲目多语预训练，把类型学先验写进数据选择，切中濒危语言文档化痛点。评价指标是扰动下的簇稳定性而非相对金标音位准确率，上限解读需克制。对声调语言/语系孤立语会退化到随机初始化，且未显式建模音高，是应用边界。
