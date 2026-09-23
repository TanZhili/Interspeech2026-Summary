# Voice Conversion

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：7
- 论文数：9
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program）；ISCA 列表（https://www.isca-archive.org/interspeech_2026/index.html）。仅依据摘要陈述，不补写未出现的数字与细节。

## 技术趋势

本场语音转换强调可解释局部线性变换、非平行回文式合成对、一步 Mean Flow、零前瞻流式、低延迟说话人匹配，以及通用内容因子分解与循环流训练。共性挑战是音色–内容–韵律解耦：信息瓶颈易丢韵律并诱发 lookahead；扰动需在音色泄漏与效用之间折中。

应用侧扩展到耳语–正常双向转换（伪平行数据扩增）与面向老年人的模仿学习 TTS。总体路径是：可分析 SSL 空间变换、高效一步生成、因果流式，以及用说话人匿名化等与解耦目标天然对齐的扰动机制。

## 技术内容

### 可解释变换、非平行对与一步流匹配

**SSL-GMMVC: Interpretable Voice Conversion via Locally Linear GMM Transforms in Self-Supervised Representation Space**（论文 1688；Tomoya Tanabu）在自监督特征空间用 GMM 建模源–目标对，以后验加权仿射变换做局部线性转换。摘要称说话人相似度提升、可懂度与自然度相当；约束协方差变体随混合分量增多可超深度学习基线，分量选择与语音结构相关。

**From A to B to A: Palindromic Zero-Shot Voice Conversion with Non-Parallel Data**（论文 1663；Moshe Mandel）在 WavLM 上用 KNN 检索对齐非平行语音，构造合成输入–真实目标输出的监督对，并以预训练说话人验证损失保持目标身份。摘要称仅英语训练即可跨多语达到高自然度与强相似度并优于竞争基线。

**MeanVoiceFlow2: Joint Optimization of Mean Flow and Content Encoder for Fast One-Step Zero-Shot Voice Conversion**（论文 1596；Takuhiro Kaneko）联合优化流式转换模块与高效内容编码器，经 MeanVoiceFlow 转换蒸馏与真实数据重建训练，并加入 diffusion-GAN、样本混合与教师引导条件增强。零样本 VC 上感知质量更高、推理约快 9×，说话人相似度相当。

### 流式解耦、低延迟与通用因子

**Zero-VC: Zero-Lookahead Streaming Voice Conversion via Speaker Anonymization**（论文 1340；Yudong Li）用说话人匿名化作扰动，在抑制音色泄漏同时保留韵律效用，缓解生成器对未来上下文依赖，实现严格因果、零前瞻网络。

**Improving Model Expressivity and Speaker Matching in Low-Latency Voice Conversion**（论文 796；Anders R. Bargum）以激励信号显式补回丢失韵律，并将互补信息融入全局说话人嵌入；训练时用编码器特异信息扰动。保持因果与低延迟约束下，摘要称说话人匹配指标优于实时 SOTA 基线。

**Universal Speech Content Factorization**（论文 198；Matthew Wiesner）将闭集内容因子分解扩展为开集：最小二乘学习通用语音到内容映射，并由数秒目标语音导出说话人变换。作为零样本 VC 具竞争力；USCF 特征还可作音色提示 TTS 的声学表征。

**CFLOW-VC: An unsupervised cycle training strategy based on normalizing flows for Voice Conversion**（论文 48；FeiBao Song）基于 VITS 的无监督循环流训练，缓解训练时内容–音色同说话人、推理需解耦的错配；加入 mel-style 编码器与数据增强。摘要称主客观均优于 SOTA 基线。

### 耳语转换与适老合成

**WhispEar: A Bidirectional Framework for Scaling Whispered Speech Conversion via Pseudo-Parallel Whisper Generation**（论文 1827；Yingda Shen）统一语义表征支撑 W2N 与 N2W；N2W 可从海量正常语音零样本生成伪平行耳语以扩增 W2N。发布迄今最大中英耳语–正常平行语料；伪平行规模增大持续提升性能。

**Imitation Learning for Elder-Facing Speech Synthesis**（论文 2107；Dongrui Han）用模仿学习从专家示范学习面向老年人的 TTS，并以两阶段 on-policy 奖励学习改进 GRPO，缓解有限监督下的奖励 hacking。摘要称 GRPO w/ OPRL 在主客观上优于 GRPO 与监督基线。

## 本场要点

- SSL 空间 GMM 局部线性变换提供可分析 VC 框架。
- KNN 构造合成–真实对支持非平行、跨语零样本训练。
- 一步 Mean Flow 与内容编码器联合优化换取数量级推理加速。
- 说话人匿名化扰动利于零前瞻流式解耦。
- USCF 以线性可逆方式抑制音色并服务下游 TTS。
- 耳语伪平行扩增与适老模仿学习扩展 VC/TTS 应用边界。

## 覆盖核对

| id | title |
|---|---|
| 1688 | SSL-GMMVC: Interpretable Voice Conversion via Locally Linear GMM Transforms in Self-Supervised Representation Space |
| 1663 | From A to B to A: Palindromic Zero-Shot Voice Conversion with Non-Parallel Data |
| 1596 | MeanVoiceFlow2: Joint Optimization of Mean Flow and Content Encoder for Fast One-Step Zero-Shot Voice Conversion |
| 1340 | Zero-VC: Zero-Lookahead Streaming Voice Conversion via Speaker Anonymization |
| 796 | Improving Model Expressivity and Speaker Matching in Low-Latency Voice Conversion |
| 198 | Universal Speech Content Factorization |
| 48 | CFLOW-VC: An unsupervised cycle training strategy based on normalizing flows for Voice Conversion |
| 1827 | WhispEar: A Bidirectional Framework for Scaling Whispered Speech Conversion via Pseudo-Parallel Whisper Generation |
| 2107 | Imitation Learning for Elder-Facing Speech Synthesis |
