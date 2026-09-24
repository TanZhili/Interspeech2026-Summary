# Fair Cognitive Impairment Detection Through Unlearning

- 论文编号：1353
- 报告人：William Nguyen
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nguyen26e_interspeech.pdf

## 问题
轻度认知障碍（MCI）筛查模型常编码性别、语言等人口属性，导致子群表现不公；多模态融合不足时鲁棒性也差。

## 方法
FMD：跨模态融合（语音/文本/图像）+ 前馈网络；辅助人口分类器识别伪相关人口特征，用梯度反转对其 unlearn。分别可对性别或语言属性做遗忘。在 TAUKADIAL、PREPARE 等多语基准评估，主指标 F1 与 worst-group F1。

## 实验与结果
TAUKADIAL：FMD_Lang 总体 F1 92.6 vs 最佳基线 CogniVoice 84.1；worst-group 90.9 vs 81.3。PREPARE：FMD_Sex 总体 F1 60.1 最高；FMD_Lang worst-group 57.4 优于 Whisper 等。探针显示遗忘后人口属性可预测性下降（更接近随机）。消融去掉跨模态或 unlearn 均伤表现或公平。

## 结论
人口属性遗忘与更强跨模态融合可同时提升 MCI 检测平均性能与最差子群表现，朝更公平筛查迈进。

## 点评
把公平做成可训练目标而非事后重加权，探针验证有说服力。需选择遗忘哪类属性；过度遗忘可能丢弃与病理相关的合法相关。PREPARE 绝对 F1 仍偏低，说明数据难度与方法上限并存。
