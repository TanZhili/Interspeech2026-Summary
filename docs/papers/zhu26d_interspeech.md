# DASM: Detecting AI-Synthetic Music via Authentic Manifold Deviation Modeling

- 论文编号：3245
- 报告人：Xinya Zhu
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhu26d_interspeech.pdf

## 问题
音乐 deepfake 检测多拟合已知伪造分布；生成器迭代导致非平稳漂移，判别边界易失效。

## 方法
提出 DASM：仅在真实样本上用重建损失训练可学习 memory bank，压缩真实音频流形先验；双分支分类器同时用原特征与 memory 重建特征，以相对真实流形的偏差识别伪造。对冻结 MERT 编码器做轻量 prompt tuning。在 SONICS 及声学降质条件下评测。

## 实验与结果
SONICS 上 EER 0.13%、Acc 99.89%、AUC 99.98%，优于 SpecGraph、WPT-XLSR-AASIST 等基线；在多种声学退化下保持稳健。

## 结论
锚定真实流形、不以伪造分布为跟踪目标，对 AI 合成音乐检测更稳，也可量化 AI 参与程度。

## 点评
把“追假”改成“离真多远”，理论上更抗未见生成器。主结果集中在 SONICS；跨生成平台与 AI 辅助混音的细粒度外推仍需更多证据。
