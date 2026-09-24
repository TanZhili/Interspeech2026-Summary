# GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-Fine Generative Language Model

- 论文编号：893
- 报告人：Haoyang Li
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26m_interspeech.pdf

## 问题
LM 生成式 TSE 若单阶段直接建模精细声学，熵高、难稳；训练教师强制与推理自回归存在暴露偏差；信号损失也不对齐感知偏好。

## 方法
GenTSE：两阶段纯 decoder-only LM——Stage-1 预测粗语义 token，Stage-2 条件生成细声学 token；两阶段均用连续 SSL/codec 嵌入作条件。Frozen-LM Conditioning（FLC）用早期检查点预测作条件以减暴露偏差；再用 DPO 对齐感知偏好。在 Libri2Mix clean 上评 DNSMOS/UTMOS/NISQA、SECS、dWER 等。

## 实验与结果
GenTSE 在多项感知与说话人一致性指标上超过先前 LM 式 TSE。消融显示 FLC 优于纯教师强制微调；DPO 相对 CE 进一步提升感知分。作者不报 PESQ/SI-SNR，因生成式与波形对齐目标不完全可比。

## 结论
粗到细全生成层次 + FLC + DPO，可提升生成式 TSE 的质量、可懂度与说话人一致性。

## 点评
把语义/声学拆开并正视暴露偏差，是对 AR TSE 的扎实工程。不报经典波形指标削弱与判别式对比；DPO 偏好对如何构造影响可复现性。
