# Spatial Audio 1

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral
- Area：5
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场空间音频主题覆盖终端近麦检测、声学场景分类跨设备适配、个性化 HRTF/HRIR，以及双耳定位与紧凑阵列 DOA。手机端 Ada-Mic 用 Generalized Cross-Correlation 特征编码 DOA，把距离与朝向因素解耦，服务 No-Hot-Word 唤醒。

个性化双耳渲染是另一主线：HRIR-Former 在时域、无网格条件下从稀疏测量重建任意方向 HRIR，并辅以 ITD/ILD 头；S2RNF 则走 sim-to-real 神经场，把 3D 头模仿真 HRTF 映射到真实测量对应物，降低消声室测量门槛。

感知与定位方面，BiEAR 借鉴内侧橄榄耳蜗（MOC）反馈，用神经控制器在推理中自适应调节双耳听觉滤波器组频率选择性；紧凑线阵端射方向 DOA 退化被理论归因于远场平面波下 TDOA—方位角映射病态，并在 reliability-aware phase transform 框架内提出加权 SRP 与精炼 TDOA。设备异构与无源数据约束下的 MSFDA（FaSoLa）则用后验调整与标签一致性聚合多源模型。瓶颈集中在朝向变化、测量成本、端射病态与设备域移。

## 论文技术总结

# Ada-Mic: Orientation-Adaptive and Robust Close-to-Mic Speech Detection on Smartphone Using Generalized Cross-Correlation Features

- 论文编号：224
- 报告人：Irina Kezele
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/fong26_interspeech.pdf

## 问题
无热词唤醒常用“贴近话筒说话”检测，但能量/爆破音等特征随手机姿态（DoA）变化，限制可持机角度，妨碍自然交互。需在双麦手机上把距离与朝向解耦。

## 方法
Ada-Mic：在现有贴近话筒检测骨干旁加 GCC-PHAT 分支（隐式编码 DoA 与多径），两支特征拼接后分类近/远。骨干对比扩展双通道的 ProxiMic 式 CNN 与 LoRA 微调 HuBERT。自采约 38 h 华为多机型双麦语音（66 人，距离 2/5/15/30 cm，底/顶麦直射与间接姿态）；Mate60 作测试；叠加音乐/办公室噪声 SNR 5–20 dB。GCC 过采样到 [−2τ,2τ] 再亚采样 100 点；GCC 支额外 FLOPs 约 7.6%（ProxiMic）/<0.01%（HuBERT）。

## 实验与结果
近=2/5 cm，远=15/30 cm。安静下平均准确率约提升 1–3%（未达显著）；Music/Office 噪声下提升更明显（平均约至 5%），Wilcoxon p<0.05。过渡距离 5/15 cm 改善约 5%；难姿态上最高约 +24%。安静场景因基线已高、样本力不足，统计不显著但趋势正向。

## 结论
GCC 插件可提升朝向鲁棒的贴近话筒检测，扩展可用姿态范围，利于无热词交互；适用于多数双麦手机，开销小。

## 点评
用经典 GCC-PHAT 当“姿态侧信道”而非显式估角，工程落地性强。自采姿态覆盖与 Mate60 外推测试有说服力；安静不显著与单测机型是边界。隐私友好（纯音频）相对摄像头方案是实际优势。


# Robust Multi-Source-Free Domain Adaptation via Posterior Adjustment and Label Agreement

- 论文编号：370
- 报告人：Hoyoung Yoon
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yoon26_interspeech.pdf

## 问题
声学场景分类跨设备部署时，隐私与传输限制导致无法共享源数据；多源无源域适应（MSFDA）又受麦克风响应造成的类别预测偏置、以及置信度不可靠困扰。仅 AdaBN 对齐特征统计仍留显著标签偏置。

## 方法
FASOLA：对 K 个冻结源模型，(1) 后验调整——用目标上的边际预测 ˆp_k 与动量估计目标先验 ˆq，校准 logits ˜z = z − τ(log ˆp − log ˆq)；(2) 标签一致性——用留一式多数一致率 s_k 作权重（softmax(γ s)），再加权聚合。先可做 AdaBN。评测 DCASE 2020 Task 1A，Leave-One-Domain-Out（目标为模拟设备 S1–S6），骨干 CP-ResNet；对比 Oracle、Uniform、DECISION、CAiDA、DATE、Bi-ATEN。

## 实验与结果
平均 Acc/F1：FASOLA 54.43/54.04，优于 Uniform 50.68/49.89 与最强基线 DECISION 约 51.88/51.16。消融（S6）：PA/LA 各自有益，完整最好。随机降采样类别时 ˆq 更贴近真先验。权重与真目标准确率相关：r=0.9365、ρ=0.9286，高于 DECISION 等。

## 结论
后验校准 + 一致性加权可在无源数据下缓解设备异质引起的偏置并选出可靠源，稳健于标签分布偏移；未来拟做在线流式、摆脱全局统计依赖。

## 点评
把“设备偏置=标签偏置”说清楚，用先验对齐替代置信度加权，切中 MSFDA 痛点。动量先验与一致性权重形成闭环；仍依赖整批目标统计，边缘实时场景需再简化。会话主题是 Spatial Audio，但内容属 ASC 域适应——按 batch 元数据写程序字段即可。


# HRIR-Former: Grid-Free Time-Domain Reconstruction of Head-Related Impulse Responses with a Spatially Encoded Transformer

- 论文编号：702
- 报告人：Shaoheng Xu
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26c_interspeech.pdf

## 问题
个性化 HRIR 测量成本高；从稀疏方向上采样时，既有学习方法多在频域、依赖最小相位或固定方向网格，损害时域保真与空间连续。需在任意目标方向做时域、无网格双耳 HRIR 重建。

## 方法
HRIR-Former：把测量/目标方向当 token，掩码补全；正弦几何编码（P=6）+ 信号投影 → Transformer 编码器（3 层，D=256，4 头）；MLP 解码全长双耳 HRIR，掩码融合保留测量点；按俯仰–方位重排后 Conv1D 时域细化；辅助 ITD/ILD 头。损失：缺失方向 Lrec + λ_HRTF 复 HRTF 损失 + λ_ITD/ILD。SONICOM（48 kHz，K=256，约 793 方向），180/20 受试者训/验；M∈{3,5,19,100} 稀疏度。指标：NMSE、CD、ITD-E、ILD-E。

## 实验与结果
相对 Nbr、HRTF-Sel、NF-CbC/LoRA、RANF 等：各 M 上 ILD-E 最优；最稀疏 M=3/5 时 ITD-E 最优（18.5/16.4 µs）。NMSE 自 −6.90 至 −10.20 dB，CD 自 0.233 至 0.102（随 M 改善）。消融（M=5）：去正弦编码劣化最大；去 ITD/ILD 头主要伤 ITD；去 Conv1D/LHRTF 均变差；最小相位预处理反而变差。

## 结论
时域无网格 Transformer 可在稀疏测量下重建任意方向 HRIR，无需最小相位假设；各模块均有贡献。未来将做听感测试。

## 点评
把 RIR 式连续空间建模迁到双耳 HRIR，并显式保 ITD/ILD，是自然且必要的扩展。与频域基线比时侧重双耳线索是公平策略；NMSE/CD 无直接跨方法对照，听感仍缺。正弦编码是无网格能力的关键。


# HRTF Personalization via Sim-to-Real Neural Field

- 论文编号：1391
- 报告人：Yoshiki Masuyama
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/masuyama26_interspeech.pdf

## 问题
个性化 HRTF 测量昂贵；仅靠 Mesh2HRTF 等仿真在高频有伪影。希望从日常可得的 3D 头模仿真，经 sim-to-real 得到逼近实测的个性化 HRTF，且无需实验室稀疏测量。

## 方法
S2RNF：共享神经场对方向 d、受试者参数 z_i、域参数 w_j（仿真 j=0 / 实测 j=1）预测 log-magnitude。推理时用 IGON 一步梯度从仿真 HRTF 推 ˆz_i（固定 w_0），再换 w_1 预测实测域。训练显式走同一路径，最小化实测损失 L1 + λL0（λ=1）。架构为 RFF 方向 + BitFit 式 FC（受试者/域偏置）。数据：扩展 SONICOM（200 对仿真–实测，160/15/25）；HUTUBS leave-one-out（对比 SPCA-DNN、BEM-DNN、Proto. DNN）。指标 MAE/RMSE/PolRMSE。

## 实验与结果
SONICOM：S2RNF MAE/RMSE/PolRMSE = 3.60/4.90/40.89，优于平均 HRTF 3.78/5.05/41.63 与 Mesh2HRTF 7.50/10.53/42.27（MAE 配对 t 检验 p=1.5%）；去 L0 变差。频谱上约 5–15 kHz 失真明显下降。HUTUBS：MAE 3.66，优于报告的 BEM-DNN 4.80，略优于 Proto. DNN 3.69，且不需人体测量特征编码器。

## 结论
域参数使受试者潜变量可从仿真推断并切换到实测域，实现无测量个性化；优于纯仿真与若干既有方法。未来拟用摄影测量头模。ITD 个性化留待后续。

## 点评
把 SuDaField 式域条件改造成可训练的显式 sim-to-real 路径，IGON 免额外编码器是实用点。增益相对平均 HRTF 不大但统计显著，且高频修正符合 Elevation 线索；对仿真网格质量与头模精度仍敏感。


# BiEAR: A Human Auditory-Inspired Adaptive Binaural Front-end for Multi-Speaker Localisation and Distance Estimation

- 论文编号：1618
- 报告人：Hanyu Meng
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/meng26c_interspeech.pdf

## 问题
双耳定位与测距多采用固定推理图与前馈前端，难适应非平稳场景与未见环境；且常省略人类听觉中的内侧橄榄耳蜗（MOC）传出反馈。需要可在推理期自适应调节频率选择性的双耳前端。

## 方法
BiEAR：八个 45° 扇区各自 SAD-Net，联合检测源、估方位、分距离类。STFT 后用 ERB 尺度可调 Gabor 子带；每耳用 GRU+FC 控制器，据瞬时与平滑子带 SPL 输出 δ∈[−1,1] 调制 Q 因子（绝对或相对基线 Q）；由 Z 提 ILD/IPD，波形算 CC（±3 ms→100 维），GRU 压缩后进后端。消融：无控制器 / 单控制器 / 双控制器 × Abs/Rel。评测无回声（见/未见说话人，1–3 说话人）与会议室、报告厅（未见说话人，可做环境迁移微调）。

## 实验与结果
无回声：双控制器+Rel 最优（如 1 说话人方位 MAE 约 0.36°/0.39° 见/未见；3 说话人约 8.03°/8.18°），优于 DeepEar、AuralNet 的检测与方位，距离上 AuralNet 仍更强。实房间零样本已优于基线，环境迁移后进一步提升（如会议室 1 说话人检测 93.74%、MAE 3.92°）。可视化显示近耳中高频增强 Q、低频两侧不对称调制，主动控制使时频能量更集中。

## 结论
MOC 启发的双耳自适应滤波可提升多说话人定位鲁棒性并对未见房间更易迁移；控制器是工程抽象而非完整生物模型。结论末抽取略有截断。

## 点评
把“传出反馈→Q 控制”接到扇区定位管线，双耳独立控制器是合理归纳。增益主要在检测/方位，距离仍弱于自注意基线，说明自适应前端与后端任务并不完全同构；实房间迁移仍依赖额外微调，纯零样本空间仍有限。


# End-Fire Degradation-Robust DOA Estimation for Compact Linear Microphone Arrays

- 论文编号：2156
- 报告人：Zheng Wen
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wen26c_interspeech.pdf

## 问题
紧凑均匀线阵在端射附近 DOA 误差显著增大；既往多作经验现象。本文从远场平面波下 TDOA→方位非线性逆映射的病态性解释该退化，并在不增大孔径、无训练条件下提出缓解方法与真实数据集。

## 方法
理论：τ∝cosθ，|∂θ/∂τ|∝1/|sinθ|，Fisher/CRLB 在端射发散。在 reliability-aware PHAT-β 框架上提出：(1) W-SRP-PHAT——逆方差启发加权的 SRP；(2) GCC-WLS——过采样、物理约束时延搜索，并在余弦域 u=cosθ 做加权最小二乘融合后再一次 arccos，避免反复放大误差。自采数据：4 麦、间距 3.5 cm（孔径 10.5 cm），5×4×3 m 房间，方位 20°–160°（步长 10°），距离 1/2 m，每条件约 100–200 段 1 s 语音；端射区定义 [20°,40°]∪[140°,160°]。对比零样本 SRP-PHAT、SRP-MVDR。

## 实验与结果
1 m：W-SRP-PHAT / GCC-WLS 全向 RMSE 约 2.45°/2.43°，端射 3.18°/3.14°，S-ACC_EF 0.82，Deg. Span 0°；基线 SRP-PHAT 全向 3.31°、端射 4.83°、Span 30°。2 m 条件更难，两提案仍显著优于基线（端射约 4.46°/4.99° vs PHAT 7.71°），退化跨度仍为 0°。误差分布呈向正横侧偏置。

## 结论
端射退化源于病态 TDOA–方位映射；方差抑制加权 SRP 与余弦域融合可在紧凑阵上显著稳住端射精度，并公布配套数据集与代码。

## 点评
用 CRLB 把“端射难”说成可设计的病态逆问题，两条补救分别打在聚合与逆映射上，论证清楚。评测全是训练无关方法，贴合电视等边缘设备；局限是单房间、单阵列几何，且端射定义到 40° 偏宽，外推需谨慎。

