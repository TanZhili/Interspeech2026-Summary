# Layer-wise Multi-factor Adaptive Disentanglement for Cross-corpus Speech Depression Detection

- 论文编号：465
- 报告人：Minggang Wang
- 程序：Wednesday 30 September 2026 / Pathological Speech Assessment 3
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26j_interspeech.pdf

## 问题
说话人解耦有助语料内抑郁检测，但跨语料时说话人/语料等多源偏移在编码器各层累积；仅输出层或仅说话人约束不够，均匀解耦强度又易过/欠解耦。

## 方法
LMAD（无监督域适应）：在多个关键层用 HSIC/CKA 估计表示对说话人 \(u\)、语料 \(c\)、抑郁 \(y\) 的依赖；层间/层内依赖比例与主损失梯度方向一致性共同得到自适应权重 \(w^*_{l,v}\)。目标：源域 BCE + 加权抑制 \(u,c\) 依赖 − 加权保留 \(y\) 依赖。骨干 DepAudioNet 与 ECAPA-TDNN；输入 3.84 s 段的 40 维 Fbank。

## 实验与结果
双向 DAIC-WoZ↔Androids。带自适应的 LMADw_Eb：DAIC→Androids macro-F1 0.62（基线 Eb 0.39；MDFA 0.42），Androids→DAIC 0.56（基线 0.44）；语料内仍具竞争力（如 DAIC 0.70）。层间抑郁依赖比例与 UMAP 显示自适应版更把最终嵌入推向抑郁相关、减弱语料/说话人簇。

## 结论
多层多因子自适应解耦可稳定提升跨语料迁移并保持语料内表现；关键层需先验选定是局限，未来希望训练中自适应选层。

## 点评
把域偏移当作层级累积问题，并用梯度一致性调节解耦强度，比单点对齐更细。HSIC 线性核与 batch 估计对小 batch/类别不均敏感；Androids 仅用自发语音以贴近 DAIC，迁移结论受此协议约束。
