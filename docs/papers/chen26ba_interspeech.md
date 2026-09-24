# Probing Spatial Structure in Pretrained Audio Representations

- 论文编号：2506
- 报告人：Sivan Ding
- 程序：Wednesday 30 September 2026 / Evaluation, Benchmarking, and Reliability of Audio Systems
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26ba_interspeech.pdf

## 问题
多通道/空间音频预训练模型增多，但端到端流水线难分离“表征里到底编码了哪些空间因素”；缺可控探测基准。

## 方法
提出 SARL：合成单源场景，独立控制源因素（方位、俯仰、距离、事件类）与房间因素（RT60、体积、形状）；对多种冻结编码器做统一线性探测，并比较源/房间扰动下的表征敏感度。覆盖 FOA/立体声等输入与 SSL/监督/编解码类模型。

## 实验与结果
三规律：(1) 输入配置与训练范式塑造空间编码；(2) 源因素 systematically 比房间因素更易解码；(3) 敏感度分析显示对源扰动响应更大、对房间更异质。FOA 输入 + SSL 倾向更稳健的空间因子编码。

## 结论
当前预训练表征对源属性偏置明显、对全局房间属性偏弱；SARL 开源以支持可复现空间表征评估。

## 点评
用可控合成把“空间信息是否在嵌入里”从下游任务里剥离出来，对机器人/沉浸音频表征很有诊断价值。线性探测与均值池化、单源设定会低估非线性可及信息与真实多源复杂度。
