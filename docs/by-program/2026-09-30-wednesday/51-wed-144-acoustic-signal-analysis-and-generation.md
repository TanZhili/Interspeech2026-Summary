# Acoustic Signal Analysis and Generation

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：5
- 论文数：7

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕声学信号的分析、表征与生成展开，覆盖量化部署、语言—音频预训练、乐器音色迁移、语音表征编解码、助听场景音乐增强、指令式时域编辑，以及判别器驱动的扩散生成。共同主线是：在保持任务性能或声学保真的同时，把控制粒度、表征紧凑性与部署效率一并推进。

在表示学习一侧，ProLAP 用概率嵌入刻画音频与文本的多对多层次关系，并配套层次诊断数据；SARA 则用双流 VAE 融合冻结 SSL 语义锚与残差声学编码，缓解纯声学编解码与纯语义 token 之间的内容—保真权衡。二者都在“语义约束 + 声学细节”的张力下寻找更可生成的潜空间。

在可控生成与编辑一侧，AdaTT 针对乐器音色迁移中结构控制与目标音色冲突，做目标自适应的音高/响度控制缩放；EMKR 在 Stable Audio Open 上实现加、删、替、移、延等时域局部编辑，并强调未编辑区保持。另有工作把冻结的噪声条件语音分类器子网络化为扩散骨干，缩短判别与条件生成之间的模型栈。

面向实际听感与部署，BeatGain 按主拍节奏放大打击事件、削弱弱拍外事件，服务人工耳蜗用户的节奏清晰度；ESC 则针对音频激活校准范围过大导致的量化信息损失，用进化策略做激活缩放，支撑 INT8 无损与近无损 INT4。整体上，本场把“听得清、编得准、压得住、控得住”连成一条从分析到生成的闭环。

## 论文技术总结

# Evolution Strategy-Based Calibration for Low-Bit Quantization of Speech Models

- 论文编号：119
- 报告人：Lucas RAKOTOARIVONY
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/rakotoarivony26_interspeech.pdf

## 问题
语音模型激活动态范围极大，Max/Percentile 等标准校准易把多数值压进同一量化档，INT4 激活量化尤其崩溃；现有语音 PTQ 多只重量化或特定结构，缺少通用权重量化+激活整型推理流水线。

## 方法
提出 ESC：先按层用 MSE 最小化 FP32 与量化层输出误差初始化激活尺度，再用 CMA-ES 全局联合优化全部尺度，目标为任务级误差。对称均匀量化（α=−β）。在 Conformer、ECAPA、MP-SENet、FastSpeech 2、AST 上做全 INT8/INT4（权+激活），校准与进化各用 100 条训练样本；并可叠 Adaround、BRECQ、SmoothQuant 等 PTQ。

## 实验与结果
- INT8：ESC 接近或达到全精度（如 Conformer WER 16.01 vs 15.94），整体优于 Max/Percentile/Entropy/MSE。
- INT4：ESC 显著优于基线（如 Conformer WER 38.49 vs MSE 41.22）；AST 相对精度仅降约 1.75%。叠 HyQ 等可进一步改善（ECAPA 等场景相对 ESC 约 +27%）。
- TensorRT INT8 部署平均加速约 2.31×（1.34×–5.07×），显存明显下降。

## 结论
局部 MSE + 全局进化策略校准可在全 INT8 近无损，并在 INT4 配合 PTQ 时接近无损。语音激活量化是关键瓶颈；跨域 PTQ 迁移效果因模型而异，仍需语音专用方法。

## 点评
问题诊断清楚：音频激活“长尾”让视觉/NLP 校准失效。把不可微尺度搜索交给 CMA-ES，工程上务实。INT4 绝对指标仍远逊全精度（ASR WER 翻倍级），“近无损”主要指相对其他校准更好；真正部署价值更在 INT8。


# ProLAP: Probabilistic Language-Audio Pre-Training

- 论文编号：845
- 报告人：Toranosuke Manabe
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/manabe26_interspeech.pdf

## 问题
CLAP 类方法默认音–文一对一确定性嵌入，但真实关系是多对多、有粗细粒度层级；音频源叠加重叠使视觉域层级建模难以直接迁移。

## 方法
ProLAP 将输入建模为对角高斯 \(N(\mu,\sigma^2)\)：PPCL 用校正相似度（CSD）做对比；跨模态/模态内 inclusion loss 编码包含关系；再提出层次化 inclusion loss，用递归随机掩码构造多级更不确定表示。编码器 HTS-AT + GPT-2，自 CLAP 权重微调。发布诊断集 AudioCaps-HC（四级抽象字幕）与 AudioCaps-EC（事件级音文），评测检索、audio traversal、inclusion 测试。

## 实验与结果
- AudioCaps/Clotho 检索与确定性 CLAP 相当或略优（如 AC 上 T→A R@1 42.70）。
- Traversal：加 \(L^h_{\mathrm{inc}}\) 后 Precision 26.83、R@1 15.67，显著高于 InfoNCE/SigLIP CLAP。
- 文本长度–不确定性相关：层次损失使 \(r_{\mathrm{TLU}}\) 达 −0.43；EC inclusion 测试文本/音频约 83.5%/91.7% 满足假设。

## 结论
概率嵌入 + 层次 inclusion 能更好刻画语义层级与不确定性，且不明显牺牲检索。音频侧层次级数过高会略伤检索，文本侧加深更利于不确定性校准。

## 点评
把 ProLIP 思路迁到音频，并用 HC/EC 与 traversal 把“学到层级”变成可测指标，比只报 R@1 更有信息量。字幕由 LLM/事件分割合成，inclusion 是否部分依赖掩码捷径需警惕；作者用 EC 测试试图排除纯 MASK 伪相关，方向对但诊断集质量仍是方法天花板。


# AdaTT: Text-Guided Instrument Timbre Transfer with Target-Adaptive Structural Control

- 论文编号：1828
- 报告人：Dabin Kim
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/kim26o_interspeech.pdf

## 问题
乐器音色迁移需保留谱级内容（旋律/节奏），又要把源乐器特有的表现细节（如小提琴音高主导颤音）改写成目标乐器习惯。标准 ControlNet 刚性复制细粒度控制，易造成音色歧义与不自然。

## 方法
在冻结 Stable Audio Open 上建 SAO-ControlNet，注入量化 \(f_0\)（CREPE）与 RMS 控制。AdaTT 加 CSP（帧级缩放 ControlNet 输出）与 TG-CSP（文本引导、分别缩放 \(f_0\)/RMS 通道）。半自动造数：按音高簇内跨乐器对，网格搜索 \(\alpha,\beta\) 再专家筛选，得 1321 对迁移伪标签（约 4.4h）。两阶段训练：先重构 ControlNet，再冻结其上训 AdaTT。

## 实验与结果
URMP+Solos，13 乐器。AdaTT：CLAP 0.490、F1 MIDI 0.302、KAD 0.495；主观 TIM/NAT/STR/QUL 均优于 ControlNet 与 SmartControl。相对 MusicMagus/ZETA 等推理编辑，结构保持（F1 MIDI）与质量优势明显。控制分辨率过细会抬 Chroma、压 CLAP，折中取 144-bin \(f_0\) + 32-bin RMS。

## 结论
文本自适应缩放异构结构控制，可在保持谱级内容的同时提升目标音色保真与自然度。局限：仅单声部，不保留空间混响等线索。

## 点评
问题切到“表现细节≠谱级内容”，比单纯“保旋律换音色”更细。TG-CSP 在输入端拆开 pitch/loudness 再文本调制，直接针对异构控制纠缠。伪标签依赖 SAO-ControlNet 网格搜索+专家，可扩展性与偏差需注意；单声部设定也限制真实编曲场景。


# SARA: A Dual-Stream VAE for High-Fidelity Speech Generation via Integrating Semantic and Acoustic Representations

- 论文编号：2082
- 报告人：Peijie Chen
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/chen26v_interspeech.pdf

## 问题
零样本 TTS 的语音 tokenizer 在保真与可控间权衡：声学编解码保细节但缺语言约束（易内容错），SSL 语义 token 对齐好但丢音色/韵律。加复杂语义正则往往难平衡。

## 方法
SARA 双流 VAE：冻结 W2v-BERT 2.0 作语义锚 + 残差 CNN–LSTM 声学编码器，50 Hz 对齐后拼接投影为 64 维连续潜变量；HiFi-GAN 式解码器，多尺度 mel + 对抗/特征匹配 + KL。在 LibriTTS+LibriHeavy（>50k 小时，统一 24 kHz）训练。下游以 F5-TTS 用 SARA 潜变量替代 mel 做零样本 TTS。

## 实验与结果
- 重构（LibriSpeech test-clean）：PESQ 4.389、STOI 0.993、UTMOS 4.100，优于 Vanilla VAE / Semantic-VAE / Vocos。
- 下游 F5-TTS-Small+SARA：WER 1.79、SIM 0.63；Base+SARA：WER 1.74、SIM 0.655，内容准确优于 CosyVoice/E2 TTS/原版 F5。
- 消融：去残差编码器 SIM/PESQ 大降；去 SSL 则 WER 变差。NFE=8 时仍可接近 32 步基线质量（RTF 0.079 vs 0.115）。

## 结论
结构上直接融合语义锚与声学残差，无需复杂正则即可在紧凑潜空间兼顾重构与生成；加速推理下仍稳。未来拟多语与自回归扩展。

## 点评
用“冻结 SSL + 学残差”把 Semantic-VAE 的正则思路换成架构约束，简洁且消融干净。50 Hz/64 维瓶颈对 flow matching 友好，解释了低 NFE 仍稳。训练数据与评测同属有声书英语域，跨领域/多语鲁棒性仍待验证。


# BeatGain - A Rhythmic Pattern Enhancement Algorithm for Music Listening with Cochlear Implants

- 论文编号：2713
- 报告人：Benjamin Lentz
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/lentz26_interspeech.pdf

## 问题
人工耳蜗用户音乐感知受限，偏好清晰节拍与低复杂度；现有增强多做干声重混或谱稀疏，未显式按节拍结构处理切分音等弱拍事件。

## 方法
BeatGain：Spleeter 分人声/贝斯/鼓/其他，各再 HPSS；BeatThis! 估四分音符拍点并插值到十六分音符位置，用 Hann 窗按节拍表 \(G\) 生成增益——四分/八分位置增益×2，非网格十六分位置衰减至 0，仅作用于贝斯/鼓/其他的打击分量。对照 V+αP（保人声与打击、压其余谐波，无节拍调制）。在 IKA CI Pop 数据集上算复杂度与 SI-SDR；17 名正常听力受试者经 8 通道噪声激励声码器仿真 CI，2AFC 评整体印象与节奏清晰度。

## 实验与结果
BeatGain 在各 α 下复杂度均低于 V+αP，相对未处理显著简化；α=1 时 SI-SDR 最高，过强增益增加失真。听感：处理条件均显著优于未处理；BeatGain 相对 V+2P 在节奏清晰度上显著更优（约 59.4% 偏好），整体印象优势未达显著。

## 结论
显式强化强拍、衰减弱拍切分可进一步提升节奏清晰度，是干声重混的有益补充。局限：仅 4/4、听测为声码器仿真非真实 CI 用户；未来需扩拍号与真实用户试验。

## 点评
把音乐理论里的强弱拍层级直接做成可听的增益表，问题定位准。客观复杂度与主观节奏清晰度一致支持“拍点结构”贡献；整体偏好未显著超过 V+2P，说明节奏只是多维音乐体验之一。声码器仿真是务实折中，但真实 CI 结论仍需后续验证。


# Edit the Moment, Keep the Rest: Time-Localized Audio Editing via Instruction

- 论文编号：3044
- 报告人：Jinwoo Jung
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/jung26c_interspeech.pdf

## 问题
指令式音频编辑多只能粗粒度改内容，难以在多声事件混叠中指定某一时刻实例（增/删/替/移/延）而不破坏其余区域。

## 方法
EMKR 基于 Stable Audio Open：在线构造（指令、输入、目标）三元组，指令含参考区间 \(R\) 与编辑区间 \(E\)；四标量时间嵌入经 cross-attention 与 timestep 双路径注入。对移动/延长任务引入源事件掩码 SEM（\(R\) 上为 1）与干净潜变量拼接，强制保留源实例声学身份。支持 add/remove/replace/move/extend。自 SAO-Instruct 初始化训 60k step。

## 实验与结果
合成测试 1000 条。区域级：add/replace 的 Target F1seg(0.1s) 超 80%，远高于 AUDIT/AudioEditor/ZETA/SAO-Instruct；move/extend 优势更明显。整段 FAD/FD/KL 与 F1seg 最优。主观（10 人）Faithfulness/Quality/Temporal/Content 全面领先。消融：无 SEM 时 move Target F1 38.3→有 SEM 64.3。

## 结论
显式区间条件 + SEM 可在多声场景做约 100 ms 精度的时域局部编辑并保非编辑区。特别改善移动与延长这类保真关键任务。

## 点评
把“改哪一段”从自然语言歧义提升为结构化 \(R/E\)，再加 SEM 区分同类别多实例，问题抓得准。评测分区 Non-Edit/Source/Target 比整段 FAD 更能暴露“其实没改”的假阳性（如 SAO-Instruct）。训练/测试同为在线混合合成，真实录音泛化仍是下一步。


# Repurposing a Speech Classifier for Guided Diffusion-Based Speech Generation

- 论文编号：3448
- 报告人：Rostislav Makarov
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/makarov26_interspeech.pdf

## 问题
扩散条件生成常用分类器引导，需独立训 score 模型与噪声条件分类器，双模型推理贵。能否把常规训练的语音分类器主干直接复用为生成骨干？

## 方法
在 log-Mel 空间：冻结噪声条件分类器，挂轻量 Score Subnet。取编码器多尺度前向特征 tap，并对 JEM 式边际 \(\log p(X_t)\) 反传得梯度 tap，RMS 归一化后交叉注意力融合，自深到浅上采样解码预测 score；仅训 Subnet（DSM）。条件采样时同一分类器做标准引导。评测 SC09（spoken digits），HiFi-GAN 声码。

## 实验与结果
无条件：Score Subnet（总参 12.3M/可训 4.4M，12.07 GMACs）ScoreQ 3.10、FID 0.17，与全训 U-Net（16.6M，14.56 GMACs）相当或略优，并优于 DiffWave/SaShiMi 等开源基线。条件（γ=3）：质量持平 U-Net+分类器，但总参/计算更低（16.44 vs 22.74 GMACs）。去梯度 tap 更省算力但多数指标变差。低数据/标签子集上，Subnet+引导 FID 优于引导 U-Net。

## 结论
冻结分类器 + 轻量 score 子网可在单骨干上实现条件语音扩散生成，降参降算；梯度 tap 有用。低数据复用分类器表示时优势更明显。

## 点评
把 JEM“分类器暗含能量模型”用到表示级而非端到端训能量模型，避开归一化不稳，策略聪明。SC09 任务偏简单，是否推广到开放词汇/长语句仍未知；但“判别–生成共用骨干”对边缘部署很有吸引力。

