# Spatial Audio 4

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：5
- 论文数：11

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场空间音频海报贯穿测量校准、盲 RIR/房间嵌入、生成空间音频评测与视频到 FOA、双耳自监督空间表示，以及分布式阵列上的几何约束分离、几何自标定、定位与 DOA 引导分离。共同主题是把空间几何与语义内容解耦，并在标注有限时用对比、正则或伪测量流程补足监督。

生成与评测侧，FAD（定位相关嵌入）与声学图在响应性、平滑性与对称性上更稳健；视频到 FOA 用“先 mono W、后 XYZ 空间化”解耦 what/where，并以语义增强数据缓解稀疏。表示学习把方向性、扩散性等声学先验写入软声学对比损失。盲估计则从 CTF 重建到房间嵌入不确定性分数，强调内容与劣化导致的表示漂移。

阵列侧从有限阶质心校准方向响应，到 DOA 约束的去中心化 IVA、TDoA CRLB 优化声源放置、网格到连续定位网络、指向性正则 FastMNMF，以及说话人表征引导的多移动声源定位，持续压低排列不一致与网格分辨率—复杂度权衡。

## 论文技术总结

# Addressing random spatial translations in measured microphone directional responses by maximizing finite order energy

- 论文编号：149
- 报告人：Xue Wen
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wen26_interspeech.pdf

## 问题
实测麦克风/阵列方向传递函数（DTF）相对参考中心存在未知空间平移；平移在球谐域间重分配能量，破坏“高阶≈更细空间细节”的假设，给有限阶处理带来不确定性。

## 方法
定义有限阶质心（FOC）：在平移类中寻找使阶数 ≤L 的能量比（FOER）最大的平移，从而最小化截断误差。离散球网格上对球谐正交化算能量，并用阶权重正则与分频段调度优化求稳。可推广到 2D 与阵列（最大化各麦最低 FOER）。将参考中心移到 FOC 作校准。

## 实验与结果
S24+、EasyCom 眼镜等：单麦 FOC 靠近物理麦、阵列 FOC 靠近几何中心，并可暴露测量偏置。插值/平滑：FOC 平移后相对误差下降。方向感知 Ambisonic 编码：方向误差 ≤10° 时多数阵列空间相关与 EQ 改善。ITA/3D3A HRTF 上 FOC 分布标准差约 10–30 mm；阵列 FOC 校准可改善 HRTF 延时图矢状对称性。

## 结论
作者认为 FOC 是声学定义的参考中心，可消除测量定位不确定并支撑有限阶下游处理；能力限于平移，其他指向性缺陷需另法。

## 点评
把“找中心”从几何直觉变成可优化的能量准则，对不规则消费级阵列很实用。用例侧重展示行为而非冲榜；高阶目标更平坦、需正则，物理位置与 FOC 的差距何时关键仍依赖场景。


# Blind Room Impulse Response Identification via Reverberant Speech Spectrum Reconstruction

- 论文编号：217
- 报告人：Pengyu Wang
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26c_interspeech.pdf

## 问题
盲估计房间冲激响应（RIR）避免侵入式扫频测量，但时域长抽头难直接回归；现有方法或固定长度、或需迭代，长 RIR 仍困难。

## 方法
提出 Rec-RIR：在 CTF 近似下，多任务网络先去噪再去混响（交错 cross-band / narrow-band/Mamba 块），融合混响与干净语音嵌入，以窄带块与帧权重池化端到端估计 CTF；主损失为 ˆH⊛S 重建混响谱（Mag+RI），辅以去噪/去混响 Mag+RI 损失。再用伪侵入测量（对数扫频 + 逆滤波）将 CTF 转为最长约 0.96 s 的 RIR。

## 实验与结果
SimACE 上相对 FiNS、BUDDy、VINP：RIR-50 ms RMSE 0.040、¯ρ 0.805；RT60 MAE 0.069、ρ 0.994；DRR MAE 0.684、ρ 0.994；C50 亦最优。约 3.1M 参数、无需迭代。消融显示辅助损失尤其提升 DRR；极早期（<2 ms）不规则峰可能因直达对齐约束而不完整。

## 结论
作者认为将盲 RIR 转为有监督的混响谱重建可稳定估计长 CTF/RIR，并在声学参数与早期反射上达所报告的 SOTA。

## 点评
用 CTF + 谱重建绕开超长时域输出，并与去噪/去混响多任务耦合，结构合理。评测基于仿真+ACE 测得 RIR 的合成观测；直达对齐假设下极早期细节损失需在应用中留意。


# Sensitivity Analysis of Generative Spatial Audio Metrics : A Study on Responsiveness, Smoothness, and Symmetry

- 论文编号：252
- 报告人：Purnima Kamath
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kamath26_interspeech.pdf

## 问题
生成式 First-Order Ambisonics（FOA）缺少对评价度量如何随方位角/仰角等空间控制参数变化的系统认识，难以判断哪些 metric 真正反映空间可控性。

## 方法
提出沿连续空间轨迹做 meta-evaluation：定义 Responsiveness（拟合距离—角位移“帐篷”曲线的平均绝对斜率×R²）、Smoothness（邻域距离抖动的逆标准差）与 Symmetry（正反轨迹距离 RMSE 的指数映射）。用 SoundSpaces RIR + SpatialScaper + FSD50K 合成单源（SS）、多源反向旋转（MS）、同类别多实例（SSMI）及加噪版本，共约 68,400 条 10 s FOA；评估 FAD（M-VGG / S-CRW / F-GRAM / F-PSELD）与样本度量（IV、LSD、IPD、GCCPHAT、MVDR-AM+LPIPS）。

## 实验与结果
F-PSELD 与 MVDR-AM 在 Responsiveness 与 Smoothness 折中上 consistently 居高，且对噪声与场景复杂度更稳；IV 在 SS/MS 尚可，SSMI 对称多源下曲线塌缩。LSD/IPD/GCCPHAT Responsiveness 低，噪声下响应更平坦。多数度量 Symmetry 都高，单独作敏感指标不够。

## 结论
定位导向嵌入与声学图类度量更适合刻画生成空间音频的参数敏感性；研究限于合成 FOA 与有限度量集，后续需真实数据与感知验证。

## 点评
把“度量是否跟得上空间控制”做成可量化的三条曲线性质，比单纯报 FAD 数字更有诊断力。合成轨迹与 20° 步进清晰可控，但对真实生成模型误差分布的迁移仍待检验；IV 在对称多源失效说明空间 cue 选择要看场景结构。


# FoleyImmersive: Decoupling What and Where for Video-to-First-Order Ambisonics

- 论文编号：531
- 报告人：Liming Liang
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liang26b_interspeech.pdf

## 问题
从静音 FoV 视频生成 FOA 时，公开视频–FOA 语料语义稀疏，端到端模型易纠缠“内容”与“几何”，两阶段管线又常在语义保真与空间一致性间折损。

## 方法
FoleyImmersive 解耦 what/where：在 YT-Ambigen 上用 Qwen2.5-VL-7B 增补结构化描述得到 YT-AmbiSem。Stage 1 以语义优先扩散生成单声道 W（MR-CFA 融合 4 fps/1 fps CLIP，并行文本交叉注意力，PTM 用时间检测概率门控残差）。Stage 2 用 complex-STFT U-Net 从 W 预测 XYZ，瓶颈处 Directional Residual Mixer 按视觉与相机方向做通道门控残差，并加能量预算正则；推理时不改动 W。

## 实验与结果
相对 ViSAGe 等：KLDdec 1.532、FADdec 4.253、FADavg 4.126；空间 CC(all)=0.741、AUC(all)=0.851。去 MR-CFA / 去 DRM 均明显掉点。主观 MOS（30 人、50 条）Semantics/Spatiality/Overall 为 4.01/4.16/4.08，优于 ViSAGe。

## 结论
语义增强数据 + 两阶段解耦与轻量方向残差可同时提升视频到 FOA 的语义与空间指标；未来需加强未见复杂场景泛化。

## 点评
把 W 钉死、只在 XYZ 做残差空间化，直接针对“空间化改写内容”的常见病。指标与消融一致支持设计；依赖 VL 自动标注与 FoV→FOA 设定，跨域与全景输入仍需另验证。


# Learning Self-Supervised Spatial Representations via Soft Acoustic Contrastive Alignment

- 论文编号：641
- 报告人：Yotam Silverman
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/silverman26_interspeech.pdf

## 问题
多数音频 SSL 面向单通道频谱语义，对 TDOA、T60、DRR 等空间参数估计不够；标注空间信息昂贵，增强式对比又易破坏细微空间 cue。

## 方法
双流 MC-Conformer（空间/频谱编码器 + 解码器）在未标注双耳数据上做 CCSR 式掩码重建；对空间编码器投影 z 施加 Soft Acoustic Contrastive（SAC）损失：用 GCC-PHAT 估计的 TDOA、GCC 峰幅与三频段相干性构成特征 c，高斯核软权重对齐 batch 内潜空间相似度。下游只保留空间编码器 + 线性头，线性评估与全微调。

## 实验与结果
WSJ×仿真 RIR 预训练 50k；下游未见房间上五任务 MAE。Linear Eval 下 CCSR+LSAC：TDOA 1.06、T60 0.113、DRR 1.86、C50 0.998、ABS 0.067，优于 CCSR 基线；Fine-Tune 下 TDOA 0.288、T60 0.075 等亦最好或接近最好。t-SNE 显示 TDOA 等结构更清晰。

## 结论
把信号处理先验写入软对比目标可改善空间参数表示；局限在仿真数据，极端低 SNR 下 GCC 等特征不可靠可能削弱 SAC。

## 点评
不依赖房间元数据、用可解析声学特征做连续正样本权重，比硬增强对比更贴回归任务。与掩码重建可叠加是工程优点；真实混响与噪声下特征质量决定上限，需实地验证。


# Geometrically Constrained Decentralized Independent Vector Analysis for Distributed Microphone Arrays

- 论文编号：1037
- 报告人：Changda Chen
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26h_interspeech.pdf

## 问题
分布式麦阵上 Dec-IVA 只交换功率统计，但常因跨阵排列不一致、源模型跨阵耦合过强，相对本地 IVA 几乎无增益，噪声下更差。

## 方法
提出 GC-Dec-IVA：MAP 代价在辅助函数上加 DOA 几何约束，使各阵第 n 路 demixing 对同一目标/干扰方向增强或置零，促进跨阵源对齐；另提出按阵分带子频带的源模型 φ，弱化全局共享活动度耦合。VCD 迭代更新 V 与 W；通信仍只交换功率相关统计。

## 实验与结果
仿真 2 讲者、2–8 个双麦阵、无噪与 SNR∈[15,25] dB。噪声下 GC-Dec-IVA II（新源模型）SDRi/SIRi 约 3.3–3.4 / 8.1–8.3 dB，优于 Loc-IVA、原 Dec-IVA I 与 GC-Loc-IVA。排列准确率与一致性近乎完美；部分阵缺 DOA 时 GC-Dec-IVA II 仍保持 Acc≈95–99%。

## 结论
DOA 约束 + 弱化跨阵依赖的源模型可同时提升分离与跨阵排列一致性；实验为同步阵、已知/可推断 DOA 的仿真设定。

## 点评
抓住 Dec-IVA 的核心失败模式（排列错位被全局 rn,t 放大），用几何先验与分阵源模型对症下药。通信开销不增是实用点；真实时钟偏移、DOA 误差与非确定场景仍待测。


# Optimal Source Placement for TDoA-based Geometry Calibration of Distributed Microphone Arrays

- 论文编号：1691
- 报告人：Xu Wang
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26ba_interspeech.pdf

## 问题
分布式麦阵几何自标定常用随机校准声源，相对几何可导致较高 CRLB；若声源位置可控（如移动机器人），如何放置以提升标定精度仍开放。

## 方法
在含 capture time offset（CTO）的 TDoA 模型下推导几何标定 FIM/CRLB，再在房间盒约束内最小化 CRLB 迹得到最优声源位置（一阶段联合优化，SPSA-Adam + 投影）。多阶段方案先联合优化 K=4 个最小可辨识声源，再逐个追加，以降复杂度；并给出 3D 扩展与复杂度分析。实践中用粗估麦位置代替真值构造目标。

## 实验与结果
相对随机放置，一阶段在不同 σd 下 MSEr/MSEδ 更低，且对麦位置初值误差不敏感（σr 至 1 m 时 MSEr 仅增约 0.0034 m²）。声学仿真（GCC-PHAT、RT60=0.3 s、SNR=15 dB、M=N=10）：一阶段 MSEr=0.0489 vs 随机 0.240；多阶段随 K 增大精度逼近一阶段、耗时更短。不同 RT60/SNR 下 one-stage 仍优于随机。

## 结论
最小化含 CTO 的 TDoA CRLB 可指导校准声源放置；多阶段适合算力受限场景。未来将考虑 TDoA 异常值。

## 点评
把“声源放哪”明确成 CRLB 优化，补上标定侧最优放置空白。依赖粗麦位与盒约束，工程上合理；真实机器人路径、障碍与异常 TDoA 会进一步约束可行域。


# G2C-NET: A Grid-to-Continuous Neural Network for Sound Source Localization in Distributed Microphone Arrays

- 论文编号：1733
- 报告人：Zhiyuan Yue
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yue26_interspeech.pdf

## 问题
分布式麦阵网格化 SSL 把回归改成分类，但粗网格量化误差大、细网格算力高；均匀聚合麦对特征也忽略各对可靠性差异。

## 方法
G2C-NET：在 pairwise 特征（GCC/SLF）上用 Adaptive Pairwise Feature Aggregator（可学习 query 注意力）得到全局网格似然 h；Continuous Position Estimation 对峰值邻域（窗口 R）做似然加权质心得到连续坐标。损失 Ld（与高斯目标分布 MAE）+ λLc（坐标 L2），CPE 可微以提供亚网格监督。

## 实验与结果
仿真与 Libri-adhoc40 微调：Ours RMSE/ACC 仿真 25.52 cm / 78.63%，真实 23.35 / 81.15，优于 SRP、GNN、LMSL。少节点时优势更大（如 SLF、M=4：33.09 vs GNN 46.22）。消融显示 APFA 在稀疏阵更关键、CPE 在多节点更关键；λ=10 最优。

## 结论
注意力聚合 + 网格到连续细化可在固定分辨率下降低量化误差并提升鲁棒性，无需更密网格。

## 点评
在保持 pairwise/可变麦数框架的前提下补“可靠性”与“亚网格”，问题切得准。注意力权重与特征质量正相关的分析有说服力；仍偏单源 2D，多源与未知高度需扩展。


# Fast Multichannel Nonnegative Matrix Factorization with Directivity Regularization for DOA-Informed Speech Separation

- 论文编号：2139
- 报告人：Ryosuke Ono
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ono26_interspeech.pdf

## 问题
FastMNMF 联合对角化域里的伪分离滤波器对应虚拟分量而非物理源，本身不利用已知 DOA，难以稳定地选择性提取目标说话人（如智能眼镜场景）。

## 方法
在 FastMNMF 负对数似然上加 directivity 正则：对每个虚拟分量在角度网格上用 von Mises 权重鼓励对目标 DOA 附近响应≈1、对其他说话人方向响应≈0，以容忍 DOA/头动误差。源模型仍乘性更新；Qf 用含线性项 afm 的闭式 VCD。κ→∞ 时退化为点约束 GC。

## 实验与结果
5 麦弧阵、N=1–4、RT60=0.3 s、SNR=20 dB。DR-FastMNMF + von Mises 在 N=1/2 最优（如 N=1 SDR 18.2 vs FastMNMF 13.8；N=2 SDR 9.2），且方差更小。N=3/4 时 SR-FastMNMF（点权重先验）SDR 更高，但提出方法感知指标仍有竞争力。迭代早期收敛更快。

## 结论
全秩空间模型 + 连续角域概率指向正则可提升已知 DOA 下的分离，软权重优于硬点约束；未来需用估计 DOA 评估。

## 点评
把 GC 从“单点内积”推广到 von Mises 软束，贴合 DOA 不确定与混响展宽。N 大时约束变挤导致相对优势下降，说明 DOA 先验与源密度需匹配；真值 DOA 设定偏乐观。


# SpkGuideDOA: Speaker-wise Representation Guidance for Multiple Moving Speaker Localization

- 论文编号：3131
- 报告人：Yongseok Choi
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26g_interspeech.pdf

## 问题
多移动说话人定位在轨迹交叉、角度重叠时仅靠空间 cue（如 DP-IPD）难稳定分轨；分离再关联或 SELD 多任务方案又重、或与纯定位目标不符。

## 方法
SpkGuideDOA：Spatial Cue Estimator 估 DP-IPD；Guidance Generator 从多通道幅度经 band-wise 特征与 SP-SimA+Mamba 得到说话人引导图，在池化分辨率上对 SCE 特征做 sigmoid 门控残差调制。训练用 Joint-PIT 共享排列，LIPD+αLVAD；VAD 损失梯度不回传到 SCE，保持定位为主任务。

## 实验与结果
仿真与 LOCATA：Ours MDR/FAR/MAE 仿真 4.0%/15.8%/5.7°、真实 9.2%/8.9%/5.5°，优于 IPDNet、TF-Mamba、IPDNet2，FLOPs 与 IPDNet2 同为 1.1 G/s。小角度间隔时检测与 MAE 更稳。消融去 GG、去 VAD、VAD 挂到 SCE、去 Joint-PIT 均变差。

## 结论
池化说话人残差引导可缓解重叠歧义并保持低开销；框架可扩展到更多说话人数。

## 点评
把“说话人区分”做成 localization enhancer 而非分离/多任务头，梯度路由与 Joint-PIT 设计干净。K=2 与仿真轨迹设定下结果强；更大 K、更极端交叉与在线时延仍是压力测试点。


# Quantifying the Uncertainty of Blindly Estimated Room Embeddings Using a Dispersion-Calibrated Score

- 论文编号：1357
- 报告人：Yang Xiang
- 程序：Thursday 1 October 2026 / Spatial Audio 4
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xiang26_interspeech.pdf

## 问题
从混响语音盲估房间嵌入时，内容、噪声与丢包等会在房间与几何不变时扭曲表示，下游不可靠；现有工作缺少面向表示可靠性、可单句推理的任务无关不确定性分数。

## 方法
三阶段：Stage-1 在 RIR log-mel 上训 VAE 得结构化潜空间；Stage-2 用混合 CNN–Transformer 语音编码器，多视角 batch（同 RIR 多句）做 KL 对齐到冻结 RIR 后验，并加 multi-positive 对比；Stage-3 冻结编码器，用轻量 MLP 头预测不确定性 U，以干净–损坏嵌入余弦色散 δ 为监督，margin 排序损失保证 U 与 δ 单调一致。

## 实验与结果
约 3000 实测 RIR×EARS 语音。Proposed 验证 AP=0.99，MAErec≈4.06 dB，优于 FiNS 与 MRL-SV；多视角是内容鲁棒主因，对比项带来小幅验证增益。U 与 δ 全局 Spearman ρ=0.90（噪声/频掩/时掩均高），选择性预测上优于按 corruption 强度排序。

## 结论
多视角对齐 + 色散校准不确定性可在单句推理下识别不可靠房间嵌入；局限包括非真正后验、训练需 clean–corrupt 对、按 RIR 划分而非严格房间不相交、损坏类型有限。

## 点评
把“嵌入是否可信”从下游任务解耦成表示级分数，对检索/参数估计统一有用。多视角消融清晰；野外干扰说话人、设备失配等未覆盖，分数解释仍属相对排序而非校准误差条。

