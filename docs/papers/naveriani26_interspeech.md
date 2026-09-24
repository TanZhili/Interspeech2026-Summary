# Diffusion Language Models for Speech Recognition

- 论文编号：2070
- 报告人：Davyd Naveriani
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/naveriani26_interspeech.pdf

## 问题
自回归 LM 重打分/联合解码受限于从左到右顺序，速度受限。离散扩散 LM（MDLM、USDM）可双向建模与并行生成，但如何系统用于 ASR 重打分，以及如何与 CTC 做 token 级联合解码，此前缺乏系统研究。

## 方法
1. **重打分**：对 CTC n-best 用 \(\lambda_{\mathrm{CTC}}\log P_{\mathrm{CTC}}+\lambda_{\mathrm{DiffLM}}F_{\mathrm{DiffLM}}-\lambda_{\mathrm{prior}}\log P_{\mathrm{prior}}\)。对 MDLM 提出样本级/全局 mask 归一化及耦合互补 mask 打分，替代高方差的序列长度归一化；USDM 用其 ELBO。
2. **CTC–USDM 联合解码**：从 CTC greedy 序列与噪声水平 \(t_{\mathrm{start}}\) 起步；每步用 CTC 帧分布（按折叠后首帧对齐、去 blank）与 USDM 全词表标签分布线性组合后 ancestral sampling，迭代去噪。

## 实验与结果
LibriSpeech：CTC 在 960h 训练；DiffLM 在 LS LM 文本 + train-other 转写上训 5/10/25 epoch，DiT 约 110M/340M，SentencePiece 10k。
- MDLM 重打分（样本级归一化，K=256）：dev-other 最优约 4.47%（25 ep），优于序列归一化 4.62%（5 ep）与 CTC 基线 5.08%。
- USDM 重打分：K=256 时约 4.72%。
- CTC–USDM 联合：\(t_{\mathrm{start}}=0.1,L=1\) 达 4.66%；RTF 约 0.003，接近 CTC-only 0.002。
- 自回归 LM 仍更强（first-pass 3.86%，rescoring 4.19%），但扩散重打分 RTF 明显更高。

## 结论
MDLM/USDM 均可提升识别；mask 归一化对 MDLM 重打分很关键；USDM 的全词表分布使其能与 CTC 高效联合解码，单步即可明显降 WER。当前数据规模下自回归 LM 仍更准，作者认为更长训练与更大模型可能缩小差距。

## 点评
贡献重点是“把扩散 LM 接到 ASR 管线”的可操作配方：打分归一化与 CTC–USDM 联合。联合解码用极少额外步数换可观增益，工程吸引力大；但与强自回归 LM 仍有差距，且 MDLM 尚未纳入联合框架，扩展价值取决于能否在保持 RTF 的同时缩小精度鸿沟。
