# Spoofing and Deepfake Detection 3

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：4
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场反欺骗与深度伪造检测强调对 LLM 时代合成器的泛化、可微自适应增强、编解码器量化层级取证，以及可解释频带注意力。遗留基准与现代 TTS/VC 失配被反复指出；VoxENES 2026、ArFake 等新基准把多语、多方言与后处理条件纳入评测。

训练侧关注多增强梯度冲突（GradHarmony）与可微噪声参数（DAR-Boost）；系统侧有软门控分数融合服务欺骗感知说话人确认（SASV）。应用边界扩展到心音编解码伪造与深度伪造源验证中的说话人因素解耦；生成侧亦出现训练无关的伪造引导推理以提升离散合成真实感。

## 论文技术总结

# DAR-Boost: A Differentiable and Adaptive Raw Data Augmentation Framework for Robust Anti-Spoofing

- 论文编号：643
- 报告人：Yingdong Li
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/li26i_interspeech.pdf

## 问题
音频 deepfake 检测在未见攻击与多样声学环境下泛化困难，声学域偏移往往比攻击算法本身更能拖垮检测器。RawBoost 一类时域增广能高效提升鲁棒性，但参数静态、偏电话语音场景：在环境声等非语音域可能破坏高频纹理，且开环随机采样无法对准检测边界，也难以对复杂噪声组合做可微联合优化。

## 方法
DAR-Boost 把增广建模为可学习对抗干预，与下游检测器端到端联合训练。核心三块：（1）可微 Boost 模块，将 LnL（线性/非线性）、ISD（脉冲）、SSI（平稳噪声）改写为可微算子（FIR 陷波卷积、温度缩放 soft-mask ISD 等），保证梯度可传；（2）Parameter Generator：用轻量卷积编码输入波形，经 Gradient Reversal Layer 预测可学习 Shape 参数（中心频率、带宽、脉冲密度）以最大化任务损失，生成“难例”；Intensity 参数（gain、SNR）仍从均匀分布随机采样，避免塌缩到极端低 SNR；（3）Adaptive Router：拼接原始与三种增广视图，Softmax 预测混合权重做实例级融合。总损失为任务损失减去对混合权重标准差的多样性正则。模块约 26.27K 参数，可挂到 W2V-AASIST、RawNet2、BEATs-AASIST 等 backbone。

## 实验与结果
数据：ASVspoof 2019/2021 LA、CtrSVDD（歌声）、EnvSDD（TTA/ATA 环境声）。指标为 EER，语音任务另报 min t-DCF。
- 语音域：与调好的静态 RawBoost 相当，并优于 Time-Drop/Band-Reject 等 WavAugment 类启发式；例如 21LA 上 Ours EER 0.88%、min t-DCF 0.2088。
- EnvSDD：静态 RawBoost 常损害性能；DAR-Boost 达 TTA EER 4.82%、ATA 0.90%（无增广基线分别为 7.19%、1.42%）。
- 消融：去掉 Generator（TTA 7.63%、ATA 2.05%）或 Router（TTA 5.63%、ATA 2.32%）均明显变差。

## 结论
作者认为可微重构加 Shape/Intensity 解耦与自适应路由，能在保持语音域鲁棒的同时显著改善非语音域泛化，并计划在更新、更多样的数据上继续评估。

## 点评
做法抓的是“增广策略本身不可学习、且偏语音信道先验”这一类问题：用 GRL 把增广参数搜索接到检测损失上，再用随机强度约束物理合理性，比纯启发式 RawBoost 更贴合环境声宽带频谱。脆弱点在于依赖与 backbone 学习率比例、多样性权重 λ_div 的任务相关调参，且 Shape 对抗仍可能在错误信号上破坏关键线索（消融中无 Generator 已低于基线），跨更新攻击分布时仍需验证。


# Quantizer-Aware Hierarchical Neural Codec Modeling for Speech Deepfake Detection

- 论文编号：3212
- 报告人：Jinyang Wu
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/wu26n_interspeech.pdf

## 问题
深度伪造语音常带细粒度、局部的合成伪迹，而 SSL 表征偏语义/上下文，可能冲淡这些线索。神经音频编解码器经 RVQ 形成粗到细的残差层次，伪迹未必均匀分布在各 quantizer；现有检测要么只用连续 encoder 特征，要么把 codec 当普通辅助流，缺少对 quantizer 层级结构的显式建模。

## 方法
在冻结 WavLM-Large（前 12 层 + Attentive Merging）的前提下，引入 EnCodec（Q=8、codebook 1024、维 128）离散码的可训练 embedding，再做层次感知聚合后与 SSL 晚期拼接融合。
- Method 1：Quantizer Mean Pooling，对各 RVQ 层均匀平均。
- Method 2（QAF-Static）：学习全局维度级权重矩阵 W∈R^{Q×D}，经温度 Softmax 得到 α_{q,d}，对每个 embedding 维跨 quantizer 加权求和，形成静态、输入无关的层次先验。
时间对齐后与 SSL 特征拼接再线性投影，送入单层 LSTM + 线性分类器。仅更新约 4.4% 额外参数（相对 SSL backbone）；对比 codec 冻结（codecF）与可微调（codecT）。

## 实验与结果
数据：ASVspoof 2019 LA、ASVspoof 5；主指标 EER。另在 CodecFake 上做跨 codec 族鲁棒性探查。
- ASVspoof5：AttM 基线 6.60%；Mean Pooling (codecF) 6.01%；QAF-Static (codecT) 5.68%（相对改进 13.9%）。
- 19LA：AttM 0.65%；QAF-Static (codecF) 0.44%；QAF-Static (codecT) 0.35%（相对改进 46.2%）。
- 所学 quantizer 权重非均匀，第一层贡献最大；CodecFake 上 Group B（紧凑 RVQ/低比特）相对 AttM-LSTM 更明显，其他 codec 族则大体相当，收益呈族依赖。

## 结论
显式建模 RVQ 残差层次、用轻量静态 quantizer 加权做 SSL–codec 融合，在冻结 SSL 时即可稳定提升检测；作者将动态、样本自适应的 quantizer 加权留作未来工作。

## 点评
核心是把“RVQ 粗到细结构”当作取证先验，而不是再堆一个复杂多视图网络；静态维度级加权可解释、训练稳，且与 AttM 的 SSL 层层次正交。脆弱处在于全局先验可能抹平不同生成机制下伪迹所在层的差异（CodecFake 已显示族依赖），且 codec-only 弱、必须依赖 SSL 上下文；跨训练 codec 分布的泛化仍是开放问题。


# VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion

- 论文编号：2712
- 报告人：Aastha Sharma
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/sharma26b_interspeech.pdf

## 问题
多数 spoofing/deepfake 基准仍依赖 2024 年前合成系统，与 LLM 时代 TTS/VC 及真实传输后处理产生的伪迹分布不匹配，导致在旧数据上很好的检测器在部署时被高估。需要能刻画这种时间漂移与后处理偏移的评测基准。

## 方法
构建双语（英/西）基准 VoxENES 2026：真实语音来自 LibriSpeech（EN）与 VoxPopuli（ES），统一 16 kHz mono、截断/补零至 4 秒；合成侧含 7 种 TTS（如 VoxCPM 1.5、Qwen3-TTS、GLM-TTS、Chroma、VibeVoice、CosyVoice 3、Chatterbox）与 3 种 VC（Seed-VC、OpenVoice v2、RVC v2），共 4,600 条原始合成，再经 10 种后处理（MP3/AAC、白噪/babble、重采样、变速、响度归一等）扩至 46,000 条增强合成，总 53,628 条。在不微调的前提下评测 8 个预训练检测器（AASIST2、RawNet2、多种 Wav2Vec2 变体、AST-ASVspoof5、ECAPA-TDNN 异常打分等），报告 EER/准确率及按合成方法、后处理的分解结果。

## 实验与结果
- 整体最优为 AST-ASVspoof5：EER 28.98%、Acc 75.94%；多数模型接近或差于随机（如 AASIST2 EER 57.86%，存在预测反转）。
- 后处理影响不均：白噪可降低部分模型 EER（如 AST 从 26.7%→17.4%），MP3 则使 AST 升至 48.4%。
- Seed-VC 最难：无一检测器 EER 低于 41%；ECAPA 在部分 TTS 上较好（如 GLM-TTS 10.2%）但在 VC 上大幅退化。

## 结论
作者认为现有反欺骗对策高度依赖脆弱、基准特异伪迹，面对 LLM 时代生成器与常规后处理仍远不够；VoxENES 2026 可作为持续跟踪合成前沿的测试床。

## 点评
工作本质是补齐“时间漂移评测”，用固定预训练、零微调暴露 OOD 落差，比只报旧基准 SOTA 更贴近部署。解读时需注意各检测器训练语料不同，绝对 EER 不宜当严格 head-to-head；后处理偶发“变好”也说明模型可能在换一套捷径线索而非真正学会真伪判别。


# Soft-Gating Score-Level Fusion for Spoofing-Aware Speaker Verification

- 论文编号：2294
- 报告人：Seongkyu Han
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/han26e_interspeech.pdf

## 问题
SASV 需融合 ASV（目标/非目标说话人）与 CM（真实/伪造）子系统。常见静态分数求和或固定加权无法随试次调整二者贡献，且对分数分布偏移敏感；已有分数感知门控（如 embedding 侧乘性门控）又常需额外联合训练，难以直接用在已训好的子系统上。

## 方法
提出无需训练的 Soft Gating Score-Level Fusion：先将 ASV 余弦相似度线性映射到 [0,1]，CM logits 经 softmax 得真实类后验；用开发集 EER 阈值 τ 定义置信度边距 δ=s−τ。三种门控：
- CM Gating：S = s_cm·δ_cm + s_asv·(1−|δ_cm|)
- ASV Gating：S = s_cm·(1−|δ_asv|) + s_asv·δ_asv
- Double Gating：S = s_cm·δ_cm + s_asv·δ_asv  
按试次把更自信子系统的权重加大，直接接到现有 SASV 流水线。

## 实验与结果
数据：ASVspoof 2019 LA、ASVspoof5 Track 2 closed。ASV：ECAPA-TDNN、ReDimNet（VoxCeleb2）；CM：AASIST、Conformer-TCM。指标：SV-EER、SPF-EER、SASV-EER、a-DCF。相对简单求和与 DNN embedding 融合基线，多数配置显著更好；LA19 上 a-DCF 平均约相对降 90%（如 Redim+AASIST Double gating a-DCF 0.0107 vs Baseline1 0.1659）。失效情形集中在 EER 阈值极端靠近 0 或 1 时：CM Gating 在 TCM 阈值近 0 时削弱说话人区分；Double Gating 在阈值近 1 时削弱 CM 对伪造的抑制。

## 结论
训练无关的软门控分数融合在多数 ASV–CM 组合上优于静态/需训练基线，但效果依赖 EER 阈值位置；作者计划改进对极端阈值的门控策略。

## 点评
抓的是“两子系统置信度随试次变化却用固定权重”的工程痛点，用阈值边距做置信度、零参数即可插拔，实用性高。脆弱点很明确：阈值定义置信度，阈值病态时门控会系统性偏置一侧；部署时需按阈值位置选门控变体，而非默认 Double/CM。


# GradHarmony: A Gradient Alignment and Magnitude Normalization Strategy for Audio Deepfake Detection

- 论文编号：2216
- 报告人：Inho Kim
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/kim26r_interspeech.pdf

## 问题
音频 deepfake 检测常用多增广（如 RawBoost、RIR、MUSAN）提升泛化，但同一迭代中干净样本与多种增广样本的梯度可能方向冲突（夹角>90°）或幅度失衡，导致更新相互抵消或被某一增广主导。已有对齐方法多面向单增广或成对对齐，缺少以干净梯度为统一锚点、并同时约束幅度的多增广策略。

## 方法
GradHarmony 两步处理每个 mini-batch 中按干净/各增广类型分别回传的梯度：
1. Clean-referenced Gradient Alignment (CGA)：以干净梯度 g^(C) 为锚；仅当增广梯度与其内积为负时，用 PCGrad 式投影去掉冲突分量（也可换 GradVac），干净梯度本身不变。
2. EMA-based Magnitude Normalization (EMA-MN)：对对齐后梯度的 ℓ2 范数取中位数，再经 EMA 平滑得阈值；曾与干净梯度冲突的增广用更严阈值，其余用 α 倍阈值做裁剪缩放。最终更新为干净梯度加各归一化增广梯度之和。超参固定（β=0.99、α=2、热身 N_w=100），batch 内 50% 干净、50% 均分多增广。

## 实验与结果
在 ASVspoof 2019 LA 上训练；评测 DF21（含 hidden）、ITW、DSD、FoR。模型含 AASIST、RawNet2、RawGATST、SSL-AASIST、SSL-Conformer。相对朴素多增广，GradHarmony 普遍更好且收敛更少 epoch；摘要称两套 SOTA 模型在 OOD 上平均 EER 降约 22%。例：SSL-AASIST 在 ITW 上从增广的 11.60% 到 7.04%；AASIST FoR 从 26.67% 到 21.68%。消融显示 CGA 与 EMA-MN 互补，二者齐全最优；GradVac 作对齐算子仍有效。

## 结论
联合处理方向冲突与幅度失衡可稳定多增广训练并加速收敛；作者将自适应参考方向选择、更丰富增广设定及自适应裁剪强度列为未来工作。

## 点评
把多增广当成“共享标签、不同视图”的优化问题，用干净梯度当主方向比盲目两两 PCGrad 更贴 ADD 设定。脆弱点在于假设干净目标始终是正确锚——若干净分布本身与部署域偏差大，锚定可能固化捷径；固定 α/β 未按模型调参，极端增广强度下幅度裁剪是否仍合适有待验证。


# Towards Detecting Neural Audio Codec Synthesized Heart Sounds

- 论文编号：2116
- 报告人：Orchid Chetia Phukan
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/girish26_interspeech.pdf

## 问题
心音（PCG）被视为难伪造的活体生物特征，但神经音频编解码器（NAC）可合成感知上接近真实的心音，对心音生物识别构成新威胁。尚无针对 NAC 合成心音的检测任务与公开基准。

## 方法
提出 Synthetic Heart Sound Detection (SHAC)，并发布 CARDIOFAKE：基于 CirCor DigiScope（3163 条真实 PCG），经 7 种 NAC（DAC、EnCodec、SoundStream、Speech Tokenizer、FunCodec、AudioDec、SNAC）encode–decode 得到 22141 条合成样本；划分 seen（训练见过的 codec）与 unseen（FunCodec、AudioDec）协议。特征侧评估 MFCC/LFCC 与冻结 SSL（Wav2vec2、Unispeech-SAT、WavLM）平均池化表示，下游用 FCN 或 1D-CNN。融合框架 GROOT：两支特征经 CNN 投影后，用基于 gram 矩阵 Frobenius 距离的 Sinkhorn 最优传输（Gram-OT）互相对齐并与原特征拼接，再经 FCN 二分类。

## 实验与结果
身份保持实验：Real→Fake 用户识别准确率仍达 86.29%（Real→Real 89.11%），说明合成心音高度保留身份。单特征：CNN+WavLM 最强（seen EER 9.45%、unseen 13.39%）。融合：MFCC+WavLM 的 GROOT 达 seen Acc 93.20%/EER 5.86%，unseen Acc 86.10%/EER 9.75%，优于简单拼接与普通 OT，也优于按相同训练设定的 AASIST、MiO 基线。

## 结论
作者认为 NAC 合成心音是可信且危险的身份保持伪造；CARDIOFAKE 与 GROOT（谱特征+SSL 的 Gram-OT 融合）为 SHAC 提供首个基准与强基线。

## 点评
把语音编解码伪造威胁迁移到心音模态，问题定义与数据管线清晰。GROOT 用 gram 空间对齐谱与 SSL，贴合“声学伪迹 vs 时序结构互补”的假设。脆弱处在于合成仅来自 resynthesis 闭环、未见更复杂攻击或信道失真，且 SSL 骨干仍是语音预训练，跨域表征是否最优未充分论证。


# Disentangling Speaker Traits for Deepfake Source Verification via Chebyshev Polynomial and Riemannian Metric Learning

- 论文编号：36
- 报告人：Xi Xuan
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/xuan26_interspeech.pdf

## 问题
深度伪造源验证判断两段合成语音是否来自同一生成器，常默认源嵌入与说话人特质无关；试点显示说话人/源嵌入跨任务仍可互推，说明存在纠缠与捷径学习。需在源验证中显式剥离说话人信息。

## 方法
SDML 双分支：可训练源编码器提 f_src，冻结 ReDimNet-B6 提 f_spk。两套说话人解耦损失：
- ChebySD-AAM：在 ChebyAAM（用 Chebyshev 多项式逼近 cos(arccos(x)+m) 以稳定梯度）上，对非目标 logit 加上阈值化说话人边距 λ·max(0, |f_src·f_spk|−τ)，惩罚源–说话人对齐。
- RiemannSD-AAM：将源/说话人嵌入与原型经指数映射投到 Poincaré 球，用双曲距离做 AAM 式分类，并以 max(0, γ−d_H(f̃_src,f̃_spk)) 抬高非目标 logit，抑制身份泄漏。
前端 80 维 filterbank；源编码器对比 ECAPA-TDNN、ResNet34、AASIST、Mamba；训练用 MUSAN+RIR 增广。

## 实验与结果
数据：MLAAD v8。因无说话人标签，用说话人嵌入余弦阈值≈0.5 构造伪说话人键，形成四协议：Seen/Unseen 源 × Same/Diff 说话人（P-I–P-IV）。指标 EER/AUC（bootstrap）。相对 AAM-Softmax 基线，两种损失在各编码器上均更好；ResNet34+RiemannSD-AAM 平均最优（EER 3.27%、AUC 0.988），未见源同说话人（P-III）EER 4.08%、异说话人（P-IV）7.13%。消融确认说话人解耦项必要；K、λ、曲率 c 在开发集网格搜索。

## 结论
结合多项式逼近与双曲度量的说话人解耦度量学习可减轻源验证对说话人捷径的依赖，并在未见源协议上提升；代码与协议已公开。

## 点评
把“源验证是否在偷用说话人”从假设变成可测协议与可优化损失，贡献扎实。伪说话人键依赖阈值划分，合成语音本身未必有清晰说话人身份，协议噪声可能影响结论；双曲空间与 Chebyshev 边距的增益是否可迁移到更新 TTS 架构仍需验证。


# Interpretable Frequency-Band Attention with Gated SSL Fusion for Audio Deepfake Detection

- 论文编号：2250
- 报告人：Abeer Alhammad
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/alhammad26_interspeech.pdf

## 问题
高准确 SSL/端到端反欺骗模型多把全频带信号当黑箱处理，难以说明伪迹落在哪些频带；已有子带方法多为后验融合或缺少能覆盖“无明显频域伪迹”攻击的互补全局表征。

## 方法
BandMIL 双分支：语音切为重叠 4 s 窗（2 s hop）。频带支路将 0–8 kHz STFT 分成 K=8 重叠子带，各渲染为 64×256 图，共享 ResNet-18 编码并拼接 24 维手工子带特征，经注意力池化得 h_band（α_k 可解释）。SSL 支路用 WavLM-Large（后 12 层微调）得 h_ssl。门控融合 h_fused = g⊙h_band+(1−g)⊙h_ssl。窗级分数经 MIL：训练用 Log-Sum-Exp，推理用 top-k（k=5）均值；目标为音频级与辅助窗级 focal loss。

## 实验与结果
ASVspoof 2019 LA：Full BandMIL EER 1.28%、min t-DCF 0.0331；SSL-only 1.73%/0.0458；Band-only 9.71%/0.1766。仍高于部分公开 SOTA（如 XLS-R-AASIST 0.22% EER），但提供频带可解释性。按攻击：Band-only 在 A07/A09/A14–A16 近零 EER，在 VC 类 A17/A18 失败（41.12%/22.89%），SSL 与门控可补；部分攻击（A10/A11/A15）融合反而不如单支路。注意力上 B8（最高频）常占主导，A09 等偏向中高频。

## 结论
频带注意力 + 门控 SSL 融合可在保持竞争力的同时给出频域决策依据；作者承认全局门控并非对所有攻击都最优，计划做攻击感知门控并扩展到更新基准。

## 点评
把可解释子带分析接到现代 SSL，并用门控承认“有的攻击根本不在频带上”，设计动机清楚。主表相对顶尖 SSL 系统仍有差距，价值更多在审计/定位而非刷榜；融合在部分攻击上双输，说明单一全局门控仍脆弱。


# ArFake: A Robust Framework for Multi-Dialect Arabic Speech Spoofing Detection Benchmark

- 论文编号：2665
- 报告人：Mohamed Elsetohy
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/elsetohy26_interspeech.pdf

## 问题
英语等资源丰富语言已有 ASVspoof 等反欺骗基准，阿拉伯语尤其是方言覆盖不足；低资源、形态复杂与非标准正字法使合成与检测都更难，方言社区面临合成语音滥用风险却缺乏系统评测资源。

## 方法
ARFAKE 五阶段流水线：（1）基于 Casablanca 八方言语料，用 XTTS-v2、FishSpeech、ArTST、VITS 生成伪造语音；（2）用分类器可分性、Whisper-Large WER、12 名母语者 MOS 评估可懂度/真实感；（3）混合真实与 FishSpeech/XTTS/ArTST 伪造构建约 54k 条语料（VITS 留作未见生成器），训练/测集约 31k/23k；（4）在 HuBERT、Whisper、wav2vec2 嵌入上接两层前馈分类头，并设 MFCC-SVM 等传统基线；（5）In-domain、Leave-One-Generator-Out（LOGO，留出 VITS）、Leave-One-Dialect-Out（LODO）协议评测鲁棒性。

## 实验与结果
单生成器上 FishSpeech 最难（Whisper-large EER 6.92%），ArTST/VITS 近乎完美可分；MOS 与难度一致（FishSpeech 均值 3.72，VITS 1.70）。组合测试集 Whisper-large EER 4.88%、ACC 96.86%；未见 VITS 上 Whisper-small ACC 98.30%。LODO：摩洛哥方言最高约 93.51%，巴勒斯坦最低约 88.45%。摘要称域内与 LOGO 分别约 96%/97%。

## 结论
作者认为 ARFAKE 是首个面向多方言阿拉伯语伪造语音生成与检测的端到端基准，为跨生成器/方言鲁棒评测提供可复现路径。

## 点评
贡献主要在资源与协议：把方言偏移、生成器偏移纳入同一流水线，并用 MOS/WER 解释“近完美 EER”可能只是低质量伪迹。检测侧偏嵌入+浅分类头，未见更强图网络反欺骗骨干；近完美可分的生成器会抬高表观鲁棒性，解读 LOGO/LODO 数字时需对照各 TTS 真实感。


# MSpoofTTS: Multi-Resolution Spoof-Guided Inference for Discrete Speech Synthesis

- 论文编号：2159
- 报告人：Junchuan Zhao
- 程序：Thursday 1 October 2026 / Spoofing and Deepfake Detection 3
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/zhao26g_interspeech.pdf

## 问题
神经 codec 语言模型做离散语音合成时，自回归解码易积累 token 级不一致与分布漂移，产生听感伪迹；偏好优化/重训成本高，而常规解码约束多只针对重复等局部失败，缺少对 codec 序列真实性的显式评估与引导。

## 方法
MSpoofTTS 在固定 NeuTTS 参数下做训练无关推理：先训多分辨率离散 token 伪造检测器——对 codec 序列做长度 L∈{10,25,50} 裁剪及 skip-sampling（r∈{1,2,5}），各用独立 Conformer+分类头区分真实/合成 token 段；再提出 Entropy-Aware Sampling（EAS，逆秩加权+时间衰减记忆缓冲）与分层伪造引导采样：warmup 后对多候选逐步用 M10→M25 剪枝，最后用 M50 及其采样变体加权重排选续写。不改动基座 AR 模型。

## 实验与结果
检测器在 LibriTTS 上用真实与 NeuCodec 合成配对训练；合成评测在 LibriSpeech/LibriTTS 与舌头绕口令 TwistList。HierEAS（MSpoofTTS）在多数客观指标上最优或次优：如 LibriSpeech WER 0.0532、NISQA 4.602、MOSNET 4.4158（Original 分别为 0.0694/4.462/4.3418）。TwistList 上感知质量最好而 WER 未必最低。主观 MOS-N/MOS-Q 显示分层伪造引导优于非分层对照，说话人相似度保持良好。

## 结论
多分辨率 token 伪造分数用于剪枝与重排，可在不重训 codec LM 的前提下提升感知质量与解码鲁棒性。

## 点评
把反欺骗从“事后分类”接到“解码时约束”，且工作在离散 token 而非波形上，思路新颖实用。收益主要在 NISQA/MOS 等感知侧，WER/SIM 提升有限；检测器与 tokenizer/TTS 绑定，换 codec 或生成器时需重训引导器，分层 beam 也会增加推理开销。

