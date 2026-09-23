# Non-Autoregressive Minimum Bayes' Risk Decoding for Fast Speech Recognition

- 论文编号：2971
- 报告人：Hiroyuki Deguchi
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/deguchi26_interspeech.pdf

## 问题
NAR ASR（如 Mask-CTC）并行解码快，但因 token 独立性与多模态路径不确定性，相对 AR beam search 仍有 WER 差距。标准 MAP 选最高概率路径不一定质量最优；MBR 用期望效用选假设可更稳健，但在 AR 设定下采样与效用计算昂贵。

## 方法
提出 NAR-MBR：在 Mask-CTC 上做无偏采样 + 期望效用（负 WER）最大化，无需额外训练。
1. **采样**：按帧独立从 CTC 分类分布采样多条对齐路径 \(|Z|\)；再按置信度 Bernoulli 采样 mask，用 CMLM 从分类分布填 mask（可用 \(N_{\mathrm{iter}}\) 迭代；\(N_{\mathrm{iter}}=0\) 仅用 CTC）；假设集与伪参考共用同一采样集。
2. **EU 最大化**：选使相对伪参考平均 WER 最小的假设；用去最长公共前后缀、去重缓存、多核并行与 Rust 实现的编辑距离加速。
相对原 Mask-CTC 的确定性 mask + greedy，改为概率采样以服务 Monte Carlo MBR。

## 实验与结果
数据：LibriSpeech、Switchboard、AMI、Web（约 346h 训练）。AR 用 Conformer + CTC 联合解码；NAR/NAR-MBR 用 Mask-CTC（ESPNet）。
- WER：\(N_{\mathrm{iter}}\in\{1,10\}\)、\(|Z|\in\{64,256\}\) 时 NAR-MBR 相对 NAR 在多数集合显著更好（如 LS Clean \(N_{\mathrm{iter}}=1,|Z|=256\)：3.1 vs NAR 3.4；Web 7.3 接近 AR Beam 7.3）。峰值多在 \(N_{\mathrm{iter}}=1\)，增大迭代几乎不再降 WER。
- 速度（相对 AR Beam）：Web 上 \(|Z|=64,N_{\mathrm{iter}}=1\) 约 43.1×，\(|Z|=256\) 约 20.7×；仍快于 AR Greedy，但 \(N_{\mathrm{iter}}=1\) 时 GPU 显存升高（Web 上 \(|Z|=256\) 约 ×5.0）。
- \(|Z|\) 增大 WER 改善并在 ≥64 趋于饱和。

## 结论
利用 NAR 独立性可一次前向廉价采多样本，再用 MBR 缓解多模态不确定性，从而在无重训下优于原 NAR，并相对 AR beam 大幅加速；未来拟扩展到更多模型与任务。显存开销与采样规模是明确边界。

## 点评
把 MBR 的“用样本估期望质量”接到 NAR 的“一次前向可多样本”上，用决策准则补独立性假设的短板，比堆迭代 mask  refinement 更对症。强在训练零改动、\(N_{\mathrm{iter}}=1\) 即可；脆弱在二次效用与多样本带来的 CPU/显存成本，以及效用仍绑定 WER——对其他评价指标需重定义 \(u(\cdot)\)。
