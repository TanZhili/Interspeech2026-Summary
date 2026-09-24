# Clinically-Supervised Hierarchical LoRA-MoE: A Parameter-Efficient Framework for Severity-Aware Dysarthric Speech Assessment

- 论文编号：3043
- 报告人：Jiaqi Wang
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26ga_interspeech.pdf

## 问题
构音障碍数据少、严重度声学异质大；全量微调 SSL 易过拟合，标准 LoRA 对所有输入共享低秩适配，难刻画不同严重度模式。

## 方法
冻结 WavLM-Large Transformer，仅训 CNN 前端与 LoRA。下层 N 层共享 LoRA；上层用多专家 LoRA，由临床严重度监督的 utterance 级 router（时序注意力池化）选专家。损失：加权 CE + \(\lambda_1\mathcal{L}_{router}+\lambda_2\mathcal{L}_{bal}\)。默认 N=9，r=16，5 专家。训练用噪声/变速/音高扰动与随机时段静音掩码。

## 实验与结果
UA-Speech，OSPS 说话人独立五折；2 类（健康/障碍）与 5 类（健康+四档可懂度）。WavLM LoRA-MoE：5 类 Acc 64.32%、macro-F1 61.55%；2 类 F1 94.54%、AUC 96.59%，优于全量微调与标准 LoRA。N 消融呈倒 U，N=9/12 最优。

## 结论
分层共享 + 严重度条件专家路由以极少可训参数超越全量微调；未来拟做连续严重度与多模态。

## 点评
把临床严重度先验写进 router，比均匀 LoRA 更贴异质性。训练时 router 用真标签、推理不用，需依赖表示是否学到可分线索；UA-Speech 说话人少、低/中档仅各 3 人，方差仍大。
