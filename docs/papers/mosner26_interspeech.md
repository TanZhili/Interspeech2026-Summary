# Effectiveness of Language Variability Compensation in Speaker Verification

- 论文编号：3367
- 报告人：Oldřich Plchot
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/mosner26_interspeech.pdf

## 问题
说话人确认研究长期受单语宽带宽数据主导，语言变异对试验分数的影响常被信道/源失配掩盖。TidyVoice 2026 把语言多样性推到前景：同一说话人多语、评测含 38 未见语种。需要系统比较在嵌入端、后端与分数端分别做语言补偿是否有效，以及它们如何交互。

## 方法
嵌入端：（1）在池化后分支加语言分类头与 GRL，多任务 L=L_s(ArcFace)+L_l，迫使共享骨干抑制语言信息；（2）DSU 在卷积特征上扰动通道均值/方差以模拟未见域偏移。后端：PSVM、球形高斯变体 SG-TPSDA，以及用 LDA 投掉主导语言方向（维数在开发集调）。分数端：ResNet18 语言分类器得语言相似度作质量度量，经逻辑回归校准说话人分数。前端含 w2v-BERT 2.0+层适配器+MFA，以及更大的 SimAM-ResNet100；微调数据试 TidyVoiceX、VoxCeleb2、NIST SRE CTS Superset（上采样至 16 kHz）等组合。

## 实验与结果
微调数据：SimAM-ResNet100 在 T+V+C 上 Dev EER 1.50% 最佳；w2v-BERT MFA 仅 T 即 1.50%，加英语主导的 V 反而变差。嵌入端：ResNet 上 GRL+DSU 达 Dev 1.20%；w2v-BERT+GRL 达 0.99%。子列表显示最难的跨语目标/同语非目标（tgt≠, imp=）在 GRL 后显著改善（如 MFA：2.83%→1.58%），最易同语目标/异语非目标则略变差，符合“语言线索被削弱”。后端：非语言补偿嵌入上 PSVM/SG-TPSDA+LDA 很强；但对已 GRL 的嵌入，后端补偿效果变弱，需大幅减小 LDA 维数。提交为 SimAM+PSVM-LN 与 w2v-BERT+SG-TPSDA 的先验加权逻辑回归融合：Dev 0.81%、eval-A 2.53%、eval-U 3.40%。分数端语言质量度量对无补偿系统有帮助（1.28%→1.10%），对已 GRL 系统几乎无增益。

## 结论
作者认为在语言多样场景下显式补偿语言变异至关重要；嵌入端 GRL/DSU、强后端与分数端质量度量可各自带来相近收益，但前端已去语言后，后端/分数端优势会减弱。提交系统 eval-A EER 2.53%。

## 点评
价值在于“整条流水线对照实验”而非单点技巧：证明语言纠缠可在前端净化，也可留给能拆说话人/非说话人子空间的后端消化；两者不可简单叠加。脆弱点在于子列表分析主要基于见语种开发集，未见语种行为未充分展开；MinDCF 在同语非目标子列表上逼近 1 也被作者怀疑部分标签问题，解读需谨慎。
