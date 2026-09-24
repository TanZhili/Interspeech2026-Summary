# Multilingual, Cross-lingual & Low-Resource ASR

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：8
- 论文数：11

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场围绕多语/低资源 ASR 的表征对齐、参数高效迁移与领域数据稀缺展开。一类工作在 Speech LLM / 多语 SSL 之上设计渐进或对齐感知的继续预训练，避免过早把各语言压入共享空间或把声—符对齐全部推到微调阶段；另一类用 LoRA/MoE-LoRA、供体语言选择与双层优化，在冻结主干前提下实现跨语适配。领域场景覆盖空管、中亚长尾语言、拉脱维亚医学听写、达罗毗荼语族、非正式波斯语、希腊歌词转写与声调语强制对齐。

数据侧手段包括声学属性仿真与口音可控合成、聚类级预训平衡与域感知采样、LLM 驱动的格式化整理与伪标校正，以及非正式语体新建语料。模型诊断则指向 Whisper 解码器自注意力与交叉注意力失衡、词长与词表稀疏导致的替换错误等。整体趋势是：对齐与路由成为多语 SLM/ASR 的核心工程点，合成与 LLM 后处理成为低资源领域的常规补数策略。

## 论文技术总结

# PART: Progressive Alignment Representation Training for Multilingual Speech-To-Text with LLMs

- 论文编号：1734
- 报告人：Pei Zhang
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26aa_interspeech.pdf

## 问题
多语 SLM 常冻住 LLM、混训多语多任务，易把各语音频表示压到共享空间，损失细粒度语言差异，且任务级对齐粗糙。

## 方法
PART 三阶段：① 仅训 adapter 做语内 ASR 粗对齐；② 渐进解冻编码器（先末 8 层再全量）+adapter，仍仅 ASR；③ 解冻 LLM，联合 ASR+S2TT。SenseVoice-large 编码器 + Qwen2.5（1.5B/7B）→ PART-2B/8B。数据：ASR 810k h（10 语）、S2TT 434k h。

## 实验与结果
FLEURS/Common Voice：PART-2B 平均 WER 4.7/7.4，优于同规模 Baseline-2stage（6.4/9.2）与 Whisper-large-v3；PART-8B 更优。CoVoST2 xx→en：PART-8B 平均 BLEU 39.1。消融显示去 ASR→S2TT 分阶段、去 LLM LoRA、去渐进解冻均降点；梯度相似分析显示语内对齐增强且跨语边界仍可区分。

## 结论
分阶段语内再跨语、任务依赖启用 LLM，可在保留语言特异性的同时提升多语 ASR 与翻译。

## 点评
抓住“过早混语混任务导致表示坍缩”的训练病，用进度表强迫先学语内映射再借 LLM 跨语。强在同数据预算对比清晰；大规模商购数据细节不可复现，方法迁移价值大于具体分数。


# Alignment-Aware Continued Pre-training for Multilingual Speech Representation Learning

- 论文编号：1185
- 报告人：Xuyang Wang
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lu26b_interspeech.pdf

## 问题
多语 SSL 基座常直接监督微调做 ASR，声学–符号对齐全压到微调阶段；异质文字与长尾语种下跨语泛化受限。

## 方法
在 MMS 300M 上插入对齐感知继续预训练：联合 SSL（对比+多样性）与 CTC，并对上下文/量化表示做随机替换使 CTC 梯度可进量化路径。比较建模单元 Char / IPA / Uroman；提出语言感知双码本（全局+语种特异，加性融合）缓解离散空间竞争。其后仍 CTC 微调。

## 实验与结果
FLEURS：Direct FT 47.2 WER → Continual SSL 43.4 → Joint(Uroman) 36.6；双码本再降至 35.5。Uroman 优于 Char 的 WER，Char CER 略优；IPA 因 G2P 覆盖/噪声在跨语上更差。MLS→FLEURS 未见语上 Uroman 更稳。

## 结论
对齐感知联合 SSL–CTC 继续预训练显著优于直接微调或纯 SSL 继续预训练；统一罗马化与双码本有助跨文书共享与长尾公平。

## 点评
把“符号对齐”前移到表示塑造阶段，比只换微调配方更治本。Uroman 实用折中 IPA 的资源依赖；双码本设计贴合长尾竞争，但语种码本规模与维护成本在更大规模上仍待验证。


# Synthetic Audio Generation Framework for Air Traffic Control Speech Recognition

- 论文编号：2422
- 报告人：Zhe Zhang
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bagat26_interspeech.pdf

## 问题
ATC 语音噪声大、L2 口音重、真实标注稀缺，通用 ASR 退化；传统增强难覆盖口音/说话人多样性，L1→L2 口音转换尤缺。

## 方法
合成管线：先分离语音/噪声并 AudioSR 超分，再经 F5-TTS、kNN-VC、TokAN 式 L2→L1，以及重用 TokAN 的可控 L1→L2（微调 token 转换与 token-to-Mel，条件目标口音）；最后 AAS（8 kHz 重采样、200 Hz 高通、注入原句噪声）。L1→L2 幻觉用 Whisper WER>50% 过滤。下游微调 Whisper-small，4 折交叉验证 ATCO2 约 4 h。

## 实验与结果
OOB Whisper 63.32% WER；仅真实微调 22.69%。仅合成中 VC+AAS 最佳约 24.18%。真实+合成时 L1→L2 AC 最优达 21.64%，显著优于仅真实；L2→L1 混训反而变差（25.92%）。AAS 对 TTS 等增益很大；口音多样性比单纯说话人多样性更关键。

## 结论
面向 ATC 的生成式增强（含可控 L1→L2）能在极少真实数据下提升识别，真实+L1→L2 合成优于仅真实微调。

## 点评
问题抓的是 ATC 的“信道+口音”双缺口，把 L1→L2 当多样性源而非归一化预处理。评测严谨（配对手测）；合成过滤丢约 35% 样本，且数据量仍小，扩展到更大 ASR 与细粒度流利度控制是自然下一步。


# GigaAM Multilingual: Foundation Model for Underrepresented Languages

- 论文编号：2483
- 报告人：Andrei Kuzmenko
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kuzmenko26_interspeech.pdf

## 问题
多语 ASR 在中亚长尾语（哈/吉/乌）上因数据极度偏斜表现差；朴素上采样易伤头语种，需可迁移的预训练与微调采样策略。

## 方法
GigaAM Multilingual：600M Conformer，HuBERT 式掩码单元预测，在约 2M 小时音频上预训练。用语言共现图聚类得 5 簇，簇级重加权（最终 E2 提高中亚簇权重）。微调 CTC 共享字符表，数据含开源/众包/弱监督/合成；域感知采样避免合成子集主导。

## 实验与结果
哈/吉/乌在 CV、FLEURS、内部野外集上大幅优于 Whisper-large-v3、Seamless M4T、Omnilingual 1B。匹配 CTC 微调下，即便 240M 变体平均 WER 亦优于 Whisper/Omni。簇重加权 E2 改善目标语且俄语几乎不变；域感知采样尤其抬升内部自发语。极低覆盖巴什基尔/格鲁吉亚适配亦最优。

## 结论
簇级预训练平衡 + 域感知微调是长尾多语 ASR 的有效配方，并开源编码器与 ASR 模型。

## 点评
贡献在数据混合与采样工程，而非新目标函数；受控编码器对比说明“预训练分布匹配目标语族”比盲目用更大通用编码器更重要。合成/弱标签过滤细节决定可复现性。


# Low-Resource Medical ASR for Rich Transcription in Latvian

- 论文编号：3469
- 报告人：Arturs Znotins
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/znotins26_interspeech.pdf

## 问题
拉脱维亚语医学口述需富文本转写（标点、缩写、数字、单位、术语），域数据仅数十小时；通用模型 WER 可从个位数升至 12–46%，规则 ITN 难维护。

## 方法
对比端到端富文本微调（Whisper/Canary/Gemma-3n）与“逐字 ASR + LLM 格式化”。用 Gemini 将遗留逐字稿与人工报告配对生成格式化标注，并扩 75 h LLM 校正伪标签（WER>15% 丢弃）。指标含 WER、标点/命令/数字/医学实体错误率。训练：先通用拉脱维亚再 LVMED。

## 实验与结果
通用基线极差；ft-whisper-large-v3 达 11.1% WER，加伪标签 10.6%；双阶段 Whisper+ft-gemma3-12b 约 11.2%，标点命令最好（PC-ER 2.1%）。跳过通用语适应或仅有通用数据均更差。学习曲线显示数据少时 LLM 管线更优，数据充足时两端到端接近。

## 结论
有限域数据 + LLM 策展/伪标可使低资源医学富文本 ASR 达可用质量；端到端与 ASR+LLM 在足够域数据下竞争力相当。

## 点评
实用路线是“活化遗留逐字语料 + 伪标扩量”，指标设计贴临床格式需求。临床幻觉风险作者自承；依赖已有人工报告做策展，无报告场景需更多人工核验。


# Probing LoRA-to-LoRA Cross-Lingual Transfer for Unseen Low-Resource Conditions in Whisper-Based ASR

- 论文编号：1133
- 报告人：Spandan Dey
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mondal26_interspeech.pdf

## 问题
低资源 ASR 中，先前 LoRA-to-LoRA 迁移多针对 Whisper 预训练已覆盖的语种；对基座几乎未见、零样本 WER≈100% 的真正低资源语，捐赠语选择与迁移是否仍有效尚未知。

## 方法
两阶段捐赠选择：先限同语系，再在候选中最小化 Jensen–Shannon 正字法（词元分布）散度。在 Whisper-small 上先训捐赠语 LoRA（r=32，Q/V/Out/FFN），再以其权重初始化接收语 LoRA。捐赠：Hindi/Marathi/Bengali（IndicVoices）；接收：Bhojpuri Rural Woman、Konkani、Assamese（40–100 h）。

## 实验与结果
捐赠初始化相对仅接收语 LoRA 一致更优，相对增益约 9–17%（Hindi→Bhojpuri 40 h 达 17%）。JS 选中的捐赠优于同文字其他候选。零样本极高 WER 确认属未见设定，增益主要来自结构对齐而非强预训练先验。

## 结论
即便捐赠与接收均弱覆盖预训练，基于谱系+正字法相似度的 LoRA-to-LoRA 仍可提供更优优化起点，适合参数高效扩展低资源语。

## 点评
把“未见语”从高资源锚点迁移中拆出，并用可测正字法散度替代启发式配对，方法清晰可复用。绝对 WER 仍偏高（方言/数据少/仅 LoRA），贡献在相对迁移而非刷榜。


# Overcoming Decoder Inconsistencies in Whisper for Dravidian and Low-Resource Languages

- 论文编号：1007
- 报告人：Kumud Tripathi
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kumar26c_interspeech.pdf

## 问题
Whisper 在达罗毗荼语上 WER 显著高于印度-雅利安语；语料分析显示更长词、更高 TTR、更低重复，错误多为已知词内字符替换，解码器自注意与交叉注意失衡。

## 方法
在 Whisper-medium 解码器每层加轻量 Weighted-Attention（门控调节自/交叉注意）；在倒数第二层做 Self-Conditioning，把中间预测投影回加到隐状态并辅 CE。形态切分仅作分析工具。Kathbath 八语评测，并外推到韩语、斯瓦希里语。

## 实验与结果
基线平均 WER 19.79，形态切分后 17.18。Weighted-Attention / Self-Conditioning / 组合在 MS 设定下平均再降约 1.5–1.65 点，马来雅拉姆等增益更大。韩语 3.34→2.51、斯瓦希里 16.07→14.58。参数增幅 <1%，推理延迟增 <2%。

## 结论
面向黏着语形态稀疏的解码器条件化可稳定降低字符级替换错误，并泛化到非印度黏着语。

## 点评
诊断（已知词内替换）与改动（平衡声学/语言注意、反馈中间预测）对症。形态切分提示问题本质，但主贡献是训练期解码器改造；增益幅度中等，强在轻量与跨语一致。


# The Impact of Informal Persian Speech on Low-Resource ASR and Speech Translation

- 论文编号：2454
- 报告人：Hadi Alizadeh
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/alizadeh26_interspeech.pdf

## 问题
波斯语正式/口语差异大，公开数据多正式朗读，非正式自发语音导致声学–文本错配，ASR/ST 在真实对话上严重退化。

## 方法
构建 T-PID：影视中单人片段人工转写非正式波斯语，ChatGPT-4o mini 译英并抽样质检（改写 WER≈4%），最终 36.77 h、22,443 句、性别均衡。针对性文本规范化并开源 Persian normalizer。微调 Whisper-small/medium 与 Wav2Vec2-BERT；级联 NLLB-200 做 ST。

## 实验与结果
基线 Whisper 在 T-PID 上因幻觉 WER 极高（200+/360+）；微调后 small/medium 约 37.5/36.3，Wav2Vec2-BERT 29.1，且 Common Voice/FLEURS 正式集也提升。级联 ST：微调后 T-PID BLEU 最高 25.30（Wav2Vec2-BERT+微调 NLLB）。T-PID 困惑度远高于正式集，解释困难度。

## 结论
高质量非正式波斯语可显著改善低资源 ASR/ST，并增强对正式域的泛化；数据集与规范化工具已公开。

## 点评
贡献在填补“口语对齐转录+平行英文”空白，而非新架构。音频优先、转写贴口语利于 CTC；翻译依赖 LLM 抽样质检，成语/文化表达仍可能有噪声。


# BELLA: Efficient Bilevel Learning with LoRA for Multilingual ASR

- 论文编号：2771
- 报告人：Xiaodong Cui
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/saif26_interspeech.pdf

## 问题
编码器–LLM 多语 ASR 中共享解码器易交叉语干扰；路由专家依赖桥接对齐质量，对齐与预测双向耦合，朴素联合训练难兼顾。

## 方法
BELLA：Whisper 编码器 + 可训桥（Q-Former）+ 冻结 Qwen2.5-7B；解码器 MoE-LoRA（共享适配器+K 专家）由路由按桥输出与语言嵌入选专家。双层优化：下层最小化嵌入回归+KD+权重衰减（对齐），上层最小化 ASR NLL+负载均衡/熵（预测）；单环惩罚梯度交替更新，避免昂贵内层求解。

## 实验与结果
CoVoST2 五语（英/西/俄/葡/瑞典）。相对 bridge-only、单 LoRA、按语固定多 LoRA，BELLA 多数语种最低或接近最优 WER；相对基座相对降约 2–4%。专家选择图显示语种特化、未坍缩。ML 在部分高资源语略优但需显式语种选适配器，扩展性较差。

## 结论
用双层学习显式分离对齐与语种特化，可在参数高效条件下缓解多语干扰并稳定路由。

## 点评
把“桥对齐 ↔ 路由选专家”的耦合写成双层问题，比简单多 LoRA 更有结构。实验语种偏高/中资源；相对按语固定 ML 的优势更多在可扩展路由而非绝对分数。


# Automatic Lyric Transcription for Greek Songs: Scaling and Task Composition Effects in Whisper Adaptation

- 论文编号：1371
- 报告人：Dimitrios Damianos
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/frangiadaki26_interspeech.pdf

## 问题
歌词转写（ALT）因旋律、节奏与伴奏比语音难，希腊语此前无系统 ALT 基准；Whisper 零样本在歌声上退化严重。

## 方法
从 GAD 策展 GAD-ALT：Demucs 分离人声、CTC 强制对齐、gpt-4o-mini 段级英译，17,458 段约 19.65 h，按歌划分。对比 Whisper Small/Medium/Large-v3：仅转写、2:1/4:1 转写–翻译多任务、两阶段（先冻编码器在 Common Voice 希腊语上适应解码器，再全开歌声微调）。

## 实验与结果
零样本 WER 92.3/65.1/53.6；最佳为 Large-v3 两阶段 27.2%。小模型受益于多任务正则（Small 2:1→33.6%），大模型更适合专注转写/两阶段。人声干声优于混音；人工增强/混音训练反而变差。错误类型含语义替换、边界漂移、幻觉、正字歧义等。

## 结论
建立希腊 ALT 首个基准；规模与任务组成交互明确，两阶段+大模型最有效。

## 点评
贡献在低资源 ALT 管线与受控消融，揭示“多任务主要帮小模型”。歌声–语音域差仍主导错误结构；阶段一用朗读稿可能声学上仍远歌声，作者已提示可换更富韵律中间域。


# CrossPhon-Tonal: Streamlining Cross-language Modeling for Forced Alignment in Low-resource Tonal Languages

- 论文编号：1770
- 报告人：Hongchen Wu
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wu26e_interspeech.pdf

## 问题
跨语强制对齐（CLFA）对声调语常忽略声调或依赖专家手工映射；忽略声调损害边界，手工又慢且难复现。

## 方法
CrossPhon-Tonal：在 CrossPhon 发音特征坐标映射音段后，对 Chao 调号做自动声调映射——先同轮廓类，再最小化首末音高水平差，并列时取更近音高；凹/凸无同类则回退首半轮廓。输出中间词典供目标语声学模型对齐。评测普通话、粤语、泰语、越南语、豪萨语、克罗地亚语。

## 实验与结果
相对语言专属基线的边界一致率（0.025 s）上，自动映射与专家映射总体相当，部分对（如泰模型对齐普通话 0.772 vs 专家 0.726）更优。声调模型常优于 3600 h Global English（如泰→普通话 0.772 vs 英 0.638）。小数据映射目标（如克罗地亚）与家族差异大时效果不均。

## 结论
自动声调编码可去掉专家瓶颈，且声调特异性往往比单纯数据规模更关键。

## 点评
把声调当“类附加符号”接进既有音段管线，工程可扩展。质量依赖源/目标词典与目标模型小时数；非声调强模型在印欧对上仍可胜，说明音系相似度与声调并非唯一因素。

