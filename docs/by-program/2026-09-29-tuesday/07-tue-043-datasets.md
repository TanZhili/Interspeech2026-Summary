# Datasets
- 日期：Tuesday 29 September 2026 / 时间：09:00-11:00 / 形式：Oral（Area 12）/ 论文数：6
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本场六篇均为数据资源与基准建设：汉语方言综合基准、俄语表情对话语料、带强度等级的易怒语音库、带自定义词表的财报 ASR 基准、视频会议与面对面多模态群体互动，以及大规模金融财报通话基准。共同取向是补齐“真实场景、细粒度标签、上下文条件、跨设置可比”等学术基准长期缺口。

方言与对话资源强调语言学分区完整性、真方言 vs 带口音普通话连续体，以及对话轮替/表情标签相对朗读语料的优势。情感与服务场景则走向序数强度与时间顺序保留，以支持升级轨迹而非二分类。工业 ASR 侧突出自定义词表与领域元数据：Contextual Earnings-22 与 Earnings25 分别针对上下文条件缺失与金融域大规模评测，并提供可复现基线。

VIP-MINGLE 用被试内配对的面对面与视频会议设置，直接证明多模态行为分布跨设置显著偏移，论证跨设置语料的必要性。

## 技术内容

### 方言、对话与情感强度资源

**GLAD-CSpeech: A Dialectologically Comprehensive Benchmark for Genuine Chinese Dialect Speech**（论文 1128；presenter：Ziyi Cheng）
覆盖 16 个方言分区（8 官话亚区 + 8 非官话大区）、23 个代表点，区分 Genuine Dialect 与 Accented Mandarin，服务 ASR/TTS/DID。含工作室与真实场景录音、方言感知转写与普通话–方言平行文本，并报告基线；非商业研究免费发布。

**Dialogs: a studio-quality expressive conversational Russian speech corpus for dialog assistants**（论文 809；presenter：Ilya Shigabeev）
专业棚录面对面表演对话，立体声分段，含每句 12 类风格/情感标签。众包 MOS 显示音质可懂度可比强俄语棚录基线，表情与会话自然度更高；并用 VITS2 证明可支撑表情对话式 TTS。

**HaessigDB: A Database of Irritable Speech with Intensity Grading**（论文 3304；presenter：Niklas Weller）
客服风格表演片段，人工标注 annoyance / frustration / aggression 三维序数强度，并经迭代得到高一致子集，保留时间顺序。面向服务场景升级信号与轨迹建模，填补强度+时序数据缺口。

### 上下文 ASR、跨设置互动与金融基准

**Contextual Earnings-22: A Speech Recognition Benchmark with Custom Vocabulary in the Wild**（论文 1375；presenter：Berkin Durmus）
假设学术基准饱和主因是缺少对可用性影响大的稀有/自定义词表上下文。基于 Earnings-22 构建开放的 Contextual Earnings-22，为 keyword prompting 与 keyword boosting 设六条强基线。摘要称扩展到商业规模系统时准确率可比且显著提升。

**VIP-MINGLE: A Corpus for Videoconference and In-Person Multimodal Interaction in Group Language Engagement**（论文 2367；presenter：Andrew Chang）
32 组 105 人、约 59 小时，含被试内面对面与视频会议配对；提供音视频、心理测量、处理特征与时间分辨人工标注。分析显示多模态行为跨设置显著偏移，论证跨设置群体对话模型需求。

**Earnings25: A Comprehensive 500-Hour Speech Benchmark for Finance**（论文 2642；presenter：Anshul Wadhawan）
金融域英语财报通话基准：testset-full 约 498 小时全量通话，testset-segmented 为行业均衡的 46 小时片段；提供对齐转写与说话人角色、行业、通话结构等元数据，超越总体 WER。报告 Whisper 与 Parakeet-TDT 可复现基线。

## 本场要点
- 汉语方言基准强调方言学分区全覆盖与真方言/口音连续体控制。
- 对话与易怒语料把表情/强度/时序置于服务与助手场景中心。
- 自定义词表上下文被论证为打通学术–工业 ASR 评测落差的关键。
- 面对面 vs 视频会议需配对跨设置语料，因行为分布会系统性偏移。
- 金融基准同时给规模与结构化元数据，支持说话人/行业感知评价。
- 多篇提供基线系统或听感验证，降低资源即用门槛。

## 覆盖核对
`1128 | GLAD-CSpeech: A Dialectologically Comprehensive Benchmark for Genuine Chinese Dialect Speech`
`809 | Dialogs: a studio-quality expressive conversational Russian speech corpus for dialog assistants`
`3304 | HaessigDB: A Database of Irritable Speech with Intensity Grading`
`1375 | Contextual Earnings-22: A Speech Recognition Benchmark with Custom Vocabulary in the Wild`
`2367 | VIP-MINGLE: A Corpus for Videoconference and In-Person Multimodal Interaction in Group Language Engagement`
`2642 | Earnings25: A Comprehensive 500-Hour Speech Benchmark for Finance`
