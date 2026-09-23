# Long-Form Speech Synthesis

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster（Area 7）
- 论文数：9
- 材料：官方程序中该场全部论文摘要（[Interspeech 2026 Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA 列表](https://www.isca-archive.org/interspeech_2026/index.html)）。摘要写明问题、方法与主要结论；未出现的数字与细节不写入。

## 技术趋势

本场围绕长文本、多角色与细粒度韵律控制下的语音合成展开。与单句 TTS 不同，长篇有声书与对话合成更强调跨句语境、说话人一致性与边界自然度；多篇工作从训练期建模与推理期补丁两条路径切入。

一类工作把“长上下文”做成显式机制：有的引入章节级语境与风格解耦，有的在不重训长文本的前提下用 soft attention prior、有状态分句推理与历史文本编码维持韵律连贯。另一类则转向系统编排，用多智能体闭环做角色建档、合成质检与人机反馈改写，把长音频叙事当作生产流程而非单模型任务。

细粒度控制是本场另一主线。Flow-matching / LLM-based TTS 在强调、词级强度与节奏上仍受数据稀缺与声学先验冲突制约；多篇采用 SFT→偏好对齐→在线强化学习的级联优化，并用韵律工具或自建偏好对提供奖励。动态韵律预测则强调“基于已生成语音再预测当前音节韵律”，以提升个性化相似度。

与“把合成做得更好”并列的是“把问题说清楚”：有工作用大规模匹配语料揭示神经 TTS 在全局 F0 变异压缩与局部音高翻转增多、元音空间收缩等层次上的解离；也有工作为非人声/设计声效转换提供数据与基准。内存瓶颈同样突出——分钟级对话在密 mel 上的条件流匹配迫使分块，压缩潜空间成为可行折中。

总体看，长篇合成正从“能念完”转向“可控、可检、可评”：语境与状态化推理解决连贯性，偏好/RL 解决局部强调，评测与数据则约束指标掩盖的真实失真。

## 技术内容

### 长上下文与叙事系统

**audiobook-cc: Controllable Long-context Speech Generation for Multicast Audiobook**（论文 2125；Min Liu）
面向单句 TTS 难以支撑的多播有声书连贯性与细粒度控制，提出语境感知、情感可控框架：语境一致性机制、风格与提示解耦，以及提升表现力的自蒸馏。摘要报告章节级 M-MOS 达 4.25（相对最强基线约 14% 相对提升），对话 S-MOS 为 4.11，高强度情感判别提升 31 个百分点。

**MagpieTTS-LF: Inference-Time Long-Form Speech Generation Without Training on Long-Form data**（论文 1461；Jing Yao Li）
针对长篇生成中的韵律漂移、说话人不一致与句界伪影，提出推理期方案 MagpieTTS-LF，无需在长文本上重训 MagpieTTS。方法含 soft attention prior、跨分句维持上下文的有状态推理，以及利用历史文本做篇章韵律规划的编码。实验称在长文本上相对基线提升长程可懂度、韵律连贯、说话人一致性与边界自然度。

**AuDirector: A Self-Reflective Closed-Loop Framework for Immersive Audio Storytelling**（论文 1180；Wen Wu）
长音频叙事常见角色设定与声线不匹配、弱自校正与交互不足。AuDirector 以自反思闭环多智能体完成身份感知前期制作、协同合成与缺陷再生，以及自然语言反馈驱动的脚本修订。实验称在结构连贯、情感表现与声学保真上优于既有基线。

**ZipL-Dialog: Memory-Efficient Long-Form Spoken Dialog Synthesis via Latent Flow Matching**（论文 185；Jihwan Kim）
零样本对话 TTS 的流匹配在密 mel 上做分钟级生成时显存瓶颈严重。ZipL-Dialog 将条件流匹配移至 4× 时间压缩（25 Hz）潜空间，并用确定性 mel 自编码器与辅助 mel 域监督、优化 ZipFormer 分层下采样。摘要称峰值 GPU 显存相对基线降 11.22×、推理加速 2.23×，同时保持感知自然度。

### 细粒度韵律与强调控制

**Refining Emphasis Control in Flow-Matching TTS via Preference Alignment and Reinforcement Learning**（论文 2284；Jiangnan Ye）
在 F5-TTS 上增加 Emphasis Encoder，并采用三阶段优化：人工标注上的 SFT、用 Wavelet Prosody Toolkit（WPT）排序样本的 Direct Preference Optimization，以及将 Flow-CPS 适配为流匹配在线 RL、以 WPT 为奖励。实验称显著提升强调强度与可控性并保持自然韵律。

**CraftTTS: Fine-Grained Prosody Control for Text-to-Speech**（论文 2018；Qihang Lu）
零样本 TTS 难做严格词级强度与语速控制。CraftTTS 三阶段：计算驱动自动构建大规模偏好对；联合 SFT 与 DPO 提升对局部韵律标签敏感度；以多维韵律奖励做 group relative policy optimization，平衡可懂度、强度对比与节奏。实验称在保持零样本能力下达到细粒度表现力上的领先结果。

**Dynamic Prosody Prediction in LLM-based TTS for Improving Speaker Similarity**（论文 2312；Zhenwei Mou）
指出 LLM-based TTS 常忽略生成语音中的风格相关韵律模式。方法基于已预测语音动态预测当前音节韵律。三数据集实验称增强韵律学习并提升说话人相似度。

### 评测诊断与非人声数据

**Not Flat, But Dissociated: Prosodic and Segmental Divergence in Neural TTS**（论文 2730；Rong Wang）
MOS 与 mel-cepstral distortion 等全局分难以定位失真。对 Tacotron2-DDC、FastSpeech2、Glow-TTS、MixerTTS 在 13,100 条匹配 LJ-TTS 上分析：全局 F0 变异压缩而局部 pitch reversal 增加，计时指标无可靠偏离；元音空间缩至人类基线的 9–30%，并见发音不足与协同发音减弱。两层次偏差大体不相关，提示韵律组织与音段精度是被标准指标混为一谈的不同维度。

**Designed Vocalizations Dataset: Sound-Designed Human and Animal Voices for Non-human Voice Conversion**（论文 932；Seolhee Lee）
公开基准多聚焦自然人类语音，怪物/机器人等设计声效转换资源不足。工作发布 Designed Vocalizations Dataset：对语音与动物发声施加专业声效处理，并提供按源音色与预设风格划分的 seen/unseen 测试集与基线结果。

## 本场要点

- 长篇合成瓶颈集中在跨句语境、说话人一致与句界伪影，而非单句音质。
- 推理期状态化方法（MagpieTTS-LF）可在不训长文本时改善连贯性；潜空间流匹配（ZipL-Dialog）主攻显存与吞吐。
- 多智能体闭环（AuDirector）把叙事一致性拆成建档、质检与交互改写。
- 强调/词级韵律控制普遍走 SFT→偏好对齐→RL，并依赖 WPT 等韵律奖励或自动偏好对。
- 诊断性研究显示神经 TTS 失真是韵律与音段“解离”，标准全局指标会掩盖层次差异。
- Designed Vocalizations Dataset 把评测边界扩到非人设计声效转换。

## 覆盖核对

- 2125 | audiobook-cc: Controllable Long-context Speech Generation for Multicast Audiobook
- 1461 | MagpieTTS-LF: Inference-Time Long-Form Speech Generation Without Training on Long-Form data
- 1180 | AuDirector: A Self-Reflective Closed-Loop Framework for Immersive Audio Storytelling
- 932 | Designed Vocalizations Dataset: Sound-Designed Human and Animal Voices for Non-human Voice Conversion
- 185 | ZipL-Dialog: Memory-Efficient Long-Form Spoken Dialog Synthesis via Latent Flow Matching
- 2730 | Not Flat, But Dissociated: Prosodic and Segmental Divergence in Neural TTS
- 2284 | Refining Emphasis Control in Flow-Matching TTS via Preference Alignment and Reinforcement Learning
- 2018 | CraftTTS: Fine-Grained Prosody Control for Text-to-Speech
- 2312 | Dynamic Prosody Prediction in LLM-based TTS for Improving Speaker Similarity
