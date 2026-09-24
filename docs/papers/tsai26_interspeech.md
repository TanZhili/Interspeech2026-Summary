# The False Resonance: A Critical Examination of Emotion Embedding Similarity for Speech Generation Evaluation

- 论文编号：39
- 报告人：Yun-Shao Tsai
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tsai26_interspeech.pdf

## 问题
表达性合成与情感 VC 广泛用 emotion2vec 等嵌入的余弦相似度作 EMO-SIM；分类准并不等于零样本相似度可靠，说话人/语言学干扰可能主导距离，从而奖励声学模仿而非情感迁移。

## 方法
对嵌入做均值中心化以缓解各向异性。三类检验：(1) 分类情感三元组（无约束、同说话人同文本、说话人干扰、语言学干扰）；(2) 效价/唤醒的趋势单调性（Spearman ρ）与位移可辨性；(3) 人工偏好对齐（多模型合成候选，Fleiss κ=0.7349，保留 400 个强共识三元组）。另做 emotion2vec 各 Transformer 层探测。对照 emotion2vec/+ 与 HuBERT、Wav2vec 2.0、TERA。

## 实验与结果
同说话人同文本时准确率多仅约 60–70%；语言学干扰下 emotion2vec 在 CREMA-D 可跌至 3.38%，说话人/语言学干扰下常低于随机。位移可辨性近 50%，ρ 近 0。人工对齐约 52–65%，不足以为可靠代理。深层对人类对齐从 L0 约 58% 降到 L7 亚随机约 45%。

## 结论
当前情感嵌入空间不适合零样本 EMO-SIM；高 SER 准确率不能推出可用的情感相似度度量。建议用对比学习等校准抑制非情感声学因素。

## 点评
把“评测指标”本身当成被测对象，用对抗式采样暴露 false resonance，对滥用不加批判的 EMO-SIM 很有杀伤力。均值中心化已尽量抬分辨率，失败更像表征结构问题；尚未给出可替代的成熟指标，实践上仍需谨慎搭配听测。
