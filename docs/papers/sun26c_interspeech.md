# Non-linear Effects of Semantic Relevance on Word Duration in Spontaneous Speech

- 论文编号：1062
- 报告人：Kun Sun
- 程序：Tuesday 29 September 2026 / Modeling L1 Acquisition
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sun26c_interspeech.pdf

## 问题
自发语音词长受频率、长度、语速与 n-gram 可预测性影响已充分，但语义语境多被浅层代理且常线性建模；语义相关（semantic relevance）已在阅读/EEG 中验证，是否及如何非线性影响产出时长未知。

## 方法
Buckeye 会话语料词级时长；用分布嵌入与近因加权相似度计算目标词对局部语境的 semantic relevance。GAMM 建模，控制词长、对数频率、短语语速、音系删音等，说话人随机效应；比较含/不含 relevance 的模型 AIC，并探索与频率的交互。

## 实验与结果
含 semantic relevance 的模型 AIC 最优；去掉它 ∆AIC≈23.2。smooth 项高度显著（p<.001）。非线性：中低相关度上升伴随时长缩短（促进），高相关度区反而拉长；探索分析显示对低频词尤其明显（语境中心词竞争/强调可能）。

## 结论
Semantic relevance 独立于频率/长度预测产出时长，且呈促进–抑制转折的非线性；提示产出与理解的语境机制不同。

## 点评
把理解侧语义拟合指标迁到产出计时并用 GAMM 抓拐点，方法匹配理论（促进 vs 竞争）。相关度依赖嵌入与窗口设定；“高频/低频依赖”偏探索，需预注册复现。
