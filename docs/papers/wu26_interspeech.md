# LISE : Listenable Interpretable Speaker Embeddings

- 论文编号：537
- 报告人：Xiaoliang Wu
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wu26_interspeech.pdf

## 问题
ASV 说话人嵌入黑箱；属性探测需标注且常伤性能，高维稀疏表示又缺听者验证。需无标签、保性能且对人可听可分的分解。

## 方法
LISE 将冻结 x-vector/ECAPA 嵌入 \(e\) 分解为 \(K\) 个正交、非负权重成分：\(\hat e=Wc\)，损失为重建 + \(\lambda\|W^\top W-I\|_F^2\)。VoxCeleb2 说话人级均值嵌入训练；K≈35。听辨：按成分权重高低组 Type A / Non-Type A，熟悉后判候选归属。

## 实验与结果
Vox1-O：LISE EER x-vector 3.08%（原 2.30%）、ECAPA 2.10%（原 1.80%），优于属性监督 Luu 等（6.70%）并接近 PCA。听辨总体准确 83.9%，显著高于 PCA 59.1% 与 Iben 等 49.0%；35 成分中多数过 70%。半量数据训练仍稳。

## 结论
低维正交非负分解可在几乎不伤 ASV 的同时得到听者可分成分；未来可用于可控合成与偏差诊断。少数成分反映语言而非声线是局限。

## 点评
把“可听性”作为可解释性硬指标，相对仅声学相关更有说服力。成分语义仍依赖听者描述，非客观标签；VoxCeleb 多语噪声使部分轴混入语言模式。
