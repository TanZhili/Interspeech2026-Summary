# Leveraging Mutual Intra-Modal Similarity Supervision for Text and Audio

- 论文编号：3300
- 报告人：Julian Miguel von Aspern
- 程序：Monday 28 September 2026 / Audio segmentation
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/vonaspern26_interspeech.pdf

## 问题
音频–文本对比学习（如 CLAP）常用 batch 内 one-hot 配对作监督，忽略同 batch 内文本或音频彼此的语义相似度；图像–文本侧已有用文本–文本相似度作软标签的做法，但音频–文本场景如何迁移、如何同时利用音频–音频相似度、以及小 batch 下软目标训练稳定性仍不清晰。

## 方法
在对比框架上：用冻结 Sentence-BERT 与冻结 PaSST 分别算 batch 内文本–文本、音频–音频余弦相似度矩阵，经加权混合（或按 Monte Carlo/确定性 dropout 估计的嵌入不确定性做逐元素混合）作为跨模态相似度软目标，再与可训练 PaSST + RoBERTa-large 的跨模态相似度做对称 CE 或 MSE。可选模态分类分支 + 梯度反转缩小模态间隙。总体在约 0.5M 样本、batch 64 的可控设定下训练 20 epoch。

## 实验与结果
下游：ESC-50 / TUT17 / US8K / NSynth 零样本分类；Clotho 上 TAR/ATR。相对同设定 baseline 与更大的 CLAP23（约 4.6M 样本、batch 1536），MSE+T（仅文本–文本软目标）多任务综合最强，多数集上优于 baseline 与 CLAP23（NSynth 除外）。TAR 上 MSE+T+A+U 累计 rank 最优；ATR 上 MSE+T+A 最好。CE 对软目标整体弱于 MSE。

## 结论
作者认为互模态内相似度作软监督、并改用 MSE，可在远小于 SOTA 的数据与 batch 下达到有竞争力的零样本分类与检索；任务最优配置因任务而异，无任务特定调优时推荐 MSE+T。

## 点评
核心是把“配对是否唯一正确”放松为“同 batch 语义邻近也应拉近”，并用音频侧镜像与不确定性混合扩展图像–文本先例；小 batch 下用 MSE 稳住软目标是务实洞察。比较是在作者限定的小数据体制下进行，与 CLAP23 等并非同算力/同数据公平对决；NSynth 仍偏弱，说明软目标对细粒度乐器家族未必充分。
