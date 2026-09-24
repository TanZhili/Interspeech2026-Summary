# Corpus Creation, Summerisation and Understanding

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
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

本场把“语料如何建、摘要如何做、理解如何可比可复现”连成一条数据—评测—应用链。长会议文档摘要强调在多段候选组合中用树搜索与自奖励做免训练选择，以缓解多阶段管线误差累积与参考摘要质量差的问题。统一实验框架则针对后处理不一致导致的评测不可比，以及跨数据规模/管线的训练难复现。

低资源场景同时覆盖跨语言文本/语音摘要、语言文献记录中的 ASR 冷启动优先级、以及人机协作会话语料构建与质控角色分工。另一条线用 IPA 引导的双转录做数据中心式语料精炼，把口语—书面对齐锚定在语音实现上，以服务文本规范化与领域 ASR。

趋势可概括为：摘要从黑盒端到端转向可组合、可搜索；语料工程强调可及工作流、阈值门控人机验证与语音学约束的规范化；评测与训练协议统一成为“选型可部署”的前提。

## 论文技术总结

# Segment-level Tree Search for Long Meeting Document Summarization

- 论文编号：3011
- 报告人：Sangwon Ryu
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/ryu26b_interspeech.pdf

## 问题
长会议转写信息稀疏、话题跳变，多阶段 extract-then-summarize 易累积误差且缺中间校验；参考摘要过短又诱导过度压缩。即便 LLM 上下文超过 100K，仅靠加长输入仍难充分覆盖全局分散要点。

## 方法
提出免训练框架 S3：滑窗切段（w=2048，r=256）并对每段采样 k=5 候选摘要（nucleus 或 DBS），离线建树；用自奖励引导的 MCTS（UCT，c=1.0，30 次模拟）选路径，奖励为 Coherence/Consistency/Fluency/Relevance 的 Likert 归一化均值；最后 refinement 去掉跨段冗余套话。对比整篇摘要基线、Refine、以及每段单候选的 S2。

## 实验与结果
数据 QMSum；骨干含 Qwen2.5-7B/72B、Gemma-3-12B。G-Eval 上 S3-7B 平均 4.56，超过同骨干基线与 72B 摘要级基线（4.54）；S3-12B 达 4.74。按长度分箱时 Base 在长文上相关性下降且摘要占比 <1%，S3 更稳、摘要约占原文 4.66%（参考仅 0.62%）。nucleus 采样优于 DBS（Avg 4.56 vs 4.51）。ROUGE-1 反而偏低，与参考过短、惩罚信息丰富输出一致。

## 结论
结构化段级组合优于单纯放大模型或依赖超长上下文；S3 能生成更合适长度、覆盖更全的会议摘要。

## 点评
把长文摘要写成「段候选组合搜索」，用自评估奖励绕开短参考监督，方向清晰。强在 7B 逼近/超过 72B 整篇生成，且长度分箱证据扎实；脆弱点在自奖励与生成模型同源可能自我偏好，以及计算开销（每段多候选 + MCTS），且 ROUGE 与 G-Eval 背离时需依赖人类/裁判模型校准。


# A Unified and Reproducible Experimentation Framework for Speech Understanding

- 论文编号：1225
- 报告人：Jing Peng
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/peng26e_interspeech.pdf

## 问题
语音理解评测常因后处理、归一化与打分不一致而不可比；现有基准模型族覆盖窄、少做真实应力场景；异构训练数据与流水线又使架构对比难复现。部署选型需要统一协议下的可复现实验框架。

## 方法
提出 SURE：统一预测格式、归一化与打分；引入相对性能分 RPS（相对同流水线当前最优归一化到 [0,1]）。三轨道——Track I：前端感知情景应力（噪声、混响、会议、码混、方言、热词等）；Track II：全栈理解横向对比（ASR、GR、S2TT、SER、SLU 等）；Track III：Agent 辅助把「论文+代码」转为可运行 SWIFT 配方，在匹配开放数据子集上从头训做受控架构比较。评测栈含 meeteval、sacrebleu 等固定后端。

## 实验与结果
Track I：会议 SA-ASR 上级联仍有竞争力（如 Diarizen+DiCoW 在 AMI 上 DER/cpWER 30.21/17.26，优于 VibeVoice-ASR 的 41.26/36.80）；不同系统在码混/方言/噪声/热词上各有长短。统一归一化可使 LibriSpeech 上某系统相对报告数字的 RPS 偏移约 0.3。Track II：级联在干净感知任务仍可竞争；情感识别普遍难；部分 Speech LLM 输出格式不遵从会拖垮自动指标。Track III：同协议下 Qwen2-audio 与 TASU(SFT)-2B 对比，后者在 GR/SER 等副语言任务落后，语义任务（SLU、S2TT）更接近。

## 结论
SURE 标准化评测并提供情景套件与受控训练转换流，开源可扩展，面向部署选型的可比与可复现。

## 点评
抓的是「评测协议与训练方差」而非新模型结构，对社区基建价值高。RPS 便于跨任务汇总但依赖动态榜单最优，解释时需看任务级指标。Track III 仍是初步，Agent 转换对非标准仓库可能需人工补丁，架构结论外推应克制。


# Bridging Languages and Modalities: Lightweight Cross-Lingual Text and Speech Summarization for Low-Resource Scenarios

- 论文编号：2655
- 报告人：Chaimae Chellaf
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/chellaf26_interspeech.pdf

## 问题
跨语言摘要需在另一种语言中压缩并重构语义；级联「翻译/ASR→摘要」易误差传播，低资源语音跨语言摘要资源尤为稀缺。现有端到端工作多偏高资源文本或高资源语对。

## 方法
统一轻量框架：文本经 BGE-M3 句向量、语音经与之对齐的 SENSE 话语嵌入；去掉 BARThez 编码器 token embed，改为句/话语级输入，经线性投影（GeLU）送入修改后的 seq2seq（SBARThez），解码器仍产出法语摘要。两阶段训练：先在 MLSUM 法语上用句嵌入适配；再按任务用文本或语音嵌入微调。嵌入模型冻结，仅训投影层与 seq2seq（约 140M 可训参数）。发布低资源语音评测集 ABT-SpeechSUM（亚美尼亚、布列塔尼、突尼斯阿拉伯语），由译文用 GPT-4o mini 合成法语摘要并人工抽检。

## 实验与结果
文本 CrossSum（X→FR）：高资源上级联常更强，但日语上 SBARThez 更优；多数低资源语上 SBARThez 超过级联与 mT5-large，且可训参数仅 140M（总约 700M）。语音：SBARThez-speech 在三种低资源语上 Rouge-L/BertScore 优于 Whisper 级联基线；仅用译文句嵌入训练的 SBARThez-text 跨模态评测语音时仍有竞争力，布列塔尼与亚美尼亚上可超过级联。Table 4 数值行在全文抽取中被截断，具体分数无法完整复述。

## 结论
语义对齐的句/话语嵌入可支撑低资源跨语言、跨模态摘要，且参数量显著小于十亿级级联；ABT-SpeechSUM 为该方向提供开放基准。

## 点评
把跨语言摘要做成「共享语义嵌入空间上的轻量解码」，避开 ASR/MT 级联，对无 MT 覆盖的语言尤其有意义。强在可训参数少与跨模态零资源迁移迹象；脆弱点在合成参考摘要、法语单目标、以及语音集规模很小（如 Breton 训练仅约 0.41h），自动指标提升未必等于事实保真。正文末表抽取不全，已在结果中标明。


# Easper: An Accessible ASR Pipeline for Language Documentation

- 论文编号：2781
- 报告人：Aso Mahmudi
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/mahmudi26_interspeech.pdf

## 问题
语言文档中转写是瓶颈；Whisper 等可微调，但田野语言学家缺工程能力。冷启动时不知应优先标哪些录音——声学干净（高 SNR、少重叠）还是语言丰富（词汇多样/重复）——缺少实证指南。

## 方法
发布 Easper：从 ELAN 导出→校验（>30s、重叠等）→云端（如 Colab）微调 Whisper-small / XLS-R→本机 diarization（SpeechBrain 或 pyannote）+ 转写写回 ELAN。优先策略实验以「整场录音 session」为不可分割单位，提取 SNR、重叠率 OVR、TyTo（type-token）、以及时长归一的 ToTy（token/type×duration）；按 Baseline 随机、SNR、最少重叠、TyTo、ToTy 五种排序逐步加入训练池，全量微调 Whisper-Small（3 epoch/步，batch 8，lr 1e-5），以 CER 衡量后期编辑成本。

## 实验与结果
三种瓦努阿图语言：Bislama（13h45m）、Nafsan（14h50m）、Nguna（1h01m）。学习曲线显示早期 ToTy 优先通常 CER 最低；SNR/最少重叠并不更优。作者认为基础模型已较抗田野噪声，缺的是目标语词汇与拼写规则，故早期喂入高词汇密度/重复会话更有效。全文在「Lexical Breadth and Depth」处抽取截断，后续定量细节与结论段不完整。

## 结论
可读部分表明：冷启动应优先语言分布（丰富度与重复）而非声学洁净度；Easper 把无代码 workflow 与该选择策略绑定，便于人在环迭代。

## 点评
同时解决工具可达性与数据选择策略，贴近真实「按场次转写」工作流。ToTy 设计针对「重复利于学习」合理；脆弱点在 session 级不可分割可能混入噪声片段，且 Nguna 极小、学习曲线有 catastrophic forgetting 尖峰。正文后半抽取截断，点评未编造未读到的数字。


# VāṇīSetu: A Human-AI Collaborative Framework for Scalable Conversational Speech Corpus Creation in Low-Resource Settings

- 论文编号：2607
- 报告人：Rishabh Kumar
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26h_interspeech.pdf

## 问题
农村印地语等场景需领域对话语音数据，但手工校对成本约 6–8× 实时；噪声、方言与码混使通用 ASR 脆弱。需要可扩展的人机协同建库流程，并量化后处理对标注负担的影响。

## 方法
VāṇīSetu 四阶段：领域关键词引导从 YouTube 采集→VAD、PyAnnote 说话人分离、IndicWav2Vec/KVWav2Vec ASR、强制对齐→mT5/ByT5 或 LLaMA/ChatGPT 后校正→增强版 Vāgyojaka 上 Annotator→Validator→Verifier 三角色、阈值门控激励（λ=5%，δ=2%）。案例产出 KrishiVāṇī（约 100h 印地语农业对话）。ASR 上用 65h IndicVoice + 10h 领域数据训 KVWav2Vec；评测分 KV-Known / Unknown / OOD。

## 实验与结果
KVWav2Vec 在 Known/Unknown 上 WER 优于 IndicWav2Vec 与 IndicConformer（如 Known 22.38 vs 23.70/24.20）；OOD 上 IndicWav2Vec 略优。后校正中 mT5 在 Known/Unknown 上最好（22.29 / 25.70），ChatGPT ICL 在 OOD 最好（22.62）；mT5 延迟最低（0.97s）。相对全手工，验证流水线标注时间降 61.1%（95% CI [57.4%, 64.8%]，p<0.001）；协议一致性 Krippendorff’s α=0.87。

## 结论
角色分离 + 激励门控 + 小模型领域后校正，可在保持保真的前提下大幅降本；领域适配 ASR 有助 in-domain，OOD 仍宜保留通用基线。

## 点评
贡献重心在可度量的人机标注操作系统，而非单纯刷 WER。mT5 胜过更大 LLM 的 in-domain 结果对低成本流水线有直接启示；脆弱点在 YouTube 版权/代表性、激励阈值对标注行为的诱导，以及农业印地语特性对其他领域的迁移程度。


# IPA-Guided Dual Transcription for Data-Centric Speech Corpus Refinement

- 论文编号：2221
- 报告人：Jeong-Ju Choi
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/choi26f_interspeech.pdf

## 问题
口语实现与正字法之间是多对多映射（日期、数字、缩写等），导致语料转写不一致，拖累下游 ASR/合成。纯文本 TN 看不到实际发音；已有双文本 STT 也未把识别器输出的音素流直接喂给下游消歧模型。

## 方法
数据中心框架两段：(1) Phoneme Intermediate Conditional（PIC）音频编码器——Conformer N=12，中间层 k=9 用 CTC 预测 IPA，末层 CTC 预测 subword，两损失等权；(2) Gemma-3-27B 经 LoRA/SFT + GRPO，以原始正字法与 IPA 为条件生成 (Written)/(Spoken) 双文本。IPA 来自 STT 而非仅文本 phonemizer，作为消歧主条件。

## 实验与结果
英语 TN（GoogleTN，TTS 合成评测语音）：Proposed 相对 Duplex 等，SA 88.7、WER 2.73、F1 0.981、DER 4.7（Duplex DER 10.2），数字类相对 Duplex 错误约降 53.9%。韩语牙科领域：由 YouTube 半自动建 100h KDSC，双转录得 KDSC V2；PIC+KDSC V2 在 KDent CER 5.1、KDigit WER 12.2，相对基线错误降约 69.8%/18.1%；原 KDSC 微调反而在领域集严重退化。

## 结论
IPA 引导双转录可缓解口语–书面歧义并支撑领域语料迭代精炼；作者承认英语 TN 评测用 TTS 而非自然语音，计划扩展到自然语料与更多语言/任务。

## 点评
把语料精炼做成「音素条件的双文本生成」，比纯文本 TN 多了声学落地。强在领域脏语料上 V1→V2 对比鲜明；脆弱点在 TN 诊断协议依赖参考 spoken 形式的 TTS，以及 LLM 规模与迭代环成本。

