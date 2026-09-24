# M-LAMA: Multimodal Automated Scoring of Long-form Spoken English

- 论文编号：1542
- 报告人：Minh Dao-Xuan-Quang
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/daoxuanquang26_interspeech.pdf

## 问题
真实口语考试需对多分钟自发回答做发音、流利、词汇、语法、语篇等多维评分，但既有工作多聚焦短句或发音；公开数据也缺乏长时、多标准熟练度标注。通用音频语言模型对细粒度发音/韵律与钟形分数分布不够适配。

## 方法
提出 **M-LAMA**：双流编码 + 语篇感知融合。
- 音频：冻结 Whisper-Large + bottleneck adapter；3–5 分钟回答切成 30s chunk，按考试三部分分层注意力池化并加位置嵌入。
- 文本：冻结 Qwen2-1.5B 编码转写与题目；题目条件交叉注意力评估任务完成度；双向 audio↔text 注意力与门控融合（含双线性交互），输出 0–10（0.5 步）21-bin 期望分数。
- 训练三阶段：对比对齐 → 粗档分类（低/中/高）→ MAE+Focal 细粒度回归，缓解中档主导。

## 实验与结果
数据：约 86,491 场、29,034 考生、~4,845 小时（按考生切分防泄漏；因保密不可公开）。全测集上 Multi-stage 相对最强开源基线（Qwen-2.5 Omni）五维 MAE 约降 15–29%、QWK/Acc@1 全面提升；相对 GPT-4o Audio 等 API（1k 子集）亦明显更好。消融：Text+Audio Acc@1 90.82% 远高于单模态；去题目模块伤语篇管理；单阶段训练明显弱于多阶段。chunk 留一分析显示前部段贡献更大但仍全局聚合。

## 结论
长时口语评分需要结构化多模态对齐（声学交付 + 语言内容 + 题目语境）与分布感知训练；M-LAMA 在五维标准上显著提升可靠性。代码与检查点公开，数据可按申请分享。

## 点评
把评分量表拆到架构组件（部分结构、题目条件、双向融合）和「先对齐再分档再回归」的三阶段优化，针对考试分数钟形分布很对症。强在大样本机构数据与完整消融；主要风险是数据不可公开、依赖 Whisper/Qwen 冻结表征，以及商业 API 只在 1k 子集对比，外推需谨慎。
