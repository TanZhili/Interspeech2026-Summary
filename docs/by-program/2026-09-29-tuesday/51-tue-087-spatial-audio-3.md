# Spatial Audio 3

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：5
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场集中于双耳合成、个性化 HRTF、分布式声学场景理解与车载个人声区。单声道/文本到双耳生成强调几何或空间提示条件化、时频域耳间关系建模，以及粗估计后再生成精炼的两阶段流程。HRTF 个性化从网格离散预测走向连续算子学习与物理可微渲染，并用双耳声学信息辅助稀疏测量重建。

理解侧把多房间遮挡下的分布式麦克风图网络与 LLM 叙事结合，并把空间音频语言对齐推进到多事件时空细粒度对比学习。应用侧引入心理声学加权的车载 MU-MIMO 预编码，以及矢状面定位中生态声源先验与空间先验的贝叶斯评估。整体上，可控空间提示、物理约束与感知加权成为共同关键词。

## 论文技术总结

# AURA: Audio-Geometry Conditioned U-Net Refinement with Flow Matching for High-Fidelity Monaural-to-Binaural Synthesis

- 论文编号：87
- 报告人：Wenjie Zhang
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26_interspeech.pdf

## 问题
从单声道合成双耳声需在保持音色细节的同时推断空间线索，传统 HRTF 管线难适应动态相对位姿与真实环境；现有深度学习方法仍难达到与真实录音难以区分的保真度。作者聚焦仅单声道+几何条件的设定。

## 方法
两阶段框架 AURA：(1) 经 Time Dynamic Warping 后，用 Transformer–CNN 下采样块（TCDB）与空间增强残差上采样块（SERUB）生成粗糙双耳估计，并以 Spatial-Awareness and Motion Attention（SAMA）融合位姿（位置+四元数朝向）；(2) 条件流匹配（CFM）以粗糙估计加噪为先验、真值为目标，在 OT 线性路径上学习速度场并 ODE 积分细化。总损失含波形 L2、相位/幅度 STFT 损失与 LCFM。

## 实验与结果
数据为 [11] 的 KEMAR 室外约 2 小时 48 kHz 配对单/双耳录音。客观：Wave-L2 0.123、Amp-L2 0.028，优于 BinauralGrad（0.128/0.030）等；Phase-L2 0.843。主观（15 听者）：MOS 3.82、Spatial MOS 3.89、Similarity MOS 4.21，均高于对比方法。消融去掉 TDW、Trans/CNN 分支、SAMA 或 CFM 均使 Wave-L2 变差，无 CFM 时升至 0.183。

## 结论
作者认为混合 U-Net 粗估计 + 流匹配细化、配合音频–位姿交互，可提升单声道到双耳的自然度与保真度；后续将探索更真实场景下的双耳合成。

## 点评
把流匹配用作“粗预测残差细化”而非端到端生成，较贴合单声道缺空间信息的结构。客观与主观一致优于扩散类两阶段基线，且参数/MACs 相对可控。弱点是评测依赖单一公开数据集与固定分裂，Phase-L2 并非最优，空间 MOS 跨模型差距也相对有限。


# GISNO: Neural Operator-based HRTF Personalization from 3D Meshes via Differentiable Helmholtz Rendering

- 论文编号：366
- 报告人：Liming Shi
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/huang26b_interspeech.pdf

## 问题
个性化 HRTF 测量成本高；数据驱动方法常绑死离散方向网格，且把不规则 3D 网格重采样到规则网格会抹掉耳廓细结构。需要能从 3D 头模直接到连续声场、并支持任意方向/距离/频率查询的方法。

## 方法
GISNO 将 HRTF 预测写成边界复压强场上的算子学习：GNO 编码器把网格几何特征（面积元、法向、源相对位置等）投影到球面潜网格（耳间坐标系+表面锚点邻域），SFNO 块做球谐域全局散射映射，解码回网格边界压强；再经可微 Helmholtz 积分渲染到任意场点得到 HRTF。训练最小化场点复压强 NMSE；利用声学互易，每受试者双耳各一次前向即可渲染多方向。

## 实验与结果
HUTUBS：40 训练 / 15 测试；法向高斯扰动增广至 160 网格。相对 DNN-PCA/VAE/SHT/CAE 等人体测量基线，LSD 均值 2.92 dB（对比约 4.29–5.27 dB）。零样本测试：训练在 1.2 m、1550 点、Δf=150 Hz 的 Mesh2HRTF 仿真，测试 1.5 m、7800 点、Δf=100 Hz；1 kHz 球面上归一化幅度误差均值 0.0139。

## 结论
作者认为神经算子 + Helmholtz 渲染可在保留网格形态细节的同时实现物理一致、可任意分辨率查询的 HRTF 个性化，并展现空间超分、径向外推与频谱细化的零样本能力。局限是 HUTUBS 规模小、零样本主要在仿真数据上验证。

## 点评
把“学边界算子、积分求场”写进端到端训练，比直接回归离散 HRTF 网格更有物理归纳偏置，也自然解释多维零样本。与人体测量基线的 LSD 优势明显，但未与近期 mesh 方法同协议对比；刚性声硬边界假设与仿真零样本仍可能高估真实测量场景的泛化。


# TTBA: Spatial Prompted Text to Binaural Audio Generation Using Transformer

- 论文编号：602
- 报告人：Changjun He
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/he26_interspeech.pdf

## 问题
现有 text-to-audio 多生成单声道，即使有立体声也缺乏可控空间信息；近期可控双耳/空间生成仍易出现空间漂移与定位误差。作者希望从文本与显式空间提示直接生成方向可控的双耳音频。

## 方法
TTBA：用预训练单声道 EnCodec 对左右声道编码后做 codebook 维交叉排列；空间提示编码器将各声源的起止方向（五扇区量化）与速度编成嵌入，经多头注意力与 T5-large 文本特征融合；解码器式 Transformer ALM 自回归生成双耳离散 token。训练上从更深的单声道教师蒸馏内容，并用 CE + KD 损失与 CFG。推理时拆开交叉 token 再解码波形。

## 实验与结果
在 BEWO-1M 的 SS/SD/DS/Mix 子集上对比 Stable-audio-open 与 SpatialSonic。多源场景（DS、Mix）上 FD/FAD/CLAP 等多数指标最优；DILD 常优于 SpatialSonic。主观（20 人）OVL/REL/SPQ 多数最高。消融：无蒸馏损害内容指标；无 SPE 主要恶化空间指标（尤其 DILD）。

## 结论
交叉排列离散表征 + 空间提示条件 + 单声道教师引导，可在复杂多源条件下生成语义与空间均较可控的双耳音频；未来拟提升空间真实感并扩展到更复杂环境。

## 点评
把“内容”与“耳间差异”拆成教师蒸馏与交叉 token，对文本驱动双耳生成是合理归纳。方向被粗量化到五扇区，精细轨迹与距离控制仍有限；定量上单静/单动态子集并非全面领先，主观优势与客观不完全一致，说明空间评价仍依赖听感。


# Spec2Spatial: A Time-Frequency Spatial Attention Network for Binaural Audio Synthesis

- 论文编号：607
- 报告人：Changjun He
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/he26b_interspeech.pdf

## 问题
深度学习单声道到双耳合成仍难忠实再现 ITD/ILD 等耳间线索，与真实录音存在明显差距。作者希望在时频域显式建模耳间关系并注入声源位姿条件。

## 方法
Spec2Spatial：先用 Time-Domain Warping（TDW）按几何延迟粗造左右通道，再 STFT；编码器堆叠 Interaural Spatial Attention Network（ISAN，含能量分析模块 EAM 的时–频门控）与 Conv2D；解码器用 Condition Fusion Residual Network（CFRN，FiLM 注入 7 维位姿）与上采样，预测复数掩码后乘到 warped 谱并 iSTFT。损失为波形 L2、相位损失与多分辨率 STFT 损失。

## 实验与结果
Binaural Speech（约 2 小时 KEMAR 配对录音）上：DILD 1.250、DITD 0.034、MRSTFT 1.174，均为对比中最优；Wave-L2 等次优。主观 MOS / Spatialization / Similarity 均最高（如 MOS 4.21）。消融：仅 TDW 时 DILD 极差；去掉 TDW、EAM 或 CFRN 均损害耳间与谱指标。作者称对音乐等 OOD 音频也有效。

## 结论
时频耳间注意力 + 位姿条件残差融合可显著改善 ILD/ITD 与感知质量；未来需更大双耳数据与更广听测以提升跨数据集泛化。

## 点评
相对纯时域/扩散基线，把优化目标对齐到 DILD/DITD/MRSTFT 更贴近空间听感。TDW 提供粗 ITD、ISAN/CFRN 补 ILD 与频相关线索的分工清晰。局限仍是单一小数据集与固定分裂；Wave-L2 并非最优也说明波形全局误差与耳间保真不完全一致。


# Geometry-Informed Distributed Acoustic Scene Understanding

- 论文编号：821
- 报告人：Yiyuan Yang
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/yang26f_interspeech.pdf

## 问题
多房间场景中墙门遮挡使单点集中阵列易漏听；分布式麦克风若忽略拓扑，难以判断哪路可靠，也无法按物理邻接补全缺失转移，叙事易出现非物理跳跃。

## 方法
输入为多节点 log-Mel、麦克风坐标与几何 Ω（边界、门洞、材料）。建拓扑图，边权按距离与墙衰减。共享 AST 提节点特征并加位置编码，经图卷积空间融合 + GRU 时序建模；查询式解码器输出每帧语义三元组 ⟨subject, relation, object⟩；将几何与三元组线性化为提示，冻结 Llama-3-8B-Instruct 生成连贯叙事并补全遮挡缺口。

## 实验与结果
基于 pyroomacoustics 的定制多房间仿真（2–4 室，N=6 麦，LibriSpeech+ESC-50）。完整系统 Triplet F1 0.87、BLEU-4 0.55、ROUGE-L 0.62、BERTScore 0.77、SCS 88.2%，优于集中式（F1 0.51、SCS 35%）与仅声学分布式。消融去掉几何先验 SCS 降至 66.5%；去掉时空图融合 Triplet F1 降至 0.81。

## 结论
分布式感知 + 拓扑感知融合 + 几何约束 LLM 推理可提升遮挡下检测与叙事空间一致性；未来需真实测试床验证并优化推理速度。

## 点评
把场景理解写成“感知→符号三元组→几何提示 LLM”流水线，对多房间逻辑接地很有针对性。全部结果来自受控仿真，材料/遮挡参数理想化；冻结 LLM 的补全能力依赖提示质量，真实噪声与标注误差下 SCS 未必同样稳健。


# Branch-wise Complementary Attention for Acoustic Scene Classification

- 论文编号：865
- 报告人：Seung-Gyu Han
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/han26b_interspeech.pdf

## 问题
轻量 ASC 的多分支卷积虽扩大感受野，但分支常简单拼接/相加，未显式建模互补关系，也难补偿各核在时/频上的盲区。通用注意力多为单路径设计，难以按分支差异分配。

## 方法
在 Rep-Mobile 四分支（3×3、3×1、1×3、1×1）上引入 Branch-wise Complementary Attention（BCA）：从融合特征池化得到通道/时间/频率描述子，生成 wc、wt、wf 与联合 wctf，经 element-wise softmax 后分别加权对应分支（通道→3×3、时间→3×1、频率→1×3、联合→1×1）。另提出通道切分的 BCA-Lite 以降参。训练保留分支而不做推理重参数合并。

## 实验与结果
TAU 2020 / 2022 Mobile：BCA 准确率 72.03% / 63.24%，优于无注意力 Rep-Mobile（68.86% / 61.52%）及 SE/ECA/CTFA；参数与 MACs 仅小幅增加。BCA-Lite 略低准确率但更省算力。消融显示提出的注意力–分支分配最优；去掉任一注意力类型均降点；有效感受野面积比明显扩大。

## 结论
按感受野互补分配通道–时间–频率注意力可提升多尺度融合且开销小，适合移动端 ASC。

## 点评
设计原则清晰：给谱向分支补时间注意力、给时向分支补频率注意力。增益来自“互补分配”而非单纯加注意力，分配消融能支撑这一点。代价是推理无法像原版 Rep-Mobile 一样合并分支，部署形态与挑战赛原骨干不完全一致。


# CoSTALA: Compositional Spatio-Temporal Audio-Language Alignment via Multi-Grain Hierarchical Contrastive Learning

- 论文编号：1110
- 报告人：Peiwei Ren
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/ren26b_interspeech.pdf

## 问题
常规 ALM/CLAP 多为全局粗粒度对齐，难处理多事件空间音频序列，易出现上下文漂移、局部语义被平均掉。需要从全局对齐迈向可分辨时序与方位组合的细粒度时空对齐。

## 方法
基于 Clotho 合成 FOA（SRIR 卷积），用 Qwen3-8B 把方位离散到八方向并改写描述；正样本为两段不重叠事件拼接，负样本含时间反转与空间互换。架构：RoBERTa 文本编码 + HTSAT 语义/空间双分支音频编码 + RoPE Transformer 时序编码；产出 hard/soft/global/spatio-temporal 多级嵌入。层次损失：对比 Lcl、三路时空 Lst、局部对齐 Llocal、特征一致性 Lconsist（soft 对齐 stop-grad hard）。

## 实验与结果
约 375 小时、3 万训练 / 9k 评估。完整 CoSTALA 全局时空检索 Text→Audio R@1/5/10 为 8.10/19.86/27.68，优于 SALM、T-CLAP 及仅部分损失配置；Audio→Text 亦最优。仅用语义音频嵌入对接时空文本时检索崩塌，说明空间通路必要。消融显示 Llocal 与 Lconsist 需联用才达峰值。

## 结论
多粒度层次对比与显式时空负样本可缓解长序列全局塌缩，为多事件空间音频–语言理解提供更细粒度基础框架。

## 点评
硬负样本设计（时间 vs 空间错误）把“顺序”和“方位”拆开监督，针对性强。数据全为两事件无重叠拼接的合成 FOA，真实重叠、混响与自然叙述复杂度仍未覆盖；语义-only 崩塌结果有说服力，但评估仍以检索为主，未展示下游生成/QA。


# Perceptually Weighted Minimum Mean Square Error Precoding for Acoustic Multi-User MIMO in Vehicular Personal Sound Zones

- 论文编号：1191
- 报告人：Huihui Wei
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/wei26c_interspeech.pdf

## 问题
车舱个人声区（PSZ）中串扰与频率选择性衰落严重；传统对比控制/压力匹配常把串扰当均匀物理能量，且 bright/dark 二分难同时服务多用户。需要把听感掩蔽纳入多用户联合预编码。

## 方法
将车载扬声器–座位麦克风建模为频域声学 MU-MIMO；在 WMMSE 框架中引入感知加权矩阵 Θ_k：由目标语音的 MPEG 风格掩蔽门限与绝对听阈生成，对敏感时频区加重误差惩罚。目标最小化加权 MSE，并约束总功率与最小声对比度。预编码按 WMMSE 迭代闭式更新或凸优化求解。

## 实验与结果
实车测得 IR：7 扬声器、四座各 16 麦（共 64），ATF 测三次平均；语音来自 LibriSpeech。MU MIMO Perceptual 的 STOI 0.859、ViSQOL 4.191，高于无加权 MU-MIMO 与 ACC/PM/VAST/RACC 等基线。频带上 AC、NRE、AE 三者折中优于偏重对比或过度稳健的方法。

## 结论
感知加权 WMMSE 可在多区同时优化重建与干扰，相对传统声区控制提升客观语音质量；未来将加强 IUI 抑制与不确定条件下的鲁棒性。

## 点评
把通信域 WMMSE 迁到宽带车舱声学，并用掩蔽驱动 Θ_k，比均匀 MSE 更贴近听感。增益相对无加权基线数值不大（STOI +0.002），主要说服力在多用户联合与指标折中；实验为离线测得信道+回放指标，未报听者主观与头动/座位变化鲁棒性。


# SA-HRTF: A Sound-Assisted Approach to Personalized HRTF Modeling

- 论文编号：1995
- 报告人：Qingyin Zhao
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/zhao26f_interspeech.pdf

## 问题
个性 HRTF 测量耗时；稀疏方向下仅靠解剖映射或检索增强（如 RANF）受限于小规模数据库与相似个体难找；纯信号法又常需额外设备且采集质量不稳。目标是在少量已测方向下更准地估计未见主体的 HRTF 幅度。

## 方法
SA-HRTF 双分支：主分支 CR-RANF 用 ITD 检索 K 个相似主体，将该方向参考 HRTF 幅度经 Conv1d 编码，与 ITD+方向经 RFF/FC/Conv 得到的辅助特征在条件残差模块中用 FiLM 仿射融合，再经 FC+LoRA 与转置卷积解码得初始估计；辅分支 SI-HRTF 对双耳波形 FFT 幅度经四层 Conv1d–ReLU–BN（第 2/3 层后加 SENet）与 AvgPool+MLP 得到补充估计；融合模块对两路拼接结果学频率相关权重 α，按元素加权后再经 Conv 精炼。三相均用 log-spectral distortion（LSD）作损失；相位用最小相位近似，本文只建模幅度。

## 实验与结果
公共数据 SONICOM（200 人，793 方向，48 kHz）训 CR-RANF；自定义双耳声由语音/白噪/音乐与 HRTF 频域相乘并加扩散场噪声（SNR 5/10 dB）训 SI-HRTF。划分 160/19/20，测点 q∈{3,5,7,9}。LSD：SA-HRTF 在 q=3/5/7/9 为 3.76/3.82/3.49/3.42，优于 nearest、ITD/LSD 选择、NIIRF、RANF、CR-RANF。声源类型中白噪最好（如 q=3 时 3.02），音乐次之，语音较差（缺高频，融合时主要保留低频并由 CR-RANF 补其余）。方位 ±5°、仰角 ±10° 偏差下 LSD 仍相对稳定。

## 结论
在稀疏测量下，用检索个体 + ITD/方向条件的 CR-RANF 与双耳声信号的 SI-HRTF，经频率自适应融合，可提升个性 HRTF 幅度估计精度与稳健性；实验显示优于若干已有方法，验证声辅助线索有效。

## 点评
贡献在于把“数据库先验检索”和“日常双耳声里的个体滤波线索”做成可学权重的频域互补，而不是只加更多测量点。白噪/音乐优于语音，说明辅分支高度依赖宽频谱激励；自定义合成双耳+固定 SNR、以及依赖 SONICOM 检索库规模，是落地到真实耳机/任意声场时的主要边界。


# Bayesian Model-Based Assessment of Spatial and Source Priors in Sagittal-Plane Sound Localization

- 论文编号：3494
- 报告人：Yunda Chen
- 程序：Tuesday 29 September 2026 / Spatial Audio 3
- 技术分类键：spatial
- 全文：https://www.isca-archive.org/interspeech_2026/chen26fa_interspeech.pdf

## 问题
矢状面定位是病态问题：未知源谱与方向依赖 HRTF 纠缠。人类可能依赖空间先验与生态源谱先验，但既往模型常简化先验或未与个体数据联合评估。本文系统比较空间先验与生态源先验在降谱分辨率下的作用。

## 方法
相关型贝叶斯观察者：gammatone 提取左右耳谱梯度，与个体 HRTF 模板相关→相似度映射→双耳加权似然，再乘空间先验取 MAP，并加响应噪声。空间先验五种：单峰高斯 UG、对称高斯 SG，以及参数化非对称 AG/AL/AvM。生态源先验为语音/环境/音乐特征上的多元高斯，经白化加权相关并入似然。对 8 名正常听者在宽带噪声与多通道声码器条件（N3–N24、CL）上个体拟合，用保护超越概率（PXP）做模型选择。

## 实验与结果
无单一空间先验在群体上稳定最优（最高 PXP 0.281，BOR 高 0.68）；非对称变体整体更贴近人类。生态源先验额外收益有限。各模型均再现随通道数增加 PE/QE 下降（平均 r>0.93），但绝对误差系统性偏高；低通道条件下 MAP 决策可能低估后验不确定性。

## 结论
支持个体化、灵活的空间先验结构；固定语料源先验在本实现与合成刺激下收益有限。低可靠性下需考虑非 MAP 决策。直接推广到人工耳蜗用户前需进一步验证。

## 点评
在同一相关贝叶斯骨架上正交比较先验族，并用声码器操控感觉可靠性，设计干净。高 BOR 说明群体偏好结论宜审慎；源先验固定、空间先验个体拟合的不对称也可能压低源先验贡献。对 CI 的启示是启发式的，数据仍来自正常听者仿真条件。

