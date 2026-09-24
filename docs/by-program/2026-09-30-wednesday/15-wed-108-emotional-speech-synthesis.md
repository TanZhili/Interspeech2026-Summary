# Emotional Speech Synthesis

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：7
- 论文数：11

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦情感语音合成的可控性、细粒度强度、个性化与评测资源。离散情绪标签正让位于连续 VAD/A-V 轨迹、词级残差向量、轨迹学习与指令嵌入；同时关注文本语义与目标情绪冲突、实时匿名中的情绪泄露，以及听者文化/个体差异。

架构上，扩散/流匹配解码器引入自适应振荡非线性以捕捉尖锐韵律；LoRA/正交分支与双向偏好优化改进条件对比；角色扮演侧出现推理时干预的解耦语音代理。资源与评测上发布大规模情绪 TTS 听感印象数据集，并用 LLM-as-judge 等与人评相关。总体从“说某种情绪”走向可连续、可个性化、可实时控制且可评测的情感表达。

## 论文技术总结

# Adaptive Oscillatory Inductive Bias for Modeling Sharp Prosodic Dynamics in Diffusion-Based TTS

- 论文编号：1655
- 报告人：Nirmesh J. Shah
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/dhar26_interspeech.pdf

## 问题
扩散 TTS（如 StyleTTS2）音质已较强，但对表情语音中的尖锐韵律转折、快速基频变化仍难稳。解码器里常用 Snake 等固定周期激活来拟合谐波结构，但对突变幅度/频率与清浊边界的适应性不足。

## 方法
在 StyleTTS2 框架上提出 **OscillaTTS**：整体两阶段训练与模块布局不变，核心是把解码器（iSTFT-Net 声码器）中的非线性换成自适应振荡激活
\[
x + \tanh(\alpha\sin^2(x)),
\]
其中 \(\sin^2(x)\) 提供周期归纳偏置，可学习 \(\alpha\) 调节振荡强度，线性旁路保持稳定性。Stage1 用重建损失训练解码器相关组件；Stage2 联合训练（含 style diffusion、SLM 判别器等），推理时从文本侧预测风格嵌入。作者从梯度/Taylor 展开对比 Snake、HOSC，说明 Oscilla 具有输入依赖的门控式振荡响应。

## 实验与结果
数据：LJSpeech（单说话人）与 ESD 英语子集（Happy/Angry/Sad）；80/10/10 划分；24 kHz；stage1 200 epoch、stage2 120 epoch。
- LJSpeech：主观 Speech Quality 86.67（StyleTTS2 81.48）；MCD 6.59、F0-RMSE 0.35；AutoPCP 4.05、WER 1.85（优于 StyleTTS2 的 3.92 / 2.86）。
- ESD：Angry/Happy/Sad 的 ES MOS、MCD 等多项优于 StyleTTS2；AutoPCP/WER 亦改善（如 Angry WER 9.21→4.05）。
- 激活消融：可学习 α 的 Oscilla 在 MCD/F0-RMSE 上优于固定 α、Snake1D、ReLU、tanh 等变体。

## 结论
作者认为在扩散 TTS 解码器中引入自适应振荡归纳偏置，能更好建模快速韵律变化；在 LJSpeech 与 ESD 上主客观均有一致提升。局限/展望：多说话人表情 TTS 与歌声合成。

## 点评
这是一篇「只改激活函数」却对准真实痛点的工作：表情语音的尖锐转折往往卡在解码器局部非线性的表达能力，而不是再加一套韵律预测器。Oscilla 相对 Snake 的可学习幅度 + tanh 阻尼 + 线性旁路，设计动机能从梯度分析直接看出来，消融也支撑了「自适应 α」的必要性。脆弱点在于：改进高度绑定 StyleTTS2/iSTFT-Net 解码路径；主观样本与情绪类别有限；与更大系统级改动相比，增益幅度中等，外推到更复杂多说话人设定仍待验证。


# Word-level Emotional Intensity Control in TTS via Emotion Residual Vectors

- 论文编号：3079
- 报告人：Ji-Hyun Park
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/park26i_interspeech.pdf

## 问题
情感 TTS 多采用句级情绪条件，难以在词级分配韵律突显，易把强度加错词。已有词级强度控制（EmoQ-TTS、HED-TTS、EME-TTS 等）虽可控，却常带来突变基频、不自然时长或过突显目标词，自然度下降。

## 方法
提出 **情绪残差向量（ERV）** 作为无标注的词级控制信号：
1. 在 ESD 平行中性–情绪同文对上，用 MFA 对齐 + WavLM-Base（层 7–12 聚合）得到词级嵌入，定义 \(r_w=u_w^{\mathrm{emo}}-u_w^{\mathrm{neu}}\)。
2. 三阶段训练：先训带说话人/句级情绪的 FastSpeech2；冻结骨干、全局情绪固定为中性，只训残差注入模块（RIM）：瓶颈投影 \(B\in\mathbb{R}^{a\times D}\)（默认 \(a=32\)）再映射到编码器隐空间，加 LayerNorm，按词级权重 \(\alpha\) 注入；再用学到的 \(B\) 生成投影目标，微调 RoBERTa 预测器从文本+情绪提示预测投影 ERV。
3. 推理：预测器输出 \(\hat z_w\)，经冻结 RIM 注入中性条件骨干，用 \(\alpha\) 连续调节词级强度。

## 实验与结果
ESD 英语子集（10 说话人，五情绪；14,900/950/1,550）；抽取约 88,400 词级 ERV。主观 NMOS/EMOS 与客观 UTMOS、Emotion2vec 情绪准确率：Proposed（\(\alpha_w=1\)）与 FS2+emo 接近（NMOS 3.83、Emo.Acc. 0.71），明显优于 HED-TTS。词级 A/B：相对 EME-TTS 赢 55.3%，相对 HED-TTS 赢 87.1%。增大 \(\alpha\) 时平均音高按情绪方向变化。消融：无瓶颈时 Emo.Acc. 偏低；\(a=32\) 附近情绪准确较好；带预测器后 Emo.Acc. 达 0.71。

## 结论
作者认为 ERV + 瓶颈注入可实现词级情绪强度控制并更好保持自然度；瓶颈使高维 S3L 残差变得可预测、可缩放。局限：依赖平行、词对齐的中性–情绪对，扩展到非约束数据仍是开放问题。

## 点评
关键洞察是「控制信号应是中性→情绪的局部残差，而不是另造一套强度标签」。把残差压进低维瓶颈再让 RoBERTa 预测，既稳定了 \(\alpha\) 缩放，又把监督从声学残差转到文本条件——这是相对直接注入高维 ERV 更工程化的一步。相对 HED/EME 类显式强度/分布控制，主观词级自然度优势明显。脆弱点紧扣作者自己指出的平行对齐依赖；且全局情绪固定为中性、情绪主要靠残差表达，对「非平行」或跨语料泛化可能变脆。


# Continuous Time-Varying Emotion Control Zero-Shot Text-To-Speech With Emotion Orthogonal LoRA

- 论文编号：1798
- 报告人：Chenchen Wan
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wan26b_interspeech.pdf

## 问题
高质量情感 TTS 常依赖大规模语料与粗糙离散标签，难以做细粒度、随时间变化的控制。参考音频提示易把情绪与说话人/内容韵律缠在一起；句内情绪转折容易被平滑或被 prompt 情绪拖偏。

## 方法
在预训练 flow matching TTS（F5-TTS / DiT）上提出两阶段方案：
1. **EO-LoRA**：在选定线性层（默认 attention 的 Value/Output 与 FFN）插入三条分别对应 Valence、Arousal、Dominance 的低秩分支（r=16），每帧用对应 VAD 标量缩放更新；用 Frobenius 余弦正交正则 \(L_{\mathrm{orth}}\) 抑制维度间干扰。支持句级常数或帧级时变 VAD。
2. **Flow-DGPO**：对候选组做偏好对齐，用组内标准化优势把样本分成正/负集，以 flow matching loss 相对冻结参考模型的间隔做偏好目标；奖励综合情绪相似度、说话人相似与 (1−WER)。
Stage1：\(L_{\mathrm{FM}}+\lambda_{\mathrm{orth}}L_{\mathrm{orth}}\)；Stage2：Flow-DGPO。帧级 VAD 由 wav2vec2 预测器（MSP-PODCAST）提取并归一化到 \([-0.5,0.5]\)。

## 实验与结果
训练：EmoVoice-DB（约 40h）+ ESD 英语（约 10h）。评测：EMO-Change（时变转折）、JVNV S2ST（日→英跨语）。相对细调 F5-TTS，EO-LoRA + Flow-DGPO 在 EMO-change 上 SIM-o 0.751、WER 0.2%、AutoPCP 3.60、Emo SIM 0.778、Aro-Val SIM 0.914；主观 SMOS/NMOS/EMOS 亦最高。数据量远小于 EmoCtrl-TTS 的大规模设定，但可控性指标可竞争甚至更优。消融：去掉 \(L_{\mathrm{orth}}\) 或改注入位置（含 Q/K）会削弱可控性；Flow-DGPO 进一步提升可控与可懂度。

## 结论
作者认为 EO-LoRA 与 Flow-DGPO 能在有限情感数据下实现稳健的连续/时变零样本情绪控制，并保持可懂度与说话人相似；计划扩展到其他生成骨干。

## 点评
核心设计是「把 V/A/D 拆成三条正交低秩调制」，比单条 LoRA 或外挂条件流更可解释，也直接服务帧级轨迹控制。Flow-DGPO 用复合奖励把情绪对齐与质量约束绑在一起，缓解了只追情绪相似度时的崩坏风险。脆弱点：VAD 依赖外部预测器质量；跨语设定下骨干未学日语，SIM/WER 仍有差距；EmoCtrl-TTS 结果来自原文报告而非同环境复现，跨论文对比需谨慎解读。


# ETC-TTS: Emotion Trajectory Learning for Controllable Emotional Text-to-Speech

- 论文编号：3088
- 报告人：Gaeun Kim
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kim26u_interspeech.pdf

## 问题
情感强度控制常在推理时对情绪嵌入做缩放/插值，中间强度并未在训练中显式学习，导致强度单调性不稳、自然度下降。作者指出这造成训练–推理不匹配：模型只在离散端点上优化，却指望推理期潜空间操纵给出一致感知强度。

## 方法
**ETC-TTS** 把强度重写为潜在风格空间中的 **中性→目标情绪轨迹**：
1. **RVQ 情绪原型**（L=3）：每级码本大小=情绪类别数，与标签一一对应；k-means 初始化 + 级联 triplet 聚类损失，并周期性复活未使用码字。
2. **原型锚定 flow matching**：源为中性原型加噪、目标为情绪原型；学习条件于音素特征与风格标签的速度场；推理用轨迹参数 \(t\in[0,1]\) 调节强度，无需参考音频。
总损失含 FastSpeech2 重建、RVQ、聚类、flow（\(\lambda_f=30\)）与中性对齐项。三阶段训练：原型初始化 → 冻结 flow 先稳抽取器 → 联合训练。

## 实验与结果
数据：AIHub 韩语情感语音（约 80h，七情绪）与 ESD 英语。骨干统一 FastSpeech2 + HiFi-GAN。相对标签条件、RA、SF：
- ESD：Proposed N-MOS 3.14、E-MOS 3.78、EmoAcc 92.93%；AIHub 上 E-MOS/CER 等亦更优。
- 强度单调性 AB 错误率在多数情绪/强度对上低于 RA/SF；emotion2vec 概率随 \(t\) 更平滑单调。
- 跨强度 UTMOS/CER 更稳定；用 SER 嵌入或高斯先验替代中性锚定会伤 EmoAcc 或自然度。

## 结论
作者认为应在训练中学习中性–情绪轨迹，而非推理期启发式嵌入操纵；在韩/英数据上获得更稳的单调强度控制并保持竞争力音质。

## 点评
问题诊断很准：强度控制的失败往往不是「没标量」，而是「中间态从未被监督」。把 rectified flow 端点钉在 RVQ 原型上，把可控 \(t\) 变成真正学过的路径参数，比 SF/插值更有训练一致性。脆弱点：原型与类别数硬绑定，细粒度/复合情绪表达受限；flow 权重大（\(\lambda_f=30\)）需小心与声学重建权衡；主对比都在同一 FastSpeech2 骨干上，换现代零样本骨干时轨迹模块是否仍成立未验证。


# Beyond One-Size-Fits-All: Personalized and Culturally Adaptive Emotional TTS via Interactive Optimization of Individual Emotion Perception Spaces

- 论文编号：1696
- 报告人：Wangzixi Zhou
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26e_interspeech.pdf

## 问题
情感 TTS 即使用 arousal–valence（A–V）连续控制，训练标注常来自单一人群平均，默认「声学线索→感知情绪」映射普适。个体与文化差异会导致模型情绪与听者感知错位；RLHF 类对齐又需大量偏好数据并重训模型，不适于快速人均适配。

## 方法
提出轻量 **训练后个性化层**，不改声学骨干：
1. **情感生成器**：Grad-TTS + Emotion Controller（Emotion Feature Predictor + pitch/energy 预测）。A–V 经 Gaussian Fourier 特征映射后由四层 MLP 预测 SER 衍生的高维情绪特征；训练用 L1 对齐预训练 SER 特征，推理只需 A–V。
2. **交互遗传算法（IGA）**：对目标离散情绪，在 A–V 空间生成候选坐标并合成语音，用户选偏好样本；多亲算术交叉 + 衰减突变强度（\(M_1=0.20,\gamma=0.90,M_{\min}=0.05\)）迭代，通常约三轮收敛，得到个人/文化平均 A–V 映射。

## 实验与结果
数据：约 9 小时美式英语女声（EXPRESSO + EmoV-DB + ESD），A–V 由 SER 估计。相对 Grad-TTS+情绪嵌入，Emotion Controller：MOS 3.37→3.75，WER 21%→17%，CCC(A/V) 0.60/0.64→0.84/0.77。
个性化：中/印尼/日各 10 人共 30 人；个人化 A–V 相对美式数据集均值明显偏移。A/B：亲历个性化者偏好个人映射 76%；新文化听者对文化平均映射偏好约 64.8–69.8%；跨文化排序亦偏好本文化映射（约 65–70%）。

## 结论
作者认为应把情绪感知空间个性化/文化适配，而非一刀切平均 A–V；交互优化可在少量反馈下提升感知对齐。未来工作包括更广语言文化与实时个性化。

## 点评
工作抓住的是「控制空间」而非「声学模型」：把适配限制在 2D A–V，用 IGA 做极少交互的人均搜索，比 RLHF 更贴近产品侧快速定制。Emotion Controller 用 SER 特征桥接低维控制与高维声学，使个性化不必重训扩散解码器。脆弱点：骨干与语料偏英语女声，跨文化听评仍用同一声学模型；A–V 监督本身来自 SER 估计，存在标签噪声；偏好实验规模中等，文化结论更偏初步观察。


# Cross-modal Consistency Guidance for Robust Emotion Control in Auto-Regressive TTS Models

- 论文编号：1986
- 报告人：Yizhou Peng
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/peng26g_interspeech.pdf

## 问题
自然语言情绪指令的 AR TTS 在「文本语义情绪」与「要求渲染的语音情绪」冲突时（如用惊讶语气说悲伤内容），表现力、自然度与音质会明显下降。标准 CFG 用无条件 dropout 外推，难以对抗文本语义拉力，且易引入伪影。

## 方法
在 CosyVoice2 上提出 **CCG-CFG** 及其蒸馏：
1. 外部 LLM 抽取 Text-Emo，并判定与 Rendered-Emo 的不一致程度（Identical / Inconsistent / Highly Inconsistent）。
2. **CCG-CFG**：不一致时把 CFG 的无条件支路换成 Text-Emo 条件，放大 Rendered-Emo 与 Text-Emo 的 logit 差；一致时退回标准 CFG。
3. **DS-CCG-CFG**：按不一致档位动态设 guidance scale（网格搜索得 {1.0, 2.5, 3.0}）。
4. **蒸馏**：用硬样本挖掘构造文本–对立情绪对，多尺度/多种子生成候选，按 \(0.5(1-\mathrm{WER})+0.5\cdot\mathrm{EmoConf}\) 排序做 DPO，把引导内化，去掉双通道推理与 CFG 伪影。

## 实验与结果
合并 ESD/MESS/MEAD/TESS/SAVEE/LibriTTS/VCTK 等，七情绪；约 40h 训练。中性参考下相对 CosyVoice2-N（EmoACC 50.63%）：
- DS-CCG-CFG：EmoACC 64.83%，MaJ 58.4（训练免费最佳之一），但 WER 升至 7.86%。
- DS-CCG-CFG-DPO+硬样本：EmoACC 59.55%，WER 3.76%，UTMOS/DNSMOS 保持高；主观 MOS 4.33、EMOS 3.67、NMOS 3.94，优于 CosyVoice2-N/R，并接近 Qwen3-TTS-R。
不一致子集上增益最大；传统高尺度 CFG 则显著伤 WER。

## 结论
作者认为用文本情绪作对比条件、按不一致动态尺度，再蒸馏进模型，可在冲突场景下显著提升情绪表达并保住可懂与自然度。

## 点评
问题设定很现实：NLEC 的失败模式往往不是「不会说情绪」，而是「文本语义把渲染情绪拉回去」。把 unconditional 换成 Text-Emo，等于显式做跨模态对照，比盲目加大 \(w\) 更对症；动态尺度与 DPO 蒸馏则分别处理「何时用力」与「推理成本/伪影」。脆弱点：推理期依赖外部 LLM 判不一致（蒸馏后可摆脱）；EmoACC 依赖 SER，与文本语义冲突时「正确情绪」定义本身主观；硬样本挖掘的对立情绪配对策略会影响泛化边界。


# A Large-Scale Dataset of Listener Impressions of Emotional TTS

- 论文编号：1521
- 报告人：Erica Cooper
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/cooper26_interspeech.pdf

## 问题
情感 TTS 的金标准仍是听测，但成本高、难快速迭代。现有自动质量评估（如 UTMOS）多在中性合成语料上训练，难以泛化到情感合成；情感 TTS 还需评估表达力与目标情绪匹配度，而公开听测结果与含合成样本的标注数据几乎空白。

## 方法
构建大规模听感数据集（非提出新合成模型）：
1. 收集/生成约 18,208 条样本：自然情感语音（主要 ESD）+ 13 类合成系统（Emo-DPO、EmoSpeech、ECSS、GPT-Talker、EmoKnob、Tortoise、MaskGCT、VALL-E X、Vevo、PromptTTS++、ParaSpeechCaps、MiMo-Audio、Gemini API 等），覆盖克隆、文本提示说话人与 API 预设音色。
2. 262 名美式英语母语听者评分：QMOS、EMOS、自由选择感知情绪类别、valence/arousal/dominance（SAM 量表）；多数样本约 7 次评分。
3. 分析评分关系，并用 SSL-MOS、UTMOS、Emotion2Vec、Gemini LLM-as-judge 做零样本预测实验。

## 实验与结果
组内系统排名给出（跨组因内容/说话人不同不可直接比）：如 ESD 自然语音 QMOS/EMOS 3.71/3.90；Gemini API 4.21/3.89；Tortoise QMOS 高但 EMOS 偏低。目标情绪选择比例与 EMOS 相关约 0.92。VAD 分布相对自然语音的 EMD 与 EMOS 呈强负相关（按情绪有所不同）。零样本预测：UTMOS 对 QMOS 系统级 SRCC 总体 0.80；Gemini 对 EMOS 总体 0.84；各情绪差异大（如 Angry 更具挑战）。

## 结论
作者贡献首个面向情感合成语音质量评估的大规模听感数据集，将公开以支持自动评估模型开发；现有预测器有一定相关性但仍有明显提升空间，且表现依赖情绪类别。

## 点评
这是「评测基础设施」论文：价值在于把多系统、多轴标注做成可训练资源，而不是比拼某个 TTS 分数。分析部分有用地提醒：QMOS/EMOS/VAD 可互补，中性 MOS 预测器不能直接当情感评测银弹。脆弱点：系统间条件不完全对齐（作者已强调），零样本预测不等于专用评估模型上限；公开后实际训练效果仍待社区验证。


# DECRA: Dynamic Emotion Control for Real-time Speech Anonymization

- 论文编号：2927
- 报告人：Ghady Nasrallah
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/nasrallah26_interspeech.pdf

## 问题
实时说话人匿名化既要抹去身份，又要控制/中和情感以防副语言泄露。现有流式 VC 多只管身份、无意中保留情绪；情感 VC 则多为离线、句级全局条件，无法因果低延迟地做时变、闭环情感操控；说话人嵌入常与情绪纠缠。

## 方法
**DECRA** 以 TVTSyn 为流式骨干，加入：
1. 对抗学习：把全局说话人嵌入投影到「去情绪」音色子空间（GRL + V/A 回归），情绪信息改由连续 valence–arousal 轨迹回注解码器。
2. 离线 SER 伪标签在大规模自然语音（LibriTTS + Natural Voices）上监督；训练时用时变 V/A 条件（250 ms hop）。
3. 因果 SER 头挂在 VQ 前内容特征上，在线预测帧级 V/A，闭环反馈到情感控制器；波形解码用 Conditional LN Fusion 融合 TVT 与 V/A。端到端可流式，GPU 延迟 <80 ms。

## 实验与结果
情感评测在 ESD。中和/转换相对 SeedVC、Vevo、TVTSyn：DECRA 的 CCC(A) 更高（中和 0.81、转换 0.74），WER/说话人相似可竞争；NISQA 低于离线基线，作者归因于流式约束而非情感模块。主观：怒/喜→中性准确率约 91–92%，悲→中性较弱；中性→情绪方向亦多数优于无控制骨干。动态 arousal 斜坡与预测轨迹相关约 0.78，valence 仅约 0.21。VPC’24：EER 46.64、WER 4.90、UAR 48.70，在匿名与情绪保留间更平衡。流式：76.1 ms 延迟、RTF 0.268。

## 结论
作者给出可同时做身份转换与闭环时变情感控制的因果流式系统；局限是 valence 控制弱于 arousal，未来拟用更丰富 SSL 情绪嵌入并加强与内容/说话人解耦。

## 点评
问题组合很贴隐私场景：匿名化若「保情绪」会泄露，若「抹情绪」又需实时可控。对抗解耦 + 在线因果 SER 闭环是清晰设计。结果也诚实：arousal/prosody 跟得上，valence 难控；音质代价主要来自流式而非控制头。脆弱点：伪标签 SER 误差会传导；与离线高保真情感 VC 比，质量–延迟权衡仍陡。


# Emo-BPO: Emotion Bidirectional Preference Optimization for Diffusion-based Emotional TTS

- 论文编号：1613
- 报告人：Jiacheng Shi
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/shi26d_interspeech.pdf

## 问题
扩散情感 TTS 的偏好对齐（如 Emo-DPO）通常只强化目标情绪条件轨迹，未显式建模与竞争情绪模式的分离；而 CFG 本质依赖条件对比，这种「单向」优化会削弱细粒度可控性。

## 方法
**Emo-BPO** 在 Grad-TTS 扩散解码器上：
1. 用同文不同情绪的平行对构造双向监督：\((c,a_1,a_2)\) 学情感对齐分支 \(\epsilon_{\theta}^{\mathrm{EA}}\)，颠倒顺序学对比分支 \(\epsilon_{\theta}^{\mathrm{EC}}\)（两套参数，非单网络硬兼两职）。
2. 推理对比引导：\(\epsilon^\omega=(1+\omega(t))\epsilon^{\mathrm{EA}}-\omega(t)\epsilon^{\mathrm{EC}}\)，并用晚步日程 \(\omega(t)=1-t/T\)，早期弱引导保结构、后期加强情绪。
无需额外奖励模型或新标注；冻结文本编码器与时长预测器，只微调 score 网络。

## 实验与结果
数据：ESD + EmoVoiceDB。客观：Emo SIM 99.23、Prosody SIM 3.85、UTMOS 4.52、SER 均值准确 0.87，多项优于 EmoSpeech、CosyVoice(2)、EmoSphere++、EmoVoice；可懂度竞争（WER 3.84，CosyVoice2 更低）。主观 MOS/Emo MOS/MOS EC 与人类情绪识别亦领先；AB 偏好优于 EmoSpeech 与 CosyVoice2。消融：去掉对比分支或晚步日程均伤情绪/韵律/WER。

## 结论
作者认为应在 CFG 框架下同时学习情绪吸引与排斥轨迹；双向偏好 + 渐进引导可提升可控性与感知质量并保持可懂度。

## 点评
洞察贴合扩散机制：CFG 已是对数似然比，把「无条件」换成「竞争情绪条件」并把两条 score 分开学，比只做 DPO 推目标更吃透对比结构。晚步日程也符合「先结构后细节」的去噪直觉。脆弱点：依赖平行同文多情绪对；双分支推理成本更高；骨干是 Grad-TTS，相对现代 LLM-TTS 的绝对 WER 仍可能吃亏。


# DeSRPA: Decoupled Speech Role-Playing Agent via Inference-Time Intervention

- 论文编号：1627
- 报告人：Wenqiu Tang
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/tang26b_interspeech.pdf

## 问题
语音角色扮演智能体（SRPA）若端到端微调，依赖角色专用数据、难泛化到未见角色，且音频–文本联合训练带来「模态对齐税」，损伤 LLM 推理与人设一致性；纯级联 LLM→TTS 又易丢情感推理，TTS 只做脱节渲染。

## 方法
**DeSRPA**：推理期干预、不更新参数的解耦框架：
1. **内部认知转向**（冻结 Qwen3-4B）：用 SAE 学稀疏控制向量，在残差流注入人格基向量、情境激活向量（Layer 15）与语言风格向量（Layer 20）；缩放系数结合 PDB 人格指标与人–LLM 协作标注。
2. **外部表达渲染**（冻结 StyleTTS 2）：从 ESD/CREMA-D 过滤高置信情绪样本，用风格减法 \(v_{\mathrm{acoustic}}^{(c)}=\mathbb{E}[S(x^{(c)})]-\mathbb{E}[S(x^{(n)})]\) 得说话人无关情绪方向；按 LLM 情绪标签与强度 \(\tau\) 做双路径融合注入风格空间并经扩散 style predictor 细化。

## 实验与结果
SpeechRole（72 英角色）与 OmniCharacter-10K（原神 10 角色）。多模态裁判均值 0.8379，开源最优、接近 GPT-4o Audio(0.8862)；EEA 0.701、SIM 0.886。消融去掉 LLM/Speech CV 分别伤人格/知识一致性与 EEA（降至 0.549）。OmniCharacter 人类评测：流畅、清晰、情感表达最高；Consistency/Immersion 逊于高度风格化的 OmniCharacter E2E（作者归因动漫夸张韵律 OOD）。

## 结论
作者认为双层推理期控制向量可在不微调下对齐「心智」与「嗓音」，提升人格/情绪一致性并缩小与专有模型自然度差距。

## 点评
路线明确反对「一切端到端」：把角色适配做成两侧冻结骨干上的向量算术，可扩展性好。风格减法解耦说话人与情绪方向，和 LLM 侧 SAE 人格向量形成对称设计。脆弱点：依赖外部过滤质量与裁判 LLM；TTFA 高于纯 E2E；对夸张 OOD 人设，固定 StyleTTS 2 风格空间仍可能不够。


# EmoInstruct-TTS: Dual-Path Instruction-Guided Emotional Speech Synthesis

- 论文编号：1834
- 报告人：Ganjun Liu
- 程序：Wednesday 30 September 2026 / Emotional Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/wu26f_interspeech.pdf

## 问题
自然语言指令可控 TTS 灵活，但常依赖粗糙情绪标签，缺少细粒度类别与强度的显式建模；仅靠语言指令也难稳定捕捉情绪的声学对应。参考音频条件则易受说话人/音色绑定。

## 方法
**EmoInstruct-TTS** 双路径框架：
1. **Emotion2embed**：Sentence-BERT 文本特征与 ECAPA-TDNN 声学特征拼接投影为 896 维；多任务分类 + 序数强度排序损失，覆盖 48 态（27 细粒度类别 + 7 主情绪×3 强度）。
2. **ICE-Flow**：MiniLM 编码指令，流/回归生成声学接地的 Emotion2embed；样本级 L2 + 协方差分布正则；推理可 CFG 调节指令遵从。
3. **合成**：指令进 LLM（Qwen2.5-0.5B+LoRA）做语义规划，Emotion2embed + 说话人嵌入条件 CFM 生成 mel，BigVGAN 声码。

## 实验与结果
ESD + CNCED；弱标注字幕集 + 人工细粒度标注集。相对 CosyVoice2/3：21 强度任务与 27 细粒度任务上 Dual-Path 的 MOS/ESMOS 整体更优；去掉任一路径均下降。48 类客观 ECS 0.870（最高），WER 2.59%（CosyVoice3 更低 1.97%）。ICE-Flow 增加端到端延迟约 <1–2%。分布一致性消融显示 Sample+Dist 最优（IOA 0.91）。

## 结论
作者认为语义指令与结构化情绪嵌入应分工：前者规划语言、后者调制声学；双路径提升细粒度/强度可控与自然度。未来拟支持无预定义类别的开放描述。

## 点评
「双路径」直接回应指令 TTS 的常见失败：文本能描述情绪，却不一定能驱动正确声学。Emotion2embed 用序数几何把强度做成可排序方向，ICE-Flow 再把自由指令接到该空间，工程上完整。脆弱点：48 态标签体系仍是封闭集；部分字幕来自 Gemini 自动生成，噪声可能影响表示；相对 CosyVoice3 在 WER 上仍有差距。

