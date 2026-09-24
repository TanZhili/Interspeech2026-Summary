# Spoofing, Deepfake Detection and Watermarking

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Long Oral
- Area：
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖音频水印攻防、歌声/语音深度伪造检测、部分伪造定位、合成语音溯源与大规模检测工具链。水印侧一方面暴露现有方案对自适应攻击的脆弱性，另一方面提出面向神经编解码压缩的潜空间零比特水印，强调在编解码不变潜空间中嵌入方向性偏移。

检测侧从“全段真假”走向高分辨率歌声伪迹、部分篡改的转移方向建模，以及无需训练的残差统计指纹归因。工程化方面出现统一可扩展的深度伪造检测工具包，并揭示前端特征提取器与训练数据偏置对跨域泛化与公平性的支配作用。

攻防与评测闭环更明显：攻击要绕过基于消息概率分布的检测器，防御要面对神经压缩与野外条件；归因与定位则把“谁生成的/哪一段被改”作为可部署能力。

## 论文技术总结

# Learning to Evade: Adaptive Attacks on Audio Watermarking

- 论文编号：814
- 报告人：Qiben Yan
- 程序：Tuesday 29 September 2026 / Spoofing, Deepfake Detection and Watermarking
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/ding26b_interspeech.pdf

## 问题
深度音频水印在版权与防克隆中常用，但对抗扰动可替换、伪造或去除水印。解码器输出的逐比特概率近似服从正态，防御方可据此做离群检测；既有攻击难在「攻击成功、音质可接受、仍落在正常概率分布内」三者间兼顾。

## 方法
提出自适应攻击 AWM：支持替换、创建、去除三类目标。攻击前用少量与目标音频特征相近的样本查询编解码器，估计消息概率的正态参数；两阶段优化——先使二进制消息命中目标并靠自适应加权把越界概率拉回估计正常区，再做阈值后处理提音质且保持概率不越界。防御侧用 GT 音频 MLE 拟合分布并以 z-score/p-value 判定是否被攻击。

## 实验与结果
摘要与贡献段称：在两种水印方法、三个语音数据集上，相对基线提升 Attack Success Rate，并能绕过基于分布的检测——替换与创建的检测率低于 10%，去除为 0%；经五种 no-box 扰动后多数 ASR 仍接近或达到 100%。正文后半方法细节后抽取截断，完整数值表未能读到。

## 结论
可读部分表明：利用解码概率正态性既可检测也可被自适应攻击规避；两阶段 + 分布估计是关键。更细结论与消融因全文截断无法完整复述。

## 点评
论文定位为对水印鲁棒性的安全评估（替换/伪造/去除三类威胁模型），抓的是「概率分布防御的可规避性」。强在把检测统计与攻击目标显式耦合；脆弱点在白盒/可查询解码器假设与有限日查询设定。抽取正文在方法论中部截断，结果细节以摘要为准，未编造未出现的表项。


# Joint Fullband-Subband Modeling for High-Resolution SingFake Detection

- 论文编号：1614
- 报告人：Chia-Yu Hu
- 程序：Tuesday 29 September 2026 / Spoofing, Deepfake Detection and Watermarking
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/hu26e_interspeech.pdf

## 问题
歌声合成（SingFake/SVDD）比语音含更丰富谐波与气息等高频细节；多数检测沿用 16 kHz（Nyquist 8 kHz），丢弃 8–22.05 kHz 线索。简单子带融合又常打不过专职全带专家，且伪影在频谱上非均匀分布。

## 方法
Sing-HiResNet：以 44.1 kHz log-power 频谱为输入。Phase 1：全带 ResNet18 专家 + 将 Nyquist 带均分为 N∈{1,2,4,8} 的子带专家，各产 32 维嵌入与 logit。Phase 2 四种融合——决策级平均、特征拼接+MLP、多头自注意力跨专家交互、跨专家蒸馏——系统比较全带全局与子带局部如何协同。

## 实验与结果
WildSVDD（约 97 歌手、3223 曲；训练 27879 句，深伪/真实约 15364/12515）；Test A 未见歌手同语言，Test B 未见波斯语歌手。摘要称显著优于 16 kHz 模型并在 WildSVDD 上达 SOTA，强调高频子带提供互补线索。全文在实验设置段截断，具体 EER/AUC 表未能读到。

## 结论
作者主张高分辨率全带–子带联合建模对野外歌声鉴伪关键；精确数字需回查 PDF。

## 点评
把「采样率天花板」与「子带伪影非均匀」同时问题化，融合策略对比设计清楚。强在相对 SSL-16kHz 路线的物理动机；脆弱点在重采数据带来分布偏移，以及 N 划分固定均匀未必最优。抽取截断已在结果中标明。


# Latent-Mark: An Audio Watermark Robust to Neural Codec Compression

- 论文编号：1979
- 报告人：Yen-Shan Chen
- 程序：Tuesday 29 September 2026 / Spoofing, Deepfake Detection and Watermarking
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/chen26u_interspeech.pdf

## 问题
AudioSeal 等波形/谱域水印对传统 DSP 稳健，但神经编解码（EnCodec、SNAC 等）把不可感知波形扰动当 off-manifold 残差滤掉，一次 encode–quantize–decode 即可抹除水印。需要在编解码器不变潜空间中嵌入可检测痕迹。

## 方法
Latent-Mark：零比特（只标「有无水印」）。对波形加扰动 δ，经梯度优化在编解码器连续潜表示上沿秘密流形轴 vc 产生可检测方向偏移，并用 SDR 约束 ||δ||∞；扰动对齐码本质心方向以保可听度。引入 Cross-Codec Optimization：同时在多个代理编解码器上优化，捕捉共享潜不变量，以零样本迁移到未见黑盒编解码器。检测对潜序列投影均值做统计检验。

## 实验与结果
摘要称对未见神经编解码有稳健零样本迁移，对传统 DSP（噪声、幅度缩放、滤波、重采样等）仍有竞争力，并保持感知不可闻。正文在方法细节处截断，完整定量表未能读到。

## 结论
可读主张：把水印做成编解码器会保留的潜空间方向偏移，而非会被滤除的波形噪声；跨编解码联合优化是迁移关键。

## 点评
威胁模型切中「神经压缩≈强力去水印」这一新攻击面，零比特+测试时优化与静态编码器训练形成对照。强在流形对齐动机清晰；脆弱点在嵌入需白盒代理与逐条优化成本，以及零比特容量限制。抽取截断，数值从略。


# Temporal Transition-Aware Multi-Head Modeling for Partially Spoofed Audio Detection and Localization

- 论文编号：474
- 报告人：Yunsu Kim
- 程序：Tuesday 29 September 2026 / Spoofing, Deepfake Detection and Watermarking
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/kim26e_interspeech.pdf

## 问题
局部伪造（Partial Spoof）只替换句中短片段即可改语义；既有方法多做帧级真伪或边界二分类，未显式建模邻帧如何演化，多段伪造或平滑拼接时边界线索弱。

## 方法
过渡感知多头框架：SSL 前端抽 20 ms 帧特征 → multi-scale GRU（扩张卷积路径捕获约 ±60 ms 局部 + 长程流）→ 三头——frame head（帧真伪）、transition head（相邻帧 Real→Fake / Fake→Real / None）、refinement head（融合帧分与过渡概率得时序一致输出）。总损失为帧损失 + λ_tran 过渡损失 + λ_ref 精炼损失，边界帧加权。

## 实验与结果
数据：PartialSpoof（Train 2580/22800 bona/fake 等官方划分）与 PartialEdit-E1/E2（说话人不相交，bona 来自 VCTK）。摘要称在三套数据、20 ms 分辨率上达 SOTA。全文在实验设定处截断（「resolution of 2…」），具体指标表未能读到。

## 结论
作者认为方向性帧间过渡是比单纯帧标签更可靠的定位线索；精炼头负责时序连贯。定量细节需回查 PDF。

## 点评
把 PSAL 从点分类推进到「邻帧状态机」监督，与多段 PartialEdit 场景匹配。强在多头分工清楚；脆弱点在过渡标签噪声与 λ 敏感，以及 20 ms 分辨率对极短音素级篡改的下限。抽取截断已注明。


# Lightweight Detection and Model Attribution of Synthetic Speech via Residual Statistical Fingerprints

- 论文编号：1361
- 报告人：Matías Pizarro
- 程序：Tuesday 29 September 2026 / Spoofing, Deepfake Detection and Watermarking
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/pizarro26_interspeech.pdf

## 问题
合成语音检测多为二分类，缺少生成系统归因；现有归因多封闭世界多分类，新模型出现需重训。法医场景需要轻量、免训练、可开放世界的来源识别。

## 方法
Residual Statistical Fingerprints（RSF）：对信号与滤波版本之差取平均残差作为模型指纹（类比图像 GAN 指纹）。测试残差相对各类指纹分布算 Mahalanobis 距离，统一覆盖开放世界单模型归因、封闭世界多模型归因、真假分类与 OOD。滤波在 STFT 上做（优选低通 1 kHz、带通 5–6 kHz）；细粒度 STFT（8 ms / 0.125 ms hop）略优于标准设置。

## 实验与结果
ASVspoof LA 上单模型归因：A16/A19 留出评测，Mahalanobis 明显优于相关（如低通 1 kHz 平均 AUROC 0.98 vs 相关 0.91）。摘要称跨多种合成系统与语言、在四类任务上表现突出，并对噪声等失真稳健。全文在 STFT 分辨率分析处截断，后续主表未能完整读取。

## 结论
可读部分支持：残差统计指纹 + Mahalanobis 可做免训练归因与检测；协方差建模优于简单相关。

## 点评
把图像域指纹思路迁到语音残差空间，部署成本低、适合开放世界单模型查询。强在统一距离框架；脆弱点在滤波/STFT 超参与合成器进化后指纹漂移。截断后半已标明。


# DeepFense: A Unified, Modular, and Extensible Framework for Robust Audio Deepfake Detection

- 论文编号：1366
- 报告人：Yassine El Kheir
- 程序：Tuesday 29 September 2026 / Spoofing, Deepfake Detection and Watermarking
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/kheir26_interspeech.pdf

## 问题
深伪检测实现碎片化、配方隐藏细节多、难公平复现；缺少覆盖大量前端/后端/数据的统一工具包。

## 方法
开源 PyTorch 工具 DeepFense：YAML 编排 + Data Foundry（Parquet 元数据、增强）+ Engine（前端→后端→损失）+ Trainer/日志。集成 Wav2Vec2、WavLM、HuBERT、EAT、MERT、Whisper 等前端，AASIST、Nes2Net、TCM 等后端及多种损失/增强；宣称 100+ recipes、400+ 预训练模型。大规模对照：4 前端 × 4 后端 × 6 训练集 ≈ 96 系统 × 3 种子，13 测试集。

## 实验与结果
前端主导性能方差：Wav2Vec2 宏平均 EER 25.5% 最优（11/13 集第一），HuBERT 33.6% 最差；后端影响较小。训练数据上 ASV19/CodecFake 等相对更好，ADD23 训练宏平均 EER 约 50.8%、跨域灾难性失败。摘要与后文强调高质量模型在音质、说话人性别、语言上存在严重偏差。工具复现可与原报告持平或更好。

## 结论
统一流水线使「前端 > 训练数据 > 后端」的贡献可分离；需关注公平数据选择与前端微调，而非只堆后端结构。

## 点评
基建型贡献：用受控大规模网格把社区传闻变成可引用证据。强在协议一致；脆弱点在固定 4 s/16 kHz/CE 设定可能偏某些架构，且 ADD23 失败提示语言–领域纠缠。文末截断于 ADD23 警示段，偏差分析细节可能不全。

