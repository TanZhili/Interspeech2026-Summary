# Multi-Channel Processing and Specialized Acquisition (UAV, Radar, Hearables)

- 日期：2026年10月1日（星期四）
- 时间：09:00-11:00
- 形式：Poster
- Area：6
- 论文数：9
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。技术论断仅依据摘要。

## 技术趋势

本场面向可穿戴听戴设备、穿墙/毫米波雷达与无人机极低信噪比听觉，以及多通道相对传递与云边协同增强。共同约束是功耗、时延与极端噪声结构；技术回应包括亚奈奎斯特采样后重建、气导/骨导一致性剪枝、相位几何约束、注意力谱扩展，以及把自噪声或雷达先验写进波束形成/生成模型。

听戴与多模态侧，CAPS 主动降采样/降比特并做带宽扩展以省电；CCAP 按跨模态一致性保留融合关键通道。相位方面 MSGLA 用 STFT 一致性消解几何相位符号歧义。雷达路径上 CAF-Former 与 RAD-GAN 分别攻克穿墙带限与低 SNR 带宽扩展。无人机侧则利用自噪声时相关、频变组成与幅度平稳性做 DoA/NCM/后滤波，或用轻量频带融合 Transformer 做实时单麦增强。多通道与部署上，深度学习估计 ReTM，以及延迟服务器输出 + 层间特征提升 + 协同多通道维纳滤波的云边协作。

## 技术内容

### 听戴采样省电、相位估计与气导/骨导压缩

**CAPS: A Cascaded Reconstruction Model to Power Saving in Hearables Using Sub-Nyquist Sampling with Bandwidth Extension**（论文 506；Sajid F. Dipto）  
有意亚奈奎斯特与低比特 ADC，摘要称听戴功耗约降 3.3×；级联重建支撑窄带到宽带，流式推理 1.36 ms、显存约 11.04 MB，兼顾可懂度与省电。

**An Investigation on Combining Geometry and Consistency Constraints into Phase Estimation for Speech Enhancement**（论文 621；Chun-Wei Ho）  
MSGLA 用复 STFT 一致性约束消解几何相位符号歧义，并基于正弦/余弦定理用噪声相位重建目标相位。Oracle 验证理想条件有效；VB-DMD 与 WSJ0-CHiME3 上匹配或略优于直接相位估计与 DNN 符号预测，尤利于背景噪声抑制。

**Cross-Modal Consistency-Aware Structured Pruning for Efficient Speech Enhancement with Air- and Bone-Conduction Microphones**（论文 1548；Yeeun Kim）  
CCAP 以模态零掩蔽估通道重要性，按与多模态输入的响应一致性排序以保留模态共享信息。成对气导/骨导数据上相对既往剪枝提升 PESQ/STOI，并在同等剪枝比降低推理时延。

### 雷达穿墙/毫米波与无人机极低 SNR

**Through-Wall Radar Speech Acquisition via Cascaded Attention Fusion**（论文 1034；Ruotong Ding）  
CAF-Former 渐进谱扩展 + 级联注意力：多查询自注意力建模长时依赖，频域注意力重标定谱关系。严重劣化下相对 Transformer 基线与 SOTA 一致提升高频恢复。

**mmWave Radar Aware Dual-Conditioned GAN for Speech Reconstruction of Signals With Low SNR**（论文 2330；JASH KARANI）  
RAD-GAN 对玻璃墙后 −5~−1 dB 的 mmWave 信号做带宽扩展；含 Multi-Mel 判别器与残差融合门，先在合成削波干净语音预训练再微调。有限数据、无预训练模块与无增强下优于该任务既有 SOTA。

**Ego-Noise-Aware Spatial Filtering for Reliable UAV Audition in Extreme Low-SNR Conditions**（论文 1530；Chanhong Jeon）  
利用自噪声结构性质：相位一致性引导 TF bin 选 DoA，交叉混合 NCM 与数据驱动空向/方差调制后滤波。−25 dB 时 DoA 准确率 98.12%，无混响与混响下 SI-SDR 与质量相对基线提升。

**DroFiT: A Lightweight Band-Fused Frequency Attention Toward Real-Time UAV Speech Enhancement**（论文 1620；Jeongmin Lee）  
全/子带编解码器 + Pre-TCN 捕谐波平稳结构，频率维 Transformer 在拼接 token 上互融。VoiceBank-DEMAND 混录制无人机噪声上相对 DCU-net/SMoLnet-T 算力约降 15–26×/9–15×，168k 参数支持帧级流式。

### 多通道 ReTM 与云边协同

**Deep Learning Based Relative Transfer Matrix Estimation for Multiple Sources and Multiple Microphones**（论文 2524；Oshan A. B. Yalegama）  
用时域/STFT 卷积与 LSTM 三类监督框架估 ReTM，五类目标指标优于协方差法，语音增强效果与基线相当。

**Cloud-Boosted Low-Compute Multi-Channel Speech Enhancement**（论文 2774；Buye Xu）  
协作框架：延迟服务器输出作附加输入、层间特征 boosting，以及融合边/云加权协方差的协作多通道维纳滤波。相对纯边缘基线显著提升且额外开销很小。

## 本场要点

- 听戴可通过亚奈奎斯特采样 + 重建换功耗，并用跨模态一致性剪枝保融合特征。
- 几何相位需 STFT 一致性消符号歧义；雷达/穿墙依赖谱扩展与双条件 GAN。
- 无人机自噪声结构可反哺 DoA、NCM 与轻量频带 Transformer。
- 深度学习 ReTM 与云边协作波束形成服务低算力多通道增强。

## 覆盖核对

| 论文 id | 标题 |
|--------|------|
| 506 | CAPS: A Cascaded Reconstruction Model to Power Saving in Hearables Using Sub-Nyquist Sampling with Bandwidth Extension |
| 621 | An Investigation on Combining Geometry and Consistency Constraints into Phase Estimation for Speech Enhancement |
| 1034 | Through-Wall Radar Speech Acquisition via Cascaded Attention Fusion |
| 1530 | Ego-Noise-Aware Spatial Filtering for Reliable UAV Audition in Extreme Low-SNR Conditions |
| 1548 | Cross-Modal Consistency-Aware Structured Pruning for Efficient Speech Enhancement with Air- and Bone-Conduction Microphones |
| 1620 | DroFiT: A Lightweight Band-Fused Frequency Attention Toward Real-Time UAV Speech Enhancement |
| 2330 | mmWave Radar Aware Dual-Conditioned GAN for Speech Reconstruction of Signals With Low SNR |
| 2524 | Deep Learning Based Relative Transfer Matrix Estimation for Multiple Sources and Multiple Microphones |
| 2774 | Cloud-Boosted Low-Compute Multi-Channel Speech Enhancement |
