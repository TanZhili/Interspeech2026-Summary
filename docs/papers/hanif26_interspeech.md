# ZEBRA: Zero-Shot Entropy-Regularized Prompt Learning for Base-to-Novel Generalization in Audio-Language Models

- 论文编号：261
- 报告人：Asif Hanif
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hanif26_interspeech.pdf

## 问题
ALM 的 prompt learning 能抬高 base 类准确率，却常使 novel 类低于零样本，暴露 base-to-novel 泛化缺口：仅用 base 监督会过拟合并扭曲预训练语义对齐。

## 方法
提出 ZEBRA：在现有 COOP/COCOOP 等 prompt 方法上无新增参数。训练与推理将零样本 logits 与 prompt logits 线性融合（λ_zs=λ_pr=0.5）；训练时在交叉熵上减去（最大化）融合分布的自熵，抑制对 base 类过度自信。零样本 logits 一次性算好可复用，开销可忽略。骨干为 Pengi 的音/文编码器（对比式）。

## 实验与结果
11 个音频分类集、每 base 类 16-shot、50 epoch。COOP/COCOOP 平均 novel 相对零样本下降约 7.13%/4.74%；加 ZEBRA 后 novel 平均升至约 59.4%/59.5%（相对零样本 +4.19%/+4.31%），base 仍保持高位（约 80%/82%）。消融显示零样本 logits 融合贡献最大，熵项边际增益；训练/测试时间几乎不变，novel ECE 下降。

## 结论
零样本锚定 + 自熵正则可在不增参数下缩小 ALM prompt learning 的 base–novel 差距。

## 点评
问题诊断清楚：抬 base 伤 novel 是常见过拟合症状；融合零样本 logits 比再学参数更轻。局限是固定 λ 与 0.05 熵缩放靠经验，部分数据集（如 CREMA-D）novel 仍低于零样本，说明并非处处有效。
