# LOPA: Enhancing Spoken Language Assessment via Latent Ordinal Prototype Alignment

- 论文编号：1346
- 报告人：Hong-Yun Lin
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26e_interspeech.pdf

## 问题
MLLM 做口语评估（SLA）成本高，且常把能力当普通回归/生成，忽略语言习得的序结构。轻量 Whisper 方案又多只用最后一层或转写特征，丢掉中间层声学/音系线索，潜空间相邻 CEFR 级重叠严重。

## 方法
冻结 Whisper Large-v3 编码器全部 32 层。Semantic-Anchored Layer Routing（SALR）对层做偏置初始化（末层锚点）的可学习加权融合；注意力时间池化后经 MLP 得到潜向量，再对有序分数期望回归。Latent Ordinal Prototype Alignment（LOPA）用可学习 CEFR 原型：吸引损失拉近同类，序约束使原型间距与分数差成比例。按 S&I 2025 的 P1/P3/P4/P5 分部分别训练。

## 实验与结果
S&I Eval：RMSE 0.361、PCC 0.828，\(\%\le0.5\) 83.3，与 Phi-4-MTL-APP（0.360/0.827）接近，优于 Whisper last-layer APP（0.383）与多种轻量基线。消融：去 LOPA→0.383、去 SALR→0.3739；配对 t 检验显示 LOPA 显著降误差。潜空间 ordinality 0.878→0.974，Silhouette −0.110→0.032。SALR 辅层偏好随部分变化（P1 偏浅层、P5 偏高层）。

## 结论
在不微调骨干、不用 LLM 的前提下，多深度路由 + 序原型正则即可达到接近大 MLLM 的 SLA 精度，并提供可解释的层偏好。

## 点评
用几何先验把“能力是有序的”写进潜空间，比单纯放大模型更贴 SLA 构念。SALR 末层仍占主导权重大，辅层增益虽在但权重很小；方法强在效率与可解释，对非 CEFR 半档量表的外推需另验。
