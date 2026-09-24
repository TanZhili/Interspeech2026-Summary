# The Hidden Cost of Pairwise Verification in Synthetic Speech Source Tracing

- 论文编号：120
- 报告人：Anton Firc
- 程序：Thursday 1 October 2026 / Audio Watermarking and Source Verification
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/firc26_interspeech.pdf

## 问题
开集合成语音源追踪常被当作验证问题，因而借鉴生物识别中的成对度量学习。但合成器间差异细微，局部 pairwise 目标是否优于全局锚定、以及性能差距是否只由嵌入维度造成，尚不清楚。

## 方法
在匹配骨干、数据与 epoch 预算下，对比全局锚定（闭集 Softmax CE，推理用 penultimate 嵌入余弦相似度）与多种 pairwise 验证目标（随机、难负挖掘、方向性覆盖、rival mining；可选 XLS-R 微调）。骨干默认冻结 XLS-R 300M，池化用 MHFA（与 AASIST 对比后选定），pairwise 头为 FFCosine。域内用 MLAAD、域外用 STOPA，claim-based 评估（R=1，MLAAD 另报 R=5）。用 k99（解释 99% 方差所需主成分数）分析嵌入衰减，并对全局基线施加 10/13 维瓶颈消融。

## 实验与结果
全局 CE 在 MLAAD 上 EER 8.61%，优于 pairwise（约 12–15%）；rival + XLS-R 微调最好 pairwise 仍为 12.39%。R=5 时全局微调可达 5.50% EER。STOPA 上各法均大幅退化（最佳约 27.74% EER），严格低 FPR 下 TPR 仅约 1%。全局 k99≈121，pairwise≈13；全局 10 维瓶颈仍具竞争力（EER 7.05%）。细粒度错误显示 pairwise 在架构相近变体（如 Bark 系列）上混淆显著增多。

## 结论
在所测设置下，全局锚定仍是开集源追踪的强基线；pairwise 的差距不能仅用维度解释，而与目标塑造的嵌入方向及更重尾的分数分布有关。建议优先用全局锚定，仅在能证明低 FPR 收益时再考虑 pairwise。局限：结论依赖所测 pairwise 与 XLS-R/池化头；STOPA 排序仅作参考。

## 点评
论文把“生物识别里有效的 pairwise”搬到源追踪并系统证伪，诊断链（k99、分数 CDF、假接受分解、二元探针）比单纯刷 EER 更有说服力。强在指出目标塑造方向而非维度本身；脆弱处在于 OOD 上全体坍塌、且未覆盖监督对比/proxy 等更强度量损失，结论不宜过度外推到全部度量学习。
