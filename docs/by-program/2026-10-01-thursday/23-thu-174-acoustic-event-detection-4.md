# Acoustic Event Detection 4

- 日期：Thursday 1 October 2026
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

本场从资源高效 SED、Audio LLM 多事件定位可靠性、训练免费歧义消解，到注意力结构剪枝、鸟鸣发育可塑性无监督度量与音频主动学习。共同关切是：复杂场景下检测/理解既要准又要省，且模型在多事件与噪声下易幻觉或不确定。

效率侧，教师无关时间蒸馏与注意力通道二阶剪枝把大模型能力压到边缘预算。理解侧大规模敏感度分析显示事件数增加则真阳降、假阳升，提示词在两者间强权衡；RAISE 用选择性提取与听觉想象把预测锚定到显式声学证据。标注效率上 TSAL 用时—频谱模式引导采样；发育生物声学则用轨迹方差无标签量化可塑性。

## 论文技术总结

# Teacher-Agnostic Temporal Knowledge Distillation for Resource-Efficient Sound Event Detection

- 论文编号：855
- 报告人：Gihun Son
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/son26_interspeech.pdf

## 问题
SED 需要帧级检测，但 SOTA 多依赖大容量模型，资源受限场景表现不足。异构教师—学生蒸馏不稳定，而面向 SED 的 KD 研究有限，直接套用图像侧 OFA-KD 又难以传递时序上下文。

## 方法
提出 TAT-KD：以教师 logits 为统一蒸馏空间，训练时在学生各编码阶段挂接 Temporal Context Projector（卷积对齐时间分辨率 + Conformer 建模时序 + MLP 投影到类别维），推理时去掉以保持轻量。提出 TCAD：对温度锐化后的教师软标签按 |ŷ−0.5| 归一化置信度加权 BCE（τ=0.5，γ=2），作用于中间投影与最终输出；最终仅用蒸馏损失、不加监督 CE。学生为 SE-CRNN 变体 SC32/16/8/4；教师含 ATST-SED、JiTTER、MDFD-SED 及用 TAT-KD 从 JiTTER 蒸馏得到的 MDFD-TAT。

## 实验与结果
在 DESED（DCASE 2023 Task 4）上以 PSDS1 评估。TAT-KD 在全部教师—学生对上优于 from-scratch、logit KD 与 feature KD；SC32←MDFD-TAT 达 PSDS 0.574（4.548M 参数、3.668G MACs）。TCP 优于 MLP/CNN/RNN 投影器；TCAD 优于普通 BCE。ATST-SED 教师 PSDS 最高但蒸馏增益较小，消融显示其对 median filtering 依赖更强（0.583→0.495）。

## 结论
TAT-KD 通过教师无关的 logits 接口、TCP 与 TCAD，在 DESED 上稳定提升轻量 SED 学生，并保持推理效率，优于训练自零与标准 KD。

## 点评
把 OFA-KD 改造成帧级时序蒸馏，并用置信度加权抑制模糊教师信号，切中 SED 边界定位需求。MDFD-TAT 与学生架构相近时蒸馏最强，说明“教师无关”仍受结构亲和影响；强依赖后处理的教师（如 ATST-SED）作软标签时增益有限，是部署时需甄别的点。


# A Sensitivity Analysis of Multi-Event Audio Grounding in Audio LLMs

- 论文编号：1684
- 报告人：Taehan Lee
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/lee26o_interspeech.pdf

## 问题
Audio LLM 在复杂声学场景中的事件定位与幻觉可靠性研究不足：既有幻觉评测规模小或标签本体不一致，主流基准也未隔离“场景事件数”对 grounding/假阳的影响。

## 方法
从 AudioCapsV2（约 71K 片段）用 LLM 抽取并人工规范化 (source, attribute) 事件，得约 145K 事件、578 类常见事件；约 74% 样本含多事件。对 present-event 做存在性检测；absent-event 用 ReCLAP 音频对齐文本嵌入按相似度过滤（α=0.3）后采样，避免近义声学事件被误判为幻觉，共约 356K 负查询。评测 Qwen3-Omni-30B、Qwen2.5-Omni-7B/3B、Audio-Flamingo 3-7B，12 种提示（4 问句 × 3 回答约束），每模型约 50 万 yes/no 查询；并分析输出 token 置信度与 prompt 敏感性（Kendall τ_bias、复杂度间隙相关）。

## 实验与结果
事件数从 1 增到 5 时，present TPR 约降 29 pp，absent FPR 约升 8 pp。提示在高 TPR 与低 FPR 间强权衡（τ_bias 为负，约 −0.66 至 −0.90）。条件 FPR（正确识别 ≥75% present 时）仅比整体 FPR 低 ≤0.3 pp。正确回答置信度随事件数上升而下降；错误回答置信度趋势不一。SSL 音频嵌入的 erank 亦随事件数升高，支持复杂度代理合理。

## 结论
当前 SOTA Audio LLM 在多事件场景中区分“在场/不在场”仍困难；提示会诱导 Yes/No 偏差并与复杂度敏感性耦合；复杂度升高时模型更不确定。作者希望该评测推动忠实音频 grounding 研究。

## 点评
贡献主要在大规模、可控的多事件评测协议（规范化事件 + 声学对齐负采样），而非新模型。强在把复杂度、提示偏差与置信度串成证据链；事件来自 caption 抽取，可能遗漏未写入字幕的声学事件，且 absent 过滤依赖 ReCLAP 相似度阈值，负例难度分布仍受阈值影响。


# RAISE: Resolving Ambiguity in Audio Understanding with Imagination and Selective Extraction

- 论文编号：1739
- 报告人：Yueqian Lin
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/lin26i_interspeech.pdf

## 问题
Audio LLM 在噪声干扰或细粒度歧义下易出现感知幻觉；单次前向无法对照原始信号验证感知。鸡尾酒会重叠说话、相近音色乐器等任务分别需要源隔离与比较参照，但现有系统对所有查询套用同一单遍策略。

## 方法
提出训练无关框架 RAISE：语义路由（gpt-4o-mini，仅看问题与选项）将查询分到 DIRECT / IMAGINE / EXTRACT。Auditory Imagination 用 Stable Audio Open 为可合成候选生成参照音频，再与原音频联合比较推理；Selective Extraction 先让 Audio LLM 描述目标声特征，再用 SAM-Audio 开集分离得到干净信号后重问。工具失败则回退 DIRECT。骨干为 Qwen2-Audio-7B、Qwen2.5-Omni-7B、Qwen3-Omni-30B-A3B-Thinking（需支持多音频输入）。

## 实验与结果
在 MMAR 与 MMAU 上，相对单遍基线最高提升 +12.4%（Qwen2-Audio@MMAR：45.1→57.5）；Qwen3-Omni 在 MMAR/MMAU 为 +10.2% / +6.6%。路由将约 75.8%（MMAR）/ 82.2%（MMAU）查询走 DIRECT，摊销耗时约 9.1 s / 7.6 s。CoT、Self-Refine 无益甚至下降；静态全量 Extraction/Imagination 低于基线；单工具路由低于完整 RAISE。增益集中在时序推理、感知、和声、情感等子类。

## 结论
通过在推理时用生成与分离实例化证据，RAISE 无需参数更新即可缓解感知歧义；局限是依赖外部工具并增加被路由样本的延迟，作者建议蒸馏生成器与批处理分离来缓解。

## 点评
核心洞察是“感知瓶颈不能靠更多文本推理补救”，用 analysis-by-synthesis 与分离做验证，消融设计清晰。强依赖多音频输入骨干与工具质量；错误回归多来自过度剥离有用上下文或参照过窄，路由误判时代价不小。


# The silence of the weights: a structural pruning strategy for Attention-based audio signal architectures with second-order metrics

- 论文编号：2026
- 报告人：Mathieu Fontaine
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/diecidue26_interspeech.pdf

## 问题
Transformer 注意力层参数与算力开销大；音频侧结构化剪枝多整头或 token 删除，对 Q/K/V 通道级细粒度剪枝探索不足。幅度剪枝还会因层间尺度差异偏向剪早期层。

## 方法
提出面向注意力块的通道级结构化剪枝：在满足 Q/K 同维、V/O 同维约束下，对每个头独立选择待删通道（per-head，PH），用贪心预算分配达到目标稀疏度；并与整头剪枝（EH）对比。重要性用 Fisher information（参数梯度平方期望）评分，对比 L 范数幅度；阈值策略分全局（G）与逐层局部（L）。在 AST（AudioSet、SpeechCommands）与 Whisper-medium（转录/翻译）上迭代剪枝：每步剪注意力块 10% 参数，共 10 步，剪后用 LoRA（AST）或大规模多语料（Whisper）微调。

## 实验与结果
Fisher 优于幅度，且全局阈值更合适；幅度宜用局部阈值。PH+FI 与 EH+FI 性能接近：60% 稀疏度下 SpeechCommands 准确率约 97.71%、AudioSet mAP 约 30.86%。整头剪枝推理略快 1–2 ms。Whisper 英文/意/法转录 WER 在 50% 稀疏附近仍接近原模型（约 1% 内）；翻译（CoVoST DE→EN BLEU）下降更大，作者归因于该语向微调数据较少。

## 结论
结合 Fisher 的通道级剪枝可与整头剪枝相当，注意力参数减半时分类/转录性能基本保持。未来可探索 CV/NLP、头与通道联合剪枝，以及放宽同层各头通道数一致的约束。

## 点评
把 NLP 侧 QKV 通道剪枝思想落到 AST/Whisper，并用 Fisher 缓解幅度偏置，工程上完整。PH 在精度上能追平 EH，但速度收益略逊；翻译任务掉点更明显，说明任务与微调数据量会限制“剪半无损”叙事。标题写 structural，正文亦称 structured，与实现一致。


# Trajectory Variance: An Unsupervised Measure of Developmental Vocal Plasticity in Birdsong

- 论文编号：3557
- 报告人：Kanghwi Lee
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/lee26z_interspeech.pdf

## 问题
鸟鸣发育中，静态声学描述只能刻画某一时刻的声音，无法回答“若在另一发育年龄发出，会差多少”。需要无需类型标签的逐发声可塑性度量，以区分学习性音节与先天叫声等发育动态。

## 方法
对每只鸟独立训练谱图 VAE（123×100→128 维 latent）。因无纵向同发声轨迹，用 minibatch OT（Hungarian）构造跨年龄训练对；6 层 AdaLN 残差 MLP 学习年龄条件位移 δ，一次前向得到反事实 latent：z_cf = z_src + f_θ(z_src, a_src, a_tgt)。对每条发声在 T=7 个均匀目标年龄生成反事实，定义 trajectory variance 为各维跨年龄方差之和。用 bout 启发式（间隙 <200 ms 且 bout≥3 标为 song）做 song/call 标签，避免与谱特征循环。

## 实验与结果
三只斑胸草雀（183K–274K 发声，40–101 dph）。duration-残差后 song/call：Cohen’s d_r=0.29–0.57，AUC=0.58–0.67；Gaussian OT、per-age k-NN、per-age OT 均不能在全部鸟上一致分离。轨迹方差与谱平坦度负相关（r=−0.48 至 −0.75），与时长正相关（r=0.70–0.80，故报告残差化指标）。解码反事实 FAD 0.01–0.06（仅作解码诊断）。

## 结论
学习到的位移模型可在无类型标签下提供发育可塑性分数，并与经典谱描述对齐；局限包括无纵向真值、时长混淆需残差化、标签启发式偏差，以及仅三只同种鸟、外推未验证。

## 点评
把单细胞 OT/反事实思路迁到鸟鸣发育，度量目标清晰：预测变化量而非分类。强在对非参数基线的系统对照；证据仍是横截面人口匹配，个体真实轨迹不可验证，且 AUC 仅中等，更适合作为可塑性探针而非部署级分类器。


# Beyond Uncertainty and Diversity: Temporal-Spectral Guided Active Learning for Audio

- 论文编号：1719
- 报告人：Qisheng Xu
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/geng26c_interspeech.pdf

## 问题
音频有监督微调标注成本高，主动学习（AL）可降本，但现有方法多依赖通用不确定性或几何多样性，把音频当静态向量，忽视决定样本信息量的时频谱结构，导致选样次优。

## 方法
提出 Temporal-Spectral Active Learning（TSAL），骨干为 SSAST。每轮在已标注集上微调后，用 soft-loss 分布筛选高于平均损失的标注样本作为时频谱“信息模式”锚点；对未标注样本提取特征嵌入，并以伪标签反传得到输入梯度，用特征—梯度余弦相似度与锚点匹配打分（β 平衡两项），选 top-B 送标。初始标注 10%，每轮查询未标注 5%，至总预算 40%。

## 实验与结果
在 ESC-50、AudioSet-20k、DCASE2016、UrbanSound8K 上对比 CONF、MARGIN、ENTROPY、CORESET、BALD、CLS-AL、RANDOM。40% 预算时 ESC-50 准确率 82.65%（RANDOM 79.90%），AudioSet-20k mAP 22.08%（RANDOM 19.89%），UrbanSound8K 82.54%，DCASE2016 约 79.23–79.74%。消融显示 soft 选择、特征相似与梯度相似缺一不可；β=1.0 较稳且最优。

## 结论
用 soft-loss 刻画信息模式、再以特征—梯度对齐选样，可在有限标注预算下稳定优于通用 AL 基线，说明时频谱结构引导对音频 AL 必要。作者计划扩展到音频—语言任务。

## 点评
把“难学样本的优化轨迹”当作时频谱结构的可操作代理，避开手写声学规则，工程上可插拔。叙述上“时频谱结构”与 soft-loss 之间仍是间接假设，正文没有独立验证所选样本确实富含瞬态/谐波等结构；在类别极不平衡或伪标签很差时，梯度匹配可能放大噪声。

