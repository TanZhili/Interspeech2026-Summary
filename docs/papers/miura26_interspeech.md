# Profiling Speech Rate Abilities of Visually Impaired Screen Reader Users by Bayesian Item Response Theory

- 论文编号：3096
- 报告人：Takahiro Miura
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/miura26_interspeech.pdf

## 问题
读屏 TTS 语速配置缺乏证据：简单正确率把题目难度与个人能力混为一谈，且日语研究不足；传统 IRT 需大样本，视障小样本难用。

## 方法
11 名日语视障读屏用户（全盲 6、低视力 5）。ITA 语料 42 句×5 语速（150–500 WPM）用 macOS Kyoko 合成；复述算 mora 正确率，另评可懂度/可听性 Likert。贝叶斯累积 probit（等级反应）与 beta 回归分离题目难度与个人能力；弱信息先验，brms HMC。并回归盲视状态与相对听速经验。

## 实验与结果
模型收敛（最大 R̂=1.004）。能力个体差大（可懂度 SD 0.91，可听性 1.10）。相对 150 WPM，≥300 WPM 可懂度显著下降（β≈−1.23 至 −2.00）；中长句反而更易。全盲能力高于低视力；盲视状态与听速经验独立预测理解，但听速经验对可听性为负。全文局限讨论有截断。

## 结论
贝叶斯 IRT 可在 N=11 下为 TTS 语速评测分离难度与能力；约 250–300 WPM 为该经验群体门槛，个性化需同时考虑盲视类型与习惯语速。证明概念，需更大样本。

## 点评
把无障碍读屏评测从“平均正确率”推进到可解释的人–题潜变量尺度，适合小样本特殊人群。弱先验与宽可信区间是诚实代价；有效响应仅 2310/6930、经验用户偏多，外推新手与默认语速设计需谨慎。
