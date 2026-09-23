# TAD: Token-Adaptive Contrastive Decoding with Confidence-Guided Gating for Hallucination Mitigation in Large Audio-Language Models

- 论文编号：637
- 报告人：Heyu Chang
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/chang26_interspeech.pdf

## 问题
LALM 在音频物体幻觉上常对不存在的声音事件回答 “yes”，语言先验压过声学证据。既有 Audio-Aware Decoding（AAD）等对比解码用固定对比强度，未按证据强弱自适应，也未专门针对决定二分类结果的首个解码步。

## 方法
训练无关的 Token-Adaptive Decoding（TAD）：对真实音频与等长全零静音参考分别取 logits，做 AAD 式组合 \(\tilde{\ell}=(1+\alpha)\ell^{audio}-\alpha\ell^{silent}\)。构造 YES/NO 多表面形式 token 集合，用 log-sum-exp 池化得音频/静音下的 yes–no margin，定义 \(\delta=m_{audio}-m_{silent}\)。仅在 t=1 且 \(\delta<\tau\) 时对 YES token 施加惩罚 \(-\gamma\)，后续步只用 AAD logits。默认 \(\tau=0.2\)、\(\gamma=2.5\)。

## 实验与结果
在 AudioCaps-Hallucination（Random/Adversarial/Popular）与 Clotho-AQA 二分类子集上评 Qwen2-Audio-7B-Instruct 与 Gemma-3n-E4B-it（NO 为正类）。相对 AAD，Qwen2 上 TAD 的 F1 提升约 0.059–0.117；Gemma 约 0.025–0.064。Clotho-AQA 上 Qwen2 F1 由 0.810 到 0.816，Gemma 与 AAD 接近。混淆矩阵与首步 ROC 显示 TAD 显著提高对真实 NO 的召回；\(\delta\) 分布上真实 YES/NO 大致分居正负，支持小阈值门控。

## 结论
首步、类条件、置信度门控的对比解码可在不训练的前提下抑制无依据肯定回答，并在幻觉基准上更稳健，同时大体保持 AQA 表现。

## 点评
把干预收窄到“首 token 的 yes 偏置”，比全程固定对比更贴合二分类 AQA 的决策结构，也解释了为何不易全面毁掉已有足够证据时的肯定回答。代价是依赖 YES/NO 词表覆盖与 \(\tau,\gamma\) 选择，对开放式长回答幻觉未必直接迁移；Gemma 上仍可见“更保守换召回”的精度/准确率折中。
