# Information Extraction and Retrieval / Survey Talk

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Oral
- Area：12
- 论文数：5（含 1 场 Survey Talk）
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场以表现力语音翻译综述开场，随后转向关键词检出、口语检索 tokenization、端到端声学命名实体识别，以及端侧少样本文本相似度编码器。信息抽取/检索线强调：零样本用户定义关键词需同时防冒名、离散 token 要可扩展且保持成对对齐、组织名实体依赖跨度结构约束，边缘设备则希望单轻量模型覆盖多类语音邻域分类。

综述覆盖 S2ST 架构、数据与合成、表征、LLM 用法与评测，突出保留说话人音色/情感及词级停顿、语速、重音、音高等局部表现力仍缺共识。应用论文则把说话人验证与音素监督 KWS 晚期融合、分阶段对比学习 + CTC/DTW 对齐训练 tokenizer，并用 LLM 增强与结构约束实体学习强化组织名识别。

## 技术内容

### 表现力语音翻译综述

**Expressive Speech Translation**（Survey Talk；Philipp Koehn）  
指出语音到语音翻译在架构、数据、评测等方面仍少共识；前沿是在译文中保留输入表现力，涵盖说话人音色、情感与声学条件等全局属性，以及停顿、语速变化、词级重音与音高等局部属性。综述将覆盖训练数据、数据合成、语音表征、模型架构、大语言模型用法与评测指标。

### 关键词、检索 token 与实体/端侧分类

**Personalized Keyword Spotting for User-Defined Keywords Leveraging Text-Independent Speaker Verification**（论文 1130；Ming-Hsiang Hu）  
用户定义 KWS 常学说话人不变表示，无法拒绝正确关键词的冒名者。ZP-KWS 结合音素监督音频编码器与约 0.9M 参数的 GE2E 预训练紧凑说话人编码器，推理时乘法晚期融合使两支路可独立否决。LibriPhrase、Google Speech Commands 与 Qualcomm 上，1% FAR 下目标 FRR 相对最强基线最高降约 60%，总约 1.55M 参数面向边缘。

**wav2tok 2.0: Scalable Audio Tokenization Maintaining Explicit Pairwise Token Alignment for Efficient Audio Retrieval**（论文 141；Adhiraj Banerjee）  
在 BEST-STD 骨干上分阶段：先对比学习 + 向量量化得判别、说话人不变表示，再用 CTC 对齐损失与新型 DTW 对齐帧级预测目标及自适应加权强制成对 token 一致性。QbE-STD 上持续优于 BEST-STD 与通用 tokenizer，且可扩展。

**Rethinking Organization Entity Modeling in End-to-End Acoustic Named Entity Recognition**（论文 3115；Spandan Dey）  
分析端到端声学 NER 中组织实体因多词跨度、缩写与词汇变异更难；常规交叉熵不足建模跨度依赖。提出组织感知 Whisper 声学 NER：LLM 定向语义增强、类别特定边界监督与结构约束实体学习（SCEL）目标。实验称组织识别大幅提升并保持强 ASR，实体识别优于多种既有方法。

**AnySimLite: A Lightweight Few-Shot Similarity Encoder for On-Device Speech-Adjacent Classification**（论文 1316；Sourav Ghosh）  
将多种语音邻域分类任务归结为细粒度文本相似度，提出词级与字符级双通道轻量相似度编码器 ANYSIM-LITE 及数据变换策略。少样本设置下达 SOTA 或接近 SOTA，最差性能降幅低于 7%，模型大小不及 SOTA qLLaMA_LoRA-7B 的 1/250。

## 本场要点

- 表现力 S2ST 需同时处理全局音色/情感与局部韵律控制，评测与数据仍开放。
- 用户定义关键词需关键词检测与说话人门控双零样本。
- 可扩展检索 tokenizer 应显式保持成对 token 对齐。
- 组织名声学 NER 需要跨度结构约束与定向增强。
- 端侧可用统一轻量相似度编码器覆盖多类语音邻域任务。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| （Survey） | Expressive Speech Translation |
| 141 | wav2tok 2.0: Scalable Audio Tokenization Maintaining Explicit Pairwise Token Alignment for Efficient Audio Retrieval |
| 1130 | Personalized Keyword Spotting for User-Defined Keywords Leveraging Text-Independent Speaker Verification |
| 1316 | AnySimLite: A Lightweight Few-Shot Similarity Encoder for On-Device Speech-Adjacent Classification |
| 3115 | Rethinking Organization Entity Modeling in End-to-End Acoustic Named Entity Recognition |
