# When Does Quality-Aware Multimodal Fusion Matter? A Leakage-Safe Diagnostic for Decision-Level Dependence

- 论文编号：2989
- 报告人：Jaden Moon
- 程序：Wednesday 30 September 2026 / Audio Language Models: Reasoning, Reliability, and Multimodal Understanding
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/moon26b_interspeech.pdf

## 问题
质量感知多模态融合常用各模态可靠性分数加权决策，但分数是否真正在推理时改变预测，还是只与性能相关，现有评测往往分不清。尤其在情感与压力识别中，模型可能因架构灵活性或缺失模式而提升，质量信号本身未必参与决策。

## 方法
将输入拆成证据 E、可用性掩码 M、质量信号 Q，训练后冻结专家与融合规则，仅在 fully observed 测试样本上打乱 Q 的实例对齐（Broken-Q），与匹配质量（Clean-Q）比较 Balanced Accuracy 的置换差距 Δ_perm。质量由信号派生指标（音频 SNR/削波、生理 dropout、视频曝光/模糊等）在 fold 上仅用训练集做分位缩放。融合包括质量加权 late fusion 与以 [M,Q] 为输入的线性 softmax MoE；单模态专家为 LR 与 HGB。主数据 StressID（语音/脸/生理），边界情形 CMU-MOSEI；并用与 corruption/正确性对齐的合成质量做阳性对照，同时报告 oracle 选最优专家的 headroom。

## 实验与结果
StressID 上专家有分歧与可竞争空间（median Δ≈0.20），但原生质量与正确性相关近零（ρ≈0）；Clean–Broken 差距近零（LR −0.002±0.06，HGB −0.011±0.06，MoE −0.003±0.02），尽管 oracle headroom 约 0.35–0.37。阳性对照则显著：corruption +0.071±0.03，correctness-aligned +0.346±0.06。CMU-MOSEI 上语言专家更强，原生质量置换差距 0.004±0.004（不显著），oracle headroom 0.216±0.006。

## 结论
质量感知融合只有在可靠性估计能指出当前样本该信任哪一路输入时才真正影响决策；原生“干净度”类质量往往不够。作者主张用对齐打破式诊断验证质量依赖，而非仅看架构是否“质量感知”。

## 点评
把“能否更好路由”“融合能否用路由信号”“原生质量是否提供该信号”拆开，用冻结后置换检验决策依赖，设计干净。强在阳性对照证明诊断有灵敏度；弱在仅决策级融合、fully observed 评估，且阳性对照主要在 StressID，对 early/mid-fusion 注意力类方法需另设可干预的可靠性通道。
