# GMOD: Voice-Face Association Learning via Graph Mining and Orthogonal Disentanglement

- 论文编号：432
- 报告人：Ju Zhang
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/wang26h_interspeech.pdf

## 问题
无监督声–脸关联学习面临两类难点：跨视频同说话人被当成假负样本；模态私有属性渗入共享嵌入干扰跨模态对齐。聚类/原型伪标签在训练早期不可靠，难以刻画身份局部分布。

## 方法
提出 GMOD：(1) 正交解缠——每模态经并行编码器得到共享身份 \(z^{\mathrm{id}}\) 与私有 \(z^n\)，软正交损失 + 拼接重构 MSE；(2) 图引导正样本挖掘——对视频级 \(L_2\) 平均原型建跨模态相似图，以 voice→face k-NN 再反向回填，\(k\) 从 20 线性衰减到 8（课程式），用多正样本 InfoNCE（双向）。骨干为 ECAPA-TDNN（声）与 FaceNet（脸），在 VoxCeleb1 上无监督训练（901/100/250 身份划分，训练不用身份标签）。

## 实验与结果
相对 Pins、SL、CMPC、PAEFF 等：验证 AUC 87.73%（U）/77.37%（G）；1:2 匹配双向约 87.04%；检索 mAP V2F/F2V 7.14%/7.59%，均为表中无监督最优。消融：去图、固定 \(k\)、去正交+重构均下降；私有支路反匹配 AUC≈49.28%，说明私有支路几乎不含身份。1:N 匹配在 N=10 时双向准确率仍 >45%。

## 结论
全局相似图 + 课程挖掘缓解假负样本，正交解缠稳住跨模态共享身份特征；在 VoxCeleb1 验证/匹配/检索上优于现有无监督方法。未来拟扩展到多语复杂场景。

## 点评
相对“先聚类再伪标”路线，直接用全局图把潜在正样本抬进分子，更贴合早期对齐不稳时的假负问题；voice 锚定图优于 face 锚定也符合“声比脸跨视频更稳”的经验。正交+重构是经典共享–私有分离套路，私有支路近随机的反匹配测试是有说服力的自检。增益幅度相对 SL/CMPC 不夸张但全面，更像工程上把两块关键拼稳。
