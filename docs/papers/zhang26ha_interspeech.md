# Margin-Aware Contrastive Regularization for Robust Streaming Keyword Spotting under Strict False-Alarm Constraints

- 论文编号：3545
- 报告人：Hanwen Zhang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26ha_interspeech.pdf

## 问题
边缘流式 keyword spotting（KWS）需在严格 false-alarm（FA）预算下保持检测灵敏度。标准 CE 训练的轻量因果模型在 ≤0.5 FA/h 等严苛工作点上，面对语音相似 imposters 时 false rejection rate（FRR）显著恶化；直接对 Unknown 做全局对比聚类会扭曲异质非目标流形。

## 方法
提出 Margin-Aware Contrastive Regularization（MACR），仅作离线辅助目标：对因果 1D-CNN 的 penultimate embedding 做 ℓ2 归一化；intra-class pull 仅作用于目标关键词，分母也只含其他目标样本，避免全局聚类 Unknown/Silence。Margin-aware repulsion 对负样本施加 max(0, cos−m)，并对离线挖掘的 hard negatives（EMA 网络上非目标窗口中目标后验 top-K）加权 α>1。总损失 L_CE+λ L_MACR；部署时丢弃 MACR 分支，参数、MACs、算法时延与 CE 基线相同。

## 实验与结果
在 Google Speech Commands V2（12 类）上，约 150K 参数因果 1D-CNN，连续流事件级协议（50 条 2 小时测试流）。MACR 闭集准确率 95.68%（CE 95.82%）；FRR 在 0.5 FA/h 从 16.32%→7.64%，在 0.2 FA/h 从 29.85%→14.80%（相对降幅约 50%）。消融表明去掉 margin、hard-negative 加权或对 Unknown 全局聚类均使 FRR 变差。DS-CNN Tiny 与 BC-ResNet-1 上也有一致 FRR 下降；Raspberry Pi 4B 上推理时延与 CE 同为约 2.15 ms。

## 结论
MACR 通过目标紧致与 hard-imposter 几何边距改善严苛 FA 下的流式 FRR，且零部署开销。证据限于英文多关键词严格 FA 流式设定；更广语言、自定义唤醒词与远场场景留待后续。

## 点评
核心洞察是 Unknown 不是紧致类，对比学习必须把“目标紧致”与“imposter 边距”拆开；这比直接套 SupCon/ArcFace 更贴 always-on FA 约束。脆弱点在于 hard-negative 挖掘依赖 EMA 与合成流协议，真实自然录音与自定义唤醒词上的边距是否仍有效有待验证。
