# Beyond Binary: Speech Representations Across the Cognitive Score Hierarchy

- 论文编号：2725
- 报告人：Serli Kopar
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/kopar26_interspeech.pdf

## 问题
临床语音分析常做 AD vs HC 二分类，对 MCI 细微变化不敏感；英语单任务语料多，且把各临床分数当扁平独立目标，忽视 CERAD+/MMSE 固有的任务—领域—全局层级结构。

## 方法
TREND 德语队列：MMSE + 五项 CERAD+（RW、BNT、RL、VF、PF），质控后 959 会话 / 593 人（698 HC、261 MCI）。优化 diarization 后得到 Prosody-Preserved 与 Concatenated 两路音频；提 eGeMAPS（prosody / voice-quality / all）与 wav2vec 2.0、HuBERT 全局均值池化嵌入。对每个层级目标独立训练 Ridge / SVM(R) / XGBoost，开发集 5×3 嵌套交叉验证（被试不相交），再在 hold-out 验证。层级：任务分 → 领域复合分（LAN/MEM/EXE/VIS）→ CERAD+ 总分（连续与阈值 85）及 MCI 二分类（>1.5 SD）。

## 实验与结果
Level 1：SSL（尤其 HuBERT）普遍优于手工艺声学；开放任务（VF/PF）相关更高，HuBERT 预测 PF 达 r=0.85±0.02（HO 0.80）。Level 2：HuBERT 仍最强，画图导向的 EXE/VIS 更弱。Level 3：开放任务出现“稀释”（任务级 → 全局级下降），受限任务（MMSE、RW）出现反向稀释。MCI 二分类最佳为 MMSE + eGeMAPS All（DEV 0.62±0.07，HO 0.63）；连续/二值 CERAD+ 与 LAN 等则 HuBERT 更优。SVM 权重显示 MCI 侧 F0/谱斜率不稳定等可解释声学线索。

## 结论
语音特征预测力同时取决于认知目标所处层级与任务约束：开放任务偏“专家”、受限筛查偏“通才”。局限为单一德语队列且未纳入社会人口学/生活方式协变量；未来可跨语言验证并做联合层级建模。

## 点评
把“测什么分数”和“任务开放度”绑在一起分析，比单一 MCI 准确率更能解释 SSL 与手工特征何时互换优劣。设计上被试不相交 + hold-out 较扎实。MCI 二分类绝对水平仍中等，且 EXE/VIS 靠言语任务跨域预测，泛化边界需明确；“specialist/generalist”是有用归纳，但依赖当前电池构造，不宜过度外推。
