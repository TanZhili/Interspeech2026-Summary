# New Architecture and Analyses for ASR and Speech LMs

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：9
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场在 ASR 与语音/文本语言模型交叉处并行推进两类工作：一类改架构或解码范式（动态旋转位置编码、扩散语言模型重打分与联合解码）；另一类做表征与感知分析（词是否独立于音素被编码、可读性是否预测 WER、嵌入中的语言学信息可及性），并延伸到 ASR 转写文本的风格匿名化隐私。

架构侧，CD-RoPE 让旋转时间索引随局部声学上下文连续弯曲，直指离散均匀时间索引与连续语音语义的错位；扩散 LM（MDLM/USDM）进入假设重打分，并与 CTC 帧级分布联合生成候选，体现双向注意力与并行文本生成对识别准确率的增益。

分析侧，通过残差化剔除音素信息后仍可测到后期层的词表征，说明“能分词”不等于“只编码词形”；可读性与 WER 近乎解耦，挑战把文本复杂度当作机器可懂度代理的历史假设；探测显示嵌入对声学—语音学属性线性可及，对形态/句法结构则弱。隐私侧则把 stylometric 指纹风险从书面文本延伸到会议/客服 ASR 转写。

## 论文技术总结

# Convolutional Dynamic Rotary Positional Encoding

- 论文编号：1312
- 报告人：Euijin Hong
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hong26_interspeech.pdf

## 问题
RoPE/RelPos 等位置编码依赖均匀离散时间索引，与语音特征连续、信息密度不均的特性错位；纯 RoPE 在 ASR 训练中还可能发散。Branchformer 的注意力支路缺少中间卷积，局部时序建模不足。

## 方法
提出 **CD-RoPE**：用轻量 depthwise-separable 1D 卷积从输入特征预测连续时间偏移 \(\Delta t\in[-1,1]\)（tanh + ReZero 式可学习 \(\alpha\)），加到基索引后再乘逆频率，得到 \(\hat{\Theta}_{t,i}=(t+\Delta t)\cdot\theta_i\)。在全维特征上算偏移再分头，保留 RoPE 谐波结构；故意调制时间索引而非直接调频率，以避免早期训练不稳定。嵌入 Branchformer 注意力支路。

## 实验与结果
SpeechBrain 上从零训练 Branchformer（18 编码器 + 6 解码器），LibriSpeech 960h；对比 RelPos（109.8M）与 CD-RoPE（107.6M）。
- WER：dev-clean 2.02→1.96；test-clean 2.17→2.13；test-other 5.07→4.95；少 2.2M 参数。
- McNemar 在 test-other 上显著（p≈0.043）。
- Speech Robust Bench：中等强度下 9 类扰动中 7 类更好，时序扰动优势最大（如 severity 4 的 tempo↑：10.73→8.63）。
- 核大小在 100h 子集上对 WER 不敏感（k=7/9/11 约为 5.44–5.47）。

## 结论
CD-RoPE 在 Branchformer 上全面优于 RelPos 且参数更少；鲁棒性增益主要落在时序扰动上，支持“时间轴弯曲”假设。作者刻意只评 Branchformer，向 Conformer 等带卷积结构迁移留作未来工作。

## 点评
把动态性放在“时间索引”而非旋转频率上，是兼顾稳定性与相对归纳偏置的合理设计；对 Branchformer 尤其对口，因为注意力支路本来缺局部卷积。增益幅度不大，且单数据集单 seed、无组件消融，推广性仍需更多证据。


# Diffusion Language Models for Speech Recognition

- 论文编号：2070
- 报告人：Davyd Naveriani
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/naveriani26_interspeech.pdf

## 问题
自回归 LM 重打分/联合解码受限于从左到右顺序，速度受限。离散扩散 LM（MDLM、USDM）可双向建模与并行生成，但如何系统用于 ASR 重打分，以及如何与 CTC 做 token 级联合解码，此前缺乏系统研究。

## 方法
1. **重打分**：对 CTC n-best 用 \(\lambda_{\mathrm{CTC}}\log P_{\mathrm{CTC}}+\lambda_{\mathrm{DiffLM}}F_{\mathrm{DiffLM}}-\lambda_{\mathrm{prior}}\log P_{\mathrm{prior}}\)。对 MDLM 提出样本级/全局 mask 归一化及耦合互补 mask 打分，替代高方差的序列长度归一化；USDM 用其 ELBO。
2. **CTC–USDM 联合解码**：从 CTC greedy 序列与噪声水平 \(t_{\mathrm{start}}\) 起步；每步用 CTC 帧分布（按折叠后首帧对齐、去 blank）与 USDM 全词表标签分布线性组合后 ancestral sampling，迭代去噪。

## 实验与结果
LibriSpeech：CTC 在 960h 训练；DiffLM 在 LS LM 文本 + train-other 转写上训 5/10/25 epoch，DiT 约 110M/340M，SentencePiece 10k。
- MDLM 重打分（样本级归一化，K=256）：dev-other 最优约 4.47%（25 ep），优于序列归一化 4.62%（5 ep）与 CTC 基线 5.08%。
- USDM 重打分：K=256 时约 4.72%。
- CTC–USDM 联合：\(t_{\mathrm{start}}=0.1,L=1\) 达 4.66%；RTF 约 0.003，接近 CTC-only 0.002。
- 自回归 LM 仍更强（first-pass 3.86%，rescoring 4.19%），但扩散重打分 RTF 明显更高。

## 结论
MDLM/USDM 均可提升识别；mask 归一化对 MDLM 重打分很关键；USDM 的全词表分布使其能与 CTC 高效联合解码，单步即可明显降 WER。当前数据规模下自回归 LM 仍更准，作者认为更长训练与更大模型可能缩小差距。

## 点评
贡献重点是“把扩散 LM 接到 ASR 管线”的可操作配方：打分归一化与 CTC–USDM 联合。联合解码用极少额外步数换可观增益，工程吸引力大；但与强自回归 LM 仍有差距，且 MDLM 尚未纳入联合框架，扩展价值取决于能否在保持 RTF 的同时缩小精度鸿沟。


# Do speech foundation models really learn words?

- 论文编号：2676
- 报告人：Robin Huo
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/huo26_interspeech.pdf

## 问题
自监督语音基础模型在探测任务上能区分词身份，但这可能只是因为编码了音素形式（能指），而非独立于局部语音内容的词表征。需要把音系信息剥离后，检验是否仍保留“词”层面的信息。

## 方法
对英文预训练 HuBERT-base 与 wav2vec 2.0 base 的卷积末层及 12 个 Transformer 层，在 LibriSpeech dev-clean 帧级对齐音素/词标签上做线性探测。用 ridge 回归从 one-hot 音素（或左右 diphone、triphone）预测嵌入并残差化，再测词身份分类准确率；先标准化再残差。并在 HuBERT 第 9 层上做无监督词发现（边界检测 + k-means，k=13967），比较残差前后 NED/F1/R。

## 实验与结果
- 残差后音素探测准确率大幅下降（验证有效），但未完全到随机（众数音素约 11.6%）。
- 词探测：原始表示在中后层峰值超约 90%；去掉音素后整体模式仍在；去掉 triphone 后多数层大降，但 HuBERT 9–10 层、wav2vec 7–8 层对长度 3–6 词仍远高于按长度/triphone 众数基线。
- 词发现：去音素残差可改善 NED/F1/R（如相对 Malan et al. 设定 NED 0.508→0.463）；去 diphone/triphone 则损害切分。

## 结论
后期层存在一定程度上独立于局部音系内容的词身份信息；简单残差化可增强词发现中的更高层语言学可及性。局限：需要音素对齐标签；残差未完全抹净线性音素信息；排除单音素词会影响完全去除效果。

## 点评
用线性残差直接拆开“能指 vs 所指”混淆，比单纯余弦相似度更干净。结果说明模型不只是记短 n-gram，但仍不能断定编码了语义/句法；对下游的实用价值受限于对齐标签需求，更适合作为解释与诊断工具。


# Readability Does Not Predict Speech Recognition Errors: Contrasting Human and Machine Perception.

- 论文编号：2439
- 报告人：Baptiste Ramonda
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ramonda26_interspeech.pdf

## 问题
人类在噪声中依赖可读性补偿理解，早期 ASR 也常因文本复杂度/困惑度升高而 WER 变差。现代端到端 ASR 是否仍对文本可读性敏感，还是已与语言学复杂度解耦？真人口语会随难度改变发音，需控制声学混杂。

## 方法
用 CLEAR 语料（4718 段）经 Amazon Polly TTS 固定语速/韵律，再加 DEMAND babble（SNR 0/10/20 dB）与 OpenAIR 混响（0.1/0.9）。可读性用多指标合成的 Global Readability Index（GRI），并对照 Bradley-Terry 简易度；可懂度用 WER；另看预测熵与压缩比作“认知努力”代理。ASR：PocketSphinx、Vosk、Wav2Vec2 Base、Whisper Tiny/Medium。并用 LibriSpeech train-clean-100 拼接自然语音做验证。

## 实验与结果
- GRI 与人类 BT 简易度强负相关（r=−0.56）；原文与转写 GRI 相关 r=0.97。
- 干净条件：Whisper Tiny/Medium 与 GRI 近正交（r≤0.03）；Wav2Vec2 r=0.24、Vosk r=0.14；PocketSphinx r=0.05（作者认为是高错误率饱和）。
- 与人类感知难度均呈负相关（r∈[−0.35,−0.19]）。
- Whisper Tiny 在 0 dB 噪声下与 GRI 仍几乎无相关（r=0.06）；自然语音上 r=−0.02。
- 预测熵与 GRI r=−0.01，压缩比 r=−0.08，未见复杂度带来的内部犹豫或简化。

## 结论
现代 E2E ASR 的转写错误与文本可读性近乎无关，即使在噪声/混响下也成立；声学转写已独立于文本结构复杂度。这支持 listenability 设计中可读性与 ASR 模块可分开优化。仍与人类感知难度保持相关，非结构因素有待厘清。

## 点评
TTS 控制把“文本难度→发音变化”拆开，结论对 Whisper 类模型很清晰。PocketSphinx 的低相关被解释为误差饱和，提醒架构对比要看误差底线。残余的“人类难度相关”说明 ASR 仍踩在某些与人共享的难例上，只是不是经典可读性公式能抓住的那一类。


# Probing Linguistic Information in Speech Embeddings: A Diagnostic Analysis across Acoustic and Structural Domains

- 论文编号：905
- 报告人：Simon Gonzalez
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalez26b_interspeech.pdf

## 问题
现代语音嵌入广泛用于 ASR 与语音–语言模型，但其语言学可解释性不足：不清楚哪些声学/语音学/更高层结构信息可被线性读出，以及信息如何沿层级分布。

## 方法
在 FLEURS 子集（36 语、43185 条、约 136 小时）上，用 W2V-BERT 2.0（约 600M，多语）提取帧级嵌入，时间维 median pooling 得话语向量（长句切 10 秒再 median）。从音频提取声学（jitter/shimmer、谱平坦度、ZCR、centroid 等）、语音学（时长、语速、pitch range、RMSE）与结构特征（Stanza：UPOS 熵、lemma 复杂度、从句复杂度、CTTR）。用 Lasso 回归学习嵌入→特征映射，五折选参，报告 train/test \(R^2\)。

## 实验与结果
线性关联强度随层级递减：
- 声学最强：Shimmer \(R^2\)=0.59，Flatness 0.56，ZCR 0.51 等。
- 语音学：Duration 0.51，Speech Rate 0.32；RMSE 0.19、Pitch Range 0.15 较弱。
- 结构：CTTR 0.43 仍可观；UPOS 0.04、Clause 0.02、Lemma 近 0。

作者强调是分布式、梯度式关联，而非维度与语言学单位一一对应。

## 结论
嵌入对贴近信号实现的声学/时序特征最敏感，词汇复杂度有可测关联，形态与句法复杂度线性可及性有限。结果受数据集、特征与模型选择约束；嵌入宜与符号语言学分析互补，尤其利好低资源场景中的可扩展诊断。

## 点评
这是一份清晰的“能线性读出什么”的诊断图：靠近声学的特征最强，句法最弱，符合自监督目标更贴信号的直觉。Median pooling 可能抹掉跨帧结构关系，因此弱句法关联未必等于模型完全不编码结构；若要追问更高层信息，需要更强探测或保留时序结构的读出方式。


# I Am No One: Style-Aware Paraphrasing for Text Anonymization

- 论文编号：3175
- 报告人：Ahmed Sohair Khan
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/khan26b_interspeech.pdf

## 问题
即使去掉显式标识，作者归属模型仍可凭稳定文风指纹重识别用户；该风险也延伸到会议/客服 ASR 转写。差分隐私文本匿名常严重损伤可读性与效用，而一般改写又缺少对风格标记的显式控制。

## 方法
两模块提示式流程（基座主要为 LLaMA-3.2-3B-Instruct，并测 MiniCPM3-4B）：
1. **风格画像**：从每位作者 K=5 样本，让 LLM 总结句长、词汇、语气、标点四维可读 profile；可消融单维。
2. **风格引导改写**：把 profile 写入提示，要求压制所述风格标记并保留语义；对比 semi-guided（只要求中性风格）与 unguided 改写。

评估 AUTHOR10（博客，10 作者）与 ILLINOIS9（短评，9 作者）；对比 DP-Prompt / Quasi-DP / Non-DP、ALISON；效用用余弦相似度、GPT-2 PPL、加权 KL；隐私用 BLEU、归属 F1、相对增益 γ 与流畅度感知 γf。

## 实验与结果
- 归属 F1 相对原文降约 60–70%：AUTHOR10 66.45→26.02（LLaMA），优于 ALISON 29.53；ILLINOIS9 76.78→20.76。
- PPL 接近原文（AUTHOR10 42.47 vs 41），远好于 ALISON（368）与严格 DP（ε=25 时约 8770）。
- Full profile 总体最稳；ILLINOIS9 上 Length-only 隐私增益可略更好。
- Style-guided 相对 semi-guided：隐私接近但效用与信息保留更好；纯 paraphrase 隐私与效用均更差。
- 补充：方法感知白盒攻击下 ILLINOIS9 攻击 F1 仍可从 77 降到 35；Yelp/IMDB 外域归属 F1 可降超 85%。

## 结论
显式风格画像引导的改写能在保持语义与可读性的同时大幅削弱作者归属信号，优于噪声型 DP 与无指导改写。局限包括依赖预设风格维度、指标可能混淆风格抹除与内容损失、尚未在 ASR 转写上系统验证。

## 点评
把匿名化重新定义为“可控风格变换”而非加噪，抓住了归属攻击真正利用的信号。对 ASR 会议文本有明确动机，但正文实验仍是博客/评论；若转写噪声与口语体改变风格线索，效果可能不同于干净文本。攻击者若利用残余内容而非纯风格，仍需与内容脱敏策略配合。

