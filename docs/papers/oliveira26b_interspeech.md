# Too Good to Be True: A Study on Modern Automatic Speech Recognition Systems for the Evaluation of Speech Enhancement

- 论文编号：2597
- 报告人：Danilo Oliveira
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/oliveira26b_interspeech.pdf

## 问题

用 ASR 的 WER 评语音增强很常见，但结果强烈依赖 ASR 选型与文本归一化；现代大模型对噪声鲁棒、会用语境，其分数是否反映“声学上增强得好”并不清楚。

## 方法

比较 QuartzNet、wav2vec2、Parakeet TDT、多种 Whisper（均贪心解码、无外置 LM）在噪声与多种 SE（SE-Mamba、NCSN++M、StoRM、SB-SGMSE+、SGMSE+）上的词正确率；并与人类听写、LPS、ESTOI、POLQA、SCOREQ 对照。听测：20 人，EARS-WHAM 子集 SNR∈[-2.5,10] dB。用裁剪后的 W Acc=max(1−WER,0) 抑制 Whisper 幻觉极端值。另测标点保留、用干净音频 ASR 作参考等管线扰动对 SE 排序的影响。

## 实验与结果

大规模噪声训练的 Parakeet/Whisper 与人类趋势相关最高（系统级 PCC 可达约 0.93–0.99），但绝对分常高于人类；且噪声子集可懂度常优于任一增强子集（与 observation adding 文献一致）。预测式 NCSN++M 词识别最好，生成式 SGMSE+ 无参考质量高，ASR 排序与 ESTOI/POLQA 不一致。Whisper 低 SNR 插入/循环幻觉严重。标点与参考文本选择可使 CTC 模型排序在约 16–19% bootstrap 样本中变化。

## 结论

作者认为与人类趋势更一致的现代 ASR，未必适合纯声学向的 SE 评测；必须透明报告模型与文本管线，并处理幻觉离群。WER 不能当作单一“真理”指标。

## 点评

核心警告精确：ASR 越强，越可能“听懂噪声、听不懂伪影”，从而低估需要的增强或误排系统。裁剪 W Acc、分解替换/删除/插入，对复现实验很有价值。听测系统数有限，系统级相关置信区间宽；结论应理解为方法学提醒，而非否定一切 ASR 代理。
