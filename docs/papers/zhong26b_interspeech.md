# A Benchmark for Early-stage Parkinson’s Disease Detection from Speech

- 论文编号：1057
- 报告人：Khiet P. Truong
- 程序：Thursday 1 October 2026 / Pathological Speech Assessment 4
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhong26b_interspeech.pdf

## 问题
早期帕金森病（EarlyPD）语音检测临床价值高，但既往工作对“早期”定义、数据、任务与评估协议不一致，结果难比；多数研究停留在全阶段 PD vs HC。

## 方法
提出首个面向 EarlyPD vs HC 的公开可复现基准：EarlyPD 定义为 H&Y≤2 且诊断后时间 TAD≤5 年。开放轨用 PC-GITA 与 NeuroVoz；另设私有轨接入荷兰 PERSPECTIVE-Base。固定说话人无关 5-fold（每折验证/测试各 6 EarlyPD + 6 HC），单任务训练持续元音 /a/、DDK /pa-ta-ka/、句子朗读。四种训练设置：AllPD、匹配人数的 AllPD-sub、仅 EarlyPD、EarlyPD+Private。基线为 BDHPD、InceptionPD、RECA-PD；主指标 AUC 与 F1（验证选阈值），5 种子报告均值±SD，并按数据集、聚合、性别、病期分层。

## 实验与结果
表 1 显示任务与数据设置交互明显：扩大说话人多样性（AllPD 或 EarlyPD+Private）总体有益；RECA-PD 跨任务平均 F1/AUC 最高，DDK 与句子尤强，InceptionPD 在元音 AUC 较有竞争力。PC-GITA 明显好于 NeuroVoz（平均 F1/AUC 约 +0.09/+0.15）。说话人级聚合（多条录音均值 logit）通常抬升 AUC。女性表现优于男性；EarlyPD 检测难于全阶段 PD（多数 Δ 为正），句子任务病期差距最大。DDK 最稳，元音最难。

## 结论
该基准为 EarlyPD 语音检测提供可复现协议与多维结果：扩大训练说话人多样性有前景，跨数据集泛化与公平性仍是关键挑战，EarlyPD 本身比全阶段检测更难、更值得作为临床相关设定。

## 点评
把 EarlyPD 操作化并固定折划分，是对领域“结果不可比”的直接回应。开放轨仅两套西语系数据，私有轨增益难被外部完全复现；单任务设定也未覆盖自发语音。全文结论在抽取中截断，但结果与讨论已支撑上述要点。
