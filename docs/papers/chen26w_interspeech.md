# T-ORR: Text-Anchored Orthogonal Residual Rectification for Robust Multimodal Sarcasm Detection

- 论文编号：2222
- 报告人：Qi Chen
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/chen26w_interspeech.pdf

## 问题
多模态讽刺检测（MSD）依赖文本字面义与视听传递的冲突；常规将各模态投到共享空间做融合，容易纠缠瞬时冲突线索与无关噪声，削弱稀疏 incongruity 信号。

## 方法
T-ORR 以冻结 DeBERTa-v3-Large / WavLM / DINOv2-Large 提特征，文本为锚：（1）Dynamic Locality-Constrained Alignment：按文本预测动态时间中心与可学习高斯窗口，约束交叉注意力对齐音视频；（2）Structure-Preserving Geometric Decomposition：映射到文本流形后，用 QR 得文本子空间正交基，正交投影得 Resonance，残差为 Dissonance，并对 resonance 加 Decoupled Topology Constraint；（3）Contrastive Incongruity Routing：构造 Literal 态（文本+resonance）与 Incongruous 态（门控文本×dissonance），拼接二者及绝对差后 MLP 分类，并对真诚样本加门控稀疏约束。总损失为任务 CE + λ1 Lstruct + λ2 Lgatesparsity。

## 实验与结果
在 MUStARD / MUStARD++ 上按 speaker-independent 协议评测。T-ORR F1 达 76.8%（MUStARD）与 72.4%（MUStARD++），高于 DIP（74.3 / 69.1）及同骨干 Simple-Concat（70.8 / 66.1）。消融：去掉动态对齐 74.2、去掉 CIR 改拼接 73.5、去掉拓扑约束 74.9、去掉门控稀疏 75.3。定性上，真诚样本门控激活约 0.05，讽刺目标词可升至约 0.88；失败多见于依赖外部常识、视听无明显冲突的讽刺。

## 结论
将 MSD 重述为文本锚定的信号分离与冲突路由，几何解耦能更干净地隔离模态 incongruity，在 MUStARD 系列上取得正文报告的最优结果。

## 点评
相对“堆注意力融合”，正交残差把“该听字面”与“该抓冲突”拆成可解释子空间，CIR 与稀疏门控也对准了讽刺决策的直觉。收益主要来自融合几何而非更强骨干，消融支持这一点；但对纯常识/语境讽刺几乎无观测量冲突时会失效，说明方法强在可观测跨模态矛盾，而非一般语用推理。
