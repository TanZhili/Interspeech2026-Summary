# Instruction-following and Controllable Speech Synthesis

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
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

本场围绕指令跟随与可控语音/音效合成：从综艺音效的多智能体分层精炼，到方向跟随 TTS、开放指令表达合成，再到指令监督稳定性、偏好后训练与交叉注意归因诊断。控制对象从全局风格扩展到音素插值、口型—音素对齐的 EMG 合成，以及能耗友好的脉冲声码器。

数据侧强调可扩展伪三元组、野外视听指令语料与漂移过滤；评测侧揭示说话人相似度掩盖口音—情绪纠缠，并主张针对口音的主观/客观度量。生成机制上出现跳跃扩散统一离散时序与连续频谱，以缓解两阶段对齐塌缩与单阶段对齐不稳。

## 论文技术总结

# ARCHES: An Agent-Based Refinement Cycle for Hierarchical Synthesis of Sound Effects for Variety Shows

- 论文编号：561
- 报告人：Li Liu
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lei26_interspeech.pdf

## 问题
综艺音效依赖人工剪辑，成本高、难规模化；通用文本/视频到音频模型偏现场自然声（diegetic），难覆盖风格化、喜剧化、稀有签名音效，且时序与情绪控制不足。

## 方法
ARCHES 多智能体迭代：Planning 检测需增强的事件 → Generation 条件合成 → Checker 评估后经 AXIS 路由到时序/情绪等细化智能体。AURA 用 Qwen2-Audio 多模态检索 26k+ 专业音效库作上下文示例；CEB 记录成功交互作模板捷径。生成骨干基于 MultiFoley，高层规划多用 Gemini-2.5 Pro。自建 VSSE-Bench（约 1000 集综艺切分）评测。

## 实验与结果
相对 MMAudio、Kling-Foley、HunyuanVideo-Foley、FoleyCrafter：LSD 0.77、OD 0.048 s、FAD 7.04、A-MOS 2.68 及主观 MOS-S/T/E（4.04/4.54/4.46）均最优。消融：无 AURA 损害多样性/FAD；无 AXIS 时序误差大增；无 CEB 略降。换 MLLM 骨干时 Gemini-2.5 Pro 最好，开源 Qwen3-VL 仍可用。

## 结论
检索增强 + 智能路由细化 + 经验库可使综艺风格音效在保真、同步与情绪匹配上显著优于通用 V2A；未来将降延迟、减对底层模型依赖并扩展跨模态生成。

## 点评
把后期剪辑流程 agent 化，切中综艺非叙境音效痛点；新基准与音效库是实质贡献。系统强依赖闭源/强 MLLM 与外部库质量，消融已显示去掉检索或细化回路即掉点；客观 LSD/FAD 对“喜剧恰当性”覆盖有限，主观三项是更关键证据。


# Scalable Direction-Following TTS via Voice Impression-Guided Pseudo Triplet Construction

- 论文编号：919
- 报告人：Kenichi Fujita
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/fujita26_interspeech.pdf

## 问题
导演式“相对上一遍如何改”的 direction-following TTS 需要 (参考句, 指导语, 修改后句) 三元组，但大规模语料几乎没有这种相对风格配对。作者要可扩展地构造伪三元组并学习说话人保持的相对风格变换。

## 方法
用印象可控零样本 TTS 生成同脚本 pre/post 句对，经说话人一致性与语速过滤后估计 13 维印象向量差 ΔI，由 LLM 生成自然语言指导语，构成伪三元组。在固定骨干 TTS 的语音嵌入空间上训练方向条件风格精炼器（整流流匹配预测加性嵌入偏移）。另采集约 8.9 小时专业配音真实三元组。对比仅伪数据、仅真实、混合及不同说话人规模子集。

## 实验与结果
伪数据约 35 万三元组（127.6 小时）。客观：精炼不损害 UTMOS；伪数据与 Full 比仅真实录制在未见说话人上更稳地保持说话人相似。主观：Recorded AlignMOS 最高但 SMOS 较低；Pseudo-all SMOS 高而对齐略保守；Full 折中。伪数据 F0 变化幅度小于专业录音，解释了更保守的调制。

## 结论
伪三元组 alone 即可稳定做说话人保持的相对修改；与真实数据结合可提升方向对齐同时维持身份稳健。伪数据韵律变化偏小是当前局限。

## 点评
把“相对指导”从绝对风格标签中拆出来，并用印象差驱动 LLM 写导演语，数据管线可扩展。伪数据依赖印象可控 TTS 与同一印象估计器，存在分布收缩风险；客观对齐也用该估计器作代理，需主观 AlignMOS 交叉验证——作者已做，但伪–真韵律差距仍制约表现力上限。


# Poly-InstructTTS: Learning In-the-Wild Expressive Speech Synthesis from Open-Ended Instructions

- 论文编号：930
- 报告人：Junhui Zhang
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26m_interspeech.pdf

## 问题
开放自然语言指令控制细粒度表情仍难，因语料多为中性朗读，且许多零样本系统把参考音频送入 GPT 易与指令风格冲突（style leakage）。

## 方法
从影视媒体构建约 1000 小时指令语料：切分去噪、ASR/说话人分离/副语言标签、字幕对齐，再用多模态 LLM（Gemini）三阶段生成上下文摘要、属性与自然语言指令。模型为 prompt-free GPT（属性型 thinking tokens：性别/强度/风格/口音）+ CosyVoice3 式 FM 仅在声学侧注入音色；另有带 Speaker ID 的指令条件说话人 SFT。扩展 InstructTTSEval 测试集覆盖口音、极端情绪、非主流风格等。

## 实验与结果
相对多开源/闭源基线，RP 等指令指标与 I-MOS 强（基测 I-MOS 3.81 最高）；WER 中等，作者归因于野生声学与标签噪声。去掉 thinking tokens 主观下降；外接指令编码器无增益。SFT 相对基座提高人格一致性 P-MOS，但 I-MOS 略降。

## 结论
野生影视指令数据 + prompt-free GPT/thinking tokens/FM 音色注入可提升开放指令表现力；说话人 SFT 可把控制迁移到指定人设。未来需平衡表达力与稳定，并改进 FM 与参考无关音色。

## 点评
数据管线与“风格走 GPT、音色走 FM”的分工直接针对泄漏问题；扩展评测集有社区价值。原始影视数据因版权未公开，可复现性依赖自建语料；表达力提升伴随 WER 上升也显示指令后训练的稳定性代价。


# Spiking Vocos: An Energy-Efficient Neural Vocoder

- 论文编号：1086
- 报告人：Yukun Chen
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26j_interspeech.pdf

## 问题
频域声码器如 Vocos 算力轻但仍非真正为低功耗优化；直接把 ANN 换成 SNN 常因二值脉冲信息瓶颈与时序建模不足而掉点。

## 方法
Spiking Vocos：在 ConvNeXt 点卷积前插入 PLIF 神经元，并用幅度捷径 |Zin|⊙Zout 保留幅值；自架构蒸馏对齐中间特征与幅相谱（含抗缠绕相位损失）；每块加入 Temporal Shift Module 融合过去/当前/未来通道。在 LibriTTS 训练，对比 ANN Vocos 与不同步数/消融。

## 实验与结果
4 步 + TSM + 蒸馏：UTMOS 3.74（ANN 3.82），PESQ 3.45；主观 MOS 3.69 接近 Vocos 3.80。理论能耗约 ANN 的 14.7%（>6.8× 能效）。单独 TSM 或蒸馏均可显著回升 4 步基线；8 步更接近 ANN 但延迟加倍。

## 结论
幅度捷径、自蒸馏与 TSM 协同可使脉冲频域声码器在感知质量接近 ANN 的同时大幅降能耗。

## 点评
把 SNN 约束对准声码器瓶颈（点卷积算力、幅值丢失、因果时序盲区）很对症。能耗为 45nm 理论估算，真实芯片部署与延迟–质量权衡仍需验证；PESQ 与主观差距也提示脉冲量化对信号级指标更敏感。


# Stabilizing Instruction Supervision for Instruct-TTS via Controllable Diversification and Drift Filtering

- 论文编号：1227
- 报告人：Yizhong Geng
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/geng26b_interspeech.pdf

## 问题
Instruct-TTS 常用 LLM 把结构化标签改写成自然语言指令，但无约束改写超过 40% 存在语义漂移（执行化、角色扮演、改属性），污染监督并削弱泛化；单纯扩多样性与单纯过滤也无法兼顾覆盖与保真。

## 方法
数据中心稳定配方：(1) 音高/语速/音量扰动 + 模板属性提示做属性对齐监督；(2) 约束人设×句法×属性槽位的可控多样化改写；(3) 异族 LLM 验证器打分投票过滤三类漂移。在 CosyVoice 2 上对中文约 90h 语料做 SFT，评 InstructTTSEval（中文）APS/DSD/RP。

## 实验与结果
约束改写使漂移 40.4%→15.4%。完整配方指令跟随平均准确率 56.4%（无 SFT 34.5%，朴素 SFT 51.0%），NR/CMOS 均 4.16。消融：去漂移过滤伤害最大（→48.9%）；去多样化与去属性监督亦降点；属性监督对音高/语速/音量 APS 增益最大。

## 结论
指令监督不稳定主要是数据质量问题；覆盖扩展、漂移过滤与属性对齐三者互补，过滤是最大单项贡献。漂移分类或可推广到其他指令生成任务。

## 点评
把 TTS 标签改写中的失败模式显性分类并量化，比“再换模型”更切中要害。评测依赖 Gemini judge，作者用多模型族缓解自评估偏差；情感维度上朴素 SFT 有时更高，说明过滤也可能去掉部分有用的情绪描述，需权衡保真与覆盖。


# Improving Stable Speech Synthesis Post-Training with ChatScorer and Margin-Based Preference Construction

- 论文编号：1881
- 报告人：Wenhuan Lu
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/niu26c_interspeech.pdf

## 问题
Codec TTS 后训练常把 CER/SIM 等异构指标融成标量奖励，候选分数分不开，偏好监督模糊，且难压制明显“机器感”对话输出。

## 方法
对每条提示采样多候选，用 CER+SIM+ChatScorer 融合排序；ChatScorer 为 WavLM+轻量 Transformer 的高斯打分头，并用 GRL 抗说话人泄漏。仅保留质量间隔足够大的组：正样本需满足 CER/SIM/Chat 阈值，负样本至少两项差，并按 margin 抽中间样本，构造 DPO / Rank3/5DPO 数据。对比 GRPO。对话式长文本提示约 2000 训 / 500 测。

## 实验与结果
Rank3DPO：CER 1.17%、SIM 失败率 0.10、BadRate 2.44%，优于 SFT/DPO/GRPO。Margin 构造优于直接按融合分选；加 ChatScore 对 CER 影响小但大幅降 BadRate 并抬高 MOS。ChatScorer 与人类 A/B 一致性高于 DNSMOS/UTMOSv2。

## 结论
辅助 ChatScorer + margin 偏好构造可把嘈杂多指标信号变成更可学监督，提升生成稳定性并抑制不良对话输出，同时保持可懂度与说话人相似。

## 点评
问题诊断（弱分离→模糊监督）清晰，稳定性指标（组失败率、BadRate）比只看均值 CER 更贴后训练目标。过滤丢弃大量提示（DPO~40%，RankDPO 更高）以换可学性；GRPO 未同用 margin 过滤，对比不完全对等。


# Accent-Emotion Entanglement in LM-Based Text-to-Speech Systems

- 论文编号：2749
- 报告人：Matthew Hayden
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/hayden26_interspeech.pdf

## 问题
零样本 TTS 常靠说话人相似度（SSM）宣称接近真人，但 SSM 可能掩盖口音问题。作者在 CosyVoice2 指令控情时观察到口音被意外改变，称之为 accent–emotion entanglement，需系统刻画并改进评测。

## 方法
以 CosyVoice2（指令“Make this sound x”+情绪参考）与 MaskGCT（仅情绪参考）为案例，在 MEAD 的 happy/angry/neutral 上合成。主观：口音 SMOS（30 名多国英语 L1）。客观：GenAID 口音嵌入 UMAP、到质心余弦距离、口音分布熵。多说话人扩展客观分析。

## 实验与结果
CosyVoice2 口音 SMOS 跨条件约 1.17–4.13、方差大；MaskGCT 多在约 3.4–4.3 且更稳。UMAP 显示 CosyVoice2 扩散到印巴/英爱/东亚非裔等区域，MaskGCT 紧靠北美参考。各说话人–情绪下 CosyVoice2 到质心距离均更大。两系统原报告 SSM 接近，但口音行为迥异。

## 结论
情感条件可诱发口音幻觉，标准 SSM 不足；应常规加入口音主观与针对性客观指标。作者推测根因可能在指令微调数据标注/分布，但因训练数据未公开无法确认。

## 点评
用“SSM 相近却口音分裂”的对照有力说明评测盲区，且点出情感–口音纠缠的刻板印象风险。案例限于两模型与有限说话人/句子；对 CosyVoice2 成因仍是推断。贡献主要在问题定义与评测范式，而非修复方法。


# How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech

- 论文编号：2805
- 报告人：Nityanand Mathur
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/mathur26_interspeech.pdf

## 问题
风格字幕 TTS 用自然语言控音色，但单个词如何影响声学仍不清楚，妨碍诊断失败与改进可控性。图像域有 DAAM，语音尚缺等价框架。

## 方法
将 DAAM 适配到 CapSpeech（T5 风格字幕 + 流匹配 DiT）：在 25 层×24 ODE 步钩取交叉注意力，聚合为每 token 时序热图。对 120 风格字幕×30 文本约 3600 组合分析，分 Style/Content/Function 类，度量时序方差、峰均比、熵，以及与 F0/能量相关，并看层–步重要性。

## 实验与结果
风格词时序方差显著低于内容/功能词（p≪0.001，d=−1.16），呈全局调制；风格注意力与 F0/能量相关且语义一致（如 “loud”–能量 r=+0.64）。风格条件在早期 ODE 步与深层更强（早期相对后期约 5.2× 衰减）；注意力熵在第 17 层最低并与风格重要性峰重合。

## 结论
首次显示风格字幕在语音扩散/流匹配中的交叉注意力机制：风格全局、内容更局部，条件作用呈层–步层次。可为诊断与可控编辑提供归因工具。

## 点评
把 DAAM 迁到时序 mel latent，并做大规模 token 统计，解释性强。归因基于注意力作为忠实代理的假设，未做因果干预（如遮挡/改写 token）验证；仅针对 CapSpeech 架构，换其他条件注入方式时模式可能不同。


# Beyond Two-stage Diffusion TTS: Joint Structure and Content Refinement via Jump Diffusion

- 论文编号：2875
- 报告人：Jiabao Ai
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ai26b_interspeech.pdf

## 问题
扩散/流匹配 TTS 中，两阶段固定对齐易塌向平均韵律；单阶段无显式时长又易对齐不稳。需要在同一过程中联合演化离散时序结构与连续频谱内容。

## 方法
跳跃扩散：前向同时删帧（保护各音素首帧）与加噪；反向用 Location Predictor 选插入槽、Content Predictor 填内容，再做标准去噪。提出 Upsample–Diffuse–Downsample（UDD）以复用固定维预训练 U-Net；One-shot 退化为用分类时长替代 Grad-TTS 回归时长预测。冻结 Grad-TTS 编码器与扩散骨干，在 LJSpeech 训练跳跃预测器。

## 实验与结果
One-shot：WER 3.37% vs Grad-TTS 4.38%，UTMOSv2 略升。直接变维 TDD 最差。UDD 在匹配目标时长下 MCD/F0 有竞争力。0.75× 慢速 OOD：Grad-TTS 近似均匀拉伸，UDD 提高静音占比（如 Argmax 静音比 9.63% vs Grad-TTS 6.38%）并略降 WER，呈现自适应停顿。

## 结论
分类时长与跳跃–扩散联合细化可缓解均值韵律，并在非常规总时长下更自然地插入停顿；UDD 使变长结构与固定维网络兼容。

## 点评
把“时长多模态”写成插入槽分类，比 MSE 时长更贴停顿等稀有事件。主表最优往往是 One-shot 而非完整迭代 UDD，说明联合细化收益仍场景依赖；实验限 LJSpeech 与 Grad-TTS 骨干，对更强单阶段流匹配基线的相对优势待证。


# PhonemeCVAE: Contrastive Latent Clustering with Class-Conditioned Priors for Controllable Phoneme Interpolation

- 论文编号：2277
- 报告人：Nina Goes
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/goes26_interspeech.pdf

## 问题
高质量 TTS 内部表征难解释，细粒度音素级编辑（如 /s/–/f/ 插值）常受限于离散音素表示，难以在连续空间平滑变换。需要结构化、可插值的音素潜空间。

## 方法
PhonemeCVAE：β-VAE 为每类音素学习条件高斯先验；编码器用时长感知高斯下采样 + Conformer 得音素 token，解码器上采样 + PostNet；辅以监督对比损失促进类内紧致、类间分离，并含时长预测与对抗/特征匹配损失。推理时在最小对立对的类中心间线性插值替换对应 token，再解码与 HiFi-GAN 声码。

## 实验与结果
在 LJSpeech、LibriSpeech、CMU ARCTIC 等上，先验+对比相对消融显著提升 silhouette 与类间分离（UMAP 更清晰）。听测（N=18）：沿 α 插值可感知音素连续变化；编辑音自然度/质量均值约 3.14/3.22，略低于原音 3.45/3.55。

## 结论
类条件先验与对比正则形成可跨数据集泛化的音素潜拓扑，支持可控插值编辑且大体保持合成质量，有望服务发音清晰与治疗等场景。

## 点评
把音素编辑写成“在先验中心间插值再 patch token”，接口直观。依赖 MFA 对齐与最小对立对听测，对协同发音与跨说话人稳健性仍待更大规模评测；编辑质量略低于原音，说明重建–可编辑性折中仍在。


# TAP-ETS: Time Aligned Phoneme Guiding for EMG-to-Speech Synthesis

- 论文编号：3485
- 报告人：Dongyub Han
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/han26f_interspeech.pdf

## 问题
EMG 到语音（ETS）常把音素分类仅作辅助损失，语言信息未显式条件化生成，外部文本/音素纠错也难回注到帧级声学合成。

## 方法
TAP-ETS：训练时以帧级音素嵌入经交叉注意力注入 mel 解码器（EMG 特征为 Q，音素为 K/V），并保留辅助音素分类。推理时用 TAP 精炼：把合并音素/文本纠错（如 MONA-LISA+GPT）经 Levenshtein 时长重分配与掩码 Transformer 再对齐到 EMG 帧，无需改合成骨干。在 Gaddy silent EMG 基准评测。

## 实验与结果
相对 Gaddy/Scheck，Acc 73.03%、PER 15.59%、CER 11.15%、WER 19.77%（基线 WER 约 25–26%），达文中所称 SOTA。消融：Lev 与掩码精炼互补；帧级音素条件优于文本或合并序列条件。

## 结论
帧对齐音素条件 + 可插拔精炼管线可显著提升静默 EMG 可懂度，并使任意音素/文本纠错模块无缝接入。

## 点评
把“音素从监督变成可控条件”是对 ETS 控制力的关键升级。精炼依赖外部强纠错（识别 WER 12.70%）与 DTW/MFA 对齐质量；测试集仅 98 句静默样本，规模有限。

