# 语音识别

- 论文数：169
- 规则：每篇论文至少进入一个技术分类；这里收录该分类下的全部单篇总结。

## 技术趋势与评论

# 语音识别：技术趋势评论

本文基于 Interspeech 2026 语音识别方向约 169 篇论文总结，概括跨论文的技术走向。不以逐篇罗列为主，只讨论方法取向与共同问题。

### 总览：基础模型上的适配、推理修补与条件化

本届 ASR 工作大体围绕 Whisper 及各类语音基础模型展开：少改骨干、多改适配与推理。参数高效微调（LoRA 族、门控卷积适配、Mamba 适配、口音专家适配等）成为领域与低资源迁移的默认路径；与此同时，大量工作刻意避开重训，转向对比解码、表征转向、发射策略、观测融合、热词偏置门控等训练无关修补。多说话人场景则把「条件化」推到前台——用 diarization 掩码调制编码器，或用全局–局部路由的序列化转写，以减轻对冻结口语大模型解码器的破坏。CTC 不再只是训练目标，而频繁出现在草稿、约束图、关键词关键帧与非自回归采样中。

### 鲁棒与高效：幻觉、噪声口音与端侧压缩

鲁棒性议题明显从「加噪再训」转向「内部表征与解码先验」。长音频上的多负样本对比解码（Whisper-CD）用噪声、静音与时移负样本抑制重复环与静音幻觉；稀疏自编码器与激活转向、以及用锚定音频约束输入分布等工作，则把幻觉当作可分离的隐空间方向来处理。尺度分析进一步指出：随模型变大，幻觉机制可从早期信号弥散转向深层吸引子锁定，单纯增大容量并不能等价于更稳。噪声与口音侧，常见做法是干净–噪声多层自蒸馏、增强流与原始流的可懂度引导融合，以及向 Whisper 注入口音适配器或对比正则，而不是全量微调。

效率线同样精细化。量化与剪枝强调「在哪里动刀」：差分感知的超低比特量化、系统化 PTQ（常保留较高精度激活）、亚比特二值分解、音素感知一次性剪枝、敏感度感知剪枝，以及无数据的参数聚类压缩。自回归与语音语言模型则通过半自回归推测解码、自推测解码、自适应 token 采样、层内 KV 池化与面向 vLLM 的批推理管线压缩延迟。流式侧，对已有带时间戳的基础模型用滑动窗、去重与发射策略（如 LocalAgreement 一类）缩小离线–流式差距，成为「不重训也能上线」的务实路线。

### 多语与低资源：先对齐，再混合；评测重于刷表

多语与低资源工作的共识是：直接把多语数据与多任务混在一起往往伤对齐。PART 一类流程先做语内 ASR、再逐步解冻编码器、最后联合 ASR 与语音翻译；对齐感知的持续预训练、课程式从标准语到方言或从翻译到识别，也反复出现。参数高效训练上，双层优化把「跨语对齐」与「语种特化」拆开（如 BELLA），LoRA 间跨语热启动、Transformer 上采成按语种路由的 MoE、以及与词表解耦的语言表示，都服务于可配置、低时延的多语部署。

方言、口语体与脚本差异被单独当作一等公民：无参考的对比偏好优化纠正方言语义漂移，地理坐标条件化适配连续方言空间，非正式语料同时拉动 ASR 与级联翻译。南亚、非洲等区域基准强调：平均 WER 会掩盖人口统计、拼写变体、连音与行业实体风险；复杂度分层、反向课程微调、野生场景与域垂直评测，比单一榜单更能指导部署。数据侧则继续依赖合成域专精语料、嵌入式数据筛选、伪音频提示的文本域适应，以及音视频半监督建库。持续学习与联邦场景下的语种平衡梯度投影、语种感知聚合，说明多语 ASR 已进入「如何共训而不遗忘」阶段；LLM 后纠错在极低资源上并非万能，开放小模型仍常落后于专用声学路线。

### 多说话人：仿真分菜、条件化与评测诊断

多说话人 ASR 与日志共享合成会话数据，但最优配方并不相同。开源仿真器 FastMSS 的系统消融表明：提高重叠往往利 ASR、伤 diarization；多样源域优于单一域匹配；噪声与混响对日志更关键；合成→真实的策略在精心配置下可接近甚至增强纯真实训练。架构上大致两路：一路强化序列化输出（全局–局部动态 MoE 的 GLAD-SOT、说话人切换计数掩码、未知人数下的约束探索联合训练）；另一路用 diarization 条件化编码器（DiCoW、Dixtral 等），冻结大模型解码器以保留指令跟随与问答能力。

流式多说话人对比把级联时间戳映射、掩码并行解码、加权长度 SOT 与说话人条件化（SSA）放在同一骨干上权衡：当前 diarization conditioning 精度领先且单说话人退化较小，而 SOT 路径仍受标签对齐与数据规模制约。解码期修补包括假设聚类中联合文本–说话人距离、级联链路的日志驱动转写纠错，以及「强在线分离 + 干净训练 ASR」的解耦。评测上，语义感知与按重叠区分解的指标表明：重叠仍是主瓶颈；任务型口语模型在两说话人上可竞争，人数与声学难度一升则迅速落后于强模块化流水线。

### 解码：训练无关加速与约束图复兴

解码专场把「搜索」重新写成可组合模块：估计、决策、先验更新与终止被统一形式化，以便同时覆盖束搜索、推测解码与边缘上的非自回归情形。实践热点是训练无关加速——多负样本对比解码、Mask-CTC 上的非自回归最小贝叶斯风险、CTC 草稿加自回归修补的半自回归推测、以及冻结 CTC 草稿的自推测解码。约束 CTC 则把字母骨架钉死、只在标音位上搜索，用轻量图约束完成阿拉伯语标音复原，跨域时往往比沉重的文本–语音融合更稳。生成式非自回归（掩码扩散解码加迭代自校正）与块级半自回归生成，继续在精度–并行度之间填缝；测试时适应侧则修正自回归熵最小化目标，使域移下的自适应更完整。

### 检索与关键词：开放词表、端侧与偏置闭环

检索与关键词检出从封闭词表走向开放词表与用户自定义。大规模开放词表 KWS 压缩基础模型隐状态（层选择、降维、帧池化）；流式侧用交叉注意力角色对调、音素级对齐与非对称对比难负样本稳住时延与区分度。端侧则强调脉冲网络匹配、CTC 引导关键帧融合、通道剪枝个性化与子模型短时记忆卷积。产品约束催生「扩词不遗忘」的模块化网络扩展，以及语音–说话人联合打分以防冒充。与 ASR 主干的接口上，声学检索加融合门控、不确定度门控的音素上下文偏置、语码转换感知热词，以及关键词门控的错误记忆检索，把检索从独立检出器拉回解码与后纠错闭环。纯音频检索则区分音乐与语音域的序列匹配策略，并出现显式成对 token 对齐与 ASR 无关的专名多视图落地。

### 语音翻译：与 ASR 同构的数据与「是否真在听」

本批 ASR 主题文档中的翻译相关工作体量小于识别本体，但方向清晰。级联实时系统暴露出：过激端点会拖垮吞吐与可用时延，短块上不当提示还可能泄漏指令、伤害流式 ASR。低资源翻译与识别共享数据建设——非正式口语语料、台语等多模态半监督字幕语料同时抬升转写与下游翻译。端到端语音到语音方向用共享发音瓶颈与中间 CTC（如 ARTIST）压参数与数据需求，并用可控合成与专用指标（如 CETS）盯住跨语言强调传递。思维链式语音到文本翻译的归因实验提醒：默认 CoT 往往在「读转写」而非「听语音」；混入直接翻译与噪声转写训练，才能提高对语音的依赖与抗错能力。同传人工评测则表明：结构化双头监督比标量 LLM 打分更能贴近分析性量规，评测设计本身成为瓶颈。

### 小结

Interspeech 2026 的 ASR 趋势可以概括为：在强大基础模型之上，用适配器与条件化扩展任务面，用训练无关解码与压缩解决延迟与端侧，用更细的评测与仿真配方暴露重叠、方言、幻觉与「假听真读」等系统性弱点。下一阶段的竞争点，更可能落在条件信号质量、推理策略可组合性，以及域真实评测，而不是单纯堆叠更大的通识 ASR 骨干。

## 论文技术总结

# Mind the Gap: Impact of Synthetic Conversational Data on Multi-Talker ASR and Speaker Diarization

- 论文编号：443
- 报告人：Alexander Polok
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/polok26_interspeech.pdf

## 问题
大规模真实会话数据稀缺，MT-ASR 与说话人日志（SD）高度依赖合成数据，但轮次动态、源域、声学增强与真实/合成混合策略对各任务的影响尚不清楚，且缺乏可复现的大规模会话仿真工具。

## 方法
发布开源仿真器 FastMSS，可配置 turn hold / turn switch / interruption / backchannel 等转移、混响与噪声，并与 Lhotse 集成。在 DiCoW（Whisper + 帧级 diarization 条件）与 Sortformer（EEND + Sort Loss）上系统消融：轮次统计（flat / NSF-1 / CALLHOME / OV boost）、源域（LibriSpeech、VoxPopuli、otoSpeech、AMI/NSF-1 close-talk 及 Combined）、noise/rvb 增强，以及 synthetic-only、real-only、joint、synthetic→real 训练策略。MT-ASR 用 tcpWER（5 s collar，ground-truth diarization）；SD 用 DER（0 s collar）。

## 实验与结果
轮次：OV boost 使 DiCoW 在 NSF-1 上达 22.1 tcpWER（优于 flat 的 24.8），但使 Sortformer macro DER 从 26.1 恶化到 27.6。源域：Combined 合成已优于 real-only 的 macro tcpWER（10.0 vs 10.9）；Real + Combined 进一步到 8.8。增强：对 DiCoW 增益有限；对 Sortformer，noise+rvb 将 macro DER 从 26.1 降至 22.2。合成+真实：DiCoW Synthetic→real macro 8.7；Sortformer Synthetic→real macro DER 15.5，优于 joint 与 real-only。

## 结论
最优仿真配方强依赖任务：提高重叠利 ASR、伤 diarization；多样源域优于单一域匹配；噪声+混响对 diarization 关键；精心配置的合成数据可接近甚至增强真实数据训练。

## 点评
把“同一套仿真能否服务 ASR 与日志”拆开验证，结论可操作：重叠与声学增强应按任务分菜。拼接仿真缺语义连贯性，作者靠冻结 ASR 解码器缓解，对依赖语言模型的链路可能仍有偏。全文末段结论略有截断，但核心四点结论在前文已完整给出。


# Grounding Spoken LLMs in Multi-Speaker Audio via Diarization Conditioning

- 论文编号：445
- 报告人：Alexander Polok
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/polok26b_interspeech.pdf

## 问题
Spoken LLM 用 SOT 扩展到多说话人时需改词表并微调解码器，易灾难性遗忘推理/摘要/问答能力；多说话人远场 grounding 与任务泛化仍弱。

## 方法
提出 diarization-conditioned SLM：用 DiCoW 的 STNO 掩码经 FDDT 在 Whisper 编码器各层调制表示，抽取目标说话人声学特征；经 modality adapter 送入冻结的 Ministral 解码器（实例化为 Dixtral = DiCoW 编码器 + Voxtral Mini 3B）。仅训练编码器与 FDDT；全局模式可将 \(p_T=1\)。Diarization 前端用 DiariZen。另构建 NSF-QA（内容/情感/性别问答与摘要），用 Gemini 评判准确率与 ROUGE-L。

## 实验与结果
转写（cpWER）：Dixtral macro 15.4，优于 Gemini 3.0 Flash（44.4）、VibeVoice（35.2）、Voxtral MTv2（31.4），接近专用 DiCoW v3.3（14.0）。消融：FDDT swap / 无全量 encoder swap 更稳；LoRA 解码器 ASR 最好（NSF-1 21.3）但伤指令跟随；QA+Summ 微调损害 Mixer6 转写。NSF-QA：zero-shot 远场内容 QA 54.6≈Gemini 55.1；微调后内容 73.0、情感 47.6、性别 95.5、ROUGE-L 41.4，超过近讲 Voxtral/Gemini。

## 结论
在编码器侧做 diarization 条件、冻结解码器，可在保留 SLM 通用能力的同时显著提升说话人归因转写；有任务数据时远场 Dixtral 可超过近讲基线，包括级联 ASR+LLM 难以回答的副语言问题。

## 点评
把多说话人问题压成“单说话人式”输入分布，避开 SOT 对 LLM 的结构性破坏，与独立按说话人解码的复杂度论证一致。强依赖外部 diarization 质量；QA 裁判与参考均用 Gemini，作者自认可能偏保守。ASR 与下游任务联合训练仍留作未来工作。


# GLAD: Global-Local Aware Dynamic Mixture-of-Experts for Multi-Talker ASR

- 论文编号：1022
- 报告人：Yujie Guo
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/guo26_interspeech.pdf

## 问题
SOT 式 MTASR 在深层中说话人相关声学线索易被稀释，标准 MoE 仅靠局部层输入路由，难以按说话人分配专家；SIMO/外部 diarization 条件方案又受限或开销大。

## 方法
GLAD-SOT：在 Conformer 编码器所有线性层换成 Mixture of Low-rank Experts（MoLE，N=3，r=8）。全局路由：卷积前端浅层特征经线性编码器得 \(X_{global}\)，KeepTopK+softmax 得 \(P_{global}\)；局部路由由层输入得 \(P_{local}\)；动态融合 \(\beta=\mathrm{softmax}(X_{in}W_{fusion})\) 按帧加权二者得到专家权重。训练损失为 ASR + Switch Transformer 式负载均衡（\(\gamma=0.01\)）。输出为带 `<sc>` 的序列化转写。

## 实验与结果
LibriSpeechMix：GLAD-SOT（35.31M）2mix OA-WER 7.4、3mix OA-WER 21.5，优于 SOT、CSE-SOT、SOT+SACTC；高重叠与 3mix 零样本仍领先。消融：去掉全局路由或改为静态求和均变差；FFN 与 Attention 同时替换最好。CH109（CH11-mix 微调 5 epoch）：平均 40.7，优于各基线。可视化：全局融合权重 \(\beta_g\) 随重叠升高，浅层与最深层更高。

## 结论
全局–局部动态融合 MoE 可提升 SOT-MTASR，尤其在高重叠与多说话人泛化场景；作者称这是首次将全局–局部融合 MoE 用于 MTASR。

## 点评
用浅层说话人线索补深网路由，直接针对“重叠越重越需要身份锚点”的瓶颈，与可视化一致。专家为低秩、规模偏学术小模型；主训仍是模拟混合，真实通话依赖短微调，跨域鲁棒性边界仍待更大规模验证。


# Speaker-Aware Hypothesis Clustering and Merging for Target-Speaker-free and Target-Speaker Multi-Talker ASR

- 论文编号：1604
- 报告人：Yosuke Kashiwagi
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kashiwagi26_interspeech.pdf

## 问题
HCM 只在转写空间聚类假设，多说话人说相同/极相似内容时编辑距离失效；目标说话人设定下离散 speaker token（k-means）又难忠实利用 enrollment。

## 方法
保持 HCM 解码与离散 token 训练不变；对每条假设用对齐片段经 TitaNet 提 embedding，AHC 距离改为 \(D_{joint}=\bar{D}_{text}+\alpha D_{spk}\)（评测 L2 / cosine / 逆 PLDA）。目标说话人场景：enrollment embedding 与各簇质心比距离选簇，替代离散 token 提示。解码 top-N=20，簇内 ROVER 合并。

## 实验与结果
LibriMix 上与 text-only HCM 接近；VCTK identical-content：2spk WER 68.3→36.6（L2，相对降 46.4%），3spk 88.3→57.2。\(\alpha\approx0.005\) 时标准条件稳定、同文条件收益最大，过大伤识别。目标说话人：clean 2spk 18.7→14.4（约 23% 相对降），noisy 2spk 28.5→25.2；3spk noisy 双方均 >120%，差异有限。

## 结论
在假设空间联合转写–说话人距离，统一改进无 enrollment 与有 enrollment 的多说话人 ASR；同文条件下收益最大，标准 LibriMix 保持竞争力。

## 点评
改动集中在聚类一步，工程侵入小，却精准打中 HCM 的文本坍缩点。\(\alpha\) 敏感、三说话人噪声下任务本身过难；多假设解码与聚类的算力开销作者亦承认仍是部署瓶颈。


# Pushing the Boundaries of Streaming Multi-Speaker ASR: A Systematic Study of Architectural Trade-offs

- 论文编号：2005
- 报告人：Taejin Park
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/park26e_interspeech.pdf

## 问题
流式多说话人 ASR 需同时权衡精度、时延、显存与是否可微调；社区缺少在同一对开源流式 ASR/diarization 骨干上对架构范式的受控对比，且 SOT 短训长推时存在转写–RTTM 标签置换对齐难题。

## 方法
基于 Nemotron Speech streaming ASR 与 streaming Sortformer v2.1，归纳四类架构：Cascaded（词时间戳映射 diarization）、Masked Input（按说话人掩码特征并行解码）、WL-SOT（单实例 + Arrival-Order Speaker Cache / speaker kernel，提出 PI-DTW + 说话频率代价对齐 SOT 与 RTTM）、SSA Diarization Conditioning（多实例条件解码）。在 CH109、Mixer6、AMI IHM/SDM 上报告 cpWER（含 oracle diarization），并在 OpenASR 单说话人集上测退化。

## 实验与结果
多说话人平均 cpWER（oracle diar / 系统 diar）：Cascaded 45.25 / 42.27，Masked 30.06 / 34.77，WL-SOT 28.66 / 33.46，SSA 16.18 / 23.36，SSA 最优。OpenASR：SSA 平均 WER 7.44，接近基座 7.16；WL-SOT 严重退化至 16.95。流式 diarizer DER 在各集约 5–20%。

## 结论
形式化流式多说话人 ASR 的架构权衡；当前 diarization conditioning（SSA）精度领先且单说话人退化小；PI-DTW 为扩展端到端 WL-SOT 扫清标签对齐障碍，但 SOT 路径仍需更大数据与原生说话人标记。

## 点评
同一骨干上的四象限对比，对“无微调 API / 数据稀缺 / 要精度”的选型很实用。WL-SOT 单说话人崩坏说明序列化训练仍伤通用识别；结论偏工程地图而非新 SOTA 叙事，与正文定位一致。


# Who Spoke What When? Evaluating Spoken Language Models for Conversational ASR with Semantic and Overlap-Aware Metrics

- 论文编号：2912
- 报告人：Naohiro Tawara
- 程序：Monday 28 September 2026 / Multi-Talker ASR & Speaker Diarization
- 技术分类键：asr-multitalker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/tawara26_interspeech.pdf

## 问题
LLM 系 CASR 在单说话人基准上表现好，但在重叠、远场、说话人数变化下相对模块化流水线的稳健性不清；cpWER/tcpWER 对语义影响与文本规范化过于敏感，且难分离重叠区错误。

## 方法
系统对比：单通道 DiCoW、多通道 NTT CHiME-8 DASR (S)、任务型 LLM（VibeVoice、Voxtral MTv2）、通用多模态 Gemini 3.0 Flash；数据为 MX6、NSF1、DiPCo。提出 tcpSemER（在 tcpWER 对齐上用 MiniLM 句向量相似度替代 Levenshtein），并将 tcpWER/cpWER 按重叠/非重叠区分解（贡献与区域归一化）。多通道 LLM/DiCoW 用逐通道识别 + MOVER 融合。

## 实验与结果
两说话人 MX6：VibeVoice/DiCoW 可竞争；复杂场景模块化明显更强（如 NSF1 tcpWER：NTT 15.0 vs DiCoW 24.6 vs VibeVoice 36.6；DiPCo 上 Voxtral 失败、Gemini 很差）。SemER 有时显示 LLM 更多是表层差异。重叠区贡献占 NSF1 总错误约 90%；VibeVoice 重叠删除多。MOVER 缩小差距（MX6 上甚至优于挑战最优 tcpWER 10.9）。说话人数↑时错误↑，NTT 计数最准。

## 结论
重叠处理仍是 CASR 主瓶颈；任务型 LLM 在两说话人上可竞争且 tcpSemER 相对友好，但随说话人数与声学难度急剧退化；通用 LLM 受说话人/时间归因拖累；原生多通道 LLM 值得探索。

## 点评
把“谁说了什么何时”拆成语义与重叠两个评价轴，比单纯报 WER 更能解释 LLM 流畅输出的假象。tcpSemER 仍继承 tcpWER 对齐，且与人类语义判断尚未验证；评测更偏诊断框架而非新识别模型。


# Constrained CTC decoding for Efficient Diacritic Restoration

- 论文编号：3220
- 报告人：Rufael Marew
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/marew26_interspeech.pdf

## 问题
阿拉伯语文本常缺标音符号，纯文本复原对同形异音仍模糊；已有语音+文本多模态复原有效但计算重、跨域弱。需在保持字母骨架不变的前提下，用语音高效恢复 diacritics。

## 方法
在给定语音与无标音参考 \(u\) 时，用 CTC ASR（Wav2vec2-XLSR 微调）预测含字母与复合标音标签的序列；推理时由 \(u\) 构图字符级 diacritization lattice（字母固定、其后通配符位只允许 diacritic/blank），与 CTC 解码图组合或限制 beam，实现部分强制对齐式约束解码。无标音用 CTC blank 表示。对比 Text-only 与 Text+ASR 基线（后者可额外用 Tashkeela 文本预训练）。

## 实验与结果
数据：ClArTTS（CA，12h 训 / 0.3h 测）、ArVoice 1+3（MSA，6h / 0.9h）。匹配 ClArTTS：Ours WER/DER 11.21 / 3.53，接近 Text+ASR。跨域与联合训练：Ours 明显更稳（如 ClArTTS 训→ArVoice：DER 12.04 vs Text+ASR 19.21；联合训练 ClArTTS DER 3.80、ArVoice 8.69）。bootstrap 95% CI 显示相对 Text+ASR 的 DER 改善显著。

## 结论
约束 CTC 解码在 CA/MSA 上优于或持平多模态基线，且更精简高效，可直接作带标音 ASR 或对无标音标注语音做复原，利于阿拉伯语数据策展。

## 点评
把“字母骨架硬约束”下沉到解码图，避开额外文本编码器与融合训练，效率与跨域表现合理。依赖已有无标音参考；未覆盖方言且基线独享大规模文本预训，公平性上作者已说明。


# Whisper-CD: Accurate Long-Form Speech Recognition using Multi-Negative Contrastive Decoding

- 论文编号：3058
- 报告人：Hoseong Ahn
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ahn26b_interspeech.pdf

## 问题
Whisper 等长音频编解码 ASR 易产生静音幻觉、跨段重复环与内容漏识；启用上一段转写作上下文时错误会放大，beam search 也难纠正高置信幻觉。

## 方法
提出训练无关的 Whisper-CD：每步用干净音频 logits 与三种声学扰动负样本对比——高斯噪声（SNR 10 dB）、全零 silence、波形左移 \(\Delta_s=7\) s；用 log-sum-exp（\(\tau=1\)）聚合负 logits，\(\ell^{CD}=(1+\alpha\tau)\ell^{pos}-\alpha\tau\log(\frac{1}{K}\sum\exp(\ell^{neg}/\tau))\)。编码器与解码器路径批并行；保持语言识别与时间戳等能力。默认开 previous-context、greedy。

## 实验与结果
五集长音频：Large-v3-Turbo 上 CORAAL 38.75→14.43（最多约 24.3 pp 降幅），Earnings22 33.25→16.16 等全面下降；Large-v3 基线因重复环 WER 可 >100%，CD 后大幅收敛但仍高于 Turbo。吞吐高于 beam=5（如 Turbo CORAAL 147 vs 99 tokens/s）。消融：单扰动不如多负样本；\(\alpha\) 过大伤干净集（TED-LIUM）。

## 结论
多负样本对比解码可在无重训条件下抑制长音频幻觉与重复，相对 greedy 开销有限、显著快于 beam search，可作已部署 Whisper 的即插替换。

## 点评
把对比解码从视觉/文本迁到 ASR，用声学退化暴露模型先验，直接打在上下文传递放大错误的链路。\(\alpha\) 与模型尺度敏感，Large-v3 深重复环仍难完全拉回；decoder-only ASR 如何注入扰动路径仍开放。


# Accelerating End-to-End ASR via Semi-Autoregressive Speculative Decoding

- 论文编号：1953
- 报告人：Long Wu
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/wu26g_interspeech.pdf

## 问题
端到端 ASR 中，AED 的自回归解码精度高但难以并行；NAR 虽快但语义建模与对齐常受损。现有 attention rescoring 等混合解码依赖 CTC prefix beam search 或复杂 CTC prefix score，成为吞吐瓶颈，且与 streaming chunk 解码不够契合。

## 方法
提出 Semi-Autoregressive Speculative Decoding（SASD），基于 joint CTC-attention 框架、无需重训：
1. 用 CTC greedy search 得到初假设（draft）；
2. 以 CTC 峰值概率为置信度，低于阈值 \(P_{\mathrm{thres}}\)（实验取 0.99）的位置记为低置信 token；
3. 高置信位置直接采用 CTC 结果；低置信位置用 attention decoder 做 speculative beam search，将 attention 分数与 CTC 分数插值后选 top-\(k\)；
4. 注意 decoder 只在原索引上替换 token，输出长度与 CTC 假设严格一致。
该设计避免精确 CTC prefix scoring，并兼容 chunk-based streaming。

## 实验与结果
数据：AISHELL-1、WenetSpeech（TestNet / TestMeeting）、内部约 33 小时工业测试集。在 WENET 五个预训练中文模型上评测。
- AISHELL-1（u2++ conformer）：SASD CER 4.73%（full），与 attention rescoring 4.77% 相当，优于 CTC greedy 5.18%；GPU RTF 0.0188，约为 attention rescoring（0.0535）的约 2.8 倍加速；batch=8 时 RTF 0.0098。
- WenetSpeech：与 attention rescoring 接近（如 TestNet full：9.40 vs 9.26），chunk 减小时更稳。
- 工业模型：CER 4.58 vs E2E 4.57，约 3.5× 加速。
摘要称相对 SOTA attention-rescoring 约 2.8×–3.5× 加速且 CER 可比。

## 结论
SASD 在解码阶段对“易”token 走 NAR（CTC）、对“难”token 走 AR（attention），省去 CTC prefix scoring / CTC beam search，在公开与工业数据上取得接近 rescoring 的 CER 与更高推理速度。

## 点评
做法本质是 token 级 draft-and-verify：用 CTC 峰度当置信门控，把昂贵的 attention 算力集中在少数低置信位置，因而延迟可接近 CTC greedy。强在兼容已有 AED、无需额外 draft 模型、对 streaming chunk 友好；脆弱点在于依赖 CTC 置信阈值与假设“多数 token 已足够自信”——若低置信比例升高（难声学条件），AR 修正成本会上升，加速比缩小。


# Self-Speculative Decoding for LLM-based ASR with CTC Encoder Drafts

- 论文编号：2680
- 报告人：Avihu Dekel
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/saon26_interspeech.pdf

## 问题
Speech-aware LLM（SLM）ASR 精度领先，但自回归逐 token 前向限制吞吐。常规 speculative decoding 常需额外 draft 模型；联合 CTC/attention 虽可加速，但如何在不重训的前提下复用 SLM 自带 CTC 编码器做 draft，并兼顾准确率与 RTFx，仍不清晰。

## 方法
提出 self-speculative decoding（SSD），三步、无需额外 draft 模型：
1. **CTC decode + verify**：CTC greedy 假设；若所有帧级 CTC 输出熵低于 \(\tau_{\mathrm{CTC}}\)，直接接受；
2. **LLM verify**：否则用单次 LLM 前向，按松弛准则检查各 token 似然是否均大于 \(\tau_{\mathrm{SLM}}\)；通过则接受 CTC 假设；
3. **AR fallback**：失败则从最长已验证 CTC 前缀继续自回归解码。
架构为 Conformer CTC encoder + Q-Former adapter + LLM；要求 CTC encoder 在 projector/LoRA 微调时冻结。松弛接受（“plausible”而非精确匹配）用于提高接受率。

## 实验与结果
主模型 granite-speech-4.0-1b（约 1B LLM + 440M CTC encoder），在 HuggingFace Open ASR 及 MLS、CommonVoice 等多语料评测（1×H100，batched）。
- High accuracy（\(\tau_{\mathrm{CTC}}=0.7,\tau_{\mathrm{SLM}}=0.2\)）：Open ASR 平均 WER 5.58%，优于 full AR 的 5.75%，RTFx 相当（548 vs 564）；作者称创纪录 5.58% WER。
- High RTFx（\(\tau_{\mathrm{CTC}}=3.0,\tau_{\mathrm{SLM}}=0.1\)）：Open ASR 平均 WER 6.56%、RTFx 2491，相对 AR 约 4.4× 加速，相对 WER 增约 12%。
- 消融显示双阶段验证在多数 WER–RTFx 区间 Pareto 更优；LLM 验证相对纯 AR 常进一步降 WER，作者归因于 CTC 与 SLM 错误互补。

## 结论
复用冻结 CTC 编码器作 draft、LLM 做验证与回退，可在不重训、不引入独立 draft 模型的情况下同时提升准确率与吞吐。局限：需 CTC 训练的 SLM；仅适用于 ASR；验证失败时整句从失败点 AR，低接受率语料收益有限。

## 点评
核心是“声学接地的 CTC draft + 语言模型验证”：高置信 CTC 可跳过 LLM，而 LLM 接受 CTC 又能纠偏 AR 的语言先验偏差。强在自投机、可调 \(\tau\) 覆盖准确–速度谱；脆弱在依赖 CTC 头质量与 utterance 级接受失败时的整段 AR 回退，对长句与低接受率场景不友好。


# Non-Autoregressive Minimum Bayes' Risk Decoding for Fast Speech Recognition

- 论文编号：2971
- 报告人：Hiroyuki Deguchi
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/deguchi26_interspeech.pdf

## 问题
NAR ASR（如 Mask-CTC）并行解码快，但因 token 独立性与多模态路径不确定性，相对 AR beam search 仍有 WER 差距。标准 MAP 选最高概率路径不一定质量最优；MBR 用期望效用选假设可更稳健，但在 AR 设定下采样与效用计算昂贵。

## 方法
提出 NAR-MBR：在 Mask-CTC 上做无偏采样 + 期望效用（负 WER）最大化，无需额外训练。
1. **采样**：按帧独立从 CTC 分类分布采样多条对齐路径 \(|Z|\)；再按置信度 Bernoulli 采样 mask，用 CMLM 从分类分布填 mask（可用 \(N_{\mathrm{iter}}\) 迭代；\(N_{\mathrm{iter}}=0\) 仅用 CTC）；假设集与伪参考共用同一采样集。
2. **EU 最大化**：选使相对伪参考平均 WER 最小的假设；用去最长公共前后缀、去重缓存、多核并行与 Rust 实现的编辑距离加速。
相对原 Mask-CTC 的确定性 mask + greedy，改为概率采样以服务 Monte Carlo MBR。

## 实验与结果
数据：LibriSpeech、Switchboard、AMI、Web（约 346h 训练）。AR 用 Conformer + CTC 联合解码；NAR/NAR-MBR 用 Mask-CTC（ESPNet）。
- WER：\(N_{\mathrm{iter}}\in\{1,10\}\)、\(|Z|\in\{64,256\}\) 时 NAR-MBR 相对 NAR 在多数集合显著更好（如 LS Clean \(N_{\mathrm{iter}}=1,|Z|=256\)：3.1 vs NAR 3.4；Web 7.3 接近 AR Beam 7.3）。峰值多在 \(N_{\mathrm{iter}}=1\)，增大迭代几乎不再降 WER。
- 速度（相对 AR Beam）：Web 上 \(|Z|=64,N_{\mathrm{iter}}=1\) 约 43.1×，\(|Z|=256\) 约 20.7×；仍快于 AR Greedy，但 \(N_{\mathrm{iter}}=1\) 时 GPU 显存升高（Web 上 \(|Z|=256\) 约 ×5.0）。
- \(|Z|\) 增大 WER 改善并在 ≥64 趋于饱和。

## 结论
利用 NAR 独立性可一次前向廉价采多样本，再用 MBR 缓解多模态不确定性，从而在无重训下优于原 NAR，并相对 AR beam 大幅加速；未来拟扩展到更多模型与任务。显存开销与采样规模是明确边界。

## 点评
把 MBR 的“用样本估期望质量”接到 NAR 的“一次前向可多样本”上，用决策准则补独立性假设的短板，比堆迭代 mask  refinement 更对症。强在训练零改动、\(N_{\mathrm{iter}}=1\) 即可；脆弱在二次效用与多样本带来的 CPU/显存成本，以及效用仍绑定 WER——对其他评价指标需重定义 \(u(\cdot)\)。


# A Generalized Formalism of Auto-Regressive Decoding for Speech Processing

- 论文编号：2768
- 报告人：Julia Gachot
- 程序：Monday 28 September 2026 / Search Methods and Inference Algorithms
- 技术分类键：asr-decoding
- 全文：https://www.isca-archive.org/interspeech_2026/gachot26_interspeech.pdf

## 问题
语音处理中序列生成高度依赖自回归搜索，但“AR / next-token / MAP beam”等概念定义分散，推测解码、NAR、随机采样等常被用不同名称复述相近机制，导致难以系统比较、消融与报告。现有分类常按任务或“确定性 vs 随机”切分，跨任务迁移结论困难。

## 方法
将生成表述为 \((M, g_{\mathrm{AR}})\)，在 SIPC（随机整数规划）视角下给出 AR 纳入准则与模块化形式：
- **模型假设**：网络估计有限字母表上的条件概率，并用解码状态/先验更新；
- **解码假设**：迭代局部搜索，且至少一次用目标函数（如 MAP）更新有限候选集。
每次迭代 \(f^t_{(M,g_{\mathrm{AR}})}(Y_t,Z_t)\) 由四步组成：**Estimation**（条件 PMF）、**Decision**（目标函数选/扩候选）、**Update of prior**（维护 \(Z_t\)）、**Termination test**。报告解码策略即报告初始条件与上述设计选择。用该框架形式化 beam search 与 temperature sampling，并讨论 speculative / “NAR” 边界案例的纳入与排除。

## 实验与结果
本文以形式化与讨论为主，未报告新的 ASR/MT 数值实验。在 2018–2025 的十篇相关工作上做归类：按解码假设排除 1 篇非 SIPC；模型假设下 speculative 与部分所谓非 AR 方法可纳入。进一步说明可用“用基线步骤替换某一步”做结构消融，以隔离 estimation / decision / prior / termination 的贡献。

## 结论
作者给出统一的 AR 搜索形式与报告清单，用以跨任务比较与设计聚焦解码的消融；主张摆脱“仅是似然最大化器”的笼统描述，转向递推关系与模块设计视角。

## 点评
贡献是元方法：把解码拆成可复用的结构组件，便于把 speculative、多样性惩罚等放到同一坐标系里比较。强在澄清报告要素与消融接口；作为纯理论/分类工作，正文没有对照实验数字，实际收益取决于社区是否采用该报告约定。技术分类虽挂在 asr-decoding，内容覆盖更广的序列生成搜索。


# MDM-ASR: Bridging Accuracy and Efficiency in ASR with Diffusion-Based Non-Autoregressive Decoding

- 论文编号：488
- 报告人：Sabato Marco Siniscalchi
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yen26_interspeech.pdf

## 问题
Seq2seq Transformer ASR 中 AR 精度高但逐 token 慢；NAR（含近期扩散/流匹配 ASR）可并行但相对强 AR 仍有明显差距。训练只见 oracle mask、推理却对自生成错误去噪，加剧训练–推理失配。

## 方法
MDM-ASR：预训练语音编码器 + Transformer **离散掩码扩散（MDM）解码器**；非因果自注意力，每步并行预测掩码位置，交叉注意条件于声学。
- **ISCT（Iterative Self-Correction Training）**：先对真值 mask 重建，再对模型自输出再 mask 并二次监督，暴露中间错误；
- **Position-Biased Entropy-Bounded Confidence sampler**：结合熵界与位置偏置的推理采样，权衡步数与质量。
架构其余与常规 encoder–decoder 一致，仅解码策略改为扩散迭代。

## 实验与结果
摘要称在多基准上相对既有 NAR 持续提升，并与强 AR 基线可比，同时保留并行解码效率；文中还计划消融缩放、ISCT 与采样器。
（PDF 抽取在采样器小节截断，具体 WER 表未进入可读全文。）

## 结论
用音频条件 MDM 替换左到右 AR，配合 ISCT 与置信采样，可在保持 NAR 吞吐的同时显著缩小与 AR 的精度鸿沟。

## 点评
把文本 MDM 的双向精炼迁到 ASR，并用自纠训练对症“自生成噪声”，路线清晰。强在与既有流匹配中间分布手搓不同、更数据驱动；**实验数字因抽取截断不可用**，加速比与绝对 WER 需回 PDF。


# Whisper Hallucination Detection and Mitigation via Hidden Representation Steering and Sparse AutoEncoders

- 论文编号：1989
- 报告人：Georgii Aparin
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/aparin26_interspeech.pdf

## 问题
Whisper 常对非语音输入生成流畅但与声学无关的转写（幻觉）。既有缓解依赖前/后处理或微调特定神经元；是否可仅靠编码器内部表示检测并在推理时纠正，且少伤正常语音 WER，仍待验证。

## 方法
提取 Whisper 音频编码器激活，在两空间分析幻觉可分性：原始激活与 **AudioSAE** 稀疏潜变量（扩展×8，Top-k=50）。线性分类器显示判别力集中于稀疏特征子集、并随层加深增强。提出免微调干预：
1. **激活空间 steering**：沿分类方向加减扰动；
2. **SAE latent steering**：对 top-k 幻觉相关潜维做加性/乘性缩放，再经 SAE 解码注入残差流。
在 Whisper small / large-v3 上评测；非语音训测严格划分（MUSAN、WHAM!、FSD50k、UrbanSound8K 等）；语音侧用 LibriSpeech、FLEURS、AISHELL-1 监控 WER/CER。

## 实验与结果
- SAE steering 将完整非语音测试集幻觉率：small **72.63%→14.11%**；large-v3 **86.88%→27.33%**；
- 语音数据上 WER 仅小幅退化，接近微调类方法效果。
（抽取在数据集与 HR 表处截断，分数据集明细与 WER 表未全读到。）

## 结论
幻觉在编码器表示中线性可分；SAE 空间 steering 可不改模型参数大幅降非语音幻觉，并在多语言语音上保持可用识别质量。

## 点评
把可解释性工具（SAE + steering）接到 ASR 幻觉，避免重训整模，工程友好。强在双规模模型与非语音–语音分离评测；脆弱在依赖幻觉标签定义与 steering 强度 \(\alpha\)——过强可能伤真实语音。


# Which Data Matter? Embedding-Based Data Selection for Speech Recognition

- 论文编号：3073
- 报告人：Zakaria Aldeneh
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/aldeneh26_interspeech.pdf

## 问题
大规模伪标注野外数据利于通才 ASR，但专科模型容量有限、无法消化全部异构数据。如何从约 **100k 小时** 源数据中选出贴合目标域的子集，仍缺系统答案。

## 方法
用互补嵌入刻画样本：说话人（MFA-Conformer）、语音/音素（WavLM Base+ 均值池化）、语义（SBERT）；再做 **batched greedy MMR**（相关–多样权衡 \(\lambda\)，相关预过滤、目标端 k-means 压缩）。在 Granary 英源上按目标域（LibriSpeech / CommonVoice / TED-LIUM）验证集选子集；训 CTC Conformer-Small（9M）与 Large（107M）。

## 实验与结果
- 全量 Granary 跨域优于仅在域内训练的专科数据（如 Conformer-Large：LS-clean 6.7 vs 仅 LS 的 3.2 但 CV/TED 更差；全量 Granary CV 25.4、TED 6.5）。
- 随机 5% 已接近全量；摘要称策略性选中的 **5% 子集相对全量最高约 36.8% 相对 WER 下降**。
（抽取在 Table 2 中途截断，MMR 主表数字不完全。）

## 结论
对专科 ASR，嵌入空间上兼顾相关与多样的数据选择可显著优于盲目用全量或随机子集；说话人/音素/语义轴需按目标域权衡。

## 点评
把信息检索里的 MMR 接到 ASR 数据策展，问题贴近工业“海量伪标→专科模型”。强在三轴嵌入与可扩展批选；**MMR 相对全量的完整对照表因截断不全**，36.8% 相对降幅以摘要为准。


# Transcription Policy as a Latent Variable: Activating Controllable Verbatim ASR with Word-Level Timing

- 论文编号：2792
- 报告人：Laurin Wagner
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wagner26_interspeech.pdf

## 问题
现代 ASR 训练数据混杂 verbatim（含填充停顿、重复等）与 intended（流利化）标注，把转写风格当成未控隐变量，导致解码不稳、评测混淆（风格错配可占报告 WER 的约 60%）、词级时间戳不可靠。模型其实已编码两种风格，缺的是可控激活。

## 方法
1. **Coverage-aware decoder task tokens**：在并行 verbatim/intended 对上训练，用任务 token 显式切换策略；
2. **Supervised cross-attention finetuning**：选与 TIMIT 对齐相关最好的 \(k=10\) 头，对平均注意力与词区间二值目标做余弦距离；推理时能量 pause 模型 + 温度锐化 + Viterbi 得词时间戳；
3. 新任务 **verbatimize**：从 intended/异构文本生成规范 verbatim，用于语料富集。

## 实验与结果
- 仅英语训练即可零样本把德语不流畅 F1 **10%→79%**；
- 全量英-only 微调在 verbatim 精度、不流畅检测与 intended 质量上英德均超基线；
- 监督交叉注意使不流畅语音上的词时间戳优于强制对齐基线。
（抽取在方法中后部截断，完整数值表未全见。）

## 结论
把转写策略显式化为可控变量，可稳定激活 verbatim/intended，并改善词级 timing；verbatimize 支持可扩展语料建设。

## 点评
问题诊断（风格作隐变量）对临床/自发语音 ASR 很关键；任务 token + 对齐头监督是轻量可控方案。强在跨语零样本不流畅检测；脆弱在依赖并行风格对与 TIMIT 头选择，泛化到更多语言/病理语音仍待验证。


# Towards Efficient Simultaneous Inverse Text Normalization with Pretrained Text-to-Text Language Model and Read-Tag-Write Policy

- 论文编号：1060
- 报告人：Kiet Anh Hoang
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hoang26_interspeech.pdf

## 问题
流式 ASR 需要把口语形式即时转为书面 ITN（标点、大小写、半符号实体等）。现有流式 ITN 多为神经标注 + 手工 FST，跨域跨语难扩展；端到端 seq2seq 精度好但全局注意力不可流式。

## 方法
基于预训练文本-to-文本模型做流式端到端 ITN：
- **流式编码器**（如块注意力）+ 自回归解码器；
- **Read–Tag–Write（RTW）**：编码器边读边对 token 做 IOB 标注；标签为 O（原样）则立即写出以降延迟；遇到需归一化跨度完成后再调解码器 WRITE；
- **Prefix-based Training Augmentation**：随机截断源、目标侧加局部 `<EOS>`，让解码器在无全局 EOS 时也能结束局部跨度；
- KV cache 与推理优化；数据来自越南语新闻语料自动生成约 5M 句对（标点/大小写/半符号/语音学 OOV 等）。

## 实验与结果
摘要：越南语数据上精度可比非流式端到端基线，优于流式混合方法，并满足实时延迟要求。
（抽取主要在方法与数据构造，完整延迟/准确率表未进入可读尾部。）

## 结论
RTW 利用 ITN 多为局部、大量 token 无需改写的结构，使预训练 T2T 模型可流式化，摆脱 FST 规则依赖。

## 点评
把 SiMT 的 read/write 思想改成 ITN 友好的 Read–Tag–Write，抓住“多数 token 直通”降低延迟。强在与预训练 LM 知识结合；**定量延迟与类别 F1 因抽取不全**需回 PDF；手工 regex 造数对真实 ASR 噪声的鲁棒性仍是潜在风险。


# Rethinking Entropy Minimization in Test-Time Adaptation for Autoregressive Models

- 论文编号：944
- 报告人：Chee-En Yu
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/huang26c_interspeech.pdf

## 问题
分类任务上熵最小化（EM）是成熟的测试时适应（TTA）手段，但用于自回归生成时，既有做法分裂为伪标签 teacher-forcing 与策略梯度 RL 启发式，缺统一、数学正确的 EM 梯度。

## 方法
推导自回归模型上精确 EM 目标，自然分解为：
- **token 级策略梯度项**；
- **token 级熵项**。
据此将先前方法解释为该统一目标的部分实现。在 Whisper ASR 上实施 episodic TTA（单样本适应后复位），比较 Greedy-EM、序列级与 token 级变体及 beam 扩展（如 EM-tok-b）。

## 实验与结果
- 加性噪声：源模型平均 WER 22.53%；Greedy-EM 21.91%；EM-seq 21.34%；EM-tok 20.77%；**EM-tok-b 平均 19.15%**，在十种噪声上最低。
- 口音迁移等亦有表（摘要称覆盖噪声、口音、多语等 **>20 域** 持续改进；自称首次对 Whisper 做 TTA）。

## 结论
正确 EM 为自回归 TTA 提供统一理论；完整 token 级目标（可加 beam）优于不完整启发式，提升 Whisper 在分布偏移下的稳健性。

## 点评
贡献首先是理论澄清：把“伪标签熵”与“RL 熵奖励”收束到同一分解。强在 Whisper 多域实证；脆弱在 episodic 单样本适应的算力与稳定性，以及伪标签质量差时策略梯度方差——噪声表显示完整目标更有效，但极端失配时仍可能放大错误。


# Massive Open-Vocabulary Keyword Spotting

- 论文编号：1444
- 报告人：Leonor Barreiros
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/barreiros26_interspeech.pdf

## 问题
开放词表关键词检出 + 上下文偏置可改善稀有术语 ASR，但声学嵌入过高维，词表上千时内存/时延不可行（基线约数百词）。

## 方法
在 CB-Whisper 式 OV-KWS 上三维压缩：(1) sparsemax 门控 + 熵稀疏自动选出预测力最强 Whisper 层（实验得 14/16/32）；(2) MLP 把隐维压到 64；(3) 1D CNN+池化帧率减半。压缩嵌入预存词表库；检出词写入 Whisper 解码器热词提示。不微调 ASR。

## 实验与结果
相对未压缩基线，嵌入约小 128×。ACL6060：LHF-comp MER 21.9、实体召回 57.2，内存 11 MB vs 基线 1406 MB；Aishell（训练未见中文）召回 71.3、MER 14.7；内部葡语医学 16,062 词表内存 882 MB vs 112,929 MB，RTF 0.76 vs 4.52。KWS F1 在压缩后仍可比或更好。

## 结论
作者认为层选择+隐维+帧率压缩可使开放词表 KWS 支撑海量词表，并在不微调 ASR、甚至未见语言上保持可比实体召回。

## 点评
生产导向：把“能不能跑上万热词”变成可落地的压缩管线，且保留声学而非纯文本匹配。内部集 MER 略升提醒偏置幻觉风险；依赖 TTS 合成关键词音频的声学匹配质量。


# SPARK: Efficient Audio-Text Matching for User-Defined Keyword Spotting via Spiking Neural Networks

- 论文编号：3336
- 报告人：Seung-Yeop Baek
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/baek26_interspeech.pdf

## 问题
用户自定义（文本注册）KWS 的 ANN 方案 MAC 重、能耗高，难 always-on；已有 SNN-KWS 多为闭集分类，开放词表未探索。

## 方法
SPARK：端到端脉冲域音–文匹配。SEE 提音频尖峰；STE 将音素嵌入时间展开后用 SDSA 做时空注意；SPE 拼接音文尖峰用 SDSA 提对齐特征；判别器出句级与音素级匹配概率，BCE 双损失。SDSA 用 Mask&Add 线性复杂度、乘法免。PLIF 神经元，仿真步 \(S=8\)。

## 实验与结果
LibriPhrase：相对 CMCD/PhonMatchNet，参数 287K（约 2.1× 更少），能量 18.44 µJ（相对 PhonMatchNet 约 21.7× 更低）。LE：AUC 99.07%、EER 3.97%；LH：AUC 82.71%、EER 24.98%，接近但略逊 PhonMatchNet。无预训练音频编码器。

## 结论
作者认为首个端到端 SNN 用户自定义 KWS 框架可在保持竞争力检出的同时大幅降能耗与参数。

## 点评
把开放词表验证迁入原生脉冲计算，针对边缘 always-on 约束。Hard 集上与强 ANN 仍有差距；能量为 45 nm 理论估算，实芯片事件驱动收益需再验证。


# Scalable Keyword Spotting via Modular Network Expansion

- 论文编号：987
- 报告人：Viktor Khaymonenko
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/khaymonenko26_interspeech.pdf

## 问题
嵌入式固定词表 KWS 部署后常需加新关键词，但原训练数据不可用，全量微调会灾难性遗忘且破坏已上线阈值与行为。

## 方法
参数封顶的模块化扩展：冻结整条基座（含 BN 统计）与核心分类头；挂接 ≤10k 参数的 Expanded Blocks（拼接冻结层激活 + Conv1D/BN/hard-swish）与独立 New Head。推理用 core-first：先按原阈值判核心词，仅拒绝时再看新头。保证核心 logits/决策规则对任意输入与出厂模型完全一致。基座约 150k 的 SVDF 风格网络。

## 实验与结果
GSC v2 五组 held-out 词对扩展，FAR 在 Common Voice 上标定 1%。新词宏平均 FRR：提出方法 4.37%，优于 Ensemble 6.46%、LoRA 6.41%、Adapters 8.05%；全微调新词好但核心 FRR 从 2.71% 飙到 69.08%。同预算下 MACs 16.34M，低于 Adapters/LoRA。消融显示扩展深度约 4 块最优。

## 结论
作者认为在无原数据与严格不回退约束下，模块化扩展可有效加入新关键词并保持出厂核心检测器不变。

## 点评
把“不回归”做成构造性保证（冻住路径），比 EWC/适配器的软约束更贴合产品安全。代价是新词依赖轻量旁路容量；扩展深度过深时基座最深层对核心词过专、迁移变差。


# Streaming Open-Vocabulary Keyword Spotting via Role Swapping in Cross-Attention

- 论文编号：1676
- 报告人：Liming Song
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/chen26q_interspeech.pdf

## 问题
跨注意力开放词表 KWS 多在整段语音上工作；流式时若仍把语音作 Key/Value，只能见局部帧却需全局上下文，与注册文本作 Query 的数据流不匹配。

## 方法
角色互换：流式语音作 Query，注册文本嵌入作 Key/Value，帧级更新亲和矩阵并做决策。约 0.8M 文本注册模型；因果卷积+GRU 音频编码器。两阶段训练：先用注意力输出对齐文本语义，再用亲和矩阵+音频嵌入训练帧级判别。辅以 InfoNCE、PhoneMatch、在线时域掩码硬负样本。

## 实验与结果
LibriPhrase：LPE EER/AUC 6.82%/97.95%，LPH 28.21%/79.19%；LPH 优于 SYNASPOT-AT 与 CTCAT。相对 CTCAT 在简单负例略弱，但困难负例更稳。单线程 RTF 0.065（float32）。消融显示硬负样本对 LPH 有益。

## 结论
作者认为角色互换使跨注意力可流式部署，并以端到端网络决策替代 CTC/启发式后处理，在困难负例上更鲁棒。

## 点评
关键洞察是流式场景下 Q/K/V 角色与信息粒度的匹配，工程上去掉 CTC 对齐降低部署复杂度。LPE 上未全面领先说明简单场景对齐法仍强；文本注册实例化，语音注册泛化需另证。


# MPA-KWS: Multi-Modal Phoneme-Level Alignment for Streaming Open-Vocabulary Keyword Spotting

- 论文编号：2485
- 报告人：Jue Zhang
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26fa_interspeech.pdf

## 问题
音素级对齐有助于区分易混词，但多数非流式；现有流式 CTC 对齐多仅支持文本注册，且训练/推理对齐策略不一致、跨模态 InfoNCE 未利用音–文非对称性。

## 方法
MPA-KWS：因果 Conv1dNet + 交叉注意力偏置注入关键词音素先验；W-CTC 强制对齐聚合音素级声学嵌入（训练推理一致）；音–文用 AsyP 损失、音–音用对称 InfoNCE；验证器交互特征 + BiGRU。支持文本-only 与文本–音频注册（训练 50% 掩码支持音频）。CTC beam-search 动态挖硬负文本。推理滑窗对齐，复杂度 \(O(W\times L_p)\)。

## 实验与结果
LibriPhrase（4.0M 参数）：文本-only AUC LPH/LPE 96.04/99.95，EER 9.53/0.77；文本–音频 97.30/99.98，EER 8.21/0.45，优于所列 CMCD、W-CTC、MM-KWS、PLCL。消融：去音素损失、去增强、去偏置、仅 InfoNCE 均掉点。

## 结论
作者认为统一 W-CTC 流式音素对齐 + 非对称跨模态对比与硬负挖掘，可在流式开放词表 KWS 上达到最佳结果并支持多模态注册。

## 点评
同时解决流式、多模态注册与训练–推理一致三个痛点，LPH 提升说明针对易混词设计有效。模型约 4M，相对超轻流式方案更重；依赖 g2p 与 CTC 对齐质量。


# SSL-based Sequence Matching for Unsupervised Audio Retrieval

- 论文编号：2369
- 报告人：Moreno La Quatra
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/laquatra26b_interspeech.pdf

## 问题
无标注音频到音频检索需稳健表示与序列匹配；不同域（哼唱 vs 口语示例）对连续对齐与离散词袋式匹配的需求不同，尚缺系统比较。

## 方法
冻结 SSL 帧嵌入（HuBERT/WavLM/w2v2/MERT/voc2vec 等）；可选 K-Means 得聚类嵌入或聚类 ID。匹配：DTW（连续/聚类嵌入）或 TF-IDF/BM25（离散 ID）。在 MIR-QBSH 哼唱检索与自建 QbE-LibriSpeech 短语检索上评 Accuracy/MRR/R@3/R@5；辅以 Soft-DTW 与 Temporal TF-IDF 分析时间敏感性。

## 实验与结果
哼唱：DTW + 原始 SSL 最优，HuBERT-LS Accuracy 0.765、MRR 0.801；文本式匹配明显更差。口语 QbE：TF-IDF on C-IDs 最优，HuBERT-LS Accuracy 0.633、MRR 0.723；DTW 反而弱。均值池化余弦全面落后。结论：音乐依赖音高轨迹轮廓，语音更依赖离散单元分布。

## 结论
作者认为无监督 SSL 检索应域依赖地选择匹配：连续 DTW 利音乐，离散 TF-IDF/BM25 利语音，且无需任务特定训练。

## 点评
贡献在“匹配范式 × 域”的系统对照与机制解释，而非新模型。QbE 集规模较小；K 与层选择影响大，实际部署需再调。


# To Be Multimodal or Not to Be: Query-Adaptive Audio-Visual Person Retrieval via Active Modality Detection

- 论文编号：790
- 报告人：Mark Gales
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/loweimi26_interspeech.pdf

## 问题
真实广播档案中目标可能仅闻其声、仅见其人或二者皆有；对缺失模态固定融合会注入噪声，使精度低于最佳单模态。

## 方法
在 MVSE（ECAPA-TDNN 说话人 + ResNet 人脸，零样本）上加查询自适应：用各模态 top-n 检索的组内分数与跨模态分数（一方检索集上另一方的分数）刻画模态一致性；分类器判 AoP/VoP/AVP 并设融合权重 \(\lambda\in\{1,0,0.5\}\)。语料 BBC Rewind（>12,000 视频）。

## 实验与结果
模态检测准确率约 89%。检索 P@1：自适应 94.2%，优于说话人-only 82.9%、人脸-only 93.4%、固定融合 90.0%；相对 oracle（96.6%）收回约 64% 的固定融合差距。固定融合在 VoP/AoP 上明显伤 P@1。

## 结论
作者认为先检测活跃模态再融合，比盲目多模态更好，避免缺失模态噪声。

## 点评
问题设定贴近真实档案，跨模态一致性作诊断信号直觉清晰。人脸单模态已很强，自适应主要补“该不该融”的决策；检测错误仍会落到次优 \(\lambda\)。


# Not All Frames Are Equal: Difference-Aware Quantization for Ultra-Low-Bit ASR

- 论文编号：1569
- 报告人：Woori Jeon
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jeon26c_interspeech.pdf

## 问题
将 GPTQ/AWQ 等 PTQ 直接用于 Whisper 在 2–3 bit 时严重退化甚至幻觉循环。语音激活在稳态与零填充区高度相关，在音素边界变化剧烈；帧均等进 Hessian 会使静态/填充主导校准，掩盖关键过渡。

## 方法
DiffAQ：用帧间激活差 ∆xt=xt−xt−1 的 L2 范数作时间密度，归一化后得权重 wt=α+(1−α)d̄t（α=0.2），缩放 Hessian 累加。仅改编码器线性层；解码器仍用标准 GPTQ。训练无关，校准 128 条 LibriSpeech train-other，评 Whisper base/small/medium、LibriSpeech 与 FLEURS。

## 实验与结果
3-bit 全配置最低或近最低 WER；2-bit 增益最大：Medium test-other 17.53%→12.93%，FLEURS 18.05%→12.07%；Small FLEURS 3-bit 11.37%→8.69%。RTN/AWQ 常 WER>100%。Base 在 2-bit 仍崩坏，属容量瓶颈。α 不敏感。

## 结论
按声学变化率加权 Hessian 可改善超低比特 ASR 的 PTQ；2-bit Medium 权重大约从 1.5 GB 压到 <200 MB。局限：噪声瞬态也可能获高权重；未验证其他编码器架构。

## 点评
抓住语音相对文本的“时间冗余/填充陷阱”，把 PTQ 校准偏到音素过渡，改动小、解释清楚。强在无需重训；弱在 Base 2-bit 仍不可救，且差分对非语音瞬态不具选择性。


# Positional Encoding in the Context of Memristor-Based Analog Computation for Automatic Speech Recognition

- 论文编号：683
- 报告人：Benedikt Hilmes
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hilmes26_interspeech.pdf

## 问题
忆阻器可模拟执行 VMM 以降耗，但编程与执行噪声大；相对位置编码（PE）对 ASR 尤其低精度很重要，却发现其线性变换输出幅值易被默认 ADC 裁剪，导致映射到忆阻器后相对无 PE 反而更差。

## 方法
在 SynaptogenML 上仿真 CTC-Conformer（~77M）带相对 PE；LibriSpeech 与 Loquacious 250h；权重 8/4-bit、激活 8-bit；ADC 默认 4 精度+4 量程位。分析 PE 线性层 ADC 裁剪（约 40% 时间），试验：扩大量程/精度、固定 8 bit 预算下移位给量程、仅调 PE 层 ADC、去掉 PE 线性层、学习型 PE、数字域保留 PE（oracle）。

## 实验与结果
数字基线：相对 PE 在 4-bit 权重更稳（dev-other 5.6 vs 无 PE 6.5）。默认忆阻器映射后有 PE 反而更差。将 PE ADC 量程提到 8 或固定预算 1/7（精度/量程）可把相对退化约减半，恢复约 15% 相对优于无 PE。去掉编码相关线性变换时相对退化约降 30%。oracle（PE 留数字）接近最优。

## 结论
PE 层输出动态范围与默认 ADC 不匹配是主要病灶；调 ADC 量程或去掉线性变换可恢复 PE 收益。部署需在硬件可改 ADC 与模型改造间权衡。

## 点评
把硬件量化裁剪与相对 PE 的幅值特性对上号，比笼统报“忆阻器掉点”更有指导性。强在软硬协同建议；弱在纯仿真、且评测子集较小（dev-other/dev）。


# Systematic PTQ Study of Integer and Floating-Point Formats for On-Device Whisper ASR

- 论文编号：698
- 报告人：Woosuk Choi
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26_interspeech.pdf

## 问题
端侧部署 Whisper 时，INT/FP 量化格式与激活精度如何影响编码器–解码器 ASR 仍缺系统证据；LLM 上流行的 W4A16 与 NVFP4/MXFP4 是否迁移到 Whisper 不清楚。

## 方法
对 tiny.en/base.en 做 80+ 组 FakeQuant PTQ：INT8/4/3 与 FP8/FP4/NVFP4/MXFP4，扫激活精度、组大小与 SmoothQuant；LibriSpeech test-clean/other；比较面积文献中 FP vs INT 乘法器。给出 Pareto 与六条部署指南。

## 实验与结果
激活位宽主导：16→8 bit 约 +1–3% 绝对 WER；INT16 与 FP16 激活几乎无差别。NVFP4 W4A16 在 base.en 达 4.88%（距 FP32 0.07%、约 6.4× 压缩）；MXFP4 标准 PTQ 严重崩（tiny 可达 38–94%）。INT3 近不可用。Pareto：>约 36 MB 时量化 base 优于 tiny。

## 结论
保 16-bit 激活比抠权重更重要；NVFP4 是近无损 4-bit 首选；FP 激活路径因乘法器面积更小更适合 NPU。指南覆盖 20–80 MB 预算。

## 点评
工程向系统扫参，结论可直接指导格式选型。强在激活位宽与 NVFP4 vs MXFP4 的机制解释（E8M0 尺度过粗）；弱在仅 tiny/base、FakeQuant 非真机延迟，且未与 GPTQ/AWQ 权重敏感方法交叉。


# Pushing the Limits of Compression: Sub-1-Bit Conformer via Variable-Rank Binary Decomposition

- 论文编号：2063
- 报告人：Jinsu Yeo
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yeo26_interspeech.pdf

## 问题
Conformer-Transducer 端侧内存受限；整数量化有 1 bit/参数硬下界。解码器对误差敏感需高精，编码器冗余多，若解码器不能再压，只能把编码器压到亚 1-bit，但标准量化做不到。

## 方法
LittleASR：用 LittleBit 式变秩二值分解 ˜W=diag(h)Ub diag(ℓ) Vb⊤ diag(g)，以秩 r 准连续控制有效 bpw。梯度敏感度 Ω(l) 引导可微预算搜索，编码器压到亚 1-bit、解码器/联合网保留更高秩，再 QAT。目标含点卷积、LSTM 投影与线性层；Conv2d 用 INT4 RTN。NeMo Conformer-Transducer Large（120M），LibriSpeech。

## 实验与结果
混合秩 1.0 bpw：dev-other WER 6.01%（AbsMean tensor 6.30%，尺寸约 18.8 MB）。可到 0.2 bpw（7.1 MB），整数基线无法进入。同尺寸下混合秩优于均匀秩（如 0.4 bpw：8.78 vs 10.82）。分配显示浅层编码器约 0.3–0.4 bpw、深层与 Value 投影更高、联合网约 2.0 bpw。

## 结论
变秩二值分解打破 1-bit 地板，敏感度分配在极端压缩下拓宽 Pareto 前沿，适合超紧内存 ASR。

## 点评
把“编码器可狠压、解码器要护”落到连续秩预算，而非死守离散比特档，问题意识准。强在亚 1-bit 可达与层内（如 Wv vs Wq）细粒度；弱在依赖 QAT、二值 GEMM 真机收益未测，且极端 0.2 bpw WER 仍明显抬升。


# Pruning as Regularization: Sensitivity-Aware One-Shot Pruning in ASR

- 论文编号：3411
- 报告人：Julian Irigoyen
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/irigoyen26_interspeech.pdf

## 问题
剪枝常被当作训后压缩；编码器–解码器 ASR Transformer 是否存在过参数冗余，使无微调的一次性幅度剪枝反而改善泛化，尚缺系统敏感度诊断。

## 方法
对 Whisper-small（244M）做训后梯度与对角 Fisher 敏感度诊断；按模块/层（早中晚）做无结构幅度剪枝，无微调。主评 LibriSpeech test-other（基线 WER 11.64%），掩码原样迁到 Common Voice、TED-LIUM。敏感度引导组件级稀疏度分配。

## 实验与结果
解码器整体更脆弱；全局剪枝 30–40% 崩溃。解码器自注意力 50% 剪枝：test-other 绝对降 2.38%；编码器末四层 50%：降 1.72%。解码器早层/FFN 极脆。40.8% 稀疏度下敏感度感知压缩近保基线，全局幅度剪枝则塌。跨语料增益可迁移。

## 结论
一次性幅度剪枝可作隐式正则；解码器自注意力与深层编码器冗余可剪，解码器早期与 FFN 需保护。方法模型无关但需按架构重验敏感度剖面。

## 点评
把“剪枝=压缩”翻成“剪枝=正则”，并用一/二阶诊断对齐实证，视角新鲜。强在无微调即增益与跨库迁移；弱在非结构化稀疏未加速实际推理，且相对某流水线基线报告，不宜与官方 Whisper 数字硬比。


# Leveraging Temporal Redundancy via Layer-wise Key-Value Pooling Attention for Efficient ASR

- 论文编号：2124
- 报告人：Yi Wu
- 程序：Tuesday 29 September 2026 / Resource Constrained Speech Recognition
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wu26k_interspeech.pdf

## 问题
自注意力 O(T²) 限制长序列 ASR；粗时间下采样伤边界精度。语音帧高度冗余，K/V 作上下文不必与 Q 同分辨率，固定步长池化又忽略层间冗余差异与相对位置错位。

## 方法
KV-Pooling Attention：对 K/V 平均池化（步长 s），Q 保持原分辨率，复杂度 O(T²/s)；中心对齐相对位置编码；因果掩码按池化窗右边界、padding 需窗内全有效。分析 Zipformer 层间帧相似与熵，浅层大步长、深层小步长，集成 KV-Pooling-Zipformer（步长配置如 4,2,1,2）。Pruned RNN-T，AISHELL-1 与 LibriSpeech。

## 实验与结果
AISHELL-1：L/M/S 测集 CER 分别 6.58→6.35、6.57→6.35、8.10→7.87；摘要称绝对约 -0.2% CER。LibriSpeech：L 上 clean/other 3.33/8.32→3.30/8.09；摘要称约 -0.3% WER。EPYC 7763 上推理 RTF 约改善 10%。注意力图更集中于对角。

## 结论
非对称分辨率注意可利用时间冗余加速并略提准确率；层差分步长与位置/掩码适配是落地关键。

## 点评
把“语音帧冗余”直接写进 K/V 池化，比整体下采样更保边界。层自适应步长有分析依据；增益幅度不大，小模型在 clean 上偶有回退，平滑可能抹掉细微音素细节。


# PART: Progressive Alignment Representation Training for Multilingual Speech-To-Text with LLMs

- 论文编号：1734
- 报告人：Pei Zhang
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26aa_interspeech.pdf

## 问题
多语 SLM 常冻住 LLM、混训多语多任务，易把各语音频表示压到共享空间，损失细粒度语言差异，且任务级对齐粗糙。

## 方法
PART 三阶段：① 仅训 adapter 做语内 ASR 粗对齐；② 渐进解冻编码器（先末 8 层再全量）+adapter，仍仅 ASR；③ 解冻 LLM，联合 ASR+S2TT。SenseVoice-large 编码器 + Qwen2.5（1.5B/7B）→ PART-2B/8B。数据：ASR 810k h（10 语）、S2TT 434k h。

## 实验与结果
FLEURS/Common Voice：PART-2B 平均 WER 4.7/7.4，优于同规模 Baseline-2stage（6.4/9.2）与 Whisper-large-v3；PART-8B 更优。CoVoST2 xx→en：PART-8B 平均 BLEU 39.1。消融显示去 ASR→S2TT 分阶段、去 LLM LoRA、去渐进解冻均降点；梯度相似分析显示语内对齐增强且跨语边界仍可区分。

## 结论
分阶段语内再跨语、任务依赖启用 LLM，可在保留语言特异性的同时提升多语 ASR 与翻译。

## 点评
抓住“过早混语混任务导致表示坍缩”的训练病，用进度表强迫先学语内映射再借 LLM 跨语。强在同数据预算对比清晰；大规模商购数据细节不可复现，方法迁移价值大于具体分数。


# Alignment-Aware Continued Pre-training for Multilingual Speech Representation Learning

- 论文编号：1185
- 报告人：Xuyang Wang
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lu26b_interspeech.pdf

## 问题
多语 SSL 基座常直接监督微调做 ASR，声学–符号对齐全压到微调阶段；异质文字与长尾语种下跨语泛化受限。

## 方法
在 MMS 300M 上插入对齐感知继续预训练：联合 SSL（对比+多样性）与 CTC，并对上下文/量化表示做随机替换使 CTC 梯度可进量化路径。比较建模单元 Char / IPA / Uroman；提出语言感知双码本（全局+语种特异，加性融合）缓解离散空间竞争。其后仍 CTC 微调。

## 实验与结果
FLEURS：Direct FT 47.2 WER → Continual SSL 43.4 → Joint(Uroman) 36.6；双码本再降至 35.5。Uroman 优于 Char 的 WER，Char CER 略优；IPA 因 G2P 覆盖/噪声在跨语上更差。MLS→FLEURS 未见语上 Uroman 更稳。

## 结论
对齐感知联合 SSL–CTC 继续预训练显著优于直接微调或纯 SSL 继续预训练；统一罗马化与双码本有助跨文书共享与长尾公平。

## 点评
把“符号对齐”前移到表示塑造阶段，比只换微调配方更治本。Uroman 实用折中 IPA 的资源依赖；双码本设计贴合长尾竞争，但语种码本规模与维护成本在更大规模上仍待验证。


# Synthetic Audio Generation Framework for Air Traffic Control Speech Recognition

- 论文编号：2422
- 报告人：Zhe Zhang
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bagat26_interspeech.pdf

## 问题
ATC 语音噪声大、L2 口音重、真实标注稀缺，通用 ASR 退化；传统增强难覆盖口音/说话人多样性，L1→L2 口音转换尤缺。

## 方法
合成管线：先分离语音/噪声并 AudioSR 超分，再经 F5-TTS、kNN-VC、TokAN 式 L2→L1，以及重用 TokAN 的可控 L1→L2（微调 token 转换与 token-to-Mel，条件目标口音）；最后 AAS（8 kHz 重采样、200 Hz 高通、注入原句噪声）。L1→L2 幻觉用 Whisper WER>50% 过滤。下游微调 Whisper-small，4 折交叉验证 ATCO2 约 4 h。

## 实验与结果
OOB Whisper 63.32% WER；仅真实微调 22.69%。仅合成中 VC+AAS 最佳约 24.18%。真实+合成时 L1→L2 AC 最优达 21.64%，显著优于仅真实；L2→L1 混训反而变差（25.92%）。AAS 对 TTS 等增益很大；口音多样性比单纯说话人多样性更关键。

## 结论
面向 ATC 的生成式增强（含可控 L1→L2）能在极少真实数据下提升识别，真实+L1→L2 合成优于仅真实微调。

## 点评
问题抓的是 ATC 的“信道+口音”双缺口，把 L1→L2 当多样性源而非归一化预处理。评测严谨（配对手测）；合成过滤丢约 35% 样本，且数据量仍小，扩展到更大 ASR 与细粒度流利度控制是自然下一步。


# GigaAM Multilingual: Foundation Model for Underrepresented Languages

- 论文编号：2483
- 报告人：Andrei Kuzmenko
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kuzmenko26_interspeech.pdf

## 问题
多语 ASR 在中亚长尾语（哈/吉/乌）上因数据极度偏斜表现差；朴素上采样易伤头语种，需可迁移的预训练与微调采样策略。

## 方法
GigaAM Multilingual：600M Conformer，HuBERT 式掩码单元预测，在约 2M 小时音频上预训练。用语言共现图聚类得 5 簇，簇级重加权（最终 E2 提高中亚簇权重）。微调 CTC 共享字符表，数据含开源/众包/弱监督/合成；域感知采样避免合成子集主导。

## 实验与结果
哈/吉/乌在 CV、FLEURS、内部野外集上大幅优于 Whisper-large-v3、Seamless M4T、Omnilingual 1B。匹配 CTC 微调下，即便 240M 变体平均 WER 亦优于 Whisper/Omni。簇重加权 E2 改善目标语且俄语几乎不变；域感知采样尤其抬升内部自发语。极低覆盖巴什基尔/格鲁吉亚适配亦最优。

## 结论
簇级预训练平衡 + 域感知微调是长尾多语 ASR 的有效配方，并开源编码器与 ASR 模型。

## 点评
贡献在数据混合与采样工程，而非新目标函数；受控编码器对比说明“预训练分布匹配目标语族”比盲目用更大通用编码器更重要。合成/弱标签过滤细节决定可复现性。


# Low-Resource Medical ASR for Rich Transcription in Latvian

- 论文编号：3469
- 报告人：Arturs Znotins
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/znotins26_interspeech.pdf

## 问题
拉脱维亚语医学口述需富文本转写（标点、缩写、数字、单位、术语），域数据仅数十小时；通用模型 WER 可从个位数升至 12–46%，规则 ITN 难维护。

## 方法
对比端到端富文本微调（Whisper/Canary/Gemma-3n）与“逐字 ASR + LLM 格式化”。用 Gemini 将遗留逐字稿与人工报告配对生成格式化标注，并扩 75 h LLM 校正伪标签（WER>15% 丢弃）。指标含 WER、标点/命令/数字/医学实体错误率。训练：先通用拉脱维亚再 LVMED。

## 实验与结果
通用基线极差；ft-whisper-large-v3 达 11.1% WER，加伪标签 10.6%；双阶段 Whisper+ft-gemma3-12b 约 11.2%，标点命令最好（PC-ER 2.1%）。跳过通用语适应或仅有通用数据均更差。学习曲线显示数据少时 LLM 管线更优，数据充足时两端到端接近。

## 结论
有限域数据 + LLM 策展/伪标可使低资源医学富文本 ASR 达可用质量；端到端与 ASR+LLM 在足够域数据下竞争力相当。

## 点评
实用路线是“活化遗留逐字语料 + 伪标扩量”，指标设计贴临床格式需求。临床幻觉风险作者自承；依赖已有人工报告做策展，无报告场景需更多人工核验。


# Probing LoRA-to-LoRA Cross-Lingual Transfer for Unseen Low-Resource Conditions in Whisper-Based ASR

- 论文编号：1133
- 报告人：Spandan Dey
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mondal26_interspeech.pdf

## 问题
低资源 ASR 中，先前 LoRA-to-LoRA 迁移多针对 Whisper 预训练已覆盖的语种；对基座几乎未见、零样本 WER≈100% 的真正低资源语，捐赠语选择与迁移是否仍有效尚未知。

## 方法
两阶段捐赠选择：先限同语系，再在候选中最小化 Jensen–Shannon 正字法（词元分布）散度。在 Whisper-small 上先训捐赠语 LoRA（r=32，Q/V/Out/FFN），再以其权重初始化接收语 LoRA。捐赠：Hindi/Marathi/Bengali（IndicVoices）；接收：Bhojpuri Rural Woman、Konkani、Assamese（40–100 h）。

## 实验与结果
捐赠初始化相对仅接收语 LoRA 一致更优，相对增益约 9–17%（Hindi→Bhojpuri 40 h 达 17%）。JS 选中的捐赠优于同文字其他候选。零样本极高 WER 确认属未见设定，增益主要来自结构对齐而非强预训练先验。

## 结论
即便捐赠与接收均弱覆盖预训练，基于谱系+正字法相似度的 LoRA-to-LoRA 仍可提供更优优化起点，适合参数高效扩展低资源语。

## 点评
把“未见语”从高资源锚点迁移中拆出，并用可测正字法散度替代启发式配对，方法清晰可复用。绝对 WER 仍偏高（方言/数据少/仅 LoRA），贡献在相对迁移而非刷榜。


# Overcoming Decoder Inconsistencies in Whisper for Dravidian and Low-Resource Languages

- 论文编号：1007
- 报告人：Kumud Tripathi
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kumar26c_interspeech.pdf

## 问题
Whisper 在达罗毗荼语上 WER 显著高于印度-雅利安语；语料分析显示更长词、更高 TTR、更低重复，错误多为已知词内字符替换，解码器自注意与交叉注意失衡。

## 方法
在 Whisper-medium 解码器每层加轻量 Weighted-Attention（门控调节自/交叉注意）；在倒数第二层做 Self-Conditioning，把中间预测投影回加到隐状态并辅 CE。形态切分仅作分析工具。Kathbath 八语评测，并外推到韩语、斯瓦希里语。

## 实验与结果
基线平均 WER 19.79，形态切分后 17.18。Weighted-Attention / Self-Conditioning / 组合在 MS 设定下平均再降约 1.5–1.65 点，马来雅拉姆等增益更大。韩语 3.34→2.51、斯瓦希里 16.07→14.58。参数增幅 <1%，推理延迟增 <2%。

## 结论
面向黏着语形态稀疏的解码器条件化可稳定降低字符级替换错误，并泛化到非印度黏着语。

## 点评
诊断（已知词内替换）与改动（平衡声学/语言注意、反馈中间预测）对症。形态切分提示问题本质，但主贡献是训练期解码器改造；增益幅度中等，强在轻量与跨语一致。


# The Impact of Informal Persian Speech on Low-Resource ASR and Speech Translation

- 论文编号：2454
- 报告人：Hadi Alizadeh
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/alizadeh26_interspeech.pdf

## 问题
波斯语正式/口语差异大，公开数据多正式朗读，非正式自发语音导致声学–文本错配，ASR/ST 在真实对话上严重退化。

## 方法
构建 T-PID：影视中单人片段人工转写非正式波斯语，ChatGPT-4o mini 译英并抽样质检（改写 WER≈4%），最终 36.77 h、22,443 句、性别均衡。针对性文本规范化并开源 Persian normalizer。微调 Whisper-small/medium 与 Wav2Vec2-BERT；级联 NLLB-200 做 ST。

## 实验与结果
基线 Whisper 在 T-PID 上因幻觉 WER 极高（200+/360+）；微调后 small/medium 约 37.5/36.3，Wav2Vec2-BERT 29.1，且 Common Voice/FLEURS 正式集也提升。级联 ST：微调后 T-PID BLEU 最高 25.30（Wav2Vec2-BERT+微调 NLLB）。T-PID 困惑度远高于正式集，解释困难度。

## 结论
高质量非正式波斯语可显著改善低资源 ASR/ST，并增强对正式域的泛化；数据集与规范化工具已公开。

## 点评
贡献在填补“口语对齐转录+平行英文”空白，而非新架构。音频优先、转写贴口语利于 CTC；翻译依赖 LLM 抽样质检，成语/文化表达仍可能有噪声。


# BELLA: Efficient Bilevel Learning with LoRA for Multilingual ASR

- 论文编号：2771
- 报告人：Xiaodong Cui
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/saif26_interspeech.pdf

## 问题
编码器–LLM 多语 ASR 中共享解码器易交叉语干扰；路由专家依赖桥接对齐质量，对齐与预测双向耦合，朴素联合训练难兼顾。

## 方法
BELLA：Whisper 编码器 + 可训桥（Q-Former）+ 冻结 Qwen2.5-7B；解码器 MoE-LoRA（共享适配器+K 专家）由路由按桥输出与语言嵌入选专家。双层优化：下层最小化嵌入回归+KD+权重衰减（对齐），上层最小化 ASR NLL+负载均衡/熵（预测）；单环惩罚梯度交替更新，避免昂贵内层求解。

## 实验与结果
CoVoST2 五语（英/西/俄/葡/瑞典）。相对 bridge-only、单 LoRA、按语固定多 LoRA，BELLA 多数语种最低或接近最优 WER；相对基座相对降约 2–4%。专家选择图显示语种特化、未坍缩。ML 在部分高资源语略优但需显式语种选适配器，扩展性较差。

## 结论
用双层学习显式分离对齐与语种特化，可在参数高效条件下缓解多语干扰并稳定路由。

## 点评
把“桥对齐 ↔ 路由选专家”的耦合写成双层问题，比简单多 LoRA 更有结构。实验语种偏高/中资源；相对按语固定 ML 的优势更多在可扩展路由而非绝对分数。


# Automatic Lyric Transcription for Greek Songs: Scaling and Task Composition Effects in Whisper Adaptation

- 论文编号：1371
- 报告人：Dimitrios Damianos
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/frangiadaki26_interspeech.pdf

## 问题
歌词转写（ALT）因旋律、节奏与伴奏比语音难，希腊语此前无系统 ALT 基准；Whisper 零样本在歌声上退化严重。

## 方法
从 GAD 策展 GAD-ALT：Demucs 分离人声、CTC 强制对齐、gpt-4o-mini 段级英译，17,458 段约 19.65 h，按歌划分。对比 Whisper Small/Medium/Large-v3：仅转写、2:1/4:1 转写–翻译多任务、两阶段（先冻编码器在 Common Voice 希腊语上适应解码器，再全开歌声微调）。

## 实验与结果
零样本 WER 92.3/65.1/53.6；最佳为 Large-v3 两阶段 27.2%。小模型受益于多任务正则（Small 2:1→33.6%），大模型更适合专注转写/两阶段。人声干声优于混音；人工增强/混音训练反而变差。错误类型含语义替换、边界漂移、幻觉、正字歧义等。

## 结论
建立希腊 ALT 首个基准；规模与任务组成交互明确，两阶段+大模型最有效。

## 点评
贡献在低资源 ALT 管线与受控消融，揭示“多任务主要帮小模型”。歌声–语音域差仍主导错误结构；阶段一用朗读稿可能声学上仍远歌声，作者已提示可换更富韵律中间域。


# CrossPhon-Tonal: Streamlining Cross-language Modeling for Forced Alignment in Low-resource Tonal Languages

- 论文编号：1770
- 报告人：Hongchen Wu
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wu26e_interspeech.pdf

## 问题
跨语强制对齐（CLFA）对声调语常忽略声调或依赖专家手工映射；忽略声调损害边界，手工又慢且难复现。

## 方法
CrossPhon-Tonal：在 CrossPhon 发音特征坐标映射音段后，对 Chao 调号做自动声调映射——先同轮廓类，再最小化首末音高水平差，并列时取更近音高；凹/凸无同类则回退首半轮廓。输出中间词典供目标语声学模型对齐。评测普通话、粤语、泰语、越南语、豪萨语、克罗地亚语。

## 实验与结果
相对语言专属基线的边界一致率（0.025 s）上，自动映射与专家映射总体相当，部分对（如泰模型对齐普通话 0.772 vs 专家 0.726）更优。声调模型常优于 3600 h Global English（如泰→普通话 0.772 vs 英 0.638）。小数据映射目标（如克罗地亚）与家族差异大时效果不均。

## 结论
自动声调编码可去掉专家瓶颈，且声调特异性往往比单纯数据规模更关键。

## 点评
把声调当“类附加符号”接进既有音段管线，工程可扩展。质量依赖源/目标词典与目标模型小时数；非声调强模型在印欧对上仍可胜，说明音系相似度与声调并非唯一因素。


# Improving Adversarial Robustness in Spoken Language Identification through Self-Defensive Distillation

- 论文编号：3091
- 报告人：Spandan Dey
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/dey26_interspeech.pdf

## 问题
对抗攻击在 ASV/ASR 中研究较多，但独立 LID 前端被攻击可拖垮多语后端，文献中系统分析与防御不足。需在白盒梯度攻击下评估 SOTA LID 并构建主动防御。

## 方法
提出 Self-Defensive Adversarial Re-Training（SDART）：在对抗重训（ART）上叠加 (1) 对抗样本挖掘 ASM（随 epoch 提高攻击比例，PGD 步长在 [0.010,0.035] 均匀采样）；(2) 无教师、基于在线标签平滑（OLS）的防御蒸馏，用上一 epoch 按语言聚合的软标签；(3) 动态 α 与按预测熵加权的软标签；(4) 仅用正确分类的干净样本更新语言软标签矩阵。主干主要为 ECAPA-TDNN，输入 80 维 log Mel；攻击含 FGSM/PGD。

## 实验与结果
VoxLingua-10（十大语）与 Common Voice 同语种；评测 EER 与 \(C_{avg}\)。基线 ECAPA 在 PGD（0.03, 5 步）上显著变差。VoxLingua-10 上 SDART：干净 EER 2.801、FGSM 3.666、PGD 3.544，优于 ART、TRADES、DD、MART。Conformer 与 Common Voice 上多数设置亦最优；从 Conformer 迁移攻击到 ECAPA 的黑盒场景中 SDART 仍低于基线 EER。

## 结论
SDART 在多种架构与语料上同时改善干净与对抗 LID 表现，优于常见主动防御；未来拟扩展到更多攻击与其他语音任务。

## 点评
把 ASM 的渐进域暴露、语言条件软标签与“只用干净正确样本引导”串成 teacher-free 蒸馏，针对 LID 的跨语一致性而非通用 logit pairing。脆弱点是攻击设定集中于白盒 FGSM/PGD 与固定步长区间，更强或自适应攻击下的外推未充分验证。


# Probing the Layer-wise Geometry of Chinese Dialect Representations in Wav2Vec 2.0

- 论文编号：975
- 报告人：Zhen Peng
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/peng26c_interspeech.pdf

## 问题
Wav2Vec 2.0 层间如何编码方言特征不清楚；现有探测多面向标准语，中文方言工程应用常默认用顶层或简单聚合，可能丢掉中间层细粒度语音信息。

## 方法
MagicHub 五方言：西南官话（四川、武汉）、中原官话（郑州）、吴语（上海）、粤语（广州）；Azure TTS（zh-CN-XiaoxiaoNeural）生成对应标准普通话作参考锚点；VAD 去静音，16 kHz。冻结 Wav2Vec 2.0 XLSR-53 的 24 层 Transformer，提取隐状态。几何探针：与锚点的归一化 DTW 距离；方言质心两两欧氏距离 + MDS；凝聚层次聚类建谱系树。

## 实验与结果
几何指标呈三阶段：L1–8 声学主导、距离高且与物理差异一致；L9–19 距离平台、保留细粒度可分性；L20–24 距离骤降（流形收缩）。MDS：L1 无序；L12 非官话靠近、官话分离且空间分散；L24 整体向中心收缩。层次聚类 L12 对郑州等局部音系敏感，L24 自发呈现与传统分类一致的宏观分支（吴/粤 vs 官话）。

## 结论
中文方言表征经历声学→语音分化→空间收敛；深层收缩可视为特征过滤器，突出宏观分类。建议口音等细粒度任务优先中间层，宽泛方言分类可用深层。

## 点评
用无参几何探针把“层该怎么用”落到可操作建议，比只报分类准确率更有解释力。合成普通话锚点便于控内容，但也可能引入 TTS 声学偏置；五方言规模有限，谱系对齐是否稳健需更大说话人池验证。


# Robust Language Identification Using Semi-positive Contrastive Learning

- 论文编号：2502
- 报告人：Shubham Sharma
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sharma26_interspeech.pdf

## 问题
低资源口语语言识别易过拟合录音条件等域特征，跨语料泛化差；多模态方法常把同语样本一视同仁，未显式建模同语异域方差。

## 方法
提出 Semi-positive Contrastive Learning（SpCL）：双模态音频–文本编码器映射到共享 512 维空间。目标矩阵 \(T\)：同语同域为 1，同语异域为 \(\alpha\in(0,1)\)，异语为 0。总损失 \(\lambda L_{con}+(1-\lambda)L_{cls}\)（\(\lambda=0.3\)）。文本侧用静态模板或由音素序列构成的动态 caption；推理仅用音频编码器+分类器。音频编码器试 wav2vec2 音素变体与 Whisper，文本为 RoBERTa。

## 实验与结果
12 种印度语言，训练见域 Ekstep+DatasetM(rs)，未见域 yt 与 IndicVoice。SpCL whisp（dynamic）准确率：Seen 98.76%、yt 91.42%、IndicVoice 54.52%，优于 MFCC/音素 Conformer、UDA、Whisper 微调等基线。VoxLingua33 上 SpCL whisp dynamic 93.0%（MuSeLI 96.1%）。消融：\(\alpha=0.7\) 与动态 caption 对未见域帮助最大。

## 结论
半正对比与动态 caption 可在无显式域适应下提升跨域 SLID；Whisper 音频编码器最稳。未来拟在联合嵌入空间做推理。

## 点评
把“同语异域”单独加权，比二元对比更贴合域偏移几何。强在训练要文本、推理只要音频。脆弱点是 IndicVoice 全体仍偏低，且域标签需在训练期可知；\(\alpha\) 需调参。


# Predict-Then-Adapt: Inferring Coordinates from Speech for Continuous Geo-Conditioned Dialectal ASR

- 论文编号：3333
- 报告人：Pouya Mehralian
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/mehralian26_interspeech.pdf

## 问题
连续地理坐标条件（如 GLoRIA）可改善方言 ASR，但推理时常无可靠说话人坐标；离散方言标签又难以刻画连续变异。

## 方法
在冻结编码器上挂轻量 Coordinate Regression Head（CRH）：多头注意力池化 + MLP，SmoothL1 回归经度/纬度。两遍推理：(1) 关闭 GLoRIA 预测 \(\hat{c}\)；(2) 用 \(\hat{c}\) 打开坐标门控低秩适应再解码。骨干为 180M Cascaded Encoder Dual Features（12 层 Conformer + 6 层 Transformer），在 GCND 荷兰方言语料上适配。CRH 增参 <0.1%，时延开销 <3%。

## 实验与结果
CRH 大圆误差随时长下降，约 10–30 s 达 15–25 km 量级（30 s overall avg 23.72 km；插值约 16 km，外推约 38 km）。GLoRIA 对坐标扰动在 ≤15 km 几乎无影响，25 km 平均 <1 个 WER 点。10 s 无元数据设置：CRH+GLoRIA 平均 WER 32.62，优于同秩 LoRA（35.67），接近 oracle 坐标（32.04），远好于 Whisper large-v3 / OWSM。

## 结论
从语音推断坐标足以激活大部分地理条件收益，且保持 GLoRIA 可解释门控；外推区更难，未来可做不确定度感知条件化。

## 点评
把“缺坐标”问题收成可度量的定位误差与 WER 鲁棒半径对齐，工程闭环完整。两遍推理开销可控是亮点。脆弱点在训练坐标流形外的方言（如 Limburgs）与短时（3 s）回归到均值；语言学分辨率限制使误差难压到公里级邻域密度。


# Dialect Bias in Speech Recognition Across 10 Spanish and French Varieties

- 论文编号：458
- 报告人：Rodrigo Nieto
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nieto26_interspeech.pdf

## 问题
ASR 方言偏差研究多聚焦英语，西语与法语等全球语言的系统差距机制不清；Common Voice 等资源多为朗读标准文本，难以暴露形态与话语标记等方言特征。

## 方法
从 Apple Podcasts 构建约 20 小时、性别平衡、按国家方言分层的评测语料（西语 5 种、法语 5 种，共 10 方言、129 说话人），人工转写保留方言正字法。评测七个模型（含 Whisper v2/v3、Otter、GPT-4o-Transcribe、Wav2Vec2、Qwen2-7B、SALMONN-7B）。对 Whisper v3：JSD word-shift 做词汇分析；用 pyannote 与 Whisper L16 说话人嵌入做方言分类与声学距离–WER 相关；LoRA 微调并分别冻结编码器/解码器定位误差源。

## 实验与结果
方言间 WER 差异显著（西语 Kruskal–Wallis H=179.24；法语 H=63.18）。西语：阿根廷/多米尼加最好，智利最差，并非人口规模单调；法语：欧洲变体整体优于加拿大与非洲。性别差距因方言而异。词汇侧见 voseo“矫正”、区域词与 pues 等话语标记失败；声学侧方言–性别分类准确率西语约 83–86%、法语约 67–77%，与 WER 相关。微调：冻结编码器接近全 LoRA，冻结解码器几乎无增益，显示偏差主要在解码器。

## 结论
西法 ASR 误差系统反映相对训练分布的语言/声学距离；公平 ASR 需建模方言语言特征。语料与诊断框架可复用于其他语言。

## 点评
把基准、JSD 错误词与解码器定位串成因果链，比单纯报 WER 更有解释力。播客语体与门控发布限制外推到全部语域；小数据 LoRA 无法消除差距，也点出仅靠轻量适应不够。


# DASR-CPO: Reference-Free Contrastive Preference Optimization for Correcting Mandarin Semantic Drift in Low-Resource Chinese Dialect ASR

- 论文编号：1228
- 报告人：Tao Zhang
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26s_interspeech.pdf

## 问题
Whisper 等预训练 ASR 在低资源中文方言上常出现 Mandarin Semantic Drift：把方言词解成音近但义错的高频普通话同音词（如“阆中→郎中”）；LoRA SFT 降 CER，却不显式压制这些竞争假设。

## 方法
提出 DASR-CPO：离线从基线假设挖掘混淆（去调拼音编辑距离≤2 的高频替换）构成硬负例；用全序列动态匹配在 BPE 下定位方言跨度；在 teacher-forcing 参考上对跨度打分，取最强负例做 reference-free CPO，并与 SFT CE 混合 \(L_{SFT}+\lambda L_{CPO}\)。骨干 Whisper-Large-v3 + LoRA（q/v，r=32）；Stage1 SFT 3 epoch，Stage2 CPO 2 epoch（β=0.5，λ=1.0，冻结编码器）。

## 实验与结果
MagicData 四川话 ASR-CSICHDIACSC（4.53 h，24 说话人，8:1:1）。相对 Pure LoRA：CER 24.85%→22.58%，方言实体 F1 72.82→74.15，Recall +1.55，假正例 39→32；优于 Context Bias 重加权。推理无额外开销。局限：划分非说话人无关、依赖词表与挖掘质量。

## 结论
把方言适应写成对漂移跨度的偏好排序，可在极低资源下同时改善 CER 与实体语义，且零推理开销；未来拟扩到更多方言与语码转换。

## 点评
针对“音近义错”这一解码先验问题，跨度级硬负对比比纯似然或 token 重加权更贴病灶。非 speaker-disjoint 与小词表可能夸大泛化；CER 绝对值改善有限，但实体指标更能说明语义收益。


# Cross-Lingual Compositional Learning for Code-Switched Lip Reading

- 论文编号：1163
- 报告人：Jeonghyeon Joo
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/joo26_interspeech.pdf

## 问题

语码转换在多语交流中普遍，但视觉语音识别（唇读）缺真实混合语料；CSLR 规模小、句式重复。多语 VSR 默认“一句一语”，难直接泛化到句内切换。

## 方法

提出 CoCoVSR：从中英单语视频拼接伪混合样本（双向顺序），与真实 CSLR 联合训练；在预训练 MultiVSR 上微调视觉前端，并用共享 LoRA adapter（非整语专家）适配 Transformer 编解码，利用跨语共同 viseme。

## 实验与结果

CSLR：CER/WER/MER 16.69/16.23/16.48，大幅优于先前 CTC/MoE 等方法（MER 约 37+）。MultiVSR 中文与未见 LRS2 英语仍保持可竞争水平。仅训 CSLR 混合集最好但单语崩；加入 CoCo 数据可在混合与单语间折中。共享 decoder adapter 优于多 adapter。

## 结论

作者认为无需额外采集或生成合成，跨语拼接 + 共享轻量适配即可让多语唇读获得语码转换能力，并尽量保住原多语性能。

## 点评

抓住视觉跨语 articulatory 重叠，故意不用 ASR 里常见的语言专家路由，参数更省。拼接伪混合边界生硬，与真实切换韵律/口型过渡有差距；CSLR 本身模式重复，SOTA 幅度需结合数据特性解读。单语保留与混合精度的权衡在消融中交代清楚。


# Refining Pseudo-Audio Prompts with Speech-Text Alignment for Text-Only Domain Adaptation in LLM-Based ASR

- 论文编号：977
- 报告人：Ryo Magoshi
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/magoshi26_interspeech.pdf

## 问题

LLM-ASR 在新领域常只有文本、无配对语音。仅微调 LLM 缺声学上下文；伪音频提示要么依赖 TTS 难扩展，要么只做文本嵌入上采样/掩码，未对齐音频编码器与投影器输出特性。

## 方法

提出 TE2SL：用可训练 Conformer 精炼模块，把 LLM 文本嵌入映射到真实音频提示潜空间。先在源域配对数据上学习文本嵌入→音频提示对齐；适配时冻结该模块，对目标域文本嵌入随机上采样、精炼并时间掩码，生成样本相关伪音频提示，再与指令一起微调 LLM。对比 text-only FT、Soft Prompt、Upsample-and-Mask。

## 实验与结果

英：LibriSpeech→SPGISpeech/SlideSpeech；日：CSJ SPS→APS（eval1/2）。TE2SL 全面最优：如 SPGISpeech WER 8.5（基线 11.1）、Rec OOV 50.1%；SlideSpeech WER 14.0；CSJ eval1/2 CER 19.6/17.5，OOV 召回亦最高。

## 结论

作者认为伪提示需同时样本相关且感知编码器/投影器特性，才能在纯文本适配中弥合模态差并提升领域词覆盖。

## 点评

把“伪音频提示像不像真提示”当成可学习对齐问题，比启发式上采样更对症。不依赖 TTS，利于多语扩展。精炼模块质量绑死源域配对数据；跨域声学差异极大时，伪提示仍可能偏语言侧。


# Content-Aware Dynamic Compression for Efficient Speech Recognition based on Large Language Model

- 论文编号：230
- 报告人：Bingqian Wang
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhu26_interspeech.pdf

## 问题

LLM-ASR 常用固定步长下采样压缩声学序列，忽略内容动态，易丢信息或冗余，损害准确率–效率权衡。

## 方法

用 Continuous Integrate-and-Fire（CIF）作动态前端：对冻结编码器输出预测 firing 权重，累加触发声学嵌入，训练时用 MAE 使权重和逼近转写 token 数；推理无文本时仍生成与内容匹配的变长序列，再经适配器送入 LLM。对比 Conv-MLP / Concat-MLP 固定 DS=2/4/6。

## 实验与结果

AISHELL-1（FireRed 编码器）：Dyn-MLP CER 2.67–3.53，ASEL 27，相对 WEST 固定基线相对降错约 15–33%，长度约减 61%。StepAudio2 设定下相对相近 ASEL 固定基线可相对降错约 12–26%，ASEL 常减约 60%。GigaSpeech Stage2 CER 11.20（ASEL 39）。TTFT 在较长句上降约 7–19%。回归损失 MAE/MSE/SMAE 影响很小。

## 结论

作者认为内容引导的 CIF 动态压缩可在更短 LLM 输入下保持或提升识别，改善准确率–效率权衡，并在大规模数据上可扩展。

## 点评

把“该留多少帧”绑到文本长度，比盲目加大固定下采样比更合理。推理无真值长度依赖学到的速率先验，极快/极慢语速可能偏。编码器冻结利于稳定，也限制与映射器联合再优化声学表示。


# Upcycling Pretrained Transformers into Mixture-of-Experts for Multilingual Speech Recognition

- 论文编号：1630
- 报告人：Kentaro Shinayama
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/shinayama26_interspeech.pdf

## 问题

多语联合微调大预训练 ASR 时，共享容量不足易负迁移，甚至不如分语种模型。LoRA-MoE 等轻量专家容量有限，难充分表达语种差异。

## 方法

将 Whisper 解码器 FFN 上循环（复制预训练参数）为稀疏 MoE，每 token 仅激活 1 个专家，活跃参数与稠密模型相同。路由：按语言身份硬路由，或基于隐状态（±语言嵌入）的 soft top-1。编码器保持共享。在 CommonVoice 10 语与亚洲 4 语上评测。

## 实验与结果

CommonVoice：硬路由 10 专家平均优于 MultiFT 与 LoRA-MoE，甚至优于 MonoFT 上界（西欧 5 语 WER 12.3 vs MultiFT 13.6）。亚洲 4 语硬路由平均 CER 5.2 vs MultiFT 6.2（约相对降 16%）。上层解码器放置 MoE 即可接近全层效果且参数更少。对 medium/large-v2 仍有效。Soft 路由更省专家数但弱于硬路由。

## 结论

作者认为直接扩容 FFN 专家比低秩专家更利于多语微调；硬路由强制语种分工，减轻负迁移；语言依赖主要在解码器上层。

## 点评

“上循环=复制 FFN 成专家”简单可落地，推理成本几乎不变。硬路由需可靠语言 ID；soft 路由因专家同初始化难分化是文中坦承的局限。对书写体系差异大的语种集合尤其有说服力。


# Token-Independent Language Representations for Low-Latency Configurable Multilingual Speech Recognition

- 论文编号：2455
- 报告人：Hongxu Zhu
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhu26c_interspeech.pdf

## 问题

可配置多语 ASR（CMM）用语言特定模块（LSM）支持任意语种子集，但解码器 LSM 每步重算，延迟随输出长度线性增长，长句开销大。

## 方法

保留编码器一次计算的神经 LSM；解码器改为 token 无关语言表示：CMM-S 用静态语言向量做加性调制；CMM-D 再融合顶层编码器 LSM 的句级池化动态线索与可缓存静态矩阵扩展，门控合成一次后整句复用。每步 LSM 复杂度从 O(d²) 降到 O(d)。

## 实验与结果

MLS 8 语：CMM-D allhot/onehot 平均 WER 8.70/8.67，与原 CMM 持平，优于多语基线 9.26。平衡 4 语（含粤/普/英/马，含语码转换）同样 parity。长输出（110–130 token）上原 CMM 额外延迟 +107.88 s，CMM-S/D 仅约 +2.23/+7.34 s，峰值额外延迟降逾 90%。

## 结论

作者认为语言身份是全局属性，不必绑在自回归逐步环上；编码器告知的 token 无关表示可在精度相当下大幅降延迟。

## 点评

把“可配置多语”的延迟瓶颈拆开：编码器保留动态语言声学，解码器只做常向量/句向量加法，工程洞察清晰。CMM-S 略损精度、CMM-D 补回，消融逻辑完整。依赖用户/提示给出语种子集；极端语码切换仍靠编码器侧 LSM。


# GC-LoRA: Gated Convolutional LoRA for Parameter-Efficient Acoustic Adaptation

- 论文编号：822
- 报告人：Abeer Alwan
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/shankar26_interspeech.pdf

## 问题

Whisper 等 Transformer 基础模型在混响、窄带、方言、儿童等声学失配域上掉点；标准 LoRA 调全局注意力，缺局部时序建模，难以补足 Conformer 式局部归纳偏置。

## 方法

提出 GC-LoRA：在 MHSA 输出投影 Wo 的低秩旁路中，嵌入 Conformer 风格门控深度可分离卷积（pointwise+GLU、depthwise、GroupNorm、Swish、再 pointwise），在瓶颈内做局部精炼。相对标准 LoRA 参数更少（如 medium 上 447k vs 829k）。

## 实验与结果

Whisper-medium：AMI/SWBD/CORAAL/MyST WER 11.5/6.3/9.9/8.6，相对 LoRA 显著更优（p&lt;0.05），参数约少 46%。跨 tiny–large-v3 多数设定仍优；tiny+AMI 相对降约 10.9%。消融显示门控深度卷积优于简单 Conv-LoRA / MultiConv-LoRA；推理延迟几乎与 LoRA 相当。

## 结论

作者认为在 LoRA 瓶颈内注入局部卷积，能以极少参数让 Transformer 获得更强声学域适应，缩小与全量微调差距。

## 点评

针对“Transformer 缺局部”的结构补丁放在注意力输出处，不改预训练全局注意，设计克制。增益在失配域一致，但绝对幅度不大；全量微调仍常更强。超参固定跨模型规模，可能解释部分非单调缩放。


# MambAdapter: Lightweight Mamba-Based Adapters for Parameter-Efficient Transfer Learning in Speech and Audio

- 论文编号：1522
- 报告人：Umberto Cappellazzo
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ali26b_interspeech.pdf

## 问题

微调大语音/音频基础模型成本高，PETL 已普及；Mamba 擅长线性复杂度长序列建模，但尚未作为适配器注入 Transformer 做高效迁移。

## 方法

提出 MambAdapter：在瓶颈适配器低秩空间插入轻量 Mamba，并用可学习缩放 α；跨层共享 down/up 投影以抵消 Mamba 参数开销。用于 AST 音频分类与 Whisper 多语 ASR（仅编码器插适配器，解码器冻结）。

## 实验与结果

分类（Pfeiffer）：MambAdapter 约 0.06M 参数，平均准确率 89.72，接近 Conformer 适配器（0.27M，90.07）且远超 LoRA/Bottleneck。ASR（五语）：平均 WER 优于 Bottleneck/Conformer/LoRA（同参预算下约降 0.8–7.4%）。低参预算（&lt;500k）优势更大；去 Mamba 则 FSC 等任务大幅掉点；共享投影以约 4× 参数换不到 1% 平均收益。

## 结论

作者认为把 Mamba 放进共享投影瓶颈，可在更少可训参数下匹配或超过强 PETL 基线，是首个将 Mamba 用于语音/音频 PETL 的工作。

## 点评

用 SSM 的时间压缩特性匹配低秩瓶颈，理论动机清楚。分类上与 Conformer 适配器接近但更省参；ASR 增益更明显。超参（expand、d_state、kernel）对结果敏感，文中有网格分析。未探索解码器侧适配。


# PhonePrune: One-shot Phoneme-Aware Pruning for Large-scale ASR Models via Phoneme Set Generation and Calibration

- 论文编号：1787
- 报告人：Minsik Lee
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26q_interspeech.pdf

## 问题

大规模 ASR 一次性剪枝常按幅度丢弃小权重，但部分小权重对细粒度音素辨别关键（Phoneme Ticket Hypothesis）；剪掉后擦音/塞音等区域识别崩溃。

## 方法

PhonePrune：按音系约束生成对比三元组校准集（互补分布、最小对等）；用掩码梯度得音素相关性分数；复合得分 S=|W|+λ|W|·S̃_ling 调制剪枝阈值，保护音素票。在 Whisper-large 50% 稀疏度一次性剪枝，校准 128 三元组。

## 实验与结果

相对幅度/OBS 等非结构化剪枝大幅更好。对 Distil-Whisper：韩/日 Common Voice 相对 WER 降 13.41%/13.83%（15.50/16.20 vs 17.90/18.80）；英语略逊于蒸馏模型，平均 WER 11.50。作者归因韩语细谱对比与日语时长对立更依赖脆弱音素票。校准样本数与 λ 消融显示 N=128、γ=0.5 较稳。

## 结论

作者认为压缩需显式保护编码精细音素的低幅度子网；音素感知校准可在高稀疏下更好保持识别，尤其对音系细节重的语言。

## 点评

把剪枝从纯幅度启发式拉回音系先验，解释了为何韩/日增益更大。一次性、无重训利于部署。校准依赖对齐音素片段与手工三元组，扩展到更多语言需重复工程；英语冗余线索多时收益较小符合叙事。


# Can Large Language Models Reliably Correct Errors in Low-Resource ASR? A Contamination-Aware Case Study on West Frisian

- 论文编号：1659
- 报告人：Yun Hao
- 程序：Tuesday 29 September 2026 / Cross-Lingual and Multilingual Speech Recognition 1
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hao26b_interspeech.pdf

## 问题

低资源 ASR 仍弱；LLM 生成式纠错（GER）在高资源语上有效，但低资源语覆盖不足，且公开评测可能污染导致虚高。需污染可控地检验是否真能纠错。

## 方法

以 XLS-R 为弗里斯兰 ASR；在 Common Voice 与新建非公开文本的 Offline 集（故事书+原创句，4 男声，1.5 h）上做 GER。比较生成式纠错与从 5-best 选择；模型含 Qwen3（±LoRA）、GPT-4o-mini、GPT-5.1；零样本到少样本。并做句级改进/退化统计与编辑级精度召回。

## 实验与结果

CV：基线 WER 13.5，oracle 9.6；GPT-5.1 生成式最低 8.9（超 oracle），选择式仅约 12.1。Offline：基线 21.1，GPT-5.1 最低 13.8（亦超 oracle 18.0），与公开集趋势一致，支持非污染解释。Qwen3 几乎不改。生成式比选择式更强；GPT-5.1 句级改进多但也可能退化；插入纠错召回高、精度偏低，删除相反。

## 结论

作者认为强 LLM 的 GER 在低资源弗里斯兰上有效且可超 N-best oracle；非公开集上的相近增益表明并非仅靠污染。开源小模型收益有限，效果高度依赖模型语言覆盖。

## 点评

用非公开文本听写集专门压污染假说，方法学贡献突出。生成式可跳出 N-best 是关键优势。强依赖闭源 GPT；开源侧几乎无效，部署可复现性受限。纠错会引入新插入错误，实际需配合置信度或过滤。


# ViP-VL: Vietnamese Self-supervised Speech Pretraining Model with Vector-Quantization Learning

- 论文编号：1077
- 报告人：Kiet Anh Hoang
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/le26b_interspeech.pdf

## 问题
越南语标注稀缺，需要公开、可部署的 SSL；既有 wav2vec2-Vi 延迟高，大规模工作权重未公开。BEST-RQ 搭配 8× 下采样易因 mask 与编码器不同步而掉点。

## 方法
ViP-VL：BEST-RQ + ChunkFormer，78M 参数，8× 时间下采样。用声学堆叠（15 帧窗、步长 8，拼接优于平均）与感受野对齐同步 mask 流形；在 10 ms filterbank 上先 mask，再按“至少 80% 组成帧被 mask”判定下采样帧是否 mask，有效时间 mask 约 45%。在约 17,000 小时无标注越南语上预训练。下游：ASR（VLSP 等）、情感（ViSEC）、方言（ViMD）、说话人验证（VoxVietnam）。

## 实验与结果
LibriSpeech 验证：ViP-VL 平均 WER 9.7，优于未对齐的 8× BEST-RQ（11.9），对齐 2× 量级。越南 ASR 平均 WER 13.76，优于 Wav2vec2-Large-Vi（17.89）与 PhoWhisper-Large（14.09）等（同范式比较）。SER UA 74.45%；方言区域/省级 F1 93.24% / 57.17%。低资源 ASR 曲线显示预训练相对从零训练优势随标注减少而增大。权重与实现开源。

## 结论
在高压缩 SSL 中，mask–下采样同步与感受野对齐和数据规模同等重要；按此训出的公开 ViP-VL 在多项越南语任务上达 SOTA 级表现。

## 点评
把“8× 掉点”归因到同步错误并用堆叠/阈值 mask 修掉，比一味堆数据更有方法贡献。公开权重填补社区缺口。与用远更大数据/监督的系统对比时需注意设定差异；省级方言仍难，说明细粒度变体仍是瓶颈。


# Dissecting ASR Failures in Low-Resource South Asian Languages

- 论文编号：1382
- 报告人：Agha Ali Raza
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/azeemi26_interspeech.pdf

## 问题
Urdu、Punjabi、Pashto、Sindhi 使用相近 Perso-Arabic / Gurmukhi 脚本、正字法不统一且命名实体常跨脚本出现，现有多语 ASR 多只报聚合 WER，难以区分声学识别失败、脚本解码错误与评测伪影。

## 方法
在 Common Voice 22.0 与 FLEURS 上零样本评测 Whisper-medium / large-v3、MMS-1b、SeamlessM4T-Medium / Large（共 40 配置）。用 jiwer 计算 WER/CER，事后按 11 类错误 taxonomy 分解：脚本混淆、编辑操作、重复循环、数字、正字变体、字符混淆、命名实体、Latin 词、OOV/稀有词、时长、跨语言污染等。实体由 LLM 标注；并对 Whisper 错误脚本输出做音译后处理，对 Perso-Arabic 做 Unicode 归一化后再算 WER。

## 实验与结果
SeamlessM4T-Large 在 8 组中 6 组最优（Urdu FLEURS 16.3%、Punjabi 22.1%）；MMS 在 Sindhi 两集最好。Whisper 在 Punjabi/Pashto/Sindhi 上大量错脚本，WER 常超 100%；音译后处理可回收至多约 25 个百分点 WER。Unicode 归一化平均降低 Pashto WER 3.1 点。稀有词准确率约 20–62%；短句 WER 高于长句；Sindhi 输出中 12–35% 字符来自其他语言（多为 Urdu）。

## 结论
聚合 WER 系统性误判南亚低资源 ASR 失败性质：脚本混淆、Unicode/正字歧义与跨语干扰是主因；语言适配架构更稳，生产级仍远未达到。局限包括 Sindhi CV 仅 40 句、仅零样本未微调。

## 点评
把“听错了”与“写错脚本/评测过严”拆开，对多脚本低资源族很有诊断价值；音译与归一化是低成本可落地的补丁。弱在测试集方言信息缺失、Sindhi 样本极少，且未验证微调后失败模式是否仍以脚本为主。


# Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition

- 论文编号：3408
- 报告人：Kavya Manohar
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/juvekar26_interspeech.pdf

## 问题
Whisper 等对印地语族微调常在朗读/录音棚语料上变好，却在自发口语上显著退化（studio-bias）；常见保守学习率与 easy-to-hard 课程未必适合低资源音系适应。

## 方法
构建 Vividh-ASR：按声学复杂度分 Tier A（studio）、B（broadcast）、C（spontaneous）、D（合成噪声，仅评测），覆盖 Hindi 与 Malayalam，聚合 Kathbath、Shrutilipi、IndicVoices、FLEURS 等。用 2×2 因子实验解耦学习率时机（递减 vs 递增）与课程方向（easy→hard vs hard→easy）。据此提出 R-MFT：Stage1 自发语高 LR（2e−4）→ Stage2 广播（1e−4）→ Stage3 A+C 混合巩固（1e−5）。并用 CKA、SVD、EMD 等分析 encoder/decoder 表征变化。

## 实验与结果
早期高 LR 是主因：Malayalam 上递减相对递增约有 12–13 点全局 WER 优势；hard-to-easy（R-MFT）再额外改善 Malayalam（39.35% vs Standard MFT 42.25%），Hindi 两课程均收敛约 18.8%。R-MFT Medium 全局 WER：Mal 39.36%、Hi 18.82%；244M Small 达 44.41%/21.41%，优于保守低 LR 的 769M。表征上成功配方主要改动 decoder，encoder CKA≈1；IndicWhisper 则扰动 encoder（CKA 0.775）并扩大有效秩。

## 结论
适应效率由更新时机与复杂度排序共同决定；R-MFT 使小模型在自发 Indic ASR 上可比甚至超过常规大模型微调。后续拟扩展语言与选择性冻结 encoder。

## 点评
把“数据不够”转为“优化轨迹不对”，用分层基准钉住 studio-bias，对法庭听写等真实场景有针对性。强在因子设计与表征证据一致；弱在语言仅两种、Tier D 为合成噪声，且与 IndicWhisper 训练分布不完全可比，因果解释需谨慎。


# Unified Gradient Projection: Language-Balanced Continual Learning for Multilingual Low-Resource ASR

- 论文编号：1915
- 报告人：Wei-Qiang Zhang
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ren26g_interspeech.pdf

## 问题
对 Whisper 等做低资源多语序贯微调易灾难性遗忘；A-GEM 等梯度投影在重放缓冲语言不平衡时会被主导语言偏置，低资源语言更易被覆盖。

## 方法
提出 Unified Gradient Projection（UGP）：每步从各历史语言均匀采样构造语言均衡参考梯度 g_ref；若当前梯度与 g_ref 内积为负则投影到其正交补。同时与 Experience Replay 结合，混合 batch 上做 L_cur + λ L_replay（λ=1）。中大型 Whisper 冻结 encoder 只训 decoder/embedding；small 全参微调。

## 实验与结果
主场景（FLEURS）：目标 Malay/Indonesian/Filipino/Javanese/Māori，重放 Thai/Vietnamese/English/French。Whisper-large-v3 上 UGP：TWER 12.91、RWER 6.68、AWER 9.80、FWER 0.04（近零遗忘）；FT 的 FWER 在 medium 可达 89.80。消融显示投影与 ER 互补：单独投影 FWER 4.20，完整 UGP 达 0.04。扩展语组与 50h→5h 数据尺度上，UGP 持续压低遗忘并保持较好 AWER。收敛后梯度余弦更近正交，冲突弱于 FT。

## 结论
语言均衡梯度投影加 ER 可在多语低资源持续学习中兼顾可塑性与稳定性，大模型上遗忘近零。作者认为这为通用语音识别的持续适配提供高效路径。

## 点评
抓住多语重放里“参考梯度被大语绑架”这一具体失效点，比笼统加正则更对准问题。强在跨尺度与稀缺数据验证；弱在主实验语言组与缓冲语言固定、数据尺度分析仅在 small，对更长任务序列是否仍稳需另证。


# Beyond Standard Greek: Adapting Whisper for Greek Dialects through Curriculum Multitask Learning

- 论文编号：2567
- 报告人：Vassilis Katsouros
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/klimi26_interspeech.pdf

## 问题
希腊方言相对标准现代希腊语（SMG）存在明显“方言税”：零样本 WER 常极高，普通微调仍大幅落后 SMG；多任务与课程学习各自有效，但少有按监督类型做跨任务/跨域递进的适配。

## 方法
四阶段 staged multitask curriculum：Stage0 仅希腊→英语音译（G_ST）；Stage1 以 α 混 SMG ASR 与方言 ST；Stage2 以 β 混方言 ASR 与方言 ST；Stage3 纯方言 ASR。任务提示动态注入 decoder。实验方言为 Cypriot、Cretan、Messenian；donor 用 GPC-5h；英译由 Llama-Krikri 生成并人工校对。评测 Whisper-small/medium/large-v3，encoder 冻结、卷积特征可训。

## 实验与结果
Curriculum 在各方言与规模上均优于零样本与常规 FT。例如 Cypriot small：ZS 81.27 → FT 52.38 → Curr. 35.61；large-v3 Curr. 24.89。Cretan/Messenian 同样有一致降幅。α/β 比例模型相关：small 上 0.5/0.5 最好（33.56）。去掉翻译监督的 ASR-only 课程全面变差（small 上可差超 12 点 WER）；极低资源 Messenian 上缺少 GPC donor 也更易受损。

## 结论
沿任务（翻译→ASR）与领域（SMG→方言）递进可减轻分布失配、稳定低资源方言适配，一致优于朴素微调。后续拟考察语言距离、参数高效适配与更难接触方言。

## 点评
把 donor 语、音译辅助与课程调度串成对角线路径，对“有近亲高资源语但方言标注极少”的场景很实用。强在三方言多尺度与消融完整；弱在部分方言时长极短（如 Messenian 预处理后约 37 分钟）、英译依赖 LLM+人工，推广到接触型北方方言仍待验证。


# Vimarsha: Faithful ASR Evaluation for Indian Languages with Demographic Diversity, In-the-Wild Audio and Spelling Variations

- 论文编号：3348
- 报告人：Kaushal Bhogale
- 程序：Tuesday 29 September 2026 / Multilingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bhogale26b_interspeech.pdf

## 问题
印度语 ASR 评测存在双向失真：干净受控语料带来乐观偏差；单一刚性参考又因拼写/语码混写变体惩罚合法输出，带来悲观偏差。缺少同时覆盖真实声学难度与多合法转写的基准。

## 方法
构建约 100 小时 Vimarsha，覆盖 22 种法定印度语言：Controlled On-Field（COF，43.3h，356 区、约 5099 说话人，朗读/即兴/电话对话）与 In-the-Wild（IW，56.1h）。IW 经多模型 CER 分歧与 BEATs 声学标签筛选难样本。用多 ASR 假设对齐并经 133 名标注员校验，构建 lattice of variations；以 OIWER（相对 lattice 最优路径）评测 10 个系统（IndicConformer、Saaras、Sarvam Audio、AWS/Azure/AssemblyAI/ElevenLabs/GPT-4o/Deepgram/Gemini 等）。

## 实验与结果
各模型在 IW 上均退化：领先系统由约 10–15% 升至 27–34% 平均 WER；AWS 相对增幅最大，GPT-4o 在 IW 近崩溃（约 89，个别语可达 150+）。I-Conf 两 split 领先且人口统计敏感度低（<2 点）；对话场景整体最难。地区 WER 跨度大（如 Bharuch 4.6 vs Koppal 54.9）。短句与极慢语速显著抬高 OIWER；Mantra/Choir 等事件普遍难，儿童喊叫等事件模型间分歧极大。

## 结论
真实声学与拼写容差会改变模型排名与部署判断；COF 不足以代表上线就绪。作者开源基准、协议与结果，以推动更贴近印度语言可变性的 ASR。

## 点评
同时纠正“测太易”与“判太严”，用 COF/IW 与 lattice/OIWER 形成完整评测叙事，对 Indic 选型很有用。强在覆盖 22 语与地理切片；弱在 IW 难样本筛选依赖现有 ASR/标签器，可能偏向特定失败模式，且部分语言时长偏短。


# Transitional Objective Learning with Connectionist Temporal Classification in Phoneme Recognition

- 论文编号：1040
- 报告人：Izabela Krysińska
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/krysinska26_interspeech.pdf

## 问题
CTC 音素识别早期易陷入 blank 主导的“抑制期”，梯度弱、对齐难学；全程细粒度音素目标加剧该问题。

## 方法
Transitional Objective Learning（TOL）：课程式动态加权多个不同粒度 CTC 目标（粗语音特征类→细音素），权重由重要性分数经 Softmax 随 epoch 转移，总损失为加权和。在英语 TIMIT、波兰 LnNor、法语 Vibravox 等上对比标准 CTC 微调。

## 实验与结果
相对基线 PER 相对降约 9.5–14.3%（TIMIT 0.049→0.044 等），t 检验显著。验证曲线显示更快进入 peaking、更早收敛；梯度范数与方差更低。消融表明层级过渡优于仅正则化效应。

## 结论
由粗到细的目标过渡可缩短 blank 主导期、加速收敛并降低 PER，提升 CTC 音素识别稳定性。

## 点评
针对 CTC 经典 blank 病理做课程化损失调度，实现简单、跨语种证据一致。粗类如何定义、权重日程是否需按语种重调，文中依赖声学特征层级；与中间 CTC 正则等方法的直接对比仍可加强。


# Align-Consistency: Improving Non-autoregressive and Semi-supervised ASR with Consistency Regularization

- 论文编号：1471
- 报告人：Wanting Huang
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/huang26i_interspeech.pdf

## 问题
一致性正则（CR）已提升 CTC，但在 Align-Refine 等非自回归迭代对齐精炼及半监督伪标签场景中如何系统结合仍不足。

## 方法
Align-Consistency：对 Align-Refine（CTC 初对齐 + S=2 步 Transformer 精炼）的 base 与各精炼步，在 SpecAugment 双视图上施加 CR；半监督时用非 AR 解码在线生成伪标签并继续训练。ESPnet Conformer，评 LibriSpeech LS-100/960 与 Libri-Light 无标数据。

## 实验与结果
监督：相对 CR-CTC，test WER LS-100 约 12.2/26.7→10.0/22.9，LS-960 4.3/9.9→3.3/7.4；CR 作用于 CTC 与精炼步可叠加。半监督：从 LS-100 模型用 960h 无标可至约 4.3/9.6，再加 LL-6000 至 3.8/9.1；Align-Consistency 伪标签优于纯 CTC。

## 结论
非 AR 精炼与 CR 互相增益；快速并行解码适合在线伪标签，半监督下 CR 对噪声监督仍稳健。

## 点评
把 CR 从纯 CTC 扩到对齐精炼全链路，并证明伪标签质量受益于非 AR，逻辑闭环。超参（α、λ、S）依赖验证调参；未与强 AR 自训练主流路线同协议全面对比。


# COALA: Robust Contextualized Speech-augmented Language Modeling for ASR via Contrastive Regularizer and Biasing Score Estimation

- 论文编号：1097
- 报告人：Jhih-Rong Guo
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/guo26b_interspeech.pdf

## 问题
SLM 语境偏置在大列表与多实体共现时易因上下文窗口与干扰项退化；既往判别损失在多正样本上训练易塌或需辅助 log loss。

## 方法
COALA：冻结骨干 + LoRA，用判别投影器把实体 token 隐状态映射为长度归一化匹配分；提出 Multi-Positive Discriminative Loss（MPD）与 Decoupled Point-wise Discriminative Loss（DPD）缓解多正样本梯度冲突。推理可用 Biasing Target Identification（Top-K 打分）过滤后再送 ASR 提示，并用 `<unbiased>` 阈值。

## 实验与结果
LibriSpeech：DPD 在 test-clean 上 Recall#20 达 99.09%，可独立收敛；相对 Bias-Loss/CTC-Filter 等更稳。加 BTI 后，在 N=500/1000/5000 偏置列表上 B-WER 显著优于无筛选的大列表直接偏置，可扩展到大 N 而避免 OOM。

## 结论
专用打分空间 + 多正样本稳健目标，可在复杂多实体场景提升语境偏置，兼顾列表规模与 B-WER。

## 点评
把“从大列表筛相关实体”从生成分布中拆出，切中 SLM 窗口瓶颈。无偏置时基线 WER 偏高，对比需看相对增益；大 N 下仍依赖 Top-K 启发式与阈值，召回–误召平衡值得更细分析。


# UGPCB: Uncertainty-Gated Phonetic Contextual Biasing for Improving Hotword Recognition in Large Speech Models

- 论文编号：1577
- 报告人：Yong-Jie Hou
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hou26_interspeech.pdf

## 问题
热词语境偏置在 BPE 切分下脆弱；拼音/语音匹配可提召回，但易过偏置与同音误触发。需免训练、可栅控的解码期方案。

## 方法
UGPCB：参数无关 logit bridge 取声学后验熵作不确定性门控，仅在高熵步注入偏置；字素 BPE trie 与拼音（带调/不带调）双轨匹配，并用字素–拼音对比惩罚抑制纯拼音假阳性；配合 N-best 重打分。在 Dolphin 基座、SeACo 测集评估，并测至 1000 干扰项。

## 实验与结果
完整系统：召回 84.19%、F1 90.81%（基线 F1 80.85%）、CER 5.60%；相对文本浅融合召回 +4.68 pp。熵门控降误报；1000 干扰下仍有约 +14.26% 召回增益。精度下降约 0.78 pp 量级、与部分对比差异不显著。

## 结论
不确定性门控 + 双模态拼音匹配可在免训练解码中提升热词召回并抑制过偏置/同音幻觉，适合大模型热词应用。

## 点评
面向普通话同音与 BPE 截断的设计很具体，免训练部署友好。依赖拼音工具规范读音、未枚举多音字；门控阈值与惩罚强度需场景调参，过严会牺牲召回（消融 B3 已体现）。


# Refining the Latent Bridge: Superior ASR Performance via Adapter-Only Alignment with Diffusion LLMs

- 论文编号：2229
- 报告人：Vinayak Abrol
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/bhooi26_interspeech.pdf

## 问题
Speech-LLM ASR 常更新骨干；严格仅训 adapter 时，自回归 LLM 易漂移，而扩散 LLM 的全局精炼是否更耐 adapter-only 瓶颈仍待验证。

## 方法
冻结语音编码器与 LLaDA 等扩散 LLM，仅训练深度 MLP adapter（帧堆叠 + LayerNorm/SiLU）做跨模态投影；对比同设定下的自回归 Llama 等。在 LibriSpeech 多数据量划分评 WER 与 RTFx。

## 实验与结果
960h：test-clean WER 2.807%，相对同设定 AR 约 54% 相对改进，RTFx 约 12.3×（吞吐约 +45%）。低资源多 100h 子集上 dLLM 方差更低、更稳。消融：归一化与手工帧堆叠优于可学习卷积时序；过强 SpecAugment 略伤精度。

## 结论
在严格 adapter-only 协议下，扩散 LLM 比 AR 更可扩展、更快，适合多模态 ASR 集成。

## 点评
把“只训桥”作为硬约束来对比 AR vs 扩散，结论有部署意义。SOTA 数字需放在同冻结协议下理解，未必优于全参微调大系统；adapter 设计消融扎实，但编码器/LLM 选型固定时外推有限。


# DASH: Dual-View Self-Distillation with Multi-Layer Hidden Representations for Robust Speech Recognition

- 论文编号：3232
- 报告人：Jaeeun Baik
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/baik26_interspeech.pdf

## 问题
噪声增强微调常在干净条件掉点并过拟合特定噪声；需在提升噪声稳健的同时保住干净识别。

## 方法
DASH：双分支自蒸馏——干净教师（EMA）与噪声学生；多层编码器隐表示经投影与原型（k-means）分配，用温度 KL 对齐干净–噪声视图。两阶段：无标签蒸馏预训练（约 5k 步，~4% 微调时长）再标准 ASR 微调。骨干 Parakeet-TDT-CTC-110m；噪声视图默认 SpecAugment+加性噪声。

## 实验与结果
相对仅微调，DASH 在 test-clean/other 与多种 SNR 噪声上更优（如 clean 2.02 / other 4.25 vs 基线 2.58/5.41、仅微调 2.14/4.40），并缓解干净–噪声折中。多层蒸馏优于仅末层；EMA 更新有益。Noisy→Clean 配置显示蒸馏阶段本身可赋予噪声不变性。

## 结论
多层原型自蒸馏能以很小开销学习干净–噪声一致性，提升稳健性且不牺牲干净精度。

## 点评
把稳健性做成标签无关预训练阶段，避开与 ASR 损失联合优化的干扰，工程上干净。噪声类型仍偏仿真混合；与 VIC/CR-CTC 等一致性方法的直接头对头对比可再加强。


# Whisper-Aware LLM: Self-Supervised Uncertainty Learning for Robust Whispered Speech Recognition

- 论文编号：879
- 报告人：Gaopeng Xu
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26g_interspeech.pdf

## 问题
耳语缺少基频与谐波结构，声学不确定度高，导致常规 ASR 陷入准确率–可靠性权衡：要么对耳语识别差，要么为提高灵敏度而更容易把噪声幻听成语音。现有伪耳语数据增强存在分布差距，静态投影适配又难以随耳语变化动态调节。

## 方法
在 Qwen2-Audio 上增加轻量 Uncertainty Perception Module（UPM）与 Confidence-Fused Decoding。UPM 用两个自监督任务感知信号质量：F0 轮廓预测（MSE，由预测误差得到帧级置信度）与掩码频谱重建（时间平均得到全局不确定性向量）。解码时，全局向量经 MLP 变成 instruction embedding 作为系统提示；帧级置信度作为可学习标量加权的加性偏置调制 LLM 对声学帧的注意力。训练分三阶段：仅训 UPM 自监督 → 编码器/适配器/UPM/接口联合、LLM 冻结 → 端到端（ASR + 辅助损失，LLM 用 LoRA）。

## 实验与结果
基座为 Qwen2-Audio（Qwen-7B）。UPM 预训练混合 WenetSpeech/GigaSpeech 子集、AISHELL-1、LibriSpeech、wTIMIT、AISHELL6-Whisper 与噪声；微调用上述数据子集。AISHELL6-Whisper 耳语 CER 1.31%（相对此前最佳 Seed-ASR 的 1.58% 降约 17%），正常语音 CER 0.63%。英文 wTIMIT 多口音正常/耳语条件均优于对比系统。AISHELL-1 CER 1.34%、LibriSpeech-clean WER 1.91%。自建 Noise Hallucination Set 上幻觉率 4.5%（强基线多在 25% 以上）。消融：仅注意力调制 3.45%、仅全局指令 1.84%、完整模型 1.31%（基线微调 3.98%）。

## 结论
通过自监督感知信号不确定性并用置信度融合解码，模型在耳语 ASR 上达到文中报告的 SOTA，同时显著降低噪声幻觉，且不明显牺牲通用 ASR 能力。

## 点评
核心不是“把耳语学得更像正常语音”，而是先量化声学证据可靠度再约束生成，直接打在耳语场景的准确率–幻觉权衡上。全局指令对 CER 与幻觉率贡献更大，帧级注意力起补充作用；依赖 F0/频谱自监督与三阶段训练是否在其他 Audio-LLM 上同样稳定，正文未充分展开。


# Probing and Mitigating Hallucinations in Speech-augmented Language Models for Automatic Speech Recognition via Small Language Models

- 论文编号：1278
- 报告人：Bi-Cheng Yan
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yan26c_interspeech.pdf

## 问题
Speech-augmented Language Models（SLM）做 ASR 时仍易幻觉：生成与语音不对齐的额外内容。文中将幻觉词定义为对齐后的一类特殊插入错误。相对视觉–语言与纯文本场景，SLM 的幻觉机制与缓解仍不足。

## 方法
先用因果中介（对 MHA/MLP 做零消融）与注意力行为分析定位幻觉来源。再提出 AudioSLM：在 connector 上建 CTC 模块得到对齐 logits，经 CTC-Gated（深度卷积 + SwiGLU 门控） refinement 音频 token；在 Transformer 块的 MHA 与 MLP 之间插入 cross-attention（query 来自 MHA，key/value 为音频 token），训练时主要更新该层。骨干为 SmolLM2，音频编码器取自 Whisper-large-v2，connector 为 3 层 CNN（下采样 4），LLM 侧用 LoRA。

## 实验与结果
LibriSpeech train-clean-100，评估 clean/other。Dev-clean 上 Vanilla-SLM 的 HER 52.01%、INS 3.69%，AudioSLM 降至 HER 8.69%、INS 0.74%；去掉 CA 或 CTC-Gate 后 HER 升至 11.96%/14.67%。WER：AudioSLM（135M）test-clean/other 为 7.11/11.92，优于 Vanilla-SLM 与 CTC/RNN-T/CTC-Atten，并在 other 上优于 LLM-Guided Decoder（LLaMA-7B）；放大到 1.7B 后 test-clean/other 为 4.71/10.21，但 Dev-clean HER 随规模从 8.69 升到 10.64、12.76。分析显示幻觉词注意力几乎全偏文本 token。

## 结论
幻觉主要来自过度偏向文本先验的自注意力；CTC 对齐门控与跨模态交叉注意力可显著降低 HER，并保持有竞争力的 WER。作者计划后续研究无训练的解码抑制策略。

## 点评
把幻觉形式化为对齐后的插入并做组件级因果分析，使缓解方向有据可依。训练数据仅 clean-100、骨干偏小，规模越大 HER 反升，提示“更强语言先验”与幻觉风险同向；方法强在对齐与跨模态约束，对极嘈杂或开放域场景的外推仍待验证。


# Rank-Distance Based Confidence Estimation for ASR

- 论文编号：1355
- 报告人：Nagarathna Ravi
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ravi26_interspeech.pdf

## 问题
ASR 解码器最大类概率常过自信，无法反映正确性；二值目标的辅助置信度模型（CEM）把部分正确词也标成 0；基于强制对齐的连续目标易受时间戳误差影响；真类概率型连续目标在大词表下又塌缩成近似二值，校准变差。

## 方法
提出 RanD 连续目标：对预测–参考词做编辑对齐，再对 token 对齐；用参考 token 在后验中的归一化秩分数 \(s_{rank}\) 与后验相对 one-hot 的归一化欧氏距离 \(s_{dis}\) 加权（\(\alpha=0.5\)），词级取 token 平均。再按架构从 ASR 抽取词级嵌入训 CEM（shrinkage loss）：CTC 用编码器/解码器隐藏与后验平均；RNN-T/TDT 用预测网络状态与后验；AED 用注意力上下文、解码状态与嵌入。CEM 结构因架构而异（全连接 / BiLSTM / 小 FFN）。

## 实验与结果
在 NeMo 预训练模型上评估：Hindi Conformer-CTC（KB 训练 CEM，PB 作域外）、Conformer RNN-T、Parakeet-TDT、Canary-Flash AED（LibriSpeech 训 CEM，NPTEL/Svarah 域外）。对比 MCP、熵、二值 CEM（M/T/S-CEM 等）及 TeLeS、TruCLeS。RanD 在多数 MAE/KLD/JSD/NCE/ECE/AUROC/AUPRC 上优于或持平 SOTA；例如 CTC 在 KB 上 MAE 0.0570、AUROC 0.8669；RNN-T/TDT/AED 在 LibriSpeech 与域外集上也整体更优，并显示对错配域有更好泛化。

## 结论
用秩与分布距离构造连续置信目标，可避免二值粗糙、对齐不准与真类概率塌缩等问题，在四种 ASR 架构及域内/域外数据上优于文中对比的 SOTA CEM。未来拟覆盖删除错误与低资源场景。

## 点评
RanD 用排序位置代替易塌缩的真类概率，同时用分布距离刻画不确定度，对大词表过自信问题针对性强。方法依赖编辑对齐与架构特定特征抽取，实现成本随 ASR 类型变化；域外结果整体更好，但部分指标并非全面最优，实用时仍需按指标与任务权衡。


# Training-Free Intelligibility-Guided Observation Addition for Noisy ASR

- 论文编号：1096
- 报告人：Haoyang Li
- 程序：Tuesday 29 September 2026 / Robust ASR: Uncertainty and Confidence
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26s_interspeech.pdf

## 问题
噪声下 ASR 差，语音增强（SE）可抑噪但常引入损害识别的伪影。Observation Addition（OA）用权重融合噪声与增强语音、无需改 SE/ASR，但 \(S'\) 若只看噪声侧信号质量，或依赖需标注 WER/CER 训练的神经预测器，则复杂且难泛化。

## 方法
提出无训练的可懂度引导 OA：理想情形用噪声与增强的 WER 反比归一化定 \(S'\)；实际用后端 ASR 置信度近似，\(S'=\mathrm{conf}(y)/(\mathrm{conf}(y)+\mathrm{conf}(\hat{x}))\)，再按 \(\bar{x}=S'y+(1-S')\hat{x}\) 融合后解码。Whisper 用段级平均 log-prob 的 token 加权几何均值；Parakeet/Wav2Vec2-CTC 用 Tsallis 熵（\(q=0.33\)）导出 token 置信度再取几何均值。另比较硬切换（选置信更高者）与基于帧级置信的 OA。

## 实验与结果
SE：Demucs 与 GR-KAN MP-SENet（VoiceBank-DEMAND 训练）；ASR：Whisper-large、parakeet-tdt-0.6b-v2、wav2vec2-large-960h。评测 VoiceBank+DEMAND 与 CHiME-4（Simu/Real，SE 域外）。对比 SNR-OA、DNSMOS-OA、Classifier-OA（2/3 类）。WER-OA 整体最低；实用的 Conf-OA 在多数设置上优于既有 OA 基线（如 MP-SENet+CHiME-4 Real 上 Whisper/Parakeet/Wav2Vec2 为 5.86/5.55/24.03）。误校准子集上 Conf-OA 明显优于硬切换；帧级 OA 相对句级反而变差（如 Wav2Vec2+MP-SENet Real：24.03→25.30）。

## 结论
用后端 ASR 置信度做句级 OA 权重，可在不改动 SE/ASR、无需额外训练的前提下改善噪声 ASR，并优于多种已有 OA；句级融合优于硬切换与帧级融合。

## 点评
把“该信噪声还是增强”直接交给识别器自身置信度，避开了信号质量与 ASR 目标不一致、以及再训预测器的开销。当噪声与增强差距极大时，融合可能略逊于单用更强支路；帧级变差说明时间一致性对后端 ASR 很敏感，句级标量更稳妥。


# ZeroSyl: Simple Zero-Resource Syllable Tokenization for Spoken Language Modeling

- 论文编号：315
- 报告人：Nicol Visser
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/visser26_interspeech.pdf

## 问题
纯语音语言模型需把 SSL 特征离散成单元，但帧级 token 序列过长，长程句法建模困难。Sylber、SyllableLM 等音节单元有效，却依赖多阶段微调与专用目标，管线复杂。

## 方法
**ZeroSyl** 训练免费：
1. 取冻结 WavLM Large 第 13 层特征的 L2 范数，平滑后做突出度峰值检测（\(\delta=0.45\sigma\)）得音节边界。
2. 在边界内对第 22 层特征均值池化，球面 K-means（K=10k，LibriSpeech 100h）离散化；层次聚类把静音质心合并，词表约 9116。
3. 用 OPT-125M 在发现单元上做因果 LM（对比实验 6k h / 扩展 60k h Libri-Light）。

## 实验与结果
边界：R-value 75%、token F1 54%，优于 Sylber，接近 SyllableLM 5Hz。发现质量：SNMI 88.9%、bitrate 52 bps，优于对比音节系统。6k h LM：sWUGGY 68.0、sBLIMP 60.5、tSC 68.1，全面高于 Sylber/SyllableLM。扩展：词汇任务仍逊帧级 SpidR，但句法随数据量上升更陡，60k h 叙事接近 SpidR。

## 结论
作者认为高质量音节发现不必复杂多阶段训练；L2 范数已含可用音节位置信号。局限：音节压缩可能伤稀有/未见词的词汇细节；L2 为何编码音节位置仍待解释。

## 点评
工作价值在「极简有效」：用冻结模型的范数峰值替代专门蒸馏边界网络，却在多项口语 LM 基准超过更重的音节管线。扩展实验也诚实标出与细粒度单元的任务分工（词 vs 句）。脆弱点：强依赖 WavLM Large 特定层；静音合并启发式；对非英语/嘈杂语料是否成立未充分验证。


# Towards Data-free and Training-free Compression for Speech Foundation Models Using Parameter Clustering

- 论文编号：1010
- 报告人：Haoning Xu
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/xu26h_interspeech.pdf

## 问题
语音基础模型（HuBERT、Whisper 等）参数大，端侧难部署。结构化剪枝虽硬件友好，但常按孤立重要性丢弃可能功能冗余却重要的单元，且依赖数据校准/微调；非结构化稀疏又需专用算子。

## 方法
**参数聚类压缩**（数据无关、可训练免费）：
1. 对 MHSA/FFN（及 Whisper 交叉注意力）中结构化单元（注意力头、FFN 中间单元）做 k-means，把相似单元融合成 \(K=\mathrm{round}(N(1-sp))\) 个质心并写回权重，而非直接删除低幅度单元。
2. **混合稀疏**：按层内参数方差把模块分高/中/低三组，高方差层保留更多簇（\(s=0.2\)），全局平均稀疏度不变。
对比基线为同结构的幅度剪枝（MP）。

## 实验与结果
LibriSpeech 上评 HuBERT-large 与 Whisper-large-v3。无微调：HuBERT 50% 均匀稀疏相对 MP，test-clean/other 绝对 WER 降 27.73%/18.61%；Whisper 10% 混合稀疏相对 MP 降 2.86%/5.02%，且相对未压缩基线无显著恶化。HuBERT 聚类后仅 3 epoch 微调，相对 MP 仍有小幅优势。混合稀疏在多数稀疏度优于均匀；过高稀疏（如 Whisper≥30%、HuBERT 60%）会崩溃。

## 结论
作者主张用「合并相似结构」替代「丢弃低幅度结构」，实现可部署的粗粒度、数据/训练免费压缩，并可用方差分配稀疏预算。

## 点评
核心反直觉但合理：高幅度单元若彼此相似，剪枝会留下冗余；聚类融合保留集体信息。数据免费这一点对「训练数据不可得」的商用基础模型尤其实用。脆弱点：极端稀疏仍崩；主要评测在 LibriSpeech 英语 ASR；聚类本身有计算开销，且融合是否损害多语 Whisper 能力正文未深挖。


# OnDA: On-device Channel Pruning for Efficient Personalized Keyword Spotting

- 论文编号：1253
- 报告人：Alessio Burello
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/risso26_interspeech.pdf

## 问题
端侧个性化关键词检测既要适配用户/环境分布偏移，又受内存、时延与能耗约束。已有自学习流水线主要在线更新权重；架构（通道数）通常只做部署前离线剪枝，未必匹配现场分布。

## 方法
**OnDA** 在 [3] 的 ProtoNet 自学习管线（预训练 → 伪标签 → 端侧 triplet 微调）上加入结构化通道剪枝：
- **OnDA-1**：用数据感知 **HAP**（Hessian-trace 加权幅度）在适配初期、基于伪标签数据剪枝，再微调。
- **OnDA-2**：先微调，再用数据无关全局 L1 剪枝，再二次微调。
可与离线剪枝叠加。剪枝对象为卷积输出通道，得到仍稠密的子网络。

## 实验与结果
MSWC 预训练；HeySnips / HeySnapdragon 个性化评测。相对未剪基线，iso 任务表现（Acc@FARh=0.5）下最高约 9.63× 模型体积压缩；Pareto 前沿显示域内数据剪枝优于直接微调更小的离线剪枝网。Jetson Orin Nano：相对仅权重适配，训练/推理时延与能耗最高约 1.52×/1.57× 与 1.64×/1.77× 改善；数据感知剪枝可前置，从而降低后续微调成本。

## 结论
作者认为个性化 KWS 应同时适配权重与架构；用现场伪标签做在线结构化剪枝，可在保持任务表现下显著压缩并加速端侧训练/推理。

## 点评
问题提得准：分布偏移不只改最优权重，也改「够用多深的通道」。把 HAP 前移到适配起点，用少而贴域的伪标签做架构决策，比「先离线剪小再硬微调」更贴部署现实。脆弱点：伪标签噪声会影响 HAP 分数；二次微调增加流水线复杂度；结论主要来自两类唤醒词数据集与 Jetson 测量，换 MCU 级平台收益需另证。


# Sub-Model Short-Term Memory Convolutions for Keyword Spotting Systems on Device

- 论文编号：1343
- 报告人：Szymon Klimaszewski
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/warlewski26_interspeech.pdf

## 问题
端侧 KWS 需在严格算力与内存下做高时间粒度在线推理；滑动窗 CNN 冗余计算多，原 STMC 为帧同步任务保留全部池化状态，对只需稀疏输出的分类任务存在状态冗余。

## 方法
提出 SM-STMC：将卷积骨干按池化/输出切成子模型，经内存缓冲连接；按调度式在时刻 t 只执行必要深度（池化 stride 带来的冗余状态被丢弃）。CNN 离线训练后 STMC/SM-STMC 仅作推理扩展，无额外参数；用独立子模型静态调度以兼容 TensorFlow Lite。输入 Mel 谱（窗 1024、hop 256），VGG 式嵌入 + MLP 分类器，约每 8 帧评一次分类器。

## 实验与结果
Google Speech Commands 11 类。标准 1 s 测试：SM-STMC1 recall/准确率约 93.8%，SM-STMC2 约 91.6%；两端补静音的 2 s 集上离线单窗 VGG 大幅掉点，8× 滑动窗与 SM-STMC1 达约 97.1%。ARM Cortex-M55（int8、TFLite Micro）：相对 8×/s 滑动窗，SM-STMC 总 MCPS 显著更低（如 VGG1 8× 59.36 vs SM-STMC1 11.37）；相对原 STMC 缓冲约减半至更少（如 STMC2 21632→SM-STMC2 7520）。摘要称相对等价频繁 CNN 与 vanilla STMC，MCPS 最高可降约 82% 与 46%。

## 结论
SM-STMC 在保持 CNN 识别性能的同时削减在线卷积冗余状态与算力，无需重训，适合穿戴等资源受限 KWS；分类频率降低会略增延迟，但仍在实时交互可接受范围。

## 点评
抓住 KWS“不必每帧出结果”与 STMC 帧同步设计的错位，用静态子模型调度换部署友好性。效果强依赖池化深度与评测频率；与 LSTM 比算力更省但延迟粒度更粗，边界对齐场景才显出相对离线窗的优势。


# An Efficient vLLM-Based Inference Pipeline for Unified Audio Understanding and Generation

- 论文编号：1244
- 报告人：Haoran Wang
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wang26w_interspeech.pdf

## 问题
高吞吐推理引擎面向单流文本自回归，难原生支持 SpeechLM 的多码本 delay-pattern 交织采样、波形解码，以及 CFG 双路前向带来的吞吐腰斩与调度同步开销。

## 方法
基于 vLLM 连续批处理：主–辅分解，仅一条码本流走引擎标准管线，其余 S−1 流在模型内采样并缓存；请求结束后 delay 解交织，GPU 内嵌声学解码器直接出波形。用每请求相位状态机（text / transition / audio / drain）与动态词表掩码管理文–音混合输出。CFG 采用 Paired Request Co-Scheduling：条件与无条件 companion 同批共享一次 backbone 前向，仅在音频相位合并 logits，采样 token 同步写回 companion。在 Bagpiper、OpusLM、OpusLM-Dialogue 上验证。

## 实验与结果
单卡 H100 80GB、FlashAttention-3。相对顺序 PyTorch：Bagpiper decode 约 52.7→5694.5 tok/s，OpusLM 36.5→4582.9，OpusLM-Dial. 53.9→5870.5；MFU 最高约 9.95%。FP32 下与参考实现 token 序列一致；BF16+FA3 有精度漂移但不伤聚合质量（MMAU-mini、LibriSpeech ASR/TTS、Eval2000 UTMOS 与基线接近）。Bagpiper CFG：decode 约 4952→3960 tok/s，约保持非 CFG 吞吐的 80%。

## 结论
在连续批处理引擎内原生支持多流音频生成与端到端合成，并用成对共调度吸收 CFG 开销；跨多种 SpeechLM 最高约 108× 生成吞吐，修改主要落在模型与 logit 层，便于复用。

## 点评
把 delay-pattern 与 CFG 嵌进现有调度/KV 基础设施，而不是另起一套服务，务实可落地。吞吐数字依赖高并发与 H100；质量表中个别指标（如对话 UTMOS）略降，说明精度与批处理路径仍需任务侧核对。开源分支便于复现。


# Audio-NSP: Data-Centric Semi-Autoregressive Generation for Large Audio-Language Models

- 论文编号：1737
- 报告人：Liang Cao
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/cao26b_interspeech.pdf

## 问题
LALM 音频序列远长于文本，逐 token 自回归延迟高；改 NAR/加 MTP 头或草稿模型有结构或显存开销，且文本低熵与音频高熵导致统一置信阈值会使并行解码退化或伤保真度。

## 方法
Audio-NSP：仅通过数据中心 SFT 激活半自回归块生成——在原序列后追加若干 Anchor-Mask 块（锚点+可学习 mask），位置 ID 对齐逻辑位置；定制注意力（前缀因果、块内双向、块间隔离），损失只算 mask 位。推理为 predict–verify–accept；模态感知动态截断：文本 τ_text=0.8、音频 τ_audio=0.2（Top-1 置信度），按置信度接受变长前缀。骨干 VITA-Audio-Plus-Vanilla，块长 W=4。

## 实验与结果
相对 VITA-Base / VITA-MTP：ASR 平均 WER 劣化约 +1.20（MTP +2.14），TPS 最高约 3.42×（LibriSpeech-clean）；SQA 平均 ACC 劣化约 −1.64（MTP −1.78），约 2.4×；TTS 平均劣化约 +0.29（MTP +0.68），约 1.9×。动态截断 Pareto 优于固定步长；Top-1 / Top-10 sum / Entropy 均可调出可用折中，默认 Top-1>0.2。

## 结论
无结构改动即可把预训练 LALM 变为块级生成，并用模态感知截断缓解文本–音频熵差，相对 MTP 在加速与质量保留上更优（约 1.89×–3.42×）。

## 点评
核心洞见是“同一阈值套在音频上会退化成 AR”，用分模态阈值换速度–保真。仍依赖 SFT 与固定 W；TTS 加速弱于 ASR 是有意保守。未改架构利于落地，但训练序列打包与注意力定制实现成本不低。


# Improving streaming ASR with foundation models using emission policies

- 论文编号：3358
- 报告人：Gerard Mas Mollà
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/masmolla26_interspeech.pdf

## 问题
Parakeet、Canary 等语音基础模型离线 ASR 强，流式切块后质量明显下降；依赖内部特征的发射策略难迁移，需要不打开模型黑盒的流式包装。

## 方法
训练无关、模型无关流水线：滑动窗音频缓冲（块长 L_c、最大窗 L_max）增量喂入；用 token 级时间戳过滤早于 T_last 的重复输出；文本侧发射策略控制提交时机——静态 Wait-K、Hold-N，动态 LocalAgreement（连续两假设最长公共前缀）及基于编辑距离阈值 τ 的 LA-Lev。仅要求模型能产时间戳。

## 实验与结果
Open ASR Leaderboard：VoxPopuli、TedLium-v3、Earnings22；模型 Parakeet-tdt-0.6b-v3、Canary-1b-v2。窗参：L_c=2、L_max=20 较稳。相对 NeMo 流式基线，各策略均降 WER；高延迟下 Parakeet+LA 接近离线（如 Earnings22 11.45% vs 离线 11.19%，延迟约 2.25 s）。L_c=1 低延迟设定下 Parakeet+LA 优于或接近 SimulStreaming Whisper（如 Earnings22 12.07%/1.32 s vs 14.92%/1.01 s），延迟略高约 0.4 s。

## 结论
滑动窗 + 时间戳去重 + 纯文本发射策略，可使带时间戳的 SFM 在实时/近实时下接近离线质量，且无需访问内部张量。

## 点评
把“黑盒+时间戳”做成可插拔流式层，利于换模型。LA 等策略用稳定性换延迟，与 AlignAtt 类模型感知策略比更易移植、延迟略逊。图文中部分抽取噪声不影响主结论；多任务 ST 等扩展作者留作未来工作。


# AdaTS: Adaptive Token Sampling for Efficient Speech Language Models

- 论文编号：2753
- 报告人：Sonal Sannigrahi
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sannigrahi26_interspeech.pdf

## 问题
SLM 将密集语音 token 塞进 LLM 上下文，序列长且冗余高，均匀卷积下采样或固定池化易在压缩与语义保留之间失衡，拖累长音频与推理成本。

## 方法
AdaTS：在预训练语音编码器输出上按成对余弦相似度做 score-and-merge——相似度高于阈值 t 的连续子组加权合并（权重 1−sim，强调更不相似单元）。两阶段训练：先冻编码器与 LLM，只训线性/MLP 模态与长度适配（ASR 对齐）；再解冻 LLM 做 ASR/SQA/ST 指令微调。编码器固定 Wav2Vec2Bert，解码器试 Qwen2.5 1.5B、Llama 3.2 1B、EuroLLM 1.7B；采样模块可只在 IT 或两阶段启用。

## 实验与结果
主结果（Qwen2.5 1.5B+AdaTS）：ASR LS Clean/Other 等显著优于 Pooling、WLQF、FLS；Spoken SQuAD F1 58.9、SLUE 37.5、LongSpeechEval 3.5，FLEURS ST COMET 82.0。t=0.85 时平均压缩约 1.65–1.85×（最高可超 4×）；加权平均合并优于简单平均与 Top-1。最佳为 MA 用全长、IT 再下采样；仅 MA 压缩会严重掉点。10 s 音频推理约 2.14 vs 卷积下采样 3.23 TFLOPS（约 34% 降算力；摘要称推理成本约降 40%）。

## 结论
无参相似度合并可在约 2× 平均压缩下保持甚至提升 ASR/ST/SQA，并降低推理算力；对齐阶段宜保留冗余，压缩宜放在指令微调。

## 点评
用内容自适应粒度替代一刀切下采样，小解码器也能压过依赖更大骨干的 CTC 融合路线。阈值对 ASR/ST 更敏感；压缩率随数据变化，部署需按任务标定 t。FLOPS 数字依赖其计算工具设定。


# Merging the Knowledge of LLMs for Automatic Speech Recognition

- 论文编号：2561
- 报告人：Hayato Futami
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/futami26_interspeech.pdf

## 问题
LLM 基 ASR 域适应常靠浅融合/密度比在解码时调用外部 LM，大模型每步推理成本高；需把目标域文本知识并入参数、推理零额外开销。

## 方法
同一预训练 LLM 上：ASR 用 LoRA，目标/源域 LM 亦用 LoRA。域扩展合并（对应浅融合）：θ = θ_pre + Δasr + λα Δlm,tgt；域迁移合并（对应密度比）：再减 λβ Δlm,src。可用 TIES（按幅度剪枝、选符号、只合同号参数）减轻任务干扰。推理仍单次 ASR 前向，无额外模块。

## 实验与结果
CSJ-SPS→CSJ-APS（LLM-jp-3-980M+Conformer）：基线 eval1 CER 13.9；TIESmerge-T 13.3，参数与 RTF 不变（1.1B / 0.45）；浅融合/密度比更低（12.8/12.5）但参数与 RTF 上升。合并可再与 SF/DR/rescoring 组合进一步降 CER。LibriSpeech→SPGISpeech（LLaMA3.2-1B）：基线 WER 11.2→TIESmerge 10.6；SF/DR 约 9.1/9.0。贪心解码下合并仍有效，CSJ 上甚至可优于 DR。

## 结论
跨模态 LoRA 算术合并能稳定提升目标域 ASR，且不增显存与延迟；绝对增益弱于逐步 LM 融合，但可与之叠加，并便于单模型部署。

## 点评
把浅融合/密度比“搬进权重空间”，切中大 LM 融合的成本痛点。跨模态对齐脆弱——加大 λα 易崩 ASR，故增益有限。无目标域配对数据、只需文本时很实用；源域文本缺失则只能做扩展合并。


# Scaling few-shot spoken word classification with generative meta-continual learning

- 论文编号：408
- 报告人：Batsirayi Mupamhi Ziki
- 程序：Wednesday 30 September 2026 / Efficient Inference for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/beyers26_interspeech.pdf

## 问题
少样本口语词分类多在小类数设定；若要持续扩到约 1000 类且每类仅 5 条，需在精度、遗忘与适应速度上可扩展的元–持续学习方案。

## 方法
用 GeMCL：编码器 + 生成式分类器，每类嵌入用 Normal-Gamma 先验、观测后闭式更新高斯后验（类参数隔离，免疫灾难遗忘）；元训练优化编码器与先验 α0、β0，元测试冻结元参数、对新词只算类统计。实现为 12 层 12 头 Transformer、MFCC 输入（约 85M 参数），在 MSWC 英语约 8915 词上元训（25-way-5-shot，估计约 477 小时有效数据）。基线为 HuBERT base（LibriSpeech 约 960 h 预训练）全量微调，以及冻骨干只训投影+分类头；类数从 25 增至 1000，每阶段 5-shot 支持集后评查询集。

## 实验与结果
全量微调多数阶段准确率最高但不稳（词级波动均值约 24.55）；GeMCL 波动约 0.48，显著更稳。GeMCL 在 <450 类优于 CH，高类数略逊；1000 类时约落后 1000-way 微调 CH 约 2%。适应时间：GeMCL 少样本适应约 0.06 h vs CH 124 / 全微调 186（摘要称适应约快 2000×）；元训远少于 HuBERT 预训练等价算力。

## 结论
从零训练的 GeMCL 在千类 5-shot 持续设定下可达接近实用 HuBERT 分类头基线的精度，真正增量更新、词级表现稳定，适合持续扩词表部署。

## 点评
把“可扩展少样本 KWS”推到 1000 类并报告过程稳定性，问题设定贴近产品。对比混入数据量与算力不对称，结论更像策略选择（相关小数据元学习 vs 大 SSL 微调）而非纯算法胜负。仅英语 MSWC；跨语与其他持续学习算法仍待验证。


# SEA-MDD: Self-adapting Mispronunciation Detection and Diagnosis Models via Test-Time Training

- 论文编号：856
- 报告人：Minglin Wu
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wu26c_interspeech.pdf

## 问题
L2 发音检测与诊断（MDD）面对学习者水平与错误类型多样，固定训练集难覆盖分布外样本；大规模标注昂贵。已有 MAML 适应仍需目标说话人较多标注数据，形成二次数据稀缺。

## 方法
SEA-MDD：在 wav2vec 2.0 Transformer 块的自注意力与 FFN 之间插入 TTT 模块（默认两层 MLP + LN + 残差 + tanh 门控；另有 Linear 变体）。内外环：内环在训练与测试时对每个输入用自监督重构更新 MLP 权重 W（θ_K x 输入、θ_V x 目标，也可时间维 mini-batch b=32）；外环用 CTC 微调其余参数。测试时仅做内环、单句适应。

## 实验与结果
CU-CHLOE（34.6 h，粤/普通话学习者）。相对 wav2vec2-CTC 与需约 2 h 适应数据的 wav2vec2-MAML：SEA-MDD-MLP（全块）PER 8.03%、F1 81.54%、DIAA 94.06 等全面更优。适应成本：1 句、延迟约 5–52 ms、参数约 3.0–35.5M，远低于 MAML（94.4M、约 30 min、2 h 数据）。浅层插入效果更好；MLP 略优于 Linear；全块略优于仅第 1 块。

## 结论
单句级 Test-Time Training 可在无额外标注下自适应当前发音样本，兼顾 MDD 精度与实时效率，为 L2 数据稀缺提供新适应范式。

## 点评
把长上下文 TTT 思路迁到 MDD，用“测试时自监督更新局部 MLP”换掉“再采目标人数据”，对课堂实时反馈很贴切。浅层更有效符合底层声学变异更大的直觉。局限是仅 CU-CHLOE 一种 L1 背景；内环学习率与插入层需调；相对 MAML 的评测设置对其更苛刻（MAML 用测试集一部分适应）。


# Mixture-of-Accent-Adapters for Robust ASR: Injecting Accent Cues into Pretrained Whisper

- 论文编号：1373
- 报告人：Mehedi Hasan Bijoy
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/bijoy26_interspeech.pdf

## 问题
带口音语音仍是包容性 ASR 瓶颈；全量微调预训练模型昂贵。既有适配器/多任务方案缺少口音专用适配器、可控编码器级口音线索注入，以及兼顾特化调节与性别信息泄漏抑制的监督设计。

## 方法
Mixture-of-Accent-Adapters（MoAA）作用于冻结 Whisper：池化状态控制瓶颈估计 accentedness；从可学习 soft accent codebook 加权检索注入口音线索并路由轻量口音专家适配器，再与骨干做门控混合。对抗性别头（GRL）抑制泄漏；reference-free hallucination suppression（DHF）抑制罕见解码伪影。默认口音弱时回退冻结骨干。

## 实验与结果
AESRC 上 Whisper-small：MoAA+DHF 达 WER 7.49%、CER 3.81%，约 0.51M 可训参数（约 1% 骨干）。优于全微调（15.50）、LoRA（15.83）与单适配器+DHF（10.25）；相对单适配器+DHF，WER 相对降约 26.9%。消融去掉线性投影或局部解冻编码器/解码器显著变差；GRL 使性别分类准确从约 98.6% 崩至约 29.8%。

## 结论
口音条件化路由 + codebook 注入在冻结 Whisper 上实现按需特化，配合 DHF 达到强口音鲁棒且参数极省。

## 点评
核心是“估计口音强度再决定是否/如何特化”，比一律加适配器更贴分布。DHF 与 MoAA 互补（前者稳解码、后者改编码器状态）。注意与带外置 LM/多阶段流水线的历史 SOTA 不完全可比；口音标签与 accentedness 估计误差会传导到路由。


# Contrastive Regularization for Accent-Robust ASR

- 论文编号：949
- 报告人：Van-Phat Thai
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/thai26_interspeech.pdf

## 问题
SSL 预训练 + CTC 微调在母语语音上强，但对口音变异敏感。口音特定方法需显式口音监督/结构改动；口音不变方法仍缺轻量、与通用 CTC 微调无缝结合的正则。

## 方法
在 CTC 微调时加 utterance 级 Supervised Contrastive（SupCon）辅助损失：对编码器隐状态均值池化后投影，以同一转写为正相关、不同转写为负相关，促进内容紧致、跨口音更稳的几何结构。训练期用、推理不加参；无架构修改、无口音标签。

## 实验与结果
L2-ARCTIC，未见转写（UT）/未见口音（UA）评测。wav2vec2-Large+4-gram：UT WER 10.47→9.14（相对约 −12.7%），UA 9.98→7.41（相对约 −25.8%）。在 W2V2/WavLM base/large、greedy 与 LM 解码上均一致降 WER；对 wav2vec2 增益通常大于 WavLM。within-transcript 余弦离散度均值 0.0518→0.0430（相对约 −17%），t-SNE 显示转写簇更紧。

## 结论
SupCon 是模型无关的轻量正则，能提升多口音 ASR 并收紧同转写跨说话人表示，尤其利于未见口音泛化。

## 点评
用“同一句不同口音应靠近”把口音不变做成对比几何，比口音分类头更少负迁移风险。增益在 UA 最大，符合不变性叙事。依赖基准中重复转写构正样本；无自然重复时需相似度分组或合成变体，外推仍待验证。


# Exploring the potential and limitations of Model Merging for Multi-Domain Adaptation in ASR

- 论文编号：1969
- 报告人：Carlos Carvalho
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/carvalho26_interspeech.pdf

## 问题
语音基础模型常按域分别微调，产生大量专用 checkpoint；新域到来时再做全量联合微调成本高且数据可能不可用。模型合并可免重训拼能力，但 ASR 多域合并系统评测与 OOD/跨语保持仍不足。

## 方法
在 WhisperLv3-X 上对 10 个欧洲葡萄牙语（EP）域独立微调后，基准 11 种合并算法（参数空间 / τ-space / τ-subspace）。提出 BoostedTSV-M：在 TSV-M 上对小奇异值做 boosting 缓解秩塌缩，并用 Newton–Schulz 正交化提升数值稳定。开源 MergeWhisper。评测 EP ID/OOD、非洲/巴西葡语、OpenASR-HF、FLEURS。

## 实验与结果
Full-FT 把 EP ID 从 15.62 降到 8.54，但伤非 EP OOD。BoostedTSV-M EP Full Avg. 11.55，略优于 Full-FT 的 11.58（MAPSSWE p<0.001），EP OOD 优于 Full-FT；相对 TSV-M 更偏 ID、略损部分非 EP OOD。PS 类（如 Karcher、Model Stock）非 EP/多语更好；τSpa（如 TIES）可伤英语。β 越小 ID 越好、EP OOD 越差，体现特化–共享权衡。

## 结论
合并是多域 ASR 相对 Full-FT 的可行替代：BoostedTSV-M 在 EP 上可匹敌甚至略超全微调，并更好保留部分泛化；但存在目标特化与跨语鲁棒的明确权衡。

## 点评
把 NLP/CV 合并族系统迁到 Whisper 多域，并量化“合并不会免费”的 OOD 代价，工程价值高。BoostedTSV-M 针对秩塌缩的修复点明确。局限是单语种族（EP）扩展为主；合并质量依赖各域微调质量与域相似度。


# Activation Steering for Accent Adaptation in Large Audio Language Models

- 论文编号：2166
- 报告人：Ting Dang
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sun26h_interspeech.pdf

## 问题
口音是 ASR 误差主因之一；主流适应靠微调，却不清楚口音信息编码在哪一层、能否在激活空间直接控制。大音频语言模型全参/启发式 PEFT 成本高且可能纠缠语义。

## 方法
把口音视为隐表示中可解释子空间：用文本匹配的标准–口音对，在各编码器层估 mean-shift 方向，注入后测与口音对齐程度，得到层敏感度剖面。推理时在选定层对隐状态加归一化转向向量 α·d̂（前向 hook，不改权重）。在 VCTK（多母语口音）与 L2-ARCTIC（印地/阿语/西语）上，说话人与转写与抽取集严格隔离。

## 实验与结果
敏感度：早期层弱、中层（约 15–19）可控、过晚层不稳；层 31 注入常大幅升 WER。中层转向：母语口音平衡子集上 ΔWER 最高约 30%，非母语约 5%；α 增大峰值更高但深层更易塌缩。相对 PEFT：小样本时转向有竞争力，大数据微调仍更强（正文比较）。八口音一致降 WER。

## 结论
口音信息集中在中层编码器；无参激活转向可在推理期降低多口音 WER，为可解释、可扩展的口音适应提供路径。

## 点评
把 LLM steering 迁到语音编码器，并用层扫 + α 扫给出可操作窗口，解释性与实用性兼具。依赖配对同文标准–口音语料估方向；非母语增益较小、强 α 易塌，部署需按口音校准层与强度。


# AccentDrift: Real-time Streaming Accent Conversion via Sparse Speech Tokenization

- 论文编号：710
- 报告人：Sang-Hoon Lee
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26g_interspeech.pdf

## 问题
实时流式口音转换（AC）对 L2 交互很重要，但现有系统多依赖平行语料、非流式架构、生成质量或口音/音色控制不足。

## 方法
AccentDrift：信息瓶颈视角下用稀疏语义量化（FSQ/iFSQ）从连续语音抽语言信息；口音适配器向稀疏语义 token 注入口音风格，音色适配器（因果 DiT + CAM++，HiFTNet 声码）分层生成说话人声学。全因果：cache-aware FastConformer、有限上下文 Transformer、因果 DiT/声码；并行流，标称约 520 ms（最小约 0.5 s）延迟。无需口音标签与口音配对数据，做零样本 AC（可选零样本音色转换）。

## 实验与结果
LibriTTS/VCTK/GLOBE 训练；L2-ARCTIC 主观、VCTK 印度口音客观。相对 Vevo-Style：流式下 WER 6.27 vs 13.8，SPK-SIM 0.72，口音相似度更高；NMOS/AMOS 可比。密集语义（CosyVoice3）难转口音。消融：NeMo-ASR 中层表征、更窄 IB、lookahead、chunk 大小影响延迟–质量权衡；GRL 抑口音泄漏。

## 结论
稀疏语义 tokenization + 分层风格适配可实现低延迟流式 AC，在保内容与音色下接近或优于非流式并行 AC 基线。

## 点评
把 AC 做成“先压成稀疏语言 token 再分层注口音/音色”，并真正落地因果流式栈，是相对并行 AC 的关键差异。不依赖口音标注利于扩展。仍需继续压解码延迟才更贴全双工；客观评测口音类相对有限，极端口音泄漏与长上下文仍是风险。


# Mitigating Speaker Leakage in Cascaded Multi-talker ASR with Diarization-based Transcript Correction

- 论文编号：3191
- 报告人：Suresh Singh
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nkouanga26_interspeech.pdf

## 问题
级联多说话人 ASR（分离→单说话人 ASR）受分离说话人泄漏限制；已有纠正多偏词汇重标注，对泄漏伪影的稳健剪除不足。

## 方法
后处理剪枝范式：用预训练说话人日志模型作多模态校验，对已转写片段在满足三方共识时剪除——时间包含（Cac）、词汇交叉验证（Clex）、时间对齐（Ctemp）。不改分离/ASR 骨干，可插在 Sepformer/Mossformer + Universal-2 等级联后面。

## 实验与结果
Libri2Mix、LibriSpeechMix、AMI（SDM/IHM）上相对基线一致降 WER；AMI 上相对改进约 5.8%–10.55%。高泄漏子集（分离源转写相似>0.4）相对 cpWER/WER 降幅最高约 29%（Mossformer AMI IHM 65.58→46.39）。消融：仅文本易过删；声学条件贡献大，三方合用最佳。相对联合 Mossformer-Diar 更跨域稳健。

## 结论
基于日志的三方共识剪枝能有效抑制级联 MT-ASR 中的说话人泄漏，尤其在高泄漏与真实会议场景。

## 点评
把泄漏当“可检测伪影”而非只重标说话人，后处理可复用强基础模型，工程上务实。依赖日志与对齐质量；仅文本条件有害说明多模态约束必要。未改分离前端，上限仍受分离 residual 限制。


# Beyond Mimicry: Constrained Exploration with GRPO for Joint Multi-Talker ASR and Diarization under Unknown Speaker Counts

- 论文编号：2297
- 报告人：Yunrui Cai
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/cai26c_interspeech.pdf

## 问题
联合多说话人 ASR（含归因与时间戳）在说话人数未知、输出结构严格时很难；仅 SFT 对齐 Speech-LLM 在高重叠下易突发幻觉与畸形 speaker/timestamp 标签。

## 方法
两阶段生成框架：(1) CoT 增强 SFT：先推断全局说话人数再转写；(2) GRPO 约束探索，用 Multi-dimensional Constraint-Aware Reward（MCAR）直接优化置换不变准确度，并强制计数、时间与结构约束（含 burst 惩罚等）。骨干 Qwen2.5-Omni-7B + LoRA；在高重叠 1 万样本上做 GRPO。

## 实验与结果
Libri2/3Mix 与 Dynamic-Mix(2+3)：SFT+CoT+GRPO 在 3 说话人 cpWER 14.52%、WDER 1.95%；Dynamic-Mix cpWER 9.24%、WDER 1.12%、CoT-Acc 99.72%。相对 SFT+CoT，GRPO 带来约 35%/54% 相对 cpWER 降幅。零样本基线说话人计数仅约 32%。

## 结论
先计数的 CoT + 多维约束 GRPO 使 Speech-LLM 在未知人数、高重叠下联合转写与日志显著更稳，超越仅模仿式 SFT。

## 点评
把“人数未知”显式建成推理前缀，再用 RL 罚结构崩坏，对准生成式多说话人输出的主要失败模式。评测偏合成混合；真实会议噪声/重叠分布外推未充分展开。奖励设计复杂，权重敏感。


# KFC-KWS: Keyframe Fusion with CTC for User-Defined Keyword Spotting

- 论文编号：1586
- 报告人：Wenbin Jiang
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/li26y_interspeech.pdf

## 问题
用户自定义关键词检测需区分目标词与音近干扰词；全序列匹配易被整体相似淹没局部可辨音素差异。

## 方法
KFC-KWS：利用 CTC 尖峰后验选高置信音素关键帧，对齐音频、音素与文本模态；再经交叉注意力与全句表示融合，兼顾局部判别与全局语境。冻结 XLS-R 音频编码 + G2P 音素 + DistilBERT 文本；可训约 2.0M 参数；模态 dropout。

## 实验与结果
LibriPhrase：无增强时平衡 AUC 98.06%（LPH 96.54%，EER 9.13%），优于 HyperSpotter-c 等且参数更少。带模态 dropout：平衡 AUC 98.73%，LPH AUC 97.65%、EER 7.75%，强于增强版 PLCL 等。易集上 EER 略逊部分全序列模型，偏重难集可辨性。

## 结论
CTC 引导关键帧融合能有效提升音近关键词判别，在 LibriPhrase 难集与平衡指标上达到强结果且参数紧凑。

## 点评
抓住“混淆发生在少数音素位置”，用 CTC 峰定位再融合，比纯全局嵌入更对症。参数效率好。易集略牺牲、依赖 CTC 对齐质量；开放域口语噪声下峰检测是否稳仍待验。


# Avoiding Catastrophic Forgetting in Text-Only Adaptation of LLM-based ASR via Multi-View Text Denoising

- 论文编号：3422
- 报告人：Sergio Burdisso
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/burdisso26_interspeech.pdf

## 问题
仅用目标域文本微调 LLM-ASR 的 LLM 会破坏 projector 学到的语音–文本对齐，引发灾难性遗忘。文本比配对音频更易得，需要不改结构、不增参的纯文本适应。

## 方法
把适应建成去噪任务，并用 multi-view noise-driven batching：每个 mini-batch 混合 (1) 源域配对音频–文本、(2) projector 诱导的噪声转写、(3) 合成破坏的源转写、(4) 破坏的目标转写。合成噪声含随机字符替换与重复，模拟 projector 噪声模式。冻结编码器与 LLM 骨干训 projector 得基座后，用该混合做文本适应；无架构改动。

## 实验与结果
SLAM-ASR（WavLM-Large + Llama 3.2 系）上 DefinedAI / SlideSpeech。域内/域外/跨域三档：相对 Fang et al.、Ma et al. 文本适应更优；跨域相对基座相对 WER 改进最高约 25.4%（An），仍低于有音频适应上界。SlideSpeech 域外相对改进约 4.2%–7.0%。

## 结论
多视角噪声混合可在纯文本适应时保持语音–文本对齐，显著优于近期文本适应法，且不增参数。

## 点评
关键洞察是“别让 LLM 只见干净目标文本”，用源音频与噪声视图当锚防遗忘。工程上轻、可插。上界仍逊真音频适应；噪声配方需调，跨声学域差距仍大。


# AQA-TTRL: Self-Adaptation in Audio Question Answering with Test-Time Reinforcement Learning

- 论文编号：288
- 报告人：Haoyu Zhang
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26c_interspeech.pdf

## 问题
LALM 部署后静态，难适应真实测试分布；有监督更新需标注。需在无标签测试数据上自进化做 Audio Question Answering。

## 方法
AQA-TTRL：对测试题多数投票（如 64 次）得伪标签，再以 GRPO 做测试时强化学习。置信度加权优势缓解伪标签噪声；multiple-attempt sampling 抑制 advantage collapse。全参微调（AdamW），小数据集约 100 步、大数据集约 500 步。对比 DI、DIMV、同伪标签 SFT。

## 实验与结果
MMAU / MMAR / MMSU：Qwen2.5-Omni 7B 平均 +4.42%（64.39→68.81），3B +11.04%（53.82→64.86）；适配后 3B 平均超过未适配 7B 的 DI。优于 DIMV 与伪标签 SFT。消融显示置信度加权与多次尝试互补。按音频类型适配时 music-only 平均最高。

## 结论
无标签测试时 RL 自适应可使 LALM 在 AQA 上显著自提升，小模型经适应可逼近更大模型直推。

## 点评
把数学域 TTRL 迁到音频，用多数票伪奖励 + 抗噪机制形成闭环。RL 比同标签 SFT 更能“忍错标签”。成本是测试时大量前向与更新；伪标签系统性偏差仍可能固化。


# AFG-Bias: Acoustic-Fusion-Gated Biasing for Plug-and-Play Hotword Customization in LLM-Based ASR

- 论文编号：2029
- 报告人：Long Wu
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wu26i_interspeech.pdf

## 问题
LLM-ASR 难识别稀有领域实体；浅层融合不适生成式解码，深度上下文化多为传统 E2E，提示注入易规模崩塌与幻觉。需不改 LLM 参数的可插拔热词偏置。

## 方法
AFG-Bias：Cross-Modal Acoustic Retrieval（CAR）用滑窗跨模态相似度从大规模候选中取相关热词；Acoustic-Fusion Gating 把经验证偏置注入解码并抑制无声学依据的幻觉。训练时冻结骨干 LLM；HotwordModule（内维 256、单层单向 LSTM）等轻量模块可训。推理 K=5、τ=3、偏置权重约 0.4。

## 实验与结果
AISHELL-1/KeSpeech 训，SeACo 与金融/医疗集评。三骨干 FireRedASR/OSUM/Kimi：相对直推，金融/医疗 CER 相对降最高约 74.1%（OSUM 10.93→2.83）；AISHELL 热词 F1 最高约 +5.4。无门控 CER 飙至约 20%；候选扩到上千仍较稳。纯提示注入常崩至 >30% CER。

## 结论
声学检索 + 门控融合可在冻结 LLM-ASR 上实现可扩展、低幻觉热词定制，显著优于提示注入。

## 点评
把“先声学证据再偏置”做对，直接打消提示列表淹没注意力的失败模式。可插拔性强。依赖 CAR 召回质量；极短/同音热词与跨语实体仍可能漏检或误门控。


# Decoding the Trade-off: A Large-Scale Analysis of Latency and Stability in LLM-based Speech Translation Cascades

- 论文编号：1821
- 报告人：Shinyoung Sun
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sun26f_interspeech.pdf

## 问题
实时字幕需低延迟与稳定译文。段级云端级联中，激进端点检测抬高请求率，可超出服务容量形成 backlog avalanche——排队延迟主导，使“更快”设置在稳态下更慢。系统评测常只报单一端到端延迟，混淆首字延迟与稳定字幕延迟。

## 方法
提出 RST：可复现 KO→EN 字幕流水线，区分 time-to-first-text（latency first）与 time-to-stable-text（latency stable）。在完整 FLEURS KO→EN（2851 clips）上回放评测；2×2 级联（whisper-1 / gpt-4o-transcribe × gpt-4.1-mini / grok-4-fast）；对比 fast vs stable 端点预设并扫 hangover/min 时长；定义运营阈值为 median RTF≤1 的最激进设置。另做 Whisper 提示消融。

## 实验与结果
fast 预设 median RTF≫1（如约 24–52），latency stable 可数十秒并随时间累积；stable 预设 RTF 可 ≤1，首字/稳定延迟约 1–3 s 量级且质量更高（BLEU/chrF）。Whisper 滚动/静态提示在短块流式下 CER +14–17 pp，并可泄漏指令。吞吐稳定是低延迟 LLM 级联的必要条件。

## 结论
端点粒度–吞吐稳定–上下文完整构成三难；应优先保证 median RTF≤1 的稳定区，再追求激进延迟。提示条件在短块流式 ASR 上可能有害。

## 点评
把“快设置变慢”量化成 backlog 机制，并拆分 first/stable 延迟，对工程运维直接可用。评测绑定特定云 API 与 KO→EN，外推需重标定阈值。


# Fed-SpeechLLM: Federated Learning Speech Language Models for Multilingual ASR

- 论文编号：689
- 报告人：Daniele Giuseppe Falavigna
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ali26_interspeech.pdf

## 问题
SpeechLLM 适于多语 ASR，但集中训练与隐私约束冲突；联邦学习面临声学与跨语双重 non-IID。语言偏斜客户端会使标准 FL 退化。

## 方法
Fed-SpeechLLM：在双语英/意设置评测联邦 SpeechLLM。选择性聚合语音编码器与投影层，LLM 骨干冻结（LoRA 可适配）。提出语言感知梯度聚合与基于采样聚类的客户端选择，缓解多语不平衡。Flower + FedAvg，每轮约 30% 客户端、本地 10 epoch、共 100 轮。数据：LibriSpeech-100 与 MLS 意大利语。

## 实验与结果
单语 FL 接近中心化（LS 约 6–7% vs 中心约 6%；MLS 约 22% vs 约 20%）。双语全客户端：LS/MLS 约 16.8/19.7，相对中心仍有差距。客户端平衡、服务端微调与早/晚语言偏置显著影响收敛；早期英语偏置可将 LS 联邦–中心差距缩至约 5 点。Whisper 作编码器的消融验证编码器选择影响。

## 结论
在复合非 IID 下，语言感知聚合与客户端采样策略可使联邦 SpeechLLM 收敛并接近中心化性能，为隐私约束多语 ASR 提供可行路径。

## 点评
首次系统分析 SpeechLLM 联邦适配，抓住“语言偏斜”这一新轴。仍偏双语音读语料；真实设备异构与通信预算未充分展开。


# Multi-Channel Differential ASR for Robust Wearer Speech Recognition on Smart Glasses

- 论文编号：127
- 报告人：Yiteng Huang
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yang26_interspeech.pdf

## 问题
智能眼镜佩戴者语音识别（WSR）在开放场易受旁人 side-talk 干扰；仅靠波束成形难完全抑制，且增强/分离/抽取前端常引入不可接受延迟或隐私敏感说话人建模。

## 方法
多通道 differential ASR：并行融合互补前端——朝向嘴部的 MVDR 波束成形、最低延迟的麦克风选择（高 SNR 通道）、轻量流式 side-talk detection（区分佩戴者/旁人、不建模身份）。不同帧率前端嵌入对齐后送入低延迟流式 RNN-T。在 Ray-Ban Meta 实测 RIR 模拟与 HATS 实采数据上评测。

## 实验与结果
模拟与真实 LibriSpeech 多通道集：相对仅波束成形基线，组合系统一致更优；真实噪声侧谈上相对 WERR 最高约 18.0%（平均约 14.4%）。实采覆盖 72 个旁人位置（角度/高度/距离）；50% 重叠时角度依赖性更明显。干净条件亦保持竞争力。

## 结论
多前端差分输入能量著提升眼镜 WSR 对 side-talk 的鲁棒性，且兼顾流式延迟与隐私约束。

## 点评
问题定义贴产品：延迟与隐私排除重前端，改用轻量互补线索喂 ASR。实采角度网格使评测可信。仍偏 LibriSpeech 读音；极强旁人主导或多人侧谈场景未充分覆盖。


# ESPnet3: Infrastructure for Scalable Speech and Audio Research in the Foundation Model Era

- 论文编号：2698
- 报告人：Masao Someki
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/someki26_interspeech.pdf

## 问题
基础模型时代语料达百万小时、模型达十亿参，实验工作流复杂；既有工具链在多数据集组合、大规模迭代、多节点训练与 PEFT 集成上工程开销大。

## 方法
ESPnet3：模块化架构 + 配置驱动数据集组合 + 统一 Python 工作流。引入 DataOrganizer 灵活拼数据，dataset sharding 控制内存；允许轻量 stage override 写配方逻辑。默认 BaseSystem 即可跑大规模预训练，并支持接入非原生 ESPnet 模型（如 Whisper）与 HuggingFace PEFT。

## 实验与结果
OWSM-V4 base（约 320k 小时）预训练：相对 ESPnet2，每 epoch 从 95.3→74.2 分钟（约 −21.1 分钟），多节点 GPU 利用率 >80%；RAM 与数据刷新开销大幅下降（约 35.9GB→73.1MB，刷新 311.5s→13.1s）。增强经 DataOrganizer 接入后 CHiME-4 WER 略降。WhisperLv3 在 FalAR 微调可用约 46 行接入新 HF 数据集（ESPnet2 手工约 374 行）；全参/LoRA 均可。

## 结论
ESPnet3 以更低工程成本支撑大规模语音基础模型训练与定制微调，并将公开释放与 checkpoint/日志。

## 点评
贡献在基础设施而非新识别算法：把“能跑大、好扩展”做成可测指标（epoch 时间、利用率、代码行数）。对社区复现大模型实验价值高；具体任务 SOTA 非本文重点。


# SCRIBE: Diagnostic Evaluation and Rich Transcription Models for Indic ASR

- 论文编号：3436
- 报告人：Kavya Manohar
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/manohar26_interspeech.pdf

## 问题
ASR 作为听写工具时，纠错成本取决于错误类型而非计数；WER 把词法/标点/数字/实体混成标量，并对黏着语 sandhi 合法合并施加结构性惩罚（可相对抬高约 30%）。印地语系富文本转写缺乏可操作诊断。

## 方法
SCRIBE：输出诊断向量 [ERlex, ERpunc, ERnum, ERent]，经 sandhi 容忍对齐与领域词表注入；聚合为 SCRIBE-WER。配套 LLM（Gemini）策展管线把 verbatim 转富文本，并发布 FLEURS-RO、IN22-Legal 基准与 Hindi/Malayalam/Kannada 开源富转写模型（Whisper 三阶段微调）。

## 实验与结果
相对 IndicWhisper/IndicConformer，SCRIBE-ASR 在 FLEURS-RO 与法律 OOD 上 WER/WERS 更低；数字错误近饱和（ERnum 常 <1%）。马来alam 法律集 WER 44.52% 而 ERlex 仅 15.96%，显示约 30% 相对膨胀来自形态对齐。人工评分：SCRIBE 分项与专家 Spearman |ρ| 约 0.36–0.92，WER 在多维（尤其马来alam）不显著。标点仍是主瓶颈。

## 结论
分类诊断 + sandhi 对齐使评测对齐专家纠错成本；富转写模型与开源工具为印地 ASR 提供可行动反馈回路。

## 点评
把“听写可用性”从 WER 单标量拆开，对黏着语尤其关键。人评验证强。策展依赖 LLM，残留幻觉需人工把关；标点仍难，说明诊断清楚后下一步应攻韵律/边界。


# Audio-KWS-Gated Error Memory Retrieval for Incremental ASR Post-Correction

- 论文编号：363
- 报告人：Taira Ashikawa
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ashikawa26_interspeech.pdf

## 问题
端到端 ASR 对稀有词与领域专有名词仍易错；LLM 二遍纠错可复用历史纠错记录，但全历史进 prompt 会撞上下文窗口，且仅靠噪声 ASR 假设做文本检索时，触发词被误识就会漏检相关记录。

## 方法
提出增量式 LLM ASR 后纠错框架：人类参考可用时，用 LLM 做错误分析，抽取 hypothesis–reference 短语对写入 error memory，并更新关键词库存与倒排索引（英语索引正误两侧；日语用 LLM 估计的读音作检索键）。对新音频段，用开词汇 Audio-KWS（AdaKWS，Whisper-medium 编码器冻结）在库存上打分，经阈值与 Top-N 得到关键词集合，再检索并按时效截断至最多 M=200 条记录，交给 LLM 做记录约束的保守编辑。

## 实验与结果
在 Earnings-21（英语，公开 ASR 假设）与 CSJ（日语，Whisper-large-v3）含至少一词的 20 个 bias-word 子集上评测。相对无 KWS 的近期历史基线，Top-20 英语约减 prompt 70.9%/65.1%（micro/macro），WER 28.92 vs 29.06，Bias-F1 0.856 vs 0.836；Top-10 日语约减 71.7%/66.7%，CER 14.62 vs 14.86，Bias-F1 0.673 vs 0.648。Top-30 精度最好但压缩更少；仅索引参考侧在日语上损害 Bias-F1。纠错 LLM 为 gpt-oss-20b。

## 结论
Audio-KWS 门控检索可在约 70% prompt 压缩下保持或提升 WER/CER 与 Bias-F1；未来需处理 KWS 漏检并加速分析/纠错推理。

## 点评
核心抓的是「纠错记忆膨胀」与「文本检索依赖错误假设」的耦合问题：用音频侧关键词门控历史，比单纯截断近期记录更贴合当前内容。日语读音键与表面编辑分离的设计合理，但系统依赖人类参考才能扩库存，且强过滤（Top-1）会明显伤 Bias-F1，SLA 上需在压缩与召回间折中。


# Rubric-Aligned Disentangled Evaluation of Human Simultaneous Interpreting

- 论文编号：1105
- 报告人：Ziyu Zhang
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26o_interspeech.pdf

## 问题
人工同传（SI）专业评测用分析性量规分开意义传递、表达与时延，但缺少面向量规、句段级的自动指标。MT 标量指标与 LLM 提示评分易把多维坍成单一质量信号。

## 方法
构建 1,101 段专业双评注 SI 语料（LQ/EXP/LAT，0–3；talk 级划分，En↔Zh）。焦点为文本侧 LQ 与 EXP。在 COMET-KIWI 上用 LoRA + 双独立回归头，残差预测与 MSE+方差正则；对比冻结 COMET-KIWI、单头标量微调、结构化 LLM 零/少样本提示等。LAT 留待多模态。

## 实验与结果
人评者间绝对一致偏低（LQ/EXP Pearson 约 0.21/0.27），一致性 ICC(3,1) 约 0.34/0.43。Dev 上 LLM 提示与人相关近零，且 LQ–EXP 耦合 corr≈0.90（人约 0.56）；标量微调亦近零。Test：双头模型 Pearson LQ 0.388、EXP 0.301，显著优于冻结 COMET-KIWI（0.219/0.175）；预测维间相关 0.529，接近人类耦合。错误多在多步骤程序性内容的步骤完整性。

## 结论
监督结构（而非仅骨干容量）是瓶颈：提示与标量监督坍缩量规维度，双头结构化监督可恢复相对人类一致性范围内的稳定排序信号，服务形成性反馈而非替代认证。

## 点评
把问题从“换更大 LLM”转到“量规监督是否可分”，并用相同骨干隔离监督结构，实验设计干净。绝对相关不高但对照人–人天花板后解读合理。文本-only 对 EXP 是下界；LAT 与客观时延几乎无关，说明“感知同步”本就不是简单 onset 差，多模态是自然下一步。数据集规模与中英双向限制外推，但对 SI 自动评测方向很清晰。


# ARTIST: Universal Articulatory Space Modeling for Multilingual Indic-to-English Speech-to-Speech Translation

- 论文编号：2384
- 报告人：Khushal Yadav
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yadav26_interspeech.pdf

## 问题
端到端 S2ST 大模型（如 SeamlessM4T）参数与双语数据需求大，Indic 低资源方向易过拟合与长序列幻觉。需要更强结构先验以跨语言共享、在极少数据下稳定翻译。

## 方法
ARTIST（166M）：先用 VQAE 在源/目标发音特征上预训练共享离散发音空间（码本 K=20）；S2A 用 Conformer 编码器 + 中间层 CTC 对齐源发音单元，Convolution-Augmented Differential Transformer 自回归预测目标发音 token；VQAE 解码后经 A2Mel + HiFi-GAN 合成。在 BhashaAnuvad 11 个 Indic→英方向上训练（短句 3–20s），长句 OOD（20–50s）评测。

## 实验与结果
相对 1.2B SM4T，各资源档 BLEU/chrF/COMET 普遍更高（如 Hindi 22.14 vs 13.21 BLEU；Gujarati 仅 10h 达 16.91 BLEU）。消融：去中间 CTC 则 BLEU 崩至 1.07；印地单语相对多语从 22.14 降至 12.95；去掉解码器卷积模块亦降分。JES（BLEU/(小时×十亿参））相对基线提升约 23×–231×。

## 结论
通用发音瓶颈促进跨语言脚手架，参数与数据效率高，并改善长音频稳健性。中间 CTC 与局部卷积对稳定训练与发音连续性至关重要。

## 点评
把“生理发音空间”做成极端压缩的共享目标，比纯声学离散单元更适合 Indic 多语少数据；中间 CTC 消融的灾难性结果说明早期语音内容解耦几乎是硬前提。对比锚定在 SM4T 且评测偏长句，对 cascade/专精 S2ST 的相对位置需读者自行外推；发音特征依赖 IMS Toucan 等前置估计，错误可能沿链路放大。


# Evaluating and Preserving Lexical Stress in English-to-Chinese Speech-to-Speech Translation

- 论文编号：2321
- 报告人：Yuchen Song
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/song26f_interspeech.pdf

## 问题
S2ST 语义与自然度已较强，但跨语言词汇重音/强调传递仍弱；汉语为声调语言，英语中心强调检测难直接迁移，且缺带重音标注的中文数据与可靠自动评测。

## 方法
自建中文重音语料（2 名普通话说话人，418 句、1883 条、2.74h）。Syl-BiLSTM：XLS-R 多层融合 + 音节级池化 + BiLSTM 做字级重音检测。CETS：EmphaClass 检英侧重音，Whisper+fa-zh 对齐中文，Syl-BiLSTM 检目标重音，SimAlign 对齐后判是否传到对应语义位置。S2ST：StressTransfer（Whisper+Qwen2.5-3B LoRA）出带 stress 标签译文，CosyVoice3 LoRA 在重音数据上微调可控合成。

## 实验与结果
Syl-BiLSTM F1 0.91，远超 Frame-Linear/Frame-BiLSTM。Proposed CETS-W/S 60.80%/58.30%，基线约 16–26%；BLEU 47.35 与 StressTransfer+Base 接近，UTMOS 最高 3.68。主观成功转移率 78.33% vs 基线约 12–25%；CETS 与人判 Pearson r=0.52，绝对一致约 79%。

## 结论
中文重音数据 + 音节级检测 + 可控 TTS 可显著提升英→中强调传递，同时保持翻译质量与自然度；CETS 可作为自动代理。未来扩展更多说话人与声调语言。

## 点评
把“评测瓶颈”和“合成可控”一起打通，CETS 的词级/句级双粒度比单纯听感更可诊断。说话人仅 2 人、TTS 用固定默认音色，强调可控性可能部分依赖说话人特异性；CETS 链路依赖 ASR/对齐/检测多模块，错误会耦合进指标，与人相关中等需谨慎解读。


# Listening or Reading? Evaluating Speech Awareness in Chain-of-Thought Speech-to-Text Translation

- 论文编号：800
- 报告人：Federico Costa
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/romerodiaz26_interspeech.pdf

## 问题
CoT/多轮 S2TT 假设翻译阶段同时可见语音与转写，从而抗 ASR 误差传播并利用韵律；该假设是否成立缺少系统验证。

## 方法
基于 SALAMANDRATA-7B + 冻结 mHuBERT 离散单元；对比 CoT 与 self-cascade。训练变体：BASE（纯 CoT）、DUAL（25% CoT + 75% Direct）、NOISY（25% CoT 样本注入损坏转写且不对转写算损失）。用 Value Zeroing 做模态归因；控制替换转写片段测鲁棒性；CONTRAPROST 测韵律敏感；FLEURS 测通用翻译质量。英→六种欧洲语言。

## 实验与结果
BASE 的语音贡献近零，行为接近 cascade；DUAL/NOISY 语音归因升至约 1.54×/2.24×。转写噪声下 BASE 的 CoT 与 cascade 掉速几乎相同；NOISY 在高至 30% 损坏下下降明显更缓。CONTRAPROST Global：NOISY-COT 最高（AVG 17.65）。FLEURS 上干预不伤质量，DUAL 整体最好，NOISY-COT 可反超 cascade。

## 结论
默认 CoT  largely 在“读转写”而非“听语音”；混合 Direct 与注入噪声转写可提高语音依赖、抗错与韵律利用。未来可组合 DUAL+NOISY。

## 点评
用归因、噪声鲁棒、韵律三维拆穿 CoT 叙事，比只报 BLEU/xCOMET 更有解释力。NOISY 仍主要依赖转写却能纠错，说明“语音作纠错信号”而非替代文本。局限：仅英→欧语、DSU 表示可能已损韵律细节；CONTRAPROST 绝对分仍低，语音整合仍有很大空间。


# A Multimodal Semi-Supervised Framework for Automatic Construction of a Cross-Lingual Taigi Speech-Chinese Subtitle Corpus

- 论文编号：2096
- 报告人：Yuan-Fu Liao
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cho26b_interspeech.pdf

## 问题
台语（Taigi）标注稀缺；大量在线视频是台语语音 + 画面硬编码繁中字幕、无独立字幕文件，常规 ASR/OCR 难以自动建库。

## 方法
多模态半监督：预处理用 PaddleOCR 抽字幕并按时码切成（文本、帧、语音）三元组；trimodal AVLM（SigLIP + Whisper Large-V2 台语微调 + Qwen2.5，早期融合，LoRA）与 OCR 各出候选；CER 过滤共识对后，用 Qwen2.5-VL 按错误模式提示并参照原图融合伪标签，迭代微调 AVLM；强制对齐精修边界。下游用所得语料微调 Whisper 与 Qwen2.5-14B 翻译。

## 实验与结果
PTS-Taigi 监督：AVLM CER 7.46%，优于 VLM 10.26%、ALM 35.29%，对模糊/噪声更稳。Golden Set 迭代：AVLM CER 36.8%→9.3%（融合约 9.4%），提取量升至池中约 87%（434h）。再扩得约 860h 语料：Whisper 台语→中文 CER 57.8%→37.8%；约 590k 平行句微调后 BLEU 0.2016→0.4033。

## 结论
音视频语言融合 + VLM 共识伪标签可规模化构建跨语言台语–中文字幕语料，并显著提升下游转写与翻译；方法可迁移其他低资源场景。

## 点评
针对“语音语言≠字幕语言”的硬编码设定，用音频作视觉识别约束、用 VLM 化解 OCR/幻觉，工程闭环完整。Golden Set 域外起分很差、迭代后逼近监督，说明半监督主要在修域移。伪标签仍依赖 OCR–AVLM 共识阈值，极端视觉损坏时召回会掉；台语 ASR 再对齐中文建 MT 语料会引入二次误差。


# AfriVox-v2: A Domain-Verticalized Benchmark for In-the-Wild African Speech Recognition

- 论文编号：3140
- 报告人：Busayo Awobade
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/awobade26_interspeech.pdf

## 问题
非洲语言/口音在 ASR 基准上覆盖不足；既有评测偏朗读、域粗、模型过时，难反映噪声自发场景与垂直行业词汇（金融、医疗、农业等）及数字/命名实体风险。

## 方法
AfriVox-v2：聚合 Waxal、Africa Next Voices、新建 Intron-YT（公开多媒体自发对话，母语者转写+元审）等，约 14+ 语种；Gemini-3 多标签域标注（10 域含 Numbers/Named Entities），人工抽检（高精度语约 precision 42%/recall 70%）。评测 Omni-CTC 300M/1B/7B、Gemini 3 Flash、Sahara-v2；报告 WER、域条件 WER、EWER/NWER。

## 实验与结果
自发语音整体更难，但跨语种/模型变化不均。AfriVox-v2 平均 WER：Sahara-v2 最低 20.49，优于 Omni-CTC-7B 27.85 与 Gemini 3 Flash 26.59。域上电信/体育等错误更高；Sahara-v2 各域最低（如农业 16.11）。数字与实体仍难（最好约 NWER 20.32、EWER 23.11）。作者指出部分语种 v2 反优于 v1，可能反映训练数据重叠而非真泛化。

## 结论
域垂直与 in-the-wild 评测暴露平均 WER 掩盖的部署风险；区域优化模型可胜过更大通用模型。基准拟推动更包容的非洲语音 AI。

## 点评
把“野生对话 + 行业域 + 实体/数字”做成评测轴，比只比朗读 WER 更贴近落地。域标签噪声（precision 约 42%）使域结论宜作趋势；作者机构自研 Sahara-v2 虽称同条件评测，读者仍需关注利益冲突与数据重叠可能抬高分。覆盖仍只是非洲语言的一小部分。


# From Dispersion to Attraction: Spectral Dynamics of Hallucination Across Whisper Model Scales

- 论文编号：1420
- 报告人：Ivan Viakhirev
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/viakhirev26_interspeech.pdf

## 问题
Whisper 等大 ASR 在静音/噪声/对抗下会产生与声学脱节的幻觉；WER 与 token 概率难预警。需从内部表征几何解释尺度依赖的失效机制。

## 方法
提出 Spectral Sensitivity Theorem：层增益 ρ、对齐 κ、谱间隙 ξ 决定语境 Jacobian 进入 Regime I（ρ<1，早期声学注入指数衰减）或 Regime II（对齐+增益导致 rank-1 吸引子）。用 SPI 观测量：有效秩 Neff、谱衰减 α、Kirchhoff 指数 Kf。在 LibriSpeech 构造 Hell 对抗集（3.5× 时伸、6 说话人混、0dB 噪声；仅 WER>0.5），分析 Tiny/Small/Large-v3-Turbo 的 Cross/Self-Attn 与 FFN。

## 实验与结果
Small Cross-Attn 谱尾 Neff 降 13.40%（Regime I）；Large Self-Attn Neff 降 2.34% 且谱硬化（Regime II）。相位图上 Tiny/Small 高秩低 α，Large 低秩高 α。作者强调 Regime II 描述的是自信而非正确，仍需外部标签区分真假。

## 结论
幻觉随尺度从「信号弥散」转向「吸引子锁定」；大模型幻觉更像过度结构化的内部先验投影。未来拟扩展到 Canary/OWSM 并用谱正则做检测/抑制。

## 点评
把幻觉从「文本症状」拉回谱几何，对「越大越稳」直觉是有力修正。κ 未直接测、仅从硬化/压缩反推，理论–实验链条仍有跳跃；但尺度分叉现象本身很清晰。


# Error Diversity and Performance Variability in Zero-Shot Children's Speech Recognition

- 论文编号：2666
- 报告人：Abhijit Sinha
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sinha26b_interspeech.pdf

## 问题
成人预训练 SSL 零样本迁到儿童语音时，常只比全局 WER；相近 WER 是否对应相似错误结构、层是否句级最优、错误能否被 LLM 纠正，仍不清楚。

## 方法
冻结 Wav2Vec2/HuBERT/Data2Vec Large 各层，作 Kaldi DNN-HMM 声学特征；仅用成人数据训（英：WSJCAM0；美：Mini LibriSpeech），测 PFSTAR 与 CMU Kids。分析 S/D/I 比例；句级 oracle 选最低 WER 层；用 Mistral-7B-Instruct（零样本与 LoRA 文本微调）做后处理纠错。

## 实验与结果
PFSTAR 最优 WER 约 5.15–5.69%，层间跨度可达 9–13%；CMU Kids 最优约 21–22%，最差可至 86%。PFSTAR 插入相对更多，CMU Kids 替换主导；成人 WSJCAM 几乎无插入。LLM 纠错几乎不改假设；LoRA 文本微调反而恶化。Oracle 增益：PFSTAR 约 1.3–1.6%，CMU Kids 约 5–6%，且不稳定性高 4–6 倍。

## 结论
相近最优 WER 掩盖层间错误结构差异；域差越大层互补越重要；儿童零样本错误主因是声学表征而非可文本修补的语言不一致。

## 点评
把「选一层」拆成错误结构/句级 oracle/可恢复性三条轴，比刷表更有设计含义。LLM 几乎无效强化了「先改声学」的结论；CMU Kids 高不稳定性是自适应层选择的直接动机。


# Gender Bias in ASR: A Controlled Study of Gender Composition Across Training Paradigms

- 论文编号：3047
- 报告人：Seshan S
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/s26_interspeech.pdf

## 问题
性别差距常被归因于训练数据失衡，并通过在性别可控子集上微调预训练 ASR 来检验；但预训练语料性别分布未知，微调能否真正暴露「组成→差距」关系存疑。

## 方法
三数据集（LibriSpeech clean、Indic TIMIT、Common Voice v3）× 11 种男:女比例（0–100%，步长 10%）× 四系统：微调 Wav2Vec2、SPRING Wav2Vec2、Whisper Medium，以及从零训 Kaldi TDNN-HMM（LF-MMI）；每配置训练时长上限 71.36h，固定测试集与外部 trigram LM。共 132 条件。用 Demographic Disparity Score DDS=100×(WER_f−WER_m)/WER_m。另在 LibriSpeech 极端比例训 Zipformer 验证。

## 实验与结果
Kaldi：DDS 随组成强且可预测（Indic TIMIT 从 +43.1 到 −37.2）；Zipformer 极端比例亦反转（−9.3→+39.4）。三预训练系统 DDS 波动小且无一致方向（多在约 ±12 内），50:50 近零不等于对组成敏感。微调性别配比无法消除如 LibriSpeech 上 Whisper 持续的女性劣势。

## 结论
组成效应在从零训练中真实存在；预训练表征掩盖了微调阶段的组成信号。仅平衡微调数据不足以缓解预训练 ASR 的性别差距，需表征级干预。

## 点评
用从零系统当阳性对照，方法上干净地拆开「效应是否存在」与「微调能否测到」。对依赖微调性别配比做公平性结论的工作是直接证伪；范围仍限英语与二元性别标注。


# Balancing ASR and diarization in end-to-end LLMs for multi-talker speech recognition

- 论文编号：1124
- 报告人：Naijun Zheng
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zheng26b_interspeech.pdf

## 问题
多人 ASR 需「谁说了什么」；流水线解耦语义与说话人，端到端 LLM 又常依赖大规模会议标注。重叠区易诱发重复幻觉，ASR 与 diarization 训练难平衡。

## 方法
双编码器：SenseVoice-small（语义，多层拼接+适配器）与冻结 Campplus（多块时长 400/200/100ms 统计后卷积对齐）。特征融合比较语义-only、特征维拼接、时间维拼接、时间交织（每 20 帧/~1.2s）。标签含 `<SC>`+说话人 ID。段长加权说话人 CE；重叠高 CE token 用自适应阈值 Tmask=max(Avg(CE),2.0) 屏蔽。多阶段：ASR→双人对话→拼接至 8 说话人→AliMeeting/Aishell4 微调。后端 Qwen2.5-0.5B-Instruct，总约 0.7B。

## 实验与结果
时间交织 + mask 最优：AliMeeting Test CER/cpCER 23.61/27.16，Aishell4 Eval 17.18/19.98；相对开源流水线约 18%/24% 相对提升（摘要）。mask 相对 cpCER 增益约 8.5%/6.9%。去掉说话人损失、mask 或 ASR 损失均变差。说话人特征可下采样至约 25% 帧仍可接受。

## 结论
有限真实会议数据下，交织融合 + 段感知说话人损失 + 重叠高损屏蔽可平衡 ASR 与归属，减轻幻觉。未来拟做说话人注册与更长时戳。

## 点评
把重叠幻觉归因于「高损 token 主导反传」并做自适应屏蔽，是很具体的训练诊断。0.7B 相对 SpeakerLM 大数据设定的可比性有测试切分差异，但结构消融本身说服力强。


# Multi-Talker ASR Unaffected by Speaker Change Count

- 论文编号：1582
- 报告人：Naoki Makishima
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/makishima26_interspeech.pdf

## 问题
自回归多人 ASR 用说话人切换 token 串接转写；推理时切换次数超过训练分布会漏说话人、CER/SCCA 崩坏。切段过短又损语义连续性。

## 方法
在 Transformer 解码器自注意力中用说话人切换 token mask 替代纯前瞻 mask：对 `[st]`（及 SOMSRED-SVC 中的时间/说话人 token）置 −∞，禁止其他 query 读到已出现的切换计数；训练时另以概率 r 随机 mask 文本 token，阻断从语境推断话轮数。推理只 mask 切换类 token。应用于「ASR+[st]」与联合 diarization 的 SOMSRED-SVC。

## 实验与结果
CSJ 伪多人混合/拼接；训练最多 2 次切换。3 SC 非重叠：基线 CER 13.5%/SCCA 59.5%，Ours(r=0.6) 5.9%/96.3%，接近含 3 SC 的 oracle。4–5 SC 时基线大量少报切换（CER 22–28%），Ours 多数正确。SOMSRED-SVC 上 r=0.4 时 3 SC CER/SCCA 亦明显改善，TER/EER 几乎不降。

## 结论
屏蔽切换计数语境可使自回归多人 ASR 外推到训练未见的切换次数，而无需为更长话轮重造数据。

## 点评
针对「从历史 `[st]` 计数」这一捷径做结构性封堵，比数据扩容更干净。r 过大伤训练；带时间/说话人 token 时与 oracle 差距仍大，说明被 mask 的结构信号越多越难逼近。


# WildElder: A Chinese Elderly Speech Dataset from the Wild with Fine-Grained Manual Annotations

- 论文编号：102
- 报告人：Hui Wang
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/wang26_interspeech.pdf

## 问题
中文老年语音多在受控环境采集，话题/自发度/信道多样性不足；野外自动管线对老年声又易出错，缺带细粒度人工标注的真实场景语料。

## 方法
WildElder：从在线视频（关键词检索 + 老年创作者频道）收集，人工切分、转写与元数据标注（年龄段、性别、口音强度轻/中/重）。质检要求抽检准确率 ≥95% 等。最终 23,701 句、33.7 小时（619 视频）；说话人级划分训/开/测 18,835/2,465/2,400 句。基线含从零 Transformer/Conformer/Branchformer/Paraformer，以及 CW（WenetSpeech）与 Whisper Tiny–Medium 零样本/微调。

## 实验与结果
从零最优约 Conformer attention rescoring CER 31.74%。CW 零样本/微调 16.43%/13.54%；Whisper-Medium 23.41%/16.14%。微调后女/男 CER 约 10.44%/16.89%；随年龄上升，85+ 明显变差（90–95 约 24.41%）。

## 结论
野外老年普通话仍难；预训练+领域微调必要。数据集可作为 ASR 与说话人画像等任务的挑战基准。

## 点评
「野外来源 + 人工细标」补上现有中文老年库的空白。人口学分解（性别/高龄）把难点落到可行动的采集与适配方向，而不只是报一个总 CER。


# Post-ASR Proper Noun Grounding via Multi-View Phonetic and Semantic Retrieval

- 论文编号：907
- 报告人：Pranshu Nema
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nema26_interspeech.pdf

## 问题
端到端 ASR 对专有名词/长尾词常产出音近但词错的替换，伤下游实体理解；微调代价高，单信号后编辑又弱。

## 方法
后处理专名 grounding：GLiNER 抽实体；对预定义词表做多视图检索——G2P 音素编辑距离、Soundex 粗语音编码、上下文嵌入余弦；min-max 归一化后加权融合排序，不改 ASR 也不用声学特征。在 United-MedSyn 药物名闭集词表上评 Whisper-large-v3 与 Qwen3-ASR-1.7B。

## 实验与结果
原 ASR 实体精确匹配约 38.27%/36.27%。融合（+text-embedding-3-large）Recall@1 达 74.67%/59.82%（相对精确匹配 +36.4/+23.6 pp），R@10 最高 87.36%。单视图中 G2P 略优于 Soundex；语义视图单独较弱但在高 K 互补。近同音与语义近邻仍是残差错误主因。

## 结论
ASR 专名错误具结构化音近性，多粒度语音+语义检索可显著提升实体级 Recall@K，且 ASR 无关。可扩展到其他专名词表；未来拟做自适应权重与解码约束。

## 点评
把「纠错」改成「排序候选供下游/人工」，产品形态更务实。评估条件在 NER 对齐成功样本上，抽取失败被排除，报告的是 grounding 上限而非端到端流水线。


# From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection

- 论文编号：338
- 报告人：Jan Jasiński
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/jasinski26_interspeech.pdf

## 问题
ASR 幻觉（流畅但与音频无关的转录）会拖垮下游系统，但传统 WER 等指标难以把它与普通误听区分开。现有文本指标多依赖参考转写，参考无关指标与 LLM 检测在部署场景下效果有限；真实语音上的人工标注数据也长期不足。

## 方法
在 HALAS 数据集上对 Whisper large v3 做话语级幻觉检测，比较三类范式并做融合：
1. **文本指标**：oracle（WER/CER/IER、BERTScore、SeMaScore、CHP 等）与 reference-free（CPS、PPL、对齐置信度、NCHP 等），用 Logistic Regression / Random Forest / XGBoost 分类。
2. **LLM**：以 GPT-4o mini、Gemini 系列零样本提示为基线，逐步加入更强推理模型、Whisper 非语音幻觉病理、few-shot，并尝试去掉参考转写。
3. **解码器内部状态**：对 Whisper 各层解码序列做 mean/max pooling 与 BLSTM 探测（自注意力 / 交叉注意力 / 最终输出，可加序列差分）。
4. **晚融合**：用 XGBoost 与 BLSTM 的 OOF 概率加音频时长，训练 Logistic Regression 元分类器。

## 实验与结果
数据为 HALAS（Earnings-22 上 Whisper large v3：858/3611 为幻觉）。主要数字：
- 单特征 AUC：oracle BERT 82.3%、CER 81.9%；reference-free 最强 CPS 68.2%。
- 文本分类：XGBoost 全特征 F1 62.8%；仅 reference-free 降至 37.7%。
- LLM：最佳 oracle 配置 F1 58.7%；reference-free 降至 32.8%，仍不如轻量 XGBoost。
- 内部状态：中间层线性可分性约 AUC 81–82%；最优 BLSTM（参考无关）AUC 87.6%、F1 65.5%。
- 晚融合：Acc 90.7%、F1 68.3%、AUC 90.0%，优于单一范式。

## 结论
幻觉信号在 Whisper 解码中间层被编码；参考无关的内部状态探测可超过依赖参考的文本/LLM 方法。文本与内部状态部分互补，晚融合达到最佳整体检测效果。三类方法对单功能词插入类幻觉仍普遍失效。

## 点评
工作把“有没有参考转写”这一部署约束放在中心：oracle 文本特征看起来强，但一旦去掉参考就崩；内部状态探测绕开了这一瓶颈，且不引入 LLM 的延迟。晚融合说明两类错误不完全重叠，但元分类器仍依赖音频时长等弱路由信号，单字幻觉仍需声学侧信息。


# Grounding Whisper: An Audio Anchor-Based Approach for Hallucination Mitigation and Throughput-Efficient ASR

- 论文编号：1314
- 报告人：Saurabh Kumar
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/agarwal26_interspeech.pdf

## 问题
Whisper 在静音与非语音上易产生虚假转录，现有 VAD、置信度、抑制或改模型等方法缓解有限。同时短对话轮次无法填满 Whisper 固定 30 秒窗口，吞吐浪费。需要不改模型、可落地的幻觉检测与安全批处理方案。

## 方法
提出 **anchor audio**：在输入前拼接一段领域内几乎不出现的短提示音频（优选 TTS 合成的 “Mongolia”），用能否正确识别该前缀作为可信度标记；锚点也作多段拼接的分隔符。
五种推理：A1 原版 Whisper；A2 仅 Silero VAD；A3 VAD+锚点前缀，匹配失败则回退整段输出；A4 朴素批拼接后按锚点切分；A5 批处理校验锚点个数，不匹配则回退到单条 A3。推理用 int8 whisper-turbo。

## 实验与结果
1–5 秒片段共约 33k：零售客服私有集、UrbanSound8K（6614，排除 children playing）、AMI、LibriSpeech。
- 整体 WER：A1 32.18% → A5 13.23%；Urban8k HER：A1 72.2% → A3 0.12% / A5 0.14%。
- A4 有 8.45% 切分失败；A5 失败率为 0。
- 并发 32 时 P95 延迟：A3 579ms、A5 566ms，与 A2（570ms）接近。
- 文本 prompt 消融（Ab1/Ab2）HER 仍高于音频锚点，且零售 WER 变差。
- LibriSpeech 上锚点略升 WER（如 clean 2.87%→3.03%），作者归因于专有名词拼写表面差异。

## 结论
输入级锚点音频可在不修改 Whisper 的情况下几乎消除非语音幻觉，并支持带校验的批拼接。A3 适合延迟敏感，A5 适合吞吐；局限包括锚点需领域调参、长句收益下降、仅评 Whisper/英语。

## 点评
做法本质是给自回归解码一个“声学 grounding token”，比纯文本 prompt 更强，且复用同一机制做批分隔，工程上很实用。风险在锚点与真实语音重叠、噪声掩蔽导致匹配失败，以及批校验回退带来的尾延迟；跨领域与跨架构是否成立仍需验证。


# Convolutional Dynamic Rotary Positional Encoding

- 论文编号：1312
- 报告人：Euijin Hong
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/hong26_interspeech.pdf

## 问题
RoPE/RelPos 等位置编码依赖均匀离散时间索引，与语音特征连续、信息密度不均的特性错位；纯 RoPE 在 ASR 训练中还可能发散。Branchformer 的注意力支路缺少中间卷积，局部时序建模不足。

## 方法
提出 **CD-RoPE**：用轻量 depthwise-separable 1D 卷积从输入特征预测连续时间偏移 \(\Delta t\in[-1,1]\)（tanh + ReZero 式可学习 \(\alpha\)），加到基索引后再乘逆频率，得到 \(\hat{\Theta}_{t,i}=(t+\Delta t)\cdot\theta_i\)。在全维特征上算偏移再分头，保留 RoPE 谐波结构；故意调制时间索引而非直接调频率，以避免早期训练不稳定。嵌入 Branchformer 注意力支路。

## 实验与结果
SpeechBrain 上从零训练 Branchformer（18 编码器 + 6 解码器），LibriSpeech 960h；对比 RelPos（109.8M）与 CD-RoPE（107.6M）。
- WER：dev-clean 2.02→1.96；test-clean 2.17→2.13；test-other 5.07→4.95；少 2.2M 参数。
- McNemar 在 test-other 上显著（p≈0.043）。
- Speech Robust Bench：中等强度下 9 类扰动中 7 类更好，时序扰动优势最大（如 severity 4 的 tempo↑：10.73→8.63）。
- 核大小在 100h 子集上对 WER 不敏感（k=7/9/11 约为 5.44–5.47）。

## 结论
CD-RoPE 在 Branchformer 上全面优于 RelPos 且参数更少；鲁棒性增益主要落在时序扰动上，支持“时间轴弯曲”假设。作者刻意只评 Branchformer，向 Conformer 等带卷积结构迁移留作未来工作。

## 点评
把动态性放在“时间索引”而非旋转频率上，是兼顾稳定性与相对归纳偏置的合理设计；对 Branchformer 尤其对口，因为注意力支路本来缺局部卷积。增益幅度不大，且单数据集单 seed、无组件消融，推广性仍需更多证据。


# Diffusion Language Models for Speech Recognition

- 论文编号：2070
- 报告人：Davyd Naveriani
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/naveriani26_interspeech.pdf

## 问题
自回归 LM 重打分/联合解码受限于从左到右顺序，速度受限。离散扩散 LM（MDLM、USDM）可双向建模与并行生成，但如何系统用于 ASR 重打分，以及如何与 CTC 做 token 级联合解码，此前缺乏系统研究。

## 方法
1. **重打分**：对 CTC n-best 用 \(\lambda_{\mathrm{CTC}}\log P_{\mathrm{CTC}}+\lambda_{\mathrm{DiffLM}}F_{\mathrm{DiffLM}}-\lambda_{\mathrm{prior}}\log P_{\mathrm{prior}}\)。对 MDLM 提出样本级/全局 mask 归一化及耦合互补 mask 打分，替代高方差的序列长度归一化；USDM 用其 ELBO。
2. **CTC–USDM 联合解码**：从 CTC greedy 序列与噪声水平 \(t_{\mathrm{start}}\) 起步；每步用 CTC 帧分布（按折叠后首帧对齐、去 blank）与 USDM 全词表标签分布线性组合后 ancestral sampling，迭代去噪。

## 实验与结果
LibriSpeech：CTC 在 960h 训练；DiffLM 在 LS LM 文本 + train-other 转写上训 5/10/25 epoch，DiT 约 110M/340M，SentencePiece 10k。
- MDLM 重打分（样本级归一化，K=256）：dev-other 最优约 4.47%（25 ep），优于序列归一化 4.62%（5 ep）与 CTC 基线 5.08%。
- USDM 重打分：K=256 时约 4.72%。
- CTC–USDM 联合：\(t_{\mathrm{start}}=0.1,L=1\) 达 4.66%；RTF 约 0.003，接近 CTC-only 0.002。
- 自回归 LM 仍更强（first-pass 3.86%，rescoring 4.19%），但扩散重打分 RTF 明显更高。

## 结论
MDLM/USDM 均可提升识别；mask 归一化对 MDLM 重打分很关键；USDM 的全词表分布使其能与 CTC 高效联合解码，单步即可明显降 WER。当前数据规模下自回归 LM 仍更准，作者认为更长训练与更大模型可能缩小差距。

## 点评
贡献重点是“把扩散 LM 接到 ASR 管线”的可操作配方：打分归一化与 CTC–USDM 联合。联合解码用极少额外步数换可观增益，工程吸引力大；但与强自回归 LM 仍有差距，且 MDLM 尚未纳入联合框架，扩展价值取决于能否在保持 RTF 的同时缩小精度鸿沟。


# Do speech foundation models really learn words?

- 论文编号：2676
- 报告人：Robin Huo
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/huo26_interspeech.pdf

## 问题
自监督语音基础模型在探测任务上能区分词身份，但这可能只是因为编码了音素形式（能指），而非独立于局部语音内容的词表征。需要把音系信息剥离后，检验是否仍保留“词”层面的信息。

## 方法
对英文预训练 HuBERT-base 与 wav2vec 2.0 base 的卷积末层及 12 个 Transformer 层，在 LibriSpeech dev-clean 帧级对齐音素/词标签上做线性探测。用 ridge 回归从 one-hot 音素（或左右 diphone、triphone）预测嵌入并残差化，再测词身份分类准确率；先标准化再残差。并在 HuBERT 第 9 层上做无监督词发现（边界检测 + k-means，k=13967），比较残差前后 NED/F1/R。

## 实验与结果
- 残差后音素探测准确率大幅下降（验证有效），但未完全到随机（众数音素约 11.6%）。
- 词探测：原始表示在中后层峰值超约 90%；去掉音素后整体模式仍在；去掉 triphone 后多数层大降，但 HuBERT 9–10 层、wav2vec 7–8 层对长度 3–6 词仍远高于按长度/triphone 众数基线。
- 词发现：去音素残差可改善 NED/F1/R（如相对 Malan et al. 设定 NED 0.508→0.463）；去 diphone/triphone 则损害切分。

## 结论
后期层存在一定程度上独立于局部音系内容的词身份信息；简单残差化可增强词发现中的更高层语言学可及性。局限：需要音素对齐标签；残差未完全抹净线性音素信息；排除单音素词会影响完全去除效果。

## 点评
用线性残差直接拆开“能指 vs 所指”混淆，比单纯余弦相似度更干净。结果说明模型不只是记短 n-gram，但仍不能断定编码了语义/句法；对下游的实用价值受限于对齐标签需求，更适合作为解释与诊断工具。


# Readability Does Not Predict Speech Recognition Errors: Contrasting Human and Machine Perception.

- 论文编号：2439
- 报告人：Baptiste Ramonda
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ramonda26_interspeech.pdf

## 问题
人类在噪声中依赖可读性补偿理解，早期 ASR 也常因文本复杂度/困惑度升高而 WER 变差。现代端到端 ASR 是否仍对文本可读性敏感，还是已与语言学复杂度解耦？真人口语会随难度改变发音，需控制声学混杂。

## 方法
用 CLEAR 语料（4718 段）经 Amazon Polly TTS 固定语速/韵律，再加 DEMAND babble（SNR 0/10/20 dB）与 OpenAIR 混响（0.1/0.9）。可读性用多指标合成的 Global Readability Index（GRI），并对照 Bradley-Terry 简易度；可懂度用 WER；另看预测熵与压缩比作“认知努力”代理。ASR：PocketSphinx、Vosk、Wav2Vec2 Base、Whisper Tiny/Medium。并用 LibriSpeech train-clean-100 拼接自然语音做验证。

## 实验与结果
- GRI 与人类 BT 简易度强负相关（r=−0.56）；原文与转写 GRI 相关 r=0.97。
- 干净条件：Whisper Tiny/Medium 与 GRI 近正交（r≤0.03）；Wav2Vec2 r=0.24、Vosk r=0.14；PocketSphinx r=0.05（作者认为是高错误率饱和）。
- 与人类感知难度均呈负相关（r∈[−0.35,−0.19]）。
- Whisper Tiny 在 0 dB 噪声下与 GRI 仍几乎无相关（r=0.06）；自然语音上 r=−0.02。
- 预测熵与 GRI r=−0.01，压缩比 r=−0.08，未见复杂度带来的内部犹豫或简化。

## 结论
现代 E2E ASR 的转写错误与文本可读性近乎无关，即使在噪声/混响下也成立；声学转写已独立于文本结构复杂度。这支持 listenability 设计中可读性与 ASR 模块可分开优化。仍与人类感知难度保持相关，非结构因素有待厘清。

## 点评
TTS 控制把“文本难度→发音变化”拆开，结论对 Whisper 类模型很清晰。PocketSphinx 的低相关被解释为误差饱和，提醒架构对比要看误差底线。残余的“人类难度相关”说明 ASR 仍踩在某些与人共享的难例上，只是不是经典可读性公式能抓住的那一类。


# Probing Linguistic Information in Speech Embeddings: A Diagnostic Analysis across Acoustic and Structural Domains

- 论文编号：905
- 报告人：Simon Gonzalez
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalez26b_interspeech.pdf

## 问题
现代语音嵌入广泛用于 ASR 与语音–语言模型，但其语言学可解释性不足：不清楚哪些声学/语音学/更高层结构信息可被线性读出，以及信息如何沿层级分布。

## 方法
在 FLEURS 子集（36 语、43185 条、约 136 小时）上，用 W2V-BERT 2.0（约 600M，多语）提取帧级嵌入，时间维 median pooling 得话语向量（长句切 10 秒再 median）。从音频提取声学（jitter/shimmer、谱平坦度、ZCR、centroid 等）、语音学（时长、语速、pitch range、RMSE）与结构特征（Stanza：UPOS 熵、lemma 复杂度、从句复杂度、CTTR）。用 Lasso 回归学习嵌入→特征映射，五折选参，报告 train/test \(R^2\)。

## 实验与结果
线性关联强度随层级递减：
- 声学最强：Shimmer \(R^2\)=0.59，Flatness 0.56，ZCR 0.51 等。
- 语音学：Duration 0.51，Speech Rate 0.32；RMSE 0.19、Pitch Range 0.15 较弱。
- 结构：CTTR 0.43 仍可观；UPOS 0.04、Clause 0.02、Lemma 近 0。

作者强调是分布式、梯度式关联，而非维度与语言学单位一一对应。

## 结论
嵌入对贴近信号实现的声学/时序特征最敏感，词汇复杂度有可测关联，形态与句法复杂度线性可及性有限。结果受数据集、特征与模型选择约束；嵌入宜与符号语言学分析互补，尤其利好低资源场景中的可扩展诊断。

## 点评
这是一份清晰的“能线性读出什么”的诊断图：靠近声学的特征最强，句法最弱，符合自监督目标更贴信号的直觉。Median pooling 可能抹掉跨帧结构关系，因此弱句法关联未必等于模型完全不编码结构；若要追问更高层信息，需要更强探测或保留时序结构的读出方式。


# I Am No One: Style-Aware Paraphrasing for Text Anonymization

- 论文编号：3175
- 报告人：Ahmed Sohair Khan
- 程序：Wednesday 30 September 2026 / New Architecture and Analyses for ASR and Speech LMs
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/khan26b_interspeech.pdf

## 问题
即使去掉显式标识，作者归属模型仍可凭稳定文风指纹重识别用户；该风险也延伸到会议/客服 ASR 转写。差分隐私文本匿名常严重损伤可读性与效用，而一般改写又缺少对风格标记的显式控制。

## 方法
两模块提示式流程（基座主要为 LLaMA-3.2-3B-Instruct，并测 MiniCPM3-4B）：
1. **风格画像**：从每位作者 K=5 样本，让 LLM 总结句长、词汇、语气、标点四维可读 profile；可消融单维。
2. **风格引导改写**：把 profile 写入提示，要求压制所述风格标记并保留语义；对比 semi-guided（只要求中性风格）与 unguided 改写。

评估 AUTHOR10（博客，10 作者）与 ILLINOIS9（短评，9 作者）；对比 DP-Prompt / Quasi-DP / Non-DP、ALISON；效用用余弦相似度、GPT-2 PPL、加权 KL；隐私用 BLEU、归属 F1、相对增益 γ 与流畅度感知 γf。

## 实验与结果
- 归属 F1 相对原文降约 60–70%：AUTHOR10 66.45→26.02（LLaMA），优于 ALISON 29.53；ILLINOIS9 76.78→20.76。
- PPL 接近原文（AUTHOR10 42.47 vs 41），远好于 ALISON（368）与严格 DP（ε=25 时约 8770）。
- Full profile 总体最稳；ILLINOIS9 上 Length-only 隐私增益可略更好。
- Style-guided 相对 semi-guided：隐私接近但效用与信息保留更好；纯 paraphrase 隐私与效用均更差。
- 补充：方法感知白盒攻击下 ILLINOIS9 攻击 F1 仍可从 77 降到 35；Yelp/IMDB 外域归属 F1 可降超 85%。

## 结论
显式风格画像引导的改写能在保持语义与可读性的同时大幅削弱作者归属信号，优于噪声型 DP 与无指导改写。局限包括依赖预设风格维度、指标可能混淆风格抹除与内容损失、尚未在 ASR 转写上系统验证。

## 点评
把匿名化重新定义为“可控风格变换”而非加噪，抓住了归属攻击真正利用的信号。对 ASR 会议文本有明确动机，但正文实验仍是博客/评论；若转写噪声与口语体改变风格线索，效果可能不同于干净文本。攻击者若利用残余内容而非纯风格，仍需与内容脱敏策略配合。


# Reducing the Offline-Streaming Gap for Unified ASR Transducer with Consistency Regularization

- 论文编号：1195
- 报告人：Andrei Andrusenko
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/andrusenko26_interspeech.pdf

## 问题
同一 ASR 模型同时做好离线高精度与低延迟流式仍难；Conformer 的 MHA/卷积在 chunk 解码下存在训练–推理失配，低延迟（<0.5 s）时离线/流式模式冲突加剧，大规模数据下的统一训练也欠研究。

## 方法
统一 RNNT：chunk-limited attention（左/当前/右上下文 L,C,R，训练时从预定义集合采样）+ Dynamic Chunk Convolution（DCConv，卷积按 chunk 与核半宽重排，离线共享参数）。训练可用单模式（每步随机 offline/streaming）或双模式（同 batch 两边 RNNT 损失加权）。进一步提出 MCR-RNNT：对离线与流式 joint logits 做对称 KL，用 Triton 融合核在线算 log-softmax/KLD，避免物化巨大 [T,U+1,V] 张量。最终目标 α L_off + (1−α) L_str + λ L_MCR。曾尝试 CR-CTC 扩展，对流式 RNNT 有害，故改为对 Transducer 输出一致性。

## 实验与结果
L-size FastConformer RNNT（~128M）在 Granary ~120k 小时归一化英文上训；Open ASR Leaderboard 平均 WER。Unified DM + MCR-RNNT：离线 6.63，流式在 0.24 s 仍 9.04，显著优于无 MCR 的 SM/DM（低延迟急剧恶化）。XL ~0.6B + 280k 小时含标点大小写：较大右上下文配置离线 AVG WER 5.76（SOTA Unified RNNT），平衡配置低延迟更稳。消融：对称 KL、λ≈0.3、α≈0.5 较优；固定总延迟下增大右上下文降 WER。

## 结论
chunk 限制注意力 + DCConv + MCR-RNNT 可把离线/流式差距压到更低延迟区间，并随模型与数据放大仍有效；框架与英文 checkpoint 开源。

## 点评
关键不是再叠一套编码器，而是在 RNNT joint 输出上显式拉齐两种上下文制度；相对 CTC 一致性，更贴合 Transducer 的对齐灵活性。工程上 Triton 全格点一致性使方法可训练。当前推理仍每步重算左上下文，作者承认速度未充分优化；极低 0.16 s 仍略逊纯流式基线。


# BACON: Boundary-Aware Convolution for Streaming Conformer Models

- 论文编号：1455
- 报告人：Hainan Xu
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/xu26o_interspeech.pdf

## 问题
Chunk-based 流式 Conformer 常把深度卷积改成因果卷积以防未来泄漏；但 chunk 内帧已全部可用，纯因果卷积过度限制右上下文，丢掉安全可用的局部未来信息。

## 方法
提出 BACON：深度卷积通道对半拆分——因果组保留完整历史（仅句首左 pad）；边界感知双向组左上下文可跨 chunk，右上下文用 chunk 末 pad，严格限制在当前 chunk 内。核大小 k 时有效感受野约 [−(k−1),(k−1)/2]，宽于因果 [−(k−1),0]，参数量不变。作为因果卷积的 drop-in 替换。

## 实验与结果
NeMo FastConformer（17 层，d=512，k=9，chunk C=14≈1120 ms）上对比因果 vs BACON，架构含 RNN-T 与 CHAT。LibriSpeech：CHAT test-other WER 8.47→7.68（相对约 9.3%，p<0.001）；test-clean 也有显著改善。En→De AST：两族模型在 MuST-C/CoVoST 上 BLEU 均显著提升（如 CHAT CoVoST 36.40→37.72）。双说话人 Fisher cpWER 27.41→27.14（方向一致，p=0.19）。消融：全通道 boundary-aware（all-bidir）常弱于 BACON，甚至在 RNN-T test-other 上差于因果；因果组起边界稳定作用。全注意力设定下非因果卷积仍比因果低 0.93 WER，说明卷积右上下文与注意力互补。平均发射 chunk 索引略降，未增延迟。

## 结论
在 chunk 流式约束下用通道拆分安全引入 chunk 内右上下文，可在多任务、多架构上提准且不增加参数与延迟。

## 点评
洞察很具体：流式约束是“不看未来 chunk”，不是“永远不看未来帧”。双组设计避免 chunk 右缘全通道有效感受野同时塌缩。收益在困难集与翻译上更明显；多说话人增益较小，可能被重叠/说话人归因噪声淹没。


# Progressive Alignment Objectives for Aligner-Encoder based ASR

- 论文编号：2132
- 报告人：Jaeyoung Lee
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26t_interspeech.pdf

## 问题
Aligner-Encoder 用编码器第 u 个位置直接预测第 u 个 token，无 cross-attention / Transducer 格点；对齐多在深层突然出现，长句上训练脆、性能差。

## 方法
提出 InterAligner：在中间层 ℓ_int（主实验第 15 层）对更长、更细粒度 BPE 序列加中间 Aligner 损失（独立 predictor/joiner）；在更早层 ℓ_ctc=12 加 InterCTC；顶层仍对较粗短序列做最终 Aligner。总损失加权 λ_final L_final + λ_int L_int + λ_ctc L_ctc，形成由早到晚、由细到粗的对齐课程。

## 实验与结果
17 层 Conformer-L（~118M），LibriSpeech 960h：Final-only 5.0/7.8 → +InterCTC 3.4/6.0 → +InterAligner 3.1/5.6（test-clean/other）。Common Voice EN：12.4→11.2→10.9。按时长分层，>21 s 句 clean/other 从 InterCTC 的 17.0/18.0 再到 InterAligner 的 11.6/13.5。消融：中间与 CTC 目标同用较小词表（如 256）优于不匹配；λ_final/λ_int=0.5/1.0 优于 1.0/0.5；InterAligner 挂在第 15 层优于第 16/13；仅缩小最终词表不够，需要层级监督。注意力可视化显示层 14 出现细粒度对角、层 16 再到粗粒度。

## 结论
中间 CTC + 中间细粒度 Aligner 可让对齐在深度上渐进形成，稳定 Aligner-Encoder 训练，并在长句上带来最大收益。

## 点评
针对“对齐瓶颈挤在顶层”的结构问题，用多粒度中间监督做课程，比单纯加深或换解码器更对症。挂层位置与词表粒度敏感（需留出至少约两层做细→粗转换）。收益主要在长句；短句上相对 InterCTC 提升有限。


# From Bilevel to Trilevel: Joint Training for Speech Recognition

- 论文编号：1738
- 报告人：Jen-Tzung Chien
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/chien26b_interspeech.pdf

## 问题
ASR 常用“无监督预训练 + 监督蒸馏微调”两阶段流程，预训练损失在微调时被丢弃，易遗忘或负迁移；既有双层优化（如 BL-JUST）联合监督与无监督，但仍缺少知识蒸馏这一层。

## 方法
提出 TL-SUD：三层嵌套优化——上层监督损失 L_sup（标注数据）、中层无监督 L_unsup、下层蒸馏 L_KD（标注+无标注，蒸馏时不用真标签）。将中下两层折叠成双层子问题，用惩罚型双层梯度下降（PBGD）两次，得到共享骨干 θ 与各任务头 ϕ/η/ψ 的嵌套更新；惩罚系数 γ1、γ2 随 epoch 从 0 退火升至最大值。实现上 FastConformer 学生（115M，17 块）用 CTC 监督、对比无监督、特征级蒸馏；教师更大 FastConformer（616M）。

## 实验与结果
LibriSpeech：unlabeled=train-other-500，labeled=train-clean-100 时，TL-SUD test-clean/other 6.7/15.9，优于 PT(U)+FT(SD) 7.4/19.5、加权求和 7.4/19.1、监督基线 8.7/23.0。相对 BL-JUST（无 KD）在 100/200/360h 标注上均更低 WER（如 100h：6.7/15.9 vs 7.0/17.1）。惩罚日程敏感，最佳约 γ1 max=180、γ2 max=0.005。解码为无外部 LM 的 greedy。

## 结论
把监督、无监督与蒸馏纳入可训练的三层优化，能比两阶段与双层 JUST 更一致地利用三类信号，并在低资源标注设定下降低 WER。

## 点评
做法把“遗忘预训练语义”的管线问题改成嵌套可行集约束，KD 放最底层注入教师先验。工程关键是惩罚调度；调不好会破坏三目标平衡。评价刻意去掉 LM，突出优化本身，但绝对数字与带 LM 系统不可直接比。


# LLM-as-Joiner: Decoupling Alignment from Language Modeling in Label-synchronous ASR

- 论文编号：2149
- 报告人：Jaeyoung Lee
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26u_interspeech.pdf

## 问题
把 LLM 当 speech-as-prefix 解码器时，模型既要学对齐又要做语言建模，上下文长达 T+U，内存与计算重；对齐本可由语音编码器更好承担。

## 方法
LLM-as-Joiner：Aligner-Encoder 产出 U 个 label-synchronous 语音状态（监督前 U 个编码器位置）；预训练 Llama-3.2-3B 在选定层 ℓ 注入语音（门控残差融合），下层当 predictor、上层当 joiner，仅上层 LoRA（rank 16），tokenizer/嵌入/LM head 不变、无 blank。同编码器并行训练轻量 LSTM+FFN 头以便无 LLM 部署。总损失：λ_llm L_llm + λ_lite L_lite + λ_ctc L_ctc（1.0/0.5/0.1）。

## 实验与结果
Conformer-L 从零训练。LibriSpeech：LLM head 3.2/5.6，优于 decoder-only 基线 3.7/7.1；Lite head 3.8/6.4，接近从零 Aligner 3.9/6.5。cv-5langs（de/en/es/fr/it）：LLM head 均 11.5，Lite 12.5，显著优于从零 Aligner 14.4；decoder-only 在多语未收敛。RTF：Lite 0.02，LLM head 0.65 vs decoder-only 0.90。消融：注入层 0/7 相近，14 变差；门控用 speech+text 对 Lite 更有利。

## 结论
用 Aligner 管对齐、LLM 管语言建模，可在更短上下文下提升识别，并让联合训练的轻量头隐式受益于 LLM。

## 点评
接口设计清晰：U 长度对齐面让 LLM 不必吞长语音前缀。对照实验刻意不用预训练语音编码器，突出架构差异。多语上 Lite 头收益更大，说明知识迁移对低资源语言更关键；晚注入失败提示融合仍需足够上层容量。


# Accurate Source-Free Speech Classification via Meta-Learned Target-Centric Model Merging

- 论文编号：371
- 报告人：Ka Hyun Park
- 程序：Thursday 1 October 2026 / New Training Methods for ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/park26b_interspeech.pdf

## 问题
无源域数据、仅有多个预训练源分类器与少量目标标注时，如何适配未见目标域；常规迁移/数据选择不可用，现有模型合并易在少样本目标上过拟合。

## 方法
提出 MOCHEE：冻结 wav2vec2 等共享嵌入，只合并各源 MLP 分类头。用 Sinkhorn 软置换矩阵对齐隐单元（消除置换对称性），再学源权重 α 做对齐参数空间加权平均。α 不直接拟合目标训练集，而用 meta-reweighting：内环在目标 train 上虚更新置换参数 p，外环用目标 val 损失对 α 取元梯度（非负后 softmax）。源参数本身不更新。

## 实验与结果
CAMEO 情感跨语料：源 CREMA-D/SubESCO/RAVDESS/MESD，目标 CAFÉ、Oréau（六类情绪）。MOCHEE 在 CAFÉ Acc/Macro-F1 50.85/49.40，Oréau 35.30/34.85，优于 Uniform、Greedy Soup、Re-basin、TIES 等；相对最差基线 Macro-F1 可高约 14.5 点。即便基线再在目标上微调，MOCHEE（不微调）仍最好。消融：去置换对齐掉点大；去 α 学习也一致变差。权重演化显示目标英源时逐步抬高英语源 CREMA-D。

## 结论
在源自由、少目标标签设定下，对齐 + 元学习源重要性的目标中心合并，可比启发式合并更好泛化到未见目标样本。

## 点评
抓住“能共享模型不能共享数据”的现实约束，把合并权重当元学习对象而非验证集挑模型。软置换让异构训练头可平均；内环改 p 而非 θ 保留合并效率。局限在分类头合并与共享冻结前端假设，且效果依赖目标 train/val 划分质量。


# LLM-HB: Language-Aware LLM-Guided Hotword Biasing for Code-Switching ASR

- 论文编号：1113
- 报告人：Yuxuan He
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/he26c_interspeech.pdf

## 问题
码切换 ASR 易受跨语混淆；热词偏置多服务单语系统，CS 场景下较少与 LLM 自适应偏置结合。

## 方法
LLM-HB：Whisper-medium 编码器 + MoE adaptor（默认 2 experts、top-2）得到语言特化语音嵌入；Qwen3-4B 经 LoRA，输入拼接语音、热词与（训练时）转写嵌入，并用辅助语言头对 LLM 隐状态做 Mandarin/English/other 监督。训练目标 L = L_ASR + λ1 L_Bias + λ2 L_Lan（λ1=0.6，λ2=0.3）。热词经冻结 LLM tokenizer/文本编码器注入提示。

## 实验与结果
评测 ASRU2019-CS，每句 15 个干扰热词。全量约 2200h（ASRU+LibriSpeech+AISHELL-2）上，完整模型 MER 5.85（基线 7.34，相对降 20.30%），B-MER 8.99（基线 22.11）；CER/WER 4.94/13.21。仅 200h CS 数据时完整模型 MER 7.36（基线 9.59），热词提示单项收益最大。消融：2 choose 2 优于更多专家；λ1 增大使 CER/WER 更平衡，主实验取 0.6。

## 结论
语言特化 MoE、语言监督与 LLM 热词提示互补，可在码切换 ASR 上显著改善总体与热词相关错误率；作者称首次将 LLM 引导偏置引入 CS-ASR，并释放热词列表。

## 点评
把“分语表示”和“上下文热词”绑在同一 LLM 条件接口上，适合双语切换。热词损失权重调节英/中错误平衡；专家数不必多，双语场景两专家即可。小数据时单独加 MoE 可能略伤性能，需与语言/偏置信号联合才稳。


# Improving Code-Switching ASR with Code-Mixing Guided Synthetic Speech

- 论文编号：642
- 报告人：Yue Heng Yeo
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/heng26_interspeech.pdf

## 问题
码切换 ASR 缺高质量 CS 语料；用 TTS 增广时多优化重建保真度，未显式约束语言边界一致性，合成数据对下游未必有用。

## 方法
提出声学级 CMI_speech：用带 Language Alignment Loss 的 Whisper 解码器交叉注意力得到帧级伪语言标签，再按非主导语言帧占比定义混合度；与真值语音的 |ΔCMI| 衡量结构保真。对 CosyVoice2 先做 SEAME CS 微调，再以 DPO 对齐：同文本随机采样多样本，用归一化 UTMOS、MER、ΔCMI 打分构造偏好对（最优 vs 最差，并过滤 MER>20%、UTMOS<2.5、ΔCMI>20%）。合成语音与真实数据按等时长混合微调下游 ASR。

## 实验与结果
SEAME 约 192h。TTS 上加 ΔCMI 使 ΔCMI 28.1→16.1、MER 16.2→10.3，UTMOS 维持约 3.8。Whisper-large v3：Real 100h MER 12.1/17.8；+CosyVoice 10.1/16.0；+DPO(UTMOS,MER) 9.6/15.1；+ΔCMI 8.9/14.2（DevMAN/DevSGE）。CTC Conformer 同步改善至 15.4/21.9。定性显示 ΔCMI 更能稳住跨语边界与英文段发音。

## 结论
用声学码混指标引导 DPO，可让合成 CS 语音更贴近真实混合结构，从而更有效地提升下游码切换 ASR。

## 点评
关键是把“文本 CMI”落到帧级声学，直接进偏好学习，补上仅 MER/MOS 管不了的边界问题。依赖伪标签 LID 质量与过滤阈值；合成与真实等时长设定保证公平，但未展开更大规模合成比。


# Reinforcement Learning for Data-Efficient Code-Switched ASR

- 论文编号：2667
- 报告人：Ziwei Ye
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ye26c_interspeech.pdf

## 问题
语音 LLM 可提示做码切换，但自回归交叉熵未直接优化序列级错误，切换边界易出现翻译整段、脚本污染等失败；标注 CS 数据稀缺。

## 方法
以 Qwen2-Audio 为可控试验台，用 GRPO 做 RLVR：组内采样 G=8 候选，用可验证奖励做相对优势。奖励 = −CER + β_sf·Script（β_sf=0.05），Script 要求字符落在语言对允许 Unicode 脚本并集。训练期两遍 draft-and-refine：第一遍 GRPO，再以最高奖励草稿条件第二遍；测试仍单遍。仅更新解码器，音频编码器冻结。

## 实验与结果
在 CS-FLEURS XTTS-TRAIN（TTS 合成）上训，评 READ-TEST 与零样本 SwitchLingua。10% 数据的 RLVR（CER+SHR+refine）可匹配全量 LoRA SFT；20% 时微均 CER 0.147 优于全量 LoRA 0.159。SHR 奖励显著降脚本幻觉且不伤 CER；CER 奖励几乎消除翻译错误。收益在类型学上更远的语对（如 ara/jpn/rus）最大。训练全用 TTS，零样本转移到真人录音。

## 结论
序列级可验证奖励 + 脚本保真与两遍自修正，能以远少于 SFT 的数据把语音 LLM 对齐到码切换转写行为，并跨声学域迁移。

## 点评
把 CS 失败拆成“翻译”与“错脚本”两条奖励通路，分析清楚；两遍 refine 对部分语对有益但阿拉伯语可能过修正，需 SHR 约束。定位是数据效率与奖励设计研究，非追 SOTA。


# Direct Preference Optimization for English-Mandarin Code-Switching Speech Recognition in Audio LLMs

- 论文编号：110
- 报告人：Minh Duc Pham
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26_interspeech.pdf

## 问题
多语 Audio LLM 在英–汉码切换转写上仍系统失败：漏掉一种语言、整段翻译、幻觉重复；即使含 CS 监督数据的模型也可能如此。

## 方法
用 DPO 对齐：chosen 为真值混合转写，rejected 由 Qwen3-32B 对真值做全局翻译（80%）或部分片段翻译（20%）以模仿失败模式。约 100K 对 / ~570h，来自 CS-Dialogue（自然对话）与 EMILIA（英汉拼接）。训练 MERaLiON-2-3B、Phi-4-MM（全参）与 Qwen2-Audio-7B（LoRA，全参易幻觉）；训练时从 20 英 + 20 中提示池随机采样，评测固定英文转写提示。

## 实验与结果
相对基线 MER：Phi-4 在 EMILIA 70.98→7.38（相对 −89.6%）；Qwen2-Audio SEAME dev man 72.89→58.30（−20.0%）；MERaLiON 因已有 CS SFT，SEAME 增益较小（0.7–2.0%），CS-Dialogue −11.1%。定性显示翻译、幻觉、漏语等三种失败模式均被纠正。SEAME 为分布外。

## 结论
偏好对可把已具备多语能力的 Audio LLM 引出正确的“原样混合转写”行为，分布内与分布外均有一致改善。

## 点评
核心是行为对齐而非重训声学：用可控合成 rejected 放大“翻译≠转写”信号。未显式构造幻觉/漏语 rejected，但三类错误仍下降。局限：仅英汉、rejected 非模型自身采样、未测对其它音频能力的副作用。


# Adding Robust Code-Switching Capabilities to High Performance Multilingual ASR

- 论文编号：1099
- 报告人：Enes Yavuz Ugan
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ugan26_interspeech.pdf

## 问题
在已很强的多语 ASR（如 Whisper）上加码切换能力时，标准合成数据微调常严重破坏单语表现；文献多评弱基线或域内设定，强模型保真场景研究不足。

## 方法
场景定位为“强模型保真”。用 GPT-4o 按等价约束与德英形态整合规则生成 CS 文本（§§…§§ 标出切换点），xTTS-v2 按段分语合成再拼接。适配采用 BLoRA（贝叶斯低秩，μ/σ 先验推向稀疏 ΔW，λ_KL=0.5）而非标准 LoRA。评 CSFleurs 的 WER 与切换词 PIER，并用 CommonVoice 做单语回退测试。

## 实验与结果
基线 Whisper：DE/EN/CSFleurs WER 8.53/13.56/11.49，PIER 26.59。标准 LoRA 在任意数据量上单语与 CS 均大幅恶化；复杂 MT+对齐拼接同类。BLoRA + 全量合成：CSFleurs WER 10.88（相对改善约 5.31%），PIER 20.84（相对约 −21.6%），单语接近基线。严过滤 CER≤5% 时，仅 1k 样本即可将 PIER 降约 32.87%（文中最佳约 17.85）。文本多样性比说话人多样性对 PIER 略更有利。定性：基线把 matter 误成 meta，BLoRA 可保留英文插入。

## 结论
对强多语模型，瓶颈在知识整合而非合成数据复杂度；稀疏不确定性感知的 BLoRA 可用少量合成数据提升 CS 且保住单语能力。

## 点评
刻意选 Whisper 已很强的德英，否定“更好合成必更好”的假设。BLoRA 稀疏更新是关键机制；过滤在小数据时极重要。依赖手工 PIER 标注与特定语言对规则，向更远语对迁移仍需验证。


# Dynamic Block-Online Streaming ASR for Low-Resource Agglutinative Code-Switching Speech with Morphology-Aware Evaluation

- 论文编号：3334
- 报告人：Nabeel Mohammed
- 程序：Thursday 1 October 2026 / Code-Switching ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/rafat26_interspeech.pdf

## 问题
低资源黏着语（Bangla–English）句内码切换 ASR 中，固定前瞻的因果流式注意力无法回头修正词根–后缀与脚本重排依赖，易在切换点截断形态；码切换数据稀缺，标准 WER 也难以区分切换、词根与后缀错误。

## 方法
以非自回归 Paraformer（SAN-M + CIF）为骨干：离线用全局双向注意力训练；推理改为 Dynamic Block-Online——VAD 在自然停顿（>200ms）切语义宏块（上限约 3s），块内恢复全局注意力以事后绑定词根与后缀。数据侧用 Script-Anchored Loanword Injection：用约 750 个英–孟语义对，将孟加拉词根替换为英语词根并保留孟加拉后缀，诱导句内 CS。提出 CS-WER，分解为 Eswitch / Eroot / Emorph。

## 实验与结果
训练约 750h Bangla（Common Voice、OpenSLR 53、IndicVoices、KathBath 等）+ 250h Gigaspeech 子集；注入后约 20% 句含 CS。Common Voice 上：因果流式即便扩到 3s（WER 37.20%）形态仍平台（Eroot≈0.35、Emorph≈0.42）；Dynamic Block（3s）WER 38.73%，但 CS-WER 达 .53/.29/.35，接近离线 topline。月经/更年期医疗 TTS 适应后，Block-Online 在噪声留出集上 WER 27%、Eroot 22。

## 结论
对黏着语 CS，灵活延迟预算上的双向块注意力比单纯拉长因果窗口更能保住形态与切换语义；脚本锚定注入与 CS-WER 分别解决数据与诊断。局限：依赖可靠 VAD，词表仅覆盖常见借词。

## 点评
核心洞见是“因果不可逆提交”与黏着 CS 的长距依赖不匹配，用 VAD 宏块换回全局注意力，比硬堆 lookahead 更对症。CS-WER 把切换/词根/后缀拆开，解释了为何 Global WER 接近时语义仍差。医疗域“无损迁移”叙事有吸引力，但合成 TTS 适应与真实临床声学差距仍需谨慎解读。


# Expressive Speech Translation

- 论文编号：
- 报告人：Philipp Koehn
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
语音到语音翻译仍具挑战，模型结构、训练数据、评估方法等尚未充分共识。前沿之一是在翻译中保留输入语音的表达性：从说话人声音、情绪与声学条件等全局属性，到停顿、语速变化、强调与单词级音高等局部属性。

## 方法
调研覆盖训练数据、数据合成方法、语音表征、模型结构、大语言模型的使用，以及评估指标等各方面。摘要未展开某一单一系统的实现细节。

## 实验与结果
未提供具体语料或数值结果。

## 结论
表达性保持是 speech-to-speech translation 的重要前沿；需要在数据、表征、架构、LLM 利用与评估上系统推进。

## 点评
把「表达性」拆成全局/局部属性，问题边界清晰。材料停留在议题地图，不含可复现配方。


# Personalized Keyword Spotting for User-Defined Keywords Leveraging Text-Independent Speaker Verification

- 论文编号：1130
- 报告人：Ming-Hsiang Hu
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/hu26c_interspeech.pdf

## 问题
用户自定义关键词检出（UD-KWS）学到说话人无关表示后，无法拒绝说对关键词的冒名者；文本相关 SV（如 PK-MTL）又绑死固定关键词，破坏零样本灵活性。需同时应对未见关键词与未见说话人（双零样本），且模型需适合边缘部署。

## 方法
提出 ZP-KWS：双分支解耦——冻结的 EfficientTDNN-Small（约 0.9M）说话人编码器（VoxCeleb2 预训练 + LibriPhrase GE2E 微调，短句嵌入稳定），与音素监督音频编码器（冻结预训练嵌入 + 可训 Conv1D–BiGRU，MFA 帧级音素对齐损失 Lalign）。文本经 G2P 后与音频经自注意力 Pattern Extractor/Discriminator 得到 putt；说话人余弦经标定线性层得 pspk。推理时乘法晚融合 pfinal = putt · pspk，可无重训切换 C-KWS / TB-KWS / TO-KWS。总损失 Lutt + Lphon + Lalign。

## 实验与结果
LibriPhrase Easy/Hard、Qualcomm、Google Speech Commands；关键词与说话人均未见。TO-KWS 上相对最强基线 PK-MTL，FRR@1%FAR 相对降幅最高约 60%（如 LibriPhrase Easy：29.47% vs 72.79%）；C-KWS EER 在多数集仍最优（Easy 2.38%）。消融：去掉 GE2E 后 TO FRR@1% 从 29.47% 升至 73.42%；去掉标定层 TO EER 恶化；总参数约 1.55M。

## 结论
功能解耦的 TI-SV + 音素监督 + 乘法门控，可在零样本关键词设定下加入生物识别安全，并在固定模型上切换严格度。未来关注噪声与失配下的置信度标定。

## 点评
把“关键词分数补偿说话人分数”的加性融合改为严格 AND，切中边缘误唤醒痛点；GE2E 短句微调是 TO 模式增益的主要来源。Hard 最小对上整体 FRR 仍高，说明音素混淆时 SV 只能互补、不能替代内容判别。


# wav2tok 2.0: Scalable Audio Tokenization Maintaining Explicit Pairwise Token Alignment for Efficient Audio Retrieval

- 论文编号：141
- 报告人：Adhiraj Banerjee
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/banerjee26_interspeech.pdf

## 问题
QbE-STD 需要可变长话语间保持相似的离散语音表示；wav2tok 用 CTC 显式对齐但聚类与对比–对齐紧耦合，难扩展；BEST-STD 可扩展但对齐仅隐式依赖 DTW 正样本采样。

## 方法
wav2tok 2.0 以 BEST-STD 为骨干（谱前端 + 双向 Mamba，约 4.7M 参数，VQ 码本）。两阶段训练：Stage I 用 SimCLR 式对比损失 + commitment，经 DTW 构造帧级锚–正对；Stage II 加入无 blank 的 CTC 成对对齐（对去重 token 序列做前向后向），并提出 DTW 对齐的帧级 token 预测损失 Lpair；λCTC 自适应缩放为对比损失量级的约一半，避免 CTC 主导或数值不稳。检索沿用 BEST-STD：1s 段、bigram 倒排索引 + Jaccard 精排。

## 实验与结果
LibriSpeech train-clean-360 训练，在 train-clean-100 检索，并测未见 TIMIT。离散一致性（Table 1）：码本 256 时 unigram/bigram Jaccard 达 0.83/0.75，优于 BEST-STD 与 wav2tok。QbE-STD（Table 2）：512 码本 LibriSpeech IV MAP/MRR 0.86/0.90，OOV 0.82/0.84；TIMIT 上仍领先；相对仅 CTC 的 wav2tok，帧级预测进一步抬高 MAP/MRR 与 MTWV。

## 结论
在可扩展骨干上把显式成对对齐做成一等训练信号，可同时提升 token 稳定（尤其 bigram）与检索指标，且不牺牲效率。未来可并入 OT 码本均衡，并扩展到多语/噪声/长音频与语音 LLM。

## 点评
分段训练把“先聚好再对齐”说清楚，自适应 λCTC 是可扩展配方的关键工程点。增益主要来自检索向目标而非通用 SSL 表征；大码本上 MAP/MRR 与 MTWV 的折中仍在，说明对齐不能消去词汇量–鲁棒性张力。


# Rethinking Organization Entity Modeling in End-to-End Acoustic Named Entity Recognition

- 论文编号：3115
- 报告人：Spandan Dey
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/dey26b_interspeech.pdf

## 问题
端到端声学 NER 中，组织名因多词跨度、缩写、OOV 与跨度内非实体词，比人名/地名更难；常规交叉熵不显式建模实体起止结构依赖，边界易截断或外扩。

## 方法
基于 Whisper-small（编码器冻结，解码器前九层冻结）：(1) LLM（Phi-3-medium）针对性语义增强——缩写展开与词汇改写，再经规则清理，XTTS-2 多说话人合成语音；(2) 训练期专用 `<org end>` 边界标记；(3) Structure-Constrained Entity Learning（SCEL）：在 LCE 上叠加实体差分、标签抑制、跨度覆盖、边界一致性，以及熵正则与置信度标定。数据为 Yadav 等英文声学 NER 库（约 150h，LibriSpeech+Common Voice，90:5:5）。

## 实验与结果
相对纯 LCE（Org-F1 30.35），SCEL 将 Org-F1 提到 40.00、WER 8.27；SCEL+TSA+`<org end>` 达 Org-F1 51.40（相对 SCEL +11.40）、WER 9.53。优于 ASR+Flair 流水线（Org-F1 19.04）与 WhisperNER（约 30–31）。合成单跨/多跨测集上，提议框架多跨 Org-F1 明显高于 CE 基线。

## 结论
组织类弱点可通过对数据增强、类别边界标记与结构损失组合显著改善，同时保持 ASR 与其他实体类别可用；未来扩展多语声学 NER。

## 点评
诊断（多词、缩写、跨度内虚词）与解法（TSA、org end、SCEL）一一对应，比单纯放大 Whisper 更可解释。Org-F1 提升伴随整体 F1/WER 小幅回退，说明类别特化存在权衡；LLM-TTS 增强对真实录音分布的外推仍是主要风险点。


# AnySimLite: A Lightweight Few-Shot Similarity Encoder for On-Device Speech-Adjacent Classification

- 论文编号：1316
- 报告人：Sourav Ghosh
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/ghosh26e_interspeech.pdf

## 问题
端侧语音相邻 NLP（意图、情感等）若为每任务部署专用大模型，存储压力大；许多任务可归约为“细粒度文本相似”（NTS），需要单一轻量编码器在少样本下覆盖多任务。

## 方法
提出 ANYSIMLITE：词嵌入通道（含注意力）+ 字符 Conv/池化通道，编码器输出后余弦相似；玩具任务 Event Title Similarity（同事件且同命名实体才算相似）。用 DBSCAN 聚类采样“困难”正负对（簇内/簇间约 8:2）把分类集改造成成对相似数据。消融选 B3 为基座，B8 用 MiniLM 蒸馏为部署变体。少样本：每类 20 个样例预计算 16 维嵌入后近邻分类。

## 实验与结果
TitleSim 消融 B3 F1 89.22（0.42M）；部署变体 Acc 90.83。跨任务（Table 2）：相对各任务 SOTA，最差降幅低于约 7%，参数远小于 qLLaMA LoRA-7B 等；SMS Spam 上 F1/Acc 达 97.50/99.28。Galaxy S25 Ultra：8-bit 约 700KB、推理 <30ms。相对最优结果平均准确率降约 2.24%±3.23%。

## 结论
词+字符轻量相似编码器配合困难对变换，可在极少参数下把多种语音相邻分类压到 NTS 少样本协议，并适合端侧。未来可探索分类以外任务。

## 点评
把多模型问题收成“一个相似核 + 每任务样例库”，工程叙事清晰；字符通道针对 OOV NE 与端侧词表限制。NTS 归约假设任务可用样例原型刻画，对细粒度多标签或强依赖语序的任务可能变脆；与大模型差距任务相关，不宜外推为通用 NLP。


# A Compact Fully-Open Cache-Aware Streaming Model for Japanese ASR

- 论文编号：3380
- 报告人：Yinchang Yang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yang26r_interspeech.pdf

## 问题
高性能日语 ASR 常闭源、缺数据细节或仅离线；端侧实时需要流式与可复现的全开放配方，且公开资源偏电视域、讲座/对话覆盖不足。

## 方法
123M FastConformer 混合 RNNT/CTC（CTC 辅助权 0.3）+ cache-aware 多上下文流式（训练采样 [L,R]∈{[70,13]…[70,0]}）。ReazonSpeech ~35K h 预训练，对比全量与 CER 分层策展（丢 CER>20%，三质量带加权）。再在约 507 h 五域渐进微调（含新建 TEDxJP-20h、MSR/BTSJ 过滤等）。

## 实验与结果
五测集平均 RNNT CER 12.4%，优于全开放 OWSM-CTC v4（13.5%）与 ReazonSpeech NeMo-v2（14.1%），参数小 5–8×；RTFx 1220（批）/446（流式）。CER 策展在缺讲座微调时显著帮 TEDx；与多域微调+更深预测 RNN 叠加时反而伤 TEDx。加 TEDx 数据单步可把 TEDxJP-10K CER 从 25.80 降到 13.71；[70,13] 与全句准确率一致，全因果平均升约 1.65 点。

## 结论
首个同时满足权重/数据清单/代码/日志全开放与 cache-aware 流式的日语 ASR；小模型+领域覆盖可打过更大离线开放基线。

## 点评
开放度与流式并重的缺口填得扎实；2×2 策展实验说明“清洗≠总更好”，与解码器容量和微调范围有交互。相对闭源大模型（如 parakeet 10.0%）仍有差距，但在可复现流式赛道上定位清晰。


# Robust Streaming ASR with Decoupled Separation and Recognition

- 论文编号：1503
- 报告人：DeLiang Wang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yang26h_interspeech.pdf

## 问题
流式 ASR 在噪声、混响与干扰说话人下研究不足；多条件训练（MCT）需大规模含噪数据且常伤干净语音表现。

## 方法
解耦框架：在线分离前端（DPDFNet、因果 oTF-CrossNet；另报全上下文 TF-CrossNet）+ 仅干净语音训练的流式后端。提出 FastMambaformer（FastConformer 中卷积换成 Mamba），并接 NeMo 预训练 FastConformer 与 SimulStreaming。前端与 MCT 基线见相当数据量；推理均零 look-ahead。

## 实验与结果
干净 LibriSpeech 上 FastMambaformer 优于同配置 FastConformer。含噪 LibriSpeech：oTF-CrossNet+干净后端平均 WER 36.1%，优于 noisy-trained MCT（36.9%）；接预训练后端同样受益。CHiME-4 实测：oTF-CrossNet+干净后端 24.56% 优于 MCT 26.17%；大模型+前端可进一步降到约 13.7%。LibriCSS：弱前端 DPDFNet 可伤性能，oTF-CrossNet 降低重叠 WER（如干净后端 26.51→22.93%）。

## 结论
足够强的在线分离可使干净训练流式 ASR 超过 MCT，且前端/后端可独立升级，无需任务专用再训。

## 点评
把稳健性外包给模块化前端，避开“为噪声重训 ASR”的代价，对大预训练模型尤其实用。收益高度依赖前端质量（DPDFNet vs oTF-CrossNet 反差大）；全上下文离线 TF-CrossNet 仍明显更好，流式稳健仍是硬问题。


# Margin-Aware Contrastive Regularization for Robust Streaming Keyword Spotting under Strict False-Alarm Constraints

- 论文编号：3545
- 报告人：Hanwen Zhang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26ha_interspeech.pdf

## 问题
边缘流式 keyword spotting（KWS）需在严格 false-alarm（FA）预算下保持检测灵敏度。标准 CE 训练的轻量因果模型在 ≤0.5 FA/h 等严苛工作点上，面对语音相似 imposters 时 false rejection rate（FRR）显著恶化；直接对 Unknown 做全局对比聚类会扭曲异质非目标流形。

## 方法
提出 Margin-Aware Contrastive Regularization（MACR），仅作离线辅助目标：对因果 1D-CNN 的 penultimate embedding 做 ℓ2 归一化；intra-class pull 仅作用于目标关键词，分母也只含其他目标样本，避免全局聚类 Unknown/Silence。Margin-aware repulsion 对负样本施加 max(0, cos−m)，并对离线挖掘的 hard negatives（EMA 网络上非目标窗口中目标后验 top-K）加权 α>1。总损失 L_CE+λ L_MACR；部署时丢弃 MACR 分支，参数、MACs、算法时延与 CE 基线相同。

## 实验与结果
在 Google Speech Commands V2（12 类）上，约 150K 参数因果 1D-CNN，连续流事件级协议（50 条 2 小时测试流）。MACR 闭集准确率 95.68%（CE 95.82%）；FRR 在 0.5 FA/h 从 16.32%→7.64%，在 0.2 FA/h 从 29.85%→14.80%（相对降幅约 50%）。消融表明去掉 margin、hard-negative 加权或对 Unknown 全局聚类均使 FRR 变差。DS-CNN Tiny 与 BC-ResNet-1 上也有一致 FRR 下降；Raspberry Pi 4B 上推理时延与 CE 同为约 2.15 ms。

## 结论
MACR 通过目标紧致与 hard-imposter 几何边距改善严苛 FA 下的流式 FRR，且零部署开销。证据限于英文多关键词严格 FA 流式设定；更广语言、自定义唤醒词与远场场景留待后续。

## 点评
核心洞察是 Unknown 不是紧致类，对比学习必须把“目标紧致”与“imposter 边距”拆开；这比直接套 SupCon/ArcFace 更贴 always-on FA 约束。脆弱点在于 hard-negative 挖掘依赖 EMA 与合成流协议，真实自然录音与自定义唤醒词上的边距是否仍有效有待验证。


# Mitigating Causality Mismatch with Causal Temporal Relation Distillation for Streaming Keyword Spotting

- 论文编号：3546
- 报告人：Hanwen Zhang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26ia_interspeech.pdf

## 问题
端侧流式 KWS 要求严格因果、零 lookahead 学生模型；从非因果教师（如 AST）做中间层蒸馏时存在 causality mismatch：教师逐步特征已含未来上下文，点式回归会与学生可实现感受野冲突，损害连续长时推理鲁棒性。

## 方法
提出 Causal Temporal Relation Distillation：用无参 Adaptive Average Pooling 将师生时序特征对齐到统一长度 L（默认 24），行内 ℓ2 归一化后构造关系矩阵；对教师关系矩阵施加下三角因果掩码，只蒸馏历史拓扑（Ours）。离线双向变体 Ours-Bi 在保留 L_rel 历史锚点基础上，额外用全矩阵 L_bi 作 privileged prior。联合目标含 CE、logits KD、L_rel 与可选 L_bi；关系匹配仅离线计算，推理仍为因果 1D-CNN。

## 实验与结果
GSC v2 上，冻结 AudioSet 预训练 AST 教师（约 85M），学生约 150K/5.2M MACs。Scratch 95.12%，Vanilla KD 95.74%，Feature KD 95.45%，Relational KD 96.08%，Ours 96.53%，Ours-Bi 96.91%。流式 FRR@1.0 FA/h：Scratch 8.52%→Ours-Bi 4.15%。消融显示仅 L_bi 不如有因果锚点的组合；L=24 优于无 pooling 或过平滑的 L=12。Raspberry Pi 逐步时延约 0.15 ms，各学生变体部署成本相同。

## 结论
用因果可实现的时序拓扑蒸馏替代点式特征回归，可缓解 causality mismatch，并在闭集准确率与连续流 FRR 上取得最佳结果，且无额外部署开销。结论限于 GSC v2、AST→1D-CNN 设定。

## 点评
把“错在绝对特征含未来”转成“只对齐可实现的相对关系，再软用全拓扑”是清晰的因果蒸馏设计。强项是关系构造与推理解耦；风险在于依赖特定教师与合成流协议，且 L 的子音素尺度是否跨域通用需再验证。


# Retention-Preserving Gradient Projection with Entropy-Guided Token-Level Distillation for Rehearsal-Free Continual ASR

- 论文编号：2309
- 报告人：Seunghee Ma
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ma26d_interspeech.pdf

## 问题
大规模预训练 ASR（如 Whisper）顺序域适应时会发生灾难性遗忘；严格 rehearsal-free 设定下仅有上一模型参数可用。标准 LwF 对所有 token 等权蒸馏，不确定教师输出会污染保留方向，且监督梯度与蒸馏梯度冲突时会损害保留。

## 方法
以冻结上一模型作教师：用教师分布熵构造 token 级权重 λ_t，抬高低熵（自信）token、压低高熵 token，得到熵引导蒸馏损失。将蒸馏梯度视为 retention direction；当 cos(g_CE, g_distill)<0 时，用系数 η 投影掉监督梯度中与蒸馏方向冲突的分量。基于对角 Fisher 分析冻结 encoder、只微调 decoder。顺序适应 LIB→AMI→TED→SPG。

## 实验与结果
Whisper Large-v3，η=0.75。最终平均 WER 8.12%，相对 LwF decoder-only（8.75%）降 7.2%，相对 FT decoder-only 降 15.9%；BWT 从 LwF 的 −4.63 改善到 −2.82。无 replay 仍优于带 1h TED 缓冲的 GEM/ER。Common Voice 多语退化平均绝对增幅 0.95%，相对 LwF（1.96%）降 51.5%。消融显示投影主推保留与泛化，熵加权在投影下略恢复目标域适应；η 可调保留–适应折中。

## 结论
熵引导 token 蒸馏 + 保留投影 + encoder 冻结，在 rehearsal-free 连续 ASR 适应上优于 LwF，并更好保住多语能力。η 提供显式折中控制。

## 点评
把蒸馏梯度当作可投影的保留方向，比固定 λ 的 LwF 更贴近“冲突时该保什么”的优化问题。代价是投影会牺牲新域适应（AMI WER 上升），且依赖教师在当前域输入上的输出质量；Fisher 仅支撑 encoder 冻结假设，未与 LoRA 等 PEFT 路线直接对比。


# Parameter-Efficient Continual Learning for Automatic Speech Recognition

- 论文编号：3169
- 报告人：Steven Vander Eeckt
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/eeckt26_interspeech.pdf

## 问题
语音基础模型下游适应面临参数量大与顺序微调灾难性遗忘；ASR 上参数高效持续学习（PECL）研究相对 NLP/视觉更少，且不少方法未显式保护相对初始预训练模型的性能。

## 方法
提出 Continual SSVD（CSSVD）：对线性层权重做 SVD，按奇异值分为 head（高能）与 tail（低能）；只在 tail 学习近似旋转 G=I−2K（省略显式 rescaling）。新任务前重算 SVD 以更新 head/tail 划分；多任务时用权重平均（α=1/(i+1)）合并当前解与新任务适应解，保护主导方向并降低共享 tail 内干扰。推理无需任务 ID。

## 实验与结果
OWSM v3.2 small（约 366.7M），约 8.9M 可训参数。实验 1：预训练语 ENG/DEU/ESP 为 T0，再适应 CGN 的 NL→VL；CSSVD 平均 WER 18.33、BWT −1.9，显著优于 LoRA、SSVD、OPLoRA、MiLoRA、BiLoRA、EWC-LoRA、LoRA+FTA 等。实验 2：VL→方言 DVL，CSSVD 平均 24.82、BWT −2.2，仍最佳。消融表明限制在 bottom-k 方向最关键，平均步骤必要，显式 rescaling 几乎无增益。

## 结论
在尾空间做近似旋转并跨任务平均，可在 ASR PECL 上同时降低遗忘与平均 WER。局限是各层均匀分配适应容量，未来可按层选择性分配。

## 点评
相对“改 top-k”（SSVD）改为“只动低能尾并平均”，直接对准保护预训练主方向；实验覆盖多类从 NLP/视觉迁来的 PECL 基线，证据较全。脆弱处在于困难方言任务上新任务 WER 仍高于无正则 LoRA，且 head/tail 重划分依赖每任务后完整 SVD。


# MoDiCoL: A Modular Diagnostic Continual Learning Dataset for Robust Speech Recognition

- 论文编号：2111
- 报告人：Theresa Pekarek Rosin
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pekarekrosin26_interspeech.pdf

## 问题
现有 ASR 鲁棒性数据集/基准常孤立考察噪声、口音或障碍等因素，难以反映真实共现与随时间累积的分布漂移；也缺少用持续学习诊断预训练 ASR 在何处遗忘的可控资源。

## 方法
发布 MoDiCoL：用 Taguchi L27 正交阵与 foldover 得 108 种因子配置×75 样本=8100 条（约 18.79 h，其中合成 14.08 h）。三因子族为语言内容（域/风格）、说话人（年龄/口音/健康/停顿/不流畅）、声学环境（噪声类型/SNR/距离）。真实与 XTTS-v2 合成语音经去噪、不流畅/损伤/停顿、混响距离与噪声注入管线对齐配置。CL 课程：t0=LibriSpeech 控制设定，再依次 Acoustic、Speaker、Linguistic、Compound 漂移；评估 ER、RLR、OGD 三种策略（whisper-small.en，online/streaming）。

## 实验与结果
未适应时 t0 A-WER 7.42，t1/t2/t3 分别升至 47.62/87.28/141.73，t4 为 43.37；合成子集整体好于真实。课程上 ER-10% 最稳：A-WER 17.31±0.48，优于 JOINT（27.24）与 FT（34.14），FM 接近 0；RLR 遗忘大，OGD 的 AI-WER 最好（21.19）且任务梯度近正交。顺序引入漂移提升可塑性，但除 ER-10% 外 FM/BWT 方差大，任务顺序敏感。

## 结论
MoDiCoL 支持对多因子漂移下 ASR 适应与遗忘做诊断；适度 replay 最利于跨漂移保持鲁棒性，梯度子空间干扰是遗忘因素之一。数据与管线已放 Hugging Face。

## 点评
价值在“可控共现因子 + CL 课程当诊断工具”，而非再堆单一噪声/口音集。合成占比高、部分配置靠损伤仿真，外推到真实共现分布时需谨慎；ER 优于 JOINT 的结果有启发，但强依赖缓冲与任务顺序。


# SCOLoRA: Similarity Conditioned Signed Orthogonal LoRA for Continual Speaker Adaptation

- 论文编号：3243
- 报告人：Ye-Eun Ko
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ko26b_interspeech.pdf

## 问题
部署 ASR 面临说话人流式到达、无可回顾历史数据的 rehearsal-free 持续说话人适应；O-LoRA 等任务无关正交分离可抑干扰，但会阻断声学相近说话人之间的正迁移。

## 方法
提出 SCOLoRA：每说话人学新 LoRA 分支并合并进骨干；用 ECAPA-TDNN 嵌入余弦相似度 S_{i,t}，经 sigmoid 先验与轻量 router 映射为有符号系数 λ(S)：相似时 λ<0 鼓励子空间对齐，不相似时 λ>0 强制正交。对 LoRA 基做单位 Frobenius 投影以稳定有符号重叠目标。总损失为 ASR 损失 + Σ λ(S)∥A_i^⊤ A_t∥_F²。

## 实验与结果
Whisper small + LoRA（r=4）于 TEDLIUM2/3 与 CHiME3。TEDLIUM3 上 SCOLoRA 测试平均 WER 4.11%、dev 4.41%、forgetting 0.05，优于 SeqLoRA（4.35/0.10）、O-LoRA（4.33/0.19）及 EWC/L2P/InfLoRA/GainLoRA。跨库一致改进；CHiME3 平均 WER 22.59（SeqLoRA 29.32，O-LoRA 28.09）。消融显示有符号加权与 router 优于仅正向相似度条件，对 τ∈{0.20,0.25} 不敏感。

## 结论
按说话人相似度调节对齐/分离，可在无回放持续说话人适应中同时降低 WER 与遗忘。

## 点评
把 O-LoRA 的硬正交改成相似度调制的有符号正则，切中说话人流“有的该共享、有的该隔离”。依赖说话人编码器质量与合并后单模型容量；长流上存储全部历史 A 基的开销与干扰累积正文未充分展开。


# Mixture of Phonetic Experts Based Low-Rank Adaptation of Conformer Models for Accented English Speech Recognition

- 论文编号：322
- 报告人：Anmol Guragain
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dahal26_interspeech.pdf

## 问题
口音英语 ASR 性能易降；按口音分配 MoE/适配器会使专家数随口音增长，且忽略口音差异常体现为系统的音素实现扭曲这一共享结构。

## 方法
提出 MoPE-LoRA：固定 6 个按发音方式划分的 LoRA 专家（元音、塞音、擦音、塞擦音、鼻音、流音/滑音），插入 Conformer 自注意力 Q/K/V。帧级混合路由：冻结音素 CTC（LibriSpeech 训练）提供监督硬分配，与可学习门控混合（β），top-2 激活。专家跨口音共享，测试无需口音标签。辅助 load-balancing 与 router Z-loss；主损失 CTC。

## 实验与结果
L2-ARCTIC（约 24 h，6 口音），说话人与句子双重 disjoint。NeMo Conformer CTC Small。最佳 MoPE-QKV（层 6–16）WER 10.43%，优于 Full FT 12.80%、Single LoRA-QKV 11.33%、MAS-LoRA 11.77%。零样本留一口音：平均 WER 9.98%，相对 Single LoRA（11.38%）相对改进 12.3%。TIMIT MI/t-SNE 支持中层最富音素信息，故聚焦 6–16 层；跨域音素 top-1 仅 36.04%，故用 top-2 补偿。

## 结论
按音素范畴分解适配、混合路由，可在固定专家数下提升多口音与未见口音识别，且参数高效。

## 点评
用发音方式归纳口音变异，比“一口音一专家”更可扩展；音素监督在口音上不准时靠学习门控补偿是务实设计。边界在于依赖额外音素模型与英语发音学分类，对更强口音或非英语音系的迁移仍需验证。


# First-to-Spike: An Early-Exit Framework for Rapid and Energy-Efficient Spiking Neural Networks

- 论文编号：1858
- 报告人：Siqi Cai
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26j_interspeech.pdf

## 问题
SNN 本具事件驱动低时延潜力，但常跑满整段序列；现有 early-exit 多用 softmax 置信阈值等非脉冲准则，偏离纯事件范式并增加部署复杂度。

## 方法
提出 First-to-Spike（F2S）：输出层每类一个 LIF 神经元，首个发放脉冲的类即为预测并立即停算；无脉冲则回退到最终膜电位 argmax。加入可学习侧向抑制 WTA 电路加速竞争。Hybrid Temporal Training（HTT）含加权 TET 分类损失、时间间隔 margin 损失与正确类发放时刻效率正则。

## 实验与结果
GSC V2：F2S Acc 92.89%、ADT 63.68、能耗 2.75 µJ，优于 ED-sKWS（90.14%/66.07/2.85 µJ）。SEED：79.35% Acc、ADT 3.06；SEED-IV：71.60%、ADT 5.45，均高于 Sparch 与 ED-sKWS 且更低时延。消融：仅 F2S 规则已有 early-exit；WTA 大幅提准，HTT 进一步降 ADT，二者合用最佳。

## 结论
脉冲本身可作为可靠决策信号；F2S+WTA+HTT 在语音指令与 EEG 情感识别上同时提升准确率并降低时延/能耗。未来需考察 SNR 鲁棒性及与异步神经形态传感器耦合。

## 点评
把 early-exit 内化为输出层“赛跑发脉冲”，比外挂置信阈值更贴 SNN 硬件。强项是跨语音与 EEG 一致；脆弱点包括无脉冲回退仍依赖满时序、以及能耗按 CMOS MAC/AC 估算，真实神经形态芯片开销可能不同。


# A light weight Continuous Speaker Verification System for Real time Monitoring

- 论文编号：3584
- 报告人：Harish Rajamani
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/keetha26b_interspeech.pdf

## 问题
电话客服、银行与医保等场景需要在通话全程持续核验客户身份，防止交接、冒充或盗用设备后泄露敏感信息。传统系统多为通话开头一次性认证，无法实时监测说话人变化；同时需满足低延迟、抗噪声混响与跨语言/语码转换的稳健性。

## 方法
演示级连续说话人验证（CSV）系统：客户侧按用户名取注册声纹或短段现场注册，开头验证失败三次则回退密码；通过后转座席，座席界面持续显示验证状态。流式处理用 1 s 窗、0.5 s 跳，经 VAD、嵌入提取与对注册声纹的余弦相似度打分，约每 500 ms 更新决策；不匹配持续约 3 s 则告警并可终止通话。模型为两阶段：Stage 1 用 ReDimNet-B1 在 log-mel 上做多语说话人分类（margin loss，含噪声/混响/变速增强）；Stage 2 冻结骨干，用轻量卷积投影网络与含同语/跨语对的 triplet 采样，得到更可分、语言不变的 256 维嵌入。

## 实验与结果
在 TidyVoice（约 457 小时多语）上训练增强（SNR 5–20 dB，RT60 0.2–0.8 s，速度 0.9/1.1）。系统在 Intel Core i7-8650U 上处理 1 s 音频约 50 ms，RTF=0.05；总约 2.5M 参数、318 M MAC/s（骨干 2.2M / 290 M MAC/s，投影约 256K / 27.36 M MAC/s）。在 TidyVoice 评估/开发集上 EER=2.08%。

## 结论
作者认为该两阶段轻量模型可学习稳健、语言不变的说话人表征，在实时 RTF 与低算力下完成连续验证与座席告警，适用于电话类安全场景并可扩展到其他应用。

## 点评
工作偏系统演示：把 CSV 接到座席告警闭环，并用两阶段（分类预训练 + 跨语 triplet 投影）压低算力。指标与效率数字清楚，但正文对公开基准对比、误报/漏报业务代价及更复杂噪声信道的系统评测着墨有限，EER 主要来自自有 TidyVoice，跨域泛化仍需外部验证。


# WaveNorm: A Low-Complexity Time-Domain Neural Adaptive Gain Control for Real-Time Speech Applications

- 论文编号：3588
- 报告人：Harish Rajamani
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ijjada26b_interspeech.pdf

## 问题
真实语音电平因距离、房间与设备大幅波动，损害 ASR、会议与助听；传统 AGC（如 WebRTC）靠包络与固定 attack/release，难区分语音/噪声，易延迟、削波或放大背景噪声；频域学习方法又增加延迟，不利于边缘实时。

## 方法
WaveNorm AGC 全时域、因果：20 ms 帧、10 ms 移。编码器为堆叠因果 Conv1D（核 3，dilation 2/4/8）+ grouped convolution + BN/PReLU，建模多尺度幅度与包络；瓶颈为 hidden 32 的 GRU 与 32 维全连接，保证增益平滑；解码器用转置 Conv1D 镜像上采样，端到端映射波形，隐式完成归一化与降噪，不显式输出增益系数。感受野约 27 样本（~0.56 ms）。损失为 0.5 MSE + 0.5 多分辨率谱损失（STFT 128–2048）；Adam 1e-3，200 epoch。

## 实验与结果
内部 48 kHz 语料 + DNS3：RMS −10 至 −70 dB，噪声 SNR −5 至 +20 dB。独立 AGC：在 VoiceBank+DEMAND 衰减与 TIMIT 放大设定下，相对 WebRTC、Carnival 更电平不变、增益更平滑，约 6 dB 降噪，Active Speech Level 近 −26 dBov，响度 −26 至 −28 LUFS，符合 ITU-T P.56/P.79。作前端时，在 DeepFilterNet2、DTLN、GTCRN 上最高约 +0.35 NISQA。模型 49 M MACs、55 KB 内存。

## 结论
WaveNorm 以极低时延与很小算存实现宽动态（至 −70 dB）稳定响度归一化，并在噪声下约 6 dB 降噪，避免传统 AGC 的削波与噪声放大，适合会议与边缘实时语音。

## 点评
把 AGC 做成时域端到端“内容感知电平映射”，用 GRU 约束增益平滑，是对规则包络跟踪的直接替代，而非再堆一套频域增强。数字披露偏概括（对比多为定性+少量 NISQA），对极端非平稳噪声与说话人切换时的 pumping 风险仍需更多公开对比表支撑；优势主要在边缘算力与标准响度合规。


# Argmax Pro: Frontier-level Real-time Speech-to-text with Speakers and Custom Vocabulary on Mobile Devices

- 论文编号：3602
- 报告人：Atila Orhon
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/angus26_interspeech.pdf

## 问题
云端 ASR 在延迟可靠性、可用性、按分钟计费与隐私上受限，而首代端侧实时系统常缺说话人分离、自定义词表等能力，或在实时模式下牺牲精度，难以成为云端的对等替代。

## 方法
Argmax Pro 在 iOS/Android 上编排三个十亿级 Transformer：Parakeet v2 做语音转写，采用可自纠错的流式推理（interim/final 词），使预录与实时输入精度对齐；Canary v2 CTC 配合 CTC-WS 做上下文偏置/自定义词表，可扩至约 3000 词且不拖累端侧延迟；Streaming Sortformer v2 经 FastMSS 合成数据微调，增强对真实声学、音量与背景噪声的稳健流式说话人分离。推理分别落在 Apple Neural Engine、高通/联发科 NPU 与 Google Tensor TPU，以控制续航、发热与与其他 App 的资源争用。

## 实验与结果
正文以系统描述为主，定量结果多指向相关工作：关键词（尤其人名/公司/产品）精度在 Contextual Earnings-22 等分析中达 frontier 水平；自定义词表规模相对多数云平台（常 <500）扩展到 3000。本文未给出完整独立 WER/DER 表格。

## 结论
作者认为该统一实时系统可在广泛移动设备上提供带说话人与自定义词表的近云端级端侧 STT，作为 feature-rich 云端方案的对等替代。

## 点评
这是工程集成型演示：把流式纠错 ASR、大词表偏置与稳健流式 diarization 绑到 NPU 上，解决“端侧功能不全或实时掉精度”的产品缺口。方法细节依赖引用论文，本文本身缺少自包含的对照实验数字，评估边界需结合配套基准工作理解。


# A Human-in-the-Loop Multi-Agent Companion for Real-Time Entity Extraction and SLU-Driven ASR Error Correction

- 论文编号：3610
- 报告人：Shiva Shankar Arumugam
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/arumugam26_interspeech.pdf

## 问题
联络中心通话密集包含客户名、账号、SKU、药名等命名实体，流式 ASR 易错，错误会传到 agent companion 界面，造成 CRM 错录与返工。人工在 UI 上的实体纠正本是高质量监督，却很少回灌到 ASR/抽取栈；且通常不能预先备好完整实体表，也不宜做声学重训。

## 方法
演示 MACE（Multi-Agent Companion Environment）闭环：ASR（带偏置列表 B）→ 词替规则 R → 抽取子代理 → companion UI 建议；reflection 子代理在音频路径外消费 UI 纠正 Δ，将误识/漏抽实体写入 B，对跨对话复发（阈值 τ）的误识模式生成替换规则 R。按对话批更新，B/R 存 KV、按 agent 作用域隔离；不改声学模型。实验用 ContextASR-Bench 英对话子集、Whisper-large-v3，确定性代理抽取器 + oracle 编辑器模拟人在环，K=100 批、τ=2，|B|≤500、|R|≤200。

## 实验与结果
相对无偏置基线，MACE Adaptive 将 NE-WER 从 0.178 降至 0.147（约 −17.1%），EditRate 从 0.304 降至 0.247（约 −18.6%），分别闭合至 oracle 偏置差距的 23.6% / 22.0%；32 批配对 bootstrap 的 95% CI 与基线不重叠。|B| 约在第 3 批饱和至 500，|R| 约第 28 批饱和至 200。

## 结论
作者认为把 companion UI 纠正闭环回写成偏置与替换规则，可在无先验实体表、无声学重训下持续降低实体错误与人工编辑率，并向 oracle 偏置靠拢。

## 点评
抓的是“人在环纠正→上下文偏置/后处理规则”的运营反馈回路，多智能体分工让更新离线于实时转写路径，工程上很贴联络中心。评测用 oracle 编辑与代理抽取，真实 LLM 抽取与真人编辑噪声下的增益可能打折；B/R 容量封顶后增益饱和，跨租户/跨域迁移也依赖作用域隔离设计。


# AppTek Call-Center Dialogues: A Multi-Accent Long-Form Benchmark for English ASR

- 论文编号：2047
- 报告人：Eugen Beck
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/beck26_interspeech.pdf

## 问题
公开英语 ASR 基准多为短切分、朗读/准备语料，且缺少显式方言标注，难以评估对话式、长时、多口音场景；大型开源模型还可能污染公开测试集。呼叫中心类应用尤其需要自发交互、命名实体与领域词汇下的稳健评测。

## 方法
发布 **AppTek Call-Center Dialogues** 评测语料（非训练用）：角色扮演的 agent–customer 对话，覆盖 14 种英语口音、16 类服务场景；专业人工逐字转写（含犹豫、截断等标记）与多轮 QA；另有约 5 小时译成中/德/日/西供 IWSLT 盲测。对多种开源 ASR，在人工切分、AppTek 切分、Silero VAD、固定 30s/60s 切分下按会话聚合 WER 评测。

## 实验与结果
规模：128.6 小时、156 说话人、873 通话、约每口音 8–11 小时。多数模型人工切分 WER 最低；Qwen3-ASR 在 60s 固定切分上更优。Silero 设置下口音间差距大，en SG/CN/GB SCT/IN 普遍偏高，en AU/US General 偏低；强弱口音差距常超 10% 绝对，且平均 WER 好不意味着口音稳健性好。无外部切分时仅少数模型可用。

## 结论
该语料从零采集、未用公开网页材料，便于可复现的长时对话与口音评测；边界检测与口音多样性仍是开放问题，平均准确率提升不能自动转化为口音稳健性。

## 点评
贡献主要在「干净评测基准」：新数据、口音标签、切分消融协议三位一体，对 conversational AI 部署很有针对性。局限也写得很清楚——角色扮演非真实通话、性别不平衡、口音自报+离散标签、无正式 IAA——解读结果时需按「所代表说话人样本」而非整口音社群。


# Segmental Attention Decoding With Long Form Acoustic Encodings

- 论文编号：341
- 报告人：Xinwei Li
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/swietojanski26_interspeech.pdf

## 问题
AED 在分段语料上训练时，交叉注意力会利用段边界「残缺上下文」作隐式绝对位置锚点；长时流式编码（LFE）消除这些边界线索后，因 key/value 置换不变性无法排序声学编码，表现为重复转写、难以发 EOS，自回归注意力解码崩溃。

## 方法
四项修改：
1. **交叉注意力绝对位置编码**：对每段 \(H_s\) 加段内复位的位置码，再进 cross-attention。
2. **声学上下文扩展 (AC)**：训练时为 LF 样本左右扩上下文，使段内编码成为真 LFE，但不对损失使用两侧无效帧。
3. **段拼接 (SC)**：拼接连续段与非语音邻域，丰富时长与 LFE 暴露。
4. **语义切分 (SS)**：CTC 头预测语义句界 token，触发二遍 AD，优于纯 VAD。

模型为 CTC-AED（Ours.base ~90M / Ours.small ~240M），编码器因果 Conformer + 可变 chunk，解码器固定约 18M。

## 实验与结果
TED-LIUM3 消融：基线 LFE 上纯 AD WER 达 295%；SC+AC+PE 后 AD 与 SFE 持平（约 5.0%）；加 SS 后 CTC-Att 达 4.3%。最终：Ours.small CAT@3.84s 在 Tedlium3 LF 3.9%、Earnings21 11.4%，短切分任务也不退化；相对同量级 Whisper 延迟更低、多数集合更优（部分集合作者注明非零样本）。

## 结论
AC 与段级 PE 互补，可关闭连续编码与分段编码的精度差距，使注意力解码器可对长时编码自回归使用；CTC 语义切分优于 VAD，混合 CTC-Att 更稳。

## 点评
问题诊断很扎实：把长时失败归因到「边界捷径消失 + 置换不变」，对策也对准这两点。强在系统消融清晰、部署上保留流式编码器与轻量解码器；脆弱点是强依赖训练侧 AC/SC 数据改造，且对伪标签 SpeechCrawl 质量敏感，语义 seg 标签本身也引入外部 Segment any Text 管线。


# M-LAMA: Multimodal Automated Scoring of Long-form Spoken English

- 论文编号：1542
- 报告人：Minh Dao-Xuan-Quang
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/daoxuanquang26_interspeech.pdf

## 问题
真实口语考试需对多分钟自发回答做发音、流利、词汇、语法、语篇等多维评分，但既有工作多聚焦短句或发音；公开数据也缺乏长时、多标准熟练度标注。通用音频语言模型对细粒度发音/韵律与钟形分数分布不够适配。

## 方法
提出 **M-LAMA**：双流编码 + 语篇感知融合。
- 音频：冻结 Whisper-Large + bottleneck adapter；3–5 分钟回答切成 30s chunk，按考试三部分分层注意力池化并加位置嵌入。
- 文本：冻结 Qwen2-1.5B 编码转写与题目；题目条件交叉注意力评估任务完成度；双向 audio↔text 注意力与门控融合（含双线性交互），输出 0–10（0.5 步）21-bin 期望分数。
- 训练三阶段：对比对齐 → 粗档分类（低/中/高）→ MAE+Focal 细粒度回归，缓解中档主导。

## 实验与结果
数据：约 86,491 场、29,034 考生、~4,845 小时（按考生切分防泄漏；因保密不可公开）。全测集上 Multi-stage 相对最强开源基线（Qwen-2.5 Omni）五维 MAE 约降 15–29%、QWK/Acc@1 全面提升；相对 GPT-4o Audio 等 API（1k 子集）亦明显更好。消融：Text+Audio Acc@1 90.82% 远高于单模态；去题目模块伤语篇管理；单阶段训练明显弱于多阶段。chunk 留一分析显示前部段贡献更大但仍全局聚合。

## 结论
长时口语评分需要结构化多模态对齐（声学交付 + 语言内容 + 题目语境）与分布感知训练；M-LAMA 在五维标准上显著提升可靠性。代码与检查点公开，数据可按申请分享。

## 点评
把评分量表拆到架构组件（部分结构、题目条件、双向融合）和「先对齐再分档再回归」的三阶段优化，针对考试分数钟形分布很对症。强在大样本机构数据与完整消融；主要风险是数据不可公开、依赖 Whisper/Qwen 冻结表征，以及商业 API 只在 1k 子集对比，外推需谨慎。


# Attentive Mamba: Channel-wise Local Attention for Speech Recognition

- 论文编号：1708
- 报告人：Jen-Tzung Chien
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/chien26_interspeech.pdf

## 问题
Transformer 自注意力全局建模强但 \(O(T^2)\) 且局部细粒度不足；Mamba 等 SSM 线性复杂度、擅长长程，但局部聚合依赖**静态**深度卷积，缺乏内容自适应。希望在保持 SSM 全局状态建模的同时，为局部特征引入动态注意力。

## 方法
提出 **Attentive Mamba (attMamba)**：用**通道维局部注意力**替换 Mamba2 中的静态因果卷积。
1. 对各通道用因果深度卷积上下文化生成 \(q,k,v\)（而非逐时刻线性投影）。
2. 在因果局部窗口 \(w\) 上做跨通道点积注意力，得到内容感知局部摘要 \(u_t\)。
3. 用 \(u_t\) 动态参数化 SSM 状态转移 \(A,B,C\)。
编码器为双向 attMamba；训练可联合 CTC 与 AED，并可加 4-gram LM 重打分。

## 实验与结果
LibriSpeech 960h：attMamba-CTC (S, 21.2M) test-clean/other 6.24/12.31，优于同配置 conformer-CTC (S, 30.0M) 的 6.59/12.57。TED-LIUM3：S/L 上均优于 conformer；attMamba+lm-CTC+AED (L) test 4.98。消融：双向相对单向 Mamba2 大幅降错；再换通道注意力进一步改善。进阶 CTC+AED+LM 下 attMamba+lm 达 test-clean/other 2.73/6.02，优于同设置 conformer 与若干自监督基线。特征图显示通道注意力使各通道时间轴更均匀，体现通道级动态调制。

## 结论
把静态卷积局部聚合换成卷积上下文化的通道维局部注意力，可增强 SSM 状态参数化，在更小参数量下于朗读与自发语音 ASR 上低于 conformer/Mamba2。

## 点评
抓的是 Mamba「时间混合强、局部聚合钝」的瓶颈，设计贴合频谱「通道内时域相干、再跨通道融合」的结构先验。强在参数更少且消融干净；脆弱点在窗口 \(w=4\) 等超参敏感、双向实现偏离严格因果流式，以及与更强预训练编码器对比时收益边界仍待更大尺度验证。


# Attention-Guided Reliability Scaling for Contrastive Decoding in Robust Audio-Visual Speech Recognition

- 论文编号：929
- 报告人：Da-Hee Yang
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/kim26h_interspeech.pdf

## 问题
LLM 系 AVSR 在噪声下仍可能过度依赖受损音频。对比解码（Expert=音视频、Amateur=仅音频）无需训练即可削弱声学偏置，但固定对比强度会在强噪声与干净条件间权衡：强干预利于低 SNR，却可能在干净语音上过纠。

## 方法
在同一 LLM-AVSR 上做训练无关对比解码，用 token 级软门控 \(w_t\) 缩放有效强度 \(\lambda_{\mathrm{eff}}^{(t)}=w_t\lambda\)。\(w_t\) 为三项乘积（保守激活）：
- **相对音频能量 \(E_t\)**：末层末 token 对音频区注意力相对本句运行均值；
- **音频熵 \(H_t\)**：音频区注意力分散度（按头独立算再平均）；
- **JS 散度**：Expert/Amateur 预测分歧，经高斯「甜区」滤波（\(\mu_{\mathrm{sweet}}=0.35\)）抑制过同或过崩塌分歧（防 rank distortion）。

## 实验与结果
LRS3 训练，MUSAN 噪声注入到 0/−5/−10/−15 dB；OOD 到 LRS2。在 Llama-AVSR(8B)、Omni(1B)、Qwen(0.5B) 上相对 AV 基线平均相对改进约 5–10%；干净与噪声均有收益。固定 \(\lambda\) 最优值随 SNR 变化；自适应在各条件更均衡。消融显示 JS 偏稳干净/轻噪，\(E_t/H_t\) 偏助重噪。延迟约 +8.6%。

## 结论
基于注意力与预测分歧的可靠性缩放，可在不改参数的前提下同时改善干净与强噪声 AVSR，避免固定 CD 的鲁棒–干净权衡。

## 点评
把「何时该压音频偏置」做成可观测门控，比一刀切 \(\lambda\) 更贴 SNR 波动。强在即插即用、跨模型尺度可迁移；脆弱点是依赖特定拼接布局提取音频索引、门控超参仍需验证集调，且极端 JS 崩塌时对比项本身就不稳定。


# Listening with Attention: Entropy-Guided Explainability for Transformer-Based Audio Models

- 论文编号：593
- 报告人：Ravi Kumar
- 程序：Thursday 1 October 2026 / Long-form Audio & New Attention Approaches
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26_interspeech.pdf

## 问题
Whisper 等 Transformer ASR 精度高但难解释；LIME/SHAP/IG 等事后解释对语音时序不友好，常不忠实且时间定位粗糙。需要与模型内部计算一致、并对齐到解码 token 的时域归因。

## 方法
LEAF-X：对每个解码 token 产生帧级归因。对 cross-attention（或 decoder-only 中指向音频伪 token 的注意力）算头熵，低熵头获更高权重并层内聚合；再用多层 attention rollout 累积证据；可用梯度调制压制对 token 概率影响小的注意力；可选按层消融 cross-attention 造成的 NLL 上升作因果重加权。输出归一化 token-to-frame 分布，映射回波形时间轴。适用于 Whisper 与 speech-augmented decoder-only（如 Canary-Qwen）。

## 实验与结果
模型：Whisper-large-v3（LibriSpeech）、Canary-Qwen-2.5B（TED-LIUM 3）。指标（归一化）：D-AOPC↓、TLoc↑、SPR↑、STAB↑、INF↓。Whisper：LEAF-X 为 0.45 / 0.72 / 0.70 / 0.78 / 0.45，全面优于多数基线，TLoc 略低于 SaCo（0.73）。Canary：0.48 / 0.70 / 0.68 / 0.76 / 0.47。消融显示去掉熵加权或 rollout 损害最大；insertion/deletion 曲线支持更高忠实度。作者强调指标为代理，非人类可信证明。

## 结论
LEAF-X 用熵引导头选择、多层 rollout 与轻量因果重加权，为 Transformer ASR 提供更忠实、稀疏且稳定的 token–时间归因，利于高风险场景下的可审计分析；局限含骨干/数据/语言覆盖、校准敏感、缺用户研究等。

## 点评
核心是把“哪些帧支持这个词”建成模型内禀流程，用低熵注意力过滤弥散头，比纯扰动或原注意力更贴计算路径。因果层消融有额外前向开销，可关掉；解释质量仍绑定注意力机制假设，对噪声域移与非注意力主导错误模式可能脆弱。


# How Linguistic Dimension Interactions Shape Meaning Preservation in Multilingual ASR

- 论文编号：920
- 报告人：Simon Gonzalez
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/gonzalez26c_interspeech.pdf

## 问题
多语 ASR 替换错误对语义保持的影响难以用 WER 刻画；先前多用 WALS 等语言层类型学代理，不清楚从 ASR 输出直接量测的音系/形态/句法/词汇特征如何交互、是否因架构而异。

## 方法
在 FLEURS 42 语、>154 小时上跑 Whisper 与 Seamless；仅分析对齐后的替换错误。因变量为句级语义相似度 SENT（paraphrase-multilingual-MiniLM）；自变量为词级 PHN（phonemizer+Levenshtein）、MOR/SYN（Stanza POS/依存差）、SEM（fastText）。用 glmmTMB 混合效应 beta 回归，分阶段加入维度交互、ASR 三阶交互与语言效应。

## 实验与结果
主效应均显著：PHN 负向最强（β=-0.31），SEM 正向最强（β=0.84）。交互模型显著改进拟合；最强为 MOR:SYN（χ²=165 量级改进中 χ²=113）。Seamless 基线更好（Whisper β=-0.20）；Whisper 对 PHN/SEM/SYN 退化更敏感，但更会利用形态保持。语言随机效应差异大（如越南语维度强但句级一般，捷克语音系差但句级可补偿，乌尔都语句级最差）。

## 结论
句级语义保持来自跨维度系统交互而非孤立错误；Whisper 与 Seamless 以不同机制整合语言学信息；类型学差异导致不同错误剖面，多维框架比聚合准确率更有信息量。

## 点评
把评价从 WER 拉到“意义是否保住”，并对架构做交互建模，对多语部署诊断有价值。仅替换错误、依赖 Stanza/phonemizer/嵌入工具链，插入删除与工具误差会偏置结论；属分析研究，未给出可直接落地的纠错或训练改法。


# Language-Aware Distillation for Multilingual Instruction-Following Speech LLMs with ASR-Only Supervision

- 论文编号：2446
- 报告人：Shreyas Gopal
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/gopal26_interspeech.pdf

## 问题
用 ASR 配对数据做上下文蒸馏可训英语 Speech LLM，但多语共用静态 Q-Former query 易语言干扰，低资源语被主导语淹没；大规模任务 SFT 又昂贵。

## 方法
冻结 Whisper-large-v3 编码器与 Llama-SEA-LION-v3-8B-IT；可训 Q-Former + 语言感知模块：query bank（每语一组）与门控网络（卷积 LID 或注意力池化），对输入语音做 soft 混合或 hard 选择（STE）；调度教师强迫稳定早期门控。损失：输入蒸馏（音频尾嵌入对齐文本头）、输出蒸馏（LLM 末隐状态对齐）+ LID CE。仅用约 5.8K 小时多语 ASR 数据。

## 实验与结果
相对匹配多语基线 ML-DiVA：开放指令跟随平均约 +14%（hard-gating；印尼 3.04→3.71）。自建 Audio-MLQA 上相对既有 Speech LLM 基线约 +32%；相对 ML-DiVA 闭集平均约 +3%（3.96 vs 3.85）。消融：L=256 显著降蒸馏损失；硬选择优于软混合；两种门控 LID 准确率均 >94.9%。

## 结论
语言感知 query 路由可在 ASR-only、骨干冻结条件下缓解多语干扰，高效扩展指令跟随与口语 QA；并释放多语评测数据。

## 点评
在 DiVA 式蒸馏上加 LID 门控，用最小可训容量打多语，工程上很实用。评测依赖 GPT-4.1 与 TTS 合成问句，与真实口音/噪声分布有差距；中文相对最弱、与主导语差异大，说明 bank 规模与数据配比仍是瓶颈。


# ERM-MinMaxGAP: Benchmarking and Mitigating Gender Bias in Multilingual Multimodal Speech-LLM Emotion Recognition

- 论文编号：3143
- 报告人：Zi Haur Pang
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/pang26b_interspeech.pdf

## 问题
Speech LLM 做多语多模态 SER 时，性别表现差距如何随语言与模态变化尚缺系统基准；多模态融合不保证更公平。

## 方法
在 MELD-ST（英/日/德，人工标注说话人性别）上基准多种 Speech LLM。提出 ERM-MinMaxGAP：LoRA 微调 Qwen2-Audio，主损失为交叉熵 ERM；正则 R=（各语言内男女损失差的最大值）^p（主设 p=2）；λ 按验证集性别差距相对阈值 ε 用投影梯度式自适应升降。评估单模态（仅语音）与多模态（语音+真值转写）。

## 实验与结果
多语设定相对最强基线：单模态 W-F1/ACC 约 +5.5/+9.8，多模态约 +5.0/+3.6；整体性别 AVG 差距分别降约 0.1 与 1.4 量级（摘要称 0.1%/1.4%），多模态下 AVG 再降 0.80。偏差强依赖语言与模型；多模态常提准确率但不稳定缩小性别差。消融：固定大 λ 可压差距但伤 SER；自适应 λ 在性能–公平折中更优；p=2 较 p=1 更利于公平。

## 结论
给出多语多模态 Speech-LLM SER 性别偏差基准，并表明惩罚最差语言内性别损失差可同时提升识别与公平折中。

## 点评
把“最差语言间隙”作为优化目标，避免平均公平掩盖某一语的极端偏差，适合多语部署。性别为人工标注、模态用金标转写，真实 ASR 转写误差下的公平性未测；固定大 λ 的效用–公平权衡表明超参仍关键。


# Confidence-Gated Mean-Teacher Consistency Regularization for Low-Resource Multilingual ASR with Shared–Private Fusion-LoRA

- 论文编号：1183
- 报告人：Jie Liu
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/liu26h_interspeech.pdf

## 问题
低资源多语 ASR 联合训练中，共享 LoRA 子空间易负迁移；一致性/自训练在预测不可靠时会放大确认偏置与跨视图不稳。

## 方法
冻结 Whisper-small，用 SPF-LoRA：共享分支学跨语共性、每语私有分支建模特异分布，可学习门控 β_ℓ 融合。训练上用 MT-CR：仅对可训适配器做 EMA 教师；双增强视图上学生 CE + 教师置信度门控（c_t>τ）的 KL 一致性；两阶段先监督训 SPF，再升温 λ、收紧 τ。

## 实验与结果
Kathbath 五语（gu/hi/mr/pa/ur）。SPF-LoRA 宏平均 WER 23.93%，加 MT-CR 至 19.85%，优于 small+LoRA（30.73%）与 medium+LoRA（22.46%）；Gujarati 38.86%→25.04%。消融：可学习融合优于纯共享/纯私有/固定求和；置信度门控是 MT-CR 关键；注入范围扩至 qkvofc 最佳。相对 LoRA 五语 CER 均下降。

## 结论
共享–私有 Fusion-LoRA 加置信度门控 Mean-Teacher，可在冻结骨干的参数高效设定下缓解负迁移并提升低资源多语 ASR。

## 点评
把“容量竞争”拆到私有 LoRA、用门控过滤不可靠一致性，针对性强。实验限于印欧系五语与 Whisper-small；最差语仍明显更高，门控阈值与增强强度需调，跨语系泛化未验证。


# Speech Encoder Fusion for LLM-based Automatic Speech Recognition

- 论文编号：1039
- 报告人：Jakob Poncelet
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/poncelet26_interspeech.pdf

## 问题
Speech-LLM 通常绑定单一预训练声学编码器；不同编码器错误互补，简单拼接未必充分利用，多语/分离场景更需自适应融合。

## 方法
在投影到 LLM 前融合两路等长编码器特征：对比 concat、sigmoid 门控、帧内多头门控、位置 Transformer、时间交织 Transformer（再池化）。编码器冻结；2 层 MLP 投影 + QLoRA（rank 4）微调 LLM。荷兰语：Whisper-large-v3 + NeLF + Tweety-7B；英语：Whisper + Wav2Vec2-FT + Llama-3.1-8B；亦可融 ECAPA2 做带说话人标注转写；可选第二阶段把解码器假设并入提示。

## 实验与结果
荷兰语单语：时间 Transformer 最佳（clean/other 6.8/8.3），优于 concat 与单编码器。英语：sigmoid 门控最好（2.8/5.5）。联合英荷训练时多头门控最佳（NL 6.5 / EN 2.5）。分离 ASR：时间 Transformer SA-WER 18.1、Spk-Conf 3.6。并入解码假设后荷兰语可到 5.6/7.8，优于纯文本纠错。

## 结论
精心设计的并行编码器融合在开销有限下全面优于特征拼接，适用于单语、多语与分离 ASR；短时 ASR 设定下仍可进一步用历史文本与更大 LoRA 提升。

## 点评
系统比较多种融合，并覆盖低资源语与说话人编码器，实用价值高。LLM 侧 rank/量化偏弱，英语难追上专用 ASR；时间 Transformer 在分离任务上强、英语上未必最优，融合策略需按任务选型。


# Dissecting Sensitivity to Training Language in Self-Supervised Speech Learning Using Neural Audio Codec Tokens

- 论文编号：3002
- 报告人：Daigo Takizawa
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/takizawa26_interspeech.pdf

## 问题
基于神经音频编解码器（NAC）离散 token 的 SSL 更省存储与算力，但语言敏感性来自 NAC 还是 SSL 预训练尚不清楚；若每语需重训 NAC 则削弱效率优势。

## 方法
控制实验解耦：RQ1 在 NAC 重建波形上做 ASR/SER；RQ2 固定 NAC、变 SSL 预训练语；RQ3 固定 SSL 与下游语一致、变 NAC 训练语。英/日/中，DAC 等公开 NAC；codec-based HuBERT（冻结 NAC 码本嵌入求和作输入）。用相对波形基线的 CoV 度量跨语变异。

## 实验与结果
RQ1：DAC 最稳，重训语（EN+/JP/ZH/All）对重建下游影响有限（ASR CoV 约 2%）。RQ2：SSL 预训练语与下游对齐显著更好，错配则 ASR/SER 大幅变差（CoV 可达 37–43%）。RQ3：SSL 对齐后更换 NAC 训练语差异小，不必按目标语重训声学 NAC。

## 结论
下游主要敏感于 SSL 预训练语言，而非 NAC 训练语言；可跨语复用单一声学 NAC，但 SSL 预训练语应与目标语对齐。

## 点评
把编解码器与 SSL 阶段拆开做因果式对照，结论对工程选路很清晰。范围限于英日中与声学型 DAC；语义型编解码器、更多语种与任务是否同样不敏感仍待验证。


# SuTRA: Structurally-Unified Tokenization with Root Awareness

- 论文编号：291
- 报告人：Vaibhav Rathore
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/rathore26_interspeech.pdf

## 问题
BPE 等子词优化压缩却忽略形态；印地语系等富形态语言以 akshara（辅音+matra）为书写原子，频率合并常切断词根与词缀（Morphological Shattering），并导致语义难恢复（Semantic Blindness）。现有形态数据集对印地语系边界标注不足。

## 方法
SuTRA 两阶段：预分词用正字规则把词绑成 akshara 单元，并用金标准词典或字符级 seq2seq 标出禁止跨越的形态边界；训练阶段在 BPE 式合并中用得分 S(a,b)=f(a,b)·Ψ(a,b)^γ_t，其中 Ψ=1−冲突次数/频次，γ_t 从高到低退火（先保词根、后挂词缀）。另构建 Hindi/Marathi/Gujarati 约 56 万词 LLM 核验形态切分金标准（IndicCorp + 规则分解 + Gemini 核验），表面边界保证可拼接还原。

## 实验与结果
形态对齐 Boundary F1：SuTRA 印地 0.586、马拉地 0.617（均最高），古吉拉特 0.584（接近 Unigram）。语义可恢复性：印地 Linear R² 相对 BPE 约 +34%（0.4464 vs 0.3329）。Hi↔Mr 翻译（3 层 Transformer，共享 32k 词表）：Marathi→Hindi chrF2 38.84、COMET 0.6554 最优；反向接近最强基线；摘要称平均 +8.08 chrF2。扰动稳健性上 Jaccard 高、Root-Affected 近零，优于纯统计分词。

## 结论
用轻量形态先验约束频率合并，可降低 Morphological Shattering，使整词语义更易从子词线性恢复，并提升翻译与扰动稳健性，而不显著推高 fertility/词表规模；未来可扩到其他富形态语言及 TTS/ASR。

## 点评
关键不是换更大模型，而是在词汇学习目标里显式惩罚跨词素合并，并保住 akshara 原子性。金标准依赖 LLM 核验，边界质量会传导到合并惩罚；对 Sandhi 强融合与词典外词仍依赖 seq2seq 推断，可能是主要误差源。虽放在 ASR 相关会场，正文实验以文本分词与 MT 为主。


# Measuring the Redundancy of Decoder Layers in SpeechLLMs

- 论文编号：1873
- 报告人：Adel Moumen
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/moumen26_interspeech.pdf

## 问题
SpeechLLM 中 LLM 解码器常占 >90% 参数，语音任务是否真需要全部深度？冗余能否跨任务复用尚未系统刻画。

## 方法
SLAM 框架：WavLM Large + MLP 投影 + Qwen2.5 / Llama 系列（1–8B）。用层间角距离找最优连续可删块；剪枝后对接收层 MLP 加 LoRA，并可选解冻投影做 healing。在 ASR（LibriSpeech、Loquacious）上量化可剪比例（相对 WER≤0.25），再迁移到 CoVoST2 AST（En→De、Fr→En，Whisper 编码器）。

## 实验与结果
文本与语音角距离热图几乎一致，冗余主要继承自预训练 LLM；深层更可删。联合 decoder+projector healing 远优于只修一侧。7–8B 可删约 28–44% 层仍保持可接受 ASR（约保留 ~60% 解码层）；更小模型可删比例更低。AST 可删约 32%，且 ASR 最优剪枝路径几乎可直接用于 AST。Llama3.1-8B 删 40% 层约 35% 加速、显存 15.72→10.37 GiB。

## 结论
解码器冗余大体模态与任务无关；可基于文本前向定剪枝路径，用单剪枝骨干加适配器服务多任务，降低计算成本。

## 点评
用角距离 + 局部 healing 把“多余容量”测清楚，并显示跨 ASR/AST 路径可迁移，对压缩部署很有启发。阈值依赖相对退化阈值；LoRA 微调解码器反降可剪性；更多家族、语种与推理类任务仍待覆盖。


# Weakly Masked Residual Reliability Learning for Unsupervised Domain Adaptation in Speech Models

- 论文编号：1767
- 报告人：Yuan Li
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/li26aa_interspeech.pdf

## 问题
无监督域适应中伪标签噪声大；仅靠置信度易受过置信误导，且丢弃不确定区域会造成边界监督不足。

## 方法
WMR²L：用最大置信度与非最大类残差离散度共同定义 token 权重（utterance 内标准化 + 高斯核），可靠 token 满权。弱置信掩码：对高权 token 以概率 r 将损失乘 λ 而非硬删，促从不可靠区恢复。多扰动一致性（时频掩码、随机裁剪缩放、均衡等）算 S=l·平均 WER，保留一致性最好的 τ 比例样本作伪标签。在 Whisper-medium 上微调。

## 实验与结果
相对 Whisper 基线相对 WER 降：CHiME-4 noisy 约 13.8%、SLURP 25.0%、CORAAL accented 15.7%；WMR²L+MP 全面优于 Confidence/Margin/Entropy+MP、STAR、Beam/Sample 等。CoVoST2 爱沙尼亚/印尼/威尔士翻译 BLEU 亦提升。Large-v3 上同样有效。消融：弱掩码优于强掩码/无掩码；m-r-eq 扰动组合最佳。

## 结论
置信度–残差可靠性加权 + 弱掩码 + 语音多扰动过滤，可提升跨域 ASR 与语音翻译的伪标签利用与泛化。

## 点评
针对过置信与选择性伪标偏差，用残差离散度与弱掩码补监督，思路细。滤波在伪标生成时只做一次，迭代自训动态未充分讨论；超参（α、r、λ、τ）与扰动组合对口音/噪声域可能需重调。


# Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition

- 论文编号：3465
- 报告人：Tung X. Nguyen
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26i_interspeech.pdf

## 问题
语码转换（CS）错误集中在嵌入语与切换边界（POI）；标准微调缺少针对这些易混片段的显式信号。

## 方法
CS-NMG：用冻结种子 ASR 的 N-best 定位 POI，仅替换 POI 构造 near-miss，并用 LLM（Gemini）离线扩展替换候选；经声学边际、音素距离、文本距离三层门控保留“难但合理”负例。Whisper-small + LoRA：POI 加权 CE（WCE）锚损失 + 多负例 InfoNCE 式对比排序（长度归一化分数）。推理仍为标准 ASR。

## 实验与结果
CS-FLEURS cmn-eng 与 ViMedCSS vie-eng：WCE+CL（tri-level）相对 CE 约降 2+ 点 WER/PIER（如 cmn-eng 16.67/17.25→14.06/15.10；vie-eng 24.72/21.95→21.87/18.74），优于 WCE、MWER 与仅 N-best 负例。消融：LLM 扩候选需门控才稳定；三层门控整体最优（约 3.8 NM/utt）。

## 结论
面向 POI 的 near-miss 对比训练比单纯上权 POI token 更能抑制跨语混淆，在总体 WER 与 PIER 上一致改进且无增推理模块。

## 点评
把偏好对齐落到声学合理的局部负例，切中 CS 错误分布。依赖外部 LLM API 与 prompt，离线成本与可复现性是短板；目前两语对、单骨干，门控阈值跨脚本迁移需谨慎。

