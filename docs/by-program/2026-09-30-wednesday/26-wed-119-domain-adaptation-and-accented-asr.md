# Domain Adaptation & Accented ASR

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：8
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕口音/领域变异下的 ASR 与发音评测：从测试时自适应、轻量适配器与对比正则，到模型合并、激活转向与实时口音转换。共同目标是在不大规模全量微调的前提下，把预训练骨干适配到多样口音与多领域。

MDD 侧用测试时训练让 wav2vec 2.0 块内 MLP 模块在新样本上自监督更新；口音 ASR 则出现 Mixture-of-Accent-Adapters（按需特化 Whisper）、无口音标注的监督对比正则，以及在表示空间识别“口音敏感中间层”并做无参数激活转向。

多领域方面，模型合并被系统基准化，并提出 BoostedTSV-M 缓解秩塌缩；口音转换 AccentDrift 则用稀疏语音标记与流式缓存，在约 520 ms 延迟下做内容与身份保持的口音变换。整体呈现“适配成本下沉到测试时/轻量模块/合并/转向”的路径谱系。

## 论文技术总结

# SEA-MDD: Self-adapting Mispronunciation Detection and Diagnosis Models via Test-Time Training

- 论文编号：856
- 报告人：Minglin Wu
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wu26c_interspeech.pdf

## 问题
L2 发音检测与诊断（MDD）面对学习者水平与错误类型多样，固定训练集难覆盖分布外样本；大规模标注昂贵。已有 MAML 适应仍需目标说话人较多标注数据，形成二次数据稀缺。

## 方法
SEA-MDD：在 wav2vec 2.0 Transformer 块的自注意力与 FFN 之间插入 TTT 模块（默认两层 MLP + LN + 残差 + tanh 门控；另有 Linear 变体）。内外环：内环在训练与测试时对每个输入用自监督重构更新 MLP 权重 W（θ_K x 输入、θ_V x 目标，也可时间维 mini-batch b=32）；外环用 CTC 微调其余参数。测试时仅做内环、单句适应。

## 实验与结果
CU-CHLOE（34.6 h，粤/普通话学习者）。相对 wav2vec2-CTC 与需约 2 h 适应数据的 wav2vec2-MAML：SEA-MDD-MLP（全块）PER 8.03%、F1 81.54%、DIAA 94.06 等全面更优。适应成本：1 句、延迟约 5–52 ms、参数约 3.0–35.5M，远低于 MAML（94.4M、约 30 min、2 h 数据）。浅层插入效果更好；MLP 略优于 Linear；全块略优于仅第 1 块。

## 结论
单句级 Test-Time Training 可在无额外标注下自适应当前发音样本，兼顾 MDD 精度与实时效率，为 L2 数据稀缺提供新适应范式。

## 点评
把长上下文 TTT 思路迁到 MDD，用“测试时自监督更新局部 MLP”换掉“再采目标人数据”，对课堂实时反馈很贴切。浅层更有效符合底层声学变异更大的直觉。局限是仅 CU-CHLOE 一种 L1 背景；内环学习率与插入层需调；相对 MAML 的评测设置对其更苛刻（MAML 用测试集一部分适应）。


# Mixture-of-Accent-Adapters for Robust ASR: Injecting Accent Cues into Pretrained Whisper

- 论文编号：1373
- 报告人：Mehedi Hasan Bijoy
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/bijoy26_interspeech.pdf

## 问题
带口音语音仍是包容性 ASR 瓶颈；全量微调预训练模型昂贵。既有适配器/多任务方案缺少口音专用适配器、可控编码器级口音线索注入，以及兼顾特化调节与性别信息泄漏抑制的监督设计。

## 方法
Mixture-of-Accent-Adapters（MoAA）作用于冻结 Whisper：池化状态控制瓶颈估计 accentedness；从可学习 soft accent codebook 加权检索注入口音线索并路由轻量口音专家适配器，再与骨干做门控混合。对抗性别头（GRL）抑制泄漏；reference-free hallucination suppression（DHF）抑制罕见解码伪影。默认口音弱时回退冻结骨干。

## 实验与结果
AESRC 上 Whisper-small：MoAA+DHF 达 WER 7.49%、CER 3.81%，约 0.51M 可训参数（约 1% 骨干）。优于全微调（15.50）、LoRA（15.83）与单适配器+DHF（10.25）；相对单适配器+DHF，WER 相对降约 26.9%。消融去掉线性投影或局部解冻编码器/解码器显著变差；GRL 使性别分类准确从约 98.6% 崩至约 29.8%。

## 结论
口音条件化路由 + codebook 注入在冻结 Whisper 上实现按需特化，配合 DHF 达到强口音鲁棒且参数极省。

## 点评
核心是“估计口音强度再决定是否/如何特化”，比一律加适配器更贴分布。DHF 与 MoAA 互补（前者稳解码、后者改编码器状态）。注意与带外置 LM/多阶段流水线的历史 SOTA 不完全可比；口音标签与 accentedness 估计误差会传导到路由。


# Contrastive Regularization for Accent-Robust ASR

- 论文编号：949
- 报告人：Van-Phat Thai
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/thai26_interspeech.pdf

## 问题
SSL 预训练 + CTC 微调在母语语音上强，但对口音变异敏感。口音特定方法需显式口音监督/结构改动；口音不变方法仍缺轻量、与通用 CTC 微调无缝结合的正则。

## 方法
在 CTC 微调时加 utterance 级 Supervised Contrastive（SupCon）辅助损失：对编码器隐状态均值池化后投影，以同一转写为正相关、不同转写为负相关，促进内容紧致、跨口音更稳的几何结构。训练期用、推理不加参；无架构修改、无口音标签。

## 实验与结果
L2-ARCTIC，未见转写（UT）/未见口音（UA）评测。wav2vec2-Large+4-gram：UT WER 10.47→9.14（相对约 −12.7%），UA 9.98→7.41（相对约 −25.8%）。在 W2V2/WavLM base/large、greedy 与 LM 解码上均一致降 WER；对 wav2vec2 增益通常大于 WavLM。within-transcript 余弦离散度均值 0.0518→0.0430（相对约 −17%），t-SNE 显示转写簇更紧。

## 结论
SupCon 是模型无关的轻量正则，能提升多口音 ASR 并收紧同转写跨说话人表示，尤其利于未见口音泛化。

## 点评
用“同一句不同口音应靠近”把口音不变做成对比几何，比口音分类头更少负迁移风险。增益在 UA 最大，符合不变性叙事。依赖基准中重复转写构正样本；无自然重复时需相似度分组或合成变体，外推仍待验证。


# Exploring the potential and limitations of Model Merging for Multi-Domain Adaptation in ASR

- 论文编号：1969
- 报告人：Carlos Carvalho
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/carvalho26_interspeech.pdf

## 问题
语音基础模型常按域分别微调，产生大量专用 checkpoint；新域到来时再做全量联合微调成本高且数据可能不可用。模型合并可免重训拼能力，但 ASR 多域合并系统评测与 OOD/跨语保持仍不足。

## 方法
在 WhisperLv3-X 上对 10 个欧洲葡萄牙语（EP）域独立微调后，基准 11 种合并算法（参数空间 / τ-space / τ-subspace）。提出 BoostedTSV-M：在 TSV-M 上对小奇异值做 boosting 缓解秩塌缩，并用 Newton–Schulz 正交化提升数值稳定。开源 MergeWhisper。评测 EP ID/OOD、非洲/巴西葡语、OpenASR-HF、FLEURS。

## 实验与结果
Full-FT 把 EP ID 从 15.62 降到 8.54，但伤非 EP OOD。BoostedTSV-M EP Full Avg. 11.55，略优于 Full-FT 的 11.58（MAPSSWE p<0.001），EP OOD 优于 Full-FT；相对 TSV-M 更偏 ID、略损部分非 EP OOD。PS 类（如 Karcher、Model Stock）非 EP/多语更好；τSpa（如 TIES）可伤英语。β 越小 ID 越好、EP OOD 越差，体现特化–共享权衡。

## 结论
合并是多域 ASR 相对 Full-FT 的可行替代：BoostedTSV-M 在 EP 上可匹敌甚至略超全微调，并更好保留部分泛化；但存在目标特化与跨语鲁棒的明确权衡。

## 点评
把 NLP/CV 合并族系统迁到 Whisper 多域，并量化“合并不会免费”的 OOD 代价，工程价值高。BoostedTSV-M 针对秩塌缩的修复点明确。局限是单语种族（EP）扩展为主；合并质量依赖各域微调质量与域相似度。


# Activation Steering for Accent Adaptation in Large Audio Language Models

- 论文编号：2166
- 报告人：Ting Dang
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sun26h_interspeech.pdf

## 问题
口音是 ASR 误差主因之一；主流适应靠微调，却不清楚口音信息编码在哪一层、能否在激活空间直接控制。大音频语言模型全参/启发式 PEFT 成本高且可能纠缠语义。

## 方法
把口音视为隐表示中可解释子空间：用文本匹配的标准–口音对，在各编码器层估 mean-shift 方向，注入后测与口音对齐程度，得到层敏感度剖面。推理时在选定层对隐状态加归一化转向向量 α·d̂（前向 hook，不改权重）。在 VCTK（多母语口音）与 L2-ARCTIC（印地/阿语/西语）上，说话人与转写与抽取集严格隔离。

## 实验与结果
敏感度：早期层弱、中层（约 15–19）可控、过晚层不稳；层 31 注入常大幅升 WER。中层转向：母语口音平衡子集上 ΔWER 最高约 30%，非母语约 5%；α 增大峰值更高但深层更易塌缩。相对 PEFT：小样本时转向有竞争力，大数据微调仍更强（正文比较）。八口音一致降 WER。

## 结论
口音信息集中在中层编码器；无参激活转向可在推理期降低多口音 WER，为可解释、可扩展的口音适应提供路径。

## 点评
把 LLM steering 迁到语音编码器，并用层扫 + α 扫给出可操作窗口，解释性与实用性兼具。依赖配对同文标准–口音语料估方向；非母语增益较小、强 α 易塌，部署需按口音校准层与强度。


# AccentDrift: Real-time Streaming Accent Conversion via Sparse Speech Tokenization

- 论文编号：710
- 报告人：Sang-Hoon Lee
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26g_interspeech.pdf

## 问题
实时流式口音转换（AC）对 L2 交互很重要，但现有系统多依赖平行语料、非流式架构、生成质量或口音/音色控制不足。

## 方法
AccentDrift：信息瓶颈视角下用稀疏语义量化（FSQ/iFSQ）从连续语音抽语言信息；口音适配器向稀疏语义 token 注入口音风格，音色适配器（因果 DiT + CAM++，HiFTNet 声码）分层生成说话人声学。全因果：cache-aware FastConformer、有限上下文 Transformer、因果 DiT/声码；并行流，标称约 520 ms（最小约 0.5 s）延迟。无需口音标签与口音配对数据，做零样本 AC（可选零样本音色转换）。

## 实验与结果
LibriTTS/VCTK/GLOBE 训练；L2-ARCTIC 主观、VCTK 印度口音客观。相对 Vevo-Style：流式下 WER 6.27 vs 13.8，SPK-SIM 0.72，口音相似度更高；NMOS/AMOS 可比。密集语义（CosyVoice3）难转口音。消融：NeMo-ASR 中层表征、更窄 IB、lookahead、chunk 大小影响延迟–质量权衡；GRL 抑口音泄漏。

## 结论
稀疏语义 tokenization + 分层风格适配可实现低延迟流式 AC，在保内容与音色下接近或优于非流式并行 AC 基线。

## 点评
把 AC 做成“先压成稀疏语言 token 再分层注口音/音色”，并真正落地因果流式栈，是相对并行 AC 的关键差异。不依赖口音标注利于扩展。仍需继续压解码延迟才更贴全双工；客观评测口音类相对有限，极端口音泄漏与长上下文仍是风险。

