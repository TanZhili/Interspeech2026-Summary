# GADVOX: The German Anxiety and Depression Voice Examination Dataset

- 论文编号：3523
- 报告人：Robert P. Spang
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/spang26_interspeech.pdf

## 问题
抑郁/焦虑语音研究过度依赖英语小样本（如 DAIC-WOZ）；德语公开资源缺失，且多仅做二分类，难支撑严重度回归与共病建模。

## 方法
众包采集 GADVOX：1004 名成人、10 条随机顺序的结构化自由说提示，人均约 18.4 分钟自发语音；同人自填 PHQ-9 与 GAD-7（α=0.85/0.86）。四阶段质控（注意力陷阱、自动筛、人工听感、ITU-T P.566 质量估计），从 1420 人中保留 1004。元数据 CC BY 4.0 公开，音频经申请提供。

## 实验与结果
人口统计覆盖 18–77 岁；PHQ-9≥10 占 29.2%，GAD-7≥10 占 20.9%，两量表相关 r=0.795。另含创伤等社会心理条目与会话质量分。正文以数据集描述与分布分析为主，未报告下游检测基线模型。

## 结论
提供首个可公开申请的德语抑郁–焦虑严重度配对语音语料，支持多目标回归与共病研究。

## 点评
规模与双量表严重度标注相对 DAIC-WOZ 是实质进步；众包偏高教育/数字素养，自报筛查≠临床诊断，音频非完全开放需注意获取门槛。
