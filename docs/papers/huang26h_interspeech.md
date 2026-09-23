# RAS: a Reliability Oriented Metric for Automatic Speech Recognition

- 论文编号：1409
- 报告人：Wenbin Huang
- 程序：Monday 28 September 2026 / Spoken Language Processing: Evaluation and Metrics
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/huang26h_interspeech.pdf

## 问题
噪声/模糊下 ASR 常吐出看似通顺却错误的转录；WER 只评准确率、不评可靠性；整句拒识又丢掉可用片段。需要细粒度弃权与匹配的评测/训练目标。

## 方法
扩展词表加占位符 PH，允许对不确定片段弃权。RAS 用修改编辑距离：PH 可对齐任意长度参考跨度，相关代价乘 α∈(0,1)；RAS=Usefulness−Cost。α 由听测 + Bradley–Terry 拟合（约 980 标注，α*≈0.5064）。训练：Whisper-Tiny 上先 GT 引导把错误段换成 PH 做监督，再用 GRPO 以 RAS 为奖励做强化学习。

## 实验与结果
LibriSpeech：PH-Supv+RL 的 RAS 0.8811，高于 Base 0.8603 与 logit 阈值基线。TALCS 码混：从负 RAS −0.11 升至 0.48。噪声 LibriSpeech 上 SNR 越低相对收益越大（0 dB 提升约 0.27）。消融显示 RL 在监督之上继续抬升。

## 结论
作者认为段级弃权 + 人类校准的 RAS 可在保持有用信息的同时提升可信度，尤其在噪声与码混场景。

## 点评
把选择性预测从“整句拒”做成“局部 PH”，对高风险场景务实。α≈0.5 意味着弃权代价约半个词错——与听测对齐是亮点。基座为 Tiny，规模外推未证；PH 过多会伤 Usefulness，RL 需在二者间权衡。
