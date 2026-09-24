# Beyond Uncertainty and Diversity: Temporal-Spectral Guided Active Learning for Audio

- 论文编号：1719
- 报告人：Qisheng Xu
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/geng26c_interspeech.pdf

## 问题
音频有监督微调标注成本高，主动学习（AL）可降本，但现有方法多依赖通用不确定性或几何多样性，把音频当静态向量，忽视决定样本信息量的时频谱结构，导致选样次优。

## 方法
提出 Temporal-Spectral Active Learning（TSAL），骨干为 SSAST。每轮在已标注集上微调后，用 soft-loss 分布筛选高于平均损失的标注样本作为时频谱“信息模式”锚点；对未标注样本提取特征嵌入，并以伪标签反传得到输入梯度，用特征—梯度余弦相似度与锚点匹配打分（β 平衡两项），选 top-B 送标。初始标注 10%，每轮查询未标注 5%，至总预算 40%。

## 实验与结果
在 ESC-50、AudioSet-20k、DCASE2016、UrbanSound8K 上对比 CONF、MARGIN、ENTROPY、CORESET、BALD、CLS-AL、RANDOM。40% 预算时 ESC-50 准确率 82.65%（RANDOM 79.90%），AudioSet-20k mAP 22.08%（RANDOM 19.89%），UrbanSound8K 82.54%，DCASE2016 约 79.23–79.74%。消融显示 soft 选择、特征相似与梯度相似缺一不可；β=1.0 较稳且最优。

## 结论
用 soft-loss 刻画信息模式、再以特征—梯度对齐选样，可在有限标注预算下稳定优于通用 AL 基线，说明时频谱结构引导对音频 AL 必要。作者计划扩展到音频—语言任务。

## 点评
把“难学样本的优化轨迹”当作时频谱结构的可操作代理，避开手写声学规则，工程上可插拔。叙述上“时频谱结构”与 soft-loss 之间仍是间接假设，正文没有独立验证所选样本确实富含瞬态/谐波等结构；在类别极不平衡或伪标签很差时，梯度匹配可能放大噪声。
