# PrefSQA: Pairwise Preference Prediction for Speech Quality Assessment and the Critical Role of High Quality Datasets

- 论文编号：1512
- 报告人：Junyi Fan
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/fan26_interspeech.pdf

## 问题

MOS 标量受评分者与实验协议噪声影响，限制回归式自动语音质量评估。成对偏好更稳定，但多数工作仍依附 MOS，且公开偏好数据少，常从 MOS 派生，噪声掩盖模型真实差距。需要 MOS-free 偏好预测，并检验数据质量如何影响“看得见的改进”。

## 方法

PrefSQA 基于 UPPSQA 双编码器（wav2vec2 语义 + WavLM 声学层加权和），加入：不确定性感知 Bradley-Terry 偏好 logit（分数差除以方差温度）、损伤注意力头强调局部退化、批内特征级非匹配参考（NMR）头用软伪标 refine 全局排序。构建/精炼五类偏好集：SOMOS/NISQA 的 MOS 派生匹配与非匹配对，以及 LibriSpeech+CHiME-3 按 SNR 差模拟的低噪声 CHiLi M/NM；另用 SpeechEval、SpeechJudge 人类偏好与未见 IUB-COSINE 测泛化。训练从不使用 MOS 数值。

## 实验与结果

MOS 派生集上各强模型差距小（如 NISQA PrefSQA 83.84% vs UPPSQA 83.46%）；CHiLi 模拟集差距拉大（M：96.29% vs UPPSQA 85.88%；NM：90.37% vs 81.05%）。人类偏好与未见集上 PrefSQA 总体领先或接近最优。误分类对的 CCC 分析：MOS 派生集模型错在相近的小间隔对，模拟集 CCC 更低，说明标签噪声会掩盖架构收益。

## 结论

高质量、低噪声偏好数据对识别架构改进至关重要；PrefSQA 的不确定性、局部损伤与 NMR 模块在干净数据上带来清晰增益，并具一定跨集泛化。

## 点评

论文同时贡献模型与“评测数据质量认识论”：没有干净标签，再好的模块也看不出。CHiLi 对照设计有说服力。脆弱点是模拟偏好（更高 SNR）未必等于感知质量全貌；人类偏好集上优势不如模拟集夸张，真实听感噪声仍在。
