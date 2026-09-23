# Analyzing Longitudinal Vocal Changes During Cognitive Behavioral Therapy for Hikikomori Patients

- 论文编号：742
- 报告人：Samara S. Leal
- 程序：Tuesday 29 September 2026 / Clinically Useful Speech Representations 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/leal26b_interspeech.pdf

## 问题
CBT/ICBT 疗效监测缺客观时序标记；多数抑郁语音研究做静态分类或前后差，难刻画治疗过程中的个体轨迹。

## 方法
SOLITAIRE 试验 35 名 hikikomori 患者、8 次会话、约 276.7 h 语音。会话级 MFCC 汇总，相对首会话基线校正。RQ1 用趋势/变异/早期跨被试稳定性筛稳定纵向 MFCC；RQ2 比较 Better/Worse 结局轨迹；RQ3 在 LOPO 下比较 MFCC+F0（MLP）与 wav2vec2（GRU）及融合。结局为归一化抑郁量表前后变化。

## 实验与结果
低阶 MFCC1–3 纵向趋势最强。年轻成人 Better/Worse 中后期轨迹分化更清晰，青少年更嘈杂。融合 wav2vec2 与 MFCC+F0 在各年龄/性别分层上 F1 最高，显示深度与手工特征互补。轨迹演化优于静态前后差。

## 结论
治疗相关语音变化更宜用会话轨迹刻画；深度与声学描述子融合可更好预测 ICBT 结局。

## 点评
真实纵向临床语音与 within-patient 归一化设计有价值。队列小、Better/Worse 阈值阈值依赖分位，泛化谨慎；仅分析声学特征符合伦理，但丢掉语言学线索也可能限性能。
