# DeepFense: A Unified, Modular, and Extensible Framework for Robust Audio Deepfake Detection

- 论文编号：1366
- 报告人：Yassine El Kheir
- 程序：Tuesday 29 September 2026 / Spoofing, Deepfake Detection and Watermarking
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/kheir26_interspeech.pdf

## 问题
深伪检测实现碎片化、配方隐藏细节多、难公平复现；缺少覆盖大量前端/后端/数据的统一工具包。

## 方法
开源 PyTorch 工具 DeepFense：YAML 编排 + Data Foundry（Parquet 元数据、增强）+ Engine（前端→后端→损失）+ Trainer/日志。集成 Wav2Vec2、WavLM、HuBERT、EAT、MERT、Whisper 等前端，AASIST、Nes2Net、TCM 等后端及多种损失/增强；宣称 100+ recipes、400+ 预训练模型。大规模对照：4 前端 × 4 后端 × 6 训练集 ≈ 96 系统 × 3 种子，13 测试集。

## 实验与结果
前端主导性能方差：Wav2Vec2 宏平均 EER 25.5% 最优（11/13 集第一），HuBERT 33.6% 最差；后端影响较小。训练数据上 ASV19/CodecFake 等相对更好，ADD23 训练宏平均 EER 约 50.8%、跨域灾难性失败。摘要与后文强调高质量模型在音质、说话人性别、语言上存在严重偏差。工具复现可与原报告持平或更好。

## 结论
统一流水线使「前端 > 训练数据 > 后端」的贡献可分离；需关注公平数据选择与前端微调，而非只堆后端结构。

## 点评
基建型贡献：用受控大规模网格把社区传闻变成可引用证据。强在协议一致；脆弱点在固定 4 s/16 kHz/CE 设定可能偏某些架构，且 ADD23 失败提示语言–领域纠缠。文末截断于 ADD23 警示段，偏差分析细节可能不全。
