# Decoding while Adapting: Zero-Shot Online Speaker Adaptation via Audio-Textual Prompts for Elderly Speech Recognition

- 论文编号：620
- 报告人：Chengxi Deng
- 程序：Tuesday 29 September 2026 / Speech and Language Technologies in Healthcare
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/deng26_interspeech.pdf

## 问题
老年语音异质性强、数据少、构音与语言能力下降，且切段 ASR 丢失跨句上下文。既有适配常有伪标签批处理延迟，或只做声学/分开建模，缺少跨句音文融合的在线说话人建模。

## 方法
在 LoRA 微调的 Whisper-medium 上：用当前及前几句历史语音嵌入与（训练用真值、推理用贪心解码）历史文本，经 Early/Late/CMF/Dual CMF 等融合后由 Q-Former 压缩为紧凑在线说话人 prompts，拼接到编码器侧，实现“边解码边适配”。多任务损失：ASR CE + 说话人分类 + 与离线 SAT prompts 的 MSE。对比 i/x-vector、ECAPA、仅音频 prompts、批处理 Enc/Enc&Dec prompts 等。

## 实验与结果
DementiaBank Pitt（英 WER）与 JCCOCC MoCA（粤 CER），训练/测试说话人不重叠（零样本）。音文 prompts 相对 SI：绝对 WER/CER 降 0.61%/1.22%（相对 2.99%/4.48%），显著；相对批处理 Enc&Dec prompts 性能可比且 RTF 加速最高约 9.83×。优于 i/x-vector、ECAPA；Dual CMF + 约 3 句历史较优。t-SNE 显示音文 prompts 说话人表征更一致。性能对适配数据量不敏感，异于批处理。

## 结论
跨句音文双模态 prompts 可在低延迟下做未见说话人在线适配，同时刻画老年语音的声学与语言侧缺陷。作者强调相对批处理适配的实时性优势。

## 点评
“decoding while adapting”直接针对老年对话助手的延迟痛点，文本历史补足话题/语言一致性是合理归纳。增益绝对值不大但统计显著，且依赖前序解码质量——早期错误可能污染 prompts；粤语基线从原始 Whisper 极高 CER 起步，LoRA 域适应仍是主贡献，在线适配是增量。
