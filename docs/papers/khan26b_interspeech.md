# I Am No One: Style-Aware Paraphrasing for Text Anonymization

- 论文编号：3175
- 报告人：Ahmed Sohair Khan
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/khan26b_interspeech.pdf

## 问题
即使去掉显式标识，作者归属模型仍可凭稳定文风指纹重识别用户；该风险也延伸到会议/客服 ASR 转写。差分隐私文本匿名常严重损伤可读性与效用，而一般改写又缺少对风格标记的显式控制。

## 方法
两模块提示式流程（基座主要为 LLaMA-3.2-3B-Instruct，并测 MiniCPM3-4B）：
1. **风格画像**：从每位作者 K=5 样本，让 LLM 总结句长、词汇、语气、标点四维可读 profile；可消融单维。
2. **风格引导改写**：把 profile 写入提示，要求压制所述风格标记并保留语义；对比 semi-guided（只要求中性风格）与 unguided 改写。

评估 AUTHOR10（博客，10 作者）与 ILLINOIS9（短评，9 作者）；对比 DP-Prompt / Quasi-DP / Non-DP、ALISON；效用用余弦相似度、GPT-2 PPL、加权 KL；隐私用 BLEU、归属 F1、相对增益 γ 与流畅度感知 γf。

## 实验与结果
- 归属 F1 相对原文降约 60–70%：AUTHOR10 66.45→26.02（LLaMA），优于 ALISON 29.53；ILLINOIS9 76.78→20.76。
- PPL 接近原文（AUTHOR10 42.47 vs 41），远好于 ALISON（368）与严格 DP（ε=25 时约 8770）。
- Full profile 总体最稳；ILLINOIS9 上 Length-only 隐私增益可略更好。
- Style-guided 相对 semi-guided：隐私接近但效用与信息保留更好；纯 paraphrase 隐私与效用均更差。
- 补充：方法感知白盒攻击下 ILLINOIS9 攻击 F1 仍可从 77 降到 35；Yelp/IMDB 外域归属 F1 可降超 85%。

## 结论
显式风格画像引导的改写能在保持语义与可读性的同时大幅削弱作者归属信号，优于噪声型 DP 与无指导改写。局限包括依赖预设风格维度、指标可能混淆风格抹除与内容损失、尚未在 ASR 转写上系统验证。

## 点评
把匿名化重新定义为“可控风格变换”而非加噪，抓住了归属攻击真正利用的信号。对 ASR 会议文本有明确动机，但正文实验仍是博客/评论；若转写噪声与口语体改变风格线索，效果可能不同于干净文本。攻击者若利用残余内容而非纯风格，仍需与内容脱敏策略配合。
