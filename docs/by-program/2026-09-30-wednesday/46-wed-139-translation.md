# Translation

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：12
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从同声传译自动评分、多语 Indic→英语直接 S2ST、重音跨语迁移、思维链语音翻译是否真用语音，到台语—中文字幕语料自动构建与非洲野外语音识别基准。

焦点从“语义准确”扩展到评分量表对齐、发音动作空间统一、词汇重音保留，以及对声学线索的真实依赖程度。数据侧强调低资源与野外噪声，用多模态半监督与领域纵向基准揭示现代模型的真实差距。

## 论文技术总结

# Rubric-Aligned Disentangled Evaluation of Human Simultaneous Interpreting

- 论文编号：1105
- 报告人：Ziyu Zhang
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26o_interspeech.pdf

## 问题
人工同传（SI）专业评测用分析性量规分开意义传递、表达与时延，但缺少面向量规、句段级的自动指标。MT 标量指标与 LLM 提示评分易把多维坍成单一质量信号。

## 方法
构建 1,101 段专业双评注 SI 语料（LQ/EXP/LAT，0–3；talk 级划分，En↔Zh）。焦点为文本侧 LQ 与 EXP。在 COMET-KIWI 上用 LoRA + 双独立回归头，残差预测与 MSE+方差正则；对比冻结 COMET-KIWI、单头标量微调、结构化 LLM 零/少样本提示等。LAT 留待多模态。

## 实验与结果
人评者间绝对一致偏低（LQ/EXP Pearson 约 0.21/0.27），一致性 ICC(3,1) 约 0.34/0.43。Dev 上 LLM 提示与人相关近零，且 LQ–EXP 耦合 corr≈0.90（人约 0.56）；标量微调亦近零。Test：双头模型 Pearson LQ 0.388、EXP 0.301，显著优于冻结 COMET-KIWI（0.219/0.175）；预测维间相关 0.529，接近人类耦合。错误多在多步骤程序性内容的步骤完整性。

## 结论
监督结构（而非仅骨干容量）是瓶颈：提示与标量监督坍缩量规维度，双头结构化监督可恢复相对人类一致性范围内的稳定排序信号，服务形成性反馈而非替代认证。

## 点评
把问题从“换更大 LLM”转到“量规监督是否可分”，并用相同骨干隔离监督结构，实验设计干净。绝对相关不高但对照人–人天花板后解读合理。文本-only 对 EXP 是下界；LAT 与客观时延几乎无关，说明“感知同步”本就不是简单 onset 差，多模态是自然下一步。数据集规模与中英双向限制外推，但对 SI 自动评测方向很清晰。


# ARTIST: Universal Articulatory Space Modeling for Multilingual Indic-to-English Speech-to-Speech Translation

- 论文编号：2384
- 报告人：Khushal Yadav
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yadav26_interspeech.pdf

## 问题
端到端 S2ST 大模型（如 SeamlessM4T）参数与双语数据需求大，Indic 低资源方向易过拟合与长序列幻觉。需要更强结构先验以跨语言共享、在极少数据下稳定翻译。

## 方法
ARTIST（166M）：先用 VQAE 在源/目标发音特征上预训练共享离散发音空间（码本 K=20）；S2A 用 Conformer 编码器 + 中间层 CTC 对齐源发音单元，Convolution-Augmented Differential Transformer 自回归预测目标发音 token；VQAE 解码后经 A2Mel + HiFi-GAN 合成。在 BhashaAnuvad 11 个 Indic→英方向上训练（短句 3–20s），长句 OOD（20–50s）评测。

## 实验与结果
相对 1.2B SM4T，各资源档 BLEU/chrF/COMET 普遍更高（如 Hindi 22.14 vs 13.21 BLEU；Gujarati 仅 10h 达 16.91 BLEU）。消融：去中间 CTC 则 BLEU 崩至 1.07；印地单语相对多语从 22.14 降至 12.95；去掉解码器卷积模块亦降分。JES（BLEU/(小时×十亿参））相对基线提升约 23×–231×。

## 结论
通用发音瓶颈促进跨语言脚手架，参数与数据效率高，并改善长音频稳健性。中间 CTC 与局部卷积对稳定训练与发音连续性至关重要。

## 点评
把“生理发音空间”做成极端压缩的共享目标，比纯声学离散单元更适合 Indic 多语少数据；中间 CTC 消融的灾难性结果说明早期语音内容解耦几乎是硬前提。对比锚定在 SM4T 且评测偏长句，对 cascade/专精 S2ST 的相对位置需读者自行外推；发音特征依赖 IMS Toucan 等前置估计，错误可能沿链路放大。


# Evaluating and Preserving Lexical Stress in English-to-Chinese Speech-to-Speech Translation

- 论文编号：2321
- 报告人：Yuchen Song
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/song26f_interspeech.pdf

## 问题
S2ST 语义与自然度已较强，但跨语言词汇重音/强调传递仍弱；汉语为声调语言，英语中心强调检测难直接迁移，且缺带重音标注的中文数据与可靠自动评测。

## 方法
自建中文重音语料（2 名普通话说话人，418 句、1883 条、2.74h）。Syl-BiLSTM：XLS-R 多层融合 + 音节级池化 + BiLSTM 做字级重音检测。CETS：EmphaClass 检英侧重音，Whisper+fa-zh 对齐中文，Syl-BiLSTM 检目标重音，SimAlign 对齐后判是否传到对应语义位置。S2ST：StressTransfer（Whisper+Qwen2.5-3B LoRA）出带 stress 标签译文，CosyVoice3 LoRA 在重音数据上微调可控合成。

## 实验与结果
Syl-BiLSTM F1 0.91，远超 Frame-Linear/Frame-BiLSTM。Proposed CETS-W/S 60.80%/58.30%，基线约 16–26%；BLEU 47.35 与 StressTransfer+Base 接近，UTMOS 最高 3.68。主观成功转移率 78.33% vs 基线约 12–25%；CETS 与人判 Pearson r=0.52，绝对一致约 79%。

## 结论
中文重音数据 + 音节级检测 + 可控 TTS 可显著提升英→中强调传递，同时保持翻译质量与自然度；CETS 可作为自动代理。未来扩展更多说话人与声调语言。

## 点评
把“评测瓶颈”和“合成可控”一起打通，CETS 的词级/句级双粒度比单纯听感更可诊断。说话人仅 2 人、TTS 用固定默认音色，强调可控性可能部分依赖说话人特异性；CETS 链路依赖 ASR/对齐/检测多模块，错误会耦合进指标，与人相关中等需谨慎解读。


# Listening or Reading? Evaluating Speech Awareness in Chain-of-Thought Speech-to-Text Translation

- 论文编号：800
- 报告人：Federico Costa
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/romerodiaz26_interspeech.pdf

## 问题
CoT/多轮 S2TT 假设翻译阶段同时可见语音与转写，从而抗 ASR 误差传播并利用韵律；该假设是否成立缺少系统验证。

## 方法
基于 SALAMANDRATA-7B + 冻结 mHuBERT 离散单元；对比 CoT 与 self-cascade。训练变体：BASE（纯 CoT）、DUAL（25% CoT + 75% Direct）、NOISY（25% CoT 样本注入损坏转写且不对转写算损失）。用 Value Zeroing 做模态归因；控制替换转写片段测鲁棒性；CONTRAPROST 测韵律敏感；FLEURS 测通用翻译质量。英→六种欧洲语言。

## 实验与结果
BASE 的语音贡献近零，行为接近 cascade；DUAL/NOISY 语音归因升至约 1.54×/2.24×。转写噪声下 BASE 的 CoT 与 cascade 掉速几乎相同；NOISY 在高至 30% 损坏下下降明显更缓。CONTRAPROST Global：NOISY-COT 最高（AVG 17.65）。FLEURS 上干预不伤质量，DUAL 整体最好，NOISY-COT 可反超 cascade。

## 结论
默认 CoT  largely 在“读转写”而非“听语音”；混合 Direct 与注入噪声转写可提高语音依赖、抗错与韵律利用。未来可组合 DUAL+NOISY。

## 点评
用归因、噪声鲁棒、韵律三维拆穿 CoT 叙事，比只报 BLEU/xCOMET 更有解释力。NOISY 仍主要依赖转写却能纠错，说明“语音作纠错信号”而非替代文本。局限：仅英→欧语、DSU 表示可能已损韵律细节；CONTRAPROST 绝对分仍低，语音整合仍有很大空间。


# A Multimodal Semi-Supervised Framework for Automatic Construction of a Cross-Lingual Taigi Speech-Chinese Subtitle Corpus

- 论文编号：2096
- 报告人：Yuan-Fu Liao
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cho26b_interspeech.pdf

## 问题
台语（Taigi）标注稀缺；大量在线视频是台语语音 + 画面硬编码繁中字幕、无独立字幕文件，常规 ASR/OCR 难以自动建库。

## 方法
多模态半监督：预处理用 PaddleOCR 抽字幕并按时码切成（文本、帧、语音）三元组；trimodal AVLM（SigLIP + Whisper Large-V2 台语微调 + Qwen2.5，早期融合，LoRA）与 OCR 各出候选；CER 过滤共识对后，用 Qwen2.5-VL 按错误模式提示并参照原图融合伪标签，迭代微调 AVLM；强制对齐精修边界。下游用所得语料微调 Whisper 与 Qwen2.5-14B 翻译。

## 实验与结果
PTS-Taigi 监督：AVLM CER 7.46%，优于 VLM 10.26%、ALM 35.29%，对模糊/噪声更稳。Golden Set 迭代：AVLM CER 36.8%→9.3%（融合约 9.4%），提取量升至池中约 87%（434h）。再扩得约 860h 语料：Whisper 台语→中文 CER 57.8%→37.8%；约 590k 平行句微调后 BLEU 0.2016→0.4033。

## 结论
音视频语言融合 + VLM 共识伪标签可规模化构建跨语言台语–中文字幕语料，并显著提升下游转写与翻译；方法可迁移其他低资源场景。

## 点评
针对“语音语言≠字幕语言”的硬编码设定，用音频作视觉识别约束、用 VLM 化解 OCR/幻觉，工程闭环完整。Golden Set 域外起分很差、迭代后逼近监督，说明半监督主要在修域移。伪标签仍依赖 OCR–AVLM 共识阈值，极端视觉损坏时召回会掉；台语 ASR 再对齐中文建 MT 语料会引入二次误差。


# AfriVox-v2: A Domain-Verticalized Benchmark for In-the-Wild African Speech Recognition

- 论文编号：3140
- 报告人：Busayo Awobade
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/awobade26_interspeech.pdf

## 问题
非洲语言/口音在 ASR 基准上覆盖不足；既有评测偏朗读、域粗、模型过时，难反映噪声自发场景与垂直行业词汇（金融、医疗、农业等）及数字/命名实体风险。

## 方法
AfriVox-v2：聚合 Waxal、Africa Next Voices、新建 Intron-YT（公开多媒体自发对话，母语者转写+元审）等，约 14+ 语种；Gemini-3 多标签域标注（10 域含 Numbers/Named Entities），人工抽检（高精度语约 precision 42%/recall 70%）。评测 Omni-CTC 300M/1B/7B、Gemini 3 Flash、Sahara-v2；报告 WER、域条件 WER、EWER/NWER。

## 实验与结果
自发语音整体更难，但跨语种/模型变化不均。AfriVox-v2 平均 WER：Sahara-v2 最低 20.49，优于 Omni-CTC-7B 27.85 与 Gemini 3 Flash 26.59。域上电信/体育等错误更高；Sahara-v2 各域最低（如农业 16.11）。数字与实体仍难（最好约 NWER 20.32、EWER 23.11）。作者指出部分语种 v2 反优于 v1，可能反映训练数据重叠而非真泛化。

## 结论
域垂直与 in-the-wild 评测暴露平均 WER 掩盖的部署风险；区域优化模型可胜过更大通用模型。基准拟推动更包容的非洲语音 AI。

## 点评
把“野生对话 + 行业域 + 实体/数字”做成评测轴，比只比朗读 WER 更贴近落地。域标签噪声（precision 约 42%）使域结论宜作趋势；作者机构自研 Sahara-v2 虽称同条件评测，读者仍需关注利益冲突与数据重叠可能抬高分。覆盖仍只是非洲语言的一小部分。

