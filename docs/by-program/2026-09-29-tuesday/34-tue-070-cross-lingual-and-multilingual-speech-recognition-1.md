# Cross-Lingual and Multilingual Speech Recognition 1

- 日期：Tuesday 29 September 2026；时间：14:00-16:00；形式：Poster；Area：9；论文数：9
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场围绕跨语/多语 ASR 与视觉语音识别的适配效率：代码切换唇读用单语语料组合学习；LLM-ASR 用语音—文本对齐的伪音频提示做纯文本域适配；内容感知动态压缩用 CIF 对齐降低 LLM 输入长度。

容量扩展与延迟控制并行：预训练 Transformer 上采样为 MoE、可配置多语解码的 token 无关语言表示，以及 GC-LoRA / MambAdapter 等参数高效适配器，都在“少参数、保精度、控延迟”三角中取舍。

PhonePrune 强调保留细粒度音素相关子网；西弗里西亚语 GER 研究则在污染可控离线集上检验 LLM 纠错是否真实有效。趋势是：跨语迁移不再只靠多语联合训练，而更依赖组合学习、对齐提示、稀疏专家与音素感知压缩。

## 技术内容

### 跨语组合、文本域适配与动态压缩

**Cross-Lingual Compositional Learning for Code-Switched Lip Reading**（论文 1163；Jeonghyeon Joo）提出 CoCoVSR，无需额外采集或生成，用单语语料适配预训练多语 VSR 至代码切换场景。在中英 CSLR 达 SOTA，并在已见/未见多语集上保持竞争表现。

**Refining Pseudo-Audio Prompts with Speech-Text Alignment for Text-Only Domain Adaptation in LLM-Based ASR**（论文 977；Ryo Magoshi）显式建模语音—文本对齐以生成更具表达力的伪音频提示，纯文本域适配中优于既有方法，并改善 OOV 覆盖。

**Content-Aware Dynamic Compression for Efffcient Speech Recognition based on Large Language Model**（论文 230；Bingqian Wang）用 CIF 做内容感知动态声学映射，训练与推理按内容下采样。AISHELL-1、LibriSpeech 在可比平均嵌入长度下相对错误率降 12–26%；可比性能下 ASEL 降逾 45%，TTFT 降 7–19%。

**Upcycling Pretrained Transformers into Mixture-of-Experts for Multilingual Speech Recognition**（论文 1630；Kentaro Shinayama）把预训练 FFN 事后转为 MoE，推理只激活一个专家以保持活跃参数量；硬语言路由与学习软路由均在 10 语 CommonVoice 等设定上改善多语微调。

**Token-Independent Language Representations for Low-Latency Configurable Multilingual Speech Recognition**（论文 2455；Hongxu Zhu）用编码器话语级线索丰富的语言表示替换解码器逐步神经 LSM，把每 token 开销从二次降到线性量级相对隐藏维；长句峰值推理延迟降逾 90%。

### 参数高效适配、剪枝与低资源纠错

**GC-LoRA: Gated Convolutional LoRA for Parameter-Efficient Acoustic Adaptation**（论文 822；Abeer Alwan）在注意力输出投影注入 Conformer 式局部卷积，捕获域特异局部依赖。跨退化/带限/方言/儿童等数据，相对基线 WER 降幅最高约 10.9%，可训练参数增量很小。

**MambAdapter: Lightweight Mamba-Based Adapters for Parameter-Efficient Transfer Learning in Speech and Audio**（论文 1522；Umberto Cappellazzo）在低秩瓶颈适配器中注入轻量 Mamba 并跨适配器参数共享；在四项音频分类与五语语音识别上匹配或超过强 PETL 基线，即使参数预算更紧。

**PhonePrune: One-shot Phoneme-Aware Pruning for Large-scale ASR Models via Phoneme Set Generation and Calibration**（论文 1787；Minsik Lee）提出 Phoneme Ticket Hypothesis，经音素集生成与音素感知校准保留细粒度权重。50% 稀疏下在韩/日 Common Voice 相对 Distil-Whisper 报告约 13.41%/13.83% WER 降幅。

**Can Large Language Models Reliably Correct Errors in Low-Resource ASR? A Contamination-Aware Case Study on West Frisian**（论文 1659；Yun Hao）在西弗里西亚语上评估 LLM 生成纠错，并用非公开文本离线集控制污染；多数设定 GER 改善 ASR，最佳 GPT-5.1 结果超过 oracle WER，离线集增益表明非单纯污染。

## 本场要点

- 代码切换 VSR 可用单语组合学习，避免昂贵的真实混语视频采集。
- LLM-ASR 的纯文本适配依赖语音—文本对齐的伪提示，而非仅微调 LLM。
- CIF 动态压缩与 token 无关语言表示分别砍输入长度与每步语言模块开销。
- Upcycling MoE、GC-LoRA、MambAdapter 提供不同形态的容量/局部建模扩展。
- 音素感知剪枝与污染可控 GER，分别服务压缩部署与低资源纠错可信度。

## 覆盖核对

| id | title |
|---|---|
| 1163 | Cross-Lingual Compositional Learning for Code-Switched Lip Reading |
| 977 | Refining Pseudo-Audio Prompts with Speech-Text Alignment for Text-Only Domain Adaptation in LLM-Based ASR |
| 230 | Content-Aware Dynamic Compression for Efffcient Speech Recognition based on Large Language Model |
| 1630 | Upcycling Pretrained Transformers into Mixture-of-Experts for Multilingual Speech Recognition |
| 2455 | Token-Independent Language Representations for Low-Latency Configurable Multilingual Speech Recognition |
| 822 | GC-LoRA: Gated Convolutional LoRA for Parameter-Efficient Acoustic Adaptation |
| 1522 | MambAdapter: Lightweight Mamba-Based Adapters for Parameter-Efficient Transfer Learning in Speech and Audio |
| 1787 | PhonePrune: One-shot Phoneme-Aware Pruning for Large-scale ASR Models via Phoneme Set Generation and Calibration |
| 1659 | Can Large Language Models Reliably Correct Errors in Low-Resource ASR? A Contamination-Aware Case Study on West Frisian |
