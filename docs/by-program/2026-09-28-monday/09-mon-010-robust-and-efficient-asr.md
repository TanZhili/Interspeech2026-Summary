# Robust and Efficient ASR

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Long Oral
- 论文数：6
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

本场 Long Oral 同时追求 ASR 精度与效率/可控性。解码端 MDM-ASR 用 Masked Diffusion 非自回归框架，配合 Iterative Self-Correction Training 与位置偏置熵界置信采样，缩小 NAR 与 AR 差距并保留并行解码。幻觉治理上，从 Whisper 编码器激活与 Sparse AutoEncoder 潜空间做线性可分检测，并以激活/SAE 转向把非语音幻觉率大幅压低。

数据与标注政策成为另一轴：嵌入多视角（说话人、音素、语义）从十万小时野外数据中为领域专家模型精选约 5% 子集即可相对全量降低 WER；把 verbatim vs intended 转写风格视为可控潜变量，用 decoder task token 与平行文本激活，并改进不流畅语音的词级时间戳。流式 ITN 则把预训练 text-to-text 模型配上 Read-Tag-Write 策略做成端到端流式规范化。测试时适应方面，严格推导自回归熵最小化目标，统一先前启发式。瓶颈包括 NAR 质量缺口、幻觉、异构标注噪声、域数据过载与流式格式化。

## 技术内容

### 扩散 NAR 解码与幻觉转向

**MDM-ASR: Bridging Accuracy and Efficiency in ASR with Diffusion-Based Non-Autoregressive Decoding**（论文 488；Sabato Marco Siniscalchi）
将预训练语音编码器与条件于声学特征及部分掩码转写的 Transformer 扩散解码器耦合，并行预测 token。Iterative Self-Correction Training 暴露模型自身中间预测以缓解训推失配，并提 Position-Biased Entropy-Bounded Confidence-based sampler。多基准上持续优于先前 NAR，并与强 AR 基线竞争力相当且保留并行效率。

**Whisper Hallucination Detection and Mitigation via Hidden Representation Steering and Sparse AutoEncoders**（论文 1989；Georgii Aparin）
研究能否用 Whisper 内部表示检测并抑制对非语音的幻觉转写。原始激活与 SAE 潜空间均线性可分且判别力集中于稀疏特征、随深层增强。提出激活空间与 SAE 潜空间转向：在完整非语音测试集上，small 幻觉率 72.63%→14.11%，large-v3 86.88%→27.33%，语音数据 WER 略降，接近微调类方法。

### 数据选择、转写风格控制与流式 ITN

**Which Data Matter? Embedding-Based Data Selection for Speech Recognition**（论文 3073；Zakaria Aldeneh）
针对领域专家模型难以消化全部异构野外数据，从 100k 小时中按说话人属性、音素内容与语义嵌入挑选相关子集。CTC 模型实验显示策略性选取 5% 子集可相对全量训练最高相对 WER 降低 36.8%。

**Transcription Policy as a Latent Variable: Activating Controllable Verbatim ASR with Word-Level Timing**（论文 2792；Laurin Wagner）
指出 verbatim/intended 风格作为未控潜变量会造成解码不稳、评测混淆（风格失配可占报告 WER 至多 60%）与不可靠词级时间。用覆盖感知 decoder task token 在平行文本上训练；德语不流畅零样本 F1 由 10% 升至 79%（仅英语训练）。并引入 supervised cross-attention 微调改进时间戳，以及 verbatimize 任务以规模化生成规范 verbatim 转写。

**Towards Efficient Simultaneous Inverse Text Normalization with Pretrained Text-to-Text Language Model and Read-Tag-Write Policy**（论文 1060；Kiet Anh Hoang）
流式 ITN 既有混合系统依赖专家 FST，端到端模型又因全局注意力非流式。工作适配预训练 text-to-text 模型，引入架构改造、专门训练策略、Read-Tag-Write 解码与推理优化。越南语实验称精度可比非流式基线、优于混合方法，并满足实时延迟。

### 自回归测试时熵最小化

**Rethinking Entropy Minimization in Test-Time Adaptation for Autoregressive Models**（论文 944；Chee-En Yu）
为生成自回归模型推导严格熵最小化形式，证明精确目标自然分解为 token 级 policy gradient 与 token 级熵损失，并把先前 teacher forcing/伪标签或策略梯度方法解释为该统一目标的部分实现。以 Whisper ASR 为试验台，在 20+ 噪声、口音与多语域上持续改进。

## 本场要点

- Masked Diffusion NAR 正逼近强 AR 精度，同时保留并行解码。
- Whisper 幻觉可在表示空间检测并用 SAE/激活转向抑制，接近微调效果。
- 对专家 ASR，嵌入驱动的少量相关数据可优于不经选择的全量数据。
- 转写风格（verbatim/intended）应被主动控制，否则会污染 WER 与时间戳。
- 流式 ITN 可由预训练文本模型 + Read-Tag-Write 走向可扩展端到端。
- 自回归 TTA 的熵最小化现有统一数学形式，可替代零散启发式。

## 覆盖核对

- 488 | MDM-ASR: Bridging Accuracy and Efficiency in ASR with Diffusion-Based Non-Autoregressive Decoding
- 1989 | Whisper Hallucination Detection and Mitigation via Hidden Representation Steering and Sparse AutoEncoders
- 3073 | Which Data Matter? Embedding-Based Data Selection for Speech Recognition
- 2792 | Transcription Policy as a Latent Variable: Activating Controllable Verbatim ASR with Word-Level Timing
- 1060 | Towards Efficient Simultaneous Inverse Text Normalization with Pretrained Text-to-Text Language Model and Read-Tag-Write Policy
- 944 | Rethinking Entropy Minimization in Test-Time Adaptation for Autoregressive Models
