# Post-Training of Speech Foundation Models

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Special Session
- Area：14
- 论文数：13

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本专题聚焦语音基础模型后训练：把通用 SSL/LLM 表征改造成任务特异、模态锚定、时间细粒度或计算高效的形式。手段包括帧级监督扰动、干预对比解耦、统一话语属性编码器、声学接地推理蒸馏、指令级偏好优化、对比音频感知蒸馏，以及文本侧 CTC 仿真与深度上扩。

安全与表示侧，混合帧后训练让 SSL 学局部伪造不一致；干预对比把纠缠空间分到内容/说话人子空间；统一框架联合学语义与说话人话语表示。音频 LLM 推理上，PolyBench 暴露复调组合推理瓶颈；Step-Audio-R1/MGRD 纠正“文本替身推理”；CAAD 把对比解码内化到学生权重以降时延。

生成与 ASR 侧，ALLM 细粒度反馈做 TTA 指令遵循 DPO；LLM 语义先验蒸馏进仅编码器多说话人 ASR；TASU2 可控 WER 的 CTC 仿真服务低资源对齐；深度上扩插入层保文本能力；知识定位编辑与音频侧时间提示强化事实与时序感知；交错堆叠加速蒸馏部署。

## 论文技术总结

# Supervised Post-training of Speech Foundation Models for Robust Adaptation in Speech Deepfake Detection

- 论文编号：908
- 报告人：Zihan Pan
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pan26_interspeech.pdf

## 问题
SSL 语音基础模型（如 WavLM）预训练目标偏音素/长程内容，对深度伪造中局部频谱–时间不连续不敏感；直接端到端微调在低资源与域外条件下易过拟合已知攻击。

## 方法
提出 Mix-Frames Post-Training（MFPT）三阶段：① 从相反类别抽取 injector，固定长度裁剪/填充后按比例 r_mix 做句内 cut-and-paste，并按帧中心是否落在注入段赋帧级标签；② 在混合波形上用线性帧分类头 + BCE 监督，经 LoRA（QKV+FFN）更新 SSL；③ 丢弃帧头，保留适配编码器，再用 Attentive Merging + 话语级分类头（LSTM / ECAPA-TDNN / Nes2Net）做 CE 微调。骨干为 WavLM Large，默认 r_mix 10–30%。

## 实验与结果
ASVspoof5 上无数据增强的单模型 EER 4.50%（ECAPA，QKV+FFN LoRA），优于文中所列多数单模型/部分融合系统。r_mix 过大（50–70%）恶化至 7.31%。低资源：在 ASV5 后训练后再用不同比例 ASV19LA 微调，相对无后训练在 ASV21DF 等域外增益明显（如 20% 数据时 DF EER 9.32%→4.34%）。ASVspoof2021 LA/DF：EER 3.88%/4.04%，绝对差距仅 0.16，最差情形与跨条件稳定性优于多篇对比系统。

## 结论
作者认为监督式后训练能把表示偏向局部伪造线索，再做话语级微调，可提升低资源与跨失真鲁棒性，并在 ASV5 取得无增强单模型 SOTA 级结果。

## 点评
核心是“先用伪造式局部拼接学帧级不一致，再做任务微调”，比直接微调更贴伪迹形态。强项是低资源与 LA–DF 平衡；弱项是混合比例与分类头需调，且 cut-and-paste 伪迹是否覆盖真实 VC/TTS 全谱仍依赖实验外推。


# Learning task-specific subspaces via interventional post-training of speech foundation models

- 论文编号：2542
- 报告人：Jack Cox
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cox26_interspeech.pdf

## 问题
SSL 语音基础模型的表示把说话人与内容等变量纠缠分布在同一空间；下游任务通常只需部分变量，标准对比学习多学单一不变子空间，缺少基于干预数据的因果式多子空间分离。

## 方法
提出 interventional contrastive learning：用 F5-TTS 在 LibriTTS 参考音上合成可干预数据（训练 32 说话人×256 文本=8192 句，开发 6×256=1536），按说话人–内容矩阵构批。冻结 wav2vec 2.0 / HuBERT / WavLM Base，均值池化后经约 1.8M 参数 3 层 MLP，将 768 维切成内容/说话人各 384 维子空间；多正样本对比损失（温度 \(\tau\)）加子空间正交正则。对比单子空间变体与无投影基线。评测：子空间直接余弦相似度做 VoxCeleb1 OOD 说话人验证（EER）；SUPERB 式线性头做 Speech Commands 关键词检出（准确率）。

## 实验与结果
说话人匹配子空间相对无投影显著降 EER（如 WavLM：38.7→约 24.7）；内容匹配子空间 KS 准确率低于池化骨干（WavLM：96.9→93.0），但仍有一定竞争力。匹配与不匹配子空间的 SV 差距支持一定分离；联合学习未必优于分别学单子空间。wav2vec 2.0 末层整体更弱。绝对 OOD EER 仍高（约 25%），因合成朗读 vs 野外语音且仅 32 说话人。

## 结论
作者认为干预对比后训练能把说话人信息从纠缠表示中拆出并改善 OOD SV，同时维持相近 KS；联合学习未显示额外收益。后续拟扩到真实大数据、换层加权并显式惩罚信息泄漏。

## 点评
工作把因果干预/合成可控对用到语音后训练，子空间交叉评测设计清晰。强项是弱标签干预矩阵与正交约束的可解释性；脆弱点在于 TTS 域与 VoxCeleb 差异大、内容对比目标（整句）与 KS（词级）错位，且末层特征与信息泄漏仍限制分离纯度。


# Learning Multiple Utterance-Level Attribute Representations with a Unified Speech Encoder

- 论文编号：3350
- 报告人：Maryem Bouziane
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bouziane26_interspeech.pdf

## 问题
SAMU-XLSR/SONAR/SENSE 等后训练把语音对齐到句级语义空间，利于多语检索，但易压制说话人等副语言信息；缺少单一编码器同时产出多种 utterance 级属性表示的统一框架。

## 方法
在 SENSE 式教师–学生对齐上扩展多任务分支：共享 w2v-BERT 2.0 编码器，每属性 \(\tau\) 有层投影、可学习层插值权重 \(\lambda_{\tau,\ell}\)、注意力池化与可选线性头，与冻结教师余弦对齐。语义教师为 BGE-M3，说话人教师为 VoxCeleb 上预训练的 ECAPA-TDNN。在 Common Voice 19（BGE-M3 支持的 83 语，约 8250 小时）加权采样训练 350K 步（8×H100）。评测：VoxPopuli/MTEDx/FLEURS 多语 speech→speech / speech→text 检索 R@1；VoxCeleb1-O 说话人验证 EER/minDCF。

## 实验与结果
Att(sem+spk) 在 VoxPopuli 等对上 R@1 略低于纯语义 Att(sem)、明显优于 SONAR；FLEURS 低资源对（如 my-en）甚至略升。说话人验证：Att(sem+spk) EER 0.91%，接近 ECAPA 教师 0.90%，略好于单任务 Att(spk) 0.93%。层权重分析：语义集中在约 13–14 层，说话人更偏高层（约 23–24）且分布更广。

## 结论
作者认为统一编码器可经多分支联合学习语义与说话人表示而互不严重拖累；层选择自动互补。后续拟加入情感、语言、口音等更多属性。

## 点评
做法把“一句一语义向量”推广为多属性分支，用层插值缓解任务干扰，工程上贴合 SENSE。强项是检索与验证双线证据加层可视化；脆弱处在于两教师空间是否正交依赖训练权衡，扩展到更多属性时分支干涉与算力成本仍未知。


# PolyBench: A Benchmark for Compositional Reasoning in Polyphonic Audio

- 论文编号：2466
- 报告人：Yang Xiao
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26aa_interspeech.pdf

## 问题
现有 LALM 评测多关注指令跟随或时序推理，对多声源重叠（复调）场景下的组合关系覆盖不足；重叠导致事件混淆与幻觉，而顺序/时长类基准很少显式测并发组合推理。

## 方法
构建 PolyBench：从 DataSED、DESED、MAESTRO-Real 抽取真实重叠片段（约 169+259+300 条，长音频裁到约 25s），用事件类与时间戳生成五类 MCQA——Counting、Duration、Concurrency、Classification、Detection；问题模板经 Qwen3-Max 改写并由人工质检。Concurrency 额外混入 AudioTime 单声源以平衡正负例。评测开源 LALM（Qwen3-Omni-30B-A3B、R1-AQA、Audio Flamingo 3、TimeAudio+Qwen3-8B、AUDSEMTHINKER-QA GRPO），用 ACC/F1，并以 NV-Embed-v2 做语义匹配；推理模型要求 CoT。

## 实验与结果
难度分层明显：Counting/Detection 最难（Qwen3-Omni 分别约 57.5% / 63.4% ACC；多数模型 Detection 仅约 37%）。Concurrency/Classification 相对更好（Qwen3-Omni 约 83.1% / 77.9%）。TimeAudio 级联在 Detection 上第二（约 51.7%）。Concurrency 在纯复调上可能虚高，混入单声源后正确率大幅下降，暴露捷径学习。

## 结论
作者认为复调组合推理是当前 LALM 瓶颈：感知不稳会在计数与区间定位上放大；需加强底层事件/时序建模与跨模态约束决策。基准已公开。

## 点评
工作把“重叠声学场景”拆成感知→关系→结构决策的五级 MCQA，能暴露纯时序基准看不到的失败。强项是真实数据与捷径诊断；脆弱点在于 MCQA 与选项设计可能低估开放生成难度，且部分指标（如 F1/ACC 差）对模型偏差敏感。


# Step-Audio-R1: Why Audio LLMs Fail at Reasoning — The Trap of Textual Surrogates

- 论文编号：256
- 报告人：Xiangyu Zhang
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26b_interspeech.pdf

## 问题
文本/视觉 LLM 常随测试时计算（更长 CoT）变强，而 Audio LLM 往往“越推理越差”；根因被归结为 textual surrogate reasoning——用转写/字幕式抽象代替声学证据，源于从文本 CoT 初始化带来的模态错位。

## 方法
提出 Modality-Grounded Reasoning Distillation（MGRD）：架构沿用 Step-Audio 2（冻结 Qwen2 音频编码器 + 12.5 Hz 适配器 + Qwen2.5-32B），输出 `<think>` 链再答。冷启动约 5M 样本联合 SFT/RLVR；随后迭代：对需感知分析的音频题自蒸馏声学推理链（Pass@k + LLM 裁判过滤）、多模态 SFT、再 PPO 多模态 RL（音频奖励 0.8 准确 + 0.2 格式）。难度筛选保留 pass@8∈[3,6] 题。另用迭代过滤 + DPO 纠“自称不能听音频”的自我认知偏差。

## 实验与结果
Speech-to-text 均值 83.6，高于 Gemini 2.5 Pro（81.5）、接近 Gemini 3 Pro（85.1）；BBA 达 98.7。Realtime 变体 Big Bench Audio 语音推理 96.1%、首包延迟 0.92s。消融：格式奖励防止推理长度塌缩（约 3000→1500 token），MMAU 76.5→77.7；中等难度数据优于全失败集；自我认知错误率由 6.76% 经蒸馏至 2.63%、DPO 后 0.02%。

## 结论
作者认为失败不在“推理本身”，而在锚定错误模态；MGRD 使测试时加长思考对音频有益，Step-Audio-R1 在多项基准上可比前沿闭源模型。

## 点评
诊断“文本替身推理”并把后训练目标从“对齐答案”推到“对齐声学证据”，对 Audio CoT 领域有针对性。强项是奖励设计与难度课程的训练动态证据；脆弱点在于强依赖裁判/过滤质量与大规模冷启动资源，声学接地是否可迁移到更开放场景仍需验证。


# Improving Text-to-Audio Instruction Following via Fine-Grained Feedback from Audio-Aware Large Language Models

- 论文编号：1111
- 报告人：Chun-Yi Kuan
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kuan26_interspeech.pdf

## 问题
TTA 在 FAD/CLAP 等全局指标上已强，但多事件与时间顺序指令常失败；现有偏好数据多靠 CLAP/启发式/人工，缺可扩展的指令级正确性监督。

## 方法
用 ALLM 作细粒度裁判，判定目标事件是否存在与时间序是否正确；经基准与人工校验后，将满足/不满足样本构造成偏好对做 DPO。提出 S3Bench：叙事多事件指令约 1200 例（2–4 事件，LLM 生成叙述，仅评测不用训练）。

## 实验与结果
ALLM 与人在存在/时序判断上高一致（协议约 89.8%/93.5%）。DPO 后在既有基准与 S3Bench 上事件完整度、时序与联合指令遵循准确率提升，同时保持音频质量竞争力。

## 结论
作者认为 ALLM 细粒度反馈可规模化改进 TTA 指令遵循，并提供叙事评测基准 S3Bench。

## 点评
把理解侧 ALLM 接到生成侧训练信号，打通“能听懂指令→能生成符合指令”。依赖 ALLM 偏置；S3Bench 叙述由 LLM 生成，可能与裁判同族。相对 Baton 人工标注更可扩展，相对 CLAP 更对准事件/时序。


# CAAD: Contrastive Audio-Aware Distillation for Efficient Speech Language Models

- 论文编号：645
- 报告人：Chun Wei Chen
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26e_interspeech.pdf

## 问题
Speech LM 参数大且易被语言先验压过声学证据；对比解码（正路径音频 / 负路径纯文本）可增强接地但双倍推理延迟。标准知识蒸馏会把教师的语言偏置一并拷给小模型，且逐步自回归对比目标训练难并行。

## 方法
提出 Contrastive Audio-Aware Distillation（CAAD）：Stage 1 按 DeSTA 从音频元数据（性别、情感、环境等）用 Llama3-8B-Instruct 生成 Pseudo-GT 锚序列；Stage 2 对冻结教师同步 teacher-forcing 正/负路径，目标 \(\hat{z}=(1+\alpha)z^+-\alpha z^-\)，学生对齐 KL（温度 \(\tau\)）并加 Pseudo-GT CE，总损失 \(\lambda L_{CD}+(1-\lambda)L_{GT}\)。学生为 DeSTA2 的 Llama-3.2-3B（教师 8B），仅训 Q-Former 适配器约 32M 参数；DeSTA2 指令数据，A6000 约 70 小时。评测 Dynamic-SUPERB 五维与 MCR-BENCH 情感冲突（Shift）。

## 实验与结果
3B CAAD 在 Dynamic-SUPERB ALL 54.44，高于 Std. KD 50.40、测试时 CD 学生 35.80，并在部分副语言任务超教师 greedy。MCR-BENCH：Acc_neu 45.90、Shift 79.03（Std. KD Shift=100）。\(\alpha=1.0\) ALL 最高 55.00，\(\alpha=2.0\) Shift 最低；元数据锚优于直接音频同步。

## 结论
作者认为把对比音频感知内化到单路径学生可降延迟并减语言偏置；局限是蒸馏收益受师生能力差约束，对已很强的小模型增益可能有限。

## 点评
核心是用 Pseudo-GT 解锁全序列对比蒸馏，把推理期双路径成本前移到训练。强项是偏置指标与 \(\alpha\)/锚消融完整；脆弱处在于 Pseudo-GT 质量决定目标分布，且只训适配器时表征上限仍受冻结 LLM 限制。


# Distilling LLM Semantic Priors into Encoder-Only Multi-Talker ASR with Talker-Count Routing

- 论文编号：612
- 报告人：Hao Shi
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shi26_interspeech.pdf

## 问题
多说话人 ASR 若用 LLM 作自回归解码慢且在重度重叠/三说话人上不稳；编码器侧序列化 CTC 虽快，但缺语义正则、训练易崩，且多数方法假定固定说话人数。

## 方法
编码器-only MT-ASR：WavLM-Large 共享前 12 层 + 二/三说话人各 12 层分支（共享层冻结），LSTM 分离器 + 序列化 CTC。训练期用 LLaMA-3.2-1B：先 LoRA/特殊 token 适配多说话人 SOT 并反传蒸馏到编码器，再固定 LLM，用 \(\alpha L_{\text{Serialized-CTC}}+(1-\alpha)L_{\text{SOT}}\) 训分离器/CTC。Talker-Count Head（注意力池化 \(\mu,\sigma\) + MLP）预测 2 vs 3 人并路由分支。数据为 LibriMix（含噪声）。

## 实验与结果
无 LLM 蒸馏时序列化 CTC 几乎训不动。oracle 说话人数下，noisy eval 2mix/3mix WER 约 9.6/22.2，优于 SOT-Llama-1B 的 11.3/39.1。TCH+12 层时 talker-count 准确率 noisy eval 约 93.7%，2mix/3mix WER 约 9.7/24.5。RTF：CTC 约 0.0043/0.0106 vs Llama-1B 约 0.115/0.098。与更大 LLM/SOT 系对比：2 人可比，3 人显著更好。

## 结论
作者认为把 LLM 语义先验蒸馏进编码器可保留 CTC 速度并稳住重叠表示；TCH 支持可变人数。三说话人计数仍难，后续拟加强噪声/重叠下的计数鲁棒性。

## 点评
把 LLM 从“推理解码器”降级为“训练教师”，对准多说话人瓶颈很务实。强项是 3-mix 与 RTF 收益清晰；脆弱点在 TCH 三说话人准确率不足会拖累整体，且仍限在 2/3 人分支而非开放人数。


# TASU2: Controllable CTC Simulation for Alignment and Low-Resource Adaptation of Speech LLMs

- 论文编号：866
- 报告人：Jing Peng
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/peng26b_interspeech.pdf

## 问题
Speech LLM 后训练缺大规模音文对成本高；TASU 用文本随机模拟 CTC 后验可做纯文本对齐，但对不确定性与错误率可控性弱，课程设计偏启发式，低资源适配时易伤源域。

## 方法
提出 TASU2：学习 WER 条件文本→CTC 后验模拟器（6+6 层 Transformer，隐维 512）。用 LibriSpeech 约 1/7 加噪/混响，教师 ASR 产出真实 CTC 后验与假设，按 WER 分三档（0–6%、10–40%、50–150%）作控制码，以分布级 CE 匹配后验。推理时指定档位自回归生成伪后验，经投影送冻结 SenseVoice-Small + Qwen2.5-1.5B。两阶段后训练可做源→目标（如 Medical）文本 Sim-CTC 适配（LoRA）。

## 实验与结果
后验相似度优于 TASU-style（CE 2.51→1.23，KL 2.34→1.05）。WER 分档可分离实现错误率。Libri 训练下 TASU2 分档：clean/other 3.41/8.15，Slide/TED 优于原 TASU。Medical 两阶段：目标 WER 12.12，优于 raw text 13.62、TTS 12.79、raw audio 12.35，且源域相对 Stage1 几乎不变（约 +0.02/+0.07）。多任务下 Libri 大升、CoVoST2 BLEU 与 TASU 接近。

## 结论
作者认为可控 CTC 模拟能更好贴合声学解码接口，强化纯文本对齐与低资源迁移并保留源域；可作缺配对音频时的 TTS 替代。

## 点评
相对 TASU，关键是把“随机扰动”换成“教师后验 + WER 旋钮”，让课程与域适配可调度。强项是保真度指标与 Medical 迁移对照完整；脆弱处在于模拟器依赖教师 ASR 与 Libri 增强分布，极端域的音素混淆是否可迁移仍存疑。


# Adapting Text LLMs to Speech via Multimodal Depth Up-Scaling

- 论文编号：2099
- 报告人：Kazuki Yano
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yano26_interspeech.pdf

## 问题
把预训练文本 LLM 经语音持续预训练变成 Speech LM 时常严重损伤原文本能力；文本回放成本高且多数模型不公开预训练数据，LoRA 对跨模态容量可能不足。

## 方法
提出 Multimodal Depth Up-Scaling：扩展词表加入语义+声学离散语音 token（原 embedding 冻结），在冻结文本 LLM 中插入约 25% 新层并仅训练新层；零初始化输出投影使新层初始为恒等。放置策略：INTERLEAVED / SANDWICH / TOP / MIDDLE / BOTTOM。另用 E-Branchformer（全局 MHSA + 局部 cgMLP，\(W_{\text{Merge}}=[I;0]\) 函数保持初始化）作插入层，cgMLP 仅作用于语音 token。推理可丢弃新层完全恢复预训练。基座 SmolLM2-360M/1.7B，OWSM v3.2 英语 ASR 约 48k 小时，无文本回放。对比全参微调与参数量匹配的大秩 LoRA。

## 实验与结果
INTERLEAVED 上 ASR 接近全参（1.7B：clean/other 约 2.4/5.5 vs 2.3/5.6），文本平均降幅远小于全参/LoRA（1.7B：\(\Delta\) -8.3 vs -32.6/-35.7；TOP 文本最好 \(\Delta\) -2.7）。E-Branchformer 进一步把 1.7B WER 提到约 2.3/5.3、文本 \(\Delta\) -6.8，可训参数约少 60%。零样本语音条件翻译/简化/摘要：深度扩展仍产出连贯文本，全参微调退化为重复 token。

## 结论
作者认为插入可丢弃新层可在少伤文本的前提下学 ASR；E-Branchformer 插入层进一步提升声学适配。后续拟扩展到更多语音任务与语言。

## 点评
“冻主干 + 插层”把遗忘问题从权重更新转为容量分配，比回放/LoRA 更可恢复。强项是放置/架构消融与指令跟随定性证据；脆弱点在于推理保留新层仍有文本开销，且实验限英语 ASR、未与回放组合。


# Localizing and Editing Knowledge in Large Audio-Language Models

- 论文编号：2066
- 报告人：Jiaheng Dong
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/chung26_interspeech.pdf

## 问题
LALM 在语音理解上表现强，但训练语料静态，可能编码过时或错误事实。文本 LLM 的 locate–then–edit（如 ROME、MEMIT、AlphaEdit）依赖离散 token 腐蚀，无法直接处理连续语音，也不清楚事实知识在音频编码器与 LLM backbone 中如何分布，以及编辑是否会破坏音频–文本对齐。

## 方法
构建面向 LALM 的语音事实定位与编辑基准，并提出语音驱动的 locate–then–edit 框架。事实表示为三元组 (s, r, o_c)，用口语 prompt 探测。定位阶段用 speech-aware causal tracing：clean / corrupted / corrupted-with-restoration 三轮前向；借 WhisperX 对齐定位主语跨度，对音频编码器首层输入加高斯噪声腐蚀，再按层窗（±4）恢复 clean 隐状态，用 Indirect Effect / AIE 标定关键层与 MLP、attention 模块。编辑阶段基于线性 key–value 假设做参数扰动，比较单层 / 多层编辑，以及仅音频、仅文本与顺序跨模态（先改音频再改 LLM）策略；多层编辑对受保护 key 做零空间投影以降低干扰。骨干为 Qwen2-Audio-7B-Instruct。

## 实验与结果
数据基于 CounterFact 与 Known-1000，经 Gemini 2.5 Flash TTS 转语音；定位分别保留 250 / 100 条模型预编辑正确样本，编辑用 500 条 CounterFact 子集。指标为 Efficacy / Paraphrase / Neighbor Score 及均值 S。因果追踪显示事实联合编码于音频编码器与 LLM，CounterFact 上音频中后层（约 25–31）与主语首词 AIE 更强，MLP 在文本中层贡献大。编辑上跨模态单层整体最优（S=77.60，ES=95.20，PS=78.70，NS=64.72），优于单模态编辑与微调；带参数重置的多层跨模态可达 79.67。层与词位选择上，AIE 更高的位置编辑效果更好。

## 结论
作者认为语音感知因果追踪能定位口语事实存储位点，并指导更有效、更特异的参数更新；跨模态协同编辑优于标准微调。工作为语音 AI 中细粒度事实控制提供初步可行路径。

## 点评
这篇工作把文本模型编辑里的因果追踪迁到连续语音上，关键在于用对齐框定主语帧并在音频路径注入噪声，从而回答“事实藏在编码器还是语言骨干”。结果强调音频层是口语事实的锚点、跨模态编辑更稳，这与 LALM 的双塔结构一致。脆弱点在于依赖 TTS 合成的事实基准与单一骨干（Qwen2-Audio），以及单层编辑需样本间重置参数，多层累积更新仍易伤 Neighbor Score，真实噪声语音与开放域事实外推仍待验证。


# Towards Fine-Grained Temporal Perception: Post-Training Large Audio-Language Models with Audio-Side Time Prompt

- 论文编号：745
- 报告人：Yanfeng Shi
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/shi26b_interspeech.pdf

## 问题
LALM 在语义理解上较强，但对细粒度时间感知不足，难以精确推断声事件起止时间，限制了 audio grounding、sound event detection 等时序任务。现有时间标注数据或特殊时间 token 仍缺显式物理时间坐标，且 SFT 的 token 级交叉熵对边界小偏差惩罚过重，与对齐质量目标不一致。

## 方法
提出 TimePro-RL：先用 Audio-Side Time Prompt（ASTP），按音频编码器帧率把 Timestamp Token（如 `<0.04>`）交错插入音频特征序列，经 Timestamp Embedding 层映射；嵌入用对应数字子词嵌入均值做语义初始化，训练时冻结以防语义漂移。随后 SFT 教模型使用该 prompt，再以 GRPO 做 RL 后训练。奖励以 Event-based F1（Eb-F1）为主；当组内主奖励方差过低时，与辅助奖励（AG/SED 用 mIoU，DAC 用 METEOR）做逐元素乘积，形成 advantage-driven adaptive temporal reward。在 Qwen2-Audio 与 Qwen2.5-Omni 上用 LoRA（r=8, α=32）做参数高效微调。

## 实验与结果
任务包括 FTAR 上的 Audio Grounding 与 Dense Audio Captioning，以及 DESED 上的 Sound Event Detection。TimePro-RL 后训练的 Qwen2.5-Omni 在 AG 上达到 R@0.5=80.1、R@0.9=39.8、mIoU=74.4，SED Eb-F1=57.6，DAC METEOR=33.9、Eb-F1=40.7，优于同数据 SFT 的多种 LALM（含 TimeAudio、Kimi-Audio 等）。消融显示随机初始化 ASTP 会退步，语义初始化有效；再加自适应 RL 相对仅 Eb-F1 奖励更均衡，尤其挽回 DAC 的 METEOR。注意力可视化显示对 Timestamp Embedding 的关注集中在事件起止边界。

## 结论
作者认为 ASTP 与面向时间对齐的自适应 RL 协同，可显著提升 LALM 的细粒度时间感知；未来拟扩展到 CoT 等复杂推理场景。

## 点评
思路是给音频侧显式“时间坐标”，再用与评测指标对齐的 RL 修边界，直击 SFT 对时间偏差不友好的问题。语义初始化与主辅奖励自适应切换是务实设计。可能脆弱处在于强依赖帧率固定的时间 token 网格与较短时长覆盖（文中 0–30 s、0.04 s 步长），以及 RL 仅单 epoch、子集 10,200 样本——复杂重叠事件与更长音频上的外推仍需观察。


# Fast Speech Foundation Model Distillation Using Interleaved Stacking

- 论文编号：3071
- 报告人：Eungbeom Kim
- 程序：Thursday 1 October 2026 / Post-Training of Speech Foundation Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/kim26t_interspeech.pdf

## 问题
将大型语音基础模型（SFM）蒸馏为高效学生可降低推理成本，但学生训练本身仍耗时。Stacking 式阶段性加深可加速训练，而现有 gradual stacking、MIDAS 在各阶段会改变层位置；SFM 具有层特异知识，位置不一致易导致下游性能下降，也难稳定接入中间层 KD。

## 方法
提出 interleaved stacking：每阶段复制每隔 b 层选出的 K 层，并把复制层插在原层之后，使早/晚层在后续阶段仍保持相对前后位置。与输出级 MSE KD 及中间层 MSE KD 结合：中间层监督在初始浅模型上设定后全程保持，教师侧目标层索引固定。总损失为 L + w L_inter。教师为 HuBERT base（94.68M），学生为 12 层、宽 384 的 Transformer（26.87M），在 LibriSpeech 960h 上训练；B=4 阶段（每阶段加 3 层），比较 equal 与 prop-1 调度。

## 实验与结果
在 SUPERB 的 PR、ASR、SF、SID 上评估。InterleaveStack 在两种调度下均大幅优于 GradStack / MIDAS；prop-1 约 ×1.16 加速，PER=8.88、WER=9.99、SF F1=85.70、SID Acc=73.60，相对无 stacking 的 Full / Full L2L 在多项指标上持平或更好。中间层损失权重消融显示 w=0.5 较优；即便 w=0，方法在 ASR/SID 仍优于现有 stacking。Gradual stacking 难直接做层对层中间 KD（易发散），改用 prediction-style 中间损失整体仍不如 interleaved。层相似度分析显示复制层与原层保持高相似，并呈现更清晰的块状结构。

## 结论
作者认为 interleaved stacking 通过保持层位置一致性，在加速 SFM 蒸馏的同时减轻性能损失，并自然兼容中间层 KD；在 SUPERB 上显著优于现有 stacking 基线。

## 点评
核心洞察是蒸馏 SFM 时“层位一致性”比单纯堆深度更重要，把复制层邻接插入既利用相邻层相似，又稳住中间监督。方法简单、与现有 KD 配方兼容，实用价值高。边界在于实验主要围绕 HuBERT→固定 12 层学生与 SUPERB 子集任务；对更大规模教师、浅宽学生或非 MSE 蒸馏目标是否同样有效，正文未充分展开。

