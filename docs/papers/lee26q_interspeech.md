# PhonePrune: One-shot Phoneme-Aware Pruning for Large-scale ASR Models via Phoneme Set Generation and Calibration

- 论文编号：1787
- 报告人：Minsik Lee
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26q_interspeech.pdf

## 问题

大规模 ASR 一次性剪枝常按幅度丢弃小权重，但部分小权重对细粒度音素辨别关键（Phoneme Ticket Hypothesis）；剪掉后擦音/塞音等区域识别崩溃。

## 方法

PhonePrune：按音系约束生成对比三元组校准集（互补分布、最小对等）；用掩码梯度得音素相关性分数；复合得分 S=|W|+λ|W|·S̃_ling 调制剪枝阈值，保护音素票。在 Whisper-large 50% 稀疏度一次性剪枝，校准 128 三元组。

## 实验与结果

相对幅度/OBS 等非结构化剪枝大幅更好。对 Distil-Whisper：韩/日 Common Voice 相对 WER 降 13.41%/13.83%（15.50/16.20 vs 17.90/18.80）；英语略逊于蒸馏模型，平均 WER 11.50。作者归因韩语细谱对比与日语时长对立更依赖脆弱音素票。校准样本数与 λ 消融显示 N=128、γ=0.5 较稳。

## 结论

作者认为压缩需显式保护编码精细音素的低幅度子网；音素感知校准可在高稀疏下更好保持识别，尤其对音系细节重的语言。

## 点评

把剪枝从纯幅度启发式拉回音系先验，解释了为何韩/日增益更大。一次性、无重训利于部署。校准依赖对齐音素片段与手工三元组，扩展到更多语言需重复工程；英语冗余线索多时收益较小符合叙事。
