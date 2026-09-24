# Interpretable Frequency-Band Attention with Gated SSL Fusion for Audio Deepfake Detection

- 论文编号：2250
- 报告人：Abeer Alhammad
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/alhammad26_interspeech.pdf

## 问题
高准确 SSL/端到端反欺骗模型多把全频带信号当黑箱处理，难以说明伪迹落在哪些频带；已有子带方法多为后验融合或缺少能覆盖“无明显频域伪迹”攻击的互补全局表征。

## 方法
BandMIL 双分支：语音切为重叠 4 s 窗（2 s hop）。频带支路将 0–8 kHz STFT 分成 K=8 重叠子带，各渲染为 64×256 图，共享 ResNet-18 编码并拼接 24 维手工子带特征，经注意力池化得 h_band（α_k 可解释）。SSL 支路用 WavLM-Large（后 12 层微调）得 h_ssl。门控融合 h_fused = g⊙h_band+(1−g)⊙h_ssl。窗级分数经 MIL：训练用 Log-Sum-Exp，推理用 top-k（k=5）均值；目标为音频级与辅助窗级 focal loss。

## 实验与结果
ASVspoof 2019 LA：Full BandMIL EER 1.28%、min t-DCF 0.0331；SSL-only 1.73%/0.0458；Band-only 9.71%/0.1766。仍高于部分公开 SOTA（如 XLS-R-AASIST 0.22% EER），但提供频带可解释性。按攻击：Band-only 在 A07/A09/A14–A16 近零 EER，在 VC 类 A17/A18 失败（41.12%/22.89%），SSL 与门控可补；部分攻击（A10/A11/A15）融合反而不如单支路。注意力上 B8（最高频）常占主导，A09 等偏向中高频。

## 结论
频带注意力 + 门控 SSL 融合可在保持竞争力的同时给出频域决策依据；作者承认全局门控并非对所有攻击都最优，计划做攻击感知门控并扩展到更新基准。

## 点评
把可解释子带分析接到现代 SSL，并用门控承认“有的攻击根本不在频带上”，设计动机清楚。主表相对顶尖 SSL 系统仍有差距，价值更多在审计/定位而非刷榜；融合在部分攻击上双输，说明单一全局门控仍脆弱。
