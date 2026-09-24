# MVCL-DAF++: Enhancing Multimodal Intent Recognition via Prototype-Aware Contrastive Alignment and Coarse-to-Fine Dynamic Attention Fusion

- 论文编号：267
- 报告人：Haofeng Huang
- 程序：Wednesday 30 September 2026 / Spoken Language Understanding
- 技术分类键：slu
- 全文：https://www.isca-archive.org/interspeech_2026/huang26_interspeech.pdf

## 问题
多模态意图识别（文本+视觉+声学）在噪声与长尾/稀有类下语义锚定弱；MVCL-DAF 等对比对齐停在实例级，融合把模态当扁平 token，忽视层次结构与冗余。

## 方法
提出 **MVCL-DAF++**：保留原 CTC 对齐、BiPeephole LSTM 音频与 BERT 池化解码器，新增 (1) **原型感知对比**：批内按类均值得原型 \(r_c\)，做实例–原型 InfoNCE；(2) **粗到细 DAF**：模态感知 Transformer 以文本为 Q、视觉为 K、声学为 V 得粗粒度 \(M_c\)，再与 token 级特征经两路 DAF 得 \(M_f\)/\(M_{cf}\)。总损失 \(L_{\mathrm{cls}}+L_{\mathrm{proto}}+L_{\mathrm{contrastive}}\)。

## 实验与结果
MIntRec / MIntRec2.0（10 种子平均）：
- Acc 76.18% / 60.40%，WF1 75.66% / 59.23%，相对 MVCL-DAF 分别 +1.46/+2.60 Acc、+1.05/+4.18 WF1；摘要称稀有类 WF1 提升同量级。
- 消融：去掉原型或粗到细融合均下降；三损失齐用最佳。
- 注意分析：更噪的 MIntRec2.0 更依赖粗特征；t-SNE 显示类簇围绕原型更紧。

## 结论
原型锚定与粗–细融合提升跨模态一致性与长尾鲁棒性，在两基准刷新 SOTA。未来拟与 LLM 架构结合。

## 点评
相对纯实例对比，类原型提供更稳的语义锚，适合不平衡意图；粗特征在噪声集上权重升高也符合直觉。增益在 MIntRec2.0 更明显，说明方法主要吃“难分布”红利；与 LLM 时代端到端 LALM 路线相比，仍是经典编码器–融合分类框架。
