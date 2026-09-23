# Adapting Self-Supervised Speech Representations for Cross-Lingual Dysarthria Detection in Parkinson’s Disease

- 论文编号：773
- 报告人：Abner Hernandez
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hernandez26_interspeech.pdf

## 问题
帕金森构音障碍数据稀缺，跨语检测重要；自监督语音表示仍编码语言结构，即使固定 /pa-ta-ka/ DDK 任务也会与病理线索混淆。需在不重训 S3M、且尽量只用目标语健康对照的前提下做表示级对齐。

## 方法
语言平移（LS）：˜x = x_src − μ_src + μ_tgt，质心仅由各语健康对照（HC）在交叉验证折内估计。提取 HuBERT-Large、WavLM-Large、XLS-R-300M 说话人级向量；逻辑回归分类 PD vs HC，嵌套 CV 选阈使灵敏度≥0.9。数据：捷克、德语、西班牙语（PC-GITA）PD/HC 队列。设定：(1) 跨语——训练含源语 PD+HC 与目标语 HC，无目标语 PD；(2) 多语——含目标语 PD。

## 实验与结果
跨语无 LS：极高特异、低灵敏（如 HuBERT CZ Spec 0.98 / Sens 0.35）。加 LS 后灵敏与 F1 大幅上升（HuBERT F1：CZ 0.74、DE 0.61、ES 0.74）。多语设定下差距缩小，LS 常提高特异而灵敏大致持平。UMAP 显示源语 PD 点移向目标质心；HC 上语言 SVM 探针准确率由约 96% 降至近随机（约 29–34%）。德语与捷克/西语质心距离更大，跨语增益相对较小。

## 结论
DDK 上的 S3M 仍含强语言身份；HC 质心平移可削弱该结构并显著改善无目标语 PD 时的跨语检测，多语有目标语 PD 时收益更温和。

## 点评
把跨语失配压成一次向量算术，临床可部署性强。强在探针与可视化支撑“去语言”解释、阈值统一灵敏约束；弱在每种语言来自不同语料，语言效应与语料效应难彻底拆开，且任务高度受控，向自然语音推广待证。
