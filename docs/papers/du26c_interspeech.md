# Orthogonal Feature Projection and Manifold-Constrained Neural PLDA for the TidyVoice2026 Cross-Lingual Speaker Verification Challenge

- 论文编号：3003
- 报告人：Yuxuan Du
- 程序：Thursday 1 October 2026 / TidyVoice2026 Challenge: Cross-Lingual Speaker Verification
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/du26c_interspeech.pdf

## 问题
跨语种说话人确认中，主流 ASV 训练常忽视语言不平衡，使模型把语言线索与说话人身份纠缠，严重限制跨语种泛化。现有后端把 Neural PLDA 的 P、Q 矩阵当作互不相关的可学习权重，切断了生成式概率约束；而侧重信道补偿的 PLDA-diag 对跨语种仍不足。TidyVoice 2026 正是针对语言无关 ASV 提出的评测。

## 方法
前端以 ResNet221（瓶颈块分布 [6,16,48,3]）+ MQMHA 池化为主干，AAM-Softmax 配合 sub-center 与 Inter-topK。正交特征投影：冻结 ResNet 与 WavLM Base+，将 WavLM 嵌入线性对齐后，用 Gram-Schmidt 分解为与 ResNet 嵌入平行的冗余分量与严格正交的互补分量；正交分量经零初始化门控的瓶颈网络 Φ（tanh）残差加回 ResNet 嵌入，逐步融入跨语种互补信息。后端提出流形约束 Neural PLDA：不直接学 P、Q，而学 Θ={μ,A,ψ}，由特征值向量 ψ 按对角化 PLDA 公式生成 P、Q，自由度从 O(d²) 降到 O(d)，以 BCE 端到端优化并保持 LLR 可解释性。训练用动态难例挖掘：挑当前分最低的同说话人跨语种对、分最高的异说话人同语种对。再加 AS-Norm（top-200 imposter）与开发集上逻辑回归分数融合。

## 实验与结果
训练分 Base（约 20 万说话人，VoxCeleb/VoxBlink/CN-Celeb 等）、Extended（扩至 60 万）、Multilingual（官方 TidyVoice + 自采 2000 人及方言筛出的约 1 万多语种说话人）。发展阶段：官方基线 Dev EER 3.07%；S1 预训练 ResNet 1.29%；加正交投影 1.07%；加流形 PLDA 0.79%；加难例挖掘 0.72%；加 AS-Norm 0.64（Test1/2：1.55%/2.22%）；最终融合 Dev 0.56%、Test1 1.39%、Test2 1.95%。按语种条件拆分时，跨语种目标/同语种非目标 EER（1.40%/1.87%）反而低于纯同语种条件（1.49%/2.45%），说明语言线索被压制。在 42 支队伍中获第 1。

## 结论
作者认为正交投影可抽取与声学监督特征互补、跨语种更稳的身份线索，流形约束 Neural PLDA 在判别优化时仍守住生成式约束，再配合多语难例挖掘可显著抑制语言干扰；最终两测试集 EER 1.39%/1.95% 夺冠。

## 点评
做法同时打前端“语言纠缠进嵌入”和后端“Neural PLDA 偏离生成流形”两端：几何正交分解比简单 concat 更可控，ψ 驱动的 P/Q 比无约束矩阵更不易过拟合。脆弱点在于依赖大规模私有/扩展数据与多阶段 curriculum，以及难例挖掘对语言标签质量的依赖；正交门控若校准不当也可能把有用声学互补当噪声滤掉。
