# Spoofing and Deepfake Detection 2

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：4
- 论文数：11

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从“二分类是否够用”转向泛化、可解释、可追溯与主动防御。SSL 前端检测器仍占主导，但工作重点转向域不变/攻击特异特征解相关、任务感知剪枝蒸馏、自蒸馏预训练与证据子空间量化，以应对未见攻击与资源受限部署。

音视频联合检测强调局部伪造痕迹、参考身份锚点与物理一致性（说话距离—能量耦合），补足单纯唇同步在动态场景的脆弱性。唱歌声伪造与局部篡改则暴露“语音检测器直接迁移”的失败模式。

基准与推理框架（FakeSound2、HIR-SDD）推动 localization / traceability / generalization 与类人推理解释；自嵌入隐写则给出无训练的主动防御路径，与被动检测形成互补。

## 论文技术总结

# Improving Generalization in Speech Deepfake Detection via Orthogonality-Constrained Common-Specific Feature Decorrelation

- 论文编号：1483
- 报告人：Donghee Kim
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26l_interspeech.pdf

## 问题
端到端 deepfake 检测（RawNet2/AASIST 等）在域内 EER 极低，但 ERM 训练易过拟合数据集伪迹，跨未见攻击、噪声与编解码时性能骤降。需要把“真伪共性线索”与“攻击/域特异线索”拆开，避免分类器依赖捷径。

## 方法
在 SSL-AASIST（wav2vec2.0 + AASIST）上，将谱/时图表示投影为 common 与 specific 两支：common 做 bonafide/spoof 主任务，specific 做 bonafide/TTS/VC 辅助分类；用余弦相似度平方作正交损失压低两支相关。总损失 L_main+L_aux+L_ortho。训练用 ASVspoof 2019 LA；评测含 19LA、21LA、21DF、ASV5、ITW；可叠加 RawBoost（LnL+ISD）。

## 实验与结果
RawBoost 下，Proposed（三损失）相对 baseline：21DF 6.64%→3.67%，ASV5 16.25%→14.39%，ITW 11.22%→8.84%；19LA/21LA 接近或略差。无增强时跨库平均 EER 约 12.83%→10.60%。消融显示仅加 aux 不够，ortho 对 OOD 关键。t-SNE 上 common/specific 聚类分离。

## 结论
作者认为正交约束的共性–特异性解耦可促使模型依赖更一致的真伪线索，从而提升未见域与攻击上的稳健性，且改动相对轻量。

## 点评
把域泛化里的 common/specific 正交直接接到 AASIST 图特征上，动机清楚：把静音时长等语料捷径赶到 specific 支。19LA 上偶有小幅回退说明解耦有代价；辅助标签粒度仍粗（仅 TTS/VC），更细攻击类型是否进一步帮助仍开放。


# Task-Aware Joint Pruning and Distillation for Efficient Audio Deepfake Detection

- 论文编号：1766
- 报告人：Miao He
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/he26f_interspeech.pdf

## 问题
SSL deepfake 检测器（常 300M+ 参数）难上端侧；ASR 等面向内容任务的剪枝/蒸馏直接搬到伪造检测时，高稀疏度下尤其 OOD 掉点严重。需要任务感知地保住伪造判别结构并迁移跨域知识。

## 方法
三阶段框架：（1）微调预训练 SSL 并算结构单元 movement score（MHA/FFN/CNN）作重要性先验；（2）Hard Concrete 可微结构化剪枝 + 增强拉格朗日满足目标稀疏度，配合跨域无标签蒸馏（19LA train、21LA、21DF、ITW），按 CKA 选代表层（如 {5,14,24}）多层蒸馏；（3）剪枝后 SSL 与 AASIST 后端联合微调。主干为 XLSR-AASIST。

## 实验与结果
相对稠密基线 317M/146.3G，90% 稀疏时约 31.9M/23.3G（约 6.3× FLOPs）。75% 稀疏：ITW 8.43%、ASV5 17.75%、FoR 10.51%，优于 Finetune/HJ/Hybrid 剪枝，并在部分 OOD 上优于稠密基线（ASV5 19.92%、FoR 14.89%）。消融去跨域蒸馏后 21LA/ITW 等显著变差；去 movement 引导也有损失。摘要称多数据集平均掉点约 1.30%。

## 结论
作者认为任务感知剪枝与跨域蒸馏联合，可在激进压缩下保持伪造检测精度与泛化，具备端侧部署潜力。

## 点评
把“伪造相关结构”用 fine-tune movement 显式优先保留，并用无标签跨域蒸馏补监督，针对 deepfake 而非 ASR 压缩是关键点。部分 OOD 优于稠密模型提示过参数化过拟合，但极端 90% 稀疏在 FoR 等上仍明显回退，端侧部署仍需按场景选稀疏档。


# ADD-DINO: A Two-Stage Self-Distillation Framework for Audio Deepfake Detection

- 论文编号：1847
- 报告人：Zhaorui Sun
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sun26g_interspeech.pdf

## 问题
SSL+后端的 ADD 依赖大量标注，且易过拟合特定伪造类型，跨域与未见合成器时稳健性差。掩码式 SSL 侧重局部预测，未必最适合捕获真伪一致性线索。

## 方法
ADD-DINO 两阶段：Stage1 在约 100 万无标注音频上做非对比 teacher–student 自蒸馏——teacher 吃全局长段、student 吃噪声增强的局部短段，对齐预测分布，teacher 用 EMA 更新；骨干为 XLS-R/WavLM 等 + AASIST 图模块。Stage2 给预训练 teacher 换新分类头，在少量有标数据上微调。评测 ASVspoof 2019/2021、In-the-Wild、DFADD 等，以及 CosyVoice、F5-TTS 等未见合成器。

## 实验与结果
少标微调时，如 XLS-R 骨干 20% 标签：19LA EER 0.55（全监督基线同比例 1.19），接近更高标注比例表现。跨域与未见合成器上相对基线：摘要称 EER 相对降 19.99%、准确率升 22.7%。多骨干对比表显示低标注比例下 ADD-DINO 普遍优于同骨干全监督微调。

## 结论
作者认为全局–局部一致性自蒸馏可在标签稀缺下逼近全监督，并提升跨域与未见伪造的泛化。

## 点评
把 DINO 式非对比蒸馏接到 ADD，用“长全局 vs 短局部”对齐伪造痕迹，比单纯掩码重建更贴检测目标。未见合成器测试用 ACC（全假样本）与标准 EER 混用，跨表比较时需注意协议差异。


# FakeSound2: A Benchmark for Explainable, Traceable, and Generalizable Deepfake Sound Detection

- 论文编号：1157
- 报告人：Zeyu Xie
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xie26_interspeech.pdf

## 问题
通用音频 deepfake 检测多停在片段级真假二分类，无法回答何时被改、如何被改、来自哪个源，且对未见生成器易崩溃（文中称操纵类型准确率可由 93.1% 掉到 32.4%）。需要面向可解释、可追溯与可泛化的诊断基准，而非只比二分类分数。

## 方法
提出 FakeSound2 基准：覆盖 6 类操纵（Generation、Editing、Inpainting、Separation、Splicing、Addition）与 12 个源，含 clip-wise 与 frame-wise；评测定位（Accidentify、F1segment）、溯源（Accsource）与操纵类型识别（Accmanipulation），并区分 in-domain / out-of-domain。资源公开于项目页。

## 实验与结果
Table 2：域内定位普遍很强（多类 Accidentify/F1 近 100%），但域外操纵类型准确率崩溃（如 Generation 99.40%→4.23%，Editing 87.96%→0.00%，Inpainting 99.75%→46.49%）。结论是现有模型擅定位、弱解释与弱泛化，易记生成器伪迹。

## 结论
作者主张把 FakeSound2 当作诊断工具：稳定追问模型是否理解伪造本质，而非追逐当前源上的排行榜分数。

## 点评
把 DSD 从“判真假”拉到 how/when/where，对取证叙事有价值；域外操纵类型崩盘的诊断结论比单一 SOTA 数字更有信息量。基准本身依赖当前 12 源构造，生成技术迭代后仍需持续扩展。


# Evidence Subspace Projection: Measuring How Much Evidence Explains Deepfake Detection in Self-Supervised Speech Models

- 论文编号：3210
- 报告人：Yixuan Xiao
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xiao26c_interspeech.pdf

## 问题
SSL 前端驱动的 ADD 域内很强、域外常塌，不清楚决策究竟依赖攻击类别、编解码、静音结构等哪类证据。既有解释常把前端与后端缠在一起；需要把冻结 SSL 前端单独拿出来，定量度量“多少决策可由某类证据解释”。

## 方法
Evidence Subspace Projection：由 Transformer FFN 神经元激活模式构造标签向量（真伪、攻击等），经 one-vs-rest 残差得到决策轴；再把决策向量投影到各证据子空间，得到解释比例标量。在 raw / fine-tuned / post-trained 设定下评估 XLSR、HuBERT 等，训练/测试覆盖 ASVspoof 2019/2021/5。

## 实验与结果
微调可降低 within-spoof 组对决策轴的对齐（E_rank），XLSR EER 整体低于 HuBERT（如训 ASV19：ASV19 0.25 vs 0.53；ASV5 17.98 vs 22.47）。低 E_rank 与低 EER 在 22 组中 18 组一致；例外分析显示聚合 EER 可被 VC 多数类拉低，掩盖 TTS 弱点。Post-training 进一步压低部分 within-spoof 对齐。

## 结论
作者认为该方法可复现并细化既有发现：冻结前端已编码大量真伪相关结构，微调/后训练会重塑决策与证据因素的关系，可用于诊断模型是否过拟合伪迹。

## 点评
把“解释力”收成可投影的标量，比纯可视化更可比较，尤其适合拆开 SSL 前端贡献。E_rank 与 EER 偶发背离提醒：证据对齐是诊断量，不等于检测分数；证据因子库本身也依赖元数据完备性。


# Towards Robust Speech Deepfake Detection via Human-Inspired Reasoning

- 论文编号：1289
- 报告人：Dmitrii Korzh
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dvirniak26_interspeech.pdf

## 问题
现有 SDD 跨域/跨生成器泛化弱，且缺少人类可感知的推理式解释。需要把 Large Audio Language Model 的链式推理与真人标注理由结合，既抬检测又给可审理由。

## 方法
提出 HIR-SDD：收集人类问卷理由与评论，过滤低准确标注者，经 Qwen-32B 整理为推理轨迹；得到约 124,410 条标注覆盖 41,414 段音频（37 名标注者）。用 SALMONN-7B 等 LALM 在 hard-label 与 reasoning 训练集上微调，并与 Wav2Vec2-AASIST 对照。

## 实验与结果
Test-1-HL 上 SALMONN-7B（Train-2-HL）准确率 94.5、平衡准确率 88.6、F1 85.7，高于 Wav2Vec2-AASIST（约 92.9 / 84.0 / 76.7）。结合 Train-2-R 与 GRPO 等设定可维持相近或略优平衡指标；文中展示推理样本说明可给出可理解理由。

## 结论
作者认为人类启发推理数据能提升 LALM 检测，并提供对真伪判定的自然语言辩护，有助于可解释反欺骗。

## 点评
把“听感理由”系统化成训练信号，是解释性 SDD 的务实路径。风险在于推理轨迹经 LLM 改写可能偏离原始听感，且硬标签过滤已剔除错误类样本，评估可能偏乐观；跨未见生成器的泛化仍需更强协议。


# Physics-Aware Deepfake Detection via Distance–Speech Consistency

- 论文编号：1541
- 报告人：Kyeongrae Kim
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26m_interspeech.pdf

## 问题
音视频 deepfake 检测多依赖唇–语音同步，且面向静态正面说话视频；动态、野外场景下说话人移动、唇部线索退化时可靠性下降。需要与唇同步互补的物理约束。

## 方法
利用真实录音中语音能量随说话人–摄像头距离可预测变化、伪造常破坏该耦合：从视频估计距离，从语音提取距离相关声学量（如 SNR、C50），检验一致性以判真伪；可与唇同步检测器简单集成。在 DF24、AuViRe RealWorld 等野外数据上训练/评测，并构造强动态子集 DF-Dynamic。

## 实验与结果
DF-Dynamic 上 ROC-AUC：SpeechForensics 0.5096、AuViRe 0.5517、本文 0.7449。全文对完整集与消融有更多表；摘要称物理线索在动态场景有效，并与唇同步集成可跨数据集稳定增益。

## 结论
作者认为距离–语音物理一致性可作为动态说话视频的有效伪造线索，补充唇同步范式。

## 点评
把声学物理先验引入 AV 伪造检测，针对“野外动态”痛点明确。距离估计与房间声学假设在剪辑/多麦/强后处理视频上可能失效；与唇同步集成依赖各模态独立错误模式不完全重叠。


# MS-GNN: Multi-Scale Graph Neural Network for Detecting Local Audio-Visual Forgery Traces

- 论文编号：416
- 报告人：Ju Zhang
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26g_interspeech.pdf

## 问题
音视频伪造常只改短时窗（如替换一句口型/语音）；全局池化多模态特征会冲淡瞬时不一致（如唇同步错位）。需要显式保留局部痕迹并与全局语义交互。

## 方法
MS-GNN 将 AV 流切成窗口构图：自底向上聚合窗口到片段语义，自顶向下回传全局上下文细化局部证据；用窗口级辅助监督 + 视频级主监督训练，再聚合得全局表示。

## 实验与结果
LAV-DF：ACC 98.12%、AUC 99.81%，高于 Referee、DimoDif 等。FakeAVCeleb 与消融亦显示窗口监督与多尺度路径有益；效率表在 A800 上比较。

## 结论
作者认为多尺度图聚合配合窗口级监督更适合捕获局部伪造痕迹，提升 AV deepfake 检测。

## 点评
针对“局部篡改被全局池化淹没”的设计动机清楚，窗口辅助损失是关键。对跨数据集未见操纵的泛化正文数字相对次要；图构建与窗口长度选择可能敏感。


# Referee: Reference-aware Audiovisual Deepfake Detection

- 论文编号：1246
- 报告人：Hyemin Boo
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/boo26_interspeech.pdf

## 问题
音视频 deepfake 检测跨操纵方法泛化仍难。多数方法不显式利用“同一说话人真实参考”作为生物识别锚点，难以放大身份级不一致。

## 方法
Referee：用 one-shot 参考样本经 identity bottleneck 与 matching 模块建模说话人特异线索的关系一致性；辅助身份匹配损失（真–真同人 vs 伪造视为不同身份）；将参考感知身份 token 与目标 AV 特征送入 AV-Transformer 做检测。代码公开。

## 实验与结果
跨数据集：在 FakeAVCeleb 训练测 FF++，Referee AUC 79.78 / AP 91.00，优于多种无参考或不同训练源的 AV/视觉基线。域内与 KoDF 跨语言协议亦称达 SOTA；消融显示身份匹配设计有效。

## 结论
作者认为显式关联参考生物识别先验是可靠 AV 取证的关键方向。

## 点评
把说话人验证式 one-shot 锚点接到伪造检测，对“像某人但不一致”的攻击很对症。实际部署依赖可获得的干净参考；参考被污染或跨会话信道差时匹配模块可能误导。


# OPERA-Net: Octave-aware Phase-sensitive Enhanced Recognition Architecture for Singing Voice Deepfake Detection

- 论文编号：3341
- 报告人：Fengwei Ye
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ye26e_interspeech.pdf

## 问题
歌声伪造检测（SVDD）上，语音反欺骗器易失效：背景音乐干扰强，且幅度谱忽略相位不连续等伪造线索。

## 方法
OPERA-Net 双流：Phase-Consistent CQT（PC-CQT）建模瞬时频率导数以捕相位异常；Semantic-Guided Gating 用预训练 WavLM 语义先验过滤 PC-CQT，抑制 BGM、突出人声伪造痕迹。在 CtrSVDD 与 SingFake（T01/T02/T03）上评测。

## 实验与结果
CtrSVDD pooled EER 1.54%（A09–A13），优于 Fosafer 等挑战系统且为单模型。SingFake overall EER 4.72%（T01 3.12 / T02 4.85 / T03 4.92），优于 SingGraph 6.05% 与 AASIST/W2V2 变体。

## 结论
作者认为相位敏感表征加语义门控可在有伴奏的野外歌声上更稳地检出伪造，无需堆叠多 SSL 集成。

## 点评
把 SVDD 难点明确落在“相位+伴奏”，PC-CQT 与 WavLM 门控分工清楚。CtrSVDD 控制集与 SingFake 野外差距仍大；对极端混响/翻唱重制等未见条件还需更多压力测试。


# A Training-Free Proactive Defense Against Partial Speech Manipulation via Self-Embedding Steganography

- 论文编号：1822
- 报告人：Yigitcan Özer
- 程序：Tuesday 29 September 2026 / Spoofing and Deepfake Detection 2
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ozer26_interspeech.pdf

## 问题
部分篡改语音（仅替换短片段）使被动检测器随伪造占比下降而不可靠，定位与恢复也难。需要不依赖大规模训练的主动防御。

## 方法
自嵌入隐写：干净语音把自身压缩表示嵌回波形；接收端提取参考并经编解码式重建 R(y)，再与收到信号 y 用 mel-log 谱上的 DTW（余弦距离）对齐，路径平均代价 s_DTW 作操纵分数。复用现有音频隐写方法，无需为检测任务训练。在 AV-Deepfake1M 验证集音频子集上，攻击替换同说话人 1–2 个词的重合成片段做概念验证。

## 实验与结果
正文报告该主动方案可与被动防御互补；操纵处 DTW 路径偏离对角线、累积代价升高。抽取文本对完整量化表覆盖有限，但强调无训练、数据高效。

## 结论
作者认为自嵌入隐写可为部分 deepfake 提供可部署的主动检测与恢复线索，补被动系统短板。

## 点评
把隐写从版权水印转到“自参考完整性校验”，对短局部篡改很对症且免训练。脆弱点在攻击者察觉并破坏/重嵌水印，以及压缩自嵌入引入的可听失真与信道鲁棒性权衡。

