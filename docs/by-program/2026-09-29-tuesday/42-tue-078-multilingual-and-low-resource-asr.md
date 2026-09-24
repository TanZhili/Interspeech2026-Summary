# Multilingual & Low-Resource ASR

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：8
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场聚焦南亚/印度语族与方言场景下的多语低资源 ASR：专用越南语自监督预训练、南亚语错误解剖、印地/马拉雅拉姆复杂度分层基准、统一梯度投影持续学习、希腊方言课程多任务，以及印度 22 种表列语言的忠实评测基准。

共同问题是：标准微调常改善朗读却损害自发语音；主导语言偏置导致灾难遗忘；WER 被正字/Unicode 变异夸大。对策包括向量量化预训练、转写后处理、学习率时机与课程顺序、语言均衡回放投影，以及允许多合法转写的评测格。趋势是“诊断基准 + 训练动力学 + 语言均衡优化”三位一体。

## 论文技术总结

# ViP-VL: Vietnamese Self-supervised Speech Pretraining Model with Vector-Quantization Learning

- 论文编号：1077
- 报告人：Kiet Anh Hoang
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/le26b_interspeech.pdf

## 问题
越南语标注稀缺，需要公开、可部署的 SSL；既有 wav2vec2-Vi 延迟高，大规模工作权重未公开。BEST-RQ 搭配 8× 下采样易因 mask 与编码器不同步而掉点。

## 方法
ViP-VL：BEST-RQ + ChunkFormer，78M 参数，8× 时间下采样。用声学堆叠（15 帧窗、步长 8，拼接优于平均）与感受野对齐同步 mask 流形；在 10 ms filterbank 上先 mask，再按“至少 80% 组成帧被 mask”判定下采样帧是否 mask，有效时间 mask 约 45%。在约 17,000 小时无标注越南语上预训练。下游：ASR（VLSP 等）、情感（ViSEC）、方言（ViMD）、说话人验证（VoxVietnam）。

## 实验与结果
LibriSpeech 验证：ViP-VL 平均 WER 9.7，优于未对齐的 8× BEST-RQ（11.9），对齐 2× 量级。越南 ASR 平均 WER 13.76，优于 Wav2vec2-Large-Vi（17.89）与 PhoWhisper-Large（14.09）等（同范式比较）。SER UA 74.45%；方言区域/省级 F1 93.24% / 57.17%。低资源 ASR 曲线显示预训练相对从零训练优势随标注减少而增大。权重与实现开源。

## 结论
在高压缩 SSL 中，mask–下采样同步与感受野对齐和数据规模同等重要；按此训出的公开 ViP-VL 在多项越南语任务上达 SOTA 级表现。

## 点评
把“8× 掉点”归因到同步错误并用堆叠/阈值 mask 修掉，比一味堆数据更有方法贡献。公开权重填补社区缺口。与用远更大数据/监督的系统对比时需注意设定差异；省级方言仍难，说明细粒度变体仍是瓶颈。


# Dissecting ASR Failures in Low-Resource South Asian Languages

- 论文编号：1382
- 报告人：Agha Ali Raza
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/azeemi26_interspeech.pdf

## 问题
Urdu、Punjabi、Pashto、Sindhi 使用相近 Perso-Arabic / Gurmukhi 脚本、正字法不统一且命名实体常跨脚本出现，现有多语 ASR 多只报聚合 WER，难以区分声学识别失败、脚本解码错误与评测伪影。

## 方法
在 Common Voice 22.0 与 FLEURS 上零样本评测 Whisper-medium / large-v3、MMS-1b、SeamlessM4T-Medium / Large（共 40 配置）。用 jiwer 计算 WER/CER，事后按 11 类错误 taxonomy 分解：脚本混淆、编辑操作、重复循环、数字、正字变体、字符混淆、命名实体、Latin 词、OOV/稀有词、时长、跨语言污染等。实体由 LLM 标注；并对 Whisper 错误脚本输出做音译后处理，对 Perso-Arabic 做 Unicode 归一化后再算 WER。

## 实验与结果
SeamlessM4T-Large 在 8 组中 6 组最优（Urdu FLEURS 16.3%、Punjabi 22.1%）；MMS 在 Sindhi 两集最好。Whisper 在 Punjabi/Pashto/Sindhi 上大量错脚本，WER 常超 100%；音译后处理可回收至多约 25 个百分点 WER。Unicode 归一化平均降低 Pashto WER 3.1 点。稀有词准确率约 20–62%；短句 WER 高于长句；Sindhi 输出中 12–35% 字符来自其他语言（多为 Urdu）。

## 结论
聚合 WER 系统性误判南亚低资源 ASR 失败性质：脚本混淆、Unicode/正字歧义与跨语干扰是主因；语言适配架构更稳，生产级仍远未达到。局限包括 Sindhi CV 仅 40 句、仅零样本未微调。

## 点评
把“听错了”与“写错脚本/评测过严”拆开，对多脚本低资源族很有诊断价值；音译与归一化是低成本可落地的补丁。弱在测试集方言信息缺失、Sindhi 样本极少，且未验证微调后失败模式是否仍以脚本为主。


# Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition

- 论文编号：3408
- 报告人：Kavya Manohar
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/juvekar26_interspeech.pdf

## 问题
Whisper 等对印地语族微调常在朗读/录音棚语料上变好，却在自发口语上显著退化（studio-bias）；常见保守学习率与 easy-to-hard 课程未必适合低资源音系适应。

## 方法
构建 Vividh-ASR：按声学复杂度分 Tier A（studio）、B（broadcast）、C（spontaneous）、D（合成噪声，仅评测），覆盖 Hindi 与 Malayalam，聚合 Kathbath、Shrutilipi、IndicVoices、FLEURS 等。用 2×2 因子实验解耦学习率时机（递减 vs 递增）与课程方向（easy→hard vs hard→easy）。据此提出 R-MFT：Stage1 自发语高 LR（2e−4）→ Stage2 广播（1e−4）→ Stage3 A+C 混合巩固（1e−5）。并用 CKA、SVD、EMD 等分析 encoder/decoder 表征变化。

## 实验与结果
早期高 LR 是主因：Malayalam 上递减相对递增约有 12–13 点全局 WER 优势；hard-to-easy（R-MFT）再额外改善 Malayalam（39.35% vs Standard MFT 42.25%），Hindi 两课程均收敛约 18.8%。R-MFT Medium 全局 WER：Mal 39.36%、Hi 18.82%；244M Small 达 44.41%/21.41%，优于保守低 LR 的 769M。表征上成功配方主要改动 decoder，encoder CKA≈1；IndicWhisper 则扰动 encoder（CKA 0.775）并扩大有效秩。

## 结论
适应效率由更新时机与复杂度排序共同决定；R-MFT 使小模型在自发 Indic ASR 上可比甚至超过常规大模型微调。后续拟扩展语言与选择性冻结 encoder。

## 点评
把“数据不够”转为“优化轨迹不对”，用分层基准钉住 studio-bias，对法庭听写等真实场景有针对性。强在因子设计与表征证据一致；弱在语言仅两种、Tier D 为合成噪声，且与 IndicWhisper 训练分布不完全可比，因果解释需谨慎。


# Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR

- 论文编号：1915
- 报告人：Wei-Qiang Zhang
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ren26g_interspeech.pdf

## 问题
对 Whisper 等做低资源多语序贯微调易灾难性遗忘；A-GEM 等梯度投影在重放缓冲语言不平衡时会被主导语言偏置，低资源语言更易被覆盖。

## 方法
提出 Unified Gradient Projection（UGP）：每步从各历史语言均匀采样构造语言均衡参考梯度 g_ref；若当前梯度与 g_ref 内积为负则投影到其正交补。同时与 Experience Replay 结合，混合 batch 上做 L_cur + λ L_replay（λ=1）。中大型 Whisper 冻结 encoder 只训 decoder/embedding；small 全参微调。

## 实验与结果
主场景（FLEURS）：目标 Malay/Indonesian/Filipino/Javanese/Māori，重放 Thai/Vietnamese/English/French。Whisper-large-v3 上 UGP：TWER 12.91、RWER 6.68、AWER 9.80、FWER 0.04（近零遗忘）；FT 的 FWER 在 medium 可达 89.80。消融显示投影与 ER 互补：单独投影 FWER 4.20，完整 UGP 达 0.04。扩展语组与 50h→5h 数据尺度上，UGP 持续压低遗忘并保持较好 AWER。收敛后梯度余弦更近正交，冲突弱于 FT。

## 结论
语言均衡梯度投影加 ER 可在多语低资源持续学习中兼顾可塑性与稳定性，大模型上遗忘近零。作者认为这为通用语音识别的持续适配提供高效路径。

## 点评
抓住多语重放里“参考梯度被大语绑架”这一具体失效点，比笼统加正则更对准问题。强在跨尺度与稀缺数据验证；弱在主实验语言组与缓冲语言固定、数据尺度分析仅在 small，对更长任务序列是否仍稳需另证。


# Beyond Standard Greek: Adapting Whisper for Greek Dialects through Curriculum Multitask Learning

- 论文编号：2567
- 报告人：Vassilis Katsouros
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/klimi26_interspeech.pdf

## 问题
希腊方言相对标准现代希腊语（SMG）存在明显“方言税”：零样本 WER 常极高，普通微调仍大幅落后 SMG；多任务与课程学习各自有效，但少有按监督类型做跨任务/跨域递进的适配。

## 方法
四阶段 staged multitask curriculum：Stage0 仅希腊→英语音译（G_ST）；Stage1 以 α 混 SMG ASR 与方言 ST；Stage2 以 β 混方言 ASR 与方言 ST；Stage3 纯方言 ASR。任务提示动态注入 decoder。实验方言为 Cypriot、Cretan、Messenian；donor 用 GPC-5h；英译由 Llama-Krikri 生成并人工校对。评测 Whisper-small/medium/large-v3，encoder 冻结、卷积特征可训。

## 实验与结果
Curriculum 在各方言与规模上均优于零样本与常规 FT。例如 Cypriot small：ZS 81.27 → FT 52.38 → Curr. 35.61；large-v3 Curr. 24.89。Cretan/Messenian 同样有一致降幅。α/β 比例模型相关：small 上 0.5/0.5 最好（33.56）。去掉翻译监督的 ASR-only 课程全面变差（small 上可差超 12 点 WER）；极低资源 Messenian 上缺少 GPC donor 也更易受损。

## 结论
沿任务（翻译→ASR）与领域（SMG→方言）递进可减轻分布失配、稳定低资源方言适配，一致优于朴素微调。后续拟考察语言距离、参数高效适配与更难接触方言。

## 点评
把 donor 语、音译辅助与课程调度串成对角线路径，对“有近亲高资源语但方言标注极少”的场景很实用。强在三方言多尺度与消融完整；弱在部分方言时长极短（如 Messenian 预处理后约 37 分钟）、英译依赖 LLM+人工，推广到接触型北方方言仍待验证。


# Vimarsha: Faithful ASR Evaluation for Indian Languages with Demographic Diversity, In-the-Wild Audio and Spelling Variations

- 论文编号：3348
- 报告人：Kaushal Bhogale
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bhogale26b_interspeech.pdf

## 问题
印度语 ASR 评测存在双向失真：干净受控语料带来乐观偏差；单一刚性参考又因拼写/语码混写变体惩罚合法输出，带来悲观偏差。缺少同时覆盖真实声学难度与多合法转写的基准。

## 方法
构建约 100 小时 Vimarsha，覆盖 22 种法定印度语言：Controlled On-Field（COF，43.3h，356 区、约 5099 说话人，朗读/即兴/电话对话）与 In-the-Wild（IW，56.1h）。IW 经多模型 CER 分歧与 BEATs 声学标签筛选难样本。用多 ASR 假设对齐并经 133 名标注员校验，构建 lattice of variations；以 OIWER（相对 lattice 最优路径）评测 10 个系统（IndicConformer、Saaras、Sarvam Audio、AWS/Azure/AssemblyAI/ElevenLabs/GPT-4o/Deepgram/Gemini 等）。

## 实验与结果
各模型在 IW 上均退化：领先系统由约 10–15% 升至 27–34% 平均 WER；AWS 相对增幅最大，GPT-4o 在 IW 近崩溃（约 89，个别语可达 150+）。I-Conf 两 split 领先且人口统计敏感度低（<2 点）；对话场景整体最难。地区 WER 跨度大（如 Bharuch 4.6 vs Koppal 54.9）。短句与极慢语速显著抬高 OIWER；Mantra/Choir 等事件普遍难，儿童喊叫等事件模型间分歧极大。

## 结论
真实声学与拼写容差会改变模型排名与部署判断；COF 不足以代表上线就绪。作者开源基准、协议与结果，以推动更贴近印度语言可变性的 ASR。

## 点评
同时纠正“测太易”与“判太严”，用 COF/IW 与 lattice/OIWER 形成完整评测叙事，对 Indic 选型很有用。强在覆盖 22 语与地理切片；弱在 IW 难样本筛选依赖现有 ASR/标签器，可能偏向特定失败模式，且部分语言时长偏短。

