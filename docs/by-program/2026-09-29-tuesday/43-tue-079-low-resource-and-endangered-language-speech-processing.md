# Low-Resource & Endangered Language Speech Processing

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：9
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从濒危语言总览出发，讨论短形式语料引导 ASR、通用音素识别配方、发音特征零样本分类，以及谱系先验自监督。特邀报告框定现状：语音 AI 约覆盖 100 种语言，其余五千余种多为低资源且多处濒危，而识别与合成可用于保存与复兴。

后续论文回应“从何入手”：词/短短语对齐比句级监督更易获得；大规模多语音素识别需要可复现配方；离散 IPA 标签不足以保证未见语音对立；语言家族感知预训练在数据受限时提升鲁棒，但不能替代大规模预训练。趋势是把语言学结构（音系、发音特征、谱系）显式写入数据与目标。

## 论文技术总结

# Low-Resource & Endangered Language Speech Processing

- 论文编号：
- 报告人：Tatsuya Kawahara
- 程序：Tuesday 29 September 2026 / Low-Resource & Endangered Language Speech Processing
- 技术分类键：multilingual
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
当前语音 AI 大约覆盖世界 5000+ 语言中的约 100 种；其余基本属低资源，其中许多面临消亡风险。语音技术可用于这些语言的保存与复兴，需要系统梳理方法与实践。

## 方法
报告概述面向低资源与濒危语言的语音识别与合成：方法途径、数据集、训练方法、可用基础模型与用例，并包括报告人团队开展的阿伊努语（Ainu）与琉球语（Ryukyuan）相关项目。

## 实验与结果
摘要给出覆盖语言数量的量级对比（约 100 / >5000），并点名 Ainu、Ryukyuan 项目，但未报告具体识别/合成指标。

## 结论
低资源与濒危语言仍是语音 AI 的主要空白；识别与合成技术有望服务保存与复兴，但需结合专门数据、训练与基础模型实践。

## 点评
用覆盖率缺口框定问题，并用团队项目作案例锚点。「~100 / >5000」来自摘要，细粒度评测与数据构成需另查材料。


# Bootstrapping Endangered Language ASR with Short-Form Corpora

- 论文编号：1302
- 报告人：Christopher Bartley
- 程序：Tuesday 29 September 2026 / Low-Resource & Endangered Language Speech Processing
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bartley26_interspeech.pdf

## 问题
濒危语言常缺 3–15 秒句级对齐语料，却有短词/短语发音资源与长录音文本；大模型路线算力门槛高，社区难以起步。

## 方法
用 Kaldi GMM-HMM（CPU 可训）在英语 LibriSpeech 上系统缩短训练单元，量化短式相对句级的代价。再对 Cornish、Manx、Hawaiian、Jejueo、Mohawk：以短式语料训 monophone → Viterbi 强制对齐长录音 → 自举 triphone 解码并按 LibriSpeech 流程切分，得到句级集。合并 short+utterance 训练 GMM/DNN-HMM，并与零样本 OmniASR、MMS、Whisper 及 LoRA 微调 Whisper 在 in-domain / OOD 上对比；外源文本降 OOV 后重建 4-gram LM。

## 实验与结果
英语上平均时长降至约 1s 前 WER 基本稳定，更短则上升；稀缺数据下句级格式重要性下降。五语 monophone 对齐成功率均 >70%；三语 bootstrapped 解码 WER <5%。自建 GMM 已在多数语上优于零样本多语大模型；DNN+增强 LM 整体最强，外源 LM 平均降约 5.82 点 WER。Jejueo/Mohawk 仍极难；文本稀缺时 Whisper-FT 在 OOD 更优。

## 结论
不必以句级监督为起点：短式资源可自举对齐长录音并训出可用 ASR，且 CPU 系统可在 OOD 上以远低于大模型的算力取得更好表现。应更好利用社区已有非常规数据。

## 点评
把“格式不对”重新定义为可对齐的数据问题，对濒危语社区路径现实。强在英语对照实验与开源五语切分集；弱在部分长录音保留率低（如 Hawaiian 仅约 23% 时长）、OOD 测试集很小，且 HMM 与 E2E 的可比边界依赖文本资源。


# An Empirical Recipe for Universal Phone Recognition

- 论文编号：1462
- 报告人：Shikhar Bharadwaj
- 程序：Tuesday 29 September 2026 / Low-Resource & Endangered Language Speech Processing
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bharadwaj26_interspeech.pdf

## 问题
英语音素识别模型跨语泛化差；多语音素识别又常未充分利用 SSL，且不清楚数据规模、架构与损失各自贡献。

## 方法
在统一 PRiSM 评测下做受控消融，确定配方：以 XEUS（大规模多语 SSL）为骨干，用 Self-Conditioned CTC 在 IPAPack++（约 17k 小时）上微调，得到 PhoneticXEUS。对比 Vanilla/Inter/Self/Hierarchical CTC 与 CTC-Attention；对比从零训练的 E-Branchformer 与 MMS/XEUS；并缩放多语训练句数（固定英语约 850k，多语 150k→600k）。进一步按语系、口音与发音特征分析错误。

## 实验与结果
PhoneticXEUS：口音英语平均 PFER 10.6，多语平均 17.7，均为表中 SOTA。SelfCTC 多语 17.7，优于 InterCTC 18.5 与 Vanilla 18.8；XEUS+SelfCTC 相对从零训练约改善英语 2.0、多语 5.4 点。增加多语数据改善多语表现且不伤英语。SSL 在 PR-vox 的 21 语系中 19 系更好；在 PR-saa 的 192 口音中 187 个更好。时域性强的特征（如 tenseness、delayed release）相对收益最小。

## 结论
SSL 初始化 + SelfCTC + 大规模多语 G2P 数据构成有效通用音素识别配方；SSL 利于跨语迁移与口音稳健，但部分发音特征与低质评测集仍是瓶颈。

## 点评
用同一评测协议把损失、骨干与数据规模拆开，给出可复现配方，比单点刷榜更有建设性。强在开源代码数据与错误剖面；弱在训练标签主要来自 G2P（偏典范音），对儿童/短音节等声学偏移仍脆弱，作者亦承认评测标注噪声。


# Improving Zero-Shot Phonetic Classification through Language-Agnostic Articulatory Features

- 论文编号：2246
- 报告人：Ryo Magoshi
- 程序：Tuesday 29 September 2026 / Low-Resource & Endangered Language Speech Processing
- 技术分类键：multilingual
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/magoshi26b_interspeech.pdf

## 问题
Speech-to-IPA 的 Phonetic Foundation Model 多靠 G2P 标签，本质偏音位且跨语记法不一致；仅靠多语离散 IPA 覆盖不足以在零样本下区分未见语音学对立。

## 方法
排除中文与日语后，在 IPAPack++ 的 Common Voice/FLEURS 部分（78 语约 3000h）训练：POWSM（CTC/Attention）与 XLS-R+AFCM（帧级预测 24 维 PanPhon 发音特征并联合 CTC）。分类时先定位目标段，再比较三种读出方式：Decoder 对齐、CTC 峰值帧 argmax、以及 AF 向量与候选模板的 L1 距离。并对比 single-frame 与 segmental 时间聚合。

## 实验与结果
零样本任务：中文送气对立（FLEURS）与日语音拍鼻音（CSJ，人工核验 IPA）。POWSM 平衡准确率差（送气约 53–58%，鼻音约 47–49%）。XLS-R+AFCM 的 CTC 送气达 94.5%；AF single-frame 进一步到 95.4%，但 AF segmental 因冲淡送气爆发几乎崩溃（约 50.8%）。鼻音上 AF segmental 最好（72.6%），稀有 [ñ] 召回 38.5%，远高于非 AF 方法（<7%）。

## 结论
连续发音特征比离散 IPA 更利于零样本语音学分类，尤其稀有音；最优时间聚合取决于线索是瞬态（送气宜单帧）还是持续（鼻音部位宜段平均）。

## 点评
把“符号覆盖了”与“声学对立学会了”拆开验证，对 G2P 训练范式是尖锐压力测试。强在两类对立与聚合消融清楚；弱在任务仅两语两类对立、训练仍依赖 G2P 派生 AF 标签，完全开放词表零样本 ASR 仍有距离。


# Genealogical Priors in Self-Supervised Learning: Improving Speech Technology for Low-Resource Languages

- 论文编号：2886
- 报告人：Elizabeth Granda
- 程序：Tuesday 29 September 2026 / Low-Resource & Endangered Language Speech Processing
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/granda26_interspeech.pdf

## 问题
全球多数语言在语音技术中资源稀缺，现有 SSL 多语预训练通常把语种多样性当成规模变量，随机混合语料，很少按谱系结构组织数据，难以把亲属语言共享的语音规律作为归纳偏置迁移到低资源语言。

## 方法
在 Unsupervised People’s Speech in the Wild（UPS）语料上，先做 VAD 与时长过滤，再用 Glottolog/Ethnologue 将语言映射到语系。构造两类时长匹配的约 60 小时继续预训练子集：language-aware（约 32 语、多语系，尽量每系 2–3 语）与随机抽样的 no-language-aware。以 WavLM-Large（316M）为骨干，冻结 CNN 特征编码器，对 transformer 与投影头做对比式继续预训练（含 Gumbel-Softmax 量化），训练时施加语速扰动与加性噪声。下游作为 embedding 提取器评估 LID、ASR 与说话人聚类。

## 实验与结果
预处理对比显示 VAD 后 HuBERT/Wav2Vec 的语言与语系 centroid 分类准确率均上升。60h 两配置验证损失接近（约 3.86 vs 3.93），但 UPS 下游差距大：language-aware 综合分/F1/CER/ARI 为 0.50/0.50/0.75/0.48，no-language-aware 为 0.04/0.037/0.90/0.39。官方未继续预训练的 WavLM-Large 基线仍明显强于二者；作者认为 60h 不足以重塑约 94k 小时英语预训练得到的表示。

## 结论
在数据严重受限时，按语系组织预训练数据可比同等规模随机多语混合带来更强下游表现；谱系结构是对大规模预训练的补充，而非替代。作者亦指出实验子集较小，语缘关系并非纯树状，未来可结合地理/接触因素。

## 点评
核心贡献是把历史语言学的语系先验变成 SSL 的采样课程：在对比学习依赖负样本结构的前提下，结构化多语混合比“同等小时数随机混合”更稳。证据主要来自受控 60h 对比，强结论应限于“数据受限下的继续预训练”；与官方大规模 WavLM 基线的落差也说明，语系先验目前是抗崩塌的数据策展手段，还不是跨越量级差距的替代路径。

