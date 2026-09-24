# Speech Synthesis: Speech Features, Codec and Representations

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：7
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场讨论语音合成中的特征、编解码与表示：从 Mel 谱冗余到紧凑 VAE/潜空间，再到离散令牌到波形的解码效率，以及无转录条件与韵律可控恢复。核心是在重建保真、可懂度、说话人相似度与推理速度之间找可训练的折中。

语义对齐进入潜空间设计：高维 VAE 潜变量若缺乏语义结构会损害可懂度；语义正则试图打破“维数越高重建越好但可懂度越差”的困境。Token2Wav 侧则用 MeanFlow 在压缩潜空间做真正一步生成，缓解多步流匹配的质量–速度矛盾。编解码训练范式上也出现免蒸馏的循环一致说话人交换，以及两阶段潜空间补丁建模，让低帧率高质量令牌化可在消费级 GPU 上完成。

面向实际可用性，有工作去掉零样本 TTS 对参考转录的依赖，改用连续自监督语音特征条件；另有工作把韵律恢复统一成从简化韵律输入重建帧级韵律的多任务扩散问题，降低用户指定负担。

## 论文技术总结

# Semantic-VAE: Semantic-Alignment Latent Representation for Better Speech Synthesis

- 论文编号：533
- 报告人：Zhikang Niu
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/niu26_interspeech.pdf

## 问题
连续潜在 TTS 中，高维潜在重建与说话人相似度好但可懂度差，低维相反，形成信息瓶颈式权衡。

## 方法
提出 Semantic-VAE：在 VAE 潜在上与 SSL 表征做语义对齐（如余弦相似度约束），使高维空间保留声学细节同时结构化语义。编码器将 16 kHz 下采样至约 40 Hz 潜在。用于下游零样本/潜在扩散等 TTS，对照不同潜在维度配置。

## 实验与结果
Semantic-VAE 特征在 LibriSpeech-PC test-clean 上达约 2.10% WER 与 0.64 说话人相似度，缓解高维可懂度崩塌。相对未对齐高维潜在，可懂度提升同时保持较好重建/相似度。

## 结论
SSL 语义对齐可打破“高维好听但听不清”的困境，为连续潜在 TTS 提供更稳表征。

## 点评
把瓶颈诊断清楚并用对齐直接干预潜在几何，比单纯调维度更 principled。主数字集中在单一测试集；与离散 codec-LM 路线的系统对比深度取决于正文完整表。


# One-Step Token-to-Waveform Generation with MeanFlow in Latent Space

- 论文编号：791
- 报告人：Zheqi Dai
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/dai26c_interspeech.pdf

## 问题
LLM 式 TTS 依赖语义 token 时，Token2Wav 解码器既要恢复韵律/音色，又要满足低延迟。主流 flow-matching 解码器质量高，但推理需多步 ODE 积分，延迟大；直接在波形空间做一步 MeanFlow 又因序列过长而不稳、吃显存。

## 方法
两阶段流水线：先用轻量波形 VAE 把 24 kHz 语音压到与语义 token 对齐的 25 Hz 潜变量 `z`（潜维 `D∈{8,16,24}`），再用条件 1D DiT 在潜空间做 MeanFlow，学区间平均速度场，推理时一次前向从噪声得到 `z_gen`，再由确定性 VAE 解码器还原波形。条件为 CosyVoice2 风格语义 token（25 Hz、单码本）与 CAM++ 说话人嵌入。为缓解生成潜变量与 VAE 训练分布不一致，在不改变推理路径的前提下做两类精炼：冻结生成器只微调解码器，或端到端联合微调（波形域 MR-STFT + 对抗 + feature matching）。

## 实验与结果
在 LibriTTS 训练、LibriSpeech test-clean 评测。最佳配置为 140M DiT、`D=24`、Joint-FT：相对 CosyVoice2 的 10-step Token2Wav（RTF 0.0775），端到端 RTF 降至 0.0046（约 17×）；WER 3.41%、SpkSim 0.932、UTMOS 3.64、MOS 3.85（基线 WER 3.18、MOS 4.05）。消融显示潜维增大改善质量；140M 略优于 600M；No-FT→Decoder-FT→Joint-FT 感知质量逐步提升。

## 结论
潜空间 MeanFlow 可在固定一次生成器+一次 VAE 解码的代价下实现近似多步 Token2Wav 的可懂度与感知质量，并显著降低 RTF；剩余差距主要来自 token→潜变量生成而非波形解码。

## 点评
核心是把一步生成放到短、低维潜序列上，用 MeanFlow 的平均速度回避多步积分，再用 decoder/joint 精炼吃掉分布 mismatch。路线对实时/端侧 Token2Wav 很务实；脆弱点在于一步大跨度对平均速度估计敏感（更大 DiT 未必更好），且条件仍绑定 CosyVoice2 tokenizer 与说话人编码器，跨 token 体系可迁移性未在正文验证。


# CycleCodec: Distillation-Free Factorized Neural Speech Codec via Cycle-Consistent Speaker Swapping

- 论文编号：806
- 报告人：Yang Ai
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zheng26_interspeech.pdf

## 问题
因子化神经语音编解码常靠 ASR/SSL 蒸馏拆开内容与说话人，低资源或未见语言缺可靠 teacher；无蒸馏的 TiCodec 等又易残留跨流泄漏，可控合成不稳。

## 方法
在 TiCodec 骨干上从零训练：帧级离散时变码 `q`（单码本大小 256，约 0.6 kbps）承载内容/韵律，全局连续嵌入 `g` 承载说话人。架构上缩小码本容量抑制时变流泄漏，并用可学习 query 的 Transformer 聚合器（N=8、L=4）+ 说话人对比损失强化 `g`。核心自监督是 cycle-consistent speaker swapping：批内置换配对，用源 `q`+目标 `g` 合成 swap 语音，再编码约束 `q_swap≈q_src`、`g_swap≈g_tgt`，并用源 `g` 解码回 cycle 语音施加 mel 重建损失。两阶段训练：先 `L_codec+L_spk`，再冻结编码器与量化器，对解码器做 cycle 微调。

## 实验与结果
LibriTTS（24 kHz）训练；重建与零样本 VC 在英语（LibriTTS）、普通话（Seed-TTS-ZH）、越南语（VieNeu-TTS）上评测。重建上 CycleCodec 全面优于 TiCodec，PESQ/STOI/V/UV F1 也优于蒸馏式 LSCodec，但 WER 仍高于 LSCodec。零样本 VC：英语上逊于 LSCodec、优于 TiCodec；跨语言时 CycleCodec 的 WER 低于 LSCodec（如 Seed-tts-zh：13.488 vs 15.426；VieNeu：25.706 vs 31.606），说话人相似度仍具竞争力。消融显示去掉 cycle 对内容保持伤害最大；迭代 VC 中 CycleCodec 的 WER 漂移小于 TiCodec。小规模听感：英/中 VC 自然度 MOS 相对 TiCodec 提升。

## 结论
不依赖预训练 teacher，仅靠编解码内部的 cycle 说话人交换与容量/对比约束，即可在跨语言设定下获得更稳的说话人–内容解耦与可控合成。

## 点评
抓住的是“低资源因子化”里 teacher 不可用时，用 codec 自洽的 swap→再分析→swap-back 代替外部语义监督。相对蒸馏路线，跨语言内容保持更稳；相对纯重建指标，WER 仍偏弱，说明内部约束对细粒度声学细节友好、对 ASR 级内容对齐未必最强。依赖说话人标签做对比损失，且第二阶段冻结分析路径，解耦上限仍受第一阶段表示质量制约。


# Low-Framerate Speech Tokenization via Two-Stage Latent Patch Modeling

- 论文编号：2863
- 报告人：Théodor Lemerle
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lemerle26_interspeech.pdf

## 问题
低帧率语义语音 tokenizer 对下游 TTS 很重要，但通常要把波形压缩、对抗训练与语义监督绑在一起训，算力贵、难在消费级 GPU 复现；离散大码本/多层量化也易塌缩、下游建模复杂。

## 方法
提出两阶段连续编解码 Z-CODEC。第一阶段 WavVAE：轻度压缩（100 Hz、瓶颈维 24），SNAC 式编码器 + Vocos 风格 ConvNeXt/iSTFT 解码，用对抗目标吸收波形建模难度。第二阶段 PatchAE：把 `z` 按 patch（8 帧）压到 12.5 Hz 的 `˜z`（连续 VAE 或 FSQ，约 1.1 kbps），用潜空间 flow matching 从 `˜z` 重建高帧率 patch；在 velocity head 上对 WavLM-large 第 6 层特征做余弦语义对齐。下游 TTS 为 encoder–decoder Transformer + 轻量 MLP 预测到 PatchVAE 潜空间的速度场。整套可在单卡 RTX 4070/4090 上训练。

## 实验与结果
数据为 HiFiTTS2 + LibriTTS。LibriTTS test-clean 上，WavVAE 重建 PESQ 达 4.14；完整 Z-CODEC（VAE/FSQ）在 12.5 Hz 上与 Mimi、Higgs、XY-Tokenizer 等可比（FSQ：PESQ 2.23、UTMOSv2 3.05、dCER 0.59%）；去掉 WavLM 监督后 dCER 升至 1.49%。MUSHRA 主观质量与 Higgs 同属前列。TTS（0.24B）CER 1.1%，NMOS/SMOS 与更大参数的 F5-TTS、SparkTTS 接近。编解码在 RTX 4090 上约 130× 实时。

## 结论
分阶段把对抗波形建模与低帧率语义压缩解耦，可在消费级硬件上得到高质量低帧率（连续/离散）tokenizer，并支撑可训练的连续潜空间 TTS；当前非因果、仅英语。

## 点评
关键设计是“先把波形难点锁在高帧率 VAE，再在潜空间做 patch 压缩+FM+SSL”，用训练可负担性换端到端一体优化。强在复现门槛与低帧率质量；脆弱点是第二阶段解码依赖多步 ODE、非因果限制流式，且语义对齐质量高度依赖 WavLM 蒸馏。


# Transcript-Free Flow-Matching Text-to-Speech via Speech Feature Conditioning

- 论文编号：3190
- 报告人：SooHwan Eom
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/eom26_interspeech.pdf

## 问题
F5-TTS 等 flow-matching 零样本 TTS 推理需参考音频转写（常靠外部 ASR）；对构音障碍、口音等非典型说话人，ASR 易错，且即便用 oracle 转写，文本条件与参考 mel 中非典型声学也可能冲突，把异常模式灌进合成。

## 方法
提出 RTFree-F5：冻结 WavLM-Large 提取参考语音连续特征，经两层 MLP 投影器映射到 F5-TTS 原文本条件空间，与目标文本经文本编码器得到的特征在时间维拼接，替代原先的参考转写条件；参考 mel 仍作 unmasked 声学上下文。两阶段训练：先只训投影器对齐空间，再联合微调投影器与 DiT 骨干；训练用同说话人跨句对。推理无需参考转写。

## 实验与结果
基于 F5-TTS v1 Base，LibriTTS 训练。典型说话人（LibriSpeech-PC / SeedTTS）：Stage 2 的 WER/MOS 不低于或优于 oracle/ASR 基线（如 LibriSpeech-PC：WER 1.77%、MOS 4.13）。非典型：SAP 构音障碍上 WER 从原始 24.62%、oracle 基线 20.71% 降到 10.39%，MOS 2.16→2.85，但 SIM 0.60→0.50；L2-ARCTIC 上 WER 10.75%→1.44%，优于 oracle 2.00%。仅 Stage 1 在 SAP 上几乎失效（WER 90%）。

## 结论
用 SSL“潜在文本”替换参考转写，可复用预训练 F5-TTS，显著提升非典型说话人可懂度与自然度，并去除参考转写依赖；说话人相似度与可懂度之间存在权衡。

## 点评
问题抓得很准：infilling 里参考文本带来的规范音素期望会与病理/口音声学打架。用与参考声学同分布的 SSL 条件化解冲突，同时保住目标文本控制。脆弱处是 SIM 下降、训练仅在健康 LibriTTS 上做跨句对，以及依赖冻结 WavLM 对非典型语音的表示质量。


# Unified Prosody Restoration Using Diffusion Models for Controllable Text-to-Speech Synthesis

- 论文编号：2942
- 报告人：Yuki Ito
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ito26_interspeech.pdf

## 问题
显式韵律可控 TTS 常要帧级 pitch/VUV/energy，用户难指定又要符合语言（尤其日语音调）的合法结构。已有工作只覆盖局部补全或平滑细化等单一场景，且常预测音素平均韵律、损失帧内细节。

## 方法
把韵律恢复统一为线性逆问题：由退化算子 `H` 从干净韵律得到易指定的退化输入。覆盖五类任务：Inpainting、从平滑/分段平均细化（Ref-S/Ref-A），以及掩码+粗化组合（InpRef-S/InpRef-A）。提出两类扩散韵律恢复器（DPR）：监督版按模拟退化训练并条件于退化 ID；无监督版只在干净韵律上训条件 score，推理用 DDRM（非盲）或 GibbsDDRM（盲平滑核）。恢复结果再送入可条件于 pitch/VUV/energy 的 FS2+flow-matching 声学模型与 HiFi-GAN。

## 实验与结果
日语情感语料 IH（约 31h）与 JVNV。相对 Det/CVAE 基线，Diff-S 与 Diff-U 在多数任务上降低 log F0/energy 误差并改善 PA-ER；主观韵律自然度上 Diff-U-B（InpRef-S）达 4.74、Diff-S 约 4.21–4.22，明显高于基线约 3.4–3.5。JVNV 上趋势一致。盲任务中已知真实退化时 Diff-U-NB 作 oracle 更优。

## 结论
扩散先验可在统一框架下从部分/粗化/二者兼有的输入恢复帧级合法韵律，监督与无监督 DPR 均优于非扩散基线，并更好保持口音相关结构。

## 点评
把多种用户交互统一成线性退化+扩散求解，对可控 TTS 产品流程很实用；无监督路线用逆问题采样扩展未见退化模式。脆弱点在于评价多用 GT duration、日语情感数据规模有限，且盲设定仍假设平滑核参数化，复杂非结构化用户输入未必覆盖。

