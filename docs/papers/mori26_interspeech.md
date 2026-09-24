# Evaluating Automatic Laughter Phone Annotation for Socially-Situated Laughter Synthesis

- 论文编号：2141
- 报告人：Hiroki Mori
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/mori26_interspeech.pdf

## 问题
情境化笑声合成依赖笑声 phone 标注，人工成本高；既有自动识别数据少、未见说话人弱，且识别误差对合成质量的影响未系统验证；音频 LLM 路线是否还需要 phone 标注也不清楚。

## 方法
在 AGSC/OGVC 上新建 11 说话人笑声集，用改进的 XLSR-53 framewise+d 识别器（含时长后处理）。合成对比：SPSS（BiLSTM 参数语音合成，显式用 phone）与 Fish-Speech（音频 LLM，prompt）。条件含 ManualLabel、AutoLabel、AutoLabel+（SPSS 增广）、NoLabel。听测评自然度 MOS 与“笑法/个体性” SMOS。

## 实验与结果
未见说话人：PBE 23.0 ms，替换/删除/插入约 30%/14%/7%，辅特征错 15%，优于先前未见结果。自然度：Fish（约 3.5–3.6）高于 SPSS（Manual 2.71，Auto 2.51，NoLabel 1.62）。笑法相似度：SPSS Manual 3.94 ≫ Auto 3.46 ≫ Fish（约 2.5）；个体性 SPSS Manual 也更高。Fish 上有无 phone 差异不显著；SPSS 上自动标注明显弱于人工。

## 结论
自动标注对未见说话人已可用但仍不足以匹配人工；Fish 自然度好但笑法可控性弱，SPSS 相反——尚无同时兼得的单系统。

## 点评
把“识别准不准”落到合成听感三条轴上，比只报 PBE 更贴应用。自动–人工标注风格不一致可能放大 AutoLabel 劣势；Fish 的 LoL prompt 实验说明 token 模型对笑声结构仍缺显式控制杆。
