# RAT: Reference-Augmented Training for ASV Anti-Spoofing

- 论文编号：132
- 报告人：Vojtěch Staněk
- 程序：Tuesday 29 September 2026 / Speaker Verification and Anti-Spoofing
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/stanek26c_interspeech.pdf

## 问题
传统 ASV 反欺骗多为单句检测，未利用注册参考；直接做参考条件架构时，作者发现模型训练后推理常忽略参考，但参考增强训练仍带来泛化收益。需解释并利用这一现象。

## 方法
RAT：共享 XLS-R 300M 提参考/测试多层特征；Reference-Informed Block 含测试侧 MLP 与测试 query–参考 key/value 的多头交叉注意力，残差相加后跨层与时间均值池化，MLP 输出 bona/spoof logits。训练时同说话人 bona fide 随机配对参考；两阶段（冻结前端再联合微调）+ 时间掩蔽/mu-law/RawBoost/噪声滤波等增强。推理可换零向量参考。

## 实验与结果
ASVspoof 5：RAT 零参考推理 EER 2.57%、minDCF 0.074，优于同配方单句 XLS-R 基线（4.87%/0.141），并超过文献单模型与接近 12 模型融合冠军。噪声、截断、静音、噪声参考、说话人不匹配等推理消融性能几乎不变。训练动力学显示参考依赖迅速下降。

## 结论
参考通道主要改善优化与表示，而非推理必需；RAT 以单检测器达到强 ASVspoof 5 表现。代码与权重已公开。

## 点评
把“参考条件失败”转成可复用训练策略，发现扎实。残差设计使模型可退回单句路径，解释了零参考仍强；代价是大 SSL 前端与 Open 条件设定，与挑战闭集规则不完全对齐。
