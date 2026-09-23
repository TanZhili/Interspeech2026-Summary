# Overcoming Decoder Inconsistencies in Whisper for Dravidian and Low-Resource Languages

- 论文编号：1007
- 报告人：Kumud Tripathi
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kumar26c_interspeech.pdf

## 问题
Whisper 在达罗毗荼语上 WER 显著高于印度-雅利安语；语料分析显示更长词、更高 TTR、更低重复，错误多为已知词内字符替换，解码器自注意与交叉注意失衡。

## 方法
在 Whisper-medium 解码器每层加轻量 Weighted-Attention（门控调节自/交叉注意）；在倒数第二层做 Self-Conditioning，把中间预测投影回加到隐状态并辅 CE。形态切分仅作分析工具。Kathbath 八语评测，并外推到韩语、斯瓦希里语。

## 实验与结果
基线平均 WER 19.79，形态切分后 17.18。Weighted-Attention / Self-Conditioning / 组合在 MS 设定下平均再降约 1.5–1.65 点，马来雅拉姆等增益更大。韩语 3.34→2.51、斯瓦希里 16.07→14.58。参数增幅 <1%，推理延迟增 <2%。

## 结论
面向黏着语形态稀疏的解码器条件化可稳定降低字符级替换错误，并泛化到非印度黏着语。

## 点评
诊断（已知词内替换）与改动（平衡声学/语言注意、反馈中间预测）对症。形态切分提示问题本质，但主贡献是训练期解码器改造；增益幅度中等，强在轻量与跨语一致。
