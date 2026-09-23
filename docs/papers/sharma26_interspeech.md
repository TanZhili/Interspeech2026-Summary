# Robust Language Identification Using Semi-positive Contrastive Learning

- 论文编号：2502
- 报告人：Shubham Sharma
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sharma26_interspeech.pdf

## 问题
低资源口语语言识别易过拟合录音条件等域特征，跨语料泛化差；多模态方法常把同语样本一视同仁，未显式建模同语异域方差。

## 方法
提出 Semi-positive Contrastive Learning（SpCL）：双模态音频–文本编码器映射到共享 512 维空间。目标矩阵 \(T\)：同语同域为 1，同语异域为 \(\alpha\in(0,1)\)，异语为 0。总损失 \(\lambda L_{con}+(1-\lambda)L_{cls}\)（\(\lambda=0.3\)）。文本侧用静态模板或由音素序列构成的动态 caption；推理仅用音频编码器+分类器。音频编码器试 wav2vec2 音素变体与 Whisper，文本为 RoBERTa。

## 实验与结果
12 种印度语言，训练见域 Ekstep+DatasetM(rs)，未见域 yt 与 IndicVoice。SpCL whisp（dynamic）准确率：Seen 98.76%、yt 91.42%、IndicVoice 54.52%，优于 MFCC/音素 Conformer、UDA、Whisper 微调等基线。VoxLingua33 上 SpCL whisp dynamic 93.0%（MuSeLI 96.1%）。消融：\(\alpha=0.7\) 与动态 caption 对未见域帮助最大。

## 结论
半正对比与动态 caption 可在无显式域适应下提升跨域 SLID；Whisper 音频编码器最稳。未来拟在联合嵌入空间做推理。

## 点评
把“同语异域”单独加权，比二元对比更贴合域偏移几何。强在训练要文本、推理只要音频。脆弱点是 IndicVoice 全体仍偏低，且域标签需在训练期可知；\(\alpha\) 需调参。
