# Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages

- 论文编号：3357
- 报告人：Ashwin Sankar
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/anand26b_interspeech.pdf

## 问题
众包成对评测可扩展，但印度多语与语音多维感知方差大；绝对 MOS 难诊断，仅报总体偏好无法解释“为何更好”。

## 方法
构建 5357 句、10 语基准（含规范化/符号/语码混合与 16 域）。1900+ 母语评委、>120K 成对比较，先锁总体偏好再评 6 维（可懂度、表达、音质、活泼、噪声、幻觉）。Bradley–Terry+Elo 排行，bootstrap CI；XGBoost+SHAP 解释轴对偏好的贡献；分析评委数/句数对排名稳定的影响。

## 实验与结果
排行：Gemini 2.5 Pro TTS > ElevenLabs V3 ≈ Sonic3 > … > IndicF5。Gemini 在 9/10 语与多数域领先；表达与可懂度对总体偏好贡献最大（SHAP），噪声/幻觉因多数系统已较强而区分度低。约 100–200 评委、~1000 句可达 ρ≥0.95 的排名一致。轴级判断可跨语预测总体偏好（准确率约 86%）。

## 结论
可控多维成对评测能稳定排出 Indic TTS 榜，并揭示偏好主要由表达与可懂度驱动；公开基准与偏好数据。

## 点评
规模与协议（先总体后分轴）设计扎实，对“可扩展又要可解释”的评测很有参考价值。商用系统主导榜单也暴露开源 Indic 差距；信噪/幻觉轴饱和时解释力下降，需更难的失败样本。
