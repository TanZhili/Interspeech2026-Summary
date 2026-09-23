# Who is Talking to Me? Addressing Egocentric TTM with Speaker-aware Conversational Context

- 论文编号：2358
- 报告人：Fukun Chen
- 程序：Monday 28 September 2026 / Multimodal Spoken Dialogue Systems
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/chen26x_interspeech.pdf

## 问题
第一人称 Talking-to-Me（TTM）要判断说话人是否在对相机佩戴者说话。现有音视频融合缺长程对话历史；多任务方法未显式建模说话人角色；SICNet 等上下文方法身份表征粗、时间窗短。真实场景中交互伙伴常出镜外或移开视线，视觉线索缺失。

## 方法
多模态对话上下文框架，三模块：
1. **SSE**：Whisper 转写 + RoBERTa 话语特征；CAM++ 聚类做说话人日记化（佩戴者 ID 固定为 0）；可学习说话人 ID 与对话轮次嵌入与文本拼接投影；
2. **CCM**：当前及前 \(T-1\) 句的 SSE 特征入记忆库，经多层 utterance Transformer 自注意力建模多轮语义依赖；
3. **GVE**：冻结 LAM（Looking-at-Me）骨干提帧级注视相关视觉特征，时序池化后投影；
文本–视觉两 token 自注意力融合（取文本侧输出 + 残差）后 MLP 分类。Whisper/CAM++/LAM 冻结，微调 RoBERTa 部分层与下游模块。

## 实验与结果
Ego4D Social Interaction TTM：训练 389 clips / 验证 50 clips；验证集 2469 样本；指标 mAP（测试集不公开，报验证）。
- 全文模型 **72.40% mAP**，相对 SICNet 68.98 提升 3.42 点，优于 Ego4D-TTM、TalkNet、EgoT2 等。
- 消融：Baseline 66.52；去 CCM 68.01；去 GVE 70.80；去 SSE 69.84。
- 上下文长度：\(T=1\) 为 68.34，\(T=3\) 升至 70.89，约 \(T=10\) 达 72.29 后饱和；推理约 31.4 FPS。

## 结论
显式说话人感知语义依赖与 LAM 注视视觉线索联合，在 Ego4D TTM 上显著优于既有基线。失败多见于缺脸与语义模糊（如低头自语）。未来拟引入更大规模多模态 LLM。

## 点评
做法把“谁在对谁说话”拆成日记化身份 + 多轮文本上下文 + 注视先验，对出镜外场景用语义补视觉缺口，设计贴合自我中心社交。强在模块消融与上下文长度曲线清楚；脆弱点在依赖上游 Whisper/日记化质量，以及 LAM 在缺脸时失效——作者亦承认此类场景仍易误判。
