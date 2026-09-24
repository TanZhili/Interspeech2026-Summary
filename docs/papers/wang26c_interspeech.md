# Blind Room Impulse Response Identification via Reverberant Speech Spectrum Reconstruction

- 论文编号：217
- 报告人：Pengyu Wang
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26c_interspeech.pdf

## 问题
盲估计房间冲激响应（RIR）避免侵入式扫频测量，但时域长抽头难直接回归；现有方法或固定长度、或需迭代，长 RIR 仍困难。

## 方法
提出 Rec-RIR：在 CTF 近似下，多任务网络先去噪再去混响（交错 cross-band / narrow-band/Mamba 块），融合混响与干净语音嵌入，以窄带块与帧权重池化端到端估计 CTF；主损失为 ˆH⊛S 重建混响谱（Mag+RI），辅以去噪/去混响 Mag+RI 损失。再用伪侵入测量（对数扫频 + 逆滤波）将 CTF 转为最长约 0.96 s 的 RIR。

## 实验与结果
SimACE 上相对 FiNS、BUDDy、VINP：RIR-50 ms RMSE 0.040、¯ρ 0.805；RT60 MAE 0.069、ρ 0.994；DRR MAE 0.684、ρ 0.994；C50 亦最优。约 3.1M 参数、无需迭代。消融显示辅助损失尤其提升 DRR；极早期（<2 ms）不规则峰可能因直达对齐约束而不完整。

## 结论
作者认为将盲 RIR 转为有监督的混响谱重建可稳定估计长 CTF/RIR，并在声学参数与早期反射上达所报告的 SOTA。

## 点评
用 CTF + 谱重建绕开超长时域输出，并与去噪/去混响多任务耦合，结构合理。评测基于仿真+ACE 测得 RIR 的合成观测；直达对齐假设下极早期细节损失需在应用中留意。
