# Indigenous Voices in Speech Science and Technology

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Special Session
- Area：14
- 论文数：7

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本特刊把原住民与少数语言语音技术同时放在算法、数据治理与用户体验三条线上。南部班图语声调条件课程学习、Warlpiri 跨语相似度迁移、北萨米半监督伪标签、普什图语 Common Voice，展示低资源 ASR/语料建设的技术路径。

与此同时，ELSI 平台与毛利语 TTS 强调社群主导的数据策展与治理；澳大利亚原住民英语使用者访谈揭示 ASR 迫使使用者“说得像白人”。趋势是：没有社群控制与语言正义，单纯刷低 WER 不足以称为成功的原住民语音科技。

## 论文技术总结

# Tone-Conditioned Curriculum Learning for Low-Resource Bantu Speech Recognition

- 论文编号：2905
- 报告人：Vukosi Marivate
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mokgosi26_interspeech.pdf

## 问题
南部班图语（isiZulu、isiXhosa、Sesotho、Setswana、Tshivenda、Xitsonga）基础 ASR 零样本 WER 常 >100%；声调扩展与短语轮廓编码语法意义，标准正字法常省略声调，通用微调忽视形态–声调难度梯度。

## 方法
混合难度 s(u)=0.7·WER_norm + 0.3·Tonal_norm（WER 来自冻结 Whisper 基线；声调特征：F0 转移率、独特模式、簇数、标准差与范围，Parselmouth，无强制对齐）。门控声调适配器（约 2.1M）按话语声调统计调制编码器输出。三阶段课程（40%→80%→全量，各约 650 步）。在社区语料 Swivuriso 上训 Whisper、W2V-BERT、MMS，匹配测 Swivuriso、迁移测 NCHLT。

## 实验与结果
跨库平均：W2V-BERT Tone-cond. 最佳 WER 28.41%；Whisper Multilingual 29.44%。Nguni 上 W2V-BERT 优于 Whisper 约 3–4 点；Sotho-Tswana 上 Whisper 更好（如 Setswana Tone+Curr. Swivuriso 18.60%）。Xitsonga 迁移：W2V-BERT Tone-cond. 23.79%，相对稳健；Tshivenda 匹配可至 17.23% 但 NCHLT 可升约 20+ 点。课程效果因架构/语言不一；MMS 上纯 WER 课程优于混合。

## 结论
无单一模型适合全部六语；应按语族选架构并跨语料验证。声调门控对 CTC 式 W2V-BERT 更有帮助，课程收益不统一。

## 点评
把班图声调扩散写进难度与适配器，比纯 WER 课程更贴语言事实。强在架构×语族交互与跨库迁移；弱在 α/β 未敏感性分析、社区与录音棚域差仍大，课程有时反而伤个别语言。


# Which Languages Transfer Best to Warlpiri? A Similarity-Based Study for Low-Resource ASR

- 论文编号：1837
- 报告人：Pravina Mylvaganam
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mylvaganam26b_interspeech.pdf

## 问题
澳大利亚原住民语言 Warlpiri 转写语音极少（本文约 1.5 小时、18 说话人），跨语迁移关键，但源语常按语系/地理启发式选取，未必反映声学或语言类型相似度。

## 方法
先用 VoxLingua107 上 ECAPA-TDNN LID 预筛近邻语；再以 ECAPA、wav2vec 2.0、XLSR-53 层间嵌入余弦测声学相似度，并以 WALS/SSWL/PHOIBLE/Grambank 等算句法、音位清单、语法与总体类型距离。Whisper-small：先在各高资源源语微调，再微调 Warlpiri；对照单语、原多语 Whisper/XLSR-53 与最不相似源语。Spearman 相关分析相似度与零样本/微调 WER、CER。

## 实验与结果
近邻含 Assamese、Hindi、Tamil 等，非 Pama–Nyungan、亦非地理邻近；英语/日语声学最远。Assamese 微调最佳：WER 32.6%、CER 12.3%（单语 86.9%/41.3%，多语 Whisper 41.0%/15.1%）。Hindi/Telugu/Tamil 约 37.6–40.7% WER；日语/爪哇语更差。零样本：音位清单与类型相似度相关更强；微调后声学相似度相关最强（ρ_WER≈−0.67）。

## 结论
系统相似度排序可改进 Warlpiri ASR 迁移；声学近邻主导微调收益，音位/类型更解释零样本。语系或地理亲近不是充分标准。

## 点评
把“选谁做源语”做成可检验的相似度–下游链路，对极低资源原住民 ASR 实用。强在多维相似度与相关分析；弱在 Warlpiri 数据仍极短、仅 Whisper-small，且部分语缺完整语言特征。


# From Academic Tool to Community Infrastructure: A Call for Indigenous Partnership in Speech Data Governance

- 论文编号：2489
- 报告人：Kaveri K. Sheth
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sheth26b_interspeech.pdf

## 问题
低资源/原住民语音数据一旦被采集，治理常反映研究者优先而非社区主权。作者团队的 ELSI 平台已托管多语儿童长时录音（含巴布亚新几内亚、墨西哥、玻利维亚、秘鲁、东帝汶、所罗门、瓦努阿图等至少 10 个原住民/小规模社区语料），但原始音频控制权集中于三名欧洲学术托管人，社区无正式否决、知情或用途定义权。

## 方法
描述 ELSI 三角色：Custodian（原始音频与授权）、Tool Creator（训模型）、Analyst（仅派生标注/指标）。对照 CARE（集体利益、控制权威、责任、伦理）与 OCAP（所有/控制/获取/占有）原则制表，说明当前模型在权威与集体利益上未落地。提出增设 Community Custodian 层：否决权、访问日志、许可用途定义、撤回/删除派生输出等，并强调“谁算合法社区托管人”须共设而非由欧方单方指定。发出公开共设邀约并承诺工程落地与设计审查。

## 实验与结果
无 ASR/检测实验。治理映射：集体利益与控制权威“未实施/未操作化”；责任与伦理仅部分（经原始采集者中介、限制访问但无社区标准）。平台功能可用，但作者明确其目前仍是研究者工具。

## 结论
在联合国原住民语言十年早期，平台基础设施选择将长期塑形；作者呼吁与社区组织共设可执行的托管识别与访问控制层，使 ELSI 从学术工具转为社区基础设施。

## 点评
少见地公开解剖自有系统的主权缺口，比空泛原则声明更有行动力。强在角色架构与 CARE 对照、以及共设边界（不代社区定义“谁是社区”）；弱在提案仍待伙伴落地，且跨境存储/法律责任与占有原则之间张力未消解。


# Indigenising Speech Technology: Building a TTS Model for te Reo Māori

- 论文编号：1443
- 报告人：Gianna Leoni
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/leoni26_interspeech.pdf

## 问题
主流 TTS 对毛利语等原住民语言质量差，公开语料常忽视正字/语音特点与说话人多样性；新西兰设备上亦无合适 Māori 或新西兰英语/双语声线。作者主张：精心策展的少量高质量数据可优于“越多越好”。

## 方法
Te Hiku Media 主导的数据主权流程：经 whakawhanaungatanga 获文本授权；内部语言专家人工校句、标长音、切句；族内广播员作男声、再扩女声。录制约男 24 小时（约 11h Māori + 13h 英语）、女 8+ 小时（约 3h Māori + 5h 英语）。质量保证含逐条听审与重录/改文本。训练沿用先前工作：IPA 音素化、借西班牙语预训练（语音相近）、男女微调。自建 90 句 Māori 基准与 100 句双语语码转换基准，由专家听评元音辅音、音高韵律与自然度。

## 实验与结果
无公开 WER/MOS 表；迭代以专家主观对照报告驱动，早期有机械切分感，后期更近母语流畅度；专名与稀有音、数字/缩写仍为难点，靠补录闭环。强调主观、文化恰当评测优于通用基准。

## 结论
原住民主导的策展、同意与部署控制可做出高质 Māori TTS 基础；质量与伦理优先于数据量。

## 点评
把数据主权写进工程全流程，比再刷架构更切原住民语境。强在基准自建与失败模式闭环；弱在定量指标少、模型细节指向前作，外部可复现性有限。


# ‘I have to talk proper white ways’: Australian Aboriginal English Speakers’ Experiences with Voice Technologies

- 论文编号：1595
- 报告人：Celeste Rodríguez Louro
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/louro26_interspeech.pdf

## 问题
澳大利亚原住民英语（Australian Aboriginal English）广泛使用却几乎不被语音技术支持；少数族裔变体上 ASR 失败常引发自我归咎与认同压力，该变体用户体验尚无实证研究。

## 方法
原住民主导质性研究：39 名 16+ 岁原住民/托雷斯海峡岛民（中位年龄 33，逾 25 个 First Nations，Nyungar 居多）半结构访谈（中位 38 分钟，Aboriginal English，RA 主导，IRB + 顾问委员会）。主题分析归纳使用场景与态度。

## 实验与结果
三大发现：(1) ASR 常失败，用户挫败甚至弃用，部分自责“说不清/没文化”；(2) 需支持多样 Aboriginal English（词汇如 dardy、南北口音差异），反对压平身份；(3) 用户将性能与种族关联，称对白人更好，并改说“proper white ways / blackfella way”以被识别，家中亦需语码转换、感到疲惫。

## 结论
语音助手失败是结构性排斥的延伸，把“讲白方式”的压力带入私人空间；技术应支持用户偏好变体，并采用去殖民方法（顾问委员会、原住民 RA 参与解读）。

## 点评
首次系统记录该变体在语音接口上的生活经验，证据直接、伦理设计扎实。强在把挫败连到殖民语言等级而非“口音难”；弱在质性样本与地域集中（西澳为主），未配 ASR 客观 WER 对照。


# Two-stage semi-supervised learning with pseudo-labels: A case study on Northern Sámi ASR

- 论文编号：2497
- 报告人：Priyanshi Pal
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pal26_interspeech.pdf

## 问题
北萨米语标注稀缺；同量监督下小模型弱于大模型。如何用伪标签半监督让轻量 wav2vec2 学生逼近大教师，且兼顾域外泛化。

## 方法
约 75h 未标注议会语音；20h 人工转写监督。教师/学生为 wav2vec2-large/base-sami-22k（22.4k 小时萨米预训练）。伪标签：全量教师输出，或师生 WER<10% 一致过滤得约 28h。策略含 PL-Full、PL-Filtered、等量 capped，及人工+伪标签混合 vs 两阶段微调（先 PL 后 HL 或相反）。单轮伪标签、不用 LM。评议会验证、282utt、YLE 播客、UIT-SME。

## 实验与结果
PL-Full 优于过滤；等量 capped 无增益。混合训练劣于基线；两阶段且先全量伪标签再人工最好（如 282utt CER 6.73 vs 基线 10.09；播客 CER 8.89 vs 11.40）。相对 CER 改进约 3.8–33.3%（摘要）。过滤偏删、全量偏插；伪标签强化常见字符、稀有/借词字符仍弱。

## 结论
单轮伪标签即可提升小模型；顺序关键，宜先伪标签再金标；过滤牺牲多样性未必更好。

## 点评
把“伪标签怎么喂、喂多少、喂顺序”在濒危语上跑清楚，实用。强在域外播客与错误类型分析；弱在未试迭代 PL/增广，且教师系统错误会灌给学生。


# Pashto Common Voice: Building the First Open Speech Corpus for a 60-Million-Speaker Low-Resource Language

- 论文编号：1432
- 报告人：Hanif Rahman
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rahman26_interspeech.pdf

## 问题
普什图语约 6–8 千万使用者，此前几乎无足够规模的开放许可语音语料；八个阿拉伯/波斯键盘缺失辅音常被替换或丢弃，转移学习易失败。

## 方法
2022–2025 在 Mozilla Common Voice 建语料：界面本地化、维基百科抽句过滤、针对 shin/zhe/dze/tse 等音位定向补句、Facebook 教程与无障碍叙事、VOA Pashto 广播动员；双评审验证。跨 CV14–CV23 十个版本。

## 实验与结果
规模：1.5h/5 人 → 147.07h/1483 人；CV17→CV18 说话人约增 108 倍（9→971）。MCV23：107781 clips，60337 已验证（82.33h），13 域；约 39% 仍未审。性别元数据缺失约 98%。Whisper Base 在 MCV20 全微调测试集 WER 13.4%（相对 Fleurs 零样本 99.0%）。

## 结论
开放普什图语料首次达到可全量微调规模；广播社区动员是可迁移的增长杠杆。后续需补审与性别覆盖。

## 点评
贡献是数据基础设施与社区增长动力学，而非新模型。强在可复现方法学与明确基线；弱在读语音 vs 自然语音差距、人口统计残缺，限制公平评测。

