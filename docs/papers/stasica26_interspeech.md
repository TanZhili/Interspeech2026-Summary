# Revisiting Emotion-Based Triage: Evidence from French Emergency Call Data

- 论文编号：1265
- 报告人：Elio Stasica
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/stasica26_interspeech.pdf

## 问题
文献常假设语音情感可直接反映急诊电话医疗紧急度，但多为模拟数据、情感分类准确率作终点，且优先级标签未必对齐真实调度方案，也未区分患者本人与第三方来电者。情感 alone 是否对临床优先级有增量信息仍缺实证。

## 方法
SAMU54 真实呼叫：每优先级随机 50 通，共 250 通（P3/P2 SNP/P2 AMU/P1/P0）。DiariZen 说话人分离后人工校对，拼接主说话人片段。分类情感：Lajavaness（Wav2Vec，五类：pleased/relaxed/neutral/sad/tense）；维量情感：SpeechDimEmo 帧级 arousal/valence 取中位数。用比例优势序次逻辑回归，经 AIC 选型：模型1 Priority~Emotion+Speaker Role+Age+Sex；模型2 含 Valence、Arousal、角色、年龄、性别及 Arousal×角色、Valence×Arousal。并检验分类情感能否由维量预测。

## 实验与结果
分类与维量表征对齐弱。模型1：年龄（β=0.035, p<0.001）与来电角色（家属/其他/医护相对患者均显著升高优先级）显著；各情感相对 Neutral 不显著；relaxed 从未被预测。模型2：年龄、男性、角色主效应显著；arousal/valence 主效应不显著；Arousal×Other（β=-1.00, p=0.024）与 Arousal×Valence（β=-0.24, p=0.036）显著；分层显示家属来电中更高 arousal 反而关联更低优先级。排除 P0 后 arousal/valence 主效应仍不显著。元数据整体比情感 alone 更具预测力。

## 结论
在真实法文 ECC、调度员标注优先级上，分类情感在纳入元数据后无增量；维量情感存在角色依赖交互，但情感 alone 是弱代理。作者质疑纯情感分诊路线，建议更大样本与临床 grounding 后再谈部署。

## 点评
价值在于用真实呼叫与专业优先级标签直接检验文献默认假设，并显式建模说话人角色——这解释了为何“紧张=紧急”可能不成立。样本每级仅 50、P0 几乎无患者本人说话，因果解释需谨慎；依赖现成法语 SER 也可能把模型偏差带入回归。
