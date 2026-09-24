# Audio segmentation

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
- 形式：Oral
- Area：5
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场名义为音频分割，实际覆盖多任务门控理解、关键词测试时适应、流式端点检测、超小 VAD、语音编解码器探测，以及文本–音频对比学习的模态内相似监督。共同点是在端侧/流式约束下决定“何时听、听什么、表示里有什么”。

门控多任务把 ASR、情感与场景分类统一在 Whisper-small 上，按干净/噪声/非语音条件激活头，并发布 ESAS-32K。KWS 的测试时适应直面关键词稀有与背景主导导致的熵最小化偏差。端点检测用“到下一语音 onset 的时间”作可从时间戳衍生的监督，缓解犹豫停顿。极简因果 VAD 强调标准 Mel、纯 CNN、结构化剪枝与角距 QAT。

另一侧是表示诊断与学习：主流 speech tokenizer 经探测更偏语音而非词义语义；对比学习则把文本–文本、音频–音频相似转为跨模态软目标。整体从“切段”扩展到“条件激活、在线适应与表示内容核对”。

## 论文技术总结

# A Gated Multi-Task Whisper Framework for Speech, Emotion, and Scene Understanding

- 论文编号：135
- 报告人：Manjiri Bhat
- 程序：Monday 28 September 2026 / Audio segmentation
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/bhat26_interspeech.pdf

## 问题
辅助场景需同时做 ASR、SER、ASC，独立模型低效；Whisper 在非语音段易幻觉。需要统一框架并按输入类型条件激活任务头。

## 方法
Whisper-small 共享编码器 + 三路门控（干净语音 / 非语音 / 噪声语音）与 ASR、SER、ASC 头。训练用加权多任务损失（门控权重大），分两阶段：先训编码器与分类头（解码器冻结），再联合微调。推理按门控路由：干净→ASR+SER；非语音→仅 ASC；噪声→三者全开。构造 ESAS-32K（约 32k，情感语音与 SPASS 场景在多 SNR 混合）。

## 实验与结果
70/10/20 划分：门控 Acc≈99.98%，SER 98.2%，ASC 94.5%；加 n-gram 限制后 WER 可到约 0.41%。无门控时非语音幻觉率约 96%，有门控约 0.015–0.4%。优于若干单任务 Whisper/专用模型；低资源划分下门控仍稳健。

## 结论
门控多任务 Whisper 可在统一模型中条件激活 ASR/SER/ASC，并显著抑制非语音幻觉，适合情境感知音频分析。

## 点评
把 VAD 式路由做成可学习三分类并与多任务联合，直接打中 Whisper 非语音幻觉痛点。ESAS-32K 为模拟混合，真实嘈杂场景泛化待证；训练时不用门控路由、仅推理用，门控错误会系统性关掉错误任务头。


# ImKWS: Test-Time Adaptation for Keyword Spotting with Class Imbalance

- 论文编号：258
- 报告人：Ting Dang
- 程序：Monday 28 September 2026 / Audio segmentation
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/ding26_interspeech.pdf

## 问题
关键词检测（KWS）在真实噪声与域偏移下性能下降，传统微调或域适应需要源域或标注目标数据，而测试时适应（TTA）虽只需无标注测试流，但现有方法（如 AdaKWS 的熵最小化）在“关键词极少、背景极多”的严重类别不平衡下，更新会被背景类主导，模型对背景过度自信、难检出稀有关键词。

## 方法
ImKWS 在预训练轻量 KWS 模型（BC-ResNet-3）上，仅用无标注测试流、只更新 BN 仿射参数做单遍 TTA。核心有三块：(1) **解耦熵最小化（DEM）**：将条件熵拆成 reward 分支（温度 τ 控制分布锐度）与 penalty 分支（缩放因子 α<1 削弱把非目标 logit 压向 −∞ 的梯度），减轻多数类过自信；(2) **多视角一致性**：对时间/频率 mask 增广视图用对称交叉熵约束预测一致，抑制不平衡流带来的梯度抖动；(3) **两阶段样本选择**（沿用并改造 AdaKWS）：DEM 损失与伪关键词一致性（PKC）双阈值筛选样本，再按 DEM 与 PKC 加权组合总损失。输入为 40 维 MFCC。

## 实验与结果
数据：Google Speech Commands v2 构造 4 类任务（yes/up/stop + 合并非关键词），测试端将关键词:非关键词比调到 1:4–1:8，并混入 ESC-50 与 MS-SNSD 噪声、多 SNR。对比 TBN、Tent、SAR、ETA、AdaKWS。在 1:8、宏/微 F1 下，ImKWS 全面最优；相对 AdaKWS，ESC-50 上 macro F1 在 −10/0/10 dB 提升约 +1.23/+1.43/+1.62%，MS-SNSD 上约 +2.96/+2.19/+1.50%。不平衡越严重（至 1:8）优势越大；消融显示去掉 DEM、一致性或样本选择均掉点。

## 结论
作者认为 DEM + 多视角一致性能在严重不平衡与低 SNR 下稳定做 KWS 的 TTA，尤其在 1:8 与 −10 dB 时优于标准熵最小化基线；未来拟扩展到内存受限的端侧学习。

## 点评
抓住的是流式 KWS 里“背景淹没关键词”导致 EM 塌缩这一具体机制，而不是泛泛的域偏移。把惩罚强度从 1 调到 α<1 是可解释的正则：主动限制多数类 one-hot 化，再靠一致性稳住梯度——和“只筛样本再做标准 EM”的 AdaKWS 路线形成互补。脆弱点在于依赖 BN 仿射更新与手工阈值/超参（τ、α、λ、选择阈值），且实验主要在 Speech Commands 人为重采样不平衡上，对真实连续长流、非固定关键词集的泛化仍待验证。


# Next-Turn: Duration-Aware Streaming Endpoint Detection via Time-to-Next-Speech-Onset Prediction

- 论文编号：1053
- 报告人：Tao Zhong
- 程序：Monday 28 September 2026 / Audio segmentation
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/tsoi26_interspeech.pdf

## 问题
流式语音交互需要可靠的端点检测（EPD），但说话人中途停顿、犹豫使纯声学 VAD 易早切或拖尾；基于 ASR 文本的语义 EPD 又受级联错误与延迟牵制。音频语义 EPD 则面临语义完成监督模糊、以及语义建模与低时延流式约束之间的张力。

## 方法
Next-Turn 以 **到下一语音起始的剩余时间 τ(t)** 为监督（由对齐时间戳得到，无需额外人工语义标注）：说话中为 0，句中停顿为到下一 onset，句后静音设为 τ_max。编码器为 Whisper + LoRA；可单独做二分类 EPD、单独做时长回归（REG）/离散分类（CLS），或共享编码器多任务联合（L_bin + L_dur）。推理时可将时长预测归一化为端点分数，并可选与二分类分数加权融合。训练时随机截断未来上下文，迫使模型在有限 look-ahead 下做判断；评测按 160 ms 非重叠 chunk 流式跑，分数可做指数平滑。

## 实验与结果
训练：约 1177 小时中文内部语料；评测 1185 句人工端点、按停顿次数均衡。单任务 REG 已优于二分类基线；联合 CLS 在网格搜索常选 w=1（推理只用二分类头）时整体最佳：EI=5.0%，ACC_320=86.7%。相对最强开源语义基线 Easy Turn（ACC_320=60.8%），Whisper-large 系统在 ACC_320 上绝对提升 25.9%。相对二分类基线，停顿越多增益越大（Joint CLS 在 4+ 停顿上 ACC_320 可多约 +7.6）。Whisper-tiny（8M）仍达 EI=12.3%、ACC_320=73.2%。

## 结论
作者认为用 time-to-next-onset 作代理监督可做出流式、低开销的语义 EPD，并显著优于声学与近期语义基线；联合时长目标能补强标准二分类，尤其在多停顿场景。更小 Whisper 骨干仍具竞争力；未来拟扩展到多轮对话与跨语料/语言验证。

## 点评
关键设计是把难标的“语义是否说完”换成可从时间戳自动得到的连续时长目标，并用随机截断适配流式——监督可规模化是相对 ASR 级联或纯人工语义标签的优势。联合训练里最好配置常退回二分类推理，说明时长更像正则/表征塑造而非必须融合的分数。对比表中开源系统未在同语料重训，数字偏部署视角；评测集仅约千句且为中文内部数据，跨域与绝对数值敏感性需谨慎看待。


# VAD to the Bone: Ultra-Tiny Speech Activity Detection for Edge Deployment

- 论文编号：2523
- 报告人：Shanza Iftikhar
- 程序：Monday 28 September 2026 / Audio segmentation
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/bauer26_interspeech.pdf

## 问题
端侧常开场景需要极小、低时延、可部署的 VAD，但近期紧凑模型常依赖可学习滤波带、RNN/特殊激活或非因果滑窗评测，与嵌入式 DSP/TFLM 工具链不兼容，且参数量或因果性能被夸大。

## 方法
提出 kiloVAD：标准 Mel 特征 + 纯 CNN（深度可分离卷积、全局平均池化、线性分类），用 1×1 adapter 解耦 Mel 维与内部通道，并对每帧 Mel bin 做窗内零均值单位方差归一化。压缩上：(1) 按层独立剪枝比，用 Optuna 多目标搜索（验证集 FPR@TPR=0.95 与参数量），剪后以未剪模型为教师做自蒸馏微调；(2) 角度感知自蒸馏 QAT：冻结全精度分类器权向量为原型，量化骨干特征对目标原型对齐、对非目标铰链排斥，针对低比特角度误差。默认约 200 ms 上下文、64 Mel bins；严格因果、无未来上下文与时间平滑的逐帧评测。

## 实验与结果
训练：LibriSpeech train-clean-100 混合清洁/风噪/DNS 噪声与部分混响。评测 AVA-Speech AUC。完整模型约 81.1k 参数、AUC 0.862；剪至 2.1k 仍约 0.850（相对未剪约 1.3% 内），匹配 MarbleNet 的 0.850 但参数少约 43×、上下文 200 ms 对 630 ms。INT8 近无损；INT4 下角度 QAT 相对标准 STE QAT 提升约 1–4%（如 2.1k：0.693→0.719）。上下文到 360 ms 可达约 0.872 AUC。

## 结论
作者认为在满足 Mel 前端、可移植算子、低时延与因果评测的前提下，kiloVAD 以极小 CNN + 按层剪枝与角度 QAT 达到可部署的因果 VAD SOTA 级表现；相对依赖特殊结构或非因果协议的紧凑模型填补了部署缺口。

## 点评
问题定义清楚：把“能不能上 MCU”拆成前端、算子、时延、因果四条硬约束，再围绕可剪枝 CNN 做压缩，比单纯追参数量更贴近工程。按层 Pareto 剪枝 + 角度几何 QAT 针对极端压缩是合理路线。对比表中他人数字协议不一，作者已提醒不可直接比 AUC；训练偏朗读语音加合成噪声、评测换域到 AVA，极端剪枝有种子层崩，仍需实机功耗/时延验证。


# Speech Codec Probing from Semantic and Phonetic Perspectives

- 论文编号：3135
- 报告人：Xuan Shi
- 程序：Monday 28 September 2026 / Audio segmentation
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/shi26g_interspeech.pdf

## 问题
连接语音与 LLM 的 speech tokenizer 常被标为带“semantic”码本，但社区用语中的 semantic 常混同 SSL 表征，未必对应词汇语义；若实际更偏语音学（phonetic），则与文本语义空间错位，可能拖累多模态理解。需要系统探测现有编解码器各层到底编码了什么。

## 方法
对 EnCodec、DAC、MIMI、MIMO 四类代表编解码器做三类探测（文中将 semantic 定义为同义词级词汇意义，phonetic 为近同音/发音相近）：(1) 在 LibriSpeech 词段上比较同义词对与近同音对的特征欧氏距离（沿用 SSL probing 思路），看相对信息密度；(2) 用 rt-MRI 导出的 Vocal Tract Distance（VTD）与码本特征做 PWCCA，做发音生理层面的语音学相关；(3) 对面向对话的 MIMI/MIMO，用 CKA 测语音–文本潜空间结构对齐，并与随机置换基线比较。

## 实验与结果
各编解码器普遍保留更多 phonetic 而非 lexical-semantic 信息；EnCodec/DAC 随层加深可见语义/语音学可区分性“淡化”，DAC 对说话人属性距离更高；MIMI/MIMO 信息随层累积，但 MIMI 因首层 WavLM 蒸馏更早收敛且偏 phonetic/acoustic。VTD 相关与上述趋势一致；单独看 MIMI 首层亦注入显著语音学相关。CKA：MIMI 0.329、MIMO 0.122，相对随机基线增益仅约 0.087 / 0.054，跨模态语义结构弱。

## 结论
作者认为当前主流 speech codec 编码以 phonetic（且有发音生理依据）为主，所谓 semantic token（如 WavLM 蒸馏）名实不符；未来 tokenizer 宜从具真正文本语义的模型蒸馏，或在训练中加入显式语义约束，以更好服务 LLM 集成。

## 点评
价值在于把“semantic token”这一流行标签用可操作定义拆开，并用词对距离、rt-MRI 与 CKA 三角互证，结论对 codec–LLM 路线有直接设计含义。弱点是探测多为相关/距离代理而非下游因果实验，且主要英语资源；CKA 绝对值受有效维度影响，作者已用置换基线校正，但仍是结构相似而非任务语义对齐。


# Leveraging Mutual Intra-Modal Similarity Supervision for Text and Audio

- 论文编号：3300
- 报告人：Julian Miguel von Aspern
- 程序：Monday 28 September 2026 / Audio segmentation
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/vonaspern26_interspeech.pdf

## 问题
音频–文本对比学习（如 CLAP）常用 batch 内 one-hot 配对作监督，忽略同 batch 内文本或音频彼此的语义相似度；图像–文本侧已有用文本–文本相似度作软标签的做法，但音频–文本场景如何迁移、如何同时利用音频–音频相似度、以及小 batch 下软目标训练稳定性仍不清晰。

## 方法
在对比框架上：用冻结 Sentence-BERT 与冻结 PaSST 分别算 batch 内文本–文本、音频–音频余弦相似度矩阵，经加权混合（或按 Monte Carlo/确定性 dropout 估计的嵌入不确定性做逐元素混合）作为跨模态相似度软目标，再与可训练 PaSST + RoBERTa-large 的跨模态相似度做对称 CE 或 MSE。可选模态分类分支 + 梯度反转缩小模态间隙。总体在约 0.5M 样本、batch 64 的可控设定下训练 20 epoch。

## 实验与结果
下游：ESC-50 / TUT17 / US8K / NSynth 零样本分类；Clotho 上 TAR/ATR。相对同设定 baseline 与更大的 CLAP23（约 4.6M 样本、batch 1536），MSE+T（仅文本–文本软目标）多任务综合最强，多数集上优于 baseline 与 CLAP23（NSynth 除外）。TAR 上 MSE+T+A+U 累计 rank 最优；ATR 上 MSE+T+A 最好。CE 对软目标整体弱于 MSE。

## 结论
作者认为互模态内相似度作软监督、并改用 MSE，可在远小于 SOTA 的数据与 batch 下达到有竞争力的零样本分类与检索；任务最优配置因任务而异，无任务特定调优时推荐 MSE+T。

## 点评
核心是把“配对是否唯一正确”放松为“同 batch 语义邻近也应拉近”，并用音频侧镜像与不确定性混合扩展图像–文本先例；小 batch 下用 MSE 稳住软目标是务实洞察。比较是在作者限定的小数据体制下进行，与 CLAP23 等并非同算力/同数据公平对决；NSynth 仍偏弱，说明软目标对细粒度乐器家族未必充分。

