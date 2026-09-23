# Long-form Audio & New Attention Approaches

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：8
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场围绕长音频场景与注意力机制改进：一端是呼叫中心长对话评测与长时自发口语评分，另一端是 AED/SSM/对比解码与可解释注意力。核心矛盾是：模型常在短切分或受限上下文上训练，却要在连续长编码、多口音与噪声条件下稳定工作。

长形声学编码暴露 AED 的位置编码陷阱——段边界外的隐式绝对位置线索在连续解码时消失，交叉注意力对 key/value 的置换不变性削弱排序能力。相应修复包括显式位置、长上下文训练、段拼接与语义切分对齐。评测侧则强调未预训练泄漏的多口音长对话基准，以及多模态（音频+ASR 文本+题目）的长答卷评分。

注意力新路径包括：把通道维局部注意力嵌入 SSM 以动态参数化状态转移；在 AVSR 的对比解码中按注意力与预测分歧自适应缩放干预强度；以及用熵引导的注意力 rollout 做更忠实的 ASR 归因。总体趋势是“长时上下文可训可评”与“注意力可诊断、可自适应”。

## 技术内容

### 长形评测与解码适配

**AppTek Call-Center Dialogues: A Multi-Accent Long-Form Benchmark for English ASR**（论文 2047；Eugen Beck）指出公开英语 ASR 语料多为短切分、朗读/准备话术，或缺乏方言标注。发布 AppTek Call-Center Dialogues：自发角色扮演客服对话，覆盖十四种英语口音与十六类服务场景，专为评测委托采集且此前未公开，降低与大规模预训练重叠风险。在不同切分策略下基准开源 ASR，摘要称口音与切分差异显著，通用美式英语基准上的好表现未必迁移到其他口音。

**Segmental Attention Decoding With Long Form Acoustic Encodings**（论文 341；Xinwei Li）分析 AED 与长形声学编码的根本不兼容：在切分训练中学到依赖段外有限上下文的绝对位置，长形解码时线索消失，交叉注意力置换不变导致无法排序声学编码。提出四项改动：向交叉注意力注入显式绝对位置；用扩展声学上下文做长形训练以消除隐式绝对位置；段拼接覆盖多样切分；语义切分使 AED 解码段与训练段对齐。摘要称可弥合连续与切分编码的精度差距，支持注意力解码器的自回归使用。

**M-LAMA: Multimodal Automated Scoring of Long-form Spoken English**（论文 1542；Minh Dao-Xuan-Quang）针对真实考试中长达数分钟的自发回答，需同时评估声学表达、语言质量与任务完成度。提出 M-LAMA：双编码器与话语感知融合解码器整合原始音频、ASR 转写与题目上下文；部分化音频结构与题目感知文本编码分别刻画“怎么说”与“说什么”，并以三阶段训练应对高利害考试的钟形分数分布。在 87,226 场完整会话上，摘要称结构化多模态对齐显著提升五项标准上的评分可靠性。

### 注意力架构与可解释性

**Attentive Mamba: Channel-wise Local Attention for Speech Recognition**（论文 1708；Jen-Tzung Chien）认为 SSM 受静态局部聚合限制。提出具因果卷积注意力的 attentive SSM：先用因果深度卷积上下文化 Q/K/V，再在时间局部窗上做跨通道注意力，以匹配语谱图中各频率通道的时间相干模式。该设计促进状态转移矩阵的动态参数化，摘要称实验确认将动态通道注意力并入 SSM 有利于 ASR。

**Attention-Guided Reliability Scaling for Contrastive Decoding in Robust Audio-Visual Speech Recognition**（论文 929；Da-Hee Yang）将对比解码（CD）用于 AVSR：在同一底层模型上对比仅音频条件与完整音视频条件。固定对比强度在噪声级间存在权衡——强干预利于重噪，却可能在干净条件过度纠正。提出基于注意力动态与模型间预测分歧的可靠性信号，按 token 自适应调制对比影响。摘要称在 LRS3 上跨干净与低 SNR 条件均有一致提升。

**Listening with Attention: Entropy-Guided Explainability for Transformer-Based Audio Models**（论文 593；Ravi Kumar）针对 Whisper 类 Transformer ASR 难解释、现有 XAI 忠实度与时间定位不足，提出 LEAF-X：熵引导注意力加权、多层 attention rollout，以及可选因果消融，识别低熵高影响头与层，生成稀疏 token-to-frame 归因。摘要称相对强基线更忠实、更稳定，有助于可审计 ASR。

## 本场要点

- 长形评测需要多口音、未泄漏的真实对话基准，并报告切分策略敏感性。
- AED 长形解码需显式位置与训练/切分对齐，才能弥合连续编码差距。
- 长时口语评分依赖音频–文本–题目的结构化多模态融合。
- SSM 可通过通道维局部注意力增强表达力。
- AVSR 对比解码应按可靠性自适应缩放，避免干净条件过纠。
- 熵引导注意力归因提供更忠实的模型内解释路径。

## 覆盖核对

| id | title |
|---|---|
| 2047 | AppTek Call-Center Dialogues: A Multi-Accent Long-Form Benchmark for English ASR |
| 341 | Segmental Attention Decoding With Long Form Acoustic Encodings |
| 1542 | M-LAMA: Multimodal Automated Scoring of Long-form Spoken English |
| 1708 | Attentive Mamba: Channel-wise Local Attention for Speech Recognition |
| 929 | Attention-Guided Reliability Scaling for Contrastive Decoding in Robust Audio-Visual Speech Recognition |
| 593 | Listening with Attention: Entropy-Guided Explainability for Transformer-Based Audio Models |
