# Speech Recognition to Accelerate Documentation of Marquesan and Cook Islands Māori

- 论文编号：3276
- 报告人：Rolando Coto-Solano
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/teikitohe26_interspeech.pdf

## 问题
马克萨斯语（Marquesan）缺乏公开 NLP/ASR 工作，田野自然口语转录慢，制约文档与社区回传。邻近波利尼西亚语（如 Cook Islands Māori, CIM）能否迁移、以及 ASR 草稿修正是否真能省时，证据仍矛盾。

## 方法
收集约 17 小时 L1 自然口语（38 说话人、六方言、ELAN 人工转录，排除明显法语码切换）。微调 Wav2Vec2-XLSR53、MMS、Whisper Medium、Parakeet、Qwen3 ASR、Omnilingual 等，部分加 KenLM；再对最优骨干做 Marquesan↔CIM 迁移与联合训练（CIM 约 4 小时）。另做小规模人时实验：纯手写 vs 对 ASR 输出在 ELAN 中修正。

## 实验与结果
单语：Wav2Vec2+LM 最佳，中位 CER=16.0、WER=31.4。联合训练 Marquesan CER/WER≈15.4/30.8（相对单语略好，Mann–Whitney 未显著）；CIM 反而不如单语（Mono CER/WER≈1.8/7.2）。人时：手写约 5.18–9.14 分钟/音频分钟，修正约 1.51–5.18，摘要称加速约 0.7×–2.4×。主要错误含词边界混淆。

## 结论
ASR 已可进入 Marquesan 文档流程并加速修正；与 CIM 联合对 Marquesan 仅有微弱帮助、对 CIM 无增益。计划把 ASR 嵌入社区工作流以加快材料回传。

## 点评
同时报模型误差与真实转录人时，比只刷 WER 更贴近文档场景。WER≈30 仍落在“是否省时”争议带附近，人时样本小；自然田野噪声与多说话人叠加使 CER–WER 落差大，词边界问题值得后续专项处理。
