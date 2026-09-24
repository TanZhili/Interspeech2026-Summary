# Safeguarding Synthetic Speech: Ethical, technical and legal perspectives

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Special Session
- Area：14
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本特刊把合成语音治理拆成技术溯源、语言数字保存、同意机制、数据集审计与法规术语对齐。检测侧从二分类走向开集少样本来源归属；同时低资源非洲语言 TTS 提醒：合成能力扩展与保护义务并行。

伦理法律侧批判一次性合同授权无法覆盖作为身份标记的声音；动态同意被提出为更合适的治理模板。数据集审计则显示公平性评估因缺人口统计元数据而基本不可行，且 bona fide 源语料高度重叠会夸大跨集泛化。

政策论文进一步指出：把图像/视频类比套到语音会失效，尤其忽视可独立开发、事后复用的说话人嵌入与复杂工作流。整体趋势是技术对策必须与同意、数据与法律定义同步修订。

## 论文技术总结

# Who Synthesized This? Joint Deepfake Detection and Generative Source Attribution

- 论文编号：2442
- 报告人：Vishal Kumar
- 程序：Tuesday 29 September 2026 / Safeguarding Synthetic Speech: Ethical, technical and legal perspectives
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kumar26f_interspeech.pdf

## 问题
合成语音检测 alone 已不够：还需在开放世界中追溯生成源（含训练未见的零日合成器）。合成系统持续发布，静态闭集分类无法扩展；ASVspoof 5 等开放条件暴露旧基准局限。

## 方法
三阶段框架：Phase1 用 LoRA（r=8, α=16）适配 WavLM-Large，分层度量学习——条件 AAM-Softmax（可训 margin）+ EMA Center Loss；课程先分架构族（LLM-Codec、Diffusion、Flow-Matching 等）再分细粒度合成器。Phase2 对 MLAAD v9 中 2025 后 Set2 模型做 few-shot 原型注册（文中经验阈值约 K≈36 稳定质心），真实语音用 VoxCeleb2 性别条件三原型。Phase3 余弦近邻检索，无参数更新。训练/注册/评测数据严格分离，ASVspoof 5 Track1 open 仅用于评测。

## 实验与结果
ASVspoof 5 open：单系统 EER 0.49%、minDCF 0.09，优于挑战最佳单系统与多数集成；actDCF 0.97 显示度量学习分数校准偏弱。渐进注册 Set2 时族/模型准确率升至 92.0%/90.3%，加 3-way 真实原型后达 99.0%/97.0%，EER 至 0.49%。t-SNE 显示真伪宏分离与族内聚类。

## 结论
分层度量学习 + 推理时原型锚定可在开放世界同时做检测与源归属，无需为新合成器重训。后续需分数校准与对抗扰动鲁棒性。

## 点评
把“谁合成的”做成可扩展原型库，比闭集归因更贴近取证部署。强在时间划分模拟零日与真实流形多原型；弱在 actDCF 偏高、原型样本数依赖经验阈值，且超低 EER 对划分与原型完备性敏感。


# Towards Digital Preservation of Efik: TTS for a Low-Resource African Language

- 论文编号：1868
- 报告人：Offiong Bassey Edet
- 程序：Tuesday 29 September 2026 / Safeguarding Synthetic Speech: Ethical, technical and legal perspectives
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/edet26_interspeech.pdf

## 问题
Efik 为尼日利亚东南部下克罗斯语系声调语言（约 150 万母语者），缺乏公开可训 TTS 语料，数字保存与可用语音技术严重滞后；声调错误会改变词义。

## 方法
自建单说话人语料约 3.08 小时、2632 句（无线麦、安静室内；训/验/测 1975/264/393），材料来自小说、民间故事与教材；因 Whisper/XLS-R 强制对齐不可靠，全文人工转写并由母语者与语言学家校验。微调 VITS、MMS-TTS、SpeechT5、Orpheus-TTS；MMS 从约鲁巴 checkpoint 扩词表/嵌入以覆盖 ọ、ñ 等字符。5 名母语者评 MOS、Nat-MOS、A-MOS。

## 实验与结果
MMS-TTS 最高：MOS 3.80±0.63，Nat-MOS 3.60，A-MOS 3.04，且可生成约 3 分钟连贯长音频无明显幻觉；Orpheus 3.08、SpeechT5 2.48、VITS 仅 1.08。各模型对 ñ 等稀有音素仍困难；Orpheus/SpeechT5 长序列易崩溃并带外来口音，声调与文化韵律保留不足。

## 结论
给出 Efik 首个可复现端到端 TTS 基线；多语预训练的 MMS 在极低资源单说话人设定下最稳，但要自然、声调准确仍需更大、多说话人、声调感知建模。

## 点评
贡献以语料与系统性对照为主，切中数字不平等。强在人工标注质量与长音频对比；弱在单说话人 3 小时、评测人少，且会话主题落在“合成语音防护”下更偏保存/伦理语境而非深度架构创新。


# Rethinking Consent Acquisition for Voice Synthesis: from Static to Dynamic Consent

- 论文编号：2379
- 报告人：Matilde Nanni
- 程序：Tuesday 29 September 2026 / Safeguarding Synthetic Speech: Ethical, technical and legal perspectives
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nanni26_interspeech.pdf

## 问题
语音合成使第三方可用某人声线说话；现行防护多依赖一次性合同式同意。声音既是数据又是身份标记、难以去标识，静态授权无法覆盖事后用途与身份性伤害（如 Paul Skye Lehrman 案例）。

## 方法
规范分析：梳理声音在表征/识别两维与身份的关系，以及数据化与商品框架张力。以知情同意要件（信息充分、自愿、能力）与同意范围理论检视合同实践。对照 BeyondWords 式概括同意（仅排除淫秽/种族主义等宽泛禁止、可转让 IPR）与 Narrativ/SAG-AFTRA 式具体同意（约 47 类可勾选，后已失效）。引入生物伦理中的动态同意：经个人数字平台持续审阅、更新、撤回对未来用途的授权。

## 实验与结果
无定量实验。论证结论：概括同意因范围过宽而不知情；具体同意仍是静态分类，无法覆盖不可预见或同类别内善恶用途（如“健康”宣传）及时变含义。动态同意更匹配身份敏感、用途演化的合成声线治理，但可能仅有议价力强的人能实际争取。

## 结论
合成声线治理应从“采集时一次授权”转向“持续控制”；动态同意平台更利于知情与防身份伤害，同时承认权力不对称这一根本局限。

## 点评
把同意从技术门控/签名扩展到身份伦理与合同结构，问题意识清楚。强在一般/具体同意的案例拆解；弱在未给出可落地的平台设计与执法路径，且动态同意的可及性依赖议价权力，弱势群体仍可能落空。


# Ethical and Technical Limits of Deepfake Speech Datasets

- 论文编号：124
- 报告人：Vojtěch Staněk
- 程序：Tuesday 29 September 2026 / Safeguarding Synthetic Speech: Ethical, technical and legal perspectives
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/stanek26b_interspeech.pdf

## 问题
深度伪造语音检测器的鲁棒性与公平性声明，取决于训练/评测数据集质量；现有基准多服务准确率竞赛，与 EU AI Act 等对文档、可追溯与偏置监测的要求错位。跨数据集评测常被当作域外测试，但可能共享真实语音源。

## 方法
审计 39 个同行评审报告的深度伪造语音数据集：可及性、许可、语言、人口统计元数据、合成工具披露、规模，并绘制 bona fide 源语料重叠图（交互浏览器公开）。属性对照论文与官方仓库交叉核对。

## 实验与结果
仅约 49%（19/39）同时报告男女说话人计数/标签；口音、年龄、族裔等几乎缺失，公平评测基本不可行。语言：64% 单语（多为英/中），多语仅约 21%。23% 仅单一合成器或未披露工具。15% 受限访问；部分许可不清或禁商用。源侧大量依赖 LJSpeech、VCTK、AISHELL、LibriVox 衍生资源，跨集评测可能泄漏语料特异伪影。无一数据集同时满足作者所列“无偏检测”全部属性。

## 结论
缺失人口/语言元数据使公平评估受阻；共享真实源削弱跨集泛化叙事。建议发布时报告人口与语言元数据、详细合成管线、真实语音来源、清晰许可与可靠获取。

## 点评
把批评落在数据集基础设施而非再刷榜，对领域很及时。强在系统表与源重叠可视化；弱在重叠无法从公开文档精确量化（作者已声明），结论偏审计清单而非因果实验。


# AI Regulation and the Technical Language of Speech Synthesis

- 论文编号：210
- 报告人：Jennifer Williams
- 程序：Tuesday 29 September 2026 / Safeguarding Synthetic Speech: Ethical, technical and legal perspectives
- 技术分类键：deepfake
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/williams26_interspeech.pdf

## 问题
全球 AI 监管（如欧盟 AI Act、加州、中国等）对深度伪造与合成语音施加透明度义务，但法律用语多借图像/视频的“生成 vs 篡改”，且聚焦输出标注；忽视可移植的说话人嵌入模型及其在 TTS/VC/ASR/ASV 工作流中的独立生命周期。

## 方法
概念与历史梳理：说明语音合成直至 WaveNet 后才被重新框为 AI；梳理 TTS、VC、ASV、ASR 的长期交叉。对比法律中 AI system/model/service 与语音研究中“模型=可组合模块”的差异。表列 i-vector、d/x-vector、ECAPA、WavLM、PPG、wav2vec 等嵌入的外部性、可复用性与是否编码说话人身份。图示编码器–解码器–声码器、端到端、ASR 中介 VC、codec+LLM 等流程。兼论哲学（后人类/嗓音复制）与医学（嗓音假体）政策含义。

## 实验与结果
无定量实验。核心主张：仅监管输出无法覆盖说话人嵌入的创建、存储、转移与跨任务复用；“完全合成/部分合成”二分法难以刻画扩散/流式迭代与多模块管线。说话人嵌入处生物特征隐私灰色地带（不可唯一反演却可支撑识别）。

## 结论
政策语言需与语音合成的模型与工作流技术现实对齐，否则透明度义务会漏掉身份编码组件；语音科学家应帮助修订法律用语，兼顾文化妥当与技术可执行。

## 点评
把监管缺口钉在“可移植说话人模型”而非笼统 deepfake 标签，对立法沟通很有用。强在历史脉络与嵌入/工作流对照表；弱在偏政策批评、未给出可操作的监管条文草案或合规度量。

