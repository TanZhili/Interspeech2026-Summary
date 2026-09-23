# Rethinking Acoustic Variability Of ADReSS and ADReSSo Datasets For Dementia Detection

- 论文编号：2862
- 报告人：Muhammad Abdullah Zafar
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/zafar26_interspeech.pdf

## 问题
ADReSS / ADReSSo 已成为语音痴呆检测事实标准，但小数据、录音条件残余不平衡可能导致模型利用通道伪相关而非病理线索；既有工作已显示静音段也可区分，整段录音上低层声学特征是否同样脆弱尚欠系统检验。

## 方法
对 openSMILE 的 eGeMAPS（88）与 ComParE（6373）做单特征筛选后再做两特征组合；一律用可解释的 logistic regression，报告 macro-F1。评价设定：(1) 官方 challenge 测试集；(2) 训练标签随机置换 100 次负对照；(3) 全数据 70/30 平衡蒙特卡洛重采样 100 次。另用 pyannote VAD 构造 silence-only / speech-only 变体，检验高分特征是否依赖语音本身。

## 实验与结果
两特征即可逼近 SOTA：ADReSS macro-F1 0.875（SOTA 0.895），ADReSSo 0.831（SOTA 0.857）；所选特征偏听觉滤波能量分位、谱质心导数、MFCC 统计等，易受通道/静音边界影响。同一特征对上 silence-only 反优于 speech-only（0.702 vs 0.643；0.631 vs 0.576）。标签置换时测试 F1 上界可分别摸到 0.875 / 0.831。蒙特卡洛下两特征均值降至 0.622 / 0.667；eGeMAPS 中极少特征对在 ≥50% 迭代复现，ComParE 无一达标，复现对最高也仅约 0.73 / 0.69。

## 结论
强测试分可能来自固定划分上的偶然相关，不宜过度解读；小样本痴呆语音评测应报告重采样离散度、标签置换负对照，并重视可解释、锚定临床标记的建模。

## 点评
用“极简两特征 + 负对照 + 重采样”拆穿乐观测试集，方法论上很干净，对后续凡报 ADReSS(o) 数字的工作都是重要刹车。它不否定病理声学信号存在，而是证明当前划分与 LLD 探针不足以支撑强泛化声称；后续若继续用这两套数据，至少应把蒙特卡洛均值/方差与静音对照一并报出。
