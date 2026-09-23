# BELLA: Efficient Bilevel Learning with LoRA for Multilingual ASR

- 论文编号：2771
- 报告人：Xiaodong Cui
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/saif26_interspeech.pdf

## 问题
编码器–LLM 多语 ASR 中共享解码器易交叉语干扰；路由专家依赖桥接对齐质量，对齐与预测双向耦合，朴素联合训练难兼顾。

## 方法
BELLA：Whisper 编码器 + 可训桥（Q-Former）+ 冻结 Qwen2.5-7B；解码器 MoE-LoRA（共享适配器+K 专家）由路由按桥输出与语言嵌入选专家。双层优化：下层最小化嵌入回归+KD+权重衰减（对齐），上层最小化 ASR NLL+负载均衡/熵（预测）；单环惩罚梯度交替更新，避免昂贵内层求解。

## 实验与结果
CoVoST2 五语（英/西/俄/葡/瑞典）。相对 bridge-only、单 LoRA、按语固定多 LoRA，BELLA 多数语种最低或接近最优 WER；相对基座相对降约 2–4%。专家选择图显示语种特化、未坍缩。ML 在部分高资源语略优但需显式语种选适配器，扩展性较差。

## 结论
用双层学习显式分离对齐与语种特化，可在参数高效条件下缓解多语干扰并稳定路由。

## 点评
把“桥对齐 ↔ 路由选专家”的耦合写成双层问题，比简单多 LoRA 更有结构。实验语种偏高/中资源；相对按语固定 ML 的优势更多在可扩展路由而非绝对分数。
