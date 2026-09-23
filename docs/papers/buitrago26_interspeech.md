# Quantifying Cross-Lingual Transfer in Paralinguistic Speech Tasks

- 论文编号：2745
- 报告人：Federico Costa
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/buitrago26_interspeech.pdf

## 问题
副语言任务常被视为较语言无关，但跨语仍见性能下降；既有研究多限少数语对或任务特异设定，缺少可比较的、基于下游性能的 donor→target 迁移度量。

## 方法
提出 Cross-Lingual Transfer Matrix（CLTM）：用等量额外目标语数据的 self-gain 归一化 donor 数据带来的 cross-gain，CLTM[i,j]=Δi←j/Δi←i。在固定 mHuBERT-147 上对 44 语微调性别识别（macro-F1）与说话人验证（AUC），10 种子平均；用 RFD1、Asymrel、prop+ 等汇总诊断。

## 实验与结果
性别识别 CLTM 接近全 1 理想：RFD1=0.162，prop+≈99.97%，行相似 cosrows≈0.990，迁移近乎语言无关。说话人验证强烈依赖语言：RFD1=2.970，prop+仅 8.93%，正迁移更集中在语系内（intra-family+ 41.68% vs GR 的 4.98%），负迁移普遍。

## 结论
CLTM 可系统量化副语言任务的跨语迁移几何；同为“副语言”，性别识别近语言无关，说话人验证则高度语言依赖。

## 点评
贡献是可复用的矩阵度量与对照协议，澄清“副语言=跨语无感”的笼统说法。单骨干、单 epoch、两任务限制外推；矩阵解释依赖 self-gain>0 等有效性条件，极端低资源语对需小心。
