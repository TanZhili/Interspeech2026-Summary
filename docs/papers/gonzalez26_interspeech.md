# Absorbing Discrete Diffusion for Speech Enhancement

- 论文编号：659
- 报告人：Philippe Gonzalez
- 程序：Monday 28 September 2026 / Neural Speech Enhancement: Survey, Diffusion and Flow Matching
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalez26_interspeech.pdf

## 问题
连续域扩散语音增强计算重；神经音频编解码（NAC）离散码虽利于 Transformer 建模，但多数下游增强仍靠自回归下一码预测、推理慢。需要在 NAC 码空间做有理论依据的非自回归生成式增强。

## 方法
ADDSE：冻结自训 RVQ 编解码器（约 2 kbps、4 码本×1024、50 Hz）将干净/带噪波形编成码；用吸收态离散扩散（ADD）建模干净码在带噪码条件下的分布，训练目标为条件 denoising cross-entropy。架构 RQDiT：沿帧与码本深度各一条 DiT，复用 NAC codebook 向量作输入（mask 为 0），以 adaLN 条件化带噪码。推理从全 mask 按 τ-leap/Euler 等价转移采样，可复用未解吸收步的网络预测以降 NFE。

## 实验与结果
训练动态混合多语料干净语音与噪声（SNR −5–15 dB）；测试 Libri-TUT 与 Clarity-FSD50K（跨噪声/跨语音泛化）。对比 Conv-TasNet、BSRNN、SGMSE+、EDM-SE、NAC-SE、EDM-NAC-SE 等。NAC 系侵入式 PESQ/ESTOI/SDR 弱（相位未重建），但非侵入指标有竞争力：含 4M 的 ADDSE-XS 在两集 DNSMOS/NISQA 上可超 Conv-TasNet 与 SGMSE+；ADDSE-XL 在 Clarity-FSD50K 上 DNSMOS 最好。NISQA 约 8 步、其余非侵入约 16 步即平台；低 SNR 优势更明显；大 Nsteps 时平均 NFE 可显著低于步数。

## 结论
作者认为在 NAC 码上做 ADD + RQDiT 能以较少采样步达到有竞争力的感知类指标，尤其低 SNR；离散吸收过程还可因预测复用提高采样效率。未来拟扩展全频带并引入语义编码。

## 点评
把“码空间语言建模”从自回归换成有吸收扩散理论的并行采样，并用 RQDiT 显式利用 RVQ 层级，是相对 MaskGIT 式 SE 更干净的一条线。代价是强依赖编解码重建上限，侵入式波形指标天然吃亏；相对 BSRNN/EDM-SE 仍非全面领先，价值更在低 SNR 感知与少步推理的折中。
