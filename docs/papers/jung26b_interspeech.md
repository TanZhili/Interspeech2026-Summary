# Hierarchical Permutation Consistency Learning for Self-Conditioned End-to-End Speaker Diarization

- 论文编号：1198
- 报告人：Bongsu Jung
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/jung26b_interspeech.pdf

## 问题
Self-conditioned（SC）EEND 把中间层说话人预测反馈到后续层做逐步 refinement，但常规层间独立 PIT（LW-PIT）每层各自选最优置换，造成 Hierarchical Permutation Inconsistency（HPI）：相邻层说话人索引冲突，置换噪声沿 SC 路径传播，破坏训练稳定与渐进精炼。

## 方法
在 EEND-NA + SC 上提出两种 PIT。(1) GW-PIT：把 min 算子移到各层加权 BCE 之和外，令所有中间层共享同一全局置换，从构造上消除层间错配。(2) CI-PIT：用高斯核 w_{l,i}=exp(−(l−i)²/(2σ²)) 聚合各层 pairwise BCE 代价矩阵，再对聚合矩阵做 Hungarian 得 ϕ_l*，软约束邻近层置换连续，同时保留局部灵活性；σ→0 退化为 LW-PIT，σ→∞ 接近 GW-PIT。另定义 PMR、ASR、ESR 诊断层间/跨 epoch 置换一致性。

## 实验与结果
SimConv（LibriSpeech，按 CALLHOME 先验模拟重叠+MUSAN）预训练，CALLHOME 2/3 说话人适配与测试。8 层 Transformer、345 维输入、0.25 s collar、中值滤波 11、阈值 0.5。CALLHOME 2-spk：LW-PIT DER 8.30，GW-PIT 8.02，CI-PIT(σ=1) 7.52（FA 3.65→2.59）；3-spk：CI-PIT 12.52 优于 baseline 13.04，而 GW-PIT 变差至 13.66。训练动态显示 CI-PIT 下 ASR/PMR 收敛近零、ESR 层间协同；σ=1 优于 2/3。消融表明 CI-PIT 与 SC 组合增益最大（8.67→7.52），单加 SC 在 LW-PIT 上几乎无增益。

## 结论
独立层间 PIT 会在 SC-EEND 中引入 HPI；CI-PIT 通过高斯加权代价聚合抑制置换噪声又保留表征灵活度，在 CALLHOME 2/3 说话人上稳定降 DER，硬全局约束 GW-PIT 在说话人增多时易过约束。

## 点评
把 SC 路径上的置换错配形式化为 HPI，并用“硬共享 vs 软邻域聚合”两条线对照，诊断指标（ASR/PMR/ESR）把训练不稳说清楚了，比单纯报 DER 更有解释力。CI-PIT 实质是在一致性与层特异梯度间插值，和分离里的级联/层间协调思路同源。风险在于仅 CALLHOME 小规模评测、SimConv 无 RIR，以及 σ 需调；硬约束在更多说话人时失效，说明一致性目标不能压死中间层自由度。
