# Weakly Masked Residual Reliability Learning for Unsupervised Domain Adaptation in Speech Models

- 论文编号：1767
- 报告人：Yuan Li
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/li26aa_interspeech.pdf

## 问题
无监督域适应中伪标签噪声大；仅靠置信度易受过置信误导，且丢弃不确定区域会造成边界监督不足。

## 方法
WMR²L：用最大置信度与非最大类残差离散度共同定义 token 权重（utterance 内标准化 + 高斯核），可靠 token 满权。弱置信掩码：对高权 token 以概率 r 将损失乘 λ 而非硬删，促从不可靠区恢复。多扰动一致性（时频掩码、随机裁剪缩放、均衡等）算 S=l·平均 WER，保留一致性最好的 τ 比例样本作伪标签。在 Whisper-medium 上微调。

## 实验与结果
相对 Whisper 基线相对 WER 降：CHiME-4 noisy 约 13.8%、SLURP 25.0%、CORAAL accented 15.7%；WMR²L+MP 全面优于 Confidence/Margin/Entropy+MP、STAR、Beam/Sample 等。CoVoST2 爱沙尼亚/印尼/威尔士翻译 BLEU 亦提升。Large-v3 上同样有效。消融：弱掩码优于强掩码/无掩码；m-r-eq 扰动组合最佳。

## 结论
置信度–残差可靠性加权 + 弱掩码 + 语音多扰动过滤，可提升跨域 ASR 与语音翻译的伪标签利用与泛化。

## 点评
针对过置信与选择性伪标偏差，用残差离散度与弱掩码补监督，思路细。滤波在伪标生成时只做一次，迭代自训动态未充分讨论；超参（α、r、λ、τ）与扰动组合对口音/噪声域可能需重调。
