# Speaker Diarization 2

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：4
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场延续说话人日志（diarization）在会议、医患对话与远场多通道场景中的工程化。一条线把日志与 ASR 或角色标签联合：医患角色日志用双 transducer，并区分说话人日志与角色日志对声学/语言线索的依赖差异。

在线与多说话人扩展方面，延迟承诺式说话人跟踪取消显式人数上限，在 VoxConverse / VoxSRC-23 多至约 21–28 说话人时保持 DER 稳定；弱监督多说话人嵌入则去掉外部 VAD/分割依赖，给出窗内帧级多说话人边界。

远场与会议鲁棒性上，神经 FCASA 引入说话人活动的 beta 先验与变分下界，用正则化连续活动分数替代原交叉熵；会议场景则用两级不确定性抑制（语言上下文调制的分割 + 已知说话人种子引导聚类）对抗边界模糊与重叠传播。

端到端自条件（SC）EEND 侧则直面层级排列不一致（HPI）：用 Group-Wise / Continuous Influence PIT 在层次间约束或软正则排列，稳定训练并改善 2/3 说话人 DER。

## 论文技术总结

# ASR-Synchronized Speaker-Role Diarization

- 论文编号：880
- 报告人：Bongjun Kim
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ghosh26d_interspeech.pdf

## 问题
医患等场景更需要 doctor/patient 角色日志而非 speaker-1/2；单换能器串行出词+角色会伤 ASR，而角色日志与说话人日志对声学/语言线索依赖不同。

## 方法
冻结 ASR 换能器，训练同步 RD 换能器：分析显示 RD 更依赖语言；故用任务专用预测器（ASR 用 CNN、RD 用 RNN）、更高层 ASR 编码器特征喂 RD，并以 1-best ASR 强制对齐路径上的交叉熵替代 blank-shared RNNT。评私有 DoPaCo 与公开 SiMeCo。

## 实验与结果
DoPaCo 上相对最佳基线相对降 R-WDER 约 6.2%（P3 达 6.1 vs B2 的 7.8）；SiMeCo 相对约 4.5%（微调后 2.1）。相对初始同步 SD 式设置，更高层特征与 1-best CE 带来更大相对降幅（文中累计可达约 19%/54% 量级于中间对比）。ASR WER 因冻结基本不变（约 15.67）。

## 结论
ASR 同步角色日志可行且不必牺牲识别；相对说话人日志，角色任务应注入更多语言上下文并简化对齐损失。

## 点评
先实证“RD≠SD”再改架构，方法叙事干净。强在保 WER 与双库结果；弱在角色集偏医患双角色，出域 SiMeCo 未微调时仍难。


# Delayed-Commitment Online Speaker Tracking for Robust Many-Speaker Diarization

- 论文编号：898
- 报告人：Youngki Kwon
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kwon26_interspeech.pdf

## 问题
在线说话人日志在多人场景易假注册/坏质心；固定容量模型说话人数封顶，聚类法虽开放但随人数增常劣化，且既有基准偏双人。

## 方法
DC-OST：每条嵌入立刻出标签，但新说话人质心延后至缓冲攒满 K 条再 medoid 提交；距离阈值随已注册人数自适应升高（有上限）抑制虚假注册；配套系统 VAD 与 1.5 s/0.5 s 步长嵌入，延迟 0.5 s。在 VoxConverse、VoxSRC-23（最多约 21/28 人）评 DER，并按说话人数分层。

## 实验与结果
系统 VAD 下 0.5 s 延迟 DER：VoxConverse 9.53%、VoxSRC-23 9.12%，优于 DIART 与 Sortformer；按人数分析显示误差更平稳（Std(∆) 一致性更好），基线随人数上升更易崩。消融称延后提交贡献大于自适应阈值。

## 结论
延迟提交质心 + 自适应阈值可在无人数上限的在线聚类中维持多人稳健性，适合真实会议流式转写。

## 点评
把“立刻出标签”与“晚点建质心”解耦，直接打多人在线痛点。强在多人基准与分层分析；弱在仍依赖嵌入与系统 VAD 质量，重叠话者处理非本文重点。


# Multi-Speaker Embeddings With Weakly Supervised Speaker Activity Detection For Granular Speaker Diarization

- 论文编号：2471
- 报告人：Jenthe Thienpondt
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/thienpondt26_interspeech.pdf

## 问题
级联日志依赖外部 VAD/切分且窗重叠启发式边界粗糙；端到端需帧级标注且场景受限。希望在弱监督下同时出多说话人嵌入与帧级活动。

## 方法
先单说话人预训练带注意力的嵌入器（注意力标量作 VAD logit）；再冻结编码器与 VAD，加 BLSTM SAD 头，用仅话语级说话人标签的置换不变 AAM-Softmax 弱监督训练，使每窗最多两人可得说话人特异嵌入与帧级活动。下游级联日志不再依赖外部 VAD/切分模型。

## 实验与结果
在 AMI、VoxConverse、DIHARD III 上，相对作者先前系统平均相对降低 confusion error rate 13.7%。示例显示弱监督 SAD 可检出基线窗启发式漏掉的说话人活动。

## 结论
弱监督多说话人嵌入可简化流水线并提供更细粒度边界，无需帧级活动金标即可接近混合端到端的粒度优势。

## 点评
用注意力把 VAD/SAD 嵌进嵌入器，弱监督路径实用。强在去外部切分依赖与跨基准相对增益；弱在窗内限两人、极端重叠/多人窗仍需分治。


# Neural Multichannel Distant Speaker Diarization and Source Separation with Beta Speaker Activity Prior

- 论文编号：1248
- 报告人：Sicheng Mao
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/mao26_interspeech.pdf

## 问题
远场说话人日志（distant speaker diarization）受噪声、混响、说话人数变化与重叠语音影响，难度大。数据驱动方法依赖增强与大规模训练；模型驱动方法可利用多通道空间信息。neural FCASA 已对分离部分做贝叶斯建模，但对日志活动仍用非贝叶斯的交叉熵监督，未能把说话倾向先验纳入训练。

## 方法
在 neural FCASA 的多通道混合生成模型上，对说话人活动倾向 η_nt 引入 Beta(α,β) 先验，再由 Bernoulli(η_nt) 生成二值活动掩码 u_nt，与潜在谱特征、PSD 与空间协方差矩阵共同生成 STFT 域混合。推理端用编码器输出 PERT 参数化的 (m,λ)（模式与集中度）得到后验 Beta，替代原先对 η 的 Bernoulli 后验。分离与日志统一用变分推断最大化 ELBO：分离项与原模型相同；日志项含 E[log p(u|η)] 与两个 Beta 的 KL，均可闭式计算（digamma），从而用连续活动分数的正则化 ELBO 替代原始交叉熵。训练目标为加权和 L_sep^(1)+γ1 L_sep^(2)+γ2 L_diar^(1)+γ3 L_diar^(2)。推理时对 η 做 11 帧中值滤波并以 0.5 阈值二值化；分离仍用多通道 Wiener 滤波。

## 实验与结果
在 AMI（约 100 小时、8 麦圆阵、官方 train/dev/eval）上复现与对比 neural FCASA。WPE 去混响；STFT 窗 512、hop 160；N=6（5 说话人+1 噪声）；γ 均取 1.0。在 m∈{0.3,0.5,0.7}、λ∈{4,10} 等设置下，相对 baseline，DER 绝对降约 3%–4%（相对约 16%–30%），JER 绝对降约 4%–6%（相对约 20%–27%）；m=0.3, λ=4 总体最好（如 Forgiving DER 10.11 vs baseline 14.48）。参数仅多约 257，对速度影响可忽略。未评分离客观指标（AMI 无孤立参考）。

## 结论
用 Beta 说话人活动先验把 neural FCASA 的日志部分也纳入全贝叶斯变分训练，日志 ELBO 可闭式求，PERT 便于学超参，显著降低 AMI 上的 DER/JER。未来工作包括先验超参估计、更复杂对话活动模型，以及更好的分离以进一步助推日志。

## 点评
做法抓住的是“活动掩码二值监督过硬、缺少说话倾向/对话氛围先验”这一建模缺口，用共轭 Beta–Bernoulli 把日志损失改成带 KL 正则的连续倾向学习，与分离端 VAE 风格统一。相对常见 EEND 式交叉熵或多通道特征工程，强在先验可解释且几乎不加参。脆弱点在于先验形状被限制为单峰（α,β≥1）、超参需调，且评测按 10 秒块、与全录音 Pyannote 基线不完全可比；分离质量未量化，日志增益是否部分依赖分离仍不清晰。


# Two-Level Uncertainty Suppression for Robust Meeting Diarization

- 论文编号：1956
- 报告人：Shuhei Asaka
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/asaka26_interspeech.pdf

## 问题
真实会议日志中，快速话轮与重叠造成边界模糊，局部活动估计不稳会传至聚类，导致全局说话人分配混乱。现有 EEND/EEND-VC 与声学表征增强未显式处理边界不确定性；且实际会议常为“部分已知说话人”，多数系统只假设全未知或全注册。

## 方法
基于 DiariZen 的 EEND-VC，提出两级不确定性抑制。(1) 分割：用 OWSM-Encoder（E-Branchformer，ASR/翻译监督）的语言学上下文，经上采样后以 FiLM（γ⊙h+β）调制 WavLM 中间层；再对多层级做可学习加权求和，送入 Conformer 做说话人活动估计。注入层对 (k,l) 由层间 Pearson 相关 + Hungarian 匹配选出对齐层，避免盲目搜层。(2) 聚类：Known-Seed Guided Clustering（KSGC）在 AHC 中，将已知说话人注册嵌入按复制因子复制后与估计嵌入联合聚类，通过抬高已知种子在质心中的权重稳定分配；含已知嵌入的簇多数表决标号，其余为未知。

## 实验与结果
数据：AMI、AliMeeting、AISHELL-4；原测试集评分割；改造测试集每人取 20 s 非重叠注册模拟混合已知/未知。对比 WavLM-base+/large、OWSM 替换、输出级融合（Weighted Sum / Concat+MLP / Gating）与 FiLM。FiLM single(5,8) 在未知条件下 AMI DER 14.1、AliMeeting 13.0，相对 WavLM-large 分别降 0.4 与 1.8 点。混合条件下 KSGC 相对标准 AHC 一致提升，AliMeeting 最大约 2.62 点（WavLM-large：19.6→17.6）；复制因子 AMI/AISHELL-4 为 5、AliMeeting 为 150。区域 DER 显示边界/内部区 confusion 下降；已知说话人数增加时 DER 进一步下降。

## 结论
在分割与聚类两端分别抑制局部边界与全局分配不确定性，FiLM 与 KSGC 在多会议语料上稳定降 DER，尤其利于重叠多、话轮快的场景。未来拟把已知说话人信息也引入分割阶段；双编码器带来的算力/显存开销待压缩。

## 点评
问题定义对准 EEND-VC 误差传播链：边界不稳 → embedding 差 → 聚类混乱，并用“语言学调制声学层”与“数据级复制种子约束”分别打两头，比只换骨干或只做输出融合更贴场景。FiLM 相关选层有设计依据；KSGC 几乎不改 AHC，工程友好。脆弱处在于双编码器成本、复制因子需按语料调、混合条件测试集因删段导致 DER 绝对变差需对照解读，且不确定性本身多为观测性指标而非直接方差测量。


# Hierarchical Permutation Consistency Learning for Self-Conditioned End-to-End Speaker Diarization

- 论文编号：1198
- 报告人：Bongsu Jung
- 程序：Wednesday 30 September 2026 / Speaker Diarization 2
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/jung26b_interspeech.pdf

## 问题
Self-conditioned（SC）EEND 把中间层说话人预测反馈到后续层做逐步 refinement，但常规层间独立 PIT（LW-PIT）每层各自选最优置换，造成 Hierarchical Permutation Inconsistency（HPI）：相邻层说话人索引冲突，置换噪声沿 SC 路径传播，破坏训练稳定与渐进精炼。

## 方法
在 EEND-NA + SC 上提出两种 PIT。(1) GW-PIT：把 min 算子移到各层加权 BCE 之和外，令所有中间层共享同一全局置换，从构造上消除层间错配。(2) CI-PIT：用高斯核 w_{l,i}=exp(−(l−i)²/(2σ²)) 聚合各层 pairwise BCE 代价矩阵，再对聚合矩阵做 Hungarian 得 ϕ_l*，软约束邻近层置换连续，同时保留局部灵活性；σ→0 退化为 LW-PIT，σ→∞ 接近 GW-PIT。另定义 PMR、ASR、ESR 诊断层间/跨 epoch 置换一致性。

## 实验与结果
SimConv（LibriSpeech，按 CALLHOME 先验模拟重叠+MUSAN）预训练，CALLHOME 2/3 说话人适配与测试。8 层 Transformer、345 维输入、0.25 s collar、中值滤波 11、阈值 0.5。CALLHOME 2-spk：LW-PIT DER 8.30，GW-PIT 8.02，CI-PIT(σ=1) 7.52（FA 3.65→2.59）；3-spk：CI-PIT 12.52 优于 baseline 13.04，而 GW-PIT 变差至 13.66。训练动态显示 CI-PIT 下 ASR/PMR 收敛近零、ESR 层间协同；σ=1 优于 2/3。消融表明 CI-PIT 与 SC 组合增益最大（8.67→7.52），单加 SC 在 LW-PIT 上几乎无增益。

## 结论
独立层间 PIT 会在 SC-EEND 中引入 HPI；CI-PIT 通过高斯加权代价聚合抑制置换噪声又保留表征灵活度，在 CALLHOME 2/3 说话人上稳定降 DER，硬全局约束 GW-PIT 在说话人增多时易过约束。

## 点评
把 SC 路径上的置换错配形式化为 HPI，并用“硬共享 vs 软邻域聚合”两条线对照，诊断指标（ASR/PMR/ESR）把训练不稳说清楚了，比单纯报 DER 更有解释力。CI-PIT 实质是在一致性与层特异梯度间插值，和分离里的级联/层间协调思路同源。风险在于仅 CALLHOME 小规模评测、SimConv 无 RIR，以及 σ 需调；硬约束在更多说话人时失效，说明一致性目标不能压死中间层自由度。

