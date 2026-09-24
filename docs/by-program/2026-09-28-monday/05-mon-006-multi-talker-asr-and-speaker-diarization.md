# Multi-Talker ASR & Speaker Diarization

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral
- Area：8
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

多说话人 ASR 与说话人日志（diarization）在本场被作为紧密耦合问题讨论。合成会话数据研究（FastMSS + DiCoW / Sortformer）表明最优仿真配方高度任务依赖：增大重叠利于 ASR 却损害 diarization；来源多样性常优于精确域匹配；合成+真实混合可超过仅真实训练。

系统路线上，Dixtral 用 diarization mask 条件化声学编码器（DiCoW→Voxtral）而非 Serialized Output Training 去改解码器，以避免灾难性遗忘；GLAD 以全局—局部融合的动态 MoE 在深层保留说话人特异声学线索；HCM 则被扩展到联合转写—说话人空间聚类，同时服务无目标说话人与目标说话人设定。

流式多说话人 ASR 被归纳为四种架构策略（是否多实例、是否微调），在精度、单说话人退化、内存与训练复杂度间权衡。评测侧提出 tcpSemER（嵌入语义相似度替代编辑距离）并按重叠/非重叠分解 tcpWER，发现 LLM 方案在两说话人有竞争力，但随说话人数与重叠上升而退化，模块化流水线更稳。瓶颈是重叠、远场、说话人数变化与评测是否抓住“改义错误”。

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

