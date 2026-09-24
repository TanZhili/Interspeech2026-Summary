# Cross-Lingual and Multilingual Speech Recognition 1

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：9
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕跨语/多语 ASR 与视觉语音识别的适配效率：代码切换唇读用单语语料组合学习；LLM-ASR 用语音—文本对齐的伪音频提示做纯文本域适配；内容感知动态压缩用 CIF 对齐降低 LLM 输入长度。

容量扩展与延迟控制并行：预训练 Transformer 上采样为 MoE、可配置多语解码的 token 无关语言表示，以及 GC-LoRA / MambAdapter 等参数高效适配器，都在“少参数、保精度、控延迟”三角中取舍。

PhonePrune 强调保留细粒度音素相关子网；西弗里西亚语 GER 研究则在污染可控离线集上检验 LLM 纠错是否真实有效。趋势是：跨语迁移不再只靠多语联合训练，而更依赖组合学习、对齐提示、稀疏专家与音素感知压缩。

## 论文技术总结

# Cross-Lingual Compositional Learning for Code-Switched Lip Reading

- 论文编号：1163
- 报告人：Jeonghyeon Joo
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/joo26_interspeech.pdf

## 问题

语码转换在多语交流中普遍，但视觉语音识别（唇读）缺真实混合语料；CSLR 规模小、句式重复。多语 VSR 默认“一句一语”，难直接泛化到句内切换。

## 方法

提出 CoCoVSR：从中英单语视频拼接伪混合样本（双向顺序），与真实 CSLR 联合训练；在预训练 MultiVSR 上微调视觉前端，并用共享 LoRA adapter（非整语专家）适配 Transformer 编解码，利用跨语共同 viseme。

## 实验与结果

CSLR：CER/WER/MER 16.69/16.23/16.48，大幅优于先前 CTC/MoE 等方法（MER 约 37+）。MultiVSR 中文与未见 LRS2 英语仍保持可竞争水平。仅训 CSLR 混合集最好但单语崩；加入 CoCo 数据可在混合与单语间折中。共享 decoder adapter 优于多 adapter。

## 结论

作者认为无需额外采集或生成合成，跨语拼接 + 共享轻量适配即可让多语唇读获得语码转换能力，并尽量保住原多语性能。

## 点评

抓住视觉跨语 articulatory 重叠，故意不用 ASR 里常见的语言专家路由，参数更省。拼接伪混合边界生硬，与真实切换韵律/口型过渡有差距；CSLR 本身模式重复，SOTA 幅度需结合数据特性解读。单语保留与混合精度的权衡在消融中交代清楚。


# Refining Pseudo-Audio Prompts with Speech-Text Alignment for Text-Only Domain Adaptation in LLM-Based ASR

- 论文编号：977
- 报告人：Ryo Magoshi
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/magoshi26_interspeech.pdf

## 问题

LLM-ASR 在新领域常只有文本、无配对语音。仅微调 LLM 缺声学上下文；伪音频提示要么依赖 TTS 难扩展，要么只做文本嵌入上采样/掩码，未对齐音频编码器与投影器输出特性。

## 方法

提出 TE2SL：用可训练 Conformer 精炼模块，把 LLM 文本嵌入映射到真实音频提示潜空间。先在源域配对数据上学习文本嵌入→音频提示对齐；适配时冻结该模块，对目标域文本嵌入随机上采样、精炼并时间掩码，生成样本相关伪音频提示，再与指令一起微调 LLM。对比 text-only FT、Soft Prompt、Upsample-and-Mask。

## 实验与结果

英：LibriSpeech→SPGISpeech/SlideSpeech；日：CSJ SPS→APS（eval1/2）。TE2SL 全面最优：如 SPGISpeech WER 8.5（基线 11.1）、Rec OOV 50.1%；SlideSpeech WER 14.0；CSJ eval1/2 CER 19.6/17.5，OOV 召回亦最高。

## 结论

作者认为伪提示需同时样本相关且感知编码器/投影器特性，才能在纯文本适配中弥合模态差并提升领域词覆盖。

## 点评

把“伪音频提示像不像真提示”当成可学习对齐问题，比启发式上采样更对症。不依赖 TTS，利于多语扩展。精炼模块质量绑死源域配对数据；跨域声学差异极大时，伪提示仍可能偏语言侧。


# Content-Aware Dynamic Compression for Efficient Speech Recognition based on Large Language Model

- 论文编号：230
- 报告人：Bingqian Wang
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhu26_interspeech.pdf

## 问题

LLM-ASR 常用固定步长下采样压缩声学序列，忽略内容动态，易丢信息或冗余，损害准确率–效率权衡。

## 方法

用 Continuous Integrate-and-Fire（CIF）作动态前端：对冻结编码器输出预测 firing 权重，累加触发声学嵌入，训练时用 MAE 使权重和逼近转写 token 数；推理无文本时仍生成与内容匹配的变长序列，再经适配器送入 LLM。对比 Conv-MLP / Concat-MLP 固定 DS=2/4/6。

## 实验与结果

AISHELL-1（FireRed 编码器）：Dyn-MLP CER 2.67–3.53，ASEL 27，相对 WEST 固定基线相对降错约 15–33%，长度约减 61%。StepAudio2 设定下相对相近 ASEL 固定基线可相对降错约 12–26%，ASEL 常减约 60%。GigaSpeech Stage2 CER 11.20（ASEL 39）。TTFT 在较长句上降约 7–19%。回归损失 MAE/MSE/SMAE 影响很小。

## 结论

作者认为内容引导的 CIF 动态压缩可在更短 LLM 输入下保持或提升识别，改善准确率–效率权衡，并在大规模数据上可扩展。

## 点评

把“该留多少帧”绑到文本长度，比盲目加大固定下采样比更合理。推理无真值长度依赖学到的速率先验，极快/极慢语速可能偏。编码器冻结利于稳定，也限制与映射器联合再优化声学表示。


# Upcycling Pretrained Transformers into Mixture-of-Experts for Multilingual Speech Recognition

- 论文编号：1630
- 报告人：Kentaro Shinayama
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/shinayama26_interspeech.pdf

## 问题

多语联合微调大预训练 ASR 时，共享容量不足易负迁移，甚至不如分语种模型。LoRA-MoE 等轻量专家容量有限，难充分表达语种差异。

## 方法

将 Whisper 解码器 FFN 上循环（复制预训练参数）为稀疏 MoE，每 token 仅激活 1 个专家，活跃参数与稠密模型相同。路由：按语言身份硬路由，或基于隐状态（±语言嵌入）的 soft top-1。编码器保持共享。在 CommonVoice 10 语与亚洲 4 语上评测。

## 实验与结果

CommonVoice：硬路由 10 专家平均优于 MultiFT 与 LoRA-MoE，甚至优于 MonoFT 上界（西欧 5 语 WER 12.3 vs MultiFT 13.6）。亚洲 4 语硬路由平均 CER 5.2 vs MultiFT 6.2（约相对降 16%）。上层解码器放置 MoE 即可接近全层效果且参数更少。对 medium/large-v2 仍有效。Soft 路由更省专家数但弱于硬路由。

## 结论

作者认为直接扩容 FFN 专家比低秩专家更利于多语微调；硬路由强制语种分工，减轻负迁移；语言依赖主要在解码器上层。

## 点评

“上循环=复制 FFN 成专家”简单可落地，推理成本几乎不变。硬路由需可靠语言 ID；soft 路由因专家同初始化难分化是文中坦承的局限。对书写体系差异大的语种集合尤其有说服力。


# Token-Independent Language Representations for Low-Latency Configurable Multilingual Speech Recognition

- 论文编号：2455
- 报告人：Hongxu Zhu
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhu26c_interspeech.pdf

## 问题

可配置多语 ASR（CMM）用语言特定模块（LSM）支持任意语种子集，但解码器 LSM 每步重算，延迟随输出长度线性增长，长句开销大。

## 方法

保留编码器一次计算的神经 LSM；解码器改为 token 无关语言表示：CMM-S 用静态语言向量做加性调制；CMM-D 再融合顶层编码器 LSM 的句级池化动态线索与可缓存静态矩阵扩展，门控合成一次后整句复用。每步 LSM 复杂度从 O(d²) 降到 O(d)。

## 实验与结果

MLS 8 语：CMM-D allhot/onehot 平均 WER 8.70/8.67，与原 CMM 持平，优于多语基线 9.26。平衡 4 语（含粤/普/英/马，含语码转换）同样 parity。长输出（110–130 token）上原 CMM 额外延迟 +107.88 s，CMM-S/D 仅约 +2.23/+7.34 s，峰值额外延迟降逾 90%。

## 结论

作者认为语言身份是全局属性，不必绑在自回归逐步环上；编码器告知的 token 无关表示可在精度相当下大幅降延迟。

## 点评

把“可配置多语”的延迟瓶颈拆开：编码器保留动态语言声学，解码器只做常向量/句向量加法，工程洞察清晰。CMM-S 略损精度、CMM-D 补回，消融逻辑完整。依赖用户/提示给出语种子集；极端语码切换仍靠编码器侧 LSM。


# GC-LoRA: Gated Convolutional LoRA for Parameter-Efficient Acoustic Adaptation

- 论文编号：822
- 报告人：Abeer Alwan
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/shankar26_interspeech.pdf

## 问题

Whisper 等 Transformer 基础模型在混响、窄带、方言、儿童等声学失配域上掉点；标准 LoRA 调全局注意力，缺局部时序建模，难以补足 Conformer 式局部归纳偏置。

## 方法

提出 GC-LoRA：在 MHSA 输出投影 Wo 的低秩旁路中，嵌入 Conformer 风格门控深度可分离卷积（pointwise+GLU、depthwise、GroupNorm、Swish、再 pointwise），在瓶颈内做局部精炼。相对标准 LoRA 参数更少（如 medium 上 447k vs 829k）。

## 实验与结果

Whisper-medium：AMI/SWBD/CORAAL/MyST WER 11.5/6.3/9.9/8.6，相对 LoRA 显著更优（p&lt;0.05），参数约少 46%。跨 tiny–large-v3 多数设定仍优；tiny+AMI 相对降约 10.9%。消融显示门控深度卷积优于简单 Conv-LoRA / MultiConv-LoRA；推理延迟几乎与 LoRA 相当。

## 结论

作者认为在 LoRA 瓶颈内注入局部卷积，能以极少参数让 Transformer 获得更强声学域适应，缩小与全量微调差距。

## 点评

针对“Transformer 缺局部”的结构补丁放在注意力输出处，不改预训练全局注意，设计克制。增益在失配域一致，但绝对幅度不大；全量微调仍常更强。超参固定跨模型规模，可能解释部分非单调缩放。


# MambAdapter: Lightweight Mamba-Based Adapters for Parameter-Efficient Transfer Learning in Speech and Audio

- 论文编号：1522
- 报告人：Umberto Cappellazzo
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ali26b_interspeech.pdf

## 问题

微调大语音/音频基础模型成本高，PETL 已普及；Mamba 擅长线性复杂度长序列建模，但尚未作为适配器注入 Transformer 做高效迁移。

## 方法

提出 MambAdapter：在瓶颈适配器低秩空间插入轻量 Mamba，并用可学习缩放 α；跨层共享 down/up 投影以抵消 Mamba 参数开销。用于 AST 音频分类与 Whisper 多语 ASR（仅编码器插适配器，解码器冻结）。

## 实验与结果

分类（Pfeiffer）：MambAdapter 约 0.06M 参数，平均准确率 89.72，接近 Conformer 适配器（0.27M，90.07）且远超 LoRA/Bottleneck。ASR（五语）：平均 WER 优于 Bottleneck/Conformer/LoRA（同参预算下约降 0.8–7.4%）。低参预算（&lt;500k）优势更大；去 Mamba 则 FSC 等任务大幅掉点；共享投影以约 4× 参数换不到 1% 平均收益。

## 结论

作者认为把 Mamba 放进共享投影瓶颈，可在更少可训参数下匹配或超过强 PETL 基线，是首个将 Mamba 用于语音/音频 PETL 的工作。

## 点评

用 SSM 的时间压缩特性匹配低秩瓶颈，理论动机清楚。分类上与 Conformer 适配器接近但更省参；ASR 增益更明显。超参（expand、d_state、kernel）对结果敏感，文中有网格分析。未探索解码器侧适配。


# PhonePrune: One-shot Phoneme-Aware Pruning for Large-scale ASR Models via Phoneme Set Generation and Calibration

- 论文编号：1787
- 报告人：Minsik Lee
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26q_interspeech.pdf

## 问题

大规模 ASR 一次性剪枝常按幅度丢弃小权重，但部分小权重对细粒度音素辨别关键（Phoneme Ticket Hypothesis）；剪掉后擦音/塞音等区域识别崩溃。

## 方法

PhonePrune：按音系约束生成对比三元组校准集（互补分布、最小对等）；用掩码梯度得音素相关性分数；复合得分 S=|W|+λ|W|·S̃_ling 调制剪枝阈值，保护音素票。在 Whisper-large 50% 稀疏度一次性剪枝，校准 128 三元组。

## 实验与结果

相对幅度/OBS 等非结构化剪枝大幅更好。对 Distil-Whisper：韩/日 Common Voice 相对 WER 降 13.41%/13.83%（15.50/16.20 vs 17.90/18.80）；英语略逊于蒸馏模型，平均 WER 11.50。作者归因韩语细谱对比与日语时长对立更依赖脆弱音素票。校准样本数与 λ 消融显示 N=128、γ=0.5 较稳。

## 结论

作者认为压缩需显式保护编码精细音素的低幅度子网；音素感知校准可在高稀疏下更好保持识别，尤其对音系细节重的语言。

## 点评

把剪枝从纯幅度启发式拉回音系先验，解释了为何韩/日增益更大。一次性、无重训利于部署。校准依赖对齐音素片段与手工三元组，扩展到更多语言需重复工程；英语冗余线索多时收益较小符合叙事。


# Can Large Language Models Reliably Correct Errors in Low-Resource ASR? A Contamination-Aware Case Study on West Frisian

- 论文编号：1659
- 报告人：Yun Hao
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hao26b_interspeech.pdf

## 问题

低资源 ASR 仍弱；LLM 生成式纠错（GER）在高资源语上有效，但低资源语覆盖不足，且公开评测可能污染导致虚高。需污染可控地检验是否真能纠错。

## 方法

以 XLS-R 为弗里斯兰 ASR；在 Common Voice 与新建非公开文本的 Offline 集（故事书+原创句，4 男声，1.5 h）上做 GER。比较生成式纠错与从 5-best 选择；模型含 Qwen3（±LoRA）、GPT-4o-mini、GPT-5.1；零样本到少样本。并做句级改进/退化统计与编辑级精度召回。

## 实验与结果

CV：基线 WER 13.5，oracle 9.6；GPT-5.1 生成式最低 8.9（超 oracle），选择式仅约 12.1。Offline：基线 21.1，GPT-5.1 最低 13.8（亦超 oracle 18.0），与公开集趋势一致，支持非污染解释。Qwen3 几乎不改。生成式比选择式更强；GPT-5.1 句级改进多但也可能退化；插入纠错召回高、精度偏低，删除相反。

## 结论

作者认为强 LLM 的 GER 在低资源弗里斯兰上有效且可超 N-best oracle；非公开集上的相近增益表明并非仅靠污染。开源小模型收益有限，效果高度依赖模型语言覆盖。

## 点评

用非公开文本听写集专门压污染假说，方法学贡献突出。生成式可跳出 N-best 是关键优势。强依赖闭源 GPT；开源侧几乎无效，部署可复现性受限。纠错会引入新插入错误，实际需配合置信度或过滤。

