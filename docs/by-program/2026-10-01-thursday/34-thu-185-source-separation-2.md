# Source Separation 2

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：5
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场源分离与目标提取从判别式高指标、听感偏弱，走向一步生成校正、音视频流匹配、伪空间条件、编解码器层级网格，以及仅用说话人身份监督。部署场景覆盖智能眼镜点引导提取、半监督联合分离–日记化，以及远场回传中的自身语音消除（OVC）。

监督信号多样化：干净波形不再唯一——对比对齐说话人嵌入、清洁混合+环境噪声半监督、空间点查询与硬负空间采样均出现。效率上强调一步 MeanFlow/流匹配、压缩潜空间 RVQ 网格与毫秒级延迟掩蔽器。

## 论文技术总结

# MeCo: One-Step MeanFlow-based Corrector for Multi-Channel Speech Separation

- 论文编号：1150
- 报告人：Dohwan Kim
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/kim26j_interspeech.pdf

## 问题
多通道分离判别模型在 SI-SDR 等参考指标上已很强，但常引入不自然伪迹，DNSMOS/UTMOS 等听感指标偏弱；纯生成或迭代修正延迟高，Fast-GeCo 一类一步修正又需两阶段蒸馏、轨迹截断与纯 SI-SNR 微调，存在分布失配且听感次优。

## 方法
MeCo：在复杂 STFT 域，以判别分离结果 ˆs（t=1）与多通道混合 y 为条件，用 Mean Flows 学习平均速度场，一步映射到干净语音（t=0），无需微调解码轨迹。引入 Data-Space Optimization (DSO)：xr-loss（等价对 MeanFlow 损失按间隔 Δ² 加权，惩罚长位移误差）+ Endpoint SI-SDR（训练时模拟一步端点重建并优化 SI-SDR）。骨干 NCSN++；判别前端含轻量 DeFTAN2、SpatialNet、CrossNet；修正器仅在 DeFTAN2 输出上训练后零样本接到其他分离器。

## 实验与结果
域内：WSJ0+WHAM! 四麦混响噪声；域外：Librispeech+DEMAND、低资源语言+DEMAND。一步修正仅 +1 NFE、RTF +0.0068。DeFTAN2+MeCo 在域内 SI-SDR 10.08、DNSMOS 3.19、UTMOS 3.70、NISQA 4.50，全面优于 Fast-GeCo/MeanFlow；域外与跨语言同样领先。消融显示 xr-loss 与 Endpoint SI-SDR 互补。

## 结论
作者认为 MeCo 是首个面向多通道分离的一步生成修正器，在保真与听感上同时达到 SOTA；文末提到独立按说话人修正等局限（正文截断处提及）。

## 点评
用平均速度场直接做判别→干净的一步传输，比扩散蒸馏更干净；DSO 把“生成轨迹误差”与“端点 SI-SDR”绑在一起，解释了为何听感与保真可兼得。脆弱点包括按说话人独立修正、依赖前端分离质量，以及跨分离器零样本仍受前端伪迹形态约束。


# AV-FlowSep: Audio-Visual Target Speaker Separation via Flow Matching

- 论文编号：1960
- 报告人：Pattara Tipaksorn
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/tipaksorn26_interspeech.pdf

## 问题
音视频目标说话人分离中，判别法可懂度强但谱过平滑；扩散生成法听感更好却需约 30 步迭代、推理慢。需要既少步高效又保持感知质量、并能跨数据集泛化的方案。

## 方法
AV-FlowSep 将分离建模为条件流匹配：源为混合 mel、目标为干净 mel，直线 OT 路径上向量场恒为 Mx1−My。DiT（DiT-S：12 层、隐维 384）估计向量场，时间步经 AdaLN 注入，TalkNet-ASD 视觉前端特征经跨注意力条件化；估计 mel 用 Vocos 声码器还原波形。推理 Euler，N_steps∈{1,5}。

## 实验与结果
VoxCeleb2 训练/域内，LRS2 零样本；speech–speech 与 speech–noise（AudioSet，SNR −5–5 dB）。对比 SepFormer、VisualVoice、AV-MossFormer2、AVDiffuSS（30 步）。单步 AV-FlowSep 在噪声场景 DNSMOS/MCD 常最优（如 VoxCeleb2-AudioSet MCD 4.400）；speech–speech 与更大数据训练的 AV-MossFormer2 接近。零样本 LRS2 退化较小。优势方/弱势方 PESQ 差距更小；全脸条件混淆率 12.60%（VisualVoice 唇区仅 0.11%，MossFormer2 33.90%）。

## 结论
条件流匹配 + DiT 可实现单步高质量音视频分离，数据效率与跨域稳定性较好；未来需缓解视觉身份捷径、扩展多说话人与下游 ASR。

## 点评
把“混合→干净”直接当直线流，天然适配少步甚至一步推理，相对扩散分离很务实。声码器路径会引入压缩/相位误差，故需同时看参考与无参考指标；全脸条件提升质量但带来混淆，说明视觉捷径仍是音视频分离的结构性风险。


# Pseudo-Spatially Conditioned TF-Locoformer with MHCA+FiLM Fusion for Single-Channel Speech Separation

- 论文编号：2027
- 报告人：Daichi Nitsu
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/nitsu26_interspeech.pdf

## 问题
单通道分离在噪声混响下困难，因推理时缺少 ITD/ILD/IPD 等空间线索；多通道模型可用这些线索，但部署常只有单麦。需要在训练期利用多通道“特权信息”、推理仍仅单通道的方案。

## 方法
伪空间条件化：（1）对比预训练——SC/MC 两套独立权重 ResNet 空间编码器；triplet 中 anchor 为单通道混合物，positive 为同空间配置不同内容的双通道，negative 为同内容不同空间配置的双通道，使嵌入偏空间配置而非语音内容；（2）与 TF-Locoformer 联合微调，用 MHCA+FiLM 融合模块在每个 Locoformer 块前注入伪空间嵌入（MHCA 得自适应嵌入，FiLM 做特征仿射调制）。推理仅用单通道左耳信号。

## 实验与结果
WHAMR!（8 kHz）：Proposed (S) SI-SNRi 17.7 / SDRi 16.1（基线 17.4/15.9，+1.0M 参数）；(M) 18.9/17.2（复现基线 18.6/16.9，+1.2M）。无噪声 NF-WHAMR! 上 (S) 从 21.4→22.0 SI-SNRi。消融：可训练编码器 + MHCA+FiLM 最优；triplet 内容重叠越少越好；推理时错配/全局平均嵌入会使性能掉到无条件基线以下。

## 结论
用多通道特权信息对比学习伪空间嵌入，再经 MHCA+FiLM 条件化单通道分离器，可在小参数开销下稳定提升 WHAMR! 表现。

## 点评
把“训练见多麦、推理单麦”做成空间表征迁移，比硬加 DOA 头更软。增益约 0.3 dB 量级但统计一致；嵌入错配会伤性能，说明模型确实依赖该条件，也意味着嵌入质量/域偏移会成为新脆弱点。


# Improving Audio Codec-based Speech Separation By Stacking Residual Vector Quantization Layers

- 论文编号：2296
- 报告人：Nhu Minh Phuong Dinh
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/dinh26_interspeech.pdf

## 问题
波形域分离算力高；神经音频编解码器（NAC）在压缩潜空间分离更省算力，但既有 Codecformer 在启用 RVQ 时把各层码本向量求和成单一嵌入，毁掉粗到细层次，导致性能下降。

## 方法
RVQ-Grid：冻结预训练 codec，将各层量化向量堆成 3D 网格 Z∈R^{N×D×T}；经 Conv2D 投影后，用 L 个双轴循环块交替沿码本轴（跨层 BiLSTM）与时间轴（时序 BiLSTM）建模；mask head 输出逐说话人、逐层 mask，再对码本维求和后经 codec 解码。实现 DAC（N=12）与 EnCodec（N=32）两变体，mask 激活对齐各 codec 内部激活。

## 实验与结果
WSJ0-2Mix：相对 Codecformer (DAC) SI-SDRi 从 5.0→8.1 dB（+3.1，摘要称 +3.6）；RVQ-Grid (EnCodec) SI-SDRi 8.6、WER 8.6%（Whisper large-v3-turbo），接近同 codec 条件下的 SepFormer 通路表现，MACs 约为 SepFormer 的 1/6。感知上 PESQ/STOI 明显优于 Codecformer。消融：更多 RVQ 层与更高码率持续提升；长序列训练（10–20 s）可再抬 SI-SDRi；GPU 显存随长度增长远缓于 SepFormer。

## 结论
显式保留 RVQ 层次可显著改善 codec 域分离与下游 ASR 可用性，同时保持压缩域高效；局限是 codec 冻结且非为分离设计。

## 点评
与“别把 RVQ 压扁”的思路一致，用码本×时间双轴建模很直接。SI-SDR 仍低于纯波形 SepFormer 属预期（有损重建），价值在边缘/传码场景；冻结通用 codec 是天花板，也是下一步可改点。


# Speaker Identity as Sole Supervision for Speech Separation

- 论文编号：2620
- 报告人：Christoph Boeddeker
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/boeddeker26_interspeech.pdf

## 问题
分离通常依赖干净参考波形/频谱、多通道空间线索或 MixIT/self-remixing 等信号级无监督目标；真实场景难获平行干净源。能否仅用说话人身份作为监督信号训练说话人无关分离器？

## 方法
Speaker-Identity Supervision (SIS)：训练时每个说话人另有辅助语句 ˜x_k；分离输出与辅助句经嵌入器得 ˆe/˜e，用温度缩放余弦相似度上的 InfoNCE（批内负样本含竞争说话人与其他混合物辅助嵌入），排列用相似度 PIT。嵌入器仅训练期使用：处理分离输出时冻结参数（梯度只回传到分离器），另一次前向更新嵌入器于辅助句，避免嵌入器适应分离伪迹。推理为常规无条件分离器，无需注册语音。骨干为轻量 STFT-magnitude BLSTMP；对比 sigmoid/softmax 掩码。

## 实验与结果
Libri2Mix max 16 kHz。干净集：波形监督 14.4 dB SDR；联合学习嵌入的 SIS 达 8.1 dB SDR、WER 19.4%；冻结预训练 ECAPA 仅 3.0 dB。噪声域：干净训练模型域移严重；用 SIS 从干净波形模型微调到含 WHAM! 噪声的混合物可达 8.7 dB SDR（N5），接近全波形噪声监督 9.7 dB。softmax 强制混合一致性但限制去噪；sigmoid 更灵活但可能引入伪迹。

## 结论
仅说话人身份即可从零训出可用分离器，并可用于无干净参考的噪声域自适应；仍弱于全波形监督，计划结合 ASR/空间约束与更强骨干。

## 点评
把 TSE 里“身份当条件”改成“身份只当损失”，推理零注册，问题设定很干净。关键在嵌入器设计：过鲁棒的验证模型反而害训练。弱监督下放松混合一致性可能生成伪内容，部署需谨慎；更适合作为适配/弱标注场景的补充监督。


# SPOT-TSE: Spatial Point-Guided Target Speech Extraction

- 论文编号：3266
- 报告人：Taewon Ryu
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/ryu26c_interspeech.pdf

## 问题
可穿戴设备上的空间目标语音提取常用固定区域（距离/方位区间）条件化：边界附近标签突变敏感，且仅用距离或方位在空间重叠（同距或同方位）时歧义；区域选择也可能保留整段区间内多源而非精确点源。

## 方法
SPOT-TSE 用连续空间点查询 q=(d_q,θ_q) 条件化多通道提取。SQE：归一化距离/方位经傅里叶特征映射再投影得 z_q，经 FiLM 注入 Mamba 版 TF-GridNet（BiMamba/Mamba 替换 LSTM 以降算力）。输入为多通道 STFT 与 ILD/IPD/CDR。训练用广义高斯邻近权重构造软目标，降低边界刚性；并以 hard-negative 采样（方位近而距离远，或反过来）迫使联合使用两维线索。推理仍按查询点条件化。

## 实验与结果
7 麦智能眼镜阵列仿真（Project Aria），D1→D3 几何难度递增。D3（随机房间+麦位）上 SDR 11.05 dB、WER 0.22（混合物约 −4.64 dB / 1.05）。消融：去掉方位查询或 SQE 性能崩溃；hard-negative 主要帮方位混淆子集；软目标提升整体与边界附近表现。相对 LSTM TF-GridNet，MAC/s 从 40.19 降到 10.54（约 −74%），SDR 相当。

## 结论
点引导空间条件化配合软目标与难负采样，可在重叠/边界模糊场景提升选择性与 ASR 可用性，并降低可穿戴算力；未来需加强距离建模与真机验证。

## 点评
把“选区域”改成“选点+软监督”，直接对准区域法的边界与重叠痛点；傅里叶 SQE 与双轴 hard-negative 设计合理。目前全仿真，真机阵列标定误差与头部运动下的点查询稳定性仍待检验。


# Semi-Supervised Joint Separation and Diarization for Multichannel Noisy Speech Mixtures

- 论文编号：3308
- 报告人：Yuto Nozaki
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/nozaki26_interspeech.pdf

## 问题
联合分离与日志（diarization）在多通道噪声混合中，neural FCASA 主要依赖空间协方差，对扩散噪声、近距离干扰或非平稳噪声稳健性不足，分离结果易残留噪声；完全仿真配对又易域失配，而真实环境又难拿到孤立语音源。

## 方法
在 neural FCASA（LGM + 联合对角化 SCM + 说话人活动）基础上做半监督扩展：训练时用干净语音混合（如会议录音）与噪声单独录音相加构造噪声混合。统一生成模型中显式写 \(x_{ft}=c_{ft}+n_{ft}\)，并给出干净混合的似然。半监督分离目标在原 ELBO 外加三项：阈值 SNR（\(L^{(snr)}\)）、干净混合负对数似然（\(L^{(nll)}\)）、多通道 Itakura–Saito 距离式后验项（\(L^{(misd)}\)）；日志仍用监督 BCE。推理网络结构沿用 RE-SepFormer + ISS 块。

## 实验与结果
用 JSALT2020 Simulate + LibriSpeech + DEMAND 构造 4 通道、最多 4 说话人合成会议数据（SNR 约 2–6 dB）。相对 Neural FCASA（SDR 12.3、PESQ 1.83、DER 4.2），组合三项目标的 P7 达 SDR 13.9、PESQ 2.18、UTMOS 2.19、DNSMOS 2.70、DER 3.6；单独 \(L^{(snr)}\) 对分离提升最大，\(L^{(nll)}\)/\(L^{(misd)}\) 对日志也有帮助。听感上可去掉 FCASA 残留的非平稳噪声。

## 结论
在无需孤立语音源的前提下，用干净混合与噪声录音的半监督目标可同时提升噪声场景下的分离与日志；后续拟扩展到移动说话人/噪声源。

## 点评
把“易采的干净混合 + 噪声”换成可解释的概率目标，比纯仿真更贴近真实会议，且与 FCASA 生成模型一致。仍依赖合成评测与固定阵列几何；空间模型本身对极近干扰或严重扩散噪声可能仍偏弱，三项权重需调。


# Don't Listen to Me: A Lightweight, Low-Latency Model for Own-Voice Cancellation in Far-Field Speech Enhancement

- 论文编号：3430
- 报告人：Mads Østergaard
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/stergaard26_interspeech.pdf

## 问题
远场设备增强后回传用户时，往返时延常超过 10–20 ms，用户自己的声音出现可感知延迟伪影。需要低算法时延地从噪声多说话人混合中去掉已注册（enrolled）的“本机声”，同时保留其余语音并做去噪——即 own-voice cancellation（OVC），与目标说话人提取（TSE）互补。

## 方法
以短 enrollment（2 s）条件化时域网络。基线为 TD-SpeakerBeam；提出 Mamba-MinGRU masker：Mamba 块 + MinGRU 时间混合，因果配置算法时延固定 2 ms（kernel \(L=32\)）。辅助网络可用 ConvTasNet 或更轻的双向线性 RNN（5 块）提说话人嵌入，经逐元素乘适配。损失为可处理静音的 thresholded SDR（active/inactive）。训练：LibriSpeech + WHAM! 动态混合，最多一个干扰说话人；并在 LibriMix 多说话人上测鲁棒性。

## 实验与结果
OVC 与 TSE 难度接近（非因果 F 条件约 13 dB SDR）。因果 Mamba-MinGRU + 线性 RNN 嵌入（c4）：F/D 上 SDR 11.98/11.35，主网 0.33 GMAC/s、辅网 0.26 GMAC/s，远低于 TD-SpeakerBeam 的约 5 GMAC/s。small 变体（d2）单线程 RTF 0.82、F 上 SDR 11.47。同基频说话人更难消本机声；3–5 说话人时 SDR 改善约降 2 dB。

## 结论
OVC 可作为远场流式去噪的实用目标；线性 RNN 主网与辅网在约 2 ms 时延下接近 ConvTasNet 级效果且算力更低，便于流式设备部署。

## 点评
把 hearing-aid 文献里的本机声延迟问题形式化为“消 enrolled、留他人”，与 TSE/AEC 边界清晰。主网轻量是亮点；训练默认双说话人、多说话人明显掉点，且未充分测混响，实场仍需扩展。

