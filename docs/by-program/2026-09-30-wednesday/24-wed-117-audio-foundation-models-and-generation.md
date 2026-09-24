# Audio Foundation Models and Generation

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：5
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场横跨音频—语言模型骨干、端侧小模型、文本到音频生成/编辑，以及对语音基础模型微调评价方法的反思。状态空间模型（Mamba-2）被用作音频—语言骨干，强调与音频编码器联合微调、紧凑信息丰富的 token，以及指令跟随监督对推理能力的提升；同时出现面向端侧推理的开源小型音频语言模型族。

生成侧，无训练精确音频编辑（FreeSonic）用解耦注意力与反演—反向流程在 Rectified Flow TTA 上编辑；在线 GRPO 与大音频语言模型奖励把强化学习引入 TTA（Resonate）；舞蹈到音乐则用体裁自适应节奏与上下文对齐的扩散 Transformer。

最后一篇警示：监督微调上的小幅增益往往高度依赖具体预训练检查点与随机种子，未必抬高“可达成性能天花板”，促使社区重新审视“更好的 SFT”与“更好的匹配”之别。

## 论文技术总结

# SAM: A Mamba-2 State-Space Audio-Language Model

- 论文编号：639
- 报告人：Taehan Lee
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/lee26d_interspeech.pdf

## 问题
Transformer 音频语言模型算力随序列长度二次增长。Mamba 等 SSM 在语言与图像理解中已显示潜力，但在音频–语言模型中如何与音频编码器交互、是否需要端到端微调、以及长未压缩 token 是否真正有利，尚缺系统表征级分析。

## 方法
SAM：EAT-base 音频编码器 → 两层 MLP 连接器 → 预训练 Mamba-2（130M/780M/2.7B）作 LLM。连接器对比 (a) 沿频率维拼接压缩为 64 token；(b)/(c) time-major / frequency-major 保留更长序列并插入 “&&” 分隔符。在 OpenAQA 上按 LTU 四阶段课程 + LoRA（in_proj/out_proj）训练，自回归 caption 交叉熵。另构 OpenReasonAQA（基于 ReasonAQA 的 BQ/MCQ，约 3.8M）强化指令跟随与推理。

## 实验与结果
SAM-2.7B（r=256, concat）AudioSet mAP 21.1、AudioCaps SPICE 17.6，可匹敌或超过更大 7B Transformer ALM 与 ssLALM-2.8B。联合微调音频编码器优于冻结；更小 SSM 对应更低 τ-effective rank、更高 token 相似度，且尺寸匹配的编码器迁移效果最好。未压缩长序列 (b/c) 未稳定超过压缩 (a)，长序列增加状态更新负担。OpenReasonAQA 使 MMAU-Sound 从约 22.8 升至 56.8（SAM+OR-2.7B），超过 Gemma3n-4B 的 sound 设置。

## 结论
Mamba-2 可作为参数更少却有竞争力的 ALM 骨干；实践上应联合微调编码器、优先紧凑信息丰富的音频 token，并用结构化 BQ/MCQ 监督解锁推理。未来拟探索 SSM–Transformer 混合结构。

## 点评
贡献不只是换骨干，而是用有效秩、编码器互换与连接器消融把“SSM 固定维状态瓶颈”说成可检验的设计原则：编码器会按容量压缩表征，盲目拉长序列未必帮 SSM。相对常见冻结编码器或堆长上下文的路线，这组结论更贴 SSM 归纳偏置。局限是主表仍偏描述/分类，强推理依赖额外数据配方；Clotho 等上并非全面 SOTA，混合架构是否补足全局交互仍待验证。


# Samsone: A Family of Open Small Audio Language Models for On-Device Inference

- 论文编号：763
- 报告人：Michal K. Grzeszczyk
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/masztalski26_interspeech.pdf

## 问题
LALM 规模大、成本高，隐私与低延迟场景需要可端侧运行的 Small Audio Language Models（SALMs，本文定义为 <1B）。现有 Pengi、Mellow 等 SALM 推理能力与真实手机部署、开源可复现实验仍不足。

## 方法
标准 ALM：Whisper-Tiny 编码器 → Mellow 式非线性 projector（两层 Linear+GeLU、残差与 LN）→ SmolLM2（135M/360M）解码。音频帧嵌入时序平均池化为每样本 50 token；可训练 SEP token 分隔多段音频与文本。尺寸优化：(1) 词汇削减（小写 ASCII、过滤稀有 token，去掉约 15042 词，降约 8.7M 参数）；(2) 深度剪枝（99M 版去掉最后 10 层，30→20 块）。变体：Samsone-99M / 134M / 356M。数据：ReasonAQA + AudioSkillsXL；对 ReasonAQA 多选题随机置换选项以纠正答案偏向；单阶段训 100 epoch（每 epoch 20 万样本），除 LM embedding 外全可训；XNNPACK/ExecuTorch 导出端侧权重。

## 实验与结果
MMAU：99M/134M/356M 平均 Test 约 58.13 / 61.33 / 62.00，均超 Mellow（53.34），134M 可与更大 LALM 竞争；MMAU-Pro 相对 Mellow 约 +34%–36%。ClothoAQA 与 entailment（CLE/ACE）上优于或持平 Mellow；AudioCaps SPICE 低于 Mellow（归因训练中 AudioCaps 占比更小），Clotho SPICE 更好。消融：换 AST、GPT-2 或线性 projector 均降 MMAU。Galaxy S25 Ultra：生成约 39–125 tok/s（356M→99M）。局限：重度 AQA 微调损害通用语言能力；以参数量代理效率、未做 GPU/NPU 硬件优化。

## 结论
开源 Samsone 系列在同尺寸 SALM 上刷新 MMAU 等表现，并给出手机实时推理与可扩展尺寸谱。未来可探索量化大模型与硬件加速。

## 点评
主线是“公开数据 + 词汇/深度剪枝 + 端侧导出”，把 SALM 从纸面精度推向可跑的 Android 应用，工程闭环完整。相对只堆更大 LLM 的路线，强调 <1B 与实机 tok/s。脆弱点在于 caption 并非全面领先、通用语言能力被 AQA 微调侵蚀，且效率叙事仍偏参数量而非精度–内存曲线。


# FreeSonic: Training-Free Temporal-Aware Decoupled Attention for Precise Audio Editing

- 论文编号：1121
- 报告人：Yuxuan Jiang
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/jiang26d_interspeech.pdf

## 问题
文本条件音频编辑需同时满足时间一致性（只改目标段）与背景保持（重叠声源下非编辑区不变）。现有反演/全局条件方法改一处常牵动整段；训练式方法依赖复杂三元组与专用结构，成本高、灵活性差。

## 方法
基于 TangoFlux（Rectified Flow + MM-DiT）的免训练框架 FreeSonic。(1) 优化 RF 反演–重建，为后续编辑提供稳定结构。(2) 反演前 5 步聚合 double blocks 的 text–audio attention，阈值+膨胀平滑得时间掩码 M，定位待编辑段。(3) 在 single blocks 做三阶段 Scheduled Attention Decoupling：早期按 δ（0.85→1.0）混合源/目标 KV，并用 M 在非编辑区强制注入源 KV；中期 δ=1 且保持掩码；后期去掉约束做全局协调。(4) Task-Oriented Noise Injection：仅在 M 内对潜变量加可调度噪声，便于删除与非刚性替换。推理用 RF-Solver、25 步；噪声强度按 Add/Remove/Replace 分别为 0.1/0.4/0.25，截止步 t1=5。

## 实验与结果
基准：AudioCaps / AudioSet Strong 等构建的 Add(1300)、Remove(1300)、Replace(750)。对比 SDEdit、AudioEditor、ZETA、训练式 SAO-Instruct。FreeSonic 多数客观指标领先（如 Add FAD 1.55、Remove FAD 1.95、Replace CLAP 0.424）；主观 Quality/Relevance/Faithfulness 整体强。消融去掉掩码、改全量 KV 替换或去掉噪声注入均变差。固定 NFE=150 时 RTF 约 0.854，优于多数训练无关基线。

## 结论
免训练下用 RF 反演 + 注意力时间定位 + 调度解耦 + 任务噪声，在保背景与局部编辑间取得更好平衡，并在多种编辑任务上达到高保真与较高效率。

## 点评
抓住音频“可加性/重叠”导致全局反演难局部改的本质，把 MM-DiT 的跨模态注意力当作时间定位器，再用掩码约束 KV，比纯改文本条件更可控。相对训练式编辑省数据与微调。风险在于掩码依赖早期注意力质量与阈值、强依赖 TangoFlux 骨干，复杂重叠或弱对齐文本时定位可能漂移。


# Resonate: Reinforcing Text-to-Audio Generation via Online Feedback from Large Audio Language Models

- 论文编号：1823
- 报告人：Xiquan Li
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/li26ba_interspeech.pdf

## 问题
TTA 上已有 RL 多采用离线 DPO，并以 CLAP 作奖励：偏好数据与策略脱节易分布漂移，CLAP 有 bag-of-words 倾向，奖励偏粗、与人对齐不足。在线 RL 与更细粒度奖励在 TTA 中仍少见。

## 方法
Resonate：MeanAudio 风格 Flux Transformer（16 MMDiT + 36 DiT，470M），FLAN-T5 条件，先在约 3.7M 对/1 万小时语料上 Conditional Flow Matching 预训练。再将去噪建成 MDP，用 Flow-GRPO：对每条 prompt 采 G 条轨迹，组内标准化优势，裁剪策略比 + KL 到参考策略；确定性 ODE 改为等价边缘的 SDE 采样以引入探索。奖励用 LALM（训练期 Qwen2.5-Omni）对 AQA 问题“音频是否包含文本描述事件？”的 Yes/No 归一化概率（AQAScore）；评测用另一模型 Qwen3-Omni-Instruct 降奖励黑客风险。后训练：AudioCaps 训练 prompt，G=24，a=0.7，β=0.04，1000 步。

## 实验与结果
TTA-Bench Accuracy（1500 prompt）：Resonate-GRPO 相对预训练全面提升（AQAScore 0.651→0.737，PQ 5.923→6.064，CLAP 0.476），并在多项上达 SOTA；主观 OVL 3.86、REL 3.83。消融：DPO/SFT 增益有限或降质量；直接 GRPO 优于 SFT+GRPO；AQAScore 奖励总体优于 CLAPScore；噪声 a=0.7、更大 G 更稳。25 NFE 推理。

## 结论
在线 Flow-GRPO + LALM 细粒度奖励可同时提升 TTA 音质与语义对齐；Resonate（470M）在 TTA-Bench 上达到新 SOTA。

## 点评
把“离线偏好 + CLAP”两条瓶颈一起拆：在线组相对优势缓解分布漂移，LALM-AQA 奖励补时间/组合推理。与图像 Flow-GRPO 同构迁移到音频较自然。需警惕奖励模型与评测模型虽不同仍属同类 LALM 家族；SDE 噪声与 G 需调，噪声过大可奖励黑客；SFT 在嘈杂 AudioCaps 上伤音质，说明后训练数据质量仍关键。


# GACA-DiT: Diffusion-based Dance-to-Music Generation with Genre-Adaptive Rhythm and Context-Aware Alignment

- 论文编号：2348
- 报告人：Jinting Wang
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/wang26da_interspeech.pdf

## 问题
Dance-to-music（D2M）需节奏一致与帧级时间对齐。已有方法常用全局运动特征或二值化关节节奏，丢失细粒度运动、跨舞种鲁棒差；特征下采样还造成舞蹈节奏嵌入与音乐潜变量长度错位，对齐不足。

## 方法
GACA-DiT（约 56M）：(1) Genre-Adaptive Rhythm Extraction（GARE）：由姿态差分得运动幅度，多尺度 Gabor 小波建模时间动态，MLP+softmax 得关节自适应权重，再构多尺度相位直方图刻画空间运动分布，经时间注意力融成节奏嵌入 R。(2) Context-Aware Temporal Alignment（CATA）：将 R 切成 Tm 段，用可学习 context queries 对段内帧做注意力池化，得到与音乐潜变量同长的 ˜R。(3) I3D 视频语义特征 V 与 ˜R、时间步共同条件化 DiT，Conditional Flow Matching 学速度场；DiffRhythm VAE 编解码波形。训练 5 s/44.1 kHz，32 步 Euler，CFG=4。

## 实验与结果
AIST++ / TikTok 上相对 D2M-GAN、CDCD、LORIS、MotionComposer：AIST++ BCS 98.13、BHS 98.72、F1 98.47、FAD 20.14 等多项最优；TikTok BCS 91.55、F1 91.21 等亦领先。消融逐步加入小波、直方图、自适应加权与 CATA 指标递增；GARE 优于 ST-GCN 与 LORIS 式节奏特征。20 人 MOS：节奏一致性与整体质量中位数更高、分布更集中。

## 结论
细粒度、舞种自适应节奏表征 + 查询式跨模态时间对齐，使扩散式 D2M 在客观对齐/美学与主观评价上全面超过先前 SOTA。

## 点评
把“粗节奏”和“长度错位”拆成两个可模块化补丁，GARE 用时–空互补特征、CATA 用可学习查询对齐下采样，问题定位清楚。参数量远小于若干大基线却指标领先，说明条件表征质量比堆模型更关键。潜在脆弱点：依赖姿态检测质量与舞种覆盖；TikTok FAD 未全面领先；短 5 s 片段设定外的长视频对齐未充分验证。


# Rethinking Speech Foundation Model Fine-tuning: Better SFT or Better Match?

- 论文编号：2436
- 报告人：Wangjin Zhou
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26i_interspeech.pdf

## 问题
下游分类上常把单一预训练 checkpoint 下的小幅 SFT 增益解读为“方法更好、天花板更高”，却默认 SFT 相对优劣在同类预训练实例间稳定。实际上骨干、预训练数据与配方交互强烈，单 checkpoint 结论可能缺乏外部效度。

## 方法
把 SFT 视为 capacity elicitation：配方差异主要反映对特定 checkpoint 的 elicitation match（激活可靠性），而非普遍抬高上限。在 FEATURE MODE（末层 / 倒数第 4 层 / 层加权和）与 FREEZE MODE（全微调 / 冻 CNN / 冻 CNN+前 N=4 层）上构造 8 种配置，作用于 wav2vec 2.0、HuBERT、WavLM 共 9 个 checkpoint；在 SUPERB 的 IC、ER、SID 上评测。用 McNemar 检验定义相对最优的 top-group；全矩阵默认 seed 1337，并对三个 base 模型额外用 seed 2048/7395。

## 实验与结果
表 2/3 显示 top-group 配方随 checkpoint 变化，同架构同规模但预训练数据不同时排序可翻转；部分“常进 top-group”的配方在个别 checkpoint 上严重 under-activation（异常低分仍完成训练）。多 seed 下同一配置可在 fully activated 与 under-activated 间双向切换。hubert-large 在 ER 上八种配方统计不可分，说明有时配方边际效应很小。约一万 GPU 小时（H20）。

## 结论
统计上“最优/同组最优”的 SFT 配方依赖预训练实例与 seed；表观增益常是激活匹配，而非普适更高天花板。应跨多 checkpoint 与多种子评估。

## 点评
把“方法进步”与“碰巧激活某 checkpoint”拆开，用 top-group 不稳定性与 seed 双向翻转直接打穿单点对比的外部效度，对 SUPERB 式对比实验很有警示意义。局限是配置空间仍沿特征层/冻结轴离散采样，未覆盖学习率等更广超参；结论偏方法论，不给出新 SOTA 配方。

