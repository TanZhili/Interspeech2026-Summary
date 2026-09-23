# End-to-End Model Compression for Personalized Neural Speech Codecs

- 论文编号：878
- 报告人：Inseon Jang
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/jang26_interspeech.pdf

## 问题

端到端神经语音编解码（如 DAC）参数与算力膨胀，难在低功耗设备实时运行。已有说话人无关压缩常绑特定结构、压缩比有限；先前个性化 LPCNet 只压缩解码端，编码端仍重，且多在干净语音上验证。

## 方法

提出端到端 Personalized DAC（PDAC）：噪声鲁棒说话人编码器 F 提 embedding，与预计算的 C 个说话人组中心做欧氏最近邻得组索引 c*；发送端只跑对应小组 utterance 编码器 G^(c*) 产生码流 y，并下传 c*；接收端用匹配的个性化解码器 D^(c*) 重建干净语音。说话人组由对比学习 Siamese embedding 上 k-means 预先聚类。相对通用 Large DAC（74.18M），设计 Small（14.99M）与 Tiny（3.02M）容量配置，各组独立训练 encoder–decoder–量化器。系统把 MoLE 做成“排他选专家”，发送与接收两侧都只跑一个小组模型。

## 实验与结果

设定基于 LibriSpeech train-clean-100（251 说话人）训练，dev/test-clean 验证测试。摘要称：相对 SOTA DAC，模型体积约减 96%、码率由 2 kbps 降至 1 kbps（减半），主观听感可维持；噪声下个性化模型仍优于基线。正文实验与表格在全文抽取中于数据集描述处截断，具体 DMOS/客观分数字未能完整读到。

## 结论

作者认为在端到端编解码两侧同时做说话人组个性化，可同时压模型与码率并保留感知质量，且对噪声与组误分类有一定鲁棒性（文中称将通过微调分类与专家缓解误分类）。部署上强调适合低功耗、干净与噪声场景。

## 点评

相对“全局小模型”或“只压解码器”，排他式组专家把容量花在更同质的说话人子集上，压缩逻辑清晰。全文 PDF 抽取在实验段中断，定量结论主要依赖摘要与方法描述，点评无法核实表格数字。潜在脆弱点包括：组数/聚类质量、测试说话人落错组、以及噪声鲁棒说话人编码器本身的误差会连带选错编解码专家。
