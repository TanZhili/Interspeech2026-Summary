# Soft-Gating Score-Level Fusion for Spoofing-Aware Speaker Verification

- 论文编号：2294
- 报告人：Seongkyu Han
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/han26e_interspeech.pdf

## 问题
SASV 需融合 ASV（目标/非目标说话人）与 CM（真实/伪造）子系统。常见静态分数求和或固定加权无法随试次调整二者贡献，且对分数分布偏移敏感；已有分数感知门控（如 embedding 侧乘性门控）又常需额外联合训练，难以直接用在已训好的子系统上。

## 方法
提出无需训练的 Soft Gating Score-Level Fusion：先将 ASV 余弦相似度线性映射到 [0,1]，CM logits 经 softmax 得真实类后验；用开发集 EER 阈值 τ 定义置信度边距 δ=s−τ。三种门控：
- CM Gating：S = s_cm·δ_cm + s_asv·(1−|δ_cm|)
- ASV Gating：S = s_cm·(1−|δ_asv|) + s_asv·δ_asv
- Double Gating：S = s_cm·δ_cm + s_asv·δ_asv  
按试次把更自信子系统的权重加大，直接接到现有 SASV 流水线。

## 实验与结果
数据：ASVspoof 2019 LA、ASVspoof5 Track 2 closed。ASV：ECAPA-TDNN、ReDimNet（VoxCeleb2）；CM：AASIST、Conformer-TCM。指标：SV-EER、SPF-EER、SASV-EER、a-DCF。相对简单求和与 DNN embedding 融合基线，多数配置显著更好；LA19 上 a-DCF 平均约相对降 90%（如 Redim+AASIST Double gating a-DCF 0.0107 vs Baseline1 0.1659）。失效情形集中在 EER 阈值极端靠近 0 或 1 时：CM Gating 在 TCM 阈值近 0 时削弱说话人区分；Double Gating 在阈值近 1 时削弱 CM 对伪造的抑制。

## 结论
训练无关的软门控分数融合在多数 ASV–CM 组合上优于静态/需训练基线，但效果依赖 EER 阈值位置；作者计划改进对极端阈值的门控策略。

## 点评
抓的是“两子系统置信度随试次变化却用固定权重”的工程痛点，用阈值边距做置信度、零参数即可插拔，实用性高。脆弱点很明确：阈值定义置信度，阈值病态时门控会系统性偏置一侧；部署时需按阈值位置选门控变体，而非默认 Double/CM。
