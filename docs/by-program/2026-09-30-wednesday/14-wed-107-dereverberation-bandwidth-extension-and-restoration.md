# Dereverberation, Bandwidth Extension and Restoration

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：6
- 论文数：8
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场聚焦去混响、带宽扩展与波形恢复：在保真与实时性之间平衡谐波一致性、瞬态清晰度与相位重建。超分辨与 BWE 出现 MDCT 域谱上下文建模、辅音/元音分建模轻量方案、高效扩散与 Vocos 骨干任意上采样比；去混响则结合迁移学习跨房间几何、无监督神经模型蒸馏信号处理结果，以及把 U-Net 中间表示解读为 RIR 编码器并用对比 RIR 嵌入条件化训练。

低延迟声码从幅度谱或 Mel 重建宽带/全带波形成为实用焦点；扩散超分被重审训练技术以压缩到约百万参数与数十 GFLOPs。共同趋势是：用物理/稀疏先验与跨域迁移减少对匹配数据依赖，并明确追求可实时部署的高质量恢复。

## 技术内容

### 语音超分与轻量带宽扩展

**STSR: High-Fidelity Speech Super-Resolution via Spectral-Transient Context Modeling**（论文 27；Jiajun Yuan）  
端到端 MDCT 域框架，谱上下文注意力与分层窗聚合非局部上下文，支持至 48 kHz 的谐波恢复；稀疏感知正则防止压缩谱表示丢失瞬态清晰度。摘要称感知质量与零样本泛化超 SOTA，并建立稳健实时范式。

**HWB-plus: A Lightweight Speech Bandwidth Extension Method with Separate Modeling for Consonants and Vowels**（论文 1498；Xueliang Zhang）  
基于 HWB-Net 的改进：Dual-WGMM（ConsWGMM 高频辅音 + VowelWGMM 中低频元音，基于 STRAIGHT 周期/非周期分解）与 VowelWGMM 的 mel 尺度初始化；参数与算力几乎不变。VCTK 上 DNSMOS P.808、PESQ、NISQA 显著优于 HWB-Net、BAE-Lite。

**FastWave: Optimized Diffusion Model for Audio Super-Resolution**（论文 2721；Nikita Kuznetsov）  
将近期扩散训练进展用于任意到 48 kHz 超分；约 50 GFLOPs、130 万参数，训练资源与时间显著少于多数近期扩散/流方案，性能与 SOTA 可比。

**LavaSR: Fast and Flexible Audio Bandwidth Extension via Vocos**（论文 2839；Yatharth Sharma）  
Vocos 骨干 BWE：输入重采样至 48 kHz，单网支持任意上采样比；轻量 Linkwitz–Riley 风格精炼器平滑拼接原低频与生成高频。验证集对数谱距离有竞争力；A100 上 RTF 0.0001，8 核 CPU 上 0.0053。

### 去混响、迁移与 RIR 表示

**A Novel Transfer Learning Approach for Room Impulse Response Estimation and Speech Dereverberation Across Geometrically Diverse and Data-Scarce Environments**（论文 31；Christian Ritz）  
几何感知编码器提取形状不变特征，物理知情解码器施加回声稀疏与能量衰减；微调时冻结编码器仅更新解码器。未见目标几何上摘要称仅 10 个训练房间即 MSE 降 56%、LSD 降 37%；下游去混响 PESQ 3.24 vs GAN 基线 2.78，STOI 0.89 vs 0.79。

**USDnet++: Distilling Signal Processing Based Dereverberation for Unsupervised Neural Speech Dereverberation**（论文 2044；Zhong-Qiu Wang）  
在 USDnet 上用 WPE/WPD 信号处理去混响结果作弱监督改进无标注混响语音上的无监督训练。WSJ0CAM-DEREVERB 上摘要验证有效性。

**Your U-Net Dereverberation Model is Secretly an RIR Encoder**（论文 2707；Sina Khanagha）  
分析 NCSN++ U-Net 去混响模型中间表示可编码结构化 RIR 依赖嵌入，且该隐式房间表示判别力与去混响客观指标相关。提出用自监督对比学习得到的预训练 RIR 嵌入显式条件化；摘要称改善表示质量、加速收敛、提升性能，并显著减少扩散模型推理反向步数。

### 低延迟无相位谱重建

**EffVOC: Low-Delay Efficient Speech Waveform Reconstruction from Spectral Representations Without Phase**（论文 2407；Renzheng Shi）  
高效低延迟声码，支持从幅度谱或 Mel 合成宽带/全带语音，统一框架评估多模型规模。摘要称延迟 20 ms（对比 32 ms 或更高）下主观 MOS 居前（WB 4.17/4.15，FB 4.14/4.11，对应幅度谱/Mel），接近真值。

## 本场要点

- STSR 在 MDCT 域兼顾谐波一致性与瞬态，服务高保真超分。
- HWB-plus 分建模辅音/元音，几乎不增复杂度即提升轻量 BWE。
- 跨几何迁移学习以极少房间数据改善 RIR 估计与去混响。
- USDnet++ 蒸馏 WPE/WPD 结果强化无监督神经去混响。
- U-Net 中间层可作 RIR 编码器，显式 RIR 条件化加速扩散推理。
- EffVOC、FastWave、LavaSR 共同推进低延迟/低算力高质量恢复。

## 覆盖核对

| id | title |
|---|---|
| 27 | STSR: High-Fidelity Speech Super-Resolution via Spectral-Transient Context Modeling |
| 31 | A Novel Transfer Learning Approach for Room Impulse Response Estimation and Speech Dereverberation Across Geometrically Diverse and Data-Scarce Environments |
| 1498 | HWB-plus: A Lightweight Speech Bandwidth Extension Method with Separate Modeling for Consonants and Vowels |
| 2044 | USDnet++: Distilling Signal Processing Based Dereverberation for Unsupervised Neural Speech Dereverberation |
| 2407 | EffVOC: Low-Delay Efficient Speech Waveform Reconstruction from Spectral Representations Without Phase |
| 2707 | Your U-Net Dereverberation Model is Secretly an RIR Encoder |
| 2721 | FastWave: Optimized Diffusion Model for Audio Super-Resolution |
| 2839 | LavaSR: Fast and Flexible Audio Bandwidth Extension via Vocos |
