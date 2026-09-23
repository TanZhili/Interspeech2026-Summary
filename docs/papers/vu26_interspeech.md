# Adaptive Multimodal Expert Specialization by Meta-Learning for Spoken English Assessment

- 论文编号：1650
- 报告人：Cong-Thanh Vu
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/vu26_interspeech.pdf

## 问题
面试式口语英语评估依赖音视频多模态，但隐私与数据稀缺使深度模型难训；单模型多准则联合优化易冲突，且难以快速适配新说话人/任务。

## 方法
在 Vericant SEE（CEFR 对齐，五维约 20 子准则）上：视频切重叠片段构造元任务；提取 DisVoice 韵律、Qwen3-Embedding 文本、话轮/rubric 统计、OpenFace HAU。经投影与 Transformer 跨模态交互后，16-expert MoE（top-2 门控）+ 多头打分。用一阶 MAML 学可快速适配的初始化。分类用 BCE；回归用 soft-discretized（KL + load-balance + MSE + margin）。贝叶斯优化超参。

## 实验与结果
ETS Vericant（427 人，9–16 岁）：Prosody-Turn（M2）上 SEE 分类 F1 84.88%、回归 MSE 0.225，相对基线 [23] F1 81.78%、MSE 0.333（约降 32.4%）。消融：去 MAML、换 Dense、去 rubric 特征等均明显变差。MIT Interview 上 Turn+Prosody+HAU 达 F1 67.04，接近既有多模态工作。

## 结论
MoE 专长化 + 元学习可在极端小数据下提升多准则口语评分，并迁移到雇佣面试可雇佣性预测。局限是仍依赖预训练特征抽取。

## 点评
把“每个准则当可适配子任务”与 MoE 路由结合，直接回应数据稀缺与准则冲突。特征侧强依赖手工/预训练表征，细粒度声学差异可能被瓶颈；MIT 结果有波动，小样本重复实验的报告方式值得注意。
