# Real-Time, Low-Latency and Edge Speech Enhancement

- 日期：Tuesday 29 September 2026
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

本场统一主题是在严格算法延迟与边缘算力下做语音增强。HALO 通过减半内部帧率消除 STFT 重叠冗余；LaCo-SENet 与 LCA 框架把延迟从“因果/非因果二元”变成可配置连续谱。

传感与结构路径包括皮肤贴附加速度计 FiLM 调制、因果时频 Mamba + 渐进蒸馏，以及面向助听器的分布式双耳 RT-Tango。趋势是：同一骨干服务多延迟档、用插件/适配器切换前瞻，并借助辅助模态或状态空间模型压低内存与 MAC。

## 论文技术总结

# HALO: Half-Frame-Rate Adaptive Learnable Operator for Lightweight STFT-Based Speech Enhancement

- 论文编号：601
- 报告人：Jiadong Zhao
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/zhao26c_interspeech.pdf

## 问题
轻量 STFT 增强模型常按帧跑，但 50% 以上重叠使相邻帧高度相关，算力在冗余时序上浪费；直接去掉重叠又会伤质量。需要在不改 STFT/ISTFT、不增算法延迟的前提下降低 backbone 内部帧率。

## 方法
提出 HALO：因果插件，在 backbone 前用动态卷积把相邻两帧自适应融合为半帧率特征，backbone 在半帧率上增强，再用对称的动态卷积把每帧还原为原网格上的两帧。门控对 T-F bin 预测 kernel 混合权重。省下的算力用于加宽通道以匹配原 MAC/s。在 DNS3（含 DiDiSpeech 普通话）上插到 GTCRN、DPCRN 系列、LiSenNet、UL-UNAS 等。

## 实验与结果
消融：无重叠 STFT 明显掉点；固定核/抽帧/复制还原均弱于自适应 HALO。GTCRN+HALO（加宽）相对基线 PESQ 2.101→2.198、SI-SNR 11.39→11.90，MAC/s 相近。跨 backbone 在可比算力下均有提升；小模型增益更大，大模型与已高度优化的 UL-UNAS 增益变小。75% 重叠设定下 HALO 仍有效。不加宽时可将 MAC/s 从约 33.8M 降到 22.1M 且接近基线质量。

## 结论
重叠引起的时序冗余是轻量 STFT 增强的共性瓶颈；HALO 以可插拔半帧率算子释放算力并用于加宽，在不增算法延迟下稳定提点。峰值逐步算力未降，峰值感知调度留待未来。

## 点评
问题切在“架构瘦身后仍被 hop 绑死”的系统层，比再削一层更对症。自适应融合/还原比简单抽帧关键。局限是还原在同一步吐两帧，峰值算力仍高；对已很强的 NAS 骨干收益有限。


# Latency-Configurable Streaming Speech Enhancement via Asymmetric Temporal Padding

- 论文编号：817
- 报告人：Yunsik Kim
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/kim26g_interspeech.pdf

## 问题
流式增强的延迟–质量常被当成因果/非因果二选一，多数模型锁死在单一延迟点。需要在固定参数量的卷积架构里系统配置延迟，并解决非对称 padding 在分块流式中污染状态缓存的问题。

## 方法
LaCo-SENet（基于 PrimeK-Net，1.37M）：训练时用固定总 padding、按比例 r 拆成左右非对称 padding，改变过去/未来占比而不改感受野与参数量。双缓冲流式：状态缓冲保过去、输入级与特征级 lookahead 缓冲供未来；选择性状态更新只写入当前块帧，防止 lookahead 泄漏进后续状态。同一骨干用不同 padding 比训出一族模型，覆盖约 12.5–75 ms（以至更高上界）。

## 实验与结果
VoiceBank+DEMAND：全因果 12.5 ms 达 PESQ 3.35±0.02，不低于先前约 46.5 ms 因果 SOTA（3.27）；随 lookahead 增至 75 ms 升到 3.43，200 ms 对称上界约 3.47。STOI/CSIG/CBAK/COVL 同步小幅上升。与多延迟点文献模型对比显示低延迟端优势明显。

## 结论
非对称时域 padding 可作为训练期延迟旋钮；配合双缓冲与选择性状态更新，可在固定预算下扫离散延迟–质量曲线，并在全因果极低延迟仍保持强 PESQ。

## 点评
把“延迟配置”从换模型改成换 padding 比，工程上很实用；选择性状态更新是能落地的关键细节。注意每个延迟点仍需单独训练，不是运行时一模型切换；与下文 LCA 的单模型多模式形成互补路线。


# Latency Controllable Speech Enhancement

- 论文编号：2997
- 报告人：Hiroshi Sato
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/sato26_interspeech.pdf

## 问题
应用延迟预算从助听的数毫秒到电话/离线的数百毫秒不等；多数增强模型只训一个固定 lookahead，多预算就要存多套全模型。需要单系统可切换延迟并尽量共享参数。

## 方法
在因果 Conv-TasNet 骨干上插入 Lookahead Module（LAM）：堆叠膨胀 depthwise 1-D 卷积，通过因果/非因果块的二进制模式控制 lookahead 帧数。Latency Control Adapter（LCA）为每个延迟预算备一个 LAM 适配器，推理时切换；可跨适配器共享因果块与非因果块参数。Intra-batch multi-latency training：同一 batch 过全部 K 个适配器并平均损失。标准设定 τenc=20 ms，K=7，总延迟约 20–650 ms；另测 τenc=5 ms 超低延迟设定。

## 实验与结果
LibriSpeech+DNS4 噪声：LCA 相对为每延迟训整模的多模型基线，多数点 SDR/DNSMOS 更高（标准设定平均约 +0.13 dB SDR；超低延迟设定平均约 +0.53 dB）。存参：七模型共 104.1M → LCA 共享 16.5M / 不共享 24.5M（约降 76%），推理 MACs 与单 LAM 相同（1.46 G/s）。消融：冻结骨干只训适配器、去掉因果块结构、或每 batch 只随机选一个适配器都会掉点。即使最终只用最低延迟，联合训仍可相对纯因果提升（如 5 ms 设定 +0.45 dB SDR）。

## 结论
LCA 实现运行时可切换的多延迟增强：共享骨干、只换轻量适配器，在恒定推理算力下减少存储并常优于分模型训练。

## 点评
与“每延迟重训整网/改 padding”不同，这篇强调部署侧一模型多模式与跨延迟蒸馏。Intra-batch 联合损失是增益来源。代价是训练算力随 K 线性放大；适配器插入位置与 lookahead 离散集合仍需先验设计。


# Real-Time Speech Enhancement on Edge Devices Guided by Harmonic and Voice-Activity Cues Utilizing Skin-Attachable Accelerometer

- 论文编号：3119
- 报告人：Yonghun Song
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/song26g_interspeech.pdf

## 问题
极低 SNR 下仅靠声学麦的轻量增强能力不足；皮肤贴附加速度计（ACC）抗噪但高频糊。既有多模态融合用并行编码器或注意力，体积大难上 MCU。需要廉价地把 ACC 线索注入轻量 U-Net。

## 方法
LAU-NetV2：从 ACC 提取帧级 VAD（功率阈值）与浊音谐波软掩码；经轻量 1D 卷积生成 FiLM 的 γ/β，分别在瓶颈 FGRU 前（谐波）与 TGRU 前（VAD）调制特征。骨干为三层下/上采样 U-Net，8 kHz，用噪声 AM 相位做 iSTFT。TAPS（60 名韩语说话人）+ DNS 噪声（SNR −20–20 dB）。部署到 STM32H753：40% 结构化剪枝后微调以满足实时预算。

## 实验与结果
全模型约 45.6k 参数、65.7M MACs/s；PESQ 从纯 U-Net 1.78 升到 2.78，低 SNR（−20–0 dB）优于 VibVoice、LAU-NetV1、FT-JNFS 及 FSPEN/LiSenNet。消融显示 ACC 拼接、VAD-FiLM、谐波-FiLM 逐步贡献；γ 置零比 β 置零伤害更大。剪枝后 PESQ 2.62，MCU 推理 48.66 ms（未剪枝 87.12 ms），端到端约 176 ms；Flash/RAM 约 154/151 KiB。真机 92.3 dBA 噪声下可抑宽带噪声并保谐波。

## 结论
用 ACC 导出的 VAD/谐波做 FiLM 调制，可在极小数参数下显著提升多模态增强，并经剪枝在可穿戴 MCU 上实时运行。

## 点评
把多模态从“重融合”改成“线索调制”，对边缘最实用。机制分析（γ 主导）增强了可解释性。局限是 8 kHz、依赖可靠 ACC 贴附与阈值 VAD；剪枝有可测质量代价。


# RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation

- 论文编号：3197
- 报告人：Sung-Feng Huang
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/chao26_interspeech.pdf

## 问题
实时增强要严守算法延迟与 RTF；Transformer 类 KV cache 随时长增长，而既有 SEMamba 多为非因果离线评估。需要全因果时频 Mamba，并用蒸馏把深层教师压到浅层学生。

## 方法
RT-SEMamba：因果 STFT（窗 400/跳 100，中心关闭→25 ms 算法延迟）、因果卷积与 LayerNorm、单向 Time-Mamba + 帧内双向 Frequency-Mamba，流式维护卷积缓冲与 SSM 状态。教师 8 层 cTF-Mamba，学生 1/2 层；输出级对齐幅/相/复谱，特征级对学生块与教师各层均值做归一化 L2；蒸馏权重前 10% 步渐进升至满值，并叠加原 SE 任务损失。在 VCTK-DEMAND 评估。

## 实验与结果
8 层教师 PESQ 3.32；直接 1 层 3.06，蒸馏后 3.18；2 层 3.19→3.22。RTF：1 层 0.11 vs 8 层 0.29（约 2.6–2.75× 加速），参数/MACs 随层数近似线性。相对因果文献模型，8→1 在 25 ms 延迟、1.05M 参数下 PESQ 3.18，具竞争力。消融支持输出+中间特征蒸馏与渐进 ramp-up。

## 结论
全因果 cTF-Mamba 适合恒定状态流式推理；渐进 KD 能在不增 RTF 下显著抬浅层学生质量，形成更好的实时质量–延迟折中。

## 点评
把 Mamba 的固定状态优势落到严格流式设定，并用深度压缩补浅层容量缺口，路线清晰。与仅加深网络相比，蒸馏更划算。学生与教师仍共享前后端结构，极限压缩潜力取决于块数下限。


# RT-Tango: Real-Time Distributed Binaural Speech Enhancement for Low-Power Hearing Aid Devices

- 论文编号：3301
- 报告人：Zahra Benslimane
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/benslimane26_interspeech.pdf

## 问题
双耳助听要实时、低功耗且设备间通信有限；既有高效方案多在单通道，分布式双耳在低延迟与低算力上仍缺统一框架。

## 方法
RT-Tango 改造 Tango 两阶段分布式架构：每耳 SN-DNN 估 mask → SDW-MWF 得压缩信号传对侧 → MN-DNN  Refine → 最终 SDW-MWF。效率手段：ERB 特征压缩、分组 RNN（SN 用 8 组、MN 用 2 组）、固定速率跳帧复用 mask（FRS）。低延迟用非对称 STFT（长分析/短综合窗）与在线 EMA 更新空间协方差；流式版称 RT-Tango-OS。在仿真双耳与 BinauRec 实测 RIR 子集上评估。

## 实验与结果
4 ms hop 下 RT-Tango 约 33.4 MMAC/s，接近保留 Tango-RNN 质量（PESQ/STOI 约 1.66–1.71 / 0.84），远低于同帧率 GTCRN（197.5）。RT-Tango-OS 算法延迟可至 8 ms，代价是 SI-SDR 等有所下降（如左耳 4.4→2.9），总约 35.1 MMAC/s。消融：SN 分组降本几乎无损，MN 过分组伤约 0.8–1 dB；FRS 优于部分学习 skip 方案。

## 结论
在分布式双耳框架内组合 ERB、分组 RNN、时域稀疏与非对称 STFT，可在超低延迟与低 MMAC 下保持有竞争力的增强与耳间平衡。

## 点评
少见地把“分布式双耳 + 助听级延迟/算力”一起做系统整合，而不是只压单通道网。两阶段 MWF 结构对压缩与耳间平衡友好。在线 SCM 适应期与跳帧对非平稳干扰的鲁棒性仍是部署关键风险。

