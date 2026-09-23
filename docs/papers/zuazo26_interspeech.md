# MEG-to-MEG Transfer Learning and Cross-Task Speech/Silence Detection with Limited Data

- 论文编号：439
- 报告人：Xabier de Zuazo
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zuazo26_interspeech.pdf

## 问题
非侵入式言语 BCI 的 MEG 解码常受单被试数据极少（分钟级）限制，现有做法多为每被试、每任务从零训练；MEG→MEG 预训练及感知–产出跨任务迁移尚未系统验证。

## 方法
在 LibriBrain（单被试约 50 h 听录音书，306 通道，250 Hz）上预训练 MEGConformer，做语音/静音检测；再在 Bourguignon 等 18 名西语被试数据上微调（听、回放、出声朗读各约 5 分钟）。输入为 0.5 s 窗原始传感器；微调引入 RollAugment、软标签（窗内语音占比）等。对比同任务（in-task）与六种跨任务（train→test 不重训）下“从零训练 vs 预训练+微调”，指标 F1-macro、balanced accuracy、AUC-macro，Wilcoxon + Holm 校正与置换检验。

## 实验与结果
In-task：听任务迁移显著（准确率 +3.7%、F1 +2.6%、AUC +7.3%）；回放/产出有小幅提升但不显著；总体置换检验 p<0.001。跨任务从零已全体显著高于机会（准确率约 65.0–73.4%）。迁移后听↔回放增益最大（准确率约 +6.1–6.3%），涉及产出的跨任务也显著受益（约 +4.8–5.3% 准确率）。感知→产出优于产出→感知；多数被试正向迁移但个体差异大（如 Subject 16 产出 F1 −13.3%）。

## 结论
大规模单被试 MEG 预训练可在新被试、分钟级数据上提升语音检测，并增强感知–产出跨任务泛化；产出→听仍可高于机会，说明学到共享言语表征而非仅运动伪迹。局限：仅检测任务、英↔西语、单被试预训练、增益幅度有限且不稳定。

## 点评
工作把“临床标定数据太少”转成 MEG 领域迁移问题，并用跨任务方向性不对称来区分共享听觉表征与产出特有运动成分，比单纯刷同任务准确率更有信息量。脆弱点在帧级随机划分、不同实验室/语言与软标签设定，以及检测任务距音素/合成解码仍远。
