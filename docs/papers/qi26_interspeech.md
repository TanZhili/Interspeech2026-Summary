# MuVAP: Multimodal Multiparty Voice Activity Projection for Turn-taking Prediction in the wild

- 论文编号：1381
- 报告人：Haotian Qi
- 程序：Wednesday 30 September 2026 / LLMs and Conversational Interaction
- 技术分类键：dialogue
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/qi26_interspeech.pdf

## 问题
多方轮次模型常依赖复杂麦阵/多相机，难用于人机交互。现有视听语料多有剪辑切口，破坏因果跟踪；需在单麦+单相机下做说话人感知的未来语音活动预测。

## 方法
MuVAP：将 Voice Activity Projection 与人脸轨迹/主动说话人检测融合；Role-Relative Projection 把任意 N 人映射为固定的“当前 vs 下一持有者”状态。发布 Audio-Visual Conversation Corpus（约 31h 未剪辑单相机多方对话）。因果设定评测 Shift-Hold 与下一说话人，覆盖双人与三人场景。

## 实验与结果
在 Shift-Hold 与下一说话人任务上优于强基线；相对编辑过的语料，未剪辑数据更适合因果跟踪与野生部署评测。

## 结论
单通道音频 + 单视角视频即可做多方说话人感知轮次预测；角色相对投影缓解组合爆炸。新语料支撑野生视听轮次研究。

## 点评
把 VAP 从双人声学推广到“人脸锚定的多方”，部署约束更现实。Role-Relative 简化状态空间是实用工程选择，但可能损失更细的多人竞争结构。性能数字正文表格较多，结论依赖作者报告的相对优势；相机视角与人脸跟踪失败是现场脆弱点。
