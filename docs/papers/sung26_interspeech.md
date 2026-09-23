# fMRI Decoding of Speech Conditions Across Brain Regions of Interest for Neural Evaluation of Speech Enhancement

- 论文编号：1947
- 报告人：Ching-Chih Sung
- 程序：Monday 28 September 2026 / Brain Studies and Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sung26_interspeech.pdf

## 问题
噪声下 Clean vs Noisy 的 fMRI 多体素模式高维且跨被试变异大；深度解码是否优于 SVM，以及如何把解码输出变成可比较增强系统的神经指标，尚不清楚。

## 方法
NeuroPAS-Net 三阶段：掩码重构 SSL → 重放增量学习 → 目标被试监督微调，同一 CNN 编码器迁移。25 名听力正常普通话听者听 Clean、Noisy（SSN −3 dB）、DNN-SE（SEMamba）、Classic-SE（MMSE）四条件句子，12 个言语相关 ROI（AAL）。在 R PreCG Clean–Noisy 解码器上取 sigmoid 输出作 NeuroPAS，增强试次仅推理。

## 实验与结果
各 ROI 均高于 50% 机会；NeuroPAS-Net 全面优于 SVM/CNN，R PreCG 峰值 79.3%。消融显示 P1+P2+P3 单调提升（R PreCG 77.46→79.30）。归一化 NeuroPAS：DNN-SE 0.60 > Classic-SE 0.41。与主观可懂度 Spearman ρ=0.43（校正后 p≈0.17）。

## 结论
框架可稳健解码声学清晰度，并给出与主观相关的连续神经增强分数；DNN-SE 比经典增强更接近 Clean 神经模式。未来拟扩展到听力损失与 EEG/MEG。

## 点评
把 SE 评测从听感分数接到“是否更像 Clean 的多体素模式”，思路直接；三阶段迁移针对跨被试难题。NeuroPAS–可懂度相关未达严格显著、ROI 解码不等于因果，且仅正常听力，神经指标宜作行为评测的补充而非替代。
