# Evidence Subspace Projection: Measuring How Much Evidence Explains Deepfake Detection in Self-Supervised Speech Models

- 论文编号：3210
- 报告人：Yixuan Xiao
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xiao26c_interspeech.pdf

## 问题
SSL 前端驱动的 ADD 域内很强、域外常塌，不清楚决策究竟依赖攻击类别、编解码、静音结构等哪类证据。既有解释常把前端与后端缠在一起；需要把冻结 SSL 前端单独拿出来，定量度量“多少决策可由某类证据解释”。

## 方法
Evidence Subspace Projection：由 Transformer FFN 神经元激活模式构造标签向量（真伪、攻击等），经 one-vs-rest 残差得到决策轴；再把决策向量投影到各证据子空间，得到解释比例标量。在 raw / fine-tuned / post-trained 设定下评估 XLSR、HuBERT 等，训练/测试覆盖 ASVspoof 2019/2021/5。

## 实验与结果
微调可降低 within-spoof 组对决策轴的对齐（E_rank），XLSR EER 整体低于 HuBERT（如训 ASV19：ASV19 0.25 vs 0.53；ASV5 17.98 vs 22.47）。低 E_rank 与低 EER 在 22 组中 18 组一致；例外分析显示聚合 EER 可被 VC 多数类拉低，掩盖 TTS 弱点。Post-training 进一步压低部分 within-spoof 对齐。

## 结论
作者认为该方法可复现并细化既有发现：冻结前端已编码大量真伪相关结构，微调/后训练会重塑决策与证据因素的关系，可用于诊断模型是否过拟合伪迹。

## 点评
把“解释力”收成可投影的标量，比纯可视化更可比较，尤其适合拆开 SSL 前端贡献。E_rank 与 EER 偶发背离提醒：证据对齐是诊断量，不等于检测分数；证据因子库本身也依赖元数据完备性。
