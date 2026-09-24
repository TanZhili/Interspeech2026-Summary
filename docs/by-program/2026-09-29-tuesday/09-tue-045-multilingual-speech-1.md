# Multilingual Speech 1

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Long - Oral
- Area：
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

跨领域长论文场从政策–治理框架、大规模合成多语语音问答数据，到社区驱动低资源 ASR 数据集、尼日利亚多语口语语料，再到同声传译的流畅度优化与时延指标元评测。技术与社会维度并置：谁的声音被机器识别，如何低成本扩展语种覆盖，以及实时翻译如何在低时延与自然语流间取舍。

数据与基准建设是主轴：MULTISPEECHQA / BENCH、南阿塞拜疆社区数据与 GoldSet、WazobiaSpeech 的自发口语与元数据。治理论文则提出 3M 伤害分类与参与式审计协议，把识别失败重新解释为隐含语言政策。同传侧 NaturalFlow 用模型内部信号减少块间静音；时延元评测揭示分割相关结构偏差，并提出 YAAL / LongYAAL 与 SOFTSEGMENTER。

瓶颈包括多语语音指令数据稀缺、阿拉伯文字歧义与删除型解码错误、脚本/自发比例、以及短时延追求导致的不自然停顿与指标不一致。

## 论文技术总结

# Decolonizing Linguistic Policies in Automatic Speech Recognition: A Framework for Cross-Culturally Competent Speech AI

- 论文编号：3351
- 报告人：Jay L. Cunningham
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cunningham26_interspeech.pdf

## 问题
ASR 与语音界面已介导公共服务、医疗与教育，但对低资源、原住民与非标准变体的持续失败常被当作技术误差；作者认为这些失败是隐式“语言政策”，通过数据、指标与模型先验再生产殖民式语言等级，使部分声音在机器侧不可读。

## 方法
本文不提新 ASR 架构或基准数字，而是提出人文评估框架。理论综合语言资本、种族语言学意识形态、语言政策研究与去殖民计算，给出七层情境化模型（语言→民族国家→地域→族群语言→社会语言意识形态→社会公正关联→社会技术后果）。引入 Three Harms（3M）：Misrecognition、Misalignment、Mistrust；将训练数据策展、WER 等指标、LM 先验与部署回退行为诊断为 policy sites；并提出参与式框架与最低审计协议（评估者角色、采样、指标、标注与裁决），主张受影响社区作为共设计者、评估者与治理伙伴。另建议在 WER/CER 之外补充 Tone Error Rate（TER）、click 辅音专项错误率与社区加权伤害分。

## 实验与结果
全文为理论与框架论文，无自建模型实验。正文举例说明政策效应，如标准美式英语 WER 约 5% 而非裔美式英语约 35%、界面支持巴黎法语但不支持塞内加尔法语等；并讨论 WER 对声调语言（如约鲁巴）与 click 辅音语言的失效。抽取文本在“语言政策三层次：数据策展…”处截断，后续参与式框架细则与协议条款未完整可见。

## 结论
作者主张把 ASR 设计选择视为可审计的语言政策，用 3M 与七层模型定位伤害，用社区参与与最小审计协议推动文化胜任的语音 AI；目标是补足 WER 中心评估对文化情境伤害的欠规范。边界在于这是评估/治理框架而非系统性能提升方案。

## 点评
抓的是“谁的口音被算作合法输入”这一制度层问题，而不是再刷多语 WER。强处是把数据菜单、参考转写、回退到英语等工程细节明确标成政策位点，并要求声调/click 等语言学敏感指标。弱处是可操作性依赖社区资源与组织成本，且全文抽取截断，审计协议落地细节不完整；若不与具体系统审计绑定，易停留在概念层。


# Turning Speech Language Models into Multilingual Listeners

- 论文编号：2584
- 报告人：Tolúlọpẹ́ Ògúnrẹ̀mí
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ogunremi26_interspeech.pdf

## 问题
开源 Speech Language Models（SLMs）多偏向英语及少数高资源语，根因是多语语音指令微调数据稀缺；现有 SLM 评测也几乎只有英语上的复杂生成任务，难以衡量多语听–答能力。

## 方法
基于英文 Voice Assistant 400K，用 SeamlessM4T v2 Large 译到 Aya Expanse 覆盖的 22 种目标语，再用 XTTS（15 语）、SeamlessM4T 或 MMS TTS（其余）合成问题语音，得到 MULTISPEECHQA：约 1080 万 spoken QA、9200 小时、23 种类型多样语言；人工评自然度平均约 3.0、内容理解约 4.1。测试集中每语 200 条经 Prolific 人工校对（约 72% 需改），并与 CommonVoice ASR、CoVoST-2 AST 拼成 MULTISPEECH-BENCH。评测用 Command-A / GPT-4o 作 LLM-as-a-judge 的成对偏好；级联基线为 Whisper Large v3 + Aya Expanse 8B。随后对 Qwen2.5-Omni 做 LoRA（rank 32）约 3 epoch 微调。

## 实验与结果
开源 SLM 中 Qwen2.5-Omni 最强，但多数在未见语上弱于 Whisper+Aya 级联；闭源中 GPT-Audio 领先，Gemini 2.5 Pro 次之，Flash Lite 未过级联。Qwen2.5-Omni 平均 ASR 错误率 49.7、BLEU 22.7、chrF 46.6，AST 可超级联。人机法官一致性：相对级联，Qwen2.5-Omni 约 75.6% 一致（κ=0.186），GPT-Audio 约 52.4%。微调后相对原 Qwen2.5-Omni 在 23 语上平均胜率约 60.6%，希伯来/希腊/波斯等更多打平；ASR WER 49.7→50.4、AST BLEU 22.7→21.0，核心识别/翻译基本不变。抽取文本在“训练数据配比如何影响 SLM”一节开头截断。

## 结论
高质量合成多语指令数据是廉价扩展 SLM 多语能力的路径；MULTISPEECHQA 微调显著抬升口语 QA，且不明显伤 ASR/AST。作者公开数据、基准与权重以服务更多语言使用者。

## 点评
核心假设是“有可用 MT+TTS 就能合成够用的指令数据”，用级联强基线压开源端到端模型，再证明 LoRA 微调主要补生成式听答而非刷 WER。强处是语言覆盖与人工校对评测子集；脆弱处在合成自然度偏低、LLM 法官 κ 低、以及希伯来等低 TTS 质量语上收益有限——多语听懂仍受合成链路质量上限约束。


# Preserving the Iranian Turkic Language: Community-Driven ASR Datasets and Benchmarking for South Azerbaijani

- 论文编号：1516
- 报告人：Jalil Nourmohammadi Khiarak
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/farsi26_interspeech.pdf

## 问题
南阿塞拜疆语（South Azerbaijani, AZB）使用阿拉伯文正字法，母语者逾 1500 万，却几乎没有公开标注语音数据；与北阿塞拜疆语（拉丁文）听感相近但正字法迥异，预训练 ASR 与标准化基准均缺失，严重制约低资源 ASR。

## 方法
构建三套社区驱动数据：（1）Community：从阿拉伯文书籍切句并规范化（数字/符号展开、去标点、统一 Unicode 等），14 名母语者（7F/7M）手机朗读，约 1.3 万句、超 25 小时；（2）External：由北阿塞拜疆语音（BHOSAI 伪标签库与 VoxLingua107）经 Whisper-large-v3 伪标后，由出版方语言专家转写/校对为阿拉伯文南阿塞拜疆正字法，约 25 万句、447.64 小时量级；（3）AZB ASR GoldSet：独立社区采集的更具挑战评测集，约 3021 句、17.49 小时。基准模型含 MMS-1B（唯一预训练含 AZB）及 Whisper Tiny/Base/Small 及其波斯/阿语/土耳其语/北阿塞拜疆语微调后再在 Community 上微调等共八套设定。

## 实验与结果
正文报告：全量数据训练整体更好；语言特定微调对极低资源设定关键；跨语微调有时优于仅在 Community 上微调的 Whisper-Small。Community 微调的 MMS 在 GoldSet 上最好，但在 External 上仍有限；MMS 的 CER 低于 Whisper，作者归因于非自回归与无显式自回归 LM。错误分析指出阿拉伯文音位/正字歧义、极短句不稳与数字转写是主因。抽取文本在 GoldSet 提示设计描述处截断，完整数值表与更多实验细节未见。

## 结论
作者发布首批公开南阿塞拜疆语大规模 ASR 数据、八模型基准与错误分析，并视社区采集—微调—系统评测流程为其他低资源语的可复用蓝图。边界是 External 声学仍来自北变体、正字法靠人工转写对齐。

## 点评
做法抓住“同族语有数据、目标语缺阿拉伯文对齐标注”这一脚本鸿沟，用伪标+专家转写扩规模、再用社区金标与 GoldSet 压测。比单纯爬取更稳；脆弱点是声学–正字法错配、书读风格与 GoldSet 自发风格差距，以及全文截断导致无法核对具体 WER/CER 数字。


# WazobiaSpeech: A Large-Scale Multilingual Speech Corpus for Robust and Fair ASR in Four Nigerian Languages

- 论文编号：3519
- 报告人：Ife Adebara
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/adebara26_interspeech.pdf

## 问题
非洲语言在大规模语音资源中系统缺位；现有语料多为朗读/脚本、人口统计标注弱、治理不足，自发语音（韵律、不流畅、方言、语码转换）尤其稀缺，限制真实场景 ASR 鲁棒性与公平性评估。

## 方法
发布 WazobiaSpeech：豪萨语、伊博语、Naijá（尼日利亚皮钦）、约鲁巴语共约 2540.8 小时、2865 说话人；约 4% 为脚本朗读以补词汇/领域，其余以自发为主。领域覆盖农业、医疗、商业、日常会话；用文本/图像/视听多模态提示诱发；Yorùbá/Igbo 全自发，Hausa/Naijá 各约 50 小时朗读。元数据含年龄段、性别、教育、领域、模态。双层音质控制（约 40 dB SNR、48 kHz 等 + 母语人工审）；母语者按规范转写，标记 [um]/[?]/[cs]。说话人级分层划分 train≈85%、dev/dev-test/test 各≈5%。另描述多语种音系与伦理知情同意、本地转写治理。

## 实验与结果
正文宣称提供跨语基线 ASR、错误分析与约鲁巴声调敏感性细粒度评估，但抽取文本在质量保障“words-per-second”自动化检查处截断，具体 WER/CER、跨语对比与声调实验结果未能读到。规模对比表中 WazobiaSpeech 约 2500 小时、4 语、2500+ 说话人，相对 NaijaVoices（1867h/3 语）等强调多领域多风格自发。

## 结论
作者将 WazobiaSpeech 定位为以自发语音与丰富元数据支撑稳健、公平非洲语 ASR/TTS 的公开资源，并强调伦理与参与式采集。后续实验结论因文本截断无法确认。

## 点评
工作重心在“真实非洲语境下的自发多语语料+治理”，而不只是再堆小时数；领域 taxonomy、说话人分层防泄漏与转写标签设计都指向可做公平与声调分析。主要风险是抽取截断导致基线数字缺失，点评只能基于数据设计：脚本比例低有利于鲁棒性，但录音设备与场景变异大，质量与标注一致性将决定下游是否真能支撑 fair ASR 结论。


# NaturalFlow: Reducing Disruptive Pauses for Natural Speech Flow in Simultaneous Speech-to-Speech Translation

- 论文编号：540
- 报告人：Dongwook Lee
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26c_interspeech.pdf

## 问题
同声 speech-to-speech translation（Simul-S2ST）为压低延迟常按块释放译文，造成频繁停顿与破碎语流，增加听者认知负荷；现有研究多优化质量–延迟（BLEU vs lag），较少直接优化停顿驱动的声学流畅度。

## 方法
在 Hibiki（Mimi codec、同步预测目标语音与对齐文本）上引入 NaturalFlow：用 Direct Preference Optimization（DPO）对齐流畅偏好。偏好数据：CVSS-C 短句 1 万条 + mTEDx Fr→En 拼接长段 6 千条；每源采样 k=32 候选；用 Whisper-medium ASR+BLEU 量翻译质量，Silero VAD 算 silence ratio（静音时长/起止间总时长）。Silver-Medal Preference：按静音比五等分，取第二档（20–40%）为 chosen，避免最上档过激降静音导致语义崩坏；chosen 相对 rejected 需满足 BLEU 差≥5、静音比差≥组内归一化 15%。DPO 只优化声学条件下的文本流策略（直接优化音频 token 不稳定）。

## 实验与结果
Fr→En：CVSS-C / VoxPopuli / Audio-NTREX / mTEDx。NaturalFlow 相对 Hibiki 降低静音比（如长表 Audio-NTREX SR 0.17→0.13，mTEDx 0.26→0.21；短表 VoxPopuli 0.12→0.10），同时保持接近的 LAAL/起止偏移与 ASR-BLEU/COMET（如 mTEDx ASR-BLEU 33.27 vs Hibiki 32.94）。相对 StreamSpeech/Seamless，在长音频上静音与延迟更可控。正文称人工偏好听感更自然；抽取文本在 text-guided DPO 公式处截断，训练细节与人评完整表未见。

## 结论
通过银牌档偏好与大间隔约束，可在不明显牺牲翻译质量与延迟的前提下压低块间静音，使同声 S2ST 更接近连贯语流。边界是优化绕开直接音频 token、且依赖 ASR-BLEU 代理质量。

## 点评
问题抓的是同声系统“为等上下文而停”的用户体验，而不是再压 LAAL。Silver-Medal 有意避开最优静音档，是对 DPO 过优化的工程防护。脆弱处：静音比依赖 VAD 阈值、质量用 ASR-BLEU 代理可能误伤韵律/专名，且全文截断使人评与消融证据不完整。


# Better Late Than Never: Meta-Evaluation of Latency Metrics for Simultaneous Speech-to-Text Translation

- 论文编号：575
- 报告人：Peter Polák
- 程序：Tuesday 29 September 2026 / Multilingual Speech 1
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/polak26_interspeech.pdf

## 问题
同声语音翻译（SimulST）需权衡质量与延迟，但现有延迟指标（AP、AL、LAAL、DAL、ATD 等）常给出不一致系统排序（如 IWSLT 2023）；短音频人为预切分与尾词（tail words）处理引入结构性偏差，长音频无切分时对齐工具又不可靠，导致评测难支持公平比较。

## 方法
对 IWSLT 等共享任务系统做跨语对、短/长形式的指标元评估。分析指出短形式模拟器在段结束后瞬时吐出剩余译文，使含尾词的指标（AP/DAL/ATD）与用 cutoff τ 的 AL/LAAL 均偏。提出 YAAL：cutoff 改为 τ_YAAL=max{i|d_i<|X|}，只计入严格早于源段结束的词。长形式提出 SOFTSEGMENTER（小写分词、禁止对齐到未来段、标点约束、字符相似软对齐，并保留延迟）与 LongYAAL（计入跨段但排除整条流结束后的尾词）。另定义对齐源词时间戳的 True Latency 作参照，并给出检测“大部分译文在输入结束后才出”的退化行为诊断。工具收入 OmniSTEval。

## 实验与结果
短形式覆盖 IWSLT 22/23 与 MuST-C tst-COMMON 多语对（EN→DE/JA/ZH 等）；长形式用 IWSLT 2025 日志与 ACL 60/60 等（含 CS→EN）。表 1 给出过滤退化系统前后的系统数。正文强调 YAAL/LongYAAL + SOFTSEGMENTER 相对常用指标与 MWERSegmenter 更可靠；抽取文本在成对 Score Difference 元评设定处截断，具体相关/排序一致率数字未见。

## 结论
延迟指标不一致主因是切分与尾词带来的结构性偏差而非仅均匀词长等假设；YAAL/LongYAAL 与更好的重切分可更稳健评估短/长同声系统，并应用退化诊断避免误导性低延迟。

## 点评
工作做的是评测基建而非新翻译模型：把“段结束瞬间免费吐尾词”标成偏差源，再改 cutoff 定义。强处是与 True Latency 对齐的元评思路和长音频软对齐；脆弱处是 True Latency 本身依赖优质转写与词对齐，低资源语难用，且全文截断使定量优势证据不完整。

