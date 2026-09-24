# Audio-Visual and Generative Target Speaker Extraction

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
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

本场围绕目标说话人提取（TSE）与视听语音增强：一步均值流生成、视觉仅做选择的插拔式解耦、扩散 AVSE 的对比跨模态对齐、粗到细生成式语言模型 TSE、视位引导的在线轻量视觉分支，以及 LLM 可解释奖励的强化学习 AVSE。

核心张力是：生成式方法提升质量但常需多步采样；深度视听融合可能受野外数据噪声牵制；实时部署又要求因果与轻量视觉前端。场内答案分别是一步生成、冻结音频骨干+潜空间转向、对比对齐增强视觉利用，以及把视觉压缩为视位线索。

## 论文技术总结

# MeanFlow-TSE: One-Step Generative Target Speaker Extraction with Mean Flow

- 论文编号：109
- 报告人：Riki Shimizu
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shimizu26_interspeech.pdf

## 问题
扩散/流匹配生成式 TSE 质量高但需多步采样，低延迟场景难用；AD-FlowTSE 虽可少步，但标准流目标并非为真正一步推理优化。

## 方法
MeanFlow-TSE：沿 AD-FlowTSE 在背景与目标间、由混合比 λ 定义的流路径，改用 mean-flow 目标训练，使从混合物（t=λ）到目标（t=1）可一步生成。在 Libri2Mix 噪声/干净集与多 NFE 设置下对比其他生成式 TSE。

## 实验与结果
干净集 PESQ 3.26、SI-SDR 18.80 dB，超过 AD-FlowTSE；噪声集亦优。NFE 分析显示 MeanFlow 在 NFE=1 时 SI-SDR/PESQ 已接近或优于多步，适合实时。

## 结论
mean-flow 引导的一步生成可在保持分离与感知质量的同时大幅降低推理步数。

## 点评
把“能一步”从启发式少步变成目标函数层面，对助听器/通话延迟约束很关键。仍依赖注册音等辅助线索设定；与强判别式骨干的绝对差距文中以生成式对照为主。


# Plug-and-Steer: Decoupling Separation and Selection in Audio-Visual Target Speaker Extraction

- 论文编号：706
- 报告人：Doyeop Kwak
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kwak26_interspeech.pdf

## 问题
常规 AV-TSE 深度融合音视频并重学分离，但野外 AV 数据噪声大，可能压低相对纯音频分离骨干已达的保真度；视觉更适合解决置换歧义而非再练分离。

## 方法
Plug-and-Steer：冻结预训练音频分离骨干（Conv-TasNet、DPRNN、TF-GridNet、MossFormer2），仅用轻量视觉模块预测 Latent Steering Matrix（C×C 线性变换），在分离块潜特征上把目标说话人锚到指定通道。对比后验选择与残差微调。

## 实验与结果
末块插入 LSM 保真率最高（如 TF-GridNet 99.91%）。LRS2-2mix：LSM 保持接近原 AO 的 DNSMOS/NISQA，而全量残差微调常抬 SI-SDRi 但伤感知分。可训参数约 1.5–2.0M，远小于全微调。

## 结论
分离与选择解耦后，可用极少参数把强 AO 骨干变成 AV-TSE，并保住声学先验与感知质量。

## 点评
“视觉只负责选人”视角清晰，规避 noisy AV 监督拖垮工作室级分离质量。表中 SI-SDRi 有时低于残差微调，但感知指标更稳，取舍合理；依赖骨干本身已解耦说话人通道。


# Audio-visual Contrastive Alignment for Diffusion-based Visual-conditioned Speech Enhancement

- 论文编号：766
- 报告人：Colombe Mboungou
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mboungou26_interspeech.pdf

## 问题
无监督扩散 AVSE（如 AV-UDiffSE+）靠交叉注意力视觉条件，但未显式对齐音视频表征，视觉利用可能不足，低 SNR 与跨域时尤甚。

## 方法
在条件扩散分数模型训练中加入对比音视频损失，强化跨模态对齐；推理仍用原后验采样（NMF 观测模型）不变。在匹配（TCD+DEMAND）与失配（LRS3+NTCD）及多 SNR 上对比 AO/AV DiffUSEEN 与监督 FlowAVSE。

## 实验与结果
匹配集相对 AV-DiffUSEEN：SI-SDR 13.6→16.0、SI-SIR 24.3→29.5；−5 dB 时增益更明显（SI-SDR +3.2、SI-SIR +6.6）。失配集仍有 SI-SIR/SI-SDR 提升。线性投影消融显示对齐头有贡献。监督 FlowAVSE 匹配更强但跨域崩塌。

## 结论
训练期对比对齐可加强视觉条件、改善干扰抑制与低 SNR 稳健性，且不改推理流程。

## 点评
改动集中在先验训练目标，部署友好。增益以干扰抑制为主；极干净高 SNR 时感知收益有限，符合“声学已够好时视觉边际变小”。


# GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-Fine Generative Language Model

- 论文编号：893
- 报告人：Haoyang Li
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26m_interspeech.pdf

## 问题
LM 生成式 TSE 若单阶段直接建模精细声学，熵高、难稳；训练教师强制与推理自回归存在暴露偏差；信号损失也不对齐感知偏好。

## 方法
GenTSE：两阶段纯 decoder-only LM——Stage-1 预测粗语义 token，Stage-2 条件生成细声学 token；两阶段均用连续 SSL/codec 嵌入作条件。Frozen-LM Conditioning（FLC）用早期检查点预测作条件以减暴露偏差；再用 DPO 对齐感知偏好。在 Libri2Mix clean 上评 DNSMOS/UTMOS/NISQA、SECS、dWER 等。

## 实验与结果
GenTSE 在多项感知与说话人一致性指标上超过先前 LM 式 TSE。消融显示 FLC 优于纯教师强制微调；DPO 相对 CE 进一步提升感知分。作者不报 PESQ/SI-SNR，因生成式与波形对齐目标不完全可比。

## 结论
粗到细全生成层次 + FLC + DPO，可提升生成式 TSE 的质量、可懂度与说话人一致性。

## 点评
把语义/声学拆开并正视暴露偏差，是对 AR TSE 的扎实工程。不报经典波形指标削弱与判别式对比；DPO 偏好对如何构造影响可复现性。


# Online Audio-Visual Target Speaker Extraction with Viseme-Guided Lightweight Visual Pretraining

- 论文编号：948
- 报告人：Zixuan Li
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26n_interspeech.pdf

## 问题
多数 AV-TSE 非因果且计算重，难上边缘实时；现有工作多减音频分支，视觉仍常用重 VSR 预训练或联合学 mouth cue，部署成本高。

## 方法
以 viseme（不可分唇形音位组）识别预训练轻量视觉前端；教师（音视频、非因果）蒸馏到因果学生（仅视频、Emformer）。再接因果修改的 TF-SkiMNet 做在线 AV-TSE。对比 mouth+SkiM、viseme+SkiM、VSR+TF-SkiMNet。

## 实验与结果
总 MAC 约 7.7G，低于 VSR 方案（11.3G）。LRS2-Mix：SI-SNR 10.07、PESQ 2.07、ESTOI 0.81，优于各基线。LRS3/Vox2 亦具竞争力。因果学生 VER 28.90%（蒸馏），无蒸馏 33.93%。跨域仍领先多数基线。

## 结论
Viseme 级视觉线索比完整 VSR 更轻、比 VVAD 更细，可支撑强性能的最低算力在线 AV-TSE。

## 点评
把部署瓶颈对准视觉前端而非只砍分离器，方向务实。viseme 标签粗于音素但够做分离条件；因果蒸馏差距仍在，边缘机上还需再压延迟。


# LLM-Guided Reinforcement Learning for Audio-Visual Speech Enhancement

- 论文编号：1816
- 报告人：Chih-Ning Chen
- 程序：Wednesday 30 September 2026 / Audio-Visual and Generative Target Speaker Extraction
- 技术分类键：separation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26s_interspeech.pdf

## 问题
现有 Audio-Visual Speech Enhancement (AVSE) 多用 SI-SNR、MSE 等目标，与主观听感对齐不足，且可解释性弱。数值指标提升不一定对应更少伪影或更自然的增强结果。

## 方法
提出 LR-AVSE：在 AVSEC-4 官方预训练的 encoder–separator–decoder（TCN 融合音视频）上做 RL 微调。将预测 mask 加高斯噪声视为随机策略；用冻结的 SALMONN 生成语音质量自然语言描述，再经 BERT 情感分析得到 1–5 分；以相对奖励 R = r(ŷ_RL) − r(ŷ_base) 配合简化 PPO（无 critic）与 SI-SNR 联合优化。对比基线用 DNSMOS 标量作为奖励。

## 实验与结果
数据为 AVSEC-4（训练 34,524 场景等）。测试集：LR-AVSE PESQ 1.25、STOI 0.58、NISQA 1.29、VQscore 0.62、S-BERT 0.57，优于 Pretrained Baseline（1.20 / 0.48 / 0.99）与 RL-DNSMOS（1.24 / 0.57 / 1.15）。21 人 A/B：对 Baseline 偏好 96.7%，对 RL-DNSMOS 偏好 67.6%。示例中奖励、PESQ、STOI 同向提升。

## 结论
据作者称，这是首个把 LLM 描述性反馈转为 AVSE 奖励的框架；相对监督与 DNSMOS-RL 在客观与主观上均更好，并提供可解释反馈。局限是当前 LLM 描述模式较固定，细粒度差异难刻画。

## 点评
把“语义丰富的自然语言评估”接到 PPO，比直接优化标量 MOS 更贴近听感维度（清晰度、噪声、失真），相对奖励也稳住了预训练策略。脆弱点在奖励链：SALMONN 句式重复 + BERT 映射可能压缩细微质量差；且 Baseline 的 STOI 低于 Noisy，说明 SI-SNR 预训练本身与可懂度目标存在张力，LLM 奖励能否系统性纠正仍需更广场景验证。

