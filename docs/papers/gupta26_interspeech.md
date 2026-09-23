# Closing the Modality Gap via Simplex-Constrained Representations

- 论文编号：2849
- 报告人：Shubham Gupta
- 程序：Monday 28 September 2026 / Model of Speech Perception
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gupta26_interspeech.pdf

## 问题
CLIP/CLAP 等对比多模态模型虽对齐配对样本，但模态质心仍系统性分离（modality gap），可能扭曲跨模态相似度；既有办法多改目标或架构。作者问：仅改输出几何——从单位球面到概率单纯形——能否在几乎不动预训练骨干的情况下大幅闭合该间隙且不伤检索。

## 方法
冻结 LAION-CLAP（音–文）与 FLAVA（图–文），加共享轻量 Linear/MLP adapter（可训参数 <1%）。欧氏分支：L2 归一化到球面，用余弦；单纯形分支：同一 adapter 后 softmax 到 ∆^{d−1}，用负 Total Variation 打分。另设 XAttn（共享交叉注意 + 欧氏余弦）对照 ReTreever（同注意机制 + 多分辨率单纯形），以及 MRL 作为欧氏 coarse-to-fine。用对称 in-batch InfoNCE（DPR 式）训练。指标：质心 ℓ₂、silhouette、几何校正 RelGap（质心距/模内散布），检索 NDCG@10。数据：Clotho、SoundDescs、AudioCaps、MS-COCO、Flickr30k。

## 实验与结果
五基准上，把相同 adapter 换成 softmax 单纯形后，质心 ℓ₂ 从约 0.36–0.81 降到约 0.005–0.020（降幅 97–99%），RelGap/silhouette 亦改善，NDCG@10 持平或更好（如 Clotho T2A 0.259→0.382；SoundDescs 上 ReTreever 0.535/0.542）。XAttn 仍保留大间隙，而 ReTreever 显著更小，说明闭合主因是输出几何而非交叉注意。Coarse-to-fine：MRL 间隙随维数增大（AudioCaps 2-d→256-d 约 0.032→0.534），ReTreever 全程 <0.06。估计 Dirichlet α̂ 显示高维单纯形嵌入偏稀疏，间隙仍小，支持“真对齐”而非纯距离尺度假象。

## 结论
单纯形的非负与单位质量和（及 softmax 对全局 logit 平移不变）构成跨模态校准先验，可在不改骨干下闭合 modality gap 并保持检索；共享交叉注意本身不足以消除间隙。单纯形还可启用 JS/Hellinger/KL 等分布相似度。

## 点评
论证干净：同容量 adapter、同注意机制只换输出域，把“几何先验”从架构容量里剥出来。TV 分数与概率预算共享坐标是可解释的机制；脆弱点在于实验全在冻结骨干上微调小头，未见端到端或生成式任务，且 RelGap 虽校正尺度，单纯形稀疏区与球面对“好对齐”的语义是否等价仍依赖检索代理指标。
