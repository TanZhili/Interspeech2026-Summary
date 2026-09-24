# PathBench: Speech Intelligibility Benchmark for Automatic Pathological Speech Assessment

- 论文编号：946
- 报告人：Bence Mark Halpern
- 程序：Thursday 1 October 2026 / Pathological Speech Assessment 4
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/halpern26_interspeech.pdf

## 问题
病理语音可懂度自动评估研究碎片化：私有数据、协议不一、目标指标混杂（可懂度/严重度/构音精度），且方法对参考文本/参考音频的依赖不同，难以公平比较。

## 方法
提出 PathBench：在公开数据上统一 Matched Content（MC，全体说话人相同文本）、Extended（EX，同说话人池用尽可用句）与 Full 协议，说话人级 Pearson 相关评估。方法分无参考、参考文本、参考音频三类，且不依赖带可懂度标签的训练。提出 DArtP：语义 ASR（wav2vec2-large-xlsr-53+LM）生成假设文本，再经 G2P 与语音学 ASR 强制对齐，以活动帧音素后验均值作为构音精度代理。基线含语速、CPP、σFo、VSA、ASR 置信度、ASRIC、PER、ArtP、P-ESTOI、NAD 等。数据覆盖 UASpeech、NeuroVoz、EasyCall、COPAS、TORGO、YouTube 等，英/西/意/荷。

## 实验与结果
说话人级平均相关：ArtP 与 NAD 并列最高（r=0.71）；无参考中 DArtP 最佳（r=0.66）。年龄与 WADA SNR 在多数集与主观分相关弱（|r|<0.4 / <0.3），个别集例外。Wilcoxon 显示 EX 显著优于 MC（N=96，p<0.0001），主要来自模型/文本/音频参考类；信号类无显著差。词 vs 句：整体句更好，主因参考音频方法对边界对齐更敏感。语言覆盖与对照说话人数量仍是限制。

## 结论
PathBench 提供可复现的多数据集、多协议基线；无标签训练下 DArtP 在无参考方法中平均相关最高；参考类方法宜多用数据（EX），信号类则 MC/EX 差异不大。

## 点评
把“临床控制刺激”与“ML 用尽数据”写成并列协议，直接回答可复现比较的痛点。DArtP 的可解释性来自音素对齐路径，但依赖多语 ASR/LM 适配；全文结论段在抽取中略有截断，主要数字与 RQ 结论已完整可读。
