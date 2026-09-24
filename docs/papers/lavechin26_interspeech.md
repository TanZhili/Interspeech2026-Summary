# BabAR: from phoneme recognition to developmental measures of young children's speech production

- 论文编号：1132
- 报告人：Marvin Lavechin
- 程序：Wednesday 30 September 2026 / Clinical and Inclusive Speech Technology
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/lavechin26_interspeech.pdf

## 问题
婴幼儿语音发展研究依赖昂贵人工音素转写，难规模化；儿童（尤其低龄）ASR/音素识别仍极难，公开跨语标注稀缺。

## 方法
整理 TinyVox（PhonBank 标准化）：>50 万条 IPA 转写发声、560 名儿童、5 语、约 388 小时。训练 BabAR：比较多种 SSL 预训练（含儿童日长录音），用 CTC；微调时提供约 20 秒周围音频上下文。在留出纵向数据上提取典型/规范发声比例等发展指标并与文献对照。

## 实验与结果
多语儿童日长录音预训练显著优于成人-only 等替代；加长上下文进一步降错。替换多落在宽语音类别内，适于粗粒度发展分析。自动成熟度指标与文献发展估计对齐。相对既往约 60% PER 的儿童音素系统，正文报告显著改进（精确数字见全文表）。

## 结论
大规模跨语儿童音素数据 + 儿童中心 SSL + 上下文微调，使自动发展度量变得可行。

## 点评
TinyVox/BabAR 直接打通“标注债”与发展科学发展需求。音素清单跨语归一与 CTC 对齐误差仍在，细粒度临床音位诊断需谨慎；公开资源对复现价值高。
