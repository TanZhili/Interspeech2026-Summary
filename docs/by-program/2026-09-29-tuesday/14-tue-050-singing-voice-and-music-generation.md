# Singing Voice and Music Generation

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
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

本场聚焦歌声编辑/合成/转换、歌曲统一生成，以及面向中文传统音乐与戏曲的数据与基线建设，并并行关注唱假检测与感知驱动重建。方法上，flow matching / rectified flow / 扩散与多模态 DiT 成为主流生成骨架；控制目标从音色克隆扩展到旋律保持、时长预算、歌词改写、伴奏协同与风格一致美化。无手动对齐的旋律引导与固定预算时长分配，是歌词编辑类任务的共同难点。

数据与评测侧，SingFox 覆盖多语与多轨假唱检测，CTMusic、YOAT/粤剧基准与 LyricEditBench 分别补齐中国传统器乐文生乐、粤剧 SVS 与旋律保持歌词编辑评测。另有工作用感知加权、相位相关与谱监督改进音乐 VAE 重建，以支撑后续大规模生成。整体趋势是：可控歌声生成与统一多任务框架并行推进，同时用领域数据集与假唱评测补齐安全与文化多样性缺口。

## 论文技术总结

# MeloDISinger: Melody-Aware & Duration-Preserving Singing Voice Editing with Audio Infilling

- 论文编号：3285
- 报告人：Yoonjeong Park
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26k_interspeech.pdf

## 问题
文本驱动歌声编辑需改歌词同时严格保持总时长与旋律以对齐伴奏；既有方法或隐式控制无法硬性保时长，或复用原音素时长导致替换不自然，且常整段重生成破坏未编辑区。

## 方法
MeloDISinger：MeloDRP 在固定编辑跨度预算下预测时长比（span 内 softmax 归一），融合音素信息与伪 MIDI（由 F0 导出）经交叉注意，并用音素–音符时间重叠引导注意；FPIP 预测编辑区 F0；flow-matching mel 解码器只在编辑掩码区域做 infilling，未编辑帧原样保留。另用 WhisperX+LLM（含音节容量约束）生成可评估的编辑歌词。

## 实验与结果
GTSinger-En（13 h，三歌手）。相对 EditSinger、Vevo2：各编辑场景（替换/插入/删除/混合）DDUR≈0、DC≈99.93%，WER/CER 与 FPC 多数最优；主观 Lyric/Melody/Naturalness MOS 亦全面领先。消融去掉时长预算条件降幅最大，去旋律条件损害节奏相关编辑。

## 结论
时长比预测 + 旋律感知 + 掩码 infilling，可在保总时长与未编辑区的前提下做旋律一致的歌词编辑，并达 SOTA 主客观表现。

## 点评
把 SVE 的硬约束（跨度预算）直接写进时长建模，比事后裁剪更干净；伪 MIDI 交叉注意缓解“像说话的时长”。评测流水线本身也是贡献，但数据规模偏小、场景由 LLM 生成，真实制作流水线的编辑分布可能更杂。


# SingFox: A Multi-Lingual Singfake Detection Corpus

- 论文编号：2573
- 报告人：Arth J. Shah
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shah26_interspeech.pdf

## 问题
现有 singfake 数据多偏英语、生成范式单一，缺少多语、替代假唱（假人声+真伴奏）与源追踪设定；语音反欺诈模型难迁移到含节奏/旋律的歌声伪造检测。

## 方法
构建 SingFox：20 语种（14 国际+6 印度）、113,802 片段、约 126.32 小时、1150 歌手；六轨 T1–T6 分别覆盖全球语、Indic、乐器类、合集、替代假、源验证。真唱来自开放资源，假唱由 GAN（HiFi-GAN/BigVGAN/UnivNet）、扩散（DiffSinger/DiffRhythm）、VC（RVC/So-VITS-SVC）、TTM（MusicGen）等生成；4 s 切片、峰值+RMS 归一、不做源分离。约 30% 子集用部分生成器训练，其余含未见生成器测试。

## 实验与结果
LFCC+ResNet 等声学特征与 SSL 基线；跨数据集时 FMC 训练在 SingFox T4 上准确率最高达 77.84%，CtrSVDD/WildSVDD 训练迁移较差。T5 替代假上 LFCC+ResNet 准确率可低至 45.13%。源追踪上 LFCC 准确率 89.06%。生成器侧 BigVGAN/RVC 极难检（准确率约 1%），UnivNet 相对易检（71.17%）。人类 MOS：假唱约 3.47，真唱约 4.03。

## 结论
提供多语、多范式、含替代假与源追踪的 singfake 评测资源，暴露现有检测器在跨语/跨生成器与混合真假伴奏上的脆弱性。

## 点评
贡献是基准与威胁面设计，而非新检测器；T5/T6 特别贴近真实攻击（假声真伴、可解释溯源）。正文注明为高度压缩版、细节在 arXiv，部分表与结论表述略乱，使用时需对照完整版协议。


# Singing Voice Conversion via Shared Speaker Space and Min-Pooling Adversarially Enhanced Flow Matching

- 论文编号：2090
- 报告人：Hao Huang
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hu26g_interspeech.pdf

## 问题
SVC 中内容–音色解耦与重建质量常冲突：VQ 等显式解耦易丢细节或漏源音色；KNN 映射到共享歌手空间可去音色，但帧级拼接不连续，且 flow matching 易糊高次谐波。

## 方法
MinFlow-SVC：WavLM 特征经 content encoder，用指定共享歌手特征池做 KNN 对齐训练（Lknn）；对 encoder 输出做 min-pooling 对抗（盯最差连续性格子）平滑不连续。目标 Mel 由 OT-CFM 在内容、目标音色、F0 条件下生成；再以动态谐波掩码（DHM）+ min-pooling 对抗强化谐波区。先训 encoder 再冻住训向量场，HiFi-GAN 声码。

## 实验与结果
M4Singer 训练，OpenSinger 6 人零样本评测。说话人分类：原 WavLM 95%，转共享空间后 98%（表明源音色被抹掉）。MinFlow-SVC-10：NMOS 3.83、SMOS 2.65、F0CORR 0.948、MOSNet 4.26，整体优于 So-Vits-SVC、DiffSVC、NeuCoSVC；消融去 content encoder 损 SMOS，去 Lmin-pooling/Ladv-harm/DHM 均降自然度或 F0 相关。

## 结论
共享空间 KNN 去音色 + 双阶段 min-pooling 对抗（特征连续与谐波感知）可缓解解耦–质量权衡，零样本转换主观/客观更优。

## 点评
用共享说话人空间替代码本，解耦更“硬”；min-pooling 专门打最差局部，贴合歌声瞬态/谐波瑕疵。依赖选定共享歌手与 KNN 匹配质量，共享池覆盖不足时可能引入内容失真。


# YingMusic-Singer: Controllable Singing Voice Synthesis with Flexible Lyric Manipulation and Annotation-free Melody Guidance

- 论文编号：1547
- 报告人：Chunbo Hao
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hao26_interspeech.pdf

## 问题
改歌词保旋律的歌声编辑：上下文掩码法控制弱，商业 SVS 需手标 MIDI/时长；Vevo2 虽免对齐但可懂度与旋律贴合不足，SoulX 仍要字级时间戳。

## 方法
YingMusic-Singer：Stable Audio 式 VAE + MIDI 提取器中间表征作旋律、IPA 句级对齐歌词、DiT-CFM。课程：TTS 预训练 → 歌声 SFT（先无旋律再开旋律+CKA）→ GRPO（多奖励、组内相对优势）。输入为可选音色参考、旋律歌声片段、修改歌词，无需手标对齐。并提出 LyricEditBench（GTSinger 衍生，六类编辑×中英，7200 例）。

## 实验与结果
相对 Vevo2，跨六类任务在 PER、F0-CORR、Vocal Score 上全面更优（尤其翻译/语码混合）；主观 N-MOS/M-MOS 亦更高。消融：SFT Phase2 抬高 F0 但损 PER，GRPO 同时拉回 PER 并再提 F0/VS；去 CKA 略损旋律，去旋律扰动会导致模型“抄”旋律潜变量语义而 intelligibility 崩塌。

## 结论
免标注对齐的扩散课程+GRPO 可同时强化歌词忠实与旋律保持，并给出首个系统评测基准 LyricEditBench。

## 点评
问题设定贴产品（只给旋律片段+新词），CKA 与 GRPO 正面处理歌词–旋律权衡。单阶段 CFM 在 SIM 上不如 Vevo2 多阶段，但作者明确优先可懂度与旋律；大规模内部歌声数据与奖励模型细节对复现仍敏感。


# CTMusic: A Traditional Chinese Instrumental Music Dataset Towards Text-to-Music Generation

- 论文编号：882
- 报告人：Haotian Guo
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26l_interspeech.pdf

## 问题
文本到音乐模型训练数据高度偏西方流行/电子，非西方仅约 5.7% 时长；缺少面向传统中国器乐的文本–音频配对资源，限制风格生成。

## 方法
构建 CTMusic：741 对、约 42.7 小时；独奏 601（12 种乐器）、合奏 140。来源为数字专辑与 Bilibili 等，机筛+人工去短于 20 s/人声/噪声，裁剪≤400 s、44.1 kHz、−14 LUFS。三位民乐专业背景标注者按三段模板写描述，合奏文本经 DeepSeek 释义增强。验证：在 CTMusic 上两阶段（独奏→合奏）LoRA 微调 Stable Audio Open，并提出 SA-TTT（每四块插入门控 TTT 层）。

## 实验与结果
相对预训练 SA，SA-LoRA 在独奏/合奏测试上 FD、KL、CLAP 与主观 OVL/TA 全面提升；SA-TTT 进一步最好（如 stage1 FDopenl3 156.77、CLAP 0.38；stage2 137.49、0.51）。预训练模型对国乐生成能力明显不足，凸显专用数据必要。

## 结论
首个面向文本生成传统中国器乐的配对数据集，并证明 LoRA/TTT 适配可显著改善风格与文本对齐。

## 点评
核心贡献是数据与文化域适配，TTT 是增强而非全新生成范式。规模相对西方大数据仍小，合奏子集尤其有限；标注依赖专家模板，扩展自动标注质量是作者自述的下一步。


# SRF-SVB: Style-Consistent Singing Voice Beautifying via Rectified Flow

- 论文编号：615
- 报告人：Wenhui Li
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26h_interspeech.pdf

## 问题
歌声美化需改正业余音高/节奏并提质，同时保歌词与原唱歌手风格；现有 APC 多只改音高，NSVB 依赖难采集的平行录音，扩散式方法质量–效率难兼顾，过度“专业化”易抹掉个人音色与表达。

## 方法
SRF-SVB：解耦音高（RMVPE）、内容（Conformer PPG）、音色（CAM++）；训练时对 Mel 连续掩码（α=0.5）做 DiT 参数化的 rectified flow 填补，损失只算掩码区。推理：业余段作上下文 Mel，专业音高+DTW 对齐内容作生成条件，音色仍取自业余；Euler 10 步，NSF-HiFiGAN 声码。

## 实验与结果
约 160 h 中英歌声训练；英测 617、中测 874 业余–专业对。RPA：英/中 0.57/0.50（业余 0.40/0.22）；SECS 0.85/0.82，显著高于 NSVB（0.58/0.40）；MOS-Q/S 英 3.91/4.47，中 3.62/4.06，风格相似领先。连续 α=0.5 掩码优于更小比例或随机碎片掩码。英测 CER 略高于仅改音高的 Diff-Pitcher。

## 结论
首个基于 rectified flow 的风格一致 SVB，可高效同时校正音高节奏并保住业余歌手个性；生成重构偶发影响发音清晰度。

## 点评
用上下文 Mel 填补把“风格一致”写成训练–推理同构的 inpainting，比事后音色约束更直接。相对 NSVB 不再强依赖平行训练对是实用优势；CER 代价说明生成式美化仍可能碰歌词保真，实时场景还需压采样步数。


# Towards Unified Song Generation and Singing Voice Conversion with Accompaniment Co-Generation

- 论文编号：481
- 报告人：Ziyu Zhang
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26e_interspeech.pdf

## 问题
歌曲生成与 SVC 长期割裂：前者缺细粒度零样本音色克隆，后者忽视人声–伴奏协同；两者输入模态与优化目标冲突，朴素多任务易梯度对抗。

## 方法
UniSinger：多模态编码器（Qwen2.5 指令、Zipformer 音素、HuBERT+VQ 语义、CAM++ 说话人、自训 VAE 44.1 kHz 潜变量）接入 MM-DiT flow matching。四阶段课程用任务特异模态掩码：纯文本歌曲 → 纯 SVC → 说话人克隆歌曲 → 指令条件下伴奏协同 SVC。跨任务说话人空间先在 SVC 中纯化再迁移到歌曲生成。

## 实验与结果
约 20k+5k 小时内部歌曲。歌曲生成：PER 19.61%、Spk-Sim 68.85%，多项 SongEval 领先 DiffRhythm+/YuE 等。SVC：PER 0.151、Spk-Sim 0.712；带伴奏变体 Harmony MOS 3.891。消融去任务掩码、去 SVC 阶段或去歌曲阶段均显著损伤对应任务。

## 结论
统一框架首次同时支持说话人克隆歌曲生成与伴奏协同 SVC，课程掩码化解冲突并带来任务互惠。

## 点评
核心是用模态掩码课程把异构任务接到同一潜空间，并把 SVC 学到的说话人表征转给歌曲生成。强在伴奏协同与可懂度；主观音质仍受野外数据伪影制约，相对超大规模 YuE 在相似/质量上未必全面领先。


# Towards Chinese Yue Opera Singing Voice Synthesis: A Benchmark with Dataset, Data Augmentation and Baseline Model

- 论文编号：131
- 报告人：Peng Bai
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bai26_interspeech.pdf

## 问题
中国戏曲 SVS 资源稀缺，越剧（吴语）此前无专用数据集与基准；专业演员少、电子谱缺失、自动对齐难、源分离差，导致低资源困境。

## 方法
构建 YOAT：专业小生演员工作室干声约 1.35 h，切分为 565 句（均约 8.61 s），人工音素/时长+Parselmouth 音高对齐。增强：DA1 约 1 h 念白；DA2 字典拼接念白至 8 h；DA3 混入 4.5 h 歌仔戏对齐数据。基线 YueOpera-Singer：Transformer 编码器 + 乐谱时长扩展 + OT-CFM U-Net 解码，HiFi-GAN 声码。

## 实验与结果
543/22 训练测试划分。YueOpera-Singer-10：F0 RMSE 0.2133、MOS-N 3.92，优于 FFT-Singer、DiffSinger、FT-GAN，参数与显存更省。DA3 最有效（F0 RMSE 0.1834、MOS-N 4.01）；DA2 随规模提升发音 MOS；DA1 主要提发音、对 F0 帮助有限。

## 结论
给出越剧 SVS 首个数据集–增强–基线基准，MOS 约 3.92，为吴语戏曲合成提供可复现起点。

## 点评
贡献在文化低资源的数据与标注管线，而非架构创新；CFM 基线质量–效率均衡。单歌手、短时长限制泛化，跨剧种音高迁移（DA3）比同语念白更有效，提示“节奏–音高结构相似”比发音同域更关键。


# Back to Ear: Perceptually Driven High Fidelity Music Reconstruction

- 论文编号：219
- 报告人：Kangdi Wang
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26d_interspeech.pdf

## 问题
开源音频 VAE 常忽视听觉感知，相位与立体声空间重建差，导致瞬态抹糊与声像不准，难作专业级音乐重建前端。

## 方法
ear-VAE：卷积编码器 + 解码端 Transformer（RoPE）瓶颈；MS-STFT 判别器。损失含多尺度对数幅度、特征匹配、LS-GAN、弱 KL；提出相位相关损失（仅 LR）；重建前加 K-weighting；幅度在 MSLR 全通道监督、相位相关仅用 LR。两阶段训练：公开数据预训练 + 约 1 万小时内部高质量音乐继续训练。

## 实验与结果
相对 DAC、EnCodec、AGC、SAO，在 MuChin 与内部验证上 Mel/STFT 距离、ICPC/CCPC、SI-SDR、dbTP 与 MOS（4.70）全面领先。消融：相关损失、去 CQT 判别、K-weighting、Transformer 块均逐步抬升 SI-SDR；仅 M/S 相位监督反而有害。

## 结论
感知加权、相位相关与 MSLR 分流监督使开源音乐重建 VAE 达更优保真，尤其高频谐波与空间特性。

## 点评
把混音工程里的 K 计权与相关表思路写进重建目标，比单纯加大模型更对症。部分优势来自内部后训练数据，与纯开源基线对比需留意；作者也指出细微空间效果仍可能被衰减。

