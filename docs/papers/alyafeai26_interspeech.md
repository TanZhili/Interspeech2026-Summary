# Hamsa: A Manually Annotated Emirati Arabic Corpus for Speech and Language Technologies

- 论文编号：1049
- 报告人：Shaikha Alsuwaidi
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/alyafeai26_interspeech.pdf

## 问题
阿联酋方言（Emirati Arabic）在公开语音资源中严重不足；既有阿拉伯语语料多偏 MSA/埃及/黎凡特，Mixat 等 Emirati 资源又偏英阿语码转换，难以支撑纯方言 ASR。

## 方法
发布 Hamsa：从公开 UAE 内容收集、母语者手工转写并二次复核（约 16 人时）的单语对话语料，约 11 小时、4174 段（训练 11,000 段/10.74h，测试 861 段/51.8min）。制定方言正字与音系转写规范，排除重叠语音。在 Whisper-v2/v3、seamless-m4t、mms-1b-all 上以相同超参微调 3 epoch，并与 Mixat 交叉评测；FastConformer、ArTST-v3 仅零样本对照。

## 实验与结果
Hamsa 微调后：
- Whisper-v2：Hamsa WER 42.25%→24.46%，CER 71.91%→8.27%；Mixat 亦改善。
- Whisper-v3：29.69%→23.04% WER。
- mms-1b-all：69.60%→41.55%；Mixat 微调反而在两基准上变差。
方言匹配微调后的 Whisper 可超过零样本阿拉伯语专用模型（FastConformer 35%、ArTST-v3 38.29%）。

## 结论
小而精的方言匹配标注即可显著提升 Emirati ASR，并泛化到 Mixat。局限：规模约 11h、地理覆盖有限、划分非严格说话人无关、无正式 IAA、音频再分发依赖授权（公开版先给转写与采集脚本）。

## 点评
价值主要在资源与规范：把 Emirati 特有的 ق/ج、否定词、阴性形态等正字规则写清，直接解释了 MSA 模型的系统性错误。实验设计用 Mixat 交叉评测避免“只在自家测试集好看”，结论可信。11 小时量级对工业级 ASR 仍偏小，但作为低资源方言微调种子库定位清楚。
