# Speech Benchmarks, Evaluation, and Resources

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：12
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场资源与基准海报强调可复现、多条件、任务对齐的评测基础设施：无监督音素发现、巴西葡语自发语音、俄语韵律感知标注流水线、印度语统一 ASR/TTS 框架、偏好指令感知 ASR、开放排行榜，以及真实 ASR 幻觉与语码转换语义错误率。共同点是单数据集单指标无法刻画系统真实行为。

低资源与多语方面，DiscoPhon 用离散单元映射预定义音素清单；Spashta Audio-Bench 插件化注册模型/数据并引入 TTS-ASR 退化作可复现可懂度。领域资源上 Tarsila 聚合 70+ 小时自发巴西葡语；Balalaika 以语义 VAD、多 ASR ROVER 与重音/标点等丰富标注支撑去噪与 TTS。

新一代评测维度包括：Preference-ASR 测自然语言输出风格偏好；Open ASR Leaderboard 统一 WER/RTFx；HALAS 在真实财报电话上标幻觉跨度；CSER 量化语码转换中语言误识等对意图的影响，并与词汇指标互补。

## 论文技术总结

# DiscoPhon: Benchmarking the Unsupervised Discovery of Phoneme Inventories With Discrete Speech Units

- 论文编号：2791
- 报告人：Maxime Poli
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/poli26_interspeech.pdf

## 问题
语言文献需发现音素清单；SSL 离散单元是否在未见、类型多样语言上对应音素仍缺统一评测。既往基准多停在连续表征 ABX，未要求限数据无监督离散化与音素映射。

## 方法
发布 DiscoPhon：6 开发语 + 6 测试语（音系跨度大），每语约 10 h 训/2 h 验测，另有 10 min/1 h 低资源划分；预训练不得见任何基准语（含英语）。两赛道：many-to-one（256 单元→最频音素）与 one-to-one（单元数=音素数+静音，线性指派）。指标 PNMI、PER、R-value、F1，可选 ABX。基线为未接触基准语的 HuBERT/SpidR，预训练于 VP-20 或 MMS-ulab-v2，可零样本或 10 h 继续预训练。

## 实验与结果
Many-to-one：SpidR VP-20 最佳；10 h 微调后测试集平均 PER 61.67、R-value 53.27、PNMI 64.38。HuBERT 更易过分割（R-value 低）。One-to-one 难得多（SpidR 零样本测试 PER≈120）。语言间差异大（如微调后 Basque PER≈41%、Mandarin≈96%）；插入主导错误；替换多发生在相近发音类之间。

## 结论
基准表明当前 SSL 离散单元已含可观音位信息但跨语不均；SpidR 优于 HuBERT；严格一对一映射仍远未解决。资源公开于 cognitive-ml.fr。

## 点评
把“发现音素清单”落成可复现的离散单元评测，对 SSL tokenizer 与濒危语言文档化都有用。金标来自强制对齐，评测映射用了金标统计，严格意义上是诊断“可映射性”而非完全无监督清单发现；one-to-one 极难也点明层次聚类等方向。


# Tarsila-ASR: A Multi-Domain Test Suite for Benchmarking Brazilian Portuguese Speech Recognition

- 论文编号：450
- 报告人：Sidney Leal
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/leal26_interspeech.pdf

## 问题
巴西葡萄牙语（BP）自发语音含填充词、犹豫、截断与口音差异，现有公开资源虽多，但缺少统一、多域的自发语音评测基准，难以公平比较开源 ASR 并推动领域适配。

## 方法
Tarsila-ASR 汇总既有公开语料的测试子集（CORAA 各子集、CV17、MLS、MuPe、NURC-SP、TEDx 等），统一保留 text/duration/audio，并加 origin 与 voice-gender-classifier 估计的 gender；音频统一 16 kHz。得到 62,094 条、72.46 小时（女/男约 48%/52%）。在此基准上零样本评测 MuPe-ASR、Whisper-large-v3、Omnilingual 7B；再将各自发语音语料的 train/val 拼成约 1,156 小时训练 + 39 小时验证，微调 Distil-Whisper、Whisper-medium/large-v3、Omnilingual 300M/1B（7B 仍零样本），报告 WER/CER、RTF、BERTScore、SeMaScore（mDeBERTa-V3-base）。

## 实验与结果
零样本均值 WER：MuPe-ASR 21.63、Whisper-large-v3 33.03、Omnilingual 7B 51.71，朗读子集明显好于自发子集。微调后 whisper-large3-ft-75k 达到整体最优：WER 15.40、CER 9.11、BERTScore 97.84；distil-whisper-ft-200k WER 16.52 且平均 RTF 更低。与既往系统比，wlarge3-ft-75k 在 CV17/CORAA/NURC-SP/MuPe 上均值 WER 15.82，优于 MuPe-ASR 的 21.27。训练步数并非越长越好（如 ft-200k 优于 ft-750k）。

## 结论
作者认为统一多域自发语音基准暴露了预训练与真实对话域差，领域微调可将错误率压到约 15–19% 并刷新 BP 自发语音开源 SOTA；资源与 checkpoint 已公开。后续拟扩展基准、改进转写规范化与风格平衡，并联合考察准确率、效率与语义保真。

## 点评
工作重心是“把已有公开测试集合起来 + 系统微调”，对 BP 对话 ASR 很务实。强项是子集级 WER 与效率/语义多指标并存，能看见朗读–自发权衡；弱项是基准依赖既有测试划分与标注惯例，结论对数据拼合与 checkpoint 选择敏感，未必直接迁移到其他语言变体。


# Balalaika: Data-Centric, Prosody-Aware Annotation Pipeline for Russian Speech

- 论文编号：83
- 报告人：Vasiliy Kudryavtsev
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/borodin26_interspeech.pdf

## 问题
俄语网络语音难规模化标注：元音弱化、腭化、移动重音影响韵律与意义，现有管线多依赖人工或有声书、忽视韵律/音素细节，限制去噪与 TTS 等生成式语音任务。

## 方法
Balalaika 开源管线：SmartTurnV3.1 语义 VAD 切分（语音占比≥70%、内部静音≤1 s，块长约 5–15 s）；过滤短于 3 s、CREST>10、NISQA-S MOS<4.2、以及 pyannote 检出重叠/多说话人段落；五路 ASR（GigaAM-CTC±LM、GigaAM-RNNT、Vosk、T-one）经 ROVER 融合，保留 CTC+LM 词级时间戳；再以 RuPunctBig 补标点、RuAccent 加重音与 ё 归一、自训轻量 Transformer G2P 出 IPA。用该管线从多源俄语资源得到约 5,078 小时多层标注语料。在等预算下用 SEMamba 训去噪、VITS 训 TTS，并做重音/标点/MOS 阈值消融。

## 实验与结果
相对 11 个公开俄语语料，Balalaika 在 NISQA 各维、UTMOS、人工 MOS（约 4.601）与 TMR 上整体最优。等预算去噪中，在 Balalaika 上训练的 SEMamba 多数指标（含 CSIG/CBAK/COVL/PESQ/STOI/SI-SDR 等）领先。等预算 TTS 中客观质量与人工 MOS（约 3.618）最高、CER 约 0.1062，IntMOS 次于单说话人 RUSLAN；消融显示重音+标点联合最好，且 MOS>4.2 严过滤优于更松阈值。

## 结论
作者认为数据中心、韵律感知标注可产出更高质俄语语料并提升等预算下的去噪与 TTS；管线模块化但当前依赖俄语专用组件。局限包括等预算未训满收敛、TTS 测试集与部分源域部分重叠。

## 点评
抓的是“标注层（标点/重音/音素/时间戳）+ 质量过滤”如何改变下游生成质量，而不是新模型结构。等预算对比设计清楚，消融能支撑重音与标点的互补；脆弱点在语言相关工具链与测试域对齐，跨语种直接复用成本高。


# Spashta Audio-Bench: Unified ASR and TTS Evaluation Framework across Indian Languages

- 论文编号：1777
- 报告人：Bikash Dutta
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dutta26_interspeech.pdf

## 问题
印度语言语音评测碎片化：模型在互不重叠的数据集上、用不一致的预处理与指标评测，难以复现与公平比较；TTS 又常只看主观自然度，掩盖可懂度失败。

## 方法
Spashta Audio-Bench 做成类 HuggingFace Evaluate 的可插拔框架：数据层接入公开测试集，预处理统一 16 kHz 单声道与 UTF-8 小写去标点，模型层注册 ASR/TTS checkpoint，评分引擎多指标汇总并出排行榜。ASR 报 WER/CER；TTS 用 IndicConformer 作 oracle 算 TTS→ASR 退化（可懂度），并报 FAD、DNSMOS/P.808 预测 MOS。在七个语料（IndicTTS、IndicVoices/R、RASA、Nirantar、OpenSLR、SVARAH 等，至多 22 语 + 印度口音英语，累计约 644 小时评测音频）上评十个开源 ASR/TTS，均用公开权重、不加微调。

## 实验与结果
ASR：无单一架构通吃——如 AudioX-S 在 IndicTTS WER 26.74% 优于 IndicConformer 31.58%，AudioX-N 在 RASA 最强（20.90%）；同语言跨数据集 WER 可差逾 30 点；低资源语（如 Maithili 58.29%、Dogri 56.71%）远差于 Hindi 23.76%，Urdu 最低 9.38%。TTS：自然度与可懂度脱节——Parler 预测 MOS 约 4.13–4.15 但 TTS→ASR WER 非最低；MMS-TTS 可懂度最好（WER 36.14%、CER 9.60%）而 pMOS 相对较低；Veena FAD 最低（IndicTTS 3.52）但 TTS→ASR WER 最高（53.79%）。讨论强调参数放大不保证跨语鲁棒，领域敏感与架构归纳偏置仍关键。

## 结论
作者认为模块化统一评测能暴露单数据集、单指标看不见的结构问题，并释放可复用基础设施，使多指标评测成为印度语言低资源语音的默认做法。

## 点评
贡献在评测基础设施与“TTS 可懂度–自然度双轴”，而非新识别/合成模型。用 IndicConformer 作 TTS oracle 实用但会把 oracle 偏差带进可懂度排序；预测 MOS 对印度语语音学校准不足也是正文自承的限制。


# Preference-ASR: A Preference-Aware Test Set for Benchmarking ASR in the Era of Speech LLMs

- 论文编号：728
- 报告人：Nithin Rao Koluguri
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koluguri26_interspeech.pdf

## 问题
主流 ASR 测试集在数字、不流畅、实体与大小写等标注惯例上不一致，标准归一化又抹掉用户关心的格式差异；SpeechLLM 虽能跟自然语言偏好指令，现有基准测不到“是否按偏好输出”。

## 方法
Preference-ASR 从七个开源语料（AMI、Common Voice、Earnings-22、GigaSpeech、LibriSpeech、SPGISpeech、VoxPopuli）取约 3,545 条并人工校 GT；两阶段用 Qwen3-30B-A3B：先分类偏好类别（normalization / entities / disfluencies / case），再生成指令与偏好参考，人工复核后得 3,210 条 (audio, instruction, reference) 三元组（另 335 条无偏好基线）。提出 preference-aware normalizer：按当前指令选择性跳过 TN/ITN、保留/剥离不流畅、跳过小写化等，再算 WER。评测 Parakeet-TDT-0.6B-v3（无指令）、Canary-Qwen-2.5B、Phi-4-Multimodal、Qwen3-Omni-30B，对比 default 与 instructed。

## 实验与结果
标准归一化下 Canary-Qwen 与 Qwen3-Omni 默认总体 WER 接近（约 5.64% vs 5.66%），但对指令反应不同：Qwen3-Omni 实体 WER 从 5.12% 升至 12.85%（提示词实体幻觉）；Phi-4 不流畅默认 50.18%、指令后 10.46%，但 case 指令反而恶化（3.93%→19.76%）。偏好感知 WER 下排名重排：如 normalization 上 Qwen3-Omni (I) Pref 9.84% 优于 Canary-Qwen (I) 11.32%；实体幻觉在 Pref 下仍约 12.68%。Canary-Qwen 对指令整体几乎平坦。

## 结论
作者认为该测试集与选择性归一化能暴露传统 WER 看不见的偏好遵循差异；局限为仅英语、尚无多说话人偏好，且 LLM 生成偏好文本需人工核验（尤其 normalization）。

## 点评
对准 SpeechLLM 时代“指令跟从 vs 声学证据”的评测缺口，四类偏好与选择性归一化器设计清楚。脆弱处在实体上下文偏置与提示敏感：强指令模型可能为跟提示而幻觉，结论高度依赖人工复核后的参考质量。


# Open ASR Leaderboard: Towards Reproducible and Transparent Multilingual and Long-Form Speech Recognition Evaluation

- 论文编号：1902
- 报告人：Eric Bezzam
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/srivastav26_interspeech.pdf

## 问题
ASR 开源与商用模型、数据集激增，开发者难选基线与公平对比方式；多数基准偏英语短音频，跨工具包评测不统一，单 WER、单数据集不足。

## 方法
Open ASR Leaderboard 提供可交互排行榜与开源评测脚本：截至 2026-03-27 覆盖约 86 个系统（26 家机构）、11 个数据集；统一跨 ESPNet / NeMo / SpeechBrain / Transformers 与多家商用 API。三条赛道——英语短音频（<30 s）、多语短音频（德/法/意/西/葡）、英语长音频（>30 s）。报告强归一化后的平均 WER 与 RTFx（音频总时长/转写时间）；社区以 PR 提交评测脚本与自报指标，经维护方复验后上榜。

## 实验与结果
短英：Conformer/FastConformer + LLM 解码整体平均 WER 更优（如表中 Zoom Scribe v1 约 5.80、Cohere Labs Transcribe 5.84、IBM Granite Speech 4.0 1B 5.87 等），但 RTFx 常低于 TDT/CTC；Parakeet TDT 0.6B v2 等吞吐更高但 WER 排名靠后。多语：闭源 ElevenLabs Scribe v2 平均 WER 约 2.67 领先；开源中 Voxtral Small 24B 约 3.70 等。长音频：闭源优势更大（如 ElevenLabs 9.05），开源中 Conformer 系仍较强，CTC/TDT 更适合大批量。约 31% 开源模型沿用 Whisper encoder；扩展语种覆盖有时伴随英语 WER 变差。

## 结论
作者认为标准化归一化与 RTFx 使准确率–效率可比较，并开源代码与数据加载以支持可扩展社区评测；未来拟扩语言/领域、加更多指标与私有评测集，并区分是否需保留不流畅的 verbatim 任务。

## 点评
基础设施型贡献：跨工具包对齐与双指标排序对选型很实用。正文也提醒架构结论与训练数据/规模纠缠；强归一化会抹掉标点/大小写/不流畅差异，不适合测偏好格式能力。


# HALAS: A Human-Annotated Dataset of Hallucinations of Modern ASR Systems

- 论文编号：337
- 报告人：Mateusz Barański
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/baranski26_interspeech.pdf

## 问题
端到端 ASR 会在自然语音上幻觉（无语音对应的插入、改意、循环重复），但既有检测/缓解多在非语音或人工加噪上评测，缺少真实未处理语音上的人工标注基准。

## 方法
在 Earnings-22 全量上跑七个低 WER 开源模型（Whisper large v2/v3/Turbo、CrisperWhisper、Canary-1B/Flash、Parakeet-TDT v2）；用去循环+归一化后的模型间平均 WER 挑难例；10 名标注员按“无语音对应”定义标 span（Hallucination / Looping / Looping Hallucination），双人标+仲裁（κ=0.87），并校正参考。得 HALAS：3,611 段，train 2,866（HR 33.6%）、test 745（HR 22.6%，>1 s 且≥3 词）。用代理指标做 ROC-AUC，并用 XGBoost / LLM 比对 / 解码器嵌入分类器（含多层扩展）做检测基准。

## 实验与结果
各模型幻觉率约 21.4–43.8%，循环约 1.1%；幻觉短语高度偏斜（平均 top-10 覆盖 55%），跨模型短语重叠明显；低 WER（可至约 6.25%）仍可幻觉。GPT-4o mini 严重度标注显示要么偏轻微填充、要么严重改意。代理指标中 CER/SeMaScore AUC 约 0.81/0.80，PPL 仅约 0.60。检测：Wv3 上 DE 单层 F1 53.1%，多层 DE 2,13,23 达 56.1%，优于参考依赖 LLM 判定；在非语音增强集上 F1 更高，说明 HALAS 更难。

## 结论
作者认为 HALAS 首次在真实语音上提供人工幻觉标注与检测基准，暴露跨模型共性与检测难度；数据集与推理配置已公开。注意采样偏向高模型分歧，不代表部署场景自然发生率。

## 点评
把评测从“非语音幻觉”拉回 earnings 通话真实错误，span 标注与跨模型分布分析有信息量。检测数字说明参考+LLM 也不够，嵌入分类器仍仅中等 F1；因故意富集难例，直接外推到“日常幻觉率”会偏高。


# CSER: Semantic Evaluation of LLM Auto-Repair for Code-Switching ASR

- 论文编号：3390
- 报告人：Tien Dat Bui
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bui26_interspeech.pdf

## 问题
语码转换（CS）ASR 仍主要用 WER/CER/PIER 等字符串匹配指标；在 ASR–LLM 语音助手中，音译/同音误识可能仍保留意图，传统指标无法衡量语义保持与 LLM 自动修复后的下游意图质量。

## 方法
提出 Code-Switching Semantic Error Rate（CSER）：ASR 假设经 LLM 做 CS 感知规范化（映射音译 OOV、保结构、去标点小写、禁止幻觉新内容）后，由另一 LLM 从参考生成针对 CS 实体与意图谓词的探测问题，再抽取参考/假设答案并由判别器判等价，CSER=1−问题级成功率。配套越–英 CS 基准：爬取种子实体 + GPT-4o 造句，人工录制（句内/句间）与 TTS（多样/媒体域）四套测试集，训练集约 794K 句。对比 Azure、Google v1/Chirp 3 等商用系统，以及 Conformer-CTC 的 VN / VN-EN Phonetic / VN-EN 训练体制；评测用 Gemini 2.0 Flash 作裁判，与数据生成模型族分离。

## 实验与结果
Phonetic 训练常 PIER 远差于正字法 CS 训练（如 Set 4：58.65 vs 24.72），但 CSER 接近（12.16 vs 10.08），说明 LLM 可修复“phay buc→Facebook”类音译。Google Chirp 3 各集 CSER 最低（约 10.47/9.14/22.03/23.52）；Google v1 在部分集 WER 尚可但 CSER 很高（Set 4 达 51.33）。VN 单语在 Set 2 PIER 82.10 但 CSER 仅 17.20，相对 VN-EN 的 CSER 改善远小于 PIER 暗示的幅度。

## 结论
作者认为面向意图的 CSER 是 CS ASR–LLM 管线的必要补充，能反映音译的语义韧性；目标 CS 训练（含 phonetic）可接近生产级语义表现。局限包括计算开销与裁判偏差风险，未来拟做人相关与蒸馏裁判。

## 点评
把评测目标从“词对不对”挪到“意图能不能过 LLM 修复”，对助手场景很贴切。CSER 强依赖规范化与裁判 LLM 设定，测的是管线上限而非纯 ASR；与 PIER 并读才看得出“词错但语义可救”的悖论。

