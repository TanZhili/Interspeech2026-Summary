# Parameter-Efficient Continual Learning for Automatic Speech Recognition

- 论文编号：3169
- 报告人：Steven Vander Eeckt
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/eeckt26_interspeech.pdf

## 问题
语音基础模型下游适应面临参数量大与顺序微调灾难性遗忘；ASR 上参数高效持续学习（PECL）研究相对 NLP/视觉更少，且不少方法未显式保护相对初始预训练模型的性能。

## 方法
提出 Continual SSVD（CSSVD）：对线性层权重做 SVD，按奇异值分为 head（高能）与 tail（低能）；只在 tail 学习近似旋转 G=I−2K（省略显式 rescaling）。新任务前重算 SVD 以更新 head/tail 划分；多任务时用权重平均（α=1/(i+1)）合并当前解与新任务适应解，保护主导方向并降低共享 tail 内干扰。推理无需任务 ID。

## 实验与结果
OWSM v3.2 small（约 366.7M），约 8.9M 可训参数。实验 1：预训练语 ENG/DEU/ESP 为 T0，再适应 CGN 的 NL→VL；CSSVD 平均 WER 18.33、BWT −1.9，显著优于 LoRA、SSVD、OPLoRA、MiLoRA、BiLoRA、EWC-LoRA、LoRA+FTA 等。实验 2：VL→方言 DVL，CSSVD 平均 24.82、BWT −2.2，仍最佳。消融表明限制在 bottom-k 方向最关键，平均步骤必要，显式 rescaling 几乎无增益。

## 结论
在尾空间做近似旋转并跨任务平均，可在 ASR PECL 上同时降低遗忘与平均 WER。局限是各层均匀分配适应容量，未来可按层选择性分配。

## 点评
相对“改 top-k”（SSVD）改为“只动低能尾并平均”，直接对准保护预训练主方向；实验覆盖多类从 NLP/视觉迁来的 PECL 基线，证据较全。脆弱处在于困难方言任务上新任务 WER 仍高于无正则 LoRA，且 head/tail 重划分依赖每任务后完整 SVD。
