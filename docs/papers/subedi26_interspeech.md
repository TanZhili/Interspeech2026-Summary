# BiMamba2 Masked Discrete-Unit Prediction for Multilingual Speech Representation for Unsupervised Speech in the Wild Challenge

- 论文编号：2966
- 报告人：Prakriti Subedi
- 程序：Monday 28 September 2026 / Grand Special Challenges Poster Showcase
- 技术分类键：challenges
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/subedi26_interspeech.pdf

## 问题
UPS Challenge 要求在无标签、声学多样的 MLCommons Unsupervised People’s Speech 上学习多语语音表示，并用冻结表示在 LID（macro-F1）、ASR（CER）、说话人聚类（ARI）上评估。多数语言缺乏标注，现有监督预训练难以覆盖；挑战还要求 Open Filtering 子赛道上的可复现流水线。

## 方法
以 HuBERT 式掩码离散单元预测训练双向 Mamba-2（BiMamba2）编码器：每层前向/反向 Mamba2 SSM 与对角跳连相加。主模型 d_model=768、12 层，约 47.88M 参数。伪标签由对 80 维 log-mel 帧的 MiniBatchKMeans（k=200）离线得到；掩码约 75% 有效帧、3–5 连续块。损失为掩码位置交叉熵 + VICReg（方差/协方差）+ 弱 LID 交叉熵（λ_lid=0.05）。数据经 VAD 与质量过滤后约 250 小时、67 语种；批次 70% 语言均衡采样、英文硬顶 10%。推理时将帧级输出按前/中/后三段平均并 L2 归一化，经 Dynabench ModelController 提交。

## 实验与结果
官方 Dynabench：主结果取 step 19,500——ARI 0.735（高于 Whisper/HuBERT-large/XLSR/wav2vec 2.0），macro-F1 0.073，CER 0.870。step 48,000 的 CER 恶化至 0.998；小模型（d=512, 8L）全面更弱。本地 holdout 反而偏好 late checkpoint，且本地 LID 高估、ARI 低估官方分，作者分析为语言重叠与探针方法不一致。

## 结论
BiMamba2 + 掩码离散单元在说话人聚类上超过四条基线，但 LID/ASR 仍弱于监督基线，受数据规模与语种覆盖限制。晚期训练出现 CER 退化与嵌入几何变化；本地诊断不能可靠预测官方排名。缺组件消融、单次运行、伪标签未迭代 refinement。

## 点评
做法把线性复杂度双向 SSM 接到 HuBERT 式目标上，并靠 VICReg/弱 LID 稳住多语嵌入。强项是说话人聚类与对本地–官方失配的实证诊断；脆弱点是固定 k-means 目标易过拟合簇边界、LID 监督过弱且语种覆盖不足，内容任务难以追上大规模监督/SSL 基线。
