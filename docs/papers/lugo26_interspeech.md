# DiffVQE: Hybrid Diffusion Voice Quality Enhancement Under Acoustic Echo and Noise

- 论文编号：2337
- 报告人：Haljan Lugo
- 程序：Wednesday 30 September 2026 / Active Noise and Echo Control, Sound Zones and Packet-Loss Concealment
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/lugo26_interspeech.pdf

## 问题
免提场景需联合 AEC 与降噪；判别式 DeepVQE 强但生成式扩散 AEC 少见且先前工作难复现。作者要做可复现的混合扩散 VQE。

## 方法
DiffVQE：Cond DNN 用麦端与远端 STFT 判别估计 ˆScond 并提供条件 C；Score DNN 做方差爆炸 SDE 的去噪分数匹配，单步/少步 Langevin 采样生成近端语音。数据与合成管线基于公开框架，并加入 Interspeech 2025 URGENT 语音/噪声。仍允许非因果。对比同数据重训的 DeepVQE。

## 实验与结果
验证集：DiffVQE（5.13M，5.37G FLOPS，RTF 0.185）平均排名 1.3，多数 PESQ/LPS/ESTOI 与 ST 指标优于 DeepVQE（5.29M，42.24G，RTF 0.317）；DeepVQE 在 DT/ST Echo 上略领先且接近 clean。更小的 DiffVQE-S（3.43M，约 10% 算力）平均排名 2.0 仍优于 DeepVQE 的 2.5。AEC Challenge 测试集趋势一致（DiffVQE 平均排名 1.17）。

## 结论
可复现的混合扩散 AEC/NS 在多数质量指标与复杂度上超过 DeepVQE，但 Echo 指标仍略逊；单步变体利于部署研究。

## 点评
“可复现 + 公开数据”本身是对扩散 AEC 文献的贡献。混合 Cond/Score 把判别稳健与生成细节结合；非因果与 Echo 上的小劣势划清了与产品级低延迟 DeepVQE 的边界。
