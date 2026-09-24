# Speech Synthesis Evaluation 1

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：7
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场集中反思 TTS 主观评测的效度与维度：大规模成对偏好需语言控制与多感知维度标注；应用情境会显著改变同一系统得分；“自然度”并不等同于跨域“适宜性”；非语言发声（NV）需要功能分类学基准；训练期需要可解释的语音学客观指标；指令式 TTS 的性别偏见呈多维社会线索绑定效应。共同信息是：单一 MOS/自然度分数不足以指导系统选择与优化。

印度语族大规模成对评测（10 语、7 系统、逾 12 万比较）示范可扩展但高方差场景下的多维标注；应用情境实验与跨域适宜性研究则指出生态效度与目标用例必须进入实验设计。NV-Bench、元音空间指标与 ITTS 偏见分析分别补齐副语言可控性、训练期可监测口音相似性，以及提示组合带来的交互偏见。整体趋势是评测协议本身成为一等研究对象。

## 论文技术总结

# Preferences of a Voice-First Nation: Large-Scale Pairwise Evaluation and Preference Analysis for TTS in Indian Languages

- 论文编号：3357
- 报告人：Ashwin Sankar
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/anand26b_interspeech.pdf

## 问题
众包成对评测可扩展，但印度多语与语音多维感知方差大；绝对 MOS 难诊断，仅报总体偏好无法解释“为何更好”。

## 方法
构建 5357 句、10 语基准（含规范化/符号/语码混合与 16 域）。1900+ 母语评委、>120K 成对比较，先锁总体偏好再评 6 维（可懂度、表达、音质、活泼、噪声、幻觉）。Bradley–Terry+Elo 排行，bootstrap CI；XGBoost+SHAP 解释轴对偏好的贡献；分析评委数/句数对排名稳定的影响。

## 实验与结果
排行：Gemini 2.5 Pro TTS > ElevenLabs V3 ≈ Sonic3 > … > IndicF5。Gemini 在 9/10 语与多数域领先；表达与可懂度对总体偏好贡献最大（SHAP），噪声/幻觉因多数系统已较强而区分度低。约 100–200 评委、~1000 句可达 ρ≥0.95 的排名一致。轴级判断可跨语预测总体偏好（准确率约 86%）。

## 结论
可控多维成对评测能稳定排出 Indic TTS 榜，并揭示偏好主要由表达与可懂度驱动；公开基准与偏好数据。

## 点评
规模与协议（先总体后分轴）设计扎实，对“可扩展又要可解释”的评测很有参考价值。商用系统主导榜单也暴露开源 Indic 差距；信噪/幻觉轴饱和时解释力下降，需更难的失败样本。


# Application context in speech synthesis evaluation: A problem and a solution

- 论文编号：747
- 报告人：Fritz Seebauer
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/seebauer26_interspeech.pdf

## 问题
合成语音评测常在“中性”孤立句上做 MOS，假定质量可模块化、与应用无关；生态效度不足，且跨场景比较可能混淆系统差异。

## 方法
80 名德语母语者，4 任务×4 系统拉丁方：学习对话、寻物导航（WoZ）、自由对话、听短故事；系统为 Tacotron2+WaveNet、VITS、Auralis/XTTS-V2、Orpheus。实体公寓与其 Unreal 数字孪生并行。评总体质量、听努力度、自然度等与短版 UEQ。贝叶斯层级模型检验任务、系统及交互；ROPE 判定实际等价。

## 实验与结果
导航任务在总体质量、听努力度、自然度等上显著更高；任务×系统交互在听努力度、语调、音质、愉悦度等上超出 ±10 ROPE。部分维度（UEQ、外向性等）更接近等价。VR 与实体条件统计可比（RQ3）。

## 结论
应用语境显著且系统依赖地改变合成语音评分；未指定场景的系统对比可能混淆。数字孪生可作为更生态评测的可行路径。

## 点评
交叉设计直接冲击“中性评测可迁移”假设，对工业选型很实用。VR 等价是降低成本的亮点。任务顺序固定、系统含未知商用数据，因果解释需谨慎。


# Is Natural Always Appropriate? Investigating Naturalness and Appropriateness Across Different Domains for TTS Evaluation

- 论文编号：3392
- 报告人：Dominika Woszczyk
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/woszczyk26_interspeech.pdf

## 问题
TTS 保真提升后，单一“自然度”难反映是否适合下游用途；合适性如何随域变化、与人类相似度是否一致，缺少系统证据。

## 方法
150 名英语听者，拉丁方评 5 系统（Kokoro、Gemini TTS、Kyutai-TTS、GPT-4o-mini-tts、ElevenLabs）+ 真人，覆盖朗读、演员、动画角色、助手、自发说话者等人格；刺激来自 LibriQuote、MSP-Podcast、MELD、AnimeVox 等。同时报人类相似度与“说服力/合适性”，并分析声学特征与自动指标相关。

## 实验与结果
合适性跨域独立于自然度：Kokoro 适朗读/助手但弱于对话；Kyutai 适自发对话但弱于助手/动画。人类相似度与合适性在 Actor/Spontaneous/Reader 正相关，动画近零、助手负相关（ρ≈−0.44）。动画偏好更高节奏波动，助手偏好更稳、更低 f0 范围。单一自动指标难以普适预测合适性。

## 结论
TTS 未“通吃”：优化一域可伤另一域；自然度会惩罚风格化、奖励自发性，需域感知评测。

## 点评
把自然度与合适性拆开并跨域对照，直接服务产品选型。低评者一致性（α≈0.2）说明合适性主观且期望驱动，榜单需报告域与协议。助手“略机器感更合适”的现象值得后续验证。


# NV-Bench: Benchmark of Nonverbal Vocalization Synthesis for Expressive Text-to-Speech Generation

- 论文编号：2211
- 报告人：Qinke Ni
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/ni26_interspeech.pdf

## 问题
表达 TTS 越来越多纳入非语言发声（NV），但评测缺标准、缺配对真人参考，常只能粗查“有没有事件”，无法量化与真实录音差距。

## 方法
发布 NV-Bench：1651 条多语（中/英）野外话语、配对 GT，按 Batliner 功能分类覆盖 14 类 NV；平衡单标签与相对平衡多标签子集。训多语 NV-ASR（SenseVoice-Small 微调）作自动评委。双维协议：指令对齐（CER/PCER/OCER）与声学保真（SIM、DNSMOS、FAD/FD、主观）。评 Orpheus、CosyVoice 变体及自训 NV-CV3/NV-FlexiVoice。

## 实验与结果
NV-ASR 在标准 ASR 与 NV 集上可靠（如 SMIIP-NV CER 1.29%）。多数模型 PCER 仍高（控制弱）；NV-CV3、NV-FlexiVoice 在对齐与保真上整体更强。客观指标与人类感知相关，可作标准化框架。

## 结论
NV-Bench 把 NV 当作交际行为评测，分离“控不住”与“听不真”；公开测试集与协议支撑可复现对比。

## 点评
配对 GT + 平衡类别 + PCER 是相对现有“有没有笑声”评测的实质进步。依赖 NV-ASR 作裁判，其标签错误会传导；多标签子集仍受长尾共现约束。


# Phonetically Grounded Vowel Space Metrics for Evaluating Synthetic Speech During TTS Model Training

- 论文编号：1579
- 报告人：Pasindu Udawatta
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/udawatta26_interspeech.pdf

## 问题
训练中反复做听感测试不现实，损失曲线又缺语言可解释性；需能在训练过程中跟踪口音/元音系统学习的客观指标。

## 方法
提出 Vowel Space Overlap（合成与真值元音空间多边形交面积）与 Procrustes Normalised Disparity（去位姿/尺度后的形状残差）。在 GAE 预训练 Tacotron 2 上分别微调 NZE 与 GIE，多步提取角元音 F1/F2，算两指标；听者评目标口音相似度并与指标做 Pearson 相关。

## 实验与结果
两口音上，Overlap 最大与 Procrustes 最小的步数与视觉最佳形状对齐（NZE≈3000、GIE≈24000）。指标与感知口音相似度显著相关，可作损失曲线的可解释补充。

## 结论
元音空间几何指标可在训练中提供感知相关、语音学可解释的监控信号，并在多口音上稳健。

## 点评
把“看图收敛”落成可复现度量，对口音适应实验很实用。依赖角元音与强制对齐/共振峰估计，噪声与错误切分会扰动；目前仅 Tacotron 2 与两口音，外推到神经声码器端到端系统仍待证。


# The Binding Effect: Analysis of How Multi-Dimensional Cues Form Gender Bias in Instruction TTS

- 论文编号：66
- 报告人：Kuan-Yu Chen
- 程序：Tuesday 29 September 2026 / Speech Synthesis Evaluation 1
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/chen26b_interspeech.pdf

## 问题
指令式 TTS（ITTS）评测性别偏见多做单属性探测，忽略社会地位、职业刻板与人格描述等线索的组合；现实提示下的 Binding Effect 会改写单维先验，掩盖交叉偏差。

## 方法
将控制空间解耦为 Social Status、Career、Persona（Big Five）三轴；Stage1 测单描述符的女性声学概率 \(P(x)\)（wav2vec2 性别分类器）；Stage2 构造双/三维组合，在 logit 空间量化相对加性基线的交互项 \(I\)。评 VoxInstruct、PromptTTS++、Parler Mini/Large；每描述符 100 条性别中性内容句。并比对文本编码器语义先验与训练数据人口分布。

## 实验与结果
单维上职业/人格常强偏女性；组合后出现显著 Binding Effect 与主导覆盖（如高地位+reckless 可翻转 nurse 的女性先验）。交互模式与预训练文本编码器语义先验强相关，不止训练数据倾斜。通用多样性提示难覆写这些组合偏差；上下文属性插入更可行。

## 结论
ITTS 性别偏差具组合依赖，需成分化诊断；偏见根源更多在文本编码器先验。缓解应面向组合动态而非单维提示。

## 点评
把交叉社会线索写入可控实验，比“测 nurse 是否女声”更贴近部署。依赖声学性别分类器作代理，音色/F0 与社会性别不完全等同；提示模板由 Gemini 生成，也可能引入额外先验。

