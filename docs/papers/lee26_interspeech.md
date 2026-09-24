# AdaLTM: Adaptive Layer-wise Task Vector Merging for Categorical Speech Emotion Recognition with ASR Knowledge Integration

- 论文编号：80
- 报告人：Chia-Yu Lee
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26_interspeech.pdf

## 问题
把 ASR 知识并入 SER 时，特征级融合受转写错误影响，多任务学习又因目标冲突（ASR 要抑情感、SER 要情感变异）产生梯度干扰；域外 ASR 任务向量还会丢掉副语言线索。

## 方法
AdaLTM：在 WavLM-Large 上分别于 MSP-Podcast 微调得到域内 ASR/SER 模型，提取任务向量 ΔW=W_ft−W_base；冻结骨干与向量，仅学习每层系数 λ_ASR^{(l)}, λ_SER^{(l)}（25 层含前端）做加权合并，再对 24 层隐状态做可学习加权求和送分类头。对比 LibriSpeech 域外 ASR 向量与全局/静态合并。

## 实验与结果
MSP-Podcast v1.12 八类情感。MTL 基线 UAR 约 29%，而 Dual-Vector AdaLTM 达 UAR 38.94%、MaF1 35.20%；SER-Only 略高（39.09%）但 Dual 显著优于冻结基线（37.05%）。域内优于域外（38.94% vs 38.68%）；层自适应优于静态全局 λ=0.5（38.30%）。可训练参数约 0.46M。

## 结论
作者认为权重空间层自适应合并可规避 MTL 梯度冲突，并强调域一致 ASR 知识；局限是需要域内转写以提取 ASR 向量，且前期仍要分别微调专家模型。

## 点评
用 task vector 绕开“ASR↔SER 梯度打架”很干净，层系数可视化也解释了语言锚定与韵律主导。Dual 略低于 SER-Only 符合容量挤兑直觉；没有可靠转写的低资源情感数据会卡住整条管线。
