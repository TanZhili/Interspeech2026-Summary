# Edge–Cloud Collaborative Speech Emotion Captioning via Token-Level Speculative Decoding in Audio-Language Models

- 论文编号：901
- 报告人：Ting Dang
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xue26b_interspeech.pdf

## 问题
Speech Emotion Captioning (SEC) 依赖大音频–语言模型，边缘设备算力不足、全量上云又有时延与生物特征隐私风险；小模型又难以刻画细粒度副语言与情感 grounding。静态边云切分忽略 token 难度差异。

## 方法
Uncertainty-Guided Speculative Decoding (UGSD)：边缘用 Qwen2.5-Omni-3B 起草 caption，以 token 熵作不确定性；若长度 L 块内最大熵超过阈值 γ，则只把该块（连同已接受前缀与设备端声学特征）送给云端 Qwen3-Omni-30B 校验；rank≤R 接受，否则用云端 argmax 纠正并丢弃后缀。L 在 {3,5,7} 间自适应。原始波形永不离开设备。

## 实验与结果
MER2024 英/中各 332 条。相对 edge-only：英文 BLEU 等相对提升约 21.6%–76.4%；中文 BLEU-1 +21.0%、ROUGE-L +38.5%、METEOR +111.7%。动态 L：总时延 40.21s→28.67s（1.4×）、OTPS 1.53→13.05（8.5×）；仅 18.2% token 上云。云端换成 7B 时增益变小但仍为正。

## 结论
作者认为 UGSD 在质量–效率–隐私间取得实用折中，适合 edge-first SEC；紧凑特征仍可能泄漏部分说话人/内容信息。

## 点评
把 speculative decoding 从单机加速改造成“难 token 才上云”，切中 SEC 部署痛点。评价在仿真边云环境，真实网络抖动未充分建模；熵阈值与 R 仍需验证集调参。
