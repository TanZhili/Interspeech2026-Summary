# Speech and Language Technologies for Health Applications 1

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：13
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场面向健康应用：咳嗽结核筛查、青少年自杀风险语音检测、抑郁检测的联邦隐私、言语治疗感知训练、神经疾病西班牙语 ASR 语料，以及德文焦虑抑郁语音数据集。共同线索是非侵入、可扩展的语音生物标志，同时强调隐私、范式泛化与真实临床/众包数据质量。

方法上出现基础模型表示与谱描述符的融合（双曲原型 + bandit 加权）、跨诱发范式的 Speech LLM + MoDE 专家、以及联邦多模态原型对齐并引入隐私–性能分数。教育与包容侧则用深度学习嗓音编辑生成锚点样本训练学生感知，并发布神经受损西班牙语与德文 GAD/抑郁开源标注资源。

趋势是：从单任务单范式检测走向跨范式统一模型、隐私可量化的联邦学习，以及面向低资源病理语音与心理健康的基准数据集建设。

## 论文技术总结

# From Signals to Patterns: Non-Invasive Tuberculosis Detection from Cough Audio using Bandit Weighted Hyperbolic Prototypes

- 论文编号：2704
- 报告人：Muskaan Singh
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/akhtar26_interspeech.pdf

## 问题
咳嗽音频结核筛查中，频谱描述子与预训练基础表示各有优劣，但简单拼接难利用互补性，且易受设备/环境伪迹影响。

## 方法
提出 COBALT：双流（如 MFCC 与 PaSST 等）经轻量适配与 tokenization，映射到共享 Poincaré 双曲原型码本；用 bandit 式可靠性权重融合原型，再接 MLP 分类。对比单流、拼接、欧氏变体与 Möbius 加法融合。

## 实验与结果
CODA TB DREAM Challenge 受试者无关五折。单流以 PaSST+CNN 最强（ACC≈79.3%）。完整 COBALT 在 MF+PST 达 ACC 88.93、F1 87.26、AUC 89.07，优于拼接与仅 Möbius 组成；COBALT-E 亦稳定优于拼接，说明结构化融合本身有益。

## 结论
双曲原型对齐 + 样本相关可靠性加权能有效融合频谱细节与基础模型时序模式，在基准上刷新报告指标。

## 点评
融合设计针对“异构表示不对齐 + 伪迹不稳定”很贴切。临床外推仍受挑战赛协议与多国设备异质性制约；可解释性主要停留在消融，未深入验证模型是否真正依赖病理声学而非通道伪迹。


# Towards Paradigm-General Suicide Risk Detection via Speech LLM

- 论文编号：666
- 报告人：Wen Wu
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/li26j_interspeech.pdf

## 问题
青少年自杀风险语音检测常依赖单一诱发范式（流利、朗读、问答等），需为每范式单独建模；简单混合多范式联合训练又难稳定增益。

## 方法
以 Qwen2.5-Omni-7B 为骨干，提出 Mixture of DoRA Experts（MoDE）：路由器对多个 DoRA 专家加权，配合负载均衡 KL 与温度缩放；在 1223 名中国青少年、10 种 SEP、MINI-KID 标注上做二分类。对比 Whisper、分范式微调与联合微调。

## 实验与结果
联合微调下 speech LLM 多数范式优于 Whisper；MoDE 平均准确率 0.656，相对分范式 0.628 约 +4.5% relative。消融去掉温度或负载均衡均下降（无负载均衡会塌到单专家）。专家数先升后降；人工指定范式–专家先验反而不如自动路由。正文报告可泛化到未见范式并改善置信校准。

## 结论
轻量 MoDE 可将多诱发范式统一进单一 speech LLM，并优于分范式与朴素联合训练。

## 点评
抓住“范式互补但分布异构”用 MoE 式适配，比硬混数据更合理。医疗场景准确率仍中等，外推依赖受控采集与文化语境；未见范式泛化与校准细节需结合原文图表谨慎解读。


# FedMPA: A Novel Privacy-Performance Optimization Approach for Multimodal Speech-Based Depression Detection

- 论文编号：586
- 报告人：Dushanthi Madhushika Manamalage
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/manamalage26_interspeech.pdf

## 问题
基于语音的抑郁症检测需兼顾性能与隐私；联邦学习下多模态非 IID、成员推理泄漏与相对中心化的性能落差同时存在，且鲜有量化隐私–性能权衡的指标。

## 方法
FedMPA：在 ALiDeR 上扩展模态特异类原型（文本/音频/融合）、EMA 稳定全局原型库、原型拉取+排斥损失、原型相似度加权聚合，以及 softmax–原型混合推理（低置信时 defer 到原型分类）。提出 PPS：UAR 与基于 MIA 置信 AUC 的隐私分的调和平均。

## 实验与结果
E-DAIC 上，完整损失组合达 UAR 0.89；混合推理优于纯 softmax/纯原型。对比 FedAvg/FedProx/FedProto/FedGPD 与中心化 ALiDeR：FedMPA 获最高 PPS 0.92（UAR 0.89，MIA_conf_AUC≈0.52），中心化 UAR 更高（0.92）但隐私更差（PPS 0.88）。

## 结论
模态特异原型对齐与混合推理可在联邦抑郁检测中同时提升效用与抗成员推理能力，并用 PPS 显式度量权衡。

## 点评
把“多模态非对齐 + 隐私–性能”做成可优化目标是贡献点。评估仍限 E-DAIC 与黑盒置信 MIA，未包含差分隐私等显式防护；原型假设两类抑郁标签空间，对更细严重度回归未展开。


# Can deep learning based voice editing enhance voice quality perception skills in speech therapy students?

- 论文编号：2475
- 报告人：Jana Wiechmann
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/wiechmann26_interspeech.pdf

## 问题
言语治疗学生难以可靠感知嗓音质量；自然锚点样本本身多维重叠，无法让新手单独体验 creaky/breathy/rough 等单一维度。

## 方法
20 名临床语言学学生组间设计：对 16 段非病理德语嗓音做前测→专家讲解→后测。控制组听自然锚点；实验组用可控制嗓音质量强度的深度学习编辑 TTS 样例隔离三维特征。以专家金标准算 κ 与感知灵敏度 d′。

## 实验与结果
合成组 d′ 由 0.73 显著升至 1.03，控制组无显著变化（0.49→0.55）；后测合成组显著高于控制组（d′ 与 κ）。ANCOVA 控制前测后组效应仍显著。分维上仅“rough”在合成组从低于机会升至显著改善；breathy/creaky 无显著提升。

## 结论
深度学习嗓音编辑可用于教学讲解，比自然锚点更能提升新手整体感知灵敏度与专家一致性，尤其有助于困难的 rough 维度。

## 点评
把生成编辑当作可解释教具而非临床替代，问题设定清晰。样本量小（每组 10）、仅女性学生、刺激为非病理日常嗓音，外推到病理评估训练需再验证；讲解交互时长未严格控制。


# S-DiverSe: Spanish Diverse Speech

- 论文编号：2529
- 报告人：Fernando López
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/lopez26b_interspeech.pdf

## 问题
西语神经疾病语音（ALS、帕金森、卒中后构音障碍）公开野外基准稀缺，标准 ASR 在病理语音上仍脆弱，难以系统评估与适配。

## 方法
发布 S-DiverSe：22 名说话人、3.2 小时野外西语音频、444 段人工转写，含性别/病种/可懂度元数据（注释与视频链接公开）。评测 Whisper-large-v3、Voxtral-Mini、omniASR CTC 1B、ElevenLabs Scribe v2；并用 NeuroVoz/TORGO/Common Voice 做微调与启发式文本后处理（去重复幻觉）。

## 实验与结果
零样本总 WER：Scribe 20.69%、omniASR 33.56%、Whisper 36.43%、Voxtral 40.43%；WER 随可懂度下降而上升。启发式后处理显著降 WER（如 Whisper 36.43→22.01）。域外神经数据微调常损害 S-DiverSe（Whisper FFT 甚至 WER 飙升），作者认为后处理对域外神经西语更稳健。

## 结论
提供多病种野外西语 ASR 基准；对当前模型，规则后处理优于跨域微调。

## 点评
填补西语病理 ASR 数据空白，野外多样性是卖点。规模小、男性/ALS 偏斜、可懂度标注一致性仅 fair，且音频本身不直接分发，限制复现与训练用途。


# GADVOX: The German Anxiety and Depression Voice Examination Dataset

- 论文编号：3523
- 报告人：Robert P. Spang
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/spang26_interspeech.pdf

## 问题
抑郁/焦虑语音研究过度依赖英语小样本（如 DAIC-WOZ）；德语公开资源缺失，且多仅做二分类，难支撑严重度回归与共病建模。

## 方法
众包采集 GADVOX：1004 名成人、10 条随机顺序的结构化自由说提示，人均约 18.4 分钟自发语音；同人自填 PHQ-9 与 GAD-7（α=0.85/0.86）。四阶段质控（注意力陷阱、自动筛、人工听感、ITU-T P.566 质量估计），从 1420 人中保留 1004。元数据 CC BY 4.0 公开，音频经申请提供。

## 实验与结果
人口统计覆盖 18–77 岁；PHQ-9≥10 占 29.2%，GAD-7≥10 占 20.9%，两量表相关 r=0.795。另含创伤等社会心理条目与会话质量分。正文以数据集描述与分布分析为主，未报告下游检测基线模型。

## 结论
提供首个可公开申请的德语抑郁–焦虑严重度配对语音语料，支持多目标回归与共病研究。

## 点评
规模与双量表严重度标注相对 DAIC-WOZ 是实质进步；众包偏高教育/数字素养，自报筛查≠临床诊断，音频非完全开放需注意获取门槛。

