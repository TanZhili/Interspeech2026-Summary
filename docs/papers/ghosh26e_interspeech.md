# AnySimLite: A Lightweight Few-Shot Similarity Encoder for On-Device Speech-Adjacent Classification

- 论文编号：1316
- 报告人：Sourav Ghosh
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/ghosh26e_interspeech.pdf

## 问题
端侧语音相邻 NLP（意图、情感等）若为每任务部署专用大模型，存储压力大；许多任务可归约为“细粒度文本相似”（NTS），需要单一轻量编码器在少样本下覆盖多任务。

## 方法
提出 ANYSIMLITE：词嵌入通道（含注意力）+ 字符 Conv/池化通道，编码器输出后余弦相似；玩具任务 Event Title Similarity（同事件且同命名实体才算相似）。用 DBSCAN 聚类采样“困难”正负对（簇内/簇间约 8:2）把分类集改造成成对相似数据。消融选 B3 为基座，B8 用 MiniLM 蒸馏为部署变体。少样本：每类 20 个样例预计算 16 维嵌入后近邻分类。

## 实验与结果
TitleSim 消融 B3 F1 89.22（0.42M）；部署变体 Acc 90.83。跨任务（Table 2）：相对各任务 SOTA，最差降幅低于约 7%，参数远小于 qLLaMA LoRA-7B 等；SMS Spam 上 F1/Acc 达 97.50/99.28。Galaxy S25 Ultra：8-bit 约 700KB、推理 <30ms。相对最优结果平均准确率降约 2.24%±3.23%。

## 结论
词+字符轻量相似编码器配合困难对变换，可在极少参数下把多种语音相邻分类压到 NTS 少样本协议，并适合端侧。未来可探索分类以外任务。

## 点评
把多模型问题收成“一个相似核 + 每任务样例库”，工程叙事清晰；字符通道针对 OOV NE 与端侧词表限制。NTS 归约假设任务可用样例原型刻画，对细粒度多标签或强依赖语序的任务可能变脆；与大模型差距任务相关，不宜外推为通用 NLP。
