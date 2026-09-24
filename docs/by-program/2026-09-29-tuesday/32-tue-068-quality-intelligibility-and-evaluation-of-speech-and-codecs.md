# Quality, Intelligibility and Evaluation of Speech and Codecs

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：6
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场把“听得清/听得省力/评得准”放在同一条评估链上。近端聆听增强从时频改到谱—时调制域能量重分配；个性化神经编解码用说话人聚类压缩模型与码率；歌词可懂度预测融合声学与 Whisper 表征。

主观评测方法论成为独立主题：众包 vs. 实验室、筛查手段、噪声与增强对编解码可懂度的交互，以及听力障碍听者跨数据集可懂度预测的小样本适配。声学传送编解码的探测式解耦评估，则指出交叉重建不足以发现泄漏。

另一端是用现代 ASR 评价增强系统时的陷阱：大模型噪声鲁棒与语言模型上下文可能使 WER“看起来太好”，与声学向的增强评测目标不完全一致；低帧率神经编解码的质量悬崖也被归因到训练配置而非根本物理障碍。

## 论文技术总结

# Energy Redistribution in the Spectro-Temporal Modulation Domain for Near-End Listening Enhancement

- 论文编号：319
- 报告人：Amin Edraki
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/edraki26_interspeech.pdf

## 问题

Near-End Listening Enhancement（NELE）需在总能量不变下重分配语音能量以提升嘈杂回放可懂度。多数方法在时–频域加权，难以显式操控对感知重要的 Spectro-Temporal Modulation（STM）结构（如共振峰过渡）。

## 方法

在 Modulation Power Spectrum（MPS）上乘以可学习非负 STM mask，再逆 2D FFT 回谱图（复用原相位），加高斯带通强调后 iSTFT，最后能量归一化到与干净语音相同。mask 为段无关全局参数，用 −ESTOI(干净参考, 处理后+噪声) 做梯度优化。消融比较 temporal-only、spectral-only、separable、joint 四种参数化，最终选用参数更少且效果接近 joint 的 separable mask（约 260 vs 16K 参数）。

## 实验与结果

训练：LibriSpeech train-clean-100 的 5 s 段 + AudioSet 噪声，SNR −15–0 dB。客观评测：dev-clean 100 句，DEMAND（restaurant/living room/station）与 SSN，SNR −10/−5 dB；指标 ESTOI、wSTMI、STGI、Whisper-small WER。相对未处理基线，所提方法平均增益通常高于 SSDRC、OptimalSII、iMetricGAN；−5 dB 下多数条件显著最优。主观：5 名正常听力普通话听者、中文矩阵句、餐厅噪声 −5 dB，句正确率 STM 0.92，高于 Noisy 0.46 及 OptimalSII/iMetricGAN，与 SSDRC（0.90）接近。

## 结论

作者认为在 STM 域联合调控谱/时调制比单维 mask 更稳；可分 mask 在参数量与效果间折中较好。主观实验规模小、条件单一，需更大验证；学到的 mask 远离调制 DC、偏向更高调制频率，反映能量从极慢包络再分配。

## 点评

把 NELE 从时–频“哪段能量重要”转到“哪类调制重要”，与可懂度文献中 STM 角色一致，且用可微 ESTOI 直接优化全局 mask，实现简单。脆弱点在于：优化目标绑死 ESTOI，其他指标/ASR/主观不完全同序；全局固定 mask 不随内容自适应；主观样本少，对声调语言的泛化仍属初步证据。


# End-to-End Model Compression for Personalized Neural Speech Codecs

- 论文编号：878
- 报告人：Inseon Jang
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/jang26_interspeech.pdf

## 问题

端到端神经语音编解码（如 DAC）参数与算力膨胀，难在低功耗设备实时运行。已有说话人无关压缩常绑特定结构、压缩比有限；先前个性化 LPCNet 只压缩解码端，编码端仍重，且多在干净语音上验证。

## 方法

提出端到端 Personalized DAC（PDAC）：噪声鲁棒说话人编码器 F 提 embedding，与预计算的 C 个说话人组中心做欧氏最近邻得组索引 c*；发送端只跑对应小组 utterance 编码器 G^(c*) 产生码流 y，并下传 c*；接收端用匹配的个性化解码器 D^(c*) 重建干净语音。说话人组由对比学习 Siamese embedding 上 k-means 预先聚类。相对通用 Large DAC（74.18M），设计 Small（14.99M）与 Tiny（3.02M）容量配置，各组独立训练 encoder–decoder–量化器。系统把 MoLE 做成“排他选专家”，发送与接收两侧都只跑一个小组模型。

## 实验与结果

设定基于 LibriSpeech train-clean-100（251 说话人）训练，dev/test-clean 验证测试。摘要称：相对 SOTA DAC，模型体积约减 96%、码率由 2 kbps 降至 1 kbps（减半），主观听感可维持；噪声下个性化模型仍优于基线。正文实验与表格在全文抽取中于数据集描述处截断，具体 DMOS/客观分数字未能完整读到。

## 结论

作者认为在端到端编解码两侧同时做说话人组个性化，可同时压模型与码率并保留感知质量，且对噪声与组误分类有一定鲁棒性（文中称将通过微调分类与专家缓解误分类）。部署上强调适合低功耗、干净与噪声场景。

## 点评

相对“全局小模型”或“只压解码器”，排他式组专家把容量花在更同质的说话人子集上，压缩逻辑清晰。全文 PDF 抽取在实验段中断，定量结论主要依赖摘要与方法描述，点评无法核实表格数字。潜在脆弱点包括：组数/聚类质量、测试说话人落错组、以及噪声鲁棒说话人编码器本身的误差会连带选错编解码专家。


# Acoustic and Semantic Feature Fusion Mapping for Lyric Intelligibility Prediction

- 论文编号：1014
- 报告人：Yuxiang Fu
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/fu26_interspeech.pdf

## 问题

歌词可懂度受演唱、伴奏、旋律与语义等影响，难于口语 intelligibility。手工声学特征缺高层语音/语义信息；ASR 词正确率与人对歌词的主观可懂度存在系统性偏差，尤其在歌唱场景。

## 方法

提出声学 + 预训练编码器特征融合再回归：声学侧含能量、RMS、过零率、谱质心/带宽/rolloff、时长、源分离 SNR 等；语义/语音侧取 Whisper base.en 编码器时序嵌入。经均值/标准差/极值/偏度/峰度等时序统计，并在重要特征间构造成对交互，标准化后送入映射模块。对比神经网络（FCN、MoE FCN、CNN+GRU、Transformer）与梯度提升树（XGBoost、LightGBM、CatBoost）。侵入式 Whisper 转录正确率作基线。

## 实验与结果

数据为 Cadenza 2026 Challenge 人工标注歌词可懂度集，5 折交叉验证；指标 RMSE（×100）与 Pearson Corr。Whisper base.en 下：Baseline RMSE 29.32 / Corr 0.59；CatBoost 最优 27.367 / 0.654；无交互 CatBoost 27.532 / 0.651；树模型整体优于神经网络，Transformer 最差（34.896 / 0.461）。图示比较中 Whisper 嵌入优于 Mert、Wav2Vec2。

## 结论

作者认为融合浅层声学与 Whisper 表示、再用树模型做结构化映射，比纯 ASR 正确率更贴近主观歌词可懂度；未来可探索端到端多模态（声学–语义–语言）一体化模型。

## 点评

问题抓得准：唱歌场景下“机器听对词 ≠ 人听得懂”。特征工程 + CatBoost 在千级样本上更稳，符合数据量不足时神经网络易过拟合的常见现象。侵入式设定依赖参考歌词；交互特征与编码器选择对结果敏感，泛化到未见曲风/语言时需再验证。


# Screening Matters: A Comparative Study of Conventional and Crowdsourced Listening Tests

- 论文编号：1387
- 报告人：Anika Treffehn
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/treffehn26_interspeech.pdf

## 问题

主观听测仍是评估经典与神经语音/音频编解码质量的可靠手段，但实验室 P.800 成本高；众包 P.808 更快更便宜，却难控环境与设备，结果常更差（评分跨度收缩、方差变大）。需要弄清哪些筛选能有效把众包结果拉近实验室基准。

## 方法

对同一套 20 条件 DCR（含参考、MNRU、低通、Codec2/AMR/EVS 及 FlowDec、Lyra、DAC、Mimi、SNAC、WavTokenizer 等），分别做实验室 P.800（27 人）与 MTurk P.808（33 人）。系统比较三类筛选：预筛选（MJNDQ 式 pretest、问卷）、中筛选（traps、参考金标准最低分阈值）、后筛选（评分跨度、MNRU 锚点排序）。以相对 P.800 条件均值的 MAE/RMSE 与 Pearson/Spearman 相关衡量对齐度。

## 实验与结果

无筛选时两测相关高（r=ρ=0.929）但绝对误差大（MAE 0.573、RMSE 0.659），参考分降 1.11、最差锚点升 0.88。Pretest/问卷几乎无效。Gold standard（最低参考≥4）+ 剔除 trap 离群后：MAE 0.327、RMSE 0.401、r=ρ=0.963（留 14 人）。评分跨度≥2.5：MAE 0.284、RMSE 0.325。完美锚点排序：MAE 0.376、RMSE 0.428。联合后筛选（跨度 2.5 + 完美排序）达 MAE 0.230、RMSE 0.259、r=0.974（留 7 人）；通过后筛选者亦通过中筛选。

## 结论

作者认为众包听测可通过 traps、最低参考分、评分跨度与锚点排序显著贴近 P.800；预筛选在本文设定下无效。建议用预设阈值做被试级筛选以替代仅靠条件内标准化离群规则，并多招 3–5 倍被试以抵消淘汰。适用于早期原型评估等需快、省的场景。

## 点评

把“众包差在哪”具体化成未用满量表与条件内方差过大，再按预/中/后筛选做可复现的消融，对实际听测协议很实用。后筛选越严越准但有效人数骤减，统计功效与偏差风险上升；结论依赖本测试集与 DMOS 设定，换语言/立体声/一般音频时阈值需重标定。相对盲目用标准化 outlier，被试级跨度与锚点排序更不易把真实感知差异误判为离群。


# Assessing the Impact of Noise and Speech Enhancement on the Intelligibility of Speech Codecs

- 论文编号：1459
- 报告人：Lyonel Behringer
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/behringer26_interspeech.pdf

## 问题

极低码率神经语音编解码常只在干净语音上评质量，缺少噪声与真实通信管线下的句级可懂度评估；可懂度易触顶（ceiling），且客观指标与主观结果在噪声条件下关联尚不充分。

## 方法

对经典编解码（AMR-WB 6.6 kbps、EVS 8 kbps）与神经编解码（LPCNet 1.6、Lyra V2 3.2、DAC 1.5、Mimi 1.1 kbps）做众包句级听测：材料来自 Clarity Speech Corpus，混入 DEMAND 四类噪声（DLIVING/PRESTO/TCAR/TMETRO），SNR 5/15/25 dB，可选 DeepFilterNet2 增强后再编码。听者转写句子并评听努力（P.800 Annex B 五分制）。转录规范化后算词正确率 SI 与 WER。用 LMM 分析 codec×噪声×SNR×SE；并与 STOI/ESTOI 及多种 ASR（Whisper-B/L、Parakeet、Canary）条件级/样本级相关。

## 实验与结果

有效 160 人、7670 条响应。干净与 25 dB 接近顶；低 SNR 下经典编解码更抗噪，神经编解码掉得更狠。SE 显著提升 DAC、LPCNet、Mimi 的可懂度（Δ 约 0.060/0.082/0.036）与听努力；对 AMR-WB、EVS、Lyra、参考不显著。PRESTO/TMETRO 最伤神经编解码。在 SI≥0.95 子集上，听努力仍能区分：DAC 听努力最低（接近参考）。条件级上 ASR 客观 SI 与主观相关高于 STOI/ESTOI（Whisper-B 条件级 PC 0.973）。

## 结论

作者认为神经编解码噪声鲁棒性弱于经典编解码；编码前 SE 可缩小差距；听努力可缓解可懂度顶棚；条件级 ASR 比 STOI/ESTOI 更宜作客观代理。低 SNR 标注者一致性下降是局限。

## 点评

把“通信管线=可选 SE + 编解码 + 噪声”做成系统听测，结论对部署很实用：低码率神经编解码不该只报干净 MOS。听努力作顶棚补丁设计干净。客观相关强调条件级而非样本级，避免过度解读单句 ASR。众包与 IAR 在极低 SNR 变差，细粒度噪声对比需谨慎。


# Improving Cross-Dataset Speech Intelligibility Prediction for Hearing-Impaired Listeners with Few-Shot Adaptation

- 论文编号：1567
- 报告人：Guojian Lin
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/lin26h_interspeech.pdf

## 问题

听障可懂度预测模型跨数据集（听者、声学、助听器设定）性能骤降；主观标注昂贵，目标域标签稀缺。仅靠增广或点对点回归，难以在少样本下学到可区分高/低可懂度的域不变表示。

## 方法

提出 CFA-SIPNet：源域（CPC3）监督预训练 + 目标域少样本适配。双通道 WavLM/Whisper 融合后经位置编码与三层 Transformer；预训练损失为 MSE + 排序对比损失。适配时冻结 SFM 与 Transformer，只更新插入各层的 bottleneck adapter（128 维）、embedding 模块与评分 MLP；并用基于真值差阈值 τ=0.4 的 embedding 对比损失，总损失加权 MSE、排序与 embedding 对比。

## 实验与结果

源域 CPC3（约 15k 训练）；目标域 Arehart 听障子集 8100 句，12 听者训练/3 未见听者测试。每听者抽 100 句作 few-shot（&lt;20% 目标训练量）。跨数据集：RMSE 26.05、PCC 0.75，优于 ZipEnhancer+MP-SENet 的 2-Clips（28.48/0.72）与零样本，并优于多数全量域内训练结果。相对该 SOTA 相对 RMSE 降 8.5%、PCC 升 4.2%。消融显示去掉 adapter+对比或源预训练均变差；few-shot 适配优于联合训练/全参微调/仅域内训练。

## 结论

作者认为源预训练与少样本适配互补，能以少量目标标注达到甚至超过全量域内训练的跨集泛化，适合听障可懂度评估落地。

## 点评

抓住“标签贵、域移大”：用冻结骨干 + 轻量 adapter 与可懂度结构对比，比盲目 2-Clips 增广更省标注。few-shot 抽样强调分数均匀，避免适配偏到某一分数段。目前在 CPC3→Arehart 设定上验证；听者与采样率差异大，换更复杂声学或更广听者时还需检验。


# Beyond Cross-Reconstruction: Probing-Based Disentanglement Evaluation for Acoustic Teleportation Codecs

- 论文编号：2406
- 报告人：Philipp Grundhuber
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/grundhuber26_interspeech.pdf

## 问题

声学传送（AT）等分区神经音频编解码用交叉重建等指标评解缠，但解码器可忽略错误分区中的冗余，泄漏检测不到；经典 DCI/MIG 也不适配分区级结构。

## 方法

将预训练 AT 编码器当固定特征提取器，对 speech / acoustic 两分区分别训练相同轻量 MLP 探针：回归 T60、C50、DRR（分频带+宽带），分类说话人 ID。以意图分区与非意图分区性能差 Δ 作解缠度量。数据：DNS5 read speech ⊕ GWAsmall RIR。系统扫描训练任务集、量化级数 N∈{4,8,16}/未量化、声学流时间下采样等配置。

## 实验与结果

AT 模型在说话人上解缠显著（如 N=8 时 Δacc 达 56.8 pp：83.1% vs 26.3%）；声学信息仅部分分离，speech 分区 T60 相关常仍 &gt;0.75。量化放大说话人分离，但声学泄漏不变；声学流下采样对房间参数估计影响小。声学嵌入盲估宽带 T60 RMSE 0.094 s（ρ=0.947），距监督 CRNN-MB（0.082 s）约 0.02 s 内。ScoreQ 等输出质量与解缠不对齐：无解缠的 +Dereverberation 基线也可有不错 ScoreQ。

## 结论

作者认为探测比交叉重建更能暴露分区泄漏；AT 目标迫使说话人信息进 speech 分区，却无对称压力把房间信息推出 speech，故解缠不对称。未来可用对抗/梯度反转等显式去相关。

## 点评

把“解缠是否真发生”从听感/重建质量里拆出来，用物理可解释的房间参数作探针，诊断力强。简单 MLP 测到的是泄漏下界。仅覆盖时不变因素；语言学内容探针与其他编解码架构尚未验，结论对 AT 训练目标结构的依赖很强。


# Too Good to Be True: A Study on Modern Automatic Speech Recognition Systems for the Evaluation of Speech Enhancement

- 论文编号：2597
- 报告人：Danilo Oliveira
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/oliveira26b_interspeech.pdf

## 问题

用 ASR 的 WER 评语音增强很常见，但结果强烈依赖 ASR 选型与文本归一化；现代大模型对噪声鲁棒、会用语境，其分数是否反映“声学上增强得好”并不清楚。

## 方法

比较 QuartzNet、wav2vec2、Parakeet TDT、多种 Whisper（均贪心解码、无外置 LM）在噪声与多种 SE（SE-Mamba、NCSN++M、StoRM、SB-SGMSE+、SGMSE+）上的词正确率；并与人类听写、LPS、ESTOI、POLQA、SCOREQ 对照。听测：20 人，EARS-WHAM 子集 SNR∈[-2.5,10] dB。用裁剪后的 W Acc=max(1−WER,0) 抑制 Whisper 幻觉极端值。另测标点保留、用干净音频 ASR 作参考等管线扰动对 SE 排序的影响。

## 实验与结果

大规模噪声训练的 Parakeet/Whisper 与人类趋势相关最高（系统级 PCC 可达约 0.93–0.99），但绝对分常高于人类；且噪声子集可懂度常优于任一增强子集（与 observation adding 文献一致）。预测式 NCSN++M 词识别最好，生成式 SGMSE+ 无参考质量高，ASR 排序与 ESTOI/POLQA 不一致。Whisper 低 SNR 插入/循环幻觉严重。标点与参考文本选择可使 CTC 模型排序在约 16–19% bootstrap 样本中变化。

## 结论

作者认为与人类趋势更一致的现代 ASR，未必适合纯声学向的 SE 评测；必须透明报告模型与文本管线，并处理幻觉离群。WER 不能当作单一“真理”指标。

## 点评

核心警告精确：ASR 越强，越可能“听懂噪声、听不懂伪影”，从而低估需要的增强或误排系统。裁剪 W Acc、分解替换/删除/插入，对复现实验很有价值。听测系统数有限，系统级相关置信区间宽；结论应理解为方法学提醒，而非否定一切 ASR 代理。


# Probing Low Frame Rate Degradation in Neural Audio Codecs

- 论文编号：3493
- 报告人：Alex Gichamba
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/gichamba26_interspeech.pdf

## 问题

低帧率神经音频编解码利于自回归 TTS（生成代价随序列长度线性），但 6.25 Hz 常出现可懂度断崖；先前归因于音素碰撞，机制仍不清，不知失败是否内禀于帧率。

## 方法

在 DAC（16 kHz）上做受控帧率消融（约 1.6–100 Hz），固定 nq=12、|V|=1024（码率 R=120·fr bps）。对比固定裁剪时长 Tclip=0.38 s 与固定每例 token 数 K=19。用 MFA 对齐统计 phones/frame；测码本利用率与熵效率；评 WER（MMS-1B）、STOI、MCD、SPK-SIM、UTMOS。并对照公开 DAC/Mimi/SNAC/WavTokenizer 等。

## 实验与结果

固定 Tclip 时 12.5→6.25 Hz：WER 10.62%→107.4%，STOI 0.89→0.46。固定 K 后 6.25 Hz 恢复至 WER 15.37%、STOI 0.89。音素碰撞与码本饱和均非断崖主因（利用率&gt;98.7%，η 几乎平坦）。匹配序列长度后可延至 3.125 Hz（WER 29.36%，375 bps）与 1.6 Hz（WER 63.22%，192 bps），退化随音素负载平滑。

## 结论

作者认为断崖主要来自低帧率下每例 token 过少、解码器学不到跨 token 连贯；修正训练配置后低帧率效率收益比原先设想更可达。

## 点评

用“固定时长 vs 固定序列长度”一刀切出训练配置伪影，推翻简单音素碰撞叙事，对 tokenizer 设计很有启发。残差退化仍随信息容量下降，属预期。评测侧重重建可懂度，未直接测下游自回归 TTS 延迟与质量权衡。

