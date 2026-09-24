# Mixture of Phonetic Experts Based Low-Rank Adaptation of Conformer Models for Accented English Speech Recognition

- 论文编号：322
- 报告人：Anmol Guragain
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dahal26_interspeech.pdf

## 问题
口音英语 ASR 性能易降；按口音分配 MoE/适配器会使专家数随口音增长，且忽略口音差异常体现为系统的音素实现扭曲这一共享结构。

## 方法
提出 MoPE-LoRA：固定 6 个按发音方式划分的 LoRA 专家（元音、塞音、擦音、塞擦音、鼻音、流音/滑音），插入 Conformer 自注意力 Q/K/V。帧级混合路由：冻结音素 CTC（LibriSpeech 训练）提供监督硬分配，与可学习门控混合（β），top-2 激活。专家跨口音共享，测试无需口音标签。辅助 load-balancing 与 router Z-loss；主损失 CTC。

## 实验与结果
L2-ARCTIC（约 24 h，6 口音），说话人与句子双重 disjoint。NeMo Conformer CTC Small。最佳 MoPE-QKV（层 6–16）WER 10.43%，优于 Full FT 12.80%、Single LoRA-QKV 11.33%、MAS-LoRA 11.77%。零样本留一口音：平均 WER 9.98%，相对 Single LoRA（11.38%）相对改进 12.3%。TIMIT MI/t-SNE 支持中层最富音素信息，故聚焦 6–16 层；跨域音素 top-1 仅 36.04%，故用 top-2 补偿。

## 结论
按音素范畴分解适配、混合路由，可在固定专家数下提升多口音与未见口音识别，且参数高效。

## 点评
用发音方式归纳口音变异，比“一口音一专家”更可扩展；音素监督在口音上不准时靠学习门控补偿是务实设计。边界在于依赖额外音素模型与英语发音学分类，对更强口音或非英语音系的迁移仍需验证。
