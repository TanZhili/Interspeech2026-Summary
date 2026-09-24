# Voice Conversion

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：7
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场语音转换强调可解释局部线性变换、非平行回文式合成对、一步 Mean Flow、零前瞻流式、低延迟说话人匹配，以及通用内容因子分解与循环流训练。共性挑战是音色–内容–韵律解耦：信息瓶颈易丢韵律并诱发 lookahead；扰动需在音色泄漏与效用之间折中。

应用侧扩展到耳语–正常双向转换（伪平行数据扩增）与面向老年人的模仿学习 TTS。总体路径是：可分析 SSL 空间变换、高效一步生成、因果流式，以及用说话人匿名化等与解耦目标天然对齐的扰动机制。

## 论文技术总结

# SSL-GMMVC: Interpretable Voice Conversion via Locally Linear GMM Transforms in Self-Supervised Representation Space

- 论文编号：1688
- 报告人：Tomoya Tanabu
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/tanabu26_interspeech.pdf

## 问题
LinearVC 等在 SSL 空间做全局线性映射简单有效，但无法适配不同音素簇的局部结构；深度 VC 又难解释。需要在可分析前提下提升表达力。

## 方法
SSL-GMMVC：WavLM-Large 第 6 层特征经双向最近邻对齐成源–目标对，对联合向量拟合 \(K\) 分量 GMM；转换时用源侧后验加权各分量仿射映射 \(\hat y=\sum_k p(k|x)\{\mu_k^y+\Sigma_k^{yx}(\Sigma_k^{xx})^{-1}(x-\mu_k^x)\}\)。\(K=1\) 退化为 LinearVC。协方差分 Full 与 Cross-Diag；HiFi-GAN 合成。

## 实验与结果
CMU ARCTIC 六说话人。数据充足时 Full+\(K>1\) 说话人 EER/主观相似度可超过 LinearVC NC，并常优于 FreeVC；可懂度与 UTMOS 总体可比。Cross-Diag 随 \(K\) 增大也可超过 FreeVC 相似度（参数更省）。分量选择与响音/阻音纯度相关；单分量变换矩阵呈收缩旋转，跨性别角度更大。

## 结论
SSL 空间局部线性 GMM 变换在保持可解释性下提升说话人相似度，并揭示分量与语音学结构、变换几何的联系。

## 点评
“简单可分析 VC”路线上把全局线性换成混合局部仿射，分析扎实。高维 SSL 下 \(K\) 难做大、跨分量旋转平面难对齐，扩展性仍受估计稳定性限制。


# From A to B to A: Palindromic Zero-Shot Voice Conversion with Non-Parallel Data

- 论文编号：1663
- 报告人：Moshe Mandel
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/mandel26_interspeech.pdf

## 问题
非平行 any-to-any 零样本 VC 常靠内容–说话人解耦，易泄漏身份或丢内容；纯 KNN-VC 在短参考下邻居稀疏、质量崩。需要能从非平行数据构造可监督训练信号的方案。

## 方法
回文（palindromic）训练：用 WavLM 特征上的 KNN-VC 把真实目标片段 \(a_1\) 映射成合成源 \(\hat B_1\)，再训 Transformer 把 \(\hat B_1\)（加目标参考 \(A_2\)）还原到目标，波形级用预训练说话人验证损失强化身份。三阶段：先 WavLM→波形 vocoder，再训转换器，再对转换特征重训 vocoder。推理时输入真实源、短目标参考。

## 实验与结果
仅英文 LibriSpeech 训练。英语上各 prompt 时长 Spk Sim/EER 优于 Seed-VC、KNN-VC、Vevo、OOVC，WER/CER/MOS 可比；3 s 参考仍稳健（相对 KNN-VC 优势最大）。多语 LibriSpeech 无微调下 WER 常最佳，相似度与 DNS-MOS 可比。vocoder 后训练抬高 DNS-MOS、抑制伪影。

## 结论
合成→真实回文监督 + 波形说话人损失，可在非平行数据上做强零样本 VC，并跨语泛化。

## 点评
把 KNN-VC 从“推理算法”变成“造平行对的数据工厂”，短参考场景收益最大。依赖离线 KNN 质量与额外 SV 模型；超大规模/高表现力数据与流式仍待扩展。


# MeanVoiceFlow2: Joint Optimization of Mean Flow and Content Encoder for Fast One-Step Zero-Shot Voice Conversion

- 论文编号：1596
- 报告人：Takuhiro Kaneko
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/kaneko26_interspeech.pdf

## 问题
MeanVoiceFlow 等一步流匹配 VC 推理快，但固定重型内容编码器（如 Conformer 瓶颈特征）耗时约为一流步的 10 倍，成为瓶颈；需在无额外预训练声码器条件下联合压缩内容编码与转换模块。

## 方法
MeanVoiceFlow2：用轻量可训内容编码器 \(c_\phi\) 替换教师固定内容编码器，并联合训学生平均速度网 \(u_\phi\)。训练含：(1) 相对教师 MeanVoiceFlow 的转换蒸馏 + 真实数据重建；(2) diffusion-GAN + 样本混合的对抗，提升真实感且不依赖外部声码器判别器；(3) 教师引导条件增强（用教师在打乱说话人条件下生成样本喂内容编码器）促内容–说话人解耦。推理仅用 \(c_\phi\) 与 \(u_\phi\)。

## 实验与结果
VCTK 零样本：相对教师 MVF，nMOS 3.93 vs 3.76，UT/DNSP 更好，CER/SECS 相近，RTF 约降 9×（0.00084 vs 0.0072）。对比 FasterVoiceGrad 主观/客观更优或持平且训练无需预训练声码器。消融显示转换+重建、扩散+混合、CondAug 均有贡献。LibriTTS 上同样约 9× 加速且质量提升。

## 结论
联合蒸馏轻量内容编码器与 Mean Flow，可在保持说话人相似度下明显提速并改善感知质量。

## 点评
抓住“一步流已快、编码仍慢”的真实瓶颈，蒸馏设计完整。仍依赖同数据训好的教师；波形合成用 HiFi-GAN，端到端一步波形未完全打通。


# Zero-VC: Zero-Lookahead Streaming Voice Conversion via Speaker Anonymization

- 论文编号：1340
- 报告人：Yudong Li
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/li26w_interspeech.pdf

## 问题
流式零样本 VC 中，信息瓶颈去音色常丢掉韵律，被迫注入 \(f_0\) 等并缓存未来帧（如 StreamVC 约 60 ms 算法前瞻）；既有说话人扰动又难在“音色泄漏 vs 效用保留”间取得优平衡。

## 方法
Zero-VC：训练时用现成 Speaker Anonymization（SA）扰动源语音以压泄漏、保语言/韵律，再经严格因果流式编码器（20 ms 帧移、零前瞻）提内容；WavLM-large 第 7 层 + 可学习注意力池化提参考音色；因果卷积 HiFi-GAN 式解码器注入全局音色。对抗训练后推理丢弃 SA 与判别器，chunk-by-chunk 缓存因果状态。

## 实验与结果
相对 LSCodec/Seed-VC 扰动，SA 中间音频 SS-S 最低（0.119）且 FPC 较好；训成 VC 后更近“低泄漏高目标相似度”理想区。零前瞻系统相对非流式开源模型：SS-S 0.171、SS-R 0.521、SMOS 最高，WER 3.96%、FPC 0.688，CPU RTF 0.063；算法延迟 20 ms，低于 DualVC3/StreamVC/RT-VC 报告值。无 SA 时对 40–60 ms 前瞻依赖更强。

## 结论
SA 作扰动可同时改善泄漏–效用权衡，并支撑真正零前瞻流式架构，把算法延迟压到单帧下限。

## 点评
把匿名化目标显式对接流式 VC 的核心权衡，延迟叙事有力。训练仍依赖外部 SA 预处理；端到端并入 SA、跨语与总系统延迟仍是后续点。


# Improving Model Expressivity and Speaker Matching in Low-Latency Voice Conversion

- 论文编号：796
- 报告人：Anders R. Bargum
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/bargum26_interspeech.pdf

## 问题
实时零样本 VC 在轻量因果约束下说话人相似度偏低：内容离散单元/发音合成丢失韵律，全局说话人嵌入容量不足，难以表达时变音色。

## 方法
并行编解码器：内容编码器蒸馏 HuBERT 软单元；韵律编码器估计 F0、周期性、V/UV、响度并合成 sinusoid-plus-noise 激励，在解码器各残差块注入；全局说话人编码器（VoxCeleb 预训练）+ 互补说话人编码器，用因果 MHA 将说话人 token 与内容/韵律查询融合为 S_Emb。训练时对内容输入做音高移位、加噪、参数均衡，对说话人编码器做单元级时间掩码以促解耦。推理时将源 F0 按目标均值比缩放。

## 实验与结果
LibriTTS 全 train（555 h / 2311 说话人）训练；零样本：LibriTTS test-clean 377 句 × VCTK 6 未见说话人。相对 RT-VC / StreamVC：SECS 80.83%（+4.18 / +3.02 pp），F0 PCC 0.885；WER/CER 与基线接近。主观 S-MOS 最高（3.25），Q-MOS 略低于 StreamVC；CPU 延迟 64.9 ms。消融显示扰动与互补编码器均提升 SECS。

## 结论
在保持可懂度与低延迟的前提下，激励注入 + 互补说话人融合 + 编码器特定扰动可提升零样本说话人匹配与音高一致性；作者将增益归因于表达能力增强，而非严格证明“动态音色”提取。

## 点评
针对实时瓶颈的设计很务实：用轻量旁路补回离散内容丢掉的韵律，并用因果注意力扩充说话人表征，而不是堆非因果 SSL。互补嵌入的可解释性仍弱（L2 与 F0/响度无清晰对应），扰动会略损可懂度，主观相似度优势也未达统计显著。


# Universal Speech Content Factorization

- 论文编号：198
- 报告人：Matthew Wiesner
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/xinyuan26_interspeech.pdf

## 问题
Speech Content Factorization（SCF）在 WavLM 特征空间用低秩线性分解做免训练 VC，但是闭集：未见说话人需重算分解，难用于开放集 VC 与众包 TTS。

## 方法
USCF：先在若干说话人上做内容对齐 WavLM 矩阵的截断 SVD（默认 r=75），再学通用 speech-to-content 映射 W（三种最小二乘：W1 以 Σ^{-1}U 为目标、W2 近似反转说话人矩阵、W3 取某说话人 S 的伪逆）。对未见说话人，用约 500 帧（约 10 s）目标 WavLM 估计 S_m≈(X'W)^†X'。VC 时 X'_s W S_t 重建目标侧 WavLM 再合成。特征也可用作 TTS 声学目标。

## 实验与结果
LibriSpeech 四组各 20 说话人评测。客观：W1 WER 2.70%、UTMOS 2.805、Spk Sim 0.524，可懂度接近/优于 kNN-VC、LinearVC，相似度弱于闭集 SCF/kNN-VC；主观 MOS/SMOS 与多数基线无显著差异。TIMIT 同音素内：说话人 EER 36.40%（去说话人信息强于 WavLM/ContentVec），音素 EER 11.43%。目标帧数低于 500 时相似度骤降；用 USCF 特征训 flow-matching TTS 较 mel 目标 WER 更低、训练更省（11.44% / 25 epochs）。

## 结论
将 SCF 推广为开放集线性内容因子，可用少量目标语音做零样本 VC，并作为去音色声学特征服务 TTS；未来拟用轻量神经网络稳定 W 与少样本 S_m。

## 点评
抓住 WavLM 几何结构做闭式线性解，数据与训练成本极低。瓶颈在 content-to-speaker 一侧：开放集相似度系统性落后闭集方法；对目标时长与秩敏感，且依赖 kNN 对齐与 WavLM 空间假设，跨域鲁棒性未充分验证。


# CFLOW-VC: An unsupervised cycle training strategy based on normalizing flows for Voice Conversion

- 论文编号：48
- 报告人：FeiBao Song
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/song26_interspeech.pdf

## 问题
非平行 VC 存在训测失配：训练时常从同说话人取样内容与音色，推理却需任意组合；FreeVC 等未充分覆盖内容–音色交叉，泛化不足。

## 方法
CFLOW-VC 基于 FreeVC/VITS：WavLM 先验 + 说话人编码器后验 + Mel-Style 风格编码器；用 flow 可逆性做 cycle training（CTS）：源先验经逆 flow 注入目标音色再循环回源，配合 StarGAN 式对抗、双向 KL、循环 KL 与 HiFiGAN 重建损失；先验侧加 GRL 说话人分类促解耦。WavAugment 加噪声/混响增强。两阶段：backbone 预训练 500k → 冻结后验与解码器后 CTS 200k。

## 实验与结果
VCTK 训练（109 说话人，16 kHz）。Clean/Noise/Accent 三测集相对 DiffVC、Diff-HierVC、StarGANv2-VC、FreeVC：Clean 上 SIM 73.5%、UTMOS 3.948；Noise 上 WER 12.09%、SIM 73.89%、UTMOS 3.911，显著优于基线；Accent 亦最优。主观 MOS 在三集均为最高（Clean 4.39）。消融：去 CTS 大幅变差；去风格编码器伤 SIM/UTMOS；去增强伤噪声鲁棒性。

## 结论
将归一化流与 StarGAN 式循环一致性结合，可在非平行设定下缓解训测失配，提升音色相似度、表现力与噪声/口音鲁棒性。

## 点评
核心是把 CTS 做在高斯先验/后验上而非 mel，降低对抗训练难度，思路清晰。仍依赖预训练说话人编码器与 VCTK 规模；去 CTS 单独加风格编码器反而劣于 FreeVC，说明循环损失才是解耦关键，组件耦合较强。


# WhispEar: A Bidirectional Framework for Scaling Whispered Speech Conversion via Pseudo-Parallel Whisper Generation

- 论文编号：1827
- 报告人：Yingda Shen
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/fang26b_interspeech.pdf

## 问题
耳语缺基频与周期激励，W2N 困难；平行耳语数据稀缺，DSP 伪耳语分布偏差大，现有方法音色/韵律保留差。

## 方法
WhispEar 三阶段：(1) 从 SenseVoice-Large 蒸馏轻量语义 tokenizer（Transformer+FSMN+FSQ），用耳语与正常语音促说话方式不变；(2) 共享 Flow-Matching Transformer（自 CosyVoice2）按方向指示 d∈{w2n,n2w} 从语义 token 生成 mel；(3) 先用真实平行数据训较易的 N2W 统一 tokenizer，再对大量正常语音零样本生成伪平行耳语，最后用真实+伪数据训更难的 W2N。发布双语语料 wEar（真实约 18 h / 146 说话人 + 伪约 3026 h）。

## 实验与结果
wTIMIT（英）与 wEar（中）测试：WhispEar-Scaled（约 3000 h 伪数据）英 SIM 0.577、WER 22.44%、UTMOS 3.75、F0 CoRR 0.513；中 SIM 0.750、CER 14.93%，全面优于 WESPER、DistillW2N、MaskCycleGAN、CosyVoice2。消融：对齐真实对 + 模型伪对（A+P）优于 RAW/DSP；伪数据预训练规模增大后再用真实对齐 SFT，各项持续提升。

## 结论
双向统一语义表征 + 可扩展伪平行耳语生成可缓解数据瓶颈，并带来一致的 W2N 增益；wEar 为后续研究提供双语基准。

## 点评
“先易后难”（N2W→扩数据→W2N）与数据中心 scaling 路线很契合耳语稀缺场景。性能仍强依赖伪数据质量与少量真实对齐微调；噪声鲁棒与多语扩展被作者列为后续工作，部署效率也未充分讨论。


# Imitation Learning for Elder-Facing Speech Synthesis

- 论文编号：2107
- 报告人：Dongrui Han
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/han26d_interspeech.pdf

## 问题
通用 TTS 未照顾老年听感；直接收老人偏好成本高、易疲劳。用专家示范做 RL 微调时，固定奖励易 reward hacking（过度放慢、插停顿）。

## 方法
模仿学习框架：医护人员录制面向老人的粤语示范（及中性对照）；专家奖励头接冻结 StyleTTS 2 韵律编码器，Bradley–Terry 成对训练；发音奖励用 SenseVoice 转写的 Jyutping 音节错误率（SER）；二者调和平均为复合奖励。以 CosyVoice2-Yue 经 SFT 为策略，用带 PPO clip 的 GRPO 优化。OPRL 两阶段：Stage1 把中等奖励、低 SER 的 rollout 并入奖励集并重训；Stage2 在外部文本上按 SER 分箱与分位数赋奖励，再 GRPO。

## 实验与结果
专家数据 125 对 / 1.5 h（train 89）。客观：GRPO w/o OPRL 静音时长 11.51 s、总时长 27.62 s（GT 约 5.43 / 19.27），SER/MOS 差，显 hacking。OPRL Stage2：SER 7.54%、CER 3.86%、MOS 3.78（8 名 66–83 岁听者），优于 base / SFT / 无 OPRL；多项韵律与可懂度指标最佳或次佳，MOS 显著高于 base 与无 OPRL。

## 结论
用专家示范 + 两阶段 OPRL 的 GRPO 可在低资源偏好对齐下缓解 reward hacking，生成更受老年人偏好、可懂度更好的粤语合成语音。

## 点评
把“奖励也 on-policy 更新”对准 hacking 很有针对性，复合奖励抑制牺牲可懂度换慢速。示范仅 1.5 h、听者 8 人，风格是否覆盖真实老人偏好仍受限；发音奖励依赖 ASR/粤拼质量，跨语种移植需重设计。

