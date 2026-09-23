# Referee: Reference-aware Audiovisual Deepfake Detection

- 论文编号：1246
- 报告人：Hyemin Boo
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/boo26_interspeech.pdf

## 问题
音视频 deepfake 检测跨操纵方法泛化仍难。多数方法不显式利用“同一说话人真实参考”作为生物识别锚点，难以放大身份级不一致。

## 方法
Referee：用 one-shot 参考样本经 identity bottleneck 与 matching 模块建模说话人特异线索的关系一致性；辅助身份匹配损失（真–真同人 vs 伪造视为不同身份）；将参考感知身份 token 与目标 AV 特征送入 AV-Transformer 做检测。代码公开。

## 实验与结果
跨数据集：在 FakeAVCeleb 训练测 FF++，Referee AUC 79.78 / AP 91.00，优于多种无参考或不同训练源的 AV/视觉基线。域内与 KoDF 跨语言协议亦称达 SOTA；消融显示身份匹配设计有效。

## 结论
作者认为显式关联参考生物识别先验是可靠 AV 取证的关键方向。

## 点评
把说话人验证式 one-shot 锚点接到伪造检测，对“像某人但不一致”的攻击很对症。实际部署依赖可获得的干净参考；参考被污染或跨会话信道差时匹配模块可能误导。
