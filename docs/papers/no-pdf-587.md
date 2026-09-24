# Mitigating Pruning-Quantization Compound Errors for Ultra-Lightweight ResNet34-Based Speaker Recognition

- 论文编号：587
- 报告人：城轩 龙
- 程序：Thursday 1 October 2026 / Speaker Recognition and Verification
- 技术分类键：speaker
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
DNN 显著推进了说话人识别，但 ResNet34 一类骨干仍有计算与内存开销，难以部署到资源受限设备。剪枝与量化可压缩模型，但二者叠加会产生复合误差，需要专门缓解。

## 方法
提出统一压缩框架，结合通道剪枝与低比特量化。剪枝侧提出 ResRep-MB：带多分支 compactor 的策略，用于更准确的通道重要性评估，以实现近无损结构压缩。为缓解剪枝与 INT4 量化的复合误差，提出 Progressive Pruning-Quantization Distillation（PPQD），采用双教师机制。

## 实验与结果
在 VoxCeleb1 与 CN-Celeb1 上，压缩后的 ResNet34 达到 19.2× 压缩比，相对 EER 仅下降 6.8%，并保持跨语言稳健性（摘要表述）。

## 结论
通道剪枝与 INT4 量化可在统一框架下大幅压缩 ResNet34 说话人识别模型；PPQD 用于抑制二者复合误差，使高压缩比下性能损失相对可控。

## 点评
贡献点集中在「剪枝+量化复合误差」而非单一压缩手段；摘要给出了压缩比与相对 EER 变化，但仍缺完整设置与对比表，需谨慎解读。
