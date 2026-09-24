# Towards Personalized Federated Learning for Dysarthric Speech Recognition

- 论文编号：1559
- 报告人：Tao Zhong
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/zhong26d_interspeech.pdf

## 问题
构音障碍 ASR 隐私敏感，适合联邦学习；但说话人异质性强，强制共享同一全局模型次优，面向构音障碍的个性化联邦聚合研究不足。

## 方法
基于 HuBERT 的 FL-ASR：模型拆成说话人无关（SI）与说话人相关（SD）部分。SI 用标准数量加权 FedAvg；SD 用说话人相似度加权聚合——(1) 参数更新余弦相似度；(2) SI 输出 embedding（每轮用随机私有子集）相似度。与数量加权混合，超参 β 平衡。在 UASpeech、TORGO 上对比正则化 FedAvg 等。

## 实验与结果
相对正则化 FedAvg，提出方法取得统计显著 WER 下降：UASpeech 最高绝对 0.99%（相对 3.15%），TORGO 最高绝对 0.56%（相对 4.73%）。个性化相似度聚合优于仅共享全局模型。

## 结论
相似说话人邻域引导的 SD 聚合可在联邦设置下个性化构音障碍 ASR，缓解异质负干扰并兼顾隐私。

## 点评
把“临床相近说话人应互拉、不相近应隔离”写进聚合权重，比盲目全局平均更贴构音障碍异质性。embedding 用随机子集兼顾隐私。增益绝对值不大，但对难任务仍有意义；客户端规模与通信轮次细节依赖完整实验设定。
