# Spoofing and Deepfake Detection 1

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster
- Area：4
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场反欺骗/深度伪造检测同时覆盖被动检测、主动防御、数据集多样性与攻击面扩展。数据侧共识是“多样性重于盲目扩规模”：固定生成方法下过度扩容可能损害跨域泛化；SEA-Spoof、LRLspoof、MultiAPI Spoof 分别补东南亚六语、66 语（含低资源）与约 30 个商业/开源 API 的覆盖，并暴露高资源训练模型的跨语退化与语言作为独立域移来源。

方法上，韵律监督掩码预测（ProSDD）提升对表情/情感伪造的泛化；域不变韵律特征在真实诈骗电话零样本/少样本设定提供轻量替代，而 HuBERT/wav2vec2.0 在有真实样本时更高。域泛化用 GMM 式偶然风格不确定性增强；主动防御 FreqGuard 以频域先验生成不可感知扰动干扰合成。

攻击面不限于分类器：Ouroboros 展示语音增强模型可被干净音频自触发后门；KEYAC 评估语音表征学习在键盘声学侧信道与 VoIP 编解码下的泛化，并用 KAN 微调。瓶颈是真实犯罪/低资源数据稀缺、表情攻击、API 异构与前端模块新威胁。

## 论文技术总结

# Comparing Self-Supervised and Domain-Invariant Features for Cross-Domain Voice Phishing Detection

- 论文编号：1975
- 报告人：Jeongmin Lee
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/lee26s_interspeech.pdf

## 问题

语音钓鱼（vishing）检测面临真实犯罪录音因隐私难获、即使有也极少、且需轻量声学端侧方案。作者比较：用场景化演员录音训练、在真实犯罪通话上测试时，域不变韵律特征与冻结 SSL（HuBERT、wav2vec2.0）谁更能跨域泛化，以及零样本/少样本下的部署权衡。

## 方法

韩语音料：场景 VP（406）、真实犯罪 VP（测试 406 + 独立 holdout 50）、场景金融咨询与真实电话咨询作非 VP；统一 8 kHz、说话人独立。eGeMAPS 88 维经 RF 重要性 + Cohen’s d<0.5 选出 4 个域稳定特征（logRelF0-H1-A3、mfcc1V、mfcc4、F2bandwidth）。SSL 用 LibriSpeech 预训练 Base 模型末层均值池化 768 维、权重冻结。分类器统一 Logistic Regression；k∈{0,1,5} 真实 VP 样本并入场景训练集。报告 F1、Recall、Precision。

## 实验与结果

零样本：精选 4 特征 F1=69.5%，全 88 特征仅 3.8%；HuBERT 58.3%、wav2vec2.0 36.2%。5-shot：HuBERT 94.2%（Recall 99.3%）、wav2vec2.0 90.2%（Precision 99.4%）、4 特征仅升至 71.0%，全 88 特征升至 85.2%。消融显示 mfcc1V 是主要检测驱动，4 特征在少样本下更利于抑制误报。部署建议：冷启动用轻量 4 特征；有少量真实样本与算力时用 SSL，并按召回/精确需求在 HuBERT 与 wav2vec2.0 间选择。

## 结论

跨域 vishing 检测存在由目标域样本量决定的体制：域不变韵律适合零样本冷启动，SSL 在 5-shot 后显著更强但精度—召回形态不同。Cohen’s d 过滤是冷启动前提；该体制是否跨语种成立仍待验证。

## 点评

贡献是把“演练数据→真实犯罪”写成可复现的零/少样本协议，并显式对比轻量特征与冻结 SSL 的部署剖面，而不是再堆一个检测网络。特征选择需用真实 VP 做离线统计这一点要诚实看待：严格意义上的“零真实数据”仍部分依赖目标域分布信息。脆弱点包括仅韩语、非 VP 类与 VP 场景未必对称，以及线性分类器可能低估微调 SSL 上限。


# Exploring the Scale and Diversity of Speech Anti-spoofing Datasets: Experiments and Analysis

- 论文编号：157
- 报告人：Zhuolin Yi
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/yi26_interspeech.pdf

## 问题

近十年反欺骗训练集规模指数膨胀，隐含“更大更好”。但在固定生成方法下盲目扩规模是否同步提升跨域泛化，以及多样性（本文主要指生成方法种类）是否比规模更关键，仍缺可控实验。观测上 Speechfake 虽小于 Spoofceleb 却可能因攻击种类更多而泛化更好，需去混杂验证。

## 方法

固定 Wav2Vec-AASIST（XLS-R 300M）+ RawBoost，做两组实验。(1) 规模：在 Speechfake-BD、ASVspoof5 训练集上按 1%/5%/10%/20%/50%/100% 随机子采样，保持生成方法集合不变，做域内与跨集（含 CD-ADD、Spoofceleb、FSW、In-the-Wild、VoiceWukong）评测。(2) 多样性：从 ASVspoof5、Speechfake-BD、CD-ADD、Spoofceleb 各生成方法抽 1000 条假样本，真实样本仅来自 Speechfake-BD，组成约 63k 句、53 种生成方法、约 94 小时的复合集，再与各全量原集在 In-the-Wild、VoiceWukong、FSW 上比跨域 EER。

## 实验与结果

规模实验：性能不随数据量单调上升；Speechfake-BD 上域内 50% 与 100% 接近甚至 50% 略好，跨域最佳多在约 20%；ASVspoof5 最佳常在 10%–20%。多样性实验：复合集平均跨域 EER 13.03，优于 CD-ADD（21.65）、ASVspoof5（27.92）、Speechfake-BD（17.52）、Spoofceleb（19.67），尽管 Spoofceleb 时长最大（约 1982h）但仅 10 种生成方法。

## 结论

固定生成方法下过度扩规模易过拟合训练集攻击分布、伤害跨域；更小但生成方法更多的复合集泛化更好。未来建库应优先扩攻击/生成多样性，而非单纯堆时长。局限：模型容量固定、子采样多为随机、多样性定义偏窄。

## 点评

用控制变量把“规模神话”拆开，对社区建库资源分配有直接政策含义。复合集设计把多库生成方法并置，能解释为何大库未必赢。脆弱点是随机子采样可能混入信息量差异，且跨库“同名方法不同流水线”被当作不同方法，多样性度量仍偏操作化；未联合扫描模型容量与数据预算。


# ProSDD: Learning Prosodic Representations for Speech Deepfake Detection against Expressive and Emotional Attacks

- 论文编号：831
- 报告人：Aurosweta Mahapatra
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/mahapatra26_interspeech.pdf

## 问题

深度伪造检测在标准基准上表现好，但对富情感/表达性合成攻击常失效。许多系统在假样本占优数据上只做分类微调，易学数据集特有伪影，而非自然语音的可迁移结构。人类更像先内化真实韵律变异，再把伪造当偏离。作者希望把说话人条件韵律结构显式写入 SSL 表征。

## 方法

ProSDD 两阶段。(I) 仅真实语音（LibriSpeech clean）：对 XLS-R 做监督掩码预测，目标为 ECAPA 说话人嵌入拼接帧级韵律（F0、voice activity、energy，256 维），用 InfoNCE 区分正样本与同说话人不同韵律 / 不同说话人同韵律负样本。(II) 在 ASVspoof 2019 或 2024 上联合加权 CE 分类与同一掩码预测辅助损失；每步 masked/unmasked 双前向；分类头仅线性+Dropout+ReLU，避免复杂池化抢功。推理只用骨干与分类头。

## 实验与结果

2019 训练：ProSDD 在 ASV19/21/24 EER 为 0.42/3.87/16.14，EmoFake 3.70、EmoSpoof 9.54，相对 XLSR-SLS 的 25.43/8.84/18.92 等明显改善（摘要称情感集约 50% 相对降幅）。2024 训练：ASV24 从 39.62% 降至 7.38%，EmoSpoof 11.96、EmoFake 25.06，并优于 RawNet2/AASIST。消融去掉掩码预测与 Stage I 全面变差；仅 Stage II 保留掩码仍不如完整两阶段稳定。

## 结论

先从真实语音学习说话人条件韵律结构，再以辅助任务保持该结构做伪造判别，可在保持传统基准竞争力的同时显著提升对情感/表达性攻击的泛化。代码与资源已公开。

## 点评

训练哲学从“盯假样本伪影”转向“先建模真语音韵律规范再找偏离”，与人类直觉和表达性 TTS 弱点对齐。轻量分类头有助于把增益归因到表征而非架构。脆弱点是韵律目标依赖外部编码器质量、Stage I 仅英语朗读、跨攻击（TTS 训 / VC 测）上 EmoFake 仍偏高，且双阶段训练成本更高。


# Impact Analysis of Speech Representation Learning Models for Acoustic Side-Channel Attack

- 论文编号：3500
- 报告人：Orchid Chetia Phukan
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/choudhury26_interspeech.pdf

## 问题

键盘敲击声可被用于声学侧信道攻击（ASCA）推断按键，但公开评测多缺现代 VoIP 编解码失真，也少系统检验语音预训练模型（PTM）表征是否适应该任务。作者要在跨键盘与 Zoom/Teams 等传输条件下量化 PTM 表现，并改进下游适配。

## 方法

发布 KEYAC：37 键盘、37440 次敲击，均分笔记本麦、手机近场与实时 VoIP 流三通道。冻结骨干提取表征：Wav2Vec2、HuBERT、WavLM、XLS-R、X-Vectors、Whisper 编码器。下游对比 FCN、CNN 与 Kolmogorov–Arnold Network（KAN，单隐层 30 单元、样条适配）。协议含 5 折域内，以及标准录音键盘留出、VoIP 下键盘留出、仅编解码迁移（标准训 / VoIP 测）。

## 实验与结果

基线中 WavLM+CNN 最强：标准域内 Acc/mF1 约 58.34/56.92，VoIP 与编解码设定明显下降。KAN 全面抬升：WavLM+KAN 标准域内 68.47/67.12，键盘 OOD 61.73/60.34；VoIP 键盘泛化 57.82/56.41；编解码泛化 58.36/57.04。其他 PTM 在 KAN 下亦系统性优于 FCN/CNN，但绝对水平仍受未见键盘与压缩伪影制约。

## 结论

语音 PTM 可为 ASCA 提供有用特征，但在 VoIP 与未见键盘上用常规下游会明显退化；KAN 适配通过显式非线性交互建模持续改进鲁棒性，WavLM 表征整体最稳。数据集按请求向研究用途开放。

## 点评

工作价值在基准化：把 ASCA 从手搓特征小实验推进到 PTM + 多通道编解码评测。KAN 提升说明瓶颈常在适配层而非再换更大 SSL。安全含义上强调现实威胁面；脆弱点是按键分类准确率仍远非“可稳定还原密码”水平，且数据集非完全公开、场景偏受控采集。


# Ouroboros: Self-Referential Backdoor Attacks on Speech Enhancement via Clean Audio Triggers

- 论文编号：455
- 报告人：Yunjie Zhou
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26_interspeech.pdf

## 问题

语音增强常作为实时语音服务前端，对抗样本研究较多，但后门威胁研究不足。既有音频后门多针对分类、并假设推理时可主动注入人工触发；增强模型是被动处理用户流，攻击者通常无法稳定改推理输入，故传统触发模型不现实。

## 方法

提出 CleanTrigger：把训练集中高纯度干净目标语音本身当作触发，使模型在遇到自然干净高 SNR 语音时激活恶意行为，无需推理期外加信号。Ouroboros 在黑盒数据投毒威胁模型下，按 SNR 排序毒化高 SNR 样本（默认毒化率 10%），将输入—目标改为（干净语音，恶意目标如静音），保留低 SNR 样本以维持正常去噪。在 VoiceBank-Demand、WSJ0-CHiME3 上攻击 MP-SENet、SEMamba、CMGAN、FlowSE；对比 BadNets（固定正弦触发）。指标：ASR（触发时输出近静音比例）与非触发噪声输入的 PESQ 相对变化。另测滤波/微调防御、物理录音触发与短语篡改扩展。

## 实验与结果

10% 毒化下 ASR 多近 100%，PESQ 降幅通常小于或可比 BadNets；生成式模型主任务受损往往更小。2% 毒化已可高 ASR；高 SNR 毒化优于随机/低 SNR。常见滤波难以在去后门与保质量间兼顾；有限干净数据微调后 ASR 仍可很高。物理世界 60 条干净人声触发：FlowSE ASR 100%、MP-SENet 96.7%。短语篡改（目标句经 TTS）在 CMGAN 上 ASR 84.15%、FlowSE 46.24%。

## 结论

清洁语音自指触发可使增强模型在被动场景被后门激活，成功率高、主任务损伤相对可控，并对简单过滤与微调有韧性。作者呼吁针对性防御与跨数据集验证；范围限于成对数据训练的增强模型。

## 点评

抓住增强系统“被动、无外部触发”的威胁模型缺口，把后门从分类迁移到回归前端，对供应链数据投毒风险有警示意义。高 SNR 优先毒化体现攻击—效用折中设计。作为学术安全研究，其启示是增强服务需审计训练数据与部署干净输入路径；文中结果亦显示简单微调难清后门，防御需专门设计。


# FreqGuard: Leveraging Frequency-Domain Feature Priors for Universal Proactive Voice Defense

- 论文编号：2069
- 报告人：Yankai Wang
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/wang26ca_interspeech.pdf

## 问题

语音克隆 TTS/VC 威胁隐私，被动检测滞后。主动防御在发布前向语音嵌入不可感知扰动以破坏说话人嵌入建模，但多数方法从随机噪声出发、主要优化嵌入空间位移，跨模型泛化弱，且易被扩散净化或频域恢复削弱。需要更结构化、可迁移的频域先验引导扰动。

## 方法

FreqGuard：先在 LibriSpeech 子集上系统评估下采样、量化、频带掩蔽、编解码、混响、噪声等操作对 SRS/PESQ/STOI 的影响，构建约 2.4 万条引导样本（平衡/强破坏/参考三类）。PriorNet 以干净—引导对学习重建幅相谱，联合时域、幅度、相位、对数谱、SSIM 与说话人余弦等多损失。GradPert 在幅度谱上生成有界对抗扰动（基于可反传幅度输入的 ASV）。保护语音由扰动幅度 + PriorNet 相位经 ISTFT 得到。评测 LJSpeech、VCTK、AIShell3，对抗 YourTTS、StyleTTS2、XTTS-v2、CosyVoice 等黑盒合成，并测跨 ASV 与 De-AntiFake 净化。

## 实验与结果

相对 Attack-VC、E2E、PoP、Enkidu，FreqGuard 在质量与跨 TTS 防御间更均衡：如 VCTK 上对多系统 ASR 更低（文中多处显著低于对比法的高 ASR），大模型如 CosyVoice 上最大 ASR 约 27.50%（对比有方法近 100%）。跨 ASV（ERes2NetV2、CAM++、ECAPA 等）表现较稳。净化后仍保持相对优势（如 LJSpeech 净化后 ASR 5%、VCTK 31.75%）。PESQ/STOI 总体优于偏重强扰动却伤可懂度的方法。

## 结论

频域操作先验引导的主动防御可在保持语音质量同时抑制克隆说话人相似度，并改善跨模型与净化场景下的鲁棒性。联合多损失与 GradPert 是实现质量—防护折中的关键。

## 点评

相对“嵌入空间乱推”，先用可解释频域操作建知识库再训练 PriorNet，更对准说话人身份的频谱统计结构，也解释了为何对部分净化更稳。工程上适合作为发布前保护流水线。脆弱点：引导集与 ASV 代理选择仍可能偏置；对最强商用合成 ASR 未归零；净化同源数据时防御仍会被削弱，说明主动防御与净化仍是军备竞赛。


# SEA-Spoof: Bridging the Gap in Multilingual Audio Deepfake Detection for South-East Asia

- 论文编号：3019
- 报告人：Jinyang Wu
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/wu26m_interspeech.pdf

## 问题

SEA 数字经济发展放大音频深度伪造风险，但主流反欺骗数据以英语等高资源语为主；MLAAD/SpeechFake 等对 SEA 覆盖稀疏或不成对，难做系统语言/系统级评测。泰语、越南语等声调语言与印地/泰米尔/马来/印尼等非声调语言的韵律差异，使高资源训练模型跨语迁移脆弱。

## 方法

发布 SEA-Spoof：覆盖 Tamil、Hindi、Thai、Indonesian、Malay、Vietnamese 六语，总约 711 小时，真假近 1:1，转录对齐配对。假语音来自 10 个开源（VITS-MMS、Edge-TTS、XTTS-v2、FastSpeech2、Indic-TTS、F5-TTS、Tacotron2 等）与 4 个闭源（HeyGen、ElevenLabs、MiniMax、ChatGPT-4o-mini-TTS）TTS/VC；真实来自 Common Voice、Indic、GigaSpeech2、马来会话与 YouTube、Thai Dialect、VIVOS 等。按语种与系统划分子集；8:1:1 分层切分。基准 AASIST、AASIST3、MoLEx，并在 SEA-Spoof 上微调 MoLEx。

## 实验与结果

高资源训练模型在 SEA-Spoof 上严重失配：如 MoLEx 在 ASVspoof5 EER 1.25% 但在 SEA-Spoof 达 43.8%。微调后 SEA-Spoof EER 降至 0.2%（ASVspoof5 略升，存在遗忘）。闭源假音比开源更难；语言上越南语相对易检，泰米尔/马来更难；系统上 ElevenLabs、ChatGPT-4o-mini-TTS 等更具挑战，HeyGen 相对易检。

## 结论

SEA-Spoof 填补区域语言空白，既作诊断基准暴露跨语/跨源失效，也可作微调资源显著恢复检测性能。未来拟扩方言与低资源语、接入新合成技术，并探索跨源适应与语言感知对策。

## 点评

典型“缺数据就建数据”贡献：用成对真假与开闭源并置，使跨语失败可归因到语言与合成源而非协议混乱。结果清楚表明英语基准高分不可外推到 SEA。脆弱点是微调后对原基准遗忘、部分语种开源模型覆盖不均，以及闭源系统随时间演进会使基准老化，需持续更新。


# When Spoof Detectors Travel: Evaluation Across 66 Languages in the Low-Resource Language Spoofing Corpus

- 论文编号：345
- 报告人：Kirill Borodin
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/borodin26b_interspeech.pdf

## 问题

反欺骗对策（CM）常在少数高资源语上训练，语言失配会使其依赖语言/音系相关伪影而非真正伪造线索。现有多语假音库在低资源语覆盖、生成器多样性或可控（语言×合成器）对比上不足，难以把“语言”当作独立域偏移轴来压力测试。

## 方法

发布仅合成的 LRLspoof：2732 小时、66 语（按 Common Voice 脚本语音 <100h 操作性定义含 45 个低资源语）、24 个开源 TTS（经典到零样本克隆）。评测 11 个公开 CM：在汇合外部真假基准（ASVspoof5、ASVspoof2021 LA/DF、In-the-Wild、DFADD、ADD2022）上标定 EER 阈值，再固定转移到 LRLspoof，报告 spoof rejection rate（SRR）。用固定 CM+固定 TTS、仅改语言的对照，隔离语言效应。故意不含目标语真实语音，以免域标签混入真假判别。

## 实验与结果

阈值转移下 SRR 跨语言与跨模型差异极大（如 aasist3 英语 93.33%、车臣 99.86%；nes2net 在加泰罗尼亚可近 0%、车臣近 100%）。语言均值 SRR：aasist3 约 90.4%，w2v2-300 约 80.5%，若干 SSL/图注意力系统均值仅约 26–46%。固定 TTS 的对照中语言差可达数十个百分点（如 Parler-TTS 英—波对 w2v2-300 差 94.46 pp；Piper 丹—威对 aasist3 差 99.51 pp）。低资源子集上部分模型进一步退化。

## 结论

语言是反欺骗独立的域偏移源；同一合成器下跨语 SRR 可剧烈变化，暴露语言伪影依赖。LRLspoof 定位为 spoof-side 跨语诊断库，强调报告跨语差距而非仅匹配语结果。局限：无目标语真实样本，SRR 高不等于完整工作点（缺 FRR）。

## 点评

用“阈值转移 + 固定合成器变语言”把语言偏移做得干净，对部署多语 CM 很有诊断价值。spoof-only 设计诚实避开了真假混域捷径，但也意味着不能直接读安全工作点。脆弱点是各语合成器覆盖不均、时长偏斜，且外部标定阈值可能对某些语过严/过松。


# MultiAPI Spoof: A Multi-API Dataset and Local-Attention Network for Speech Anti-spoofing Detection

- 论文编号：1187
- 报告人：Xueping Zhang
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26p_interspeech.pdf

## 问题

既有反欺骗基准多依赖少数公开 TTS/VC，与工业闭源 API 生态差距大，模型在真实 API 假音上是否可靠未知。同时需要更细粒度的“假音来自哪个 API”溯源能力。

## 方法

构建 MultiAPI Spoof：约 230 小时英语假音 + 等量 CommonVoice 真音，来自 30 个 API（商业 TTS、开源模型、网页 TTS），标签 A0–A29。A0–A20 内 70/10/20 划分，A21–A23 仅开发、A24–A29 仅评测未见。提出 Nes2Net-LA：在 Nes2Net 嵌套块间加滑窗局部自注意（窗口半径 K=1），增强块间局部上下文。骨干统一 XLSR-300M；另设 API tracing：对 21 个 seen API 分类，低置信度判为 unseen。训练不加增强，4 秒切段。

## 实验与结果

不加 MultiAPI 训练时，模型在 MultiAPI 测试上 EER 较高（如 XLSR+AASIST overall 7.30%）；加入训练后降至 0.70%，未见子集亦改善，且 ITW、AI4T 同步受益。Nes2Net-LA 在 Data Collection 2 上 ITW EER 1.42%、AI4T 5.64%，优于同设置 Nes2Net/AASIST。Scoreq 分布显示该集质量跨度更广。API tracing：seen F1 约 0.936，unseen 召回偏低（eval F1 0.678）；t-SNE 显示未见 API 嵌入与 seen 混叠。

## 结论

多 API 数据可缩小研究基准与真实合成生态差距，并提升跨域检测；局部注意进一步增强细粒度伪造线索。API 溯源对未见源仍难，需更强不变表征。代码与数据已发布。

## 点评

同时做“检测数据补洞”和“溯源新任务”，贴近实战取证需求。质量分布更广的假音有助于解释跨域增益。脆弱点是仅英语、未见溯源召回弱，说明当前仍偏 API 特异声学指纹而非深层生成机制不变式。


# Aleatoric Style Uncertainty Augmentation with GMM for Domain Generalization in Anti-spoofing

- 论文编号：582
- 报告人：Jin Li
- 程序：Monday 28 September 2026 / Spoofing and Deepfake Detection 1
- 技术分类键：deepfake
- 全文：https://www.isca-archive.org/interspeech_2026/li26g_interspeech.pdf

## 问题

反欺骗在未见攻击域上易退化。风格增强（MixStyle/DSU/CSU）用特征均值方差合成新域，但常假设批内风格单峰高斯；多域混合批（不同说话人、编解码、噪声、伪造痕迹）风格多模态，单高斯会低估变差、限制可分性。

## 方法

提出 ASU：在通道风格统计空间建 K 分量对角协方差 GMM，对线 EM 式更新混合权重/均值/方差；将 within-component 方差定义为偶然风格不确定性，与批级 DSU 不确定性相加后做重参数化风格扰动。插入 WavLM + multi-head factorized attentive pooling 管线的训练分支，以概率 p 启用，推理关闭。设定 p=0.5、K=7、λ=0.9。在 ASVspoof5 Track1 open 做反欺骗，Track2 与 ResNet221 ASV 联做 SASV；对比 DSU、CSU 与融合 SOTA。

## 实验与结果

Track1：WavLM+MHFA+ASU 在 Eval 上 minDCF 0.108、EER 3.96%，优于基线 4.99%、DSU 4.77%、CSU 4.64%，且优于若干更大/融合系统中的单模型结果。消融显示批级变差与 GMM 偶然不确定均贡献增益。K 与 λ 敏感曲线在 K=7、λ=0.9 最优。bootstrap 显示 ASU EER 分布显著更低。SASV：ASU 的 min a-DCF 0.118、min t-DCF 0.192、t-EER 4.23，优于基线与 DSU/CSU。

## 结论

用在线 GMM 建模多峰风格偶然不确定性，可在不增加推理成本、无需额外标签下提升反欺骗与 SASV 的域泛化。代码已开源。

## 点评

把“批统计单峰假设”点破，用轻量风格空间混合模型补偶然变差，契合反欺骗训练批天然多域的现实。强项是训练期即插即用、推理零开销。脆弱点是 K/λ 需调、对角协方差忽略通道相关，且增益依赖上游 WavLM+MHFA 与已有强增强配方。

