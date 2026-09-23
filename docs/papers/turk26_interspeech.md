# When “yeah” means “not quite”: Multimodal detection of backchannels expressing incomplete understanding

- 论文编号：713
- 报告人：Olcay Türk
- 程序：Wednesday 30 September 2026 / Entrainment and Dialogue Coordination
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/turk26_interspeech.pdf

## 问题
表面肯定性反馈（如“mhm”+点头）未必反映真实理解；这种“不一致 backchannel”会误导 grounding，但其声学、头部与话语结构线索是否可系统区分尚不清楚。

## 方法
基于 MUNDEX 桌游讲解语料中 45 段德语互动：EE 事后 video-recall 自标理解水平，将表面肯定反馈标为 congruent（675）或 incongruent（809）。提取声学、头部运动（俯仰/滚转加速度等）与话语特征（话题时长、距既往提及距离等），用嵌套交叉验证的 XGBoost 分类并用 SHAP 解释。

## 实验与结果
CV：Average Precision 0.73、ROC-AUC 0.71、F1≈0.68；保留验证集准确率 0.73。SHAP 显示平均头俯仰角最重要（不一致时更中性直立）；话题时长与距既往提及次之；声学动态性偏低亦关联不一致。短而久未提及的话题、或新引入的长密话题更易预测为不一致。

## 结论
不一致与一致 backchannel 可由多模态特征系统分离；不一致反馈往往伴随更低信号努力（中性头姿、较低声学动态）。

## 点评
用 video-recall 锚定主观理解状态，把“假懂反馈”做成可学标签，对解释性对话系统有直接价值。局限是仅正面词汇反馈、德语桌游场景、单标注者理解归类，以及分类目标偏特征诊断而非实时检测。
