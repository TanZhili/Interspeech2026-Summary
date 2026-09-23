# Speech Synthesis: Speech Features, Codec and Representations

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：7
- 论文数：6
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场讨论语音合成中的特征、编解码与表示：从 Mel 谱冗余到紧凑 VAE/潜空间，再到离散令牌到波形的解码效率，以及无转录条件与韵律可控恢复。核心是在重建保真、可懂度、说话人相似度与推理速度之间找可训练的折中。

语义对齐进入潜空间设计：高维 VAE 潜变量若缺乏语义结构会损害可懂度；语义正则试图打破“维数越高重建越好但可懂度越差”的困境。Token2Wav 侧则用 MeanFlow 在压缩潜空间做真正一步生成，缓解多步流匹配的质量–速度矛盾。编解码训练范式上也出现免蒸馏的循环一致说话人交换，以及两阶段潜空间补丁建模，让低帧率高质量令牌化可在消费级 GPU 上完成。

面向实际可用性，有工作去掉零样本 TTS 对参考转录的依赖，改用连续自监督语音特征条件；另有工作把韵律恢复统一成从简化韵律输入重建帧级韵律的多任务扩散问题，降低用户指定负担。

## 技术内容

### 潜空间语义对齐与一步 Token2Wav

**Semantic-VAE: Semantic-Alignment Latent Representation for Better Speech Synthesis**（论文 533；Zhikang Niu）  
针对 Mel 冗余与声学 VAE 维数困境，提出 Semantic-VAE，在潜空间施加语义对齐正则，使高维潜表示 simultaneously 利于重建与生成。接入 F5-TTS 后，摘要报告在 LibriSpeech-PC 上 WER 2.10%、说话人相似度 0.64，优于 Mel 系统与普通声学 VAE，并提升训练效率。

**One-Step Token-to-Waveform Generation with MeanFlow in Latent Space**（论文 791；Zheqi Dai）  
在高度压缩潜空间对平均速度而非瞬时速度场建模（MeanFlow），实现真正一步 Token2Wav。摘要称相对多步基线 RTF 最高可提升约 17×，质量下降可忽略；并用仅解码器微调（冻结 MeanFlow 生成器）与端到端联合微调缓潜空间失配，不增加推理代价。

### 免蒸馏解耦编解码与两阶段低帧率令牌化

**CycleCodec: Distillation-Free Factorized Neural Speech Codec via Cycle-Consistent Speaker Swapping**（论文 806；Yang Ai）  
无需 SSL/ASR 蒸馏、从零训练的因式分解编解码。引入循环一致说话人交换作为编解码内部自监督，降低说话人条件生成时的跨流泄漏；并限制时间容量，用基于 query 的 Transformer 聚合器与说话人对比损失强化说话人建模。在英语与未见语言（普通话、越南语）上摘要称优于免蒸馏基线，解耦更稳健。

**Low-Framerate Speech Tokenization via Two-Stage Latent Patch Modeling**（论文 2863；Théodor Lemerle）  
Z-CODEC 两阶段：先用对抗目标训练高帧率 VAE 捕获细粒度声学细节；再在其潜空间用流匹配做最终压缩并加入语义监督。摘要称在低码率离散与连续设置均达先进重建质量，且可在单块 RTX 4070 上可复现训练。

### 无转录条件与统一韵律恢复

**Transcript-Free Flow-Matching Text-to-Speech via Speech Feature Conditioning**（论文 3190；SooHwan Eom）  
RTFree-F5 用连续自监督语音表示经轻量适配器映射到 F5-TTS 文本条件空间，替代推理时的参考转录，并复用预训练检查点。在构音障碍语音上摘要称 WER 从 24.6% 降至 10.4%，超过真实参考转录基线，自然度提升，且在标准基准上仍有竞争力。

**Unified Prosody Restoration Using Diffusion Models for Controllable Text-to-Speech Synthesis**（论文 2942；Yuki Ito）  
将韵律恢复统一为从简化、易指定的韵律输入恢复帧级韵律，共覆盖五项任务（扩展既有两项并新增三项），支持部分、粗粒度或二者兼有的输入。提出监督式（反演模拟退化）与无监督式（线性逆问题采样器）两套扩散韵律恢复器。摘要称五任务上均比非扩散基线更准确，并保留语言上有效的韵律结构。

## 本场要点

- Semantic-VAE 用语义对齐缓解高维潜变量的重建–可懂度权衡。
- MeanFlow 潜空间一步 Token2Wav 大幅降低 RTF。
- CycleCodec 用循环说话人交换实现免蒸馏内容–说话人解耦。
- Z-CODEC 两阶段潜空间补丁使低帧率高质量令牌化可在消费级 GPU 训练。
- RTFree-F5 去掉参考转录，改善非典型说话人零样本 TTS。
- 扩散韵律恢复统一多任务，降低可控 TTS 的帧级指定负担。

## 覆盖核对

| id | title |
|---|---|
| 533 | Semantic-VAE: Semantic-Alignment Latent Representation for Better Speech Synthesis |
| 791 | One-Step Token-to-Waveform Generation with MeanFlow in Latent Space |
| 806 | CycleCodec: Distillation-Free Factorized Neural Speech Codec via Cycle-Consistent Speaker Swapping |
| 2863 | Low-Framerate Speech Tokenization via Two-Stage Latent Patch Modeling |
| 3190 | Transcript-Free Flow-Matching Text-to-Speech via Speech Feature Conditioning |
| 2942 | Unified Prosody Restoration Using Diffusion Models for Controllable Text-to-Speech Synthesis |
