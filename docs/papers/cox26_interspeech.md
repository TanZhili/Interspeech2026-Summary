# Learning task-specific subspaces via interventional post-training of speech foundation models

- 论文编号：2542
- 报告人：Jack Cox
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cox26_interspeech.pdf

## 问题
SSL 语音基础模型的表示把说话人与内容等变量纠缠分布在同一空间；下游任务通常只需部分变量，标准对比学习多学单一不变子空间，缺少基于干预数据的因果式多子空间分离。

## 方法
提出 interventional contrastive learning：用 F5-TTS 在 LibriTTS 参考音上合成可干预数据（训练 32 说话人×256 文本=8192 句，开发 6×256=1536），按说话人–内容矩阵构批。冻结 wav2vec 2.0 / HuBERT / WavLM Base，均值池化后经约 1.8M 参数 3 层 MLP，将 768 维切成内容/说话人各 384 维子空间；多正样本对比损失（温度 \(\tau\)）加子空间正交正则。对比单子空间变体与无投影基线。评测：子空间直接余弦相似度做 VoxCeleb1 OOD 说话人验证（EER）；SUPERB 式线性头做 Speech Commands 关键词检出（准确率）。

## 实验与结果
说话人匹配子空间相对无投影显著降 EER（如 WavLM：38.7→约 24.7）；内容匹配子空间 KS 准确率低于池化骨干（WavLM：96.9→93.0），但仍有一定竞争力。匹配与不匹配子空间的 SV 差距支持一定分离；联合学习未必优于分别学单子空间。wav2vec 2.0 末层整体更弱。绝对 OOD EER 仍高（约 25%），因合成朗读 vs 野外语音且仅 32 说话人。

## 结论
作者认为干预对比后训练能把说话人信息从纠缠表示中拆出并改善 OOD SV，同时维持相近 KS；联合学习未显示额外收益。后续拟扩到真实大数据、换层加权并显式惩罚信息泄漏。

## 点评
工作把因果干预/合成可控对用到语音后训练，子空间交叉评测设计清晰。强项是弱标签干预矩阵与正交约束的可解释性；脆弱点在于 TTS 域与 VoxCeleb 差异大、内容对比目标（整句）与 KS（词级）错位，且末层特征与信息泄漏仍限制分离纯度。
