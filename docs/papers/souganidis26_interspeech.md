# Discriminating Proficiency Levels in L2 Speech: A Comparative Study of Self-Supervised Models in Basque

- 论文编号：1948
- 报告人：Christoforos Souganidis
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/souganidis26_interspeech.pdf

## 问题
自动化口语评估（ASA）多集中在英语等资源丰富语言与中低水平；对低资源语言（如巴斯克语）高阶 C1 级细粒度区分更难，且缺乏大标注语料。需检验多语自监督语音表示能否做纯语音的能力等级二分类。

## 方法
在 C1-HABE（巴斯克官方 C1 口试独白，Pass/Fail，切 20 秒段）与公开 ICNALE（英语 B1 vs B2+ 独白，作可复现对照）上，微调 wav2vec 2.0 与 mHuBERT-147：CNN 冻结，mean-pool + 线性二分类头，交叉熵。多学习率选 EER，再五随机种子；段级预测聚合，并用 model soup / seed majority vote (SMV) / probability averaging majority vote (PMV) 融合。用混合效应逻辑回归比较架构与策略。

## 实验与结果
C1-HABE：mHuBERT-147 显著优于 wav2vec 2.0 xlsr（准确率预测更好，β=0.30，p=.036）；最佳约 ACC 0.795 / F1 0.715（SMV）。ICNALE：wav2vec 2.0 base 显著优于 mHuBERT（SMV 下 ACC 0.965 / F1 0.842）；策略上 SMV > MS > PMV。作者讨论差异可能来自 L1（声调语 vs 巴斯克/西语）、预训练语种覆盖、等级边界与语料构成等。

## 结论
mHuBERT-147 更适合巴斯克 C1 通过/未通过判别；英语 B2 对照上则是 wav2vec 2.0 base 更强。多语 SSL 可支持低资源高阶口语评估，但最优骨干依赖语言与任务设定。

## 点评
把“高阶邻近等级”与低资源语种组合起来，比常见 A2–B1 分类更贴近证书考试需求。巴斯克数据不可公开、两语料难度与标签定义不完全对齐，跨语结论需谨慎；ICNALE 上 SMV 极高准确率也可能受类不平衡与测试规模影响。
