# Information Extraction and Retrieval

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Poster
- Area：12
- 论文数：7

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场以关键词发现（KWS）与音频检索为主线，并延伸到广播档案中的视听人物检索。开放词表与用户自定义关键词成为共同目标，但落地约束分化为：词库规模与存储、端侧能耗、部署后增量加词，以及流式推理下的对齐一致性。

开放词表 KWS 多依赖多模态对齐与上下文偏置。大规模术语库需要极致压缩特征存储；用户自定义场景则出现脉冲神经网络以累加运算替代浮点注意力，以及参数封顶的模块化扩展分支以冻结基座并避免旧关键词回归。流式设定下，交叉注意力中 Query/Key 角色与 CTC 音素对齐成为关键设计点。

检索侧强调无标注表示：自监督嵌入配合 DTW 或离散化后的 TF-IDF/BM25，在哼唱检索与示例检索上呈现域相关最优策略。视听人物检索则质疑“永远多模态融合”的默认假设——缺席模态会注入噪声，查询自适应的活跃模态检测成为精度关键。

总体方向是：开放词表要可扩展、可流式、可低功耗；检索要按任务选择序列匹配形态；多模态融合要先判断模态是否可用。

## 论文技术总结

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

