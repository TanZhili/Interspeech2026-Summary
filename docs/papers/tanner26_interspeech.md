# wav2VOT: automatic estimation of voice onset time, closure duration, and burst realisation with wav2vec2

- 论文编号：743
- 报告人：James Tanner
- 程序：Monday 28 September 2026 / Tools and Techniques for Phonetic Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/tanner26_interspeech.pdf

## 问题
语音学流水线中 VOT、闭塞时长、爆破实现等标注常需大量人工校正或专用训练数据。大模型如 wav2vec2 在分类任务上表现好，但能否直接服务塞音细粒度声学标注仍待检验。

## 方法
提出 **wav2VOT**：基于 wav2vec2 对塞音片段做帧级分类（闭塞/爆破等状态），经上采样达约 **1 ms** 时间分辨率，再由状态序列推定 VOT、闭塞时长与爆破是否实现。可零样本用于未见语料，也可对目标数据集微调。默认最小区间约 5 ms。

## 实验与结果
- 初始模型：帧准确率约 **96.4%**；爆破实现准确率 **93.3%**（F1 0.96）；微调后更高。
- 未见语料（如 SWB、BB）上，多数 VOT 在 5 ms 容差内的比例与既有工具可比（如约 80% vs 73–79%）；闭塞时长估计容差略宽。
- 贝叶斯对比显示，手动与 wav2VOT 在整体 VOT/闭塞时长及清浊、部位效应上差异可忽略（如浊音对比约 10.76 vs 10.5 ms）。

## 结论
wav2vec2 类大模型可产出接近人工的塞音标注；微调进一步提升，并激励将其用于更多语音学标注任务（如负 VOT、预送气等）。

## 点评
把通用 SSL 表征接到经典语音学测量点，门槛低于专用对齐器再手工改。强在跨语料可比与效应量验证；脆弱在闭塞边界本身就比 VOT 难标，以及不同三向对立/方言实现需额外验证。
