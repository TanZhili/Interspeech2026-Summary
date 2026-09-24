# Datasets

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：12
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场六篇均为数据资源与基准建设：汉语方言综合基准、俄语表情对话语料、带强度等级的易怒语音库、带自定义词表的财报 ASR 基准、视频会议与面对面多模态群体互动，以及大规模金融财报通话基准。共同取向是补齐“真实场景、细粒度标签、上下文条件、跨设置可比”等学术基准长期缺口。

方言与对话资源强调语言学分区完整性、真方言 vs 带口音普通话连续体，以及对话轮替/表情标签相对朗读语料的优势。情感与服务场景则走向序数强度与时间顺序保留，以支持升级轨迹而非二分类。工业 ASR 侧突出自定义词表与领域元数据：Contextual Earnings-22 与 Earnings25 分别针对上下文条件缺失与金融域大规模评测，并提供可复现基线。

VIP-MINGLE 用被试内配对的面对面与视频会议设置，直接证明多模态行为分布跨设置显著偏移，论证跨设置语料的必要性。

## 论文技术总结

# GLAD-CSpeech: A Dialectologically Comprehensive Benchmark for Genuine Chinese Dialect Speech

- 论文编号：1128
- 报告人：Ziyi Cheng
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26j_interspeech.pdf

## 问题
中文方言语音资源按行政地理标签易错分（省内多方言、跨省同方言），且真方言与带口音普通话常混杂，缺语言学根据地、覆盖完整、可支撑 ASR/TTS/DID 的统一评测基准。

## 方法
发布 GLAD-CSpeech：按《中国语言地图集》覆盖 16 方言区（8 官话亚区 + 8 非官话大区）、23 代表点；区分 Genuine Dialect 与 Accented Mandarin；>163 小时，ASR 用多样真实场景、TTS 用棚录；每点 6 说话人、ASR/TTS 任务量见表；三层标注含方言感知转写与普通话–方言平行文本。提供 ASR/TTS/DID 基线；非商用免费。

## 实验与结果
零样本 ASR（6 代表点、方言层转写 CER）：Whisper-large-v3 / Qwen3-ASR / Dolphin 总 CER 61.65% / 28.97% / 38.63%；温州、梅县最难，官话点明显易。同点 KeSpeech 上 CER 低得多。Xi’an TTS（GPT-SoVITS 微调 3.93 h）：MOS 3.78、IMOS 3.91、AMOS 3.65。DID：FireRedLID 零样本 Macro F1 72.29%；Dolphin-FT 达 99.08%。

## 结论
语言学分区 + 真方言/口音普通话对照的多任务基准，能暴露非官话方言上的脆性和行政标签 DID 的迁移差；高纯度标注可补偿数据量做方言 TTS 适配。

## 点评
贡献在数据与分类学：用方言学标签替代省界标签，并显式拆开“口音 vs 真方言”。ASR 用方言层转写评测避免与普通话归一化混淆，诊断更诚实；点位按人口/影响力抽样，未必覆盖最濒危变体。


# Dialogs: a studio-quality expressive conversational Russian speech corpus for dialog assistants

- 论文编号：809
- 报告人：Ilya Shigabeev
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shigabeev26_interspeech.pdf

## 问题
俄语缺同时具备棚录质量、对话风格与句级情感/风格标注的公开语料；现有资源多为单人朗读或非受控网络数据，难训对话向表达 TTS。

## 方法
Dialogs：3 名演员面对面棚录 20.6 小时、11796 句、44.1 kHz 立体声；脚本作提示可即兴；12 类风格/情感众包标注；划分 19.9/0.30/0.37 小时。众包 MOS 对标 Ruslan、Natasha。用 VITS2 在训练集上训 615k 步作可行性验证。OpenRAIL 许可。

## 实验与结果
语料 MOS：Overall 4.15，表达力 4.11、对话自然度 4.08，显著高于 Ruslan/Natasha 的表达与对话维，音质/可懂度相当。VITS2 合成 Overall 2.83、表达 2.56、对话 2.59、UTMOS 3.36；单人时长不均（4.4–9.9 h）限制绝对质量，适合与更大数据混合。

## 结论
填补俄语棚录对话表达语料空白，可支撑表达/对话式 TTS 训练与评测；局限为表演式非完全自发、无叠语与噪声、说话人时长不平衡。

## 点评
定位清晰：用专业表演对话换可控标注与棚录质量。众包 MOS 维度设计贴合对话助手；单语料 VITS2 分数偏低符合数据量预期，价值在风格分布而非单独刷榜。


# HaessigDB: A Database of Irritable Speech with Intensity Grading

- 论文编号：3304
- 报告人：Niklas Weller
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/weller26_interspeech.pdf

## 问题
客服语音机器人需按烦躁强度与时间轨迹做升级转接，但常用情感语料（Emo-DB、IEMOCAP 等）缺服务场景、序数强度与对话时间演化；二分类难以支撑早期干预。

## 方法
HaessigDB：合成银行客服脚本（客户逐渐烦躁）由 4 名英语演员棚录；切成约 3.91 s 句级片段；Prolific 众包对 annoyance/frustration/aggression 打 1–10 分。按维度迭代剔除低一致性项至 Krippendorff α≥0.80，得高一致子集。公开 Zenodo/Hugging Face。

## 实验与结果
原始有效片段 1068；高一致子集 annoyance/frustration/aggression 为 553/537/516；内外连接合并 250/832。轨迹显示前约 10 片段三维度平均上升。现成 HF 情感分类器在阈值扫描下召回曲线平坦，难分辨中间强度；LoRA 微调 HuBERT/XLSR 做攻击强度回归：MAE 1.502/1.333，Pearson r=0.607/0.710（80/20 非说话人分离划分）。

## 结论
提供带序数强度与时间顺序的烦躁语音资源，可支持分级检测与升级策略；初步证明预训练编码器可适配强度回归。

## 点评
把“烦躁=可升级的序数轨迹”做成数据规格，贴合客服场景。高一致子集与失败模式分析有用；局限为表演式合成脚本、微调划分未说话人分离，外推需谨慎。


# Contextual Earnings-22: A Speech Recognition Benchmark with Custom Vocabulary in the Wild

- 论文编号：1375
- 报告人：Berkin Durmus
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/munyampirwa26_interspeech.pdf

## 问题
学术 ASR 榜 WER 近饱和，但工业场景中人名/公司/产品等自定义词错误往往决定可用性；缺标准化的、带真实语境词表与干扰项的公开评测。

## 方法
基于 Earnings-22：LLM 抽人/公司/产品词，按词切 15 s 片段，wav2vec 对齐并人工校对（约 29.5% 片段改词）。提供 local（仅本段词）与 global（整通电话词表含干扰）两种语境。评测 WER + 关键词 Precision/Recall/F。基线含 Deepgram、OpenAI Whisper API、AssemblyAI、Whisper OSS、CTC-WS、Parakeet+CTC-WS。测试 630 样本。

## 实验与结果
给语境普遍抬升关键词 F，WER 变化因系统而异（有的变差，存在幻觉/重复等伪影）。local 比 global 更容易；提示与 boosting 两路线均可显著改善自定义词，规模系统与学术 boosting 均有收益。强调关键词指标与 WER 互补。

## 结论
公开 Contextual Earnings-22 为自定义词 ASR 提供可复现基准，暴露“WER 相近但关键词差距大”的现象，并对比 prompting vs boosting。

## 点评
问题卡在“可用性 = 稀有实体”，评测设计（local/global）贴近部署。人工校对提升可信度；规模仍相对小（55 源文件），且部分商用 API 版本随时间变化需锁定。


# VIP-MINGLE: A Corpus for Videoconference and In-Person Multimodal Interaction in Group Language Engagement

- 论文编号：2367
- 报告人：Andrew Chang
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chang26f_interspeech.pdf

## 问题
多人会话模型多在面对面语料上训练，视频会议会重构轮替与非言语行为；缺同一被试组跨两种介质、可对照的多模态公开数据，难分离介质效应与任务/说话人混淆。

## 方法
VIP-MINGLE：32 组、105 人、约 59 小时；组内完成面对面与 Zoom 两场（顺序平衡），任务为 Family Feud 式协作问答。提供原始音视频、心理测量、说话人分离、Whisper 转写、OpenFace/DeepFace 特征与人工时间标注。DOI 发布。

## 实验与结果
配对比较：视频会议轮替间隙更长（β=0.113,p=.037）、话语更短（β=−0.094,p<.001）；语言句法复杂度与面部 AU/表情亦有系统性偏移（视频会议整体表情更弱但部分局部增强）。结论为质变式行为分布偏移而非单纯降质。

## 结论
被试内跨设置多模态语料可量化域偏移，支撑跨介质稳健的群组会话模型。

## 点评
设计核心是 within-subject 对照，比拼凑不同视频会议语料更干净。特征管线开箱可用；样本以大学生为主、任务偏游戏化，外推到职场会议需谨慎。


# Earnings25: A Comprehensive 500-Hour Speech Benchmark for Finance

- 论文编号：2642
- 报告人：Anshul Wadhawan
- 程序：Tuesday 29 September 2026 / Datasets
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jiang26f_interspeech.pdf

## 问题
财报电话会议含行话、数字、口音、重叠与角色切换，通用 ASR 易域偏移；现有金融语音资源或偏训练规模、或缺行业均衡与说话人角色等元数据，难做可复现细粒度评测。

## 方法
Earnings25：testset-full 498 小时 S&P 500 英语完整电话（2025 Q4）；testset-segmented 46 小时、290 段（每行业一段，5–10 分钟，自 2025 全年美股池分层抽样）。CTC 强制对齐、过滤操作员套话，提供转写与行业/说话人等元数据。基线 Whisper base/medium/large-v2 与 Parakeet-TDT-0.6B-v2，报告多种归一化 WER。

## 实验与结果
testset-full 上 Parakeet WER 0.108、WER-N-nc-np 0.061；Whisper-large-v2 约 0.140/0.080。segmented 集类似。行业级显示 Biotech/Pharma 等更高错误。支持说话人角色与行业感知分析。

## 结论
提供近期、元数据丰富、行业均衡的金融 ASR 评测基准，补全长格式与分段两种协议。

## 点评
相对 Earnings-21/22，强调行业分层与角色元数据，评测更“能诊断”。体量接近“~500h 全量测试”对计算要求高；segmented 子集更适合常规迭代。无外部 LM 的基线设定清晰可复现。

