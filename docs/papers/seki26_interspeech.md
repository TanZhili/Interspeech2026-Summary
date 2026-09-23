# Improving DF-Conformer using Hydra for high-fidelity generative speech enhancement on discrete codec token

- 论文编号：1833
- 报告人：Shogo Seki
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/seki26_interspeech.pdf

## 问题
Genhancer 用 DF-Conformer（FAVOR+ 线性注意力 + 膨胀卷积）在离散 DAC token 上做高保真生成式增强，但 FAVOR+ 近似 softmax 会损伤 focus、特征多样性、单射性与浅层局部建模，限制性能；需要在保持线性复杂度下加强全局序列建模。

## 方法
分析 Genhancer 中 FAVOR+：注意力图模糊、秩远低于 softmax、不同 query 的注意力向量近乎相同。提出 DC-Hydra：在 macaron 式块中用 Hydra（Mamba-2 双向、准可分矩阵 mixer）替换 FAVOR+，保留膨胀深度卷积做局部建模。仍服务 Genhancer：潜在去噪器与 token 生成器估计干净 DAC token，WavLM-large 加权中间层作 SSL 条件，DAC 解码波形。对比 Softmax、FAVOR+、加法 Bi-Mamba 与 Hydra 变体。

## 实验与结果
训练用 LibriTTS-R（升采样至 44.1 kHz）+ 多种噪声/IR，on-the-fly 混响与噪声（SNR [-10,20] dB）等失真；测 DAPS 真实场景录音。Hydra（约 106M）在 NISQA 4.81、SpeechBERTScore 0.89、CAcc 88.95% 等上优于 FAVOR+/Bi-Mamba，部分指标接近甚至超过 Softmax（CAcc 优于 Softmax 的 87.88%）。长序列（96 s）上 Softmax 明显掉点，Hydra 相对稳健；生成式方法 CAcc 均低于 noisy，因幻觉（如多余气息）影响下游。

## 结论
用 Hydra 替代 FAVOR+ 可缓解线性注意力近似缺陷，在保持线性复杂度下提升 Genhancer 的增强质量与下游指标。

## 点评
工作把“线性注意力近似损失”落到注意力秩与 query 混淆的可视化证据上，再用结构化 SSM 替换，属于对症改骨干。强在复杂度与效果兼顾、长输入更稳；弱在仍受生成式幻觉拖累 CAcc，且评测集单一（DAPS），对更广失真分布的泛化需另证。
