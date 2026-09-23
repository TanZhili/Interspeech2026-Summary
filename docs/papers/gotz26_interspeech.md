# Improving multichannel speech enhancement through accurate room-acoustic simulations

- 论文编号：2512
- 报告人：Georg Götz
- 程序：Wednesday 30 September 2026 / Challenges in Speech Data Collection, Curation, and Annotation
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gotz26_interspeech.pdf

## 问题
多通道语音增强训练常依赖简化几何声学（如镜像源 ISM）合成 RIR，难以刻画模态、衍射与刚性散射体；仿真保真度对真实阵列增强与下游 ASR 的影响尚缺系统比较。

## 方法
固定 SpatialNet-small（16 kHz，Eigenmike 六通道子集）与训练流程，比较三类增广：ISM-U（随机房间/T20）、ISM-M（匹配混合法房间尺寸与 T20）、Hybrid（Treble SDK 波场+几何混合，频率相关材料，含 Eigenmike DRTF）。在实测 Motus/Arni6DoF RIR 构造的 LibriCSS-EM6（约 5000 句、六种重叠条件）上评测增强后 Kaldi 转写的中位 WER。

## 实验与结果
Hybrid 在各重叠条件下均最优；相对 ISM-U 中位 WER 相对改善最高约 38.3%（OV40），总体约 30%；相对 ISM-M 总体约 16.3%。除 0L 对 ISM-M 的置信区间跨零外，其余配对改善均显著。未增强噪声混响 WER 约 73–88%。

## 结论
更高物理保真度的房间声学仿真可在不改网络与训练策略的情况下提升多通道增强与下游识别；仿真保真度本身构成可迁移的增益来源。

## 点评
把“增广保真度”从网络架构里拆出来，用实测阵列评测闭环，结论对数据中心路线很有说服力。强在 ISM-M 控制场景参数后仍见差距；弱在阵列与网络固定为 Eigenmike/SpatialNet，外推到商用小阵列需再验证。
