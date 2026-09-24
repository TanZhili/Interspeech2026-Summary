# A Large-Scale Per-Speaker Analysis of Re-identification Risk in Speech Anonymization

- 论文编号：440
- 报告人：Orane Dufour
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/dufour26_interspeech.pdf

## 问题
匿名化隐私常用平均 EER，掩盖个体再识别风险差异；既有说话人级研究样本小、攻击架构单一，难以判断“易/难链接”是否为说话人固有属性。

## 方法
在约 4,949 名 CommonVoice 试验说话人上，用 linkability（正确 enrollment 相似度是否高于所有其他）做最坏情形评测；enrollment 池大小 N 从 22,024 二分至 21，每说话人 5 次随机抽样×11 个 N；对话长度 L∈{1,3,5}。匿名器：VPC 2025 B3、B5（句级不同伪说话人）。半知情攻击者：ECAPA、WavLM ECAPA、ResNet-101。按 Q3/Q1 定义 easy-/hard-to-link 列表，比较 18 配置的交集/并集与 Jaccard 相似度。

## 实验与结果
说话人级 linkability 高度两极化；但跨 18 配置 consistently easy 仅 5 人、consistently hard 166 人，并集却覆盖约 86.9%/92.4% 试验说话人。WavLM ECAPA 最强，B3 比 B5 更易攻；L 增大显著增强链接。Jaccard 均值均 ≤0.47：攻击者架构影响相对最小（约 0.39/0.47），匿名器与 L 影响更大且相近。

## 结论
再识别风险主要由攻击者、匿名器与可用语音量交互决定，而非稳定的内在说话人脆弱性；隐私保证需条件化于具体威胁模型。未来拟探索给定匿名–攻击对的先验风险估计。

## 点评
大规模负结果很有价值：打破“某些人天生更不安全”的直觉，指出平均 EER 与固定脆弱说话人清单都不够。协议强调句级随机目标映射与多样半知情攻击，结论对外推到其他匿名范式仍需验证，但已足够挑战当前评测叙事。
