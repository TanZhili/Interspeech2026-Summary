# Speech and Language Representation

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：4
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场涵盖模仿语音说话人嵌入、语音表征是否编码语系结构、维度独立性的信息论度量、非言语发声上的说话人验证、声—脸关联图挖掘、神经转码后的传统编解码器溯源、阿联酋阿拉伯语人工标注语料、法证子带倒谱分析，以及低资源澳大利亚原住民语言识别的混合持续学习。

主线是表征中“身份—语言—情感/病理—编解码痕迹”如何纠缠与解耦，以及低资源方言/濒危语言如何获得可用资源与防遗忘适应。

## 论文技术总结

# ECAPA-TDNN-based Speaker Embedding Framework for Voice Mimicry Assessment

- 论文编号：1535
- 报告人：Bhasi K.C.
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kc26_interspeech.pdf

## 问题
如何客观评估模仿语音与目标说话人的接近度；需融合谱与韵律线索，并使自动排序与听感 MOS 一致。

## 方法
在 MIMICz（20 名人）上：从谱特征（MFCC、chroma、tonnetz、滚降/带宽/通量/质心等）与韵律（响度、音高、语速、shimmer、tempogram 等）提取说话人嵌入；比较 x-vector、ECAPA（E-vector）、d-vector；稀疏自编码器增强；分数级融合；DNN 预测与感知测试最优模仿艺人是否一致（top-1 hit）。

## 实验与结果
融合谱+韵律一致优于单通道。增强 ECAPA 融合 top-1 hit 75%，高于 x-vector 55%、d-vector 65%，并优于作者所列先前方法（如 60%/50%/41%/72%）。t-SNE 显示增强后簇更紧、边界更清。

## 结论
注意力增强的 ECAPA 嵌入 + 谱–韵律融合更适合模仿质量排序，更能对齐人工 MOS 最优艺人。

## 点评
把“hit MOS 冠军”当作任务定义，比单纯说话人验证更贴模仿评测。数据集规模与名人集合有限；分数融合权重敏感（文中有 α 曲线）。未强调跨性别/跨语言模仿等更难设定。


# Do speech representational spaces encode language family structures?

- 论文编号：2418
- 报告人：Emily Gaughan
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/gaughan26_interspeech.pdf

## 问题
多语语音表示已知含语种信息，但是否编码有意义的语系/谱系结构仍不清晰。现有可视化难以量化，监督 probe 只看固定层级且可能扭曲显著性，而树结构评估在语音域尚未系统开展。

## 方法
用 Common Voice 23.0 测试集中 230 个 languoid（26 语系）各约 100 条，取六类模型中间层隐状态均值后算语种间余弦距离，再以 WPGMC 凝聚聚类建树，与 Glottolog 金标准树比较。评估六种树距离（PARTITION/Robinson–Foulds、PATH、QUARTET、NYE、P-RF、P-QUARTET），并与 ASJP 的 LDND 词典统计上线对照；另用 logistic regression / k-NN / LDA 做顶层语系 probe。模型含 XLS-R、Whisper、XEUS、mHubert-147、ECAPA-LID、Whisper-LID。

## 实验与结果
- 神经表示中 Whisper-LID 平均树距离最好（Avg. Tree Dist −0.80），XEUS 最差（1.14）；均明显弱于 LDND（−1.99）。
- LID 目标整体优于通用编码器；树指标与 probe 对“最佳空间”判断不一致（probe 更看好 mHubert-147）。
- 多数模型在“已见语种比例升高”时树距离变差（如 XLS-R r=0.62）；Whisper / Whisper-LID 相关性弱或无显著相关。

## 结论
树距离比 probe 更适于评估层级谱系结构；宽语种覆盖（如 XEUS）并不自动带来谱系结构。作者建议联合使用 QUARTET、PARTITION、NYE，慎用对树形敏感的 PATH。局限包括只分析单层、架构与数据未严格对照。

## 点评
把历史语言学的谱系树距离迁到语音表示评估，比“看一眼聚类图”或固定层级 probe 更贴合“语言如何分化”的问题。结果暗示 LID 目标比“覆盖尽量多语种”更利于学到家族结构，而未见语种有时反而更接近 Glottolog，点出“已见语种被分得太开”可能破坏谱系几何——这对多语预训练目标设计有直接启发。


# Quantifying Dimensional Independence in Speech: An Information-Theoretic Framework for Disentangled Representation Learning

- 论文编号：1654
- 报告人：Bipasha Kashyap
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/kashyap26_interspeech.pdf

## 问题
情绪、语言内容与病理标记共享声学通道，但解缠质量常靠下游任务间接判断。若维度间互信息很高，完全解缠可能理论上不可行；需要能量化跨维统计依赖的原则性框架。

## 方法
对手工声学特征划分 Emotional（28维）、Linguistic（33）、Pathological（16）以及 Source（9，声门）/ Filter（32，声道），用 Praat / librosa / openSMILE 提取。以 MINE（EMA 稳定下界）+ CLUB（方差钳位上界）+ KSG（k-NN 非参校验）做有界互信息估计，并按不确定性自适应加权得到最终 MI；再对语义维做 Source–Filter 归因比例。在 RAVDESS、IEMOCAP、L2-ARCTIC、GMU Accent、UA-Speech、MDVR-KCL 的全部 8 种 corpus 组合上评估。

## 实验与结果
- 跨维 Final MI 均 <0.15 nats（Emotion–Linguistic 0.12、Emotion–Pathology / Linguistic–Pathology 0.10），Δ 较紧；Source–Filter 显著更高（0.47±0.38）。
- 归因：情绪约 80% 来自 source；语言与病理分别为 filter 主导（约 60%、58%）。
- 跨组合一致性较好；跨维估计约 8–16 epoch 收敛，Source–Filter 需满 100 epoch。

## 结论
在所考手工特征空间中，三语义维近独立，解缠在理论上可行；Source–Filter 耦合更高但低于经典直觉预期。局限：未验证 wav2vec2/HuBERT 等学习表示、静态特征、分组有重叠、病理/情绪范式覆盖有限。

## 点评
把解缠从“下游涨了几个点”换成可复现的 MI 上下界，方法论价值大于任何单一数字。结论强依赖手工特征与操作化分组，作者也明确承认：测到的是这套特征集的依赖，不是抽象“情绪/语言/病理”本身。对编码器设计的启示（分路、按维对齐 source/filter）需在学习表示上再验证才站得住。


# Speaker Identity in Non-Verbal Vocalizations: Conditional Distillation and Mixture of Experts Approach

- 论文编号：77
- 报告人：Yi-Cheng Lin
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/wei26b_interspeech.pdf

## 问题
表情 TTS/VC 越来越多生成笑声、咳嗽等非言语发声（NVV），需要说话人验证同时覆盖言语与 NVV。现有 SV 在 NVV 上泛化差，直接在 NVV 上微调又会灾难性遗忘言语验证能力。

## 方法
冻结 Data2Vec 前端 + ECAPA-TDNN，插入 MoE：Post-Fusion MoE 与 Inter-Layer Residual MoE（IR-MoE，每层后接适配器）。训练总损失含 AAM-Softmax、事件引导路由约束（负载均衡 + 事件内 KL + 事件间余弦间隔）、仅对言语样本生效的条件蒸馏（对齐冻结 WavLM-SV teacher）、以及跨域同说话人正样本的监督对比损失。数据用 NonverbalTTS（17 小时，10 类 NVV；1314/46/147 说话人划分），MFA 切分言语与 NVV。

## 实验与结果
- Zero-shot wavlm-base-plus-sv：SvS EER 5.60%，但 NvS/NvN 达 38.93%/39.13%。
- 自训基线中 Data2Vec+ECAPA NvS 23.33%；提出的 MoE-2（4 experts）NvS 22.66%、NvN 27.52%、SvS 9.24%。
- 消融：无蒸馏时 SvS 13.17%、NvS 24.95%；加条件蒸馏后分别到 9.24%/22.66%。专家数 4 时 NvS 最优，再增专家 NvS 略降但 SvS 可继续改善。

## 结论
条件蒸馏 + IR-MoE 在缩小 Speech–NVV 域差的同时显著缓解言语遗忘；中间层分离域、最终嵌入用对比统一说话人流形。局限：相对 VoxCeleb2 规模，NonverbalTTS 数据量小，SvS 仍不及 zero-shot WavLM-SV。

## 点评
核心洞察是“NVV 不是再加一类噪声，而是异构声学域”，用条件蒸馏只在言语上贴 teacher，避免把 NVV 硬拽进言语流形，设计干净。10 类 NVV 系统评估是贡献；但 Breath 占样本 67%+，稀有类（鼾声、喷嚏等）是否真正学到仍存疑，后续应看按类分解或合成 NVV 的零样本评测。


# GMOD: Voice-Face Association Learning via Graph Mining and Orthogonal Disentanglement

- 论文编号：432
- 报告人：Ju Zhang
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/wang26h_interspeech.pdf

## 问题
无监督声–脸关联学习面临两类难点：跨视频同说话人被当成假负样本；模态私有属性渗入共享嵌入干扰跨模态对齐。聚类/原型伪标签在训练早期不可靠，难以刻画身份局部分布。

## 方法
提出 GMOD：(1) 正交解缠——每模态经并行编码器得到共享身份 \(z^{\mathrm{id}}\) 与私有 \(z^n\)，软正交损失 + 拼接重构 MSE；(2) 图引导正样本挖掘——对视频级 \(L_2\) 平均原型建跨模态相似图，以 voice→face k-NN 再反向回填，\(k\) 从 20 线性衰减到 8（课程式），用多正样本 InfoNCE（双向）。骨干为 ECAPA-TDNN（声）与 FaceNet（脸），在 VoxCeleb1 上无监督训练（901/100/250 身份划分，训练不用身份标签）。

## 实验与结果
相对 Pins、SL、CMPC、PAEFF 等：验证 AUC 87.73%（U）/77.37%（G）；1:2 匹配双向约 87.04%；检索 mAP V2F/F2V 7.14%/7.59%，均为表中无监督最优。消融：去图、固定 \(k\)、去正交+重构均下降；私有支路反匹配 AUC≈49.28%，说明私有支路几乎不含身份。1:N 匹配在 N=10 时双向准确率仍 >45%。

## 结论
全局相似图 + 课程挖掘缓解假负样本，正交解缠稳住跨模态共享身份特征；在 VoxCeleb1 验证/匹配/检索上优于现有无监督方法。未来拟扩展到多语复杂场景。

## 点评
相对“先聚类再伪标”路线，直接用全局图把潜在正样本抬进分子，更贴合早期对齐不稳时的假负问题；voice 锚定图优于 face 锚定也符合“声比脸跨视频更稳”的经验。正交+重构是经典共享–私有分离套路，私有支路近随机的反匹配测试是有说服力的自检。增益幅度相对 SL/CMPC 不夸张但全面，更像工程上把两块关键拼稳。


# Tracing the Origins: Legacy Codec Identification in Neural Audio Transcoding

- 论文编号：2354
- 报告人：Shinee Youn
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/heo26b_interspeech.pdf

## 问题
RVQ 神经音频编解码（EnCodec 等）把信号变成离散 token，传统基于线性假设的编解码取证在神经转码后失效；legacy→neural 叠加伪迹下能否识别原始传统编解码器，尚缺乏系统框架。

## 方法
输入 EnCodec RVQ token，经预训练码本嵌入后过三模块：(1) Layer-Causal RVQ Transformer（层间因果掩码注意力建模层次依赖）；(2) Dynamic Layer-wise Attentive Aggregator（全局层权 + 时变层注意后沿层聚合）；(3) Temporal Context Transformer（捕捉预回声/带宽等时序签名）→ MLP 分类。数据：VCTK 先经 FFmpeg 的 MP3/AAC/Opus/Vorbis/G.711 再 48 kHz EnCodec 转码，比特率 32–128 kbps，说话人无关划分。

## 实验与结果
- 固定比特率编解码识别：32/64/96/128 kbps 准确率 99.99%/99.70%/98.36%/97.32%（均 >97%），低比特率更易辨。
- 固定编解码比特率分类：AAC/Vorbis >99%；MP3 84.43%、Opus 71.01%（96 vs 128 kbps 易混）。
- 18 类联合识别：完整模型 Acc 89.34%、Macro-F1 89.31%，相对 CNN+MLP 基线（73.71%）提升 >15%；LCR-Trans 贡献最大。

## 结论
legacy 编解码伪迹在神经转码后仍可检测；固定比特率识别很强，高比特率 MP3/Opus 与部分低比特率跨编解码混淆仍是难点。未来需扩编解码覆盖并加强高比特率分辨。

## 点评
把 NAC 当成“传输信道”而非不可穿透黑箱，用 RVQ 层次因果与层注意去拆叠加伪迹，问题定义清晰。近完美的固定比特率识别令人印象深刻，但联合 18 类与 Opus 高码率仍露怯，说明“透明区”伪迹收敛才是真难点。当前仅 EnCodec 转码、VCTK 语音，泛化到音乐/其他 NAC 仍待证。


# Hamsa: A Manually Annotated Emirati Arabic Corpus for Speech and Language Technologies

- 论文编号：1049
- 报告人：Shaikha Alsuwaidi
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/alyafeai26_interspeech.pdf

## 问题
阿联酋方言（Emirati Arabic）在公开语音资源中严重不足；既有阿拉伯语语料多偏 MSA/埃及/黎凡特，Mixat 等 Emirati 资源又偏英阿语码转换，难以支撑纯方言 ASR。

## 方法
发布 Hamsa：从公开 UAE 内容收集、母语者手工转写并二次复核（约 16 人时）的单语对话语料，约 11 小时、4174 段（训练 11,000 段/10.74h，测试 861 段/51.8min）。制定方言正字与音系转写规范，排除重叠语音。在 Whisper-v2/v3、seamless-m4t、mms-1b-all 上以相同超参微调 3 epoch，并与 Mixat 交叉评测；FastConformer、ArTST-v3 仅零样本对照。

## 实验与结果
Hamsa 微调后：
- Whisper-v2：Hamsa WER 42.25%→24.46%，CER 71.91%→8.27%；Mixat 亦改善。
- Whisper-v3：29.69%→23.04% WER。
- mms-1b-all：69.60%→41.55%；Mixat 微调反而在两基准上变差。
方言匹配微调后的 Whisper 可超过零样本阿拉伯语专用模型（FastConformer 35%、ArTST-v3 38.29%）。

## 结论
小而精的方言匹配标注即可显著提升 Emirati ASR，并泛化到 Mixat。局限：规模约 11h、地理覆盖有限、划分非严格说话人无关、无正式 IAA、音频再分发依赖授权（公开版先给转写与采集脚本）。

## 点评
价值主要在资源与规范：把 Emirati 特有的 ق/ج、否定词、阴性形态等正字规则写清，直接解释了 MSA 模型的系统性错误。实验设计用 Mixat 交叉评测避免“只在自家测试集好看”，结论可信。11 小时量级对工业级 ASR 仍偏小，但作为低资源方言微调种子库定位清楚。


# Sub-band Cepstral Analysis of Speaker-Specific Information: A Case Study of Japanese Word /saN/

- 论文编号：303
- 报告人：Shunichi Ishihara
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/ishihara26_interspeech.pdf

## 问题
说话人区分信息在频谱上分布不均；既往子带研究多看连续语流或依赖滤波组，难灵活定位。辅音（擦音/鼻音）上说话人敏感子带位置与强度仍不清楚，法医声纹比对需要可解释的频谱粒度。

## 方法
对全日警科研所 306 名成年男性日语 /saN/（两会话各两遍）下采样到 16 kHz，提 14 维线性频率 CC，经线性变换得 band-limited cepstral coefficients（BLCC），在 0–8 kHz 用 0.6 kHz 宽、0.2 kHz 步进共 38 个子带。用多元核密度估计似然比并 logistic 校准，六折交叉验证，以 \(C_{\mathrm{llr}}\)（及分解）与 EER 评估。实验 1 逐子带；实验 2 融合 2–4 个子带并与全带 LFCC 对照。

## 实验与结果
全带：/a/ \(C_{\mathrm{llr}}\)=0.388 最好，/N/ 0.435，/s/ 0.681 最弱。子带均 \(C_{\mathrm{llr}}\)<1，但 7–8 kHz 普遍偏弱。敏感区大致：/s/ 约 1–2 kHz（另有 ~4、6.5 kHz 局部）；/a/ 最强约 5–6 kHz，另有 ~1.1、2.5 kHz（近 F2/F3）；/N/ 主要在 <4 kHz，尤其 ~0.5–1 kHz。融合四个优选子带可接近全带性能。

## 结论
说话人信息频谱分布不均且随音段变化；/a/、/N/ 强于 /s/；敏感子带并不总与发音/声学直觉一一对应。局限：仅男性、音段少；未来拟扩人群与 Mel/LP 等分析。BLCC 便于在案件中聚焦相关子带并解释结果。

## 点评
把“哪段频谱在说话人比对里值钱”做成可扫的 \(C_{\mathrm{llr}}\) 曲线，对法庭科学可读性比黑盒嵌入更友好。/s/ 在 1–2 kHz 的强线索与高能区直觉不完全一致，提示共现元音或语言因素——作者也谨慎未过度因果化。方法省去重分析信号，适合法医场景里反复试子带组合。


# Hybrid Continual Learning for Low-Resource Australian Aboriginal Language Identification

- 论文编号：1789
- 报告人：Pravina Mylvaganam
- 程序：Wednesday 30 September 2026 / Speech and Language Representation
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/mylvaganam26_interspeech.pdf

## 问题
澳大利亚原住民语言（AAL）极度缺数据，从高资源语种迁移做语种识别易灾难性遗忘；单独用 EWC / ER / KD 在长程适应与数据极不平衡下仍不稳，混合持续学习在 LID 上几乎空白。

## 方法
基于 VoxLingua107 预训练 ECAPA-TDNN LID，提出两套混合 CL：(1) **RA-EWC**：新语言 NLL + 回放缓冲 NLL + Fisher 加权 EWC，仅微调分类头；(2) **CG-KD**：新语言 NLL + EWC + 对冻结 teacher 在高资源类上的温度软目标 KLD，学生端编码器与分类头均可训。评测 Warlpiri（~3h）、Dalabon（~40min）、Dharawal（~11min）的单语适应与多语顺序适应，对照 TL、EWC、ER、KD。

## 实验与结果
单语适应（F1%）：CG-KD 总体最优——Warlpiri overall 93.38（HRL 92.89）、Dalabon 85.68、Dharawal 76.41，且目标语多为 100%；TL 严重伤 HRL（如 Dharawal 场景 HRL 仅 31.25）。顺序适应中，联合训练对最稀缺的 Dharawal 仅 50%/66.67%，而顺序任务下两方法均可达 100%；CG-KD 最佳 overall 约 89.43（DH⇒WA⇒DA）。

## 结论
混合 CL 优于朴素微调与单一 CL；CG-KD 在极低资源下最稳，并支持按任务顺序增量纳入多种 AAL 而不依赖数据均衡。面向濒危语种多语 LID 的可扩展适应路径。

## 点评
把“回放/蒸馏 + EWC”对准 AAL 极不平衡场景，问题抓得准；顺序适应相对联合训练在 Dharawal 上的反差，说明任务级容量分配比硬混数据更关键。测试集绝对规模很小（尤其 Dharawal），100% F1 需谨慎解读方差；HRL 只报 33 语子集也限制了遗忘评估的广度。

