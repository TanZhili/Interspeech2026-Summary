# Dual-Stream DNN-KAN Networks with Bangla-Specific Features for Speech Emotion Recognition

- 论文编号：3374
- 报告人：Kazi Reyazul Hasan
- 程序：Tuesday 29 September 2026 / Speech Emotion Recognition and Representation 2
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hasan26_interspeech.pdf

## 问题
孟加拉语 SER 研究不足；多数既往结果为说话人相关（SD），可能只是记住说话人。大 SSL（emotion2vec、wav2vec2-xlsr）参数量大，且缺少针对孟加拉语韵律的归纳偏置。

## 方法
从 OpenSMILE 80 候选中用 η² 与 ANOVA 筛选 15 个高判别特征，三时间窗聚合得 51 维韵律描述子；与 80 维 MFCC 统计拼接为 131 维。双流：MFCC 走因子化 DNN；韵律走共享 B 样条基的轻量 KAN。双向交叉注意力 + 情绪自适应门控（高唤醒偏韵律、低唤醒偏频谱）后瓶颈融合分类。无数据增强；主评说话人独立（SI）：SUBESCO 16/4、BanglaSER 25/9 说话人划分。仅 1.1M 参数。

## 实验与结果
SUBESCO SI 92.12%（SD 95.35%），超 emotion2vec 89.42%、wav2vec2-xlsr 91.05%；BanglaSER SI 82.79%。同管道在 EmoDB 上重选特征达 93.92%。跨语直接测西方集掉点，韵律-only 掉更狠；消融显示加韵律与 KAN/门控逐步增益。McNemar p<0.01。

## 结论
统计特征筛选 + DNN-KAN 双流可在极少参数下达到或超过大 SSL 的孟加拉语 SI 表现；方法可迁移到其他语言重跑筛选，而非声称特征普适。

## 点评
工作同时打“语言适配”和“评测诚实（坚持 SI）”两张牌，用可解释特征工程对抗堆参数。强处是轻量与门控可解释性；脆弱处是表演/会话语料差距大（SUBESCO vs BanglaSER）、η² 阈值极严可能过拟合训练子集，以及无增强的保守设定未必是部署最优。
