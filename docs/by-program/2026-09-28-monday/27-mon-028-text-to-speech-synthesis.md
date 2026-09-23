# Text-to-Speech Synthesis

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Long Oral
- 论文数：6
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场为跨领域长口头报告，覆盖流匹配 TTS 的在线 RL、离散流匹配零样本合成、通用 GAN 声码器目标、零样本评测、文本到音频指令遵循，以及可流式零样本风格转换。主线是：生成质量之外，还要可控优化、可区分评测与实时风格迁移。

训练侧，FlowTTS-GRPO 把 ODE 轨迹改写为 SDE 路径，直接对开源 FM 模型做在线 RL；DiFlow-TTS 在离散空间做流匹配以降低连续 token 优化难度；RAF 用 SSL 辅助判别器与相对论配对提升 GAN 声码器域内保真与泛化。评测与对齐侧，I2D 用迭代自参考放大系统差距；ALLM 细粒度反馈构造偏好对改进多事件时序指令。系统侧 StyleStream 以 Destylizer+DiT Stylizer 实现约 1 s 端到端延迟的流式转换。

## 技术内容

### 流匹配优化与离散/GAN 合成

**FlowTTS-GRPO: Online Reinforcement Learning with Multi-Objective Reward Optimization for Flow-Matching Based Text-to-Speech**（论文 1102；Haoxu Wang）
将 ODE 轨迹转为 SDE 路径，无需辅助模型即可微调开源 FM TTS。加权奖励组合收敛快于概率方案；训练时省略 CFG、合成难例、对 FM 组件做 RL 可提升音频细节指标。在 CosyVoice 3.0 与 F5-TTS 上报告说话人相似度与感知质量的主客观提升，F5-TTS 还可懂度改善。

**DiFlow-TTS: Compact and Low-Latency Zero-Shot Text-to-Speech with Discrete Flow Matching**（论文 1043；Son Nguyen）
提出离散流匹配零样本框架：确定性 Phoneme-Content Mapper 做语言学建模，Factorized Discrete Flow Denoiser 同步生成韵律与声学 token。摘要称多指标验证有效，旨在平衡质量与推理效率。

**RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis**（论文 646；Yongjoon Lee）
用语音 SSL 协助判别器评估样本质量，并以相对论真假波形配对。多数据集上 GAN 声码器主客观指标一致提升；RAF 训练的 BigVGAN-base 以仅 12% 参数在感知质量上优于 LSGAN 训练的 BigVGAN。

### 评测、指令遵循与流式风格转换

**Iterate to Differentiate: Enhancing Discriminability and Reliability in Zero-Shot TTS Evaluation**（论文 2414；Shengfan Shen）
I2D 递归地把模型上一轮合成当作下一轮参考。强模型在更多迭代中保持可懂度、说话人与感知质量，弱模型更快退化。聚合迭代客观指标提升可区分性与人类一致性，UTMOSv2 系统级 SRCC 从 0.118 升至 0.464；覆盖 11 模型与中英及情绪数据。

**Improving Text-to-Audio Instruction Following via Fine-Grained Feedback from Audio-Aware Large Language Models**（论文 1111；Chun-Yi Kuan）
用 ALLM 核验目标事件存在与时序关系，经人类验证后构造 DPO 偏好对；并发布叙事基准 S3Bench。实验称在现有基准与 S3Bench 上提升事件完整性、时序次序与联合指令遵循准确率，同时保持音频质量。

**StyleStream: Real-Time Zero-Shot Voice Style Conversion**（论文 404；Yisi Liu）
首个可流式零样本风格转换系统：Destylizer 去风格保内容，DiT Stylizer 依参考重注入音色/口音/情感；文本监督与强信息瓶颈保证解耦。全非自回归，端到端延迟约 1 s，代码公开。

## 本场要点

- 流匹配 TTS 可用 ODE→SDE 改造直接做在线多目标 RL。
- 离散流匹配与相对论对抗反馈分别瞄准延迟/优化难度与声码器泛化。
- 零样本 TTS 客观指标易饱和，迭代自参考评测可放大差距并贴近人类判断。
- ALLM 细粒度反馈可改善多事件时序文本到音频指令遵循。
- StyleStream 显示实时零样本风格转换在约 1 s 延迟下可行。

## 覆盖核对

- 1102 | FlowTTS-GRPO: Online Reinforcement Learning with Multi-Objective Reward Optimization for Flow-Matching Based Text-to-Speech
- 1043 | DiFlow-TTS: Compact and Low-Latency Zero-Shot Text-to-Speech with Discrete Flow Matching
- 646 | RAF: Relativistic Adversarial Feedback For Universal Speech Synthesis
- 2414 | Iterate to Differentiate: Enhancing Discriminability and Reliability in Zero-Shot TTS Evaluation
- 1111 | Improving Text-to-Audio Instruction Following via Fine-Grained Feedback from Audio-Aware Large Language Models
- 404 | StyleStream: Real-Time Zero-Shot Voice Style Conversion
