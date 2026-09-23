# Hearing Smiles in the Crowd: How Babble Noise Shapes Smiled Speech Perception

- 论文编号：1178
- 报告人：Rong Li
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/li26t_interspeech.pdf

## 问题
听觉“微笑语音”研究多在干净条件下进行，而真实场景常有多说话人 babble 掩蔽。噪声是否削弱 smile-like 检测，以及在 smile-like 内部对 amused 与 spread-lip 的区分是否同等受损，尚不清楚。

## 方法
基于 AMuS 语料，选取覆盖 amused / spread-lip / neutral 的 Speaker B（法语男）与 Speaker C（英语女）；干净语音归一化至 70 dB，与 NOISEX-92 食堂 babble 混合，条件为 Quiet、−3 dB、−6 dB。任务 1：smile-like vs. neutral；任务 2：仅 smile-like 上 amused vs. spread-lip。经 Prolific 招募并通过耳机与注意力筛查后，有效样本为英语流利 38 人、法语流利 37 人。用二项 GLMM（Noise×Category、Speaker 交互，被试与刺激随机截距）分析正确率，并用 SDT（d′、准则 c、AUC）分离敏感度与反应偏向。

## 实验与结果
任务 1：相对安静与中性，spread-lip 与 amused 在 −3/−6 dB 准确率显著下降，中性相对稳定；amused 全程高于 spread-lip，且二者噪声效应近似平行。d′ 由 1.87→1.00→0.58，c 由 0.09→0.49→0.69（更保守、更少报“听到微笑”）；AUC 由 0.97→0.83→0.73。任务 2：安静时 amused 明显更准，噪声下 amused 准确率骤降而 spread-lip 上升并出现交叉；d′ 1.28→0.82→0.55，c 由 −0.51（偏 amused）翻转为 0.25/0.64；AUC 0.93→0.84→0.77。Speaker 效应主要出现在任务 1 的中性与 spread-lip。

## 结论
噪声不仅降低微笑判断的感觉证据，也促使听者在不确定下转向更保守的决策策略；任务 1 中 amused 比机械 spread-lip 更易识别，与更丰富的情感声学线索一致。局限包括仅两名说话人及语料说话人/语言/性别混杂，正文末段也提醒谨慎外推。

## 点评
工作把微笑语音感知从“能否听出来”推进到噪声下敏感度与准则如何联动变化，对无视觉的嘈杂通信与相关语音技术评测有直接含义。实验设计清晰，但说话人覆盖极窄，Speaker 差异也可能混入性别与语言，结论更适合作为机制证据而非大规模人群效应估计。
