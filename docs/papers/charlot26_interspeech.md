# BabyHuBERT: Multilingual Self-Supervised Learning for Segmenting Speakers in Child-Centered Long-Form Recordings

- 论文编号：2772
- 报告人：Théo Charlot
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：https://www.isca-archive.org/interspeech_2026/charlot26_interspeech.pdf

## 问题
儿童中心日长录音含大量非语音、重叠、远场与儿童声学特性，成人干净语音预训练模型失效；英语日长预训练（如 W2V2-LL4300）规模与语种覆盖不足。

## 方法
BabyHuBERT：在 40+ 语种约 13,164 小时儿童中心录音上做 HuBERT 式两轮掩码预测预训练（先用 PyanNet-VTC 抽语音段，非英语约 43%）。在 BabyTrain-2025（670h）上微调多标签 Voice Type Classification（关键儿童/其他儿童/男成人/女成人），仅训 Transformer。与成人 HuBERT、英语日长 W2V2-LL4300 对比。

## 实验与结果
BabyHuBERT-VTC 在六语料 F1 55.0%–76.1%，平均 66.9%，接近人类标注者 69.8%；一致优于 W2V2-LL4300 与 HuBERT。Vanuatu、Solomon Islands 上相对 HuBERT 绝对 F1 +14.0 / +18.3。模型与代码公开。

## 结论
大规模多语儿童中心域预训练显著提升说话人类别分割，缩小与人类标注差距，并惠及低资源语种研究。

## 点评
用真正“脏”的日长域做 SSL，比继续微调成人模型更对症。多标签 VTC 贴合发育研究“谁在说”需求。预训练依赖 VTC 过滤可能引入偏差；少数语料仍距人类有差距。
