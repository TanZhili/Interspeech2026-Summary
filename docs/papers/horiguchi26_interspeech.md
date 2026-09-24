# Tight Boundary Prediction in Speaker Diarization Using Causal-Anticausal Consistency

- 论文编号：45
- 报告人：Shota Horiguchi
- 程序：Thursday 1 October 2026 / Speaker Diarization and Recognition
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/horiguchi26_interspeech.pdf

## 问题
用多说话人 ASR 语料训 diarization 时，标注常把停顿与边界 padding 算进语音段，模型学会“松边界”；下游 GSS、对话数据构建等有时更需要紧边界，而强制对齐紧标注又依赖分轨录音、成本高。

## 方法
把紧标签视为真值、松标注视为弱监督。因果/反因果单向模型在松标签下仍难学前向 padding 或后向 pause-filling；对其后验取平均再阈值，与松标注做掩码得紧伪标签 Ytight = Ỹ ⊙ ϕτ((⃗P+⃖P)/2)。多说话人扩展：Basic（说话人对齐后逐说话人）、VAD（用 powerset 静音类抗说话人混淆）、SC（后验重分配纠正漏检/虚警）。过紧时若删超 50% 则恢复松段。并提出因果–反因果协同训练：逐步用输出收紧标签并更新参数；最终用紧伪标签训非因果 EEND（powerset，S≤4，至多两人重叠）。

## 实验与结果
摘要报告：相对理想紧标签训练，所提方法可恢复约 70% 的收紧效果，并改善下游表现。正文实验表与 DER 等具体数字在抽取全文中截断未完整出现。

## 结论
无需分轨强制对齐，仅用松 ASR 标注即可通过因果–反因果一致性构造更紧伪标签，使非因果 diarization 输出更紧并惠及下游。

## 点评
核心洞见是“松边界依赖未来/过去上下文”，用单向模型结构性禁止 padding/filling，再合成紧伪标签——比置信度去噪更贴问题本质。多说话人混淆时的 VAD/SC 变体说明简单平均不够。因全文抽取在方法中后段截断，实验数字仅能引用摘要中的约 70% 收紧恢复率。
