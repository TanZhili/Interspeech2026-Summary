# Language-Model and Codec-Token Speech Enhancement
- 日期：Tuesday 29 September 2026 / 时间：09:00-11:00 / 形式：Oral（Area 6）/ 论文数：6
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本场聚焦基于语言模型与神经编解码离散/连续表征的生成式语音增强（SE）：统一多任务、压幻觉、提听感，以及用感知奖励做后训练对齐。相对判别式 SE，生成式在低 SNR、瞬态噪声下更易出现语音样幻觉，成为贯穿摘要的核心瓶颈。

统一与条件化方面，UniSE 用解码器唯一自回归 LM 覆盖恢复、目标说话人提取与分离，并加渐进强化学习；DelayGSE 用延迟多码本建模与文本感知机制抑幻觉。质量路径上，StuPASE 在 PASE 上换干目标与 flow-matching 模块追求棚级听感；Genhancer 系工作用 Hydra（双向 Mamba）替换 DF-Conformer 的 FAVOR+ 以加强全局序列建模。

表征空间选择成为理论–实验交叉点：cNAC-SE 预测连续潜变量、dNAC-SE 预测离散 token，摘要称充分细调的连续方案总体更优，并强调 VQ 正则本身可带来干净先验约束、不必依赖离散 token 路径。后训练则直接用 GSPO 与 DNSMOS/WER/UTMOS 等多度量感知奖励，避免单度量 reward hacking。

## 技术内容

### 统一 LM 增强、文本感知与低幻觉生成

**UniSE: A Unified Framework for Decoder-Only Autoregressive LM-Based Speech Enhancement**（论文 192；presenter：Chengwei Liu）
探索自回归 LM 统一 SE 任务的有效性。UniSE 在输入语音特征条件下自回归生成目标离散 token，覆盖 speech restoration、target speaker extraction 与 speech separation，并用多评估准则的渐进强化学习优化质量。摘要称相对判别/生成基线具竞争力。

**DelayGSE: A Generative Speech Enhancement Framework with Delayed Text-Aware Conditioning**（论文 232；presenter：Xin Yuan）
面向去噪、去混响与音频超分的多码本语言模型框架，条件为带噪 STFT 与 Whisper 编码，延迟建模多码本；文本感知抑幻觉，重要性感知码本加权平衡听感与语义。摘要称达先进水平，消融显示幻觉抑制与相对 WER 下降。

**StuPASE: Towards Low-Hallucination Studio-Quality Generative Speech Enhancement**（论文 837；presenter：Xiaobin Rong）
在稳健但听感有限的 PASE 上：用干目标而非含模拟早期反射的目标细调以改善去混响；用 flow-matching 替换 GAN 生成模块以在强加性噪声下仍达棚级质量。摘要称在低幻觉同时听感优于既有 SE。

### 编解码表征、序列骨干与感知奖励后训练

**Improving DF-Conformer using Hydra for high-fidelity generative speech enhancement on discrete codec token**（论文 1833；presenter：Shogo Seki）
用双向选择性状态空间 Hydra 替换 DF-Conformer 中的 FAVOR+，以去除随机特征近似并保持相对序列长度线性复杂度。在离散 codec token 生成式 SE 模型 Genhancer 上，摘要称超过 DF-Conformer。

**Towards Robust Generative Speech Enhancement Using Vector Quantisation-Based Neural Audio Codec**（论文 2564；presenter：Haixin Zhao）
比较 VQ-NAC SE 中连续（cNAC-SE）与离散（dNAC-SE）潜空间建模及 VQ 正则作用。摘要称充分细调 cNAC-SE 在多样测试条件下优于各 dNAC-SE，DNS-MOS 领先；并认为 VQ 通过干净先验约束增强鲁棒，可迁移到其他连续建模。

**Post-Training Speech Enhancement Language Models with Perceptual Rewards**（论文 3405；presenter：Antonis Asonitis）
自回归 SE LM 常用 token 交叉熵，与感知评测脱节。用 GSPO 与多度量感知奖励（DNSMOS、WER、UTMOS）做后训练，无需可微代理或离线偏好对。应用于 UniSE 与 GenSE，摘要称 DNS2020 达先进；人评显示复合奖励优于任一单度量。

## 本场要点
- 生成式 SE 的统一多任务与幻觉抑制是并列目标。
- 文本/语义条件与延迟多码本建模用于稳定生成并减幻觉。
- 干目标细调与 flow-matching 被用于在强噪声下抬听感。
- 状态空间（Hydra）替代近似注意力以加强 codec-token SE 的全局建模。
- VQ 正则的干净先验效应可与是否走离散 token 预测分开讨论。
- 多度量感知奖励后训练可缓解单度量 reward hacking。

## 覆盖核对
`192 | UniSE: A Unified Framework for Decoder-Only Autoregressive LM-Based Speech Enhancement`
`232 | DelayGSE: A Generative Speech Enhancement Framework with Delayed Text-Aware Conditioning`
`837 | StuPASE: Towards Low-Hallucination Studio-Quality Generative Speech Enhancement`
`1833 | Improving DF-Conformer using Hydra for high-fidelity generative speech enhancement on discrete codec token`
`2564 | Towards Robust Generative Speech Enhancement Using Vector Quantisation-Based Neural Audio Codec`
`3405 | Post-Training Speech Enhancement Language Models with Perceptual Rewards`
