# Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
- 形式：Special Session
- Area：14
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本特邀专场把太平洋原住民语言的语音科学、文档化与技术适配放在同一议程。技术侧关注低资源基础模型持续适配中的表征漂移与可塑性—稳定性两难、大规模语种识别拓扑中浮现的“太平洋宏观簇”，以及马克萨斯语等真实转写数据上的微调、跨波利尼西亚迁移与“ASR 是否真正节省文档化时间”的人因实验。语言科学侧则用感知—声学—标注三角测量可接受发音范围，并报告法属波利尼西亚多种语言塞音 VOT、毛利语塞—元音协同发音等基线描写。

社区治理与合作治理同样是主线：巴布亚新几内亚 Hula 社区自建众包平台 Vavanagi、毛利语 TTS 的机构—企业合作案例，以及首个毛利语情感语音库 Pā-Kakare（16 类社区定义情感）。另有工作半自动采集库克群岛毛利语语速的社会语音学变异。整体上，本场强调技术必须与社区治理、文化相关评测与扎实语音描写同步推进，而非单向“低资源微调”。

## 论文技术总结

# Continual Adaptation for Pacific Indigenous Speech Recognition

- 论文编号：2215
- 报告人：Ting Dang
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xiao26_interspeech.pdf

## 问题
太平洋原住民语言低资源且与预训练分布远；全量微调可能灾难性遗忘。多数低资源 ASR 只报最终 WER，不问适应是否引发大规模表征漂移与顺序学习中的稳定–塑性困境。

## 方法
新整理 PARADISEC 语料：Bislama（13.75h）、Nafsan（14.83h）、Lelepa（3.55h），共约 32h。以 Whisper-Small 做：(1) 不同数据量下 Full FT vs LoRA（encoder+decoder）跨语适应；(2) 层间余弦距离测适应前后表征漂移；(3) 顺序学习 Nafsan→Lelepa，并比较 DoRA、O-LoRA；另测仅编码器/仅解码器 LoRA 对目标准确与英语遗忘的权衡。扩展词表字符并用预训练词嵌入均值初始化。

## 实验与结果
Bislama 随数据增加明显改善（Full FT 10h WER 19.64）；Nafsan 低数据不稳定，约 5h 才明显提升；Lelepa 极低资源下 2h 时 LoRA WER 75.66 优于 Full FT 84.10。漂移：Bislama/Nafsan 偏后层，Lelepa 早期编码器即大漂移。适应 Lelepa 后英语 WER：基线 15.68 → LoRA 18.89 → Full FT 26.24。仅解码器保英语更好但目标差；仅编码器目标好但英语遗忘更重。顺序学习：Full FT 保 Nafsan 更好但学不好 Lelepa；LoRA/DoRA/O-LoRA 对新任务更好却严重遗忘前语（Nafsan WER 飙至 84+）。

## 结论
对语言距离大的太平洋语言，适应常伴随深层表征改写与遗忘；现有参数高效法无法同时解决顺序适应中的塑性–稳定矛盾。亟需面向低资源、结构远语言的稳健适应策略。

## 点评
把“能不能认出”升级为“适应改写了什么、忘了什么”，对太平洋场景很有政策与工程含义。语料规模与语言数仍有限，英语遗忘用 LibriSpeech 等代理，未必等同多语能力全面退化；结论偏警示性，未给出可部署解法。


# Scaling Self-Supervised Speech Models Uncovers Deep Linguistic Relationships: Evidence from the Pacific Cluster

- 论文编号：3205
- 报告人：Minu Kim
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26w_interspeech.pdf

## 问题
既有观察认为 S3M 语言表征主要反映地理邻近或浅层接触，难以恢复深层谱系与长时区域汇聚。问题是：把 LID 覆盖从百级扩到数千语种，是否会非线性地改变嵌入拓扑并显现深层历史结构。

## 方法
比较同骨干 MMS-LID 的 126/256/1K/4K 语种模型；对 49 语（DoReCo+FLEURS）取末层双平均质心，标准化后 Ward 层次聚类，以 ARI/NMI 对照谱系子群，并用文件级 bootstrap（B=1000）估枝置信度。对 POA（Papuan–Oceanic–Australian）簇做维级 t 检验与 30 项声学特征相关，Mann–Whitney 在原始信号上独立验证。1K 与 4K 对 45/49 语 seen/unseen 状态一致，以隔离“覆盖规模”效应。

## 实验与结果
谱系恢复在 126–1K 平台期后，4K 跃升（峰值 ARI 0.74、NMI 0.95，K=18）。4K 树恢复多数家族，并高置信出现早期中华文化圈、波斯区域、达罗毗荼底等接触簇；澳斯特罗尼西亚分裂为未过新几内亚的 A 组与 Oceanic+Papuan+Australian 的 POA 宏簇（bootstrap 约 57%，Oceanic–Papuan 74%）。POA 分离精度 4K 达 1.0（1K 最高约 0.92）。4K 以更少显著维、更集中编码区分 POA；Bonferroni 下 energy dynamic range 最突出（28%），且原始声学上 POA 能量动态范围更高、谱变异更低，与嵌入相关一致。

## 结论
大规模语言覆盖可定性重塑 S3M 几何，恢复深层谱系与长时接触；太平洋宏簇提供声学侧区域汇聚证据。作者视为计算历史语言学与接触研究的新视角。

## 点评
规模效应的“平台期→跃迁”叙事清楚，并用 seen/unseen 控制与声学验证降低“只是看过这些语”的解释。POA 仍是相关性证据，bootstrap 中等、录音条件/语料构成可能混淆；不宜直接当作谱系证明，更适合作为接触与声学共性的计算假说生成器。


# Speech Recognition to Accelerate Documentation of Marquesan and Cook Islands Māori

- 论文编号：3276
- 报告人：Rolando Coto-Solano
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/teikitohe26_interspeech.pdf

## 问题
马克萨斯语（Marquesan）缺乏公开 NLP/ASR 工作，田野自然口语转录慢，制约文档与社区回传。邻近波利尼西亚语（如 Cook Islands Māori, CIM）能否迁移、以及 ASR 草稿修正是否真能省时，证据仍矛盾。

## 方法
收集约 17 小时 L1 自然口语（38 说话人、六方言、ELAN 人工转录，排除明显法语码切换）。微调 Wav2Vec2-XLSR53、MMS、Whisper Medium、Parakeet、Qwen3 ASR、Omnilingual 等，部分加 KenLM；再对最优骨干做 Marquesan↔CIM 迁移与联合训练（CIM 约 4 小时）。另做小规模人时实验：纯手写 vs 对 ASR 输出在 ELAN 中修正。

## 实验与结果
单语：Wav2Vec2+LM 最佳，中位 CER=16.0、WER=31.4。联合训练 Marquesan CER/WER≈15.4/30.8（相对单语略好，Mann–Whitney 未显著）；CIM 反而不如单语（Mono CER/WER≈1.8/7.2）。人时：手写约 5.18–9.14 分钟/音频分钟，修正约 1.51–5.18，摘要称加速约 0.7×–2.4×。主要错误含词边界混淆。

## 结论
ASR 已可进入 Marquesan 文档流程并加速修正；与 CIM 联合对 Marquesan 仅有微弱帮助、对 CIM 无增益。计划把 ASR 嵌入社区工作流以加快材料回传。

## 点评
同时报模型误差与真实转录人时，比只刷 WER 更贴近文档场景。WER≈30 仍落在“是否省时”争议带附近，人时样本小；自然田野噪声与多说话人叠加使 CER–WER 落差大，词边界问题值得后续专项处理。


# Mapping Acceptable Pronunciation Range for te reo Māori through Perceptual, Acoustic, and Marker Evaluative Data

- 论文编号：1561
- 报告人：Catherine I Watson
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/evans26_interspeech.pdf

## 问题
发音教学常假定单一“标准音”，但 Māori 元音跨说话人/代际变异大，可接受范围未系统标定；双元音常被教成单元音串联，是否与流利说话人判断一致存疑。

## 方法
301 名大学 Māori 课程学生 pepeha 朗读；MAUS 强制对齐。FRED 平台三角化：声学共振峰、语音学家转写变体、流利说话人（markers）接受/拒绝。聚焦单元音 /a u/（文中记为 /5 0/）与双元音 /ai ae au/（/5i 5e 50/）。

## 实验与结果
单元音：canonical 与常见替换（如 /0/→[u]、/5/→[@]）被 markers 同等高度接受（Fisher 不显著）。双元音 /50/：[@0] 与 canonical 同等可接受，但第二目标偏后的 [5u] 显著更易被拒（p<.001）。/5/ 在 /50/ 起点声学接近 [@] 而非 monophthong [5]，而 /5e/ 起点与 [5] 不可区分；/5i/ 与 /5e/ 交叉替换近天花板接受，提示可能合并。声学差异显著（如 [5] vs [@] F1、[0] vs [u] F2）。

## 结论
同一声学变体在单元音可接受，在双元音中可被惩罚——挑战“双元音=元音序列”教学观；流利说话人更像把双元音当作独立单位音位，应单独教学。属可接受范围研究的初步案例。

## 点评
把“可接受性”从轶事变成声学–转写–母语判断三方证据，对振兴语境下的发音教学很实用。样本为课程学生最终提交、非母语/流利说话人生产，反映的是学习者产出+流利评判；/5i–/5e 合并解读需更大、更多样说话人复现。


# Oral stop realisation in three French Polynesian languages

- 论文编号：899
- 报告人：Janet Fletcher
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/fletcher26_interspeech.pdf

## 问题
法属波利尼西亚多种濒危东波利尼西亚语的清塞音多为印象描写，Rurutu/Marquesan 缺系统 VOT/闭塞时长量化，Tahitian 亦仅有初步研究；是否 short-lag、是否有方式/浊音弱化尚不清楚。

## 方法
12 名双语说话人（Tahitian 5♀；北 Marquesan 2♂2♀；南 Marquesan 1♀；Rurutu 2♀）在安静室录音。Tahitian 为句框中的双音节词，Marquesan/Rurutu 为修订 Swadesh 孤立词；测量 VOT、闭塞时长与浊音比例，线性混合模型分析音位、后接元音、词位、突显等。

## 实验与结果
三语塞音均为清、short-lag，平均 VOT 约 20 ms；Marquesan 软腭 /k/ 长于双唇/齿音。后接元音是 VOT 最强因素：/t/ 在前高元音前更长，/p/ 在后圆唇前更长。闭塞时长仅 Tahitian 显示重音音节更长；浊音比例整体偏低，词中略高，但无强浊化或擦音弱化证据（无 intervocalic 擦音实现）。

## 结论
确认三语单系列清塞音为 short-lag，VOT 主要受后接元音共发音驱动，目前语料少见方式/浊音弱化。局限包括说话人少、任务不完全对齐，需更平衡语料。

## 点评
为法语波利尼西亚塞音提供首批可比声学基线，并与 Hawaiian/Māori 文献对话。任务与样本不均（Tahitian 句框 vs 他语孤立词）限制跨语因果比较；“无弱化”结论对随意口语外推需谨慎。


# A preliminary exploration of stop-vowel coarticulation in Māori

- 论文编号：1456
- 报告人：Isabella Shields
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shields26_interspeech.pdf

## 问题
Māori 语音学长期偏重元音，共发音与塞音对元音质量的影响证据很少；早期 MAONZE 曾称除 /r/ 外预期性过渡不多，需用当代数据检验。

## 方法
7 名流利女性说话人朗读 CVCV 真词（C∈{p,t,k}，V∈{i,e,a,o,u}）于载体句，首音节重读、前后同辅音；524 个有效 token。WebMAUS 初分后人工校正边界与 F1/F2，用 GAMM（bark 尺度）建模辅音×元音对轨迹的影响。

## 实验与结果
辅音语境显著影响 F1/F2；F2（前后）变化更突出，F1（高低）差异虽显著但较少“显著可感”。/t/ 语境使 /o u/ 明显前移（/o/ 的 F2 可接近 /a/）；/k/ 在前元音旁抬高 F2（可能腭化），在后元音旁相对后缩。与“高前元音抗共发音”的跨语倾向不完全一致。作者称首次记录 Māori /o/ 在齿龈语境的前移。

## 结论
当代说话人中塞音共发音可改变元音质量，尤其后度；提示需重估“共发音弱”的旧描述，并考虑与音变的关联。局限：仅年轻女性、实验室朗读。

## 点评
用 GAMM 动态轨迹填补 Māori 辅音–元音共发音空白，对解释 /u/ 前移等已知变化有机制意义。说话人同质与朗读体限制推广；与 MAONZE 历史语料的直接对比仍是下一步。


# Vavanagi: a Community-run Platform for Documentation of the Hula Language in Papua New Guinea

- 论文编号：815
- 报告人：Bri Olewale
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/olewale26_interspeech.pdf

## 问题
巴布亚新几内亚 Hula（Vula’a，约 1 万说话人）面临 Tok Pisin 压力与城乡流动；外部主导的文档项目难以保证社区对数据与目标的主权，且同规模语言少有社区自建语言技术平台。

## 方法
社区自研平台 Vavanagi：众包英–Hula 文本翻译与语音录制，长老主导审阅；Firebase 存数据与角色权限。提出五级社区参与谱系（咨询→完全社区发起与治理），并将本项目标为 Level 5。技术成本低于 20 美元。

## 实验与结果
77 名译者、4 名审阅者产出 12,124+ 平行句对、覆盖约 9k 独特 Hula 词；首批 2000 句两周完成，次批 1500 句三天；一审通过率 91%；SUS 均值 73.4。审阅反馈反映 Tok Pisin 借词与码切换上升。尚无训练下游 MT/ASR 的正式指标。

## 结论
展示万人量级语言亦可由社区发起、设计、实施并治理语言技术基础设施；平台 bridging 城乡与代际。未来计划训练 MT 与 ASR 并做社区面向应用。

## 点评
贡献主要在治理框架与实践证据，而非模型分数；五级谱系为领域提供可比较的“谁掌权”词汇。技术结果尚处语料阶段；可持续性依赖志愿者审阅带宽与后续模型是否仍由社区控制。


# Working Together on Technologies: A Case Study of Collaboration in Aotearoa

- 论文编号：1573
- 报告人：Ben Hutchinson
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hutchinson26_interspeech.pdf

## 问题
te reo Māori 长期在 TTS、键盘等产品中支持不足；原住民组织与全球科技公司合作时，如何在不同价值观、数据主权与问责观下达成互利且尊重自决的伙伴关系，案例仍少。

## 方法
案例研究 Te Taura Whiri i te Reo Māori 与 Google 的 TTS 合作（新西兰口音英语 + 流利发 Māori 地名）。不以模型细节为主，而以 Māori 概念组织叙述：whakawhanaungatanga（关系）、manaakitanga（关怀）、tauira（实践范例）。记录挑战与共创产物：MoU、IP 协议、CARP 对齐框架、语言互动文档、选声伦理等。

## 实验与结果
无传统 CER/MOS 表。过程结果包括：签署 MoU；2024 年交付 macron 键盘支持；共创 IP 协议承认发音词典与评测数据的 Māori 监护并许可 Google 开发 TTS；用 CARP 记录“可接受承诺 vs 理想偏好”（如收入回流振兴无法承诺，但确认无故意从该 TTS 谋利）；系统记录英–Māori 触点问题（如 ’s 附着）。指出双方在关系优先级、规范框架、语言认识论、选声标准、问责观上的张力。

## 结论
原住民组织与科技公司可建立互利伙伴关系，但关键在过程与关系而非仅交付物；共创治理与记录工具有助于穿越价值冲突。

## 点评
把“怎么合作”写成可复用的张力清单与制度工件，对领域比又一个 TTS demo 更稀缺。不可避免偏自我叙述、缺少外部评估与负面案例；技术效果与社区满意度的量化仍留白。


# Pā‑Kakare: The First Emotional Speech Database for Te Reo Māori

- 论文编号：1543
- 报告人：Himashi Rathnayake
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/rathnayake26_interspeech.pdf

## 问题
Māori 缺乏情感语音资源；通用 Ekman 类目未必契合社区定义，且原住民参与不足会导致文化错位。需文化相关语料并初步刻画声学表达。

## 方法
基于先前社区研究得到的 16 类 Māori 情感（如 ngenge、aroha、hōhā、hīkaka 等）建表演语料：4 名职业 Māori 演员（2♂2♀），每类 15 句（10 中性语境 + 5 情感显著），共 3840 条高质量录音。感知验证：18 听者、288 句、每句 3 人、八类子集任务；另用 f0、强度、mora/秒语速相对基线 pai 做初步声学比较。

## 实验与结果
八类识别总体准确率 36.15%（远高于 12.5% 偶然）；女演员约 51%/40%，男演员约 30%/26%。四选一跟测升至 51.46%，提示大选择集认知负荷。ngenge、hōhā、pōuri、hīkaka 较易认；相近唤醒度对易混。声学上不同情感在 f0、强度、语速呈系统差异（图示趋势）。

## 结论
提供首个太平洋原住民语言情感语音库之一，并显示 Māori 情感表达有可测声学差异。局限：表演语料、类别细导致感知难、听者文化深度不一。

## 点评
用社区定义类目替代“普世六情”，并半团队 Māori 身份嵌入流程，方法论立场清楚。表演+大标签集使识别率中等属预期；下游 SER 可用性仍取决于类目是否可合并与标注协议如何扩展到自然口语。


# Automating Sociophonetic Research in Under-Resourced Languages: A Case Study of Speech Rate in Cook Islands Māori

- 论文编号：3507
- 报告人：Rolando Coto-Solano
- 程序：Tuesday 29 September 2026 / Pacific Voices: Speech Science and Technology for the Languages of the Pacific Ocean
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cotosolano26_interspeech.pdf

## 问题
社会语音学需要大量带社会标签的口语，低资源语难以手工扩展；AI（ASR、年龄识别）能否半自动扩充语料并揭示 Cook Islands Māori（CIM）语速的岛屿×年龄变异，尚缺报告。

## 方法
合并 Paradisec 田野转录与公开社媒音视频：Silero VAD 切段，ASR 助算 mora/秒语速；尝试人脸年龄估计失败后改为人工“>/<50 岁”。共 60 说话人、约 7.5 小时、8083 韵律短语，覆盖 Rarotonga、Nga Pū Toru、Aitutaki。线性回归检验年龄×岛屿交互。

## 实验与结果
人脸年龄模型在 Cook Islander 面孔上表现很差。语速（mora/s）：Aitutaki 最快（老/青约 8.4/8.7）；Rarotonga 约 6.6/6.4 无年龄差；Nga Pū Toru 年轻人显著快于年长者（7.7 vs 6.8，p<.0001）。Rarotonga 年轻人慢于 Nga Pū Toru 年轻人；Aitutaki 各年龄均快于同龄他岛。作者将无“年轻更快”的岛屿与语言转移/熟练度下降联系起来。

## 结论
自动化可加速语速测量，但年龄等社会标签对原住民面孔仍不可靠，需人工/社区众包。语速地理–年龄格局与岛屿活力差异一致。将扩更多岛与说话人。

## 点评
把 ASR 当 sociophonetic 量尺而非终点，并诚实报告年龄 AI 失败，对低资源计算社会语言学很有方法论价值。在线数据的岛屿归属与迁移史噪声大；语速–熟练度因果仍是解释性假说。

