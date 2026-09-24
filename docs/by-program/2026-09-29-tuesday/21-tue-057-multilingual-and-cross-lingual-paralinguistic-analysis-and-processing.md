# Multilingual and Cross-Lingual Paralinguistic Analysis and Processing

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：3
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场追问副语言任务究竟多“语言无关”。零样本跨语情感识别用监督对比学习做跨语情感对齐，并用说话人对抗抑制说话人线索；系统性工具 Cross-Lingual Transfer Matrix（CLTM）在性别识别与说话人验证上量化供体—受体语言对的迁移结构。合成增强方面，八种声线克隆模型在五项副语言（含临床）任务上多数能保留信号，并把英语临床语音克隆到日语后优于原始跨语迁移。

与人类对比，英语单语听者与英语单语 SLM 在法/日/希/泰基本情感上均显著高于随机，支持普遍性，但人类更擅负面情绪、模型更偏快乐/惊讶。说话人嵌入的跨语泛化在粤—英双语材料上与人类评分及声学结构对照；魅力韵律在卢森堡语—法语双语政治家演讲中，说话人身份解释大部分方差，语言仍带来系统但较小的差异。整体趋势是：用矩阵化评测、对抗/对比学习与克隆增强，把“副语言可跨语”从口号变为可度量、可增强的性质。

## 论文技术总结

# Learning Emotion-discriminative Representations for Zero-Shot Cross-Lingual Speech Emotion Recognition

- 论文编号：1170
- 报告人：Jinyi Mi
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mi26_interspeech.pdf

## 问题
零样本跨语 SER 中，仅源语标注训练时分布失配严重；许多方法仍需目标语无标注语音或语言标签，且多减分布差而未显式对齐情感结构。

## 方法
在源语/非目标情感语音上：预训练特征提取器 + 情感分类；监督对比学习拉近同情感、推远异情感跨语样本；说话人对抗分类（GRL）抑制说话人线索。九组零样本设置（英/中/德/法互为源–目标）。指标 UAR 与 Macro-F1。

## 实验与结果
Proposed 平均 UAR/F1=82.26%/81.96%，相对 Baseline 2 提升约 9.05/9.38 点，最接近 upper bound（91.92/91.41）。去监督对比学习降约 5.40 UAR；去说话人对抗降约 2.15 UAR。表征可视化显示情感簇更跨语对齐。

## 结论
对比对齐情感结构 + 说话人对抗可在仅少量语言标注下提升零样本跨语 SER；两者均有贡献，对比项更关键。

## 点评
把“跨语”问题明确成情感条件表征对齐，消融干净。语种仍偏欧亚主流、任务为表演/实验室情感设定的典型局限；相对需目标语无标注数据的 DANN 类方法，零样本约束更强，实用价值更高。


# Quantifying Cross-Lingual Transfer in Paralinguistic Speech Tasks

- 论文编号：2745
- 报告人：Federico Costa
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/buitrago26_interspeech.pdf

## 问题
副语言任务常被视为较语言无关，但跨语仍见性能下降；既有研究多限少数语对或任务特异设定，缺少可比较的、基于下游性能的 donor→target 迁移度量。

## 方法
提出 Cross-Lingual Transfer Matrix（CLTM）：用等量额外目标语数据的 self-gain 归一化 donor 数据带来的 cross-gain，CLTM[i,j]=Δi←j/Δi←i。在固定 mHuBERT-147 上对 44 语微调性别识别（macro-F1）与说话人验证（AUC），10 种子平均；用 RFD1、Asymrel、prop+ 等汇总诊断。

## 实验与结果
性别识别 CLTM 接近全 1 理想：RFD1=0.162，prop+≈99.97%，行相似 cosrows≈0.990，迁移近乎语言无关。说话人验证强烈依赖语言：RFD1=2.970，prop+仅 8.93%，正迁移更集中在语系内（intra-family+ 41.68% vs GR 的 4.98%），负迁移普遍。

## 结论
CLTM 可系统量化副语言任务的跨语迁移几何；同为“副语言”，性别识别近语言无关，说话人验证则高度语言依赖。

## 点评
贡献是可复用的矩阵度量与对照协议，澄清“副语言=跨语无感”的笼统说法。单骨干、单 epoch、两任务限制外推；矩阵解释依赖 self-gain>0 等有效性条件，极端低资源语对需小心。


# Synthetic Speech, Real Signal: Paralinguistic Preservation and Cross-Lingual Augmentation via Voice Cloning

- 论文编号：2993
- 报告人：Roseline Polle
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/polle26_interspeech.pdf

## 问题
合成语音增强在 ASR 等语言任务中常见，但在情感、临床生物标志物等副语言任务中研究较少；语音克隆通常只评 WER、说话人相似度与 MOS，不清楚克隆后是否保留下游副语言分类所需信号。临床抑郁/焦虑检测几乎全是英语标注数据，低资源语言难以直接迁移。

## 方法
评测八个开源克隆模型（XTTS v2、Zonos、E2-TTS、F5-TTS、OpenAudio S1-mini、CosyVoice 2/3、MaskGCT）。流程：Whisper medium 转写，去首尾静音并截断至 10s；两种文本条件——Repeat（复述原转写）与 Standard（所有说话人读同一固定段）。特征用 WavLM Large 1024 维嵌入，Logistic Regression（L2，C=0.001）做分类，指标为 AUC，并定义保留分数 \(P=(A_c-0.5)/(A_r-0.5)\)。RQ1：公有数据与自有英语临床语料上，Real vs Cloned 五折说话人无关交叉验证。RQ2：将英语临床语音克隆为日语（Qwen 3 235B 翻译），对比 in-language JP、raw EN→JP、cloned EN→JP。RQ3：说话人嵌入余弦相似度与 AUC 退化的相关性。

## 实验与结果
数据含 IEMOCAP、MELD、MUSTARD、VCTK 与自有 EN（约 82k 样本）/JP（约 14k）临床集。RQ1：176 组配置均显著高于随机；相对 Real 中位退化 3.2 pp，中位 \(P=0.87\)；Repeat 下五模型 \(P\geq0.90\)，Standard 中位 \(P=0.75\)。RQ2（N=10k EN 说话人）：四模型克隆条件均显著优于 raw EN（如 OpenAudio 抑郁 +3.3 pp，CosyVoice 3 焦虑 +4.0 pp），仍低于 JP in-language 参考。缩放分析约从 1k 说话人起克隆优于 raw baseline。RQ3：临床与 IEMOCAP 上说话人相似度与退化强相关（如 general \(r=0.87\)），噪声语料上较弱。

## 结论
现代克隆模型在 Repeat 下可保留多数副语言判别信号（最优 >90% above-chance），并可用作英→日临床增强，优于原始跨语种迁移；与 in-language 仍有差距。局限：仅一对语言、分类器固定为 LR、特征仅 WavLM、临床数据不可公开复现。

## 点评
把“克隆质量”直接接到下游副语言 AUC，并用 Repeat/Standard 拆开语义与副语言贡献，设计清楚。跨语增强在段落朗读上也有增益，说明收益不全来自译文语义。脆弱点是依赖自有临床语料与单一 WavLM+LR 探针，以及英→日外推是否成立未知。


# Universality of Speech Emotion Recognition in Humans and Speech Language Models

- 论文编号：3061
- 报告人：Yuka Tatsumi
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/tatsumi26_interspeech.pdf

## 问题
人类能在不熟悉语言中较好识别语音情绪（universality），但英语单语 ASR 编码器是否同样具备跨语种情绪识别、且是否与人类在情绪类别与反应偏向上一致，尚不清楚。

## 方法
人类侧：Prolific 招募英语单语听众（分析用有效样本约 101 人量级，文中 119 人录音后排除 18 人），对法语、日语、希腊语、泰语情绪语音做六选一（happy/sad/angry/fear/surprise/neutral）。模型侧：冻结 Whisper-medium.en 与 HuBERT-large-ll60k，在各层做全局平均池化后训 \(L_2\) 多项 Logistic Regression 探针；仅用英语 ESD、CREMA-D、RAVDESS 训练，非英语刺激与人类完全相同且不做适配。主分析层按英语验证集最优选取（Whisper L17、HuBERT L11）。

## 实验与结果
人类总体准确率 43.8%（机会水平按最频类 sad 为 21.4%），中性最高（80.0%），happy 最低（22.6%）。非英语上 Whisper 39.0%、HuBERT 48.3%。bootstrap：Whisper–人类差异不显著（−1.4%，CI 跨 0）；HuBERT 显著高于人类（+6.8%）。情绪准确率排序人类与模型明显不同；错误反应中人类默认 neutral（32.4%），Whisper 默认 happy（52.4%），HuBERT 默认 surprise（53.0%）。

## 结论
冻结单语 ASR 编码器也表现出跨语种情绪识别 universality，整体可达或超过人类；但类别表现与反应偏向与人类不同。局限：英语训练语料选择、Whisper 英语变体是否绝对无非英语音频、每语一种数据集、情绪标签不完全对齐。

## 点评
用相同刺激直接对比人与探针，把 universality 从“高于随机”推进到“系统差异”。强在拆开总体准确率与默认标签偏差。脆弱点是 acted 语料与探针层选择：主分析层按英语最优选取，非英语最优层可能不同，文中亦提示结果为下界。


# Human-like cross-language generalisation in deep neural speaker embeddings and its acoustic foundations

- 论文编号：858
- 报告人：Tianze Xu
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/xu26f_interspeech.pdf

## 问题
说话人嵌入的跨语种泛化（如英粤）对合成与识别重要，但相对人类感知与声学结构的对齐研究不足；既有工作多停留在较早 MFCC 系统或单语相似度相关。

## 方法
基于 SpiCE 语料 10 名粤英双语女性说话人的节日问候短句，沿用既有 40 名听者（20 双语 / 20 英语单语）的 9 点声纹相似度评分（同/异说话人 × 粤/英/混合语言，共 220 对）。从 18 个 Wespeaker 预训练模型（ResNet、SimAM、ECAPA、CAM++ 等）及粤语微调版本提取嵌入，用余弦相似度；声学侧提取 29 个变量（语速、f0、共振峰、谐波/噪声等）。用线性混合模型预测机器相似度；用 RSA 将机器 RDM 与感知/声学 RDM 相关。

## 实验与结果
机器相似度同说话人显著高于异说话人（0.78 vs 0.60）；混合语言条件同–异对比减弱；粤语微调未提升相似度，预训练略高于微调。机器–感知 RSA 中等相关（均值 ρ≈0.44）；听者语言背景与刺激语言有交互，但微调状态无显著效应。机器–声学相关最强多为语速、F1–F4 均值与 SHR；粤语更偏 F2/F4 与高频谐波差，英语更偏 f0、FD、CPP。

## 结论
深度说话人嵌入在跨语种声纹相似度上与人类行为大体平行：能区分身份、对语言切换敏感，并依赖部分语言敏感、大体共享的声学线索；小规模粤语微调未见收益。局限含粤语微调数据量、短句样本与说话人数。

## 点评
把 LMM 身份/语言效应与 RSA–声学拆解绑在一起，证据链比单纯“跨语识别准确率”更贴近认知对齐问题。微调无增益与人类“语言背景不显著”平行，值得注意；若微调数据过小导致表征扰动而非增益，外推到大规模粤语适应仍需验证。


# Speaker or Language? Explaining Variance in Charismatic Prosody Across Luxembourgish and French

- 论文编号：26
- 报告人：Nina Hosseini-Kivanani
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/hosseinikivanani26_interspeech.pdf

## 问题
魅力语音的副语言线索多在单语、准备性语料中研究；双语政客在卢森堡语（认同语）与法语（高声望机构语）间切换时，魅力相关韵律由说话人个体还是语言主导，方向如何，尚不清楚。

## 方法
10 名卢森堡政治公众人物（5F/5M），每人各 20 句自发卢森堡语与法语，共 400 句，情境尽量可比。LuxASR 转写、WebMAUS 对齐、ProsodyPro 提取 41 维声学–韵律特征（F0、强度、时长、BID/音质等），z 标准化。PCA 概览；线性混合模型 `feature ~ Language + Gender + Duration + (1|Speaker)`，用 ICCSpeaker 与 Language 边际 \(R^2\) 分解方差；Language×Gender 交互检验 RQ1，FDR 校正。

## 实验与结果
PC1/PC2 解释约 31.4%/16.8% 方差，语言在空间上有系统但重叠的位移。Speaker ICC 中位 0.56，Language 中位仅约 0.5% 方差。41 特征中 18 个 Language 效应 FDR 显著：法语更高 shimmer、句末 F0（\(d=0.90, 0.68\)）；卢森堡语多数中频能量带更高（如 2750 Hz \(d=-1.67\)）。由六维线索合成的魅力指数无可靠语言主效应（\(d=-0.03\)）。

## 结论
说话人身份主导魅力相关韵律方差；语言带来系统但局部的音质/谱与轮廓差异，与社会语言学角色相符，却未形成整体“哪一语更魅力”的优势。局限：仅 10 人政治语体、无听者主观评分、句内容非平行。

## 点评
用 within-speaker 双语设计直接回答“说话人还是语言”，方差分解结论清晰。复合魅力指数无语言效应，提醒勿把单特征差异直接等同全局魅力。脆弱点是声学–感知相关依赖既有文献，且句内容跨语不完全平行可能混入话题效应。

