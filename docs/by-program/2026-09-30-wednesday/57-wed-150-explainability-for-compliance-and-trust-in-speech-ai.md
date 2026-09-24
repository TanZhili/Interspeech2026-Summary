# Explainability for Compliance and Trust in Speech AI

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Special Session
- Area：14
- 论文数：16

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本专场围绕语音 AI 的可解释性、合规与信任：深伪检测证据定位、说话人嵌入可听分解、情感描述符校正、多模态句嵌入诊断，以及分离/编解码/空间 SSL 内部机制探测；同时覆盖 SLM 越狱攻防、LALM 音文融合因果追踪、临床语音中的人群差异审计，与交叉注意力作为解释代理的限度。

方法谱从归因与因果干预（Integrated Gradients、因果掩码、causal tracing、影响函数样本级解释），到稀疏自编码器、因子化线性投影、可听组件分解，再到将 XAI 证据接入免训练多模态 LLM 生成自然语言说明。共同诉求是：解释须与决策因果相关、可被人核验，且不能用全局平均掩盖人口学/语言差异。

安全线与可解释线交织：多模态联合越狱远强于单模态；统一安全子空间跨模态转移拒绝向量。工程上，对稳定层注意力缓存等“解释驱动加速”开始出现。对从业者而言，本场强调：分数不够，必须说明“听了什么、在何处融合、对谁可靠”。

## 论文技术总结

# What Do Deepfake Speech Detectors Actually Hear?

- 论文编号：123
- 报告人：Vojtěch Staněk
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/stanek26_interspeech.pdf

## 问题
深度伪造语音检测器常只给分数，难说明证据在时间何处、依赖何种线索；同性能模型是否学到不同决策逻辑。

## 方法
对 WavLM Base+ 时齐帧表示做 Integrated Gradients，相对 bona fide 质心基线，层/维求和得时间归因；人工标注最高归因区的线索类型与局部性。检测器：AASIST、CA-MHFA、SLS，联合微调 SSL+后端。在 ASVspoof 5 上取 100 条（高置信正确/错误与边界）做语义标注，并用静音/高能音素/频谱/压缩掩码做因果验证。

## 实验与结果
EER：AASIST 4.06%、CA-MHFA 5.26%、SLS 3.98%；三分数 LR 融合 3.77%。语义上 AASIST 偏非语音/环境，CA-MHFA 偏局部音素伪影，SLS 偏词界与谱完整性。掩码：静音扰动重创 AASIST（FARb→99.99%）；压缩使三者 FRR 升。重压缩与 YourTTS(A28) 主导高置信错误。

## 结论
相近性能可依赖互补线索；IG+人工语义+掩码验证可回答“侦测器实际听什么”，并提示压缩伪影是共性弱点。

## 点评
把可解释性从定性例子推到结构化标注与因果消融，证据链完整。子集仅 100 条、标注主观；融合增益有限因共享压缩失败模式。


# LISE : Listenable Interpretable Speaker Embeddings

- 论文编号：537
- 报告人：Xiaoliang Wu
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wu26_interspeech.pdf

## 问题
ASV 说话人嵌入黑箱；属性探测需标注且常伤性能，高维稀疏表示又缺听者验证。需无标签、保性能且对人可听可分的分解。

## 方法
LISE 将冻结 x-vector/ECAPA 嵌入 \(e\) 分解为 \(K\) 个正交、非负权重成分：\(\hat e=Wc\)，损失为重建 + \(\lambda\|W^\top W-I\|_F^2\)。VoxCeleb2 说话人级均值嵌入训练；K≈35。听辨：按成分权重高低组 Type A / Non-Type A，熟悉后判候选归属。

## 实验与结果
Vox1-O：LISE EER x-vector 3.08%（原 2.30%）、ECAPA 2.10%（原 1.80%），优于属性监督 Luu 等（6.70%）并接近 PCA。听辨总体准确 83.9%，显著高于 PCA 59.1% 与 Iben 等 49.0%；35 成分中多数过 70%。半量数据训练仍稳。

## 结论
低维正交非负分解可在几乎不伤 ASV 的同时得到听者可分成分；未来可用于可控合成与偏差诊断。少数成分反映语言而非声线是局限。

## 点评
把“可听性”作为可解释性硬指标，相对仅声学相关更有说服力。成分语义仍依赖听者描述，非客观标签；VoxCeleb 多语噪声使部分轴混入语言模式。


# Explainable and Trustworthy Speech Emotion Recognition Using Confidence Score and Reinforcement Learning Rectified Speech Emotion Descriptors

- 论文编号：1683
- 报告人：Youjun Chen
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26r_interspeech.pdf

## 问题
可解释 SER 依赖音高/音量/语速/性别/年龄等 SED，但自动标注阈值统一、不可靠，且训练中无法据情绪标签纠错，解释可信度不足。

## 方法
基于 VIB-Emo 类 SER-SLM：MLP CEM 用最后隐状态估各 SED 置信并均值池化，按阈值筛可靠子集做 SFT；RNN SED Controller 采样保留/修改策略，交替更新——用情绪 CE 变化作奖励（类 GRPO 组归一）在线校正 SED。SpeechCraft 预训，IEMOCAP/MELD 自动 SED 后训。

## 实验与结果
置信筛选 + RL 校正优于无筛选/无校正；最佳（约保留 90% + RL）IEMOCAP 80.98%、MELD 64.11%，相对全量无校正基线绝对 +2.9%/+3.3%。单独筛选最优约 80% 保留；策略数 M=6 整体最佳。t-SNE 显示情绪簇更清晰。

## 结论
置信筛选与在线 SED 校正可同时提升 SER 精度与解释可信度。

## 点评
直面自动 SED 噪声，用“先选再纠”闭环贴合部署现实。信任主要靠准确率与可视化间接论证，缺少人工 SED 正确率评测；奖励仅看情绪 token，可能放过语义上仍错的 SED。


# FLiP: Towards understanding and interpreting multimodal multilingual sentence embeddings

- 论文编号：3315
- 报告人：Santosh Kesiraju
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kesiraju26_interspeech.pdf

## 问题
多语/多模态句向量压缩为单向量后难解释“装了什么”；现有线性探测多为非分解或英语中心，缺系统跨语跨模态诊断。

## 方法
FLiP：将嵌入映到词表分布的 log-linear 模型，\(W=AB\) 因式分解（隐含正则，可低秩）；目标最大化 bag-of-words 似然，可混合同句语音/文本或双语文本（\(\alpha\)）。推理取 top-k 词作关键词。训于 SONAR / LaBSE / Gemini 嵌入；MCV 英德法语音–文本，Europarl/Samanantar 平行文本。

## 实验与结果
SONAR 英：因式化全秩文本准确约 77%（非因式约 59%）；r=512 接近全秩。同语内语音–文本对齐较好；跨语呈英语偏置，远距离语（如 TA、TE）线性可恢复性下降。同设置下 SONAR 优于 LaBSE/Gemini。相对 SpLiCE，span-aware 准确约翻倍（文本 61.45% vs 29.58%）。去 bias 可提高命名实体召回。

## 结论
良对齐嵌入空间中多数词汇内容可线性恢复；FLiP 可作为不依赖下游榜单的内在诊断工具，揭示模态对齐与英语偏置。

## 点评
把解释落成可量化的关键词召回，比单点 MTEB 分数更细。线性假设与词袋忽略语序；“诊断工具”定位清楚，但高召回不等于语义忠实。


# Inside the Latent Flow: Causal Deciphering of Attention Dynamics in Audio Separation Foundation Models

- 论文编号：2684
- 报告人：Yuxuan Chen
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/chen26ca_interspeech.pdf

## 问题
Flow-matching transformer（如 SAM Audio）分离效果强，但多模态条件如何注入、注意力如何沿 ODE 轨迹演化仍不透明；直接把视觉扩散中“cross-attention=语义锚定”的假设搬到音频可能误导。

## 方法
在推理期对 SAM Audio 做确定性因果探针（不改权重）：(1) Orthogonal probing 分别清零 additive text injection、cross-attention 或强制均匀注意力；(2) Causal freezing 按注意力熵变化率划分 stable/fast 层并中途冻结；(3) Gate hijacking 强行打开 span gate（γ=+5.0）检验时序分段几何能力。据此提出训练无关的 Layer-Selective Attention Caching（LSAC）：对已收敛的 stable 层缓存注意力矩阵（V 仍每步重算），设 SAFE/BALANCED/AGGRESSIVE 冻结步配置。

## 实验与结果
在 SAM Audio Small（12 层、16 步 Euler）与 3B（22 层）上，Clean/Noisy/Env 三档共逾万次 ODE 运行。Additive 消融对语义轴冲击最大（STOI Δ=−0.219，d=−0.89）；清零 CA 对声学轴冲击大（SAR −9.85 dB）。Stable 层可早至 Step 4 冻结（SI-SNR 仅劣 0.05 dB）；Fast 层 Step 8 冻结劣 0.66 dB。Gate 劫持使 L06 Block Ratio 5.76→9.55，同时 SI-SNR 崩约 14.6 dB。LSAC 约省 25% self-attention 计算，质量保持明显优于 naive 减步（Noisy 档可达约 6.7× 相对优势）。

## 结论
文本条件呈非对称双通路：additive 管语义身份，cross-attention 管声学结构；层间异步“搭脚手架再雕细节”；模型会主动抑制离散时序边界先验以保连续流稳定。LSAC 把该洞察转成可扩展加速。

## 点评
用因果干预而非被动看注意力图，直接挑战“CA=语义 grounding”的常见迁移假设，并落到可部署缓存策略。结论依赖 SAM Audio 一类 flow DiT；gate 与冻结阈值阈值模型特定，推广到其他分离骨干需再验证。PDF 抽取中部分图表数字有乱码，正文表格与叙述仍可读。


# Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information

- 论文编号：811
- 报告人：Shih-Heng Wang
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/wang26n_interspeech.pdf

## 问题
Neural Audio Codec（NAC）广泛用于语音系统，但离散表征如何编码语言与副语言信息仍不清晰；尤其口音这类纠缠因素，缺少可量化的任务级可解释性框架。

## 方法
对 utterance 级 NAC 表征 u（时间均值池化）训练 TopK Sparse Autoencoder 得到稀疏激活 z；再用 logistic regression 做口音二分类。将 z 分解为 position（激活位置二值）与 magnitude（top-k 幅值排序）两路分别探针。用相对指标 ΔF1=F1_SAE−F1_ref（相对各 NAC 在 u 上的参考 F1）比较可解释性，避免原始口音信息量不同导致的不公。

## 实验与结果
数据来自 Vox-Profile：US vs. UK 与 US vs. Non-US-UK。覆盖 EnCodec（1.5/6/12 kbps）、DAC、Mimi、SpeechTokenizer，共 16 组 (latent ratio q×相对稀疏 s) SAE。参考 F1 上 SpeechTokenizer/Mimi 更高，但可解释性上 DAC（US vs. UK 16 配置中 13 次第一）与 SpeechTokenizer（Non-US-UK 14/16 第一）更强。声学导向 NAC 口音信息更偏激活幅值；语音学导向更偏激活位置。EnCodec 低码率（1.5 kbps）ΔF1 掉幅更小，可解释性高于高码率变体。

## 结论
提出以 SAE+ΔF1 量化 NAC 任务级可解释性的框架，并以口音为案例表明：原始口音信息多≠可稀疏分解；编码方式随 NAC 目标（声学/语音学）与码率而异。

## 点评
用相对性能而非绝对 F1 比较可解释性，避免“信息多就显得可解释”的混淆；position/magnitude 分解给出可操作的编码差异。局限是任务级代理、口音二分类，且低维 NAC（如 EnCodec）的绝对稀疏容量可能影响公平性，正文亦有说明。


# Spectro-Temporal Interference Confounds Phase Encoding in Spatial Audio Foundation Models

- 论文编号：2873
- 报告人：Yuxuan Chen
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/chen26da_interspeech.pdf

## 问题
空间自监督音频模型在定位等宏观任务上表现好，但未必真正编码微秒级耳间相位（IPD）；下游成功可能来自捷径，现有几何/房间声学基准无法检验这一点。

## 方法
提出基于 binaural masking level difference（BMLD）的心理声学表征基准：在冻结模型嵌入上用特征距离比 ΔBMLD 度量 SπN0 相对 S0N0 的空间释掩。对照 Durlach EC 解析基线与 GCC-PHAT 正对照；评估双耳 SSL（WavJEPA、GRAM-T、Spatial-AST、DSpAST）、单耳负对照（HuBERT-L/WavLM-L/Wav2Vec2-L、DAC）与编解码器（EnCodec）。用高通、Mel 带能量均衡、50 Hz envelope vocoder 等逐步物理消融隔离机制；并在 AIR BRIR+LibriSpeech 上做生态评测。

## 实验与结果
500 Hz、−14 dB SNR：EC 为 +15.7 dB；WavJEPA +0.5、GRAM-T +2.1（远低于天花板）；Spatial-AST/DSpAST/EnCodec 约 +6.8–7.0 dB；四类单耳对照恒为 0。GRAM-T 对 ILD 敏感（峰 18.2）远强于 ITD（~2.6），Spatial-AST 相反（ITD 152 > ILD 85）。高通与能量均衡几乎不伤 GRAM-T/EnCodec 检出；vocoder 摧毁 TFS 后 GRAM-T 100%→75%、EnCodec 100%→20%、Spatial-AST 100%→60%。语音生态条件下双耳模型显著率很高，但机制上仍可能是宽带包络干扰纹理而非真相位计算。

## 结论
通用双耳 SSL 主要依赖每通道 spectro-temporal interference / 包络纹理，而非跨通道相位；专用 IPD 架构可达实质但亚天花板的相位敏感。未来预训练需显式相位约束。

## 点评
把经典 BMLD 做成冻结表征探针，再用物理消融 falsify“相位编码”叙事，对空间音频可解释性很有力。注意 ΔBMLD 是嵌入距离比而非人类听阈；结论对预训练目标（MAE 重建谱 vs IPD 特征）的归因合理，但未覆盖全部空间模型族。


# On Optimizing Multimodal Jailbreaks for Spoken Language Models

- 论文编号：309
- 报告人：Aravind Krishnan
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/krishnan26_interspeech.pdf

## 问题
Spoken Language Models 同时接受语音与文本，现有越狱多只优化单一模态；仅凭单模态鲁棒性可能高估多模态系统安全性。

## 方法
提出 JAMA：白盒联合优化文本后缀（GCG）与音频扰动（PGD），每步对同一联合损失同时更新 δ 与离散 suffix。评估 Audio Flamingo 3、Qwen2 Audio、Gemma 3N、Qwen2.5 Omni；PGD 初始化用朗读/对话/音乐等四类基音频。据梯度能量分析提出 SAMA：先纯文本 GCG 再固定后缀做 PGD，作为更便宜的序列近似。数据为 AdvBench（8 训 / 480 测，5 seed），成功判据含 LLaMA Guard 3。

## 实验与结果
JAMA 相对单模态 GCG/PGD 越狱率提升约 1.5×–20×；Gemma 3N 对纯 GCG 很硬（长后缀仍约 3%），但联合优化（尤其音乐+较长 PGD）明显打开缺口。PGD 单独通常弱于 GCG；音乐初始化与更长音频往往更强。t-SNE 显示成功多模态攻击落在远离 benign 的独立子空间。SAMA 在足够长的 GCG/PGD 配置下接近 JAMA，平均差距约 10%，计算约快 4×–6×（同配置 H100）。

## 结论
多模态同时扰动暴露单模态评测看不见的脆弱面；序列近似可作强基线。作者主张发布前需在复合攻击空间加强护栏。

## 点评
把 GCG 与 PGD 真正“同时”接到同一损失上，比“一模态优化、另一模态旁观”更贴近对手。结果依赖可微特征提取器改写与白盒设定；对不可微/闭源 SLM 的迁移性正文未覆盖。


# A Unified Safety Subspace Exists in Speech Language Models

- 论文编号：2797
- 报告人：Nurdaulet Mukhituly
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/mukhituly26_interspeech.pdf

## 问题
SLM 同时面临文本与音频越狱；先验常把语音安全当独立问题。不清楚音频攻击是否走模态特异失效，还是绕过与文本共享的内部安全机制。

## 方法
在中间层 last-token residual stream 上对 harmful/jailbreak 激活做 PCA，估计从拒绝簇到顺从簇的方向并回投为全维 steering 向量（Audio Vector 来自 AdvWave，Text Vector 来自 AutoDAN）。推理时在选定层对激活加减归一化方向（α 控制幅度与符号），无需再训练。在 Qwen2-Audio（层 15）与 GLM-4-Voice（层 17）上评估跨攻击、跨模态迁移；ASR 由 GPT-5 作 judge。

## 实验与结果
PCA 上 harmful 与 jailbreak 可分，jailbreak 落在 benign 与 harmful 之间。负向 steering 把五类攻击 ASR 压到大多 <7%：如 AdvWave 97.93%→0.52%（Qwen）、AutoDAN 72.69%→2.82%；音频向量对文本越狱、文本向量对音频越狱同样有效。正向 steering 使原本拒绝的有害输入 ASR 升至约 56–90%。同范数随机方向远弱于定向向量。摘要亦报告拒绝向量使文本越狱约 76.5%→2.2%、音频约 79.0%→3.1%。

## 结论
SLM 残差流中存在跨模态、跨攻击族共享的低维安全子空间；单一方向即可在推理期翻转拒绝/顺从，支持“统一几何边界”而非纯模态特异漏洞。

## 点评
把文本 LM 的 refusal-direction 叙事推进到语音-文本双通道，并用跨模态迁移做因果证据，说服力强。依赖中间层选择、α 扫描与 LLM judge；对不同对齐策略/规模的稳定性以及是否被自适应攻击绕过，仍是开放问题。


# Do Learned Layer Weights Reflect Pretrained Information Structure in Self-Supervised Speech Models?

- 论文编号：566
- 报告人：Yaroslav Getman
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/getman26b_interspeech.pdf

## 问题
先验认为 SUPERB 类可学习层权重与单层下游性能相关弱（ρ 约 0.39–0.71），“不可靠”。作者改问：这些权重分布是否反映预训练模型的层间信息结构？

## 方法
在冻结 SSL 上按层提取 phone/word 段表征，k-means 聚类后算与标签的 adjusted mutual information（AMI）。层权重取自 ML-SUPERB 英语 ASR（softmax 加权和 + CTC），比较 10 min 与 1 h 有标签监督；对每层输出做 layer norm 再聚合。用 Spearman ρ + 置换检验关联权重与 AMI。覆盖对比学习（wav2vec 2.0 族）、聚类（HuBERT）、聚类+去噪（WavLM）共 13 个 Base/Large/XLarge 模型。

## 实验与结果
52 个模型-条件组合中 49 个显著正相关。对比模型在 10 min 上最强（phone/word AMI 均值 ρ=0.86/0.91，个体可达 0.98）；1 h 降至 0.65/0.70。HuBERT/WavLM 更弱且更易变。额外监督使权重更集中于较深层、熵更低，偏离宽峰 AMI 曲线。权重虽仍接近均匀（归一化熵>0.996），但排序系统且与 AMI 对齐。

## 结论
层权重并非无信息：它们系统反映预训练层间音素/词信息结构，尤其在对比目标与低资源监督下；弱“权重–单层性能”相关更可能是参照不当，而非权重本身无用。

## 点评
把评价参照从下游单层分数换成预训练 AMI，直接回应“权重不可靠”叙事，结论清晰可复现。边界是仅 ASR + phone/word AMI；非 ASR 任务可能需要别的信息度量。


# XAI-Grounded Explanation Generation for Speech Deepfake Detection with Training-Free Multimodal Large Language Models

- 论文编号：161
- 报告人：Yupei Li
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/li26_interspeech.pdf

## 问题
语音深度伪造检测需要可信解释：传统 XAI 给出难读的低层归因；纯 LLM 解释又易幻觉、缺任务证据与专用数据集。

## 方法
提出训练无关框架 XGEG：用预训练 wav2vec 2.0 / HuBERT / WavLM 检测器生成 IG、LIME、Saliency 谱图归因，经 Qwen2.5-VL-7B 汇总时频异常；另用 openSMILE eGeMAPSv02 + MLP 的 SHAP 取 top 声学特征。将音频与这些证据交给 Qwen3-Omni-30B，按结构化模板（异常时频、自由解释、XAI 聚合说明）生成文本，并强调批判使用 XAI 而非照抄。基于 PartialSpoof 构建约 6.5 万条可解释实例（仅保留四模型均判对的伪造样本）。

## 实验与结果
人工评测（600 条、20 人）：XAI 引导相对纯音频在正确性/证据/特异性上提升明显；三模型聚合 overall preference 最高（1.50 vs 基线 0.35）。时间定位：纯音频 IoU 高但 Inside Accuracy 仅 0.049；单 XAI/聚合可将 IA 提至约 0.48–0.81（摘要称 IA 提升超 45%）。Area-Normalised Local Logit Sensitivity 上 XAI 方法远高于基线（LIME 可达约 327×）。发布数据集采用单模型全 XAI 配置（综合质量最佳）。

## 结论
跨模型/多方法 XAI 证据可引导免训练多模态 LLM 生成更具体、更少幻觉的 SDD 解释，并释放大规模 grounded 解释数据以支持后续研究。

## 点评
把“归因热图可读化 + LLM 叙事”接到同一管线，并用 IoU/IA 与 logit 灵敏度约束 faithfulness，比纯 post-hoc 文案更扎实。代价是流水线重、依赖多检测器与大模型推理；对 bona fide“证明无异常”仍难，正文亦承认。


# Cross-Attention is Half Explanation in Speech-to-Text Models

- 论文编号：40
- 报告人：Luisa Bentivogli
- 程序：Monday 28 September 2026 / Speech Representations and Alignment
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/papi26_interspeech.pdf

## 问题
S2T 中 cross-attention 常被用作音字对齐、时间戳、同传引导等，默认它反映输入–输出依赖。NLP 对 attention-as-explanation 争论已久，语音域仍缺系统验证；encoder 上下文混合可能使 CA 与原始声学相关性脱节。

## 方法
将 decoder **cross-attention（CA）** 与特征归因显著性对比：
- 输入显著性 \(SM_X\)：SPES 对 mel 频谱扰动聚类得 token 级 saliency，再沿频率聚合并下采样到编码器时间步；
- 编码器输出显著性 \(SM_H\)：对 encoder 隐状态做类似扰动归因，隔离上下文混合；
- 多层多头 CA 可按层/头/全局平均；与 saliency 算 Pearson 相关。
模型：自训 monolingual ASR（125M）与开放数据 FAMA 多任务多语 small/large（474M/878M，en/it ASR+ST）；测试 EuroParl-ST。

## 实验与结果
（抽取在 §4.4 聚合函数处截断；主结论取自摘要与引言汇总。）
- CA 与输入 saliency **中等**相关，跨头/层聚合时更明显；
- CA 大约只覆盖约 **50%** 输入相关性；相对 encoder saliency 最好约 **52–75%**；
- 趋势在单语/多语、单任务/多任务、多尺度上一致；CA 更贴近 encoder 输出而非原始输入，提示上下文混合影响。

## 结论
Cross-attention 提供有用但不完整的解释线索，不宜单独当作 S2T 行为的充分代理；正式特征归因仍更全面，CA 可作轻量辅助。

## 点评
把 NLP 的 attention 解释争论落到语音 encoder–decoder，并用 \(SM_X\) vs \(SM_H\) 拆开上下文混合，问题意识强。标题数字“一半”来自约 50% 输入覆盖。**详细相关表与聚合消融未完整进入抽取**，精确分层/头结果需回原文。


# Causal Tracing of Audio-Text Fusion in Large Audio Language Models

- 论文编号：1118
- 报告人：Wei-Chih Chen
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/chen26k_interspeech.pdf

## 问题
LALM 任务表现强，但声学特征与文本上下文何时、在何处融合仍是黑盒；多数评测只看最终输出，无法定位跨模态因果通路。

## 方法
将 ROME 式因果追踪适配到 LALM：clean（原音频）、corrupted（静音替换音频）、patched（把 clean 的选定隐状态写入 corrupted 继续前向）。用 Recovery Rate RR=(P_patched−P_corrupted)/(P_clean−P_corrupted) 量化因果贡献。层向：整层文本 token 隐状态整体替换；词向：单 token 位置替换，并把 prompt 分为 early / object / late / last token。在 SAKURA 四属性（animal/emotion/gender/language）上评 DeSTA2/2.5、Qwen/Qwen2、Voxtral。

## 实验与结果
层向：DeSTA 呈渐进融合（约层 15 后稳定）；Qwen 族早期 RR≈0、约在层 18–31 陡升（晚融合）；Voxtral 更早达到高 RR（早融合）。词向：所有模型最高 RR 集中在生成前最后一 token（信息瓶颈）；中间层 object token 出现次级因果峰，类似“查询触发”拉取任务相关音频。

## 结论
不同 LALM 族采用 progressive / late / early 等不同融合策略；最后 token 是跨模态检索瓶颈，object token 触发类注意力查询。这些定位可为效率优化与幻觉监测提供线索。

## 点评
用静音 corrupted 干净消融声学、再用 RR 做因果度量，比纯 logit-lens 观察更强。发现与 VLM 末 token 瓶颈类似，暗示 transformer 通用机制。局限是分类式约束生成设定与选定模型族；开放生成或更复杂推理任务是否同构仍待验。


# Disentangling Acoustic Cues in Alzheimer’s Pathology and Perception: The Roles of Language and Gender

- 论文编号：1149
- 报告人：Liu He
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/he26d_interspeech.pdf

## 问题
AD 语音生物标志与人类听感线索是否对齐，尚少跨语言、跨性别系统审计；全局 XAI 可能掩盖人群特异失败，影响临床公平部署。

## 方法
对 Mandarin（NCMMSC2021）与 Greek（ADReSS-M）看图描述各 30 条（AD/HC 各半）提取 21 维声学特征（时序流畅、韵律、发声、发音）。训练 Random Forest：病理分类（临床 AD）与感知回归（16 名普通话听者的 Perception Weighted Score）。用 SHAP 比较两任务特征重要性，并用 GLMER 验证语言/性别与声学交互；年龄与教育仅作统计协变量，不进预测模型。

## 实验与结果
全数据病理 AUC=0.70、感知 r=0.72；Mandarin 与女性病理模型显著（AUC 0.83/0.79），Greek 与男性病理未超机会（0.60/0.52），但感知模型均显著。病理–感知特征排序总体 Spearman ρ=0.55；Mandarin/女性仍显著对齐（ρ≈0.52–0.54），Greek/男性对齐消失。病理更重 pause/jitter/F1 等，感知更重语速、停顿总长与 F0。GLMER 显示停顿、F0 标准差等驱动 AD 听感，且 F0/F2 等与性别有显著交互。

## 结论
病理与感知线索仅部分对齐，且强依赖语言与性别；人群特异 XAI 审计可暴露“模型对某人口几乎无效”的失败模式，是公平临床语音 AI 的前提。

## 点评
把“XAI 是否对人类利益相关者有效”从模型内正确性推进到跨人群外部效度，问题设置很有临床意义。样本每语种仅 30 句、听者文化同质，作者亦定位为假说生成；Greek/男性病理接近机会时，其 SHAP 解读需谨慎。


# Towards Dys-XAI: Influence-Based Explanations for Dysarthria Severity Assessment

- 论文编号：538
- 报告人：Xiaoliang Wu
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/wu26b_interspeech.pdf

## 问题
构音障碍严重度自动评估黑盒难获临床信任；常见谱图/声学特征归因不易转成临床可比对的证据，也难体现相邻等级的序数关系。

## 方法
在 TORGO 四类序数分类（typical/mild/moderate/severe）上，用训练轨迹梯度内积近似各训练样本对测试预测的影响 I_i→t，得到支持/对抗样本。按严重度聚合得类级影响矩阵 S，并按序数距离 d 统计 ¯S(d) 检验序数敏感。用控制删除（删高/低影响或随机 5–20%）验证影响分数因果性。基分类器为 80-dim FBank + 单层线性分类器，说话人分层 K-fold。

## 实验与结果
删高影响样本使准确率显著下降（如 moderate 36.8%→0.3%、severe 72.3%→43.1%）；删低影响反而提升（mild 5.5%→17.6% 等）；随机删除 |Δ|<2%。S 呈块对角：同级支持最强；typical 只受 typical 正影响，构音障碍等级间互相正支持。¯S(d) 随 d 单调衰减（13427→1028→−642→−2561）。案例显示影响排名可揪出近静音伪相关训练文件；相对 SHAP 的 OpenSMILE 分数列表，音频参考样本更可听验。

## 结论
基于训练实例影响的解释把决策连到可感知参考样例，并通过删除实验与序数衰减模式验证忠实性，适合临床审计与数据质检。

## 点评
案例式解释对准临床“与原型比较”的推理习惯，且能做数据集审计，比热图更可行动。当前骨干极简、数据以 TORGO 为主；影响计算依赖多 checkpoint，扩展到大模型与更细标注粒度仍需验证。


# What Do Neural Networks Learn for TDOA Estimation? A Cross-Architecture Probing Study

- 论文编号：3246
- 报告人：Yaozhong Kang
- 程序：Wednesday 30 September 2026 / Explainability for Compliance and Trust in Speech AI
- 技术分类键：trust
- 全文：https://www.isca-archive.org/interspeech_2026/kang26b_interspeech.pdf

## 问题
神经网络在噪声/混响下常优于 GCC-PHAT 做 TDOA，但其内部是否复现 GCC-PHAT 的交叉功率与 PHAT 白化步骤尚不清楚，影响混合管线设计。

## 方法
以双麦 STFT 窄带观测为输入，训练 MLP-per-bin、1D-CNN、Transformer 回归延迟。用线性（及非线性对照）probe 解码各层是否含 cross-power、PHAT 相位与 τ；辅以梯度频率归因与单频 bin 掩蔽因果检验。在合成噪声、混响、LibriSpeech 仿真通道与 LOCATA 真实阵列上评测。

## 实验与结果
各架构均能高 R² 解码 cross-power（如 Transformer 0.94），而理论 PHAT 相位持续低（≤0.21）；网络另编码 |G12|（R²=0.82）。学习权重与 |G12| 正相关（r=+0.53）、与 1/|G12| 反相关；掩蔽 ΔMAE 与归因高度一致（r=+0.94）。经典与神经 GCC 在加性噪声下去掉 PHAT（Flat）多数条件更优；LOCATA 上 PHAT 仍是最佳经典加权，但端到端 Transformer MAE 5.75，约为经典机会水平的约 2.4× 更低误差。

## 结论
跨架构共享的是交叉功率计算，而非 PHAT 白化；网络学到保留频带可靠性的幅度感知加权。PHAT 对神经管线常是信息瓶颈，但在真实混响经典设定下仍有价值。

## 点评
把经典算法步骤变成可探针靶标，再辅因果掩蔽，解释力强、对 NGCC 设计有直接建议。局限是单声源假设与频谱输入；波形端模型与更强混响下是否转向去混响类特征，正文留作开放问题。

