# VIP-MINGLE: A Corpus for Videoconference and In-Person Multimodal Interaction in Group Language Engagement

- 论文编号：2367
- 报告人：Andrew Chang
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chang26f_interspeech.pdf

## 问题
多人会话模型多在面对面语料上训练，视频会议会重构轮替与非言语行为；缺同一被试组跨两种介质、可对照的多模态公开数据，难分离介质效应与任务/说话人混淆。

## 方法
VIP-MINGLE：32 组、105 人、约 59 小时；组内完成面对面与 Zoom 两场（顺序平衡），任务为 Family Feud 式协作问答。提供原始音视频、心理测量、说话人分离、Whisper 转写、OpenFace/DeepFace 特征与人工时间标注。DOI 发布。

## 实验与结果
配对比较：视频会议轮替间隙更长（β=0.113,p=.037）、话语更短（β=−0.094,p<.001）；语言句法复杂度与面部 AU/表情亦有系统性偏移（视频会议整体表情更弱但部分局部增强）。结论为质变式行为分布偏移而非单纯降质。

## 结论
被试内跨设置多模态语料可量化域偏移，支撑跨介质稳健的群组会话模型。

## 点评
设计核心是 within-subject 对照，比拼凑不同视频会议语料更干净。特征管线开箱可用；样本以大学生为主、任务偏游戏化，外推到职场会议需谨慎。
