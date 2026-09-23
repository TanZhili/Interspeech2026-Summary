# EII-SCL: Harnessing Emotional Inertia for Multimodal Emotion Recognition in Conversation

- 论文编号：3532
- 报告人：Zilong Huang
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/huang26p_interspeech.pdf

## 问题
对话多模态情绪识别（MERC）多建模上下文依赖，却常忽略同一说话人情绪的“惯性”——情绪倾向平滑过渡而非剧烈跳变；忽略惯性会使情绪切换处的负样本构造不当，限制特征判别。

## 方法
提出可插拔的 Emotional Inertia-Informed Supervised Contrastive Learning（EII-SCL）。骨干先用模态编码器（RoBERTa/Wav2vec2/CLIP）+ Bi-GRU + Transformer 或 DialogueGCN 式融合得到话语嵌入，再加 CE。对比学习中：同说话人同情绪为正；同说话人异情绪且落在注意力估计的动态惯性窗口内为 hard-negative（动态权重 1−cos/2），窗外或异说话人为 easy-negative。总损失 L=L_CE+α L_eii。

## 实验与结果
IEMOCAP LOSO、MELD 官方划分。MM-TransFormer+EII-SCL：IEMOCAP Acc/w-F1 73.95/74.01，MELD 68.19/67.33；MM-DialogGCN+EII-SCL：IEMOCAP 73.13/73.15，MELD 67.83/66.97，整体超 FEMI、AdaIGN 等。硬负样本平均余弦相似显著高于易负样本（ω=1 时差约 0.3645）；动态窗口优于固定窗口；模糊情绪对误分下降。

## 结论
无需额外标注即可把情绪惯性写入对比目标，提升通用 MERC 骨干表现。边界是依赖说话人标签与局部窗口假设。

## 点评
把心理学“情绪惯性”落成 hard-negative 采样与动态排斥权重，比单纯情绪切换检测更贴近同说话人连续表达。强处是即插即用；脆弱处是窗口依赖注意力估计质量，且离散标签仍强制切分渐变情绪。
