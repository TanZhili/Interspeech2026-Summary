# Do Speech Emphasis Models Generalize across Languages and Emotions?

- 论文编号：2783
- 报告人：Megan Wei
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/wei26e_interspeech.pdf

## 问题
既有强调检测多在英语中性朗读/合成数据上训练，跨语言族、跨情绪唤醒与感知–合成标签的泛化能力不明。

## 方法
发布 MMEE：7 语（含变体）、34 情绪/风格、约 1 万句（14.13 h）、每句 10 人三级感知标注。基准 EmphaClass 与 WhiStress，覆盖单语、跨语、多语、跨唤醒、跨数据集与数据规模设定。

## 实验与结果
单语零样本跨语衰减明显，尤其类型距离大的语言；多语训练显著提升稳健性。高/低唤醒情绪间双向迁移稳健；感知与合成基准可相互迁移，提示共享韵律结构；较小训练规模下性能仍较稳。WhiStress 总体准确率常高于 EmphaClass；Pearson 相关显示跨语难度更大。

## 结论
强调建模需多语多情绪数据：多语训练优于单语零样本；情绪唤醒与标签来源并非主要瓶颈。

## 点评
用专业演员表达语料填补「多语+情绪+人类分级标注」空白，直接服务 TTS/翻译中的强调控制。Cohen’s κ 中等（约 0.29–0.52）反映强调主观性；专有语料可复现性依赖公开发布范围。
