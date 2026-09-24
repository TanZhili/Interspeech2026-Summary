# Language-Model and Codec-Token Speech Enhancement

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：6
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦基于语言模型与神经编解码离散/连续表征的生成式语音增强（SE）：统一多任务、压幻觉、提听感，以及用感知奖励做后训练对齐。相对判别式 SE，生成式在低 SNR、瞬态噪声下更易出现语音样幻觉，成为贯穿摘要的核心瓶颈。

统一与条件化方面，UniSE 用解码器唯一自回归 LM 覆盖恢复、目标说话人提取与分离，并加渐进强化学习；DelayGSE 用延迟多码本建模与文本感知机制抑幻觉。质量路径上，StuPASE 在 PASE 上换干目标与 flow-matching 模块追求棚级听感；Genhancer 系工作用 Hydra（双向 Mamba）替换 DF-Conformer 的 FAVOR+ 以加强全局序列建模。

表征空间选择成为理论–实验交叉点：cNAC-SE 预测连续潜变量、dNAC-SE 预测离散 token，摘要称充分细调的连续方案总体更优，并强调 VQ 正则本身可带来干净先验约束、不必依赖离散 token 路径。后训练则直接用 GSPO 与 DNSMOS/WER/UTMOS 等多度量感知奖励，避免单度量 reward hacking。

## 论文技术总结

# UniSE: A Unified Framework for Decoder-Only Autoregressive LM-Based Speech Enhancement

- 论文编号：192
- 报告人：Chengwei Liu
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yan26_interspeech.pdf

## 问题
神经音频编解码推动了 LM 在语音任务上的应用，但自回归 LM 能否在统一框架内覆盖语音恢复（SR）、目标说话人提取（TSE）与语音分离（SS）仍探索不足；现有 LM-SE 多限于单失真或单任务，且 RL 在 SE 中的感知对齐较少被系统使用。

## 方法
UniSE：冻结 WavLM（层均特征）+ 可训线性 adapter 提供参考/受损连续条件；BiCodec 将目标语音编成固定长全局 token（32）与变长语义 token（50/s）；LLaMA 式 decoder-only LM 自回归预测目标离散 token。用任务 token 区分 SR / TSE / 反向 TSE（rTSE）三种模式，组合模式做两说话人 SS（先 SR 取较响说话人，再 TSE/rTSE）。监督训练后用渐进强化学习（PRL）：DPO 阶段 1 以 DNSMOS 定胜负，阶段 2 再混入 WavLM 特征距离作相似度准则，并保留 CE 项（α=0.4）。训练数据来自 VoxBox 清洁语音与多种噪声/RIR 仿真多失真。

## 实验与结果
DNS 2020：UniSE+PRL 在 With Reverb 上 SIG/BAK/OVRL 达 3.83/4.26/3.64，No Reverb 3.76/4.23/3.57，优于 MaskSR、GenSE、LLaSE-G1 等。URGENT 2025 盲测 OVRL/NISQA/UTMOS 为 3.34/3.83/2.95。Libri2Mix TSE 上 +PRL 的 OVRL 3.45；SS 上 Libri2Mix/WSJ0-2mix OVRL 3.55/3.49。消融：NAR 明显变差；换 Qwen2 骨干相近；X-codec2 因码本过大下降；α 过低会导致 OVRL 虚高而 SIM 崩塌。

## 结论
任务 token + AR 离散建模可把 SR/TSE/SS 统一到同一 decoder-only LM，PRL 进一步抬升感知质量且多任务不伤单任务。局限：全句条件不利于严格流式，解码效率低于 NAR。

## 点评
工作抓住“多任务 SE 的条件前缀可组合性”，用模式切换而非多头网络实现统一，方向清晰。PRL 的粗到细偏好有助于缓解单一奖励与相似度冲突。脆弱点在 BiCodec 重建上限（正文亦用干净语音过编解码说明瓶颈）以及 SS 依赖多轮推理，错误会级联。


# DelayGSE: A Generative Speech Enhancement Framework with Delayed Text-Aware Conditioning

- 论文编号：232
- 报告人：Xin Yuan
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yuan26b_interspeech.pdf

## 问题
基于 LM/扩散的生成式语音增强感知质量强，但在低 SNR 与瞬态噪声下易出现类语音幻觉，语义准确率（WER）常劣于判别式甚至劣于噪声输入。需要在统一框架内同时做去噪、去混响与超分，并抑制幻觉。

## 方法
DelayGSE：16 kHz 噪声语音经 STFT+4 层 Conformer 得声学条件，Whisper-large-v3 编码器得语义条件；AR Transformer（由 Qwen2.5-0.5B 初始化）预测 44.1 kHz DAC 的多码本 RVQ token。两层 delay：(1) MusicGen 式码本级 stride-1 delay；(2) Moshi 式 text-first：先预测文本 token，语音 token 延迟 k=5 步。训练目标为 λtext Ltext + Σ wℓ Lspeech；wℓ 由对 10 万片段逐层保留真值码本测 STOI/Sim/MOS 增量归一得到。可选推理时用真值文本进一步约束。

## 实验与结果
仿真清洁 >3 万小时、噪声约 600 小时。对比 GAN、StoRM、FlowSE、LLaSE-G1 与内部变体。DGSE-IW（重要性加权）在多数据集上 MOS/SIM 最优或近最优且 WER 竞争力强；+T 延迟文本监督相对 WER 降 15.8%；+TG（真值文本）相对降约 33.1%。内部集上 DGSE-IW MOS 4.043、WER 0.099、SIM 0.344；URGENT 英文 WER 可到 0.153（+TG）。随机文本实验表明高失真时才更依赖文本。

## 结论
延迟文本感知与重要性码本加权在抑制幻觉、提升可懂度的同时保持感知质量，并统一增强与超分。未来方向为降延迟与多语扩展。

## 点评
抓住生成 SE 的“语义先于声学”约束，把幻觉问题从后验修补前移到生成顺序与损失权重。强度在消融清楚、码本重要性可复现；脆弱点是依赖 ASR/文本质量与仿真分布，真值文本推理是上界而非部署常态，低延迟场景需再压复杂度。


# StuPASE: Towards Low-Hallucination Studio-Quality Generative Speech Enhancement

- 论文编号：837
- 报告人：Xiaobin Rong
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rong26_interspeech.pdf

## 问题
生成式 SE 易幻觉；PASE 靠语义增强压幻觉，但在强噪声/混响下感知质量有限，且训练目标常保留仿真早反射，可能使目标本身听感混响、谱细节模糊，从而偏置生成分布。

## 方法
StuPASE 在 PASE 上两步改进：(1) dry-target 微调得 PASE-R——先用 DRD 把 DeWavLM 微调到 dry 干净语音的 phonetic 表示（DeWavLM-R），再微调 DualVocoder-R 重建 dry 波形；(2) 用 DiT flow-matching 生成干净 Mel，再经 Mel vocoder（改进 Vocos）合成波形，替代 GAN DualVocoder。条件为 DeWavLM-R 投影后的增强 phonetic 表示与噪声 Mel；训练采用 SenSE 式 speech-infilling（遮罩干净/噪声 Mel 区域，预测速度场 MSE）。工作室质量子集约 1000 小时（UTMOS≥4.0）。

## 实验与结果
DNS1 with-reverb 消融：PASE→PASE-R 的 UTMOS 1.61→3.23、dWER 9.78%→8.01%；StuPASE 达 UTMOS 4.01、dWER 7.89%。去语义或用噪声语义显著抬升 dWER（至 19.79%/36.36%）。DNS1 与 1000 条仿真测试上相对 TF-GridNet、FlowSE、PASE、SenSE、Adobe Enhance Speech V2，StuPASE 在混响与难例上 UTMOS/内容指标领先或并列，with-reverb dWER 最低（7.89%）。主观：Q-MOS 约 4.19（文末截断处给出最佳质量）。

## 结论
dry 目标提升去混响与语义保真；flow-matching 声学模块把质量推到工作室级，同时保留低幻觉。相对 SenSE 框架更简（无额外语义 LM）且内容指标更好。

## 点评
问题定位准：生成 SE 的目标定义与生成容量同等重要。dry-target 与 infilling 共同降低对噪声声学线索的依赖。脆弱点包括依赖 DeWavLM 语义质量、多模块分阶段训练，以及文末主观结果抽取略有截断；SpkSim 在换评测骨干后与原 PASE 论文不可直接比。


# Improving DF-Conformer using Hydra for high-fidelity generative speech enhancement on discrete codec token

- 论文编号：1833
- 报告人：Shogo Seki
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/seki26_interspeech.pdf

## 问题
Genhancer 用 DF-Conformer（FAVOR+ 线性注意力 + 膨胀卷积）在离散 DAC token 上做高保真生成式增强，但 FAVOR+ 近似 softmax 会损伤 focus、特征多样性、单射性与浅层局部建模，限制性能；需要在保持线性复杂度下加强全局序列建模。

## 方法
分析 Genhancer 中 FAVOR+：注意力图模糊、秩远低于 softmax、不同 query 的注意力向量近乎相同。提出 DC-Hydra：在 macaron 式块中用 Hydra（Mamba-2 双向、准可分矩阵 mixer）替换 FAVOR+，保留膨胀深度卷积做局部建模。仍服务 Genhancer：潜在去噪器与 token 生成器估计干净 DAC token，WavLM-large 加权中间层作 SSL 条件，DAC 解码波形。对比 Softmax、FAVOR+、加法 Bi-Mamba 与 Hydra 变体。

## 实验与结果
训练用 LibriTTS-R（升采样至 44.1 kHz）+ 多种噪声/IR，on-the-fly 混响与噪声（SNR [-10,20] dB）等失真；测 DAPS 真实场景录音。Hydra（约 106M）在 NISQA 4.81、SpeechBERTScore 0.89、CAcc 88.95% 等上优于 FAVOR+/Bi-Mamba，部分指标接近甚至超过 Softmax（CAcc 优于 Softmax 的 87.88%）。长序列（96 s）上 Softmax 明显掉点，Hydra 相对稳健；生成式方法 CAcc 均低于 noisy，因幻觉（如多余气息）影响下游。

## 结论
用 Hydra 替代 FAVOR+ 可缓解线性注意力近似缺陷，在保持线性复杂度下提升 Genhancer 的增强质量与下游指标。

## 点评
工作把“线性注意力近似损失”落到注意力秩与 query 混淆的可视化证据上，再用结构化 SSM 替换，属于对症改骨干。强在复杂度与效果兼顾、长输入更稳；弱在仍受生成式幻觉拖累 CAcc，且评测集单一（DAPS），对更广失真分布的泛化需另证。


# Towards Robust Generative Speech Enhancement Using Vector Quantisation-Based Neural Audio Codec

- 论文编号：2564
- 报告人：Haixin Zhao
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhao26i_interspeech.pdf

## 问题
基于 VQ 的神经音频编解码（NAC）语音增强中，连续潜空间预测与离散 token 分类两种策略的信息建模差异仍不清楚；连续建模常不用 VQ，作者假设 VQ 本身可独立于离散分类带来鲁棒性。预训练编解码在干净语音上训练，对失真输入存在失配。

## 方法
以 DAC（K=12、码本 1024、维 1024）为基座，提出：dNAC-SE——对噪声潜表示做残差 VQ 后用 enhancer 预测各码本 logits（IM/JM/HM 三种残差建模）；cNAC-SE——在连续潜空间回归干净表示，再经 VQ 作干净先验正则，并与无 VQ 的判别式变体对比。Enhancer 为 6 层 Transformer，梯形掩码约 1 s 因果上下文。损失：cNAC-SE 用潜空间 L2 + 多分辨率波形损失；dNAC-SE 用加权 CE。编码器/解码器可冻结或微调（soft/hard）。在 DNS3 约 140 小时合成数据上训练，用 DNS-MOS 评估。

## 实验与结果
dNAC-SE 中 JM 最好且算力更低；全微调 cNAC-SE 在 With Reverb / Without / Real 上 OVRL 约 2.91 / 3.37 / 3.19，全面优于各 dNAC-SE，enhancer 仅 2.58 GMAC/s。相对判别式 cNAC-SE，有 VQ 正则在混响未见失真上增益更明显。对标 CDiffuSE、SGMSE、StoRM、SELM 等，cNAC-SE 多数 DNS-MOS 领先。PCA 显示 cNAC-SE 相对干净先验的偏差更紧、更居中。

## 结论
连续潜空间增强 + VQ 干净先验正则优于离散 token 分类；VQ 鲁棒性可与离散建模解耦。全编解码微调有效。局限是完整 codec 管线算力仍可能限制端侧部署。

## 点评
把“VQ 当正则还是当分类目标”拆开验证，理论图示与 PCA 支撑了连续回归在误差几何上更稳。强在机制解释；脆弱点是评测以非参考 DNS-MOS 为主、且依赖干净先验码本，对分布外失真的先验覆盖仍是瓶颈。


# Post-Training Speech Enhancement Language Models with Perceptual Rewards

- 论文编号：3405
- 报告人：Antonis Asonitis
- 程序：Tuesday 29 September 2026 / Language-Model and Codec-Token Speech Enhancement
- 技术分类键：enhancement
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/berdo26_interspeech.pdf

## 问题
自回归 SE 语言模型用离散音频 token 的交叉熵训练，却以 DNSMOS、WER、UTMOS 等感知指标评测，存在 train–eval 鸿沟；单指标优化易 reward hacking。NLP 的 pretrain–SFT–RL 流水线在 AR SE LM 上尚未补齐后训练阶段。

## 方法
对 UniSE 与 GenSE 的公开 SFT 权重施加 Group Sequence Policy Optimization（GSPO）：每输入采样 G=4 条完整序列，用复合奖励 R=DNSMOS+(1−WER)+UTMOS（等权）算组内相对优势，做序列级重要性比裁剪与 KL 约束，无需 critic。训练约 20k 条 5 s DNS 风格配对数据，3000 步。人类偏好消融对比 SFT 基线与单指标/复合 GSPO。

## 实验与结果
DNS2020：两基座各项 DNSMOS 均升；GenSE+GSPO 混响/无混响 OVRL 3.53/3.55，UniSE+GSPO 真实录音 OVRL 3.37，均超 MaskSR、AnyEnhance、LLaSE-G1 等。DNS5 pDNSMOS：GenSE+GSPO Track1/2 的 pOVRL 达 4.45/4.36（相对基座 +1.04/+1.40）；UniSE+GSPO Track1 最佳 4.63。21 人成对偏好：复合奖励 Elo 1571 最高；仅 DNSMOS Elo 1335 低于基线 1476，显示单指标 hacking。

## 结论
GSPO 多指标后训练可直接优化不可微感知目标，补齐 SE LM 的 RL 阶段，并在榜单与听感上优于单指标变体。后训练可作为架构与数据之外的第三条提升轴。

## 点评
把 SE LM 明确接到 LLM 式后训练范式，并用真人消融钉死“复合奖励 vs hacking”，证据扎实。强在无需替代网络与离线偏好对；弱在奖励仍是代理指标组合、采样 G 增加训练成本，且增益幅度依赖基座起点（GenSE 在 DNS5 上提升空间更大）。

