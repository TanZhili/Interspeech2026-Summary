# Neural Speech Enhancement: Survey, Diffusion and Flow Matching

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral
- Area：6
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场以综述串联单通道神经语音增强史，再聚焦离散扩散、Schrödinger Bridge 与“漂移”生成等少步/单步推理方案。主线是：增强从映射/掩蔽与时域回归，转向分布采样式生成，并借预训练表征与桥接轨迹压低迭代成本。

综述勾勒浅层网络→时频映射/掩蔽→时域建模→生成式→speech foundation model 重用，并反思评测、鲁棒性与“干净语音”定义。实证研究则分别在 codec 码空间做吸收离散扩散；用 SB+Mamba 单步联合去噪去混响；把去噪写成均衡问题的 DriftSE；以及可学习 SB 的单次扩散 EffDiffSE+。

共同瓶颈是多步扩散的推理复杂度；共同策略是单步/少步轨迹匹配、桥接初始化与架构协同（Mamba 相对 MHSA/LSTM 在 SB 下更强）。评测上既有非侵入客观指标，也有 PESQ/POLQA/NISQA 等综合榜。

## 论文技术总结

# Monaural Speech Enhancement: From Shallow Networks to Speech Foundation Models

- 论文编号：
- 报告人：Sabato Marco Siniscalchi
- 程序：Monday 28 September 2026 / Neural Speech Enhancement: Survey, Diffusion and Flow Matching
- 技术分类键：enhancement
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
单通道（monaural）神经语音增强如何从早期浅层学习走到当今语音基础模型时代，以及这一演进对评估、鲁棒性乃至「干净语音」定义意味着什么。

## 方法
报告按时间线综述：先回顾深度学习之前的早期尝试；再进入时频域映射与掩蔽类公式，说明全连接前馈网络相对经典统计估计器的优势及其结构演进；接着讨论绕开显式频谱表示的时域建模；再转向把增强重述为分布式、基于采样的干净语音生成（相对确定性回归/分类）的生成式框架；最后讨论用大规模预训练语音模型改用于增强的前沿做法。

## 实验与结果
摘要未列出具体数据集、基线或定量指标。

## 结论
语音增强正从浅层/判别式映射走向生成式与基础模型复用；随之需要重新审视评估方式、鲁棒性，以及对「干净语音」本身的理解。

## 点评
线索清晰：表示域（时频→时域）与目标形式（回归/分类→生成→基础模型）两条主轴。无 PDF，只能跟摘要脉络，不能还原具体网络或损失设计。


# Absorbing Discrete Diffusion for Speech Enhancement

- 论文编号：659
- 报告人：Philippe Gonzalez
- 程序：Monday 28 September 2026 / Neural Speech Enhancement: Survey, Diffusion and Flow Matching
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalez26_interspeech.pdf

## 问题
连续域扩散语音增强计算重；神经音频编解码（NAC）离散码虽利于 Transformer 建模，但多数下游增强仍靠自回归下一码预测、推理慢。需要在 NAC 码空间做有理论依据的非自回归生成式增强。

## 方法
ADDSE：冻结自训 RVQ 编解码器（约 2 kbps、4 码本×1024、50 Hz）将干净/带噪波形编成码；用吸收态离散扩散（ADD）建模干净码在带噪码条件下的分布，训练目标为条件 denoising cross-entropy。架构 RQDiT：沿帧与码本深度各一条 DiT，复用 NAC codebook 向量作输入（mask 为 0），以 adaLN 条件化带噪码。推理从全 mask 按 τ-leap/Euler 等价转移采样，可复用未解吸收步的网络预测以降 NFE。

## 实验与结果
训练动态混合多语料干净语音与噪声（SNR −5–15 dB）；测试 Libri-TUT 与 Clarity-FSD50K（跨噪声/跨语音泛化）。对比 Conv-TasNet、BSRNN、SGMSE+、EDM-SE、NAC-SE、EDM-NAC-SE 等。NAC 系侵入式 PESQ/ESTOI/SDR 弱（相位未重建），但非侵入指标有竞争力：含 4M 的 ADDSE-XS 在两集 DNSMOS/NISQA 上可超 Conv-TasNet 与 SGMSE+；ADDSE-XL 在 Clarity-FSD50K 上 DNSMOS 最好。NISQA 约 8 步、其余非侵入约 16 步即平台；低 SNR 优势更明显；大 Nsteps 时平均 NFE 可显著低于步数。

## 结论
作者认为在 NAC 码上做 ADD + RQDiT 能以较少采样步达到有竞争力的感知类指标，尤其低 SNR；离散吸收过程还可因预测复用提高采样效率。未来拟扩展全频带并引入语义编码。

## 点评
把“码空间语言建模”从自回归换成有吸收扩散理论的并行采样，并用 RQDiT 显式利用 RVQ 层级，是相对 MaskGIT 式 SE 更干净的一条线。代价是强依赖编解码重建上限，侵入式波形指标天然吃亏；相对 BSRNN/EDM-SE 仍非全面领先，价值更在低 SNR 感知与少步推理的折中。


# Schrödinger Bridge Mamba for One-Step Speech Enhancement

- 论文编号：682
- 报告人：Jing Yang
- 程序：Monday 28 September 2026 / Neural Speech Enhancement: Survey, Diffusion and Flow Matching
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/yang26e_interspeech.pdf

## 问题
Schrödinger Bridge（SB）语音增强可缓解扩散的 mean prior mismatch，但常用 NCSN++ 骨干往往需多步求解、实时性差；而 Mamba 虽已用于 SE，多停留在确定性映射/掩码，未与 SB 轨迹监督结合。作者强调训练范式与骨干归纳偏置应对齐。

## 方法
SBM：在退化分布与干净分布之间用 VE 调度构造 OT 中间态 x_t = μ_x(t)+σ_x(t)z，以 STFT 上的 x_t 与时间嵌入训练 Mamba 骨干做 data prediction（幅度/复数 MSE 与多分辨率项）。骨干基于 oSpatialNet-Mamba，加时间条件与全频带 Mamba 层，小 look-ahead（约 2–4 帧、<40 ms 算法时延）。推理固定 t=1（退化先验）单步直出干净谱。

## 实验与结果
训练约 800 h 干净语音 + 噪声 + RIR，SNR ∈[−10,20]，联合去噪去混响。评测 DNS（含/无混响、真实录音）与 VoiceBank-Demand。约 3.93M 参数、RTF≈0.0048。DNS With Reverb / Real Recordings 上多项 DNSMOS、NISQA、语义/说话人相似度等领先；无混响与 VBD 上与 ZipEnhancer 互有胜负。优于同骨干映射基线、FM-Mamba、一/多步 SB-NCSN++、SBCTM、SB-UFOGen。消融：SB 相对 mapping 在 MHSA/LSTM/Mamba 上均提升，且 Mamba+SB 最强。

## 结论
作者认为 SB 轨迹监督与 Mamba 状态演化归纳偏置协同，可在单步推理下取得高质量联合去噪去混响，并具备竞争 RTF；强调范式–骨干对齐对连续时间序列建模的启示。

## 点评
卖点不在发明新扩散公式，而在论证“中间态轨迹 + 选择性 SSM”比“同骨干硬映射”或“同 SB 换 NCSN++”更匹配。一、挑战场景（混响/真实录音）优势更清晰；对齐敏感指标上相对强判别模型未必全面占优，作者也提到双讲训练策略会影响部分语义分。流式 look-ahead 与边缘部署潜力写在设计里，正文未给大规模端侧实测。


# Speech Enhancement Based on Drifting Models

- 论文编号：833
- 报告人：Liang Xu
- 程序：Monday 28 September 2026 / Neural Speech Enhancement: Survey, Diffusion and Flow Matching
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/xu26d_interspeech.pdf

## 问题
扩散/流匹配类增强推理常需多步离散化，低 NFE 难逼近弯曲轨迹；一致性蒸馏等一方法仍根植于轨迹压缩。需要一种原生单步、且可按分布匹配而非成对回归学习的生成式增强框架。

## 方法
DriftSE 将增强写成 pushforward 分布的平衡问题：映射 f_θ 一次输出增强样本，在冻结 SSL（HuBERT/WavLM/DistilHuBERT）多层潜空间用 mean-shift 式 Drifting Field（吸引干净帧、排斥当前生成帧）作 stop-grad 回归目标，使生成分布逼近干净分布。两种设定：直接映射 ˆx=f_θ(y+σϵ)；条件生成 ˆx=f_θ(ϵ,y)。骨干为无时间嵌入的 NCSN++V2；推理直接映射取 σ=0。因监督是 batch 内潜空间相似度，天然支持 unpaired 训练。

## 实验与结果
VoiceBank-DEMAND：DistilHuBERT、σ=0 达 PESQ 3.15、SI-SDR 16.1 dB，超 30 步 SGMSE+ 与一法 MeanFlowSE；加辅助 PESQ/SI-SDR 损失的 DriftSE† 更具竞争力。条件变体 SCOREQ 达 4.33、DNSMOS 3.64。DNS 2020 盲测：DistilHuBERT 变体 WV-MOS 2.65、SCOREQ 2.97 等领先或很强。Unpaired 跨数据集/跨性别仍有可用非侵入分（成对保真下降符合预期）。可视化显示潜空间分布由噪声向干净收敛。

## 结论
作者认为潜空间漂移场可在 1 NFE 对齐干净语音分布，达到有竞争力的感知与泛化，并支持完全 unpaired 设定，为原生单步生成式 SE 提供新范式。

## 点评
相对“压轨迹步数”，这里用分布平衡 + SSL 语义距离做生成监督，解释了为何能 unpaired。直接映射与条件生成在保真/感知上可切换，实用。依赖外部 SSL 层选择与温度核；† 变体加了成对指标损失后才逼近部分蒸馏基线，说明纯漂移未必在 PESQ 上压过强辅助损失系统。跨性别 unpaired 会改说话人属性，边界也写清楚了。


# Learnable Schrödinger Bridge and Activations for Efficient Diffusion-based Speech Enhancement

- 论文编号：2465
- 报告人：Yihui Fu
- 程序：Monday 28 September 2026 / Neural Speech Enhancement: Survey, Diffusion and Flow Matching
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/fu26b_interspeech.pdf

## 问题
扩散/SB 语音增强效果好但反向过程多步、算力高；混合判别–生成可减步，但经典 SB 训练用干净语音构造边际、推理却从噪声出发，训练–推理初态不匹配，单步推理仍有空间。

## 方法
EffDiffSE+：条件 DNN 预增强 + bridge DNN 做单步 SB。提出可学习 SB：(1) 用条件 DNN 输出 ˆX_cond 替代干净语音构造条件边际，推理以复高斯 XT′=wXˆXcond+wYY+σZ（最优 T′≈0.3）作单步初态，使训练/推理匹配；(2) 两层辅助网络自适应预测 wX、wY、σ 取代固定解析式；(3) 拓扑升级：sub-pixel 上采样、Snake/SnakeBeta、条件–bridge 交互模块、子带 Conv/DeConv。损失含心理声学条件损失与波形 L1 辅助项。

## 实验与结果
URGENT 2024 数据（排除部分 CommonVoice），约 634.5 h 训练。同数据重训多基线。EffDiffSE+ 约 9.40M、3.84 GMAC/s（对比中最低），PESQ 2.58、POLQA 3.55、NISQA 4.07、ESTOI/LPS 0.84、主观 MOS 3.95（近干净 3.96），总体 rank 1.27，优于 EffDiffSE（rank 3.09）及 SGMSE+、SB、Universe++ 等。消融显示辅助网络与各拓扑逐步抬升。

## 结论
作者认为可学习 SB 初态与激活/拓扑改进能在单步、低复杂度下达到跨侵入/非侵入与主观指标的领先表现。

## 点评
关键是把“单步可行”建立在训练–推理初态对齐上，辅助网络把固定 bridge 权重变成数据自适应，再叠加工程向拓扑。对比公平性较好（同数据同步数预算）。相对多步大模型在 DNSMOS 等单项未必处处第一，但综合 rank 与 MOS 优势明确；仍依赖预增强条件分支质量。

