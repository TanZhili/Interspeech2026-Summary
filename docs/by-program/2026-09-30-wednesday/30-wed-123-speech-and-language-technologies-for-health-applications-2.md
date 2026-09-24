# Speech and Language Technologies for Health Applications 2

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
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

本场聚焦认知障碍与精神健康相关的言语技术：零样本跨语阿尔茨海默检测、认知状态条件 TTS 增强、临床知情加权言语图、病因感知构音障碍 ASR、半监督老年 ASR，以及弱监督抑郁检测。

跨语与数据稀缺是主轴：ORBIT 用多模态双几何对抗学习语言不变表示；CoSTA 用 CS 条件 TTS 与 ASR 转写池扩增 AD 检测数据。可解释性方面，WSG 把临床动机属性写入言语图，少数特征即可接近全基线表现。构音障碍识别强调把病因推理嵌入自回归生成流，而非仅作辅助分类。老年与抑郁场景则分别用置信引导增量伪标签与标签校正双流多示例学习应对弱/半监督噪声标签。

## 论文技术总结

# Synergizing Zero-Shot Cross-Lingual Alzheimer Detection with Language-Invariant Multimodal Bi-Geometric Adversarial Learning

- 论文编号：2756
- 报告人：Muskaan Singh
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/girish26b_interspeech.pdf

## 问题
基于语音的阿尔茨海默检测（SADD）需跨语言零样本迁移；单模态预训练表征易泄漏语言身份，简单拼接融合难以抑制语言特异伪线索。

## 方法
提出 ORBIT：冻结/浅层解冻多语语音与文本 PTM，注意力池化后双向交叉注意融合；在融合表征、球/双曲几何投影与聚类责任上施加多点 GRL 语言对抗；球空间与 Poincaré 球上做共识聚类与原型 PoE 投票分类。数据：Pitt（英）、Ivanova（西）、NCMMSC（中）、Dem@Care（希，Whisper-large-v3 转写），二分类 AD vs HC。协议含 LTLO 与 LOLO。

## 实验与结果
合并语种上 CNN 通常优于 FCN；单模态最强为 mHuBERT 与 BERT。零样本下 ORBIT+交叉注意优于单模态与拼接：LOLO 最佳 mHuBERT+Qwen3 达 86.98 Acc / 85.29 F1；LTLO 最佳 Acc 为 mHuBERT+E5（85.49），最佳 F1 为 Whisper+E5（83.34）。消融：去掉 GRL 或仅单几何均下降，完整球+双曲+对抗最好。

## 结论
多模态融合加语言不变约束能提升零样本跨语 SADD；交叉注意与双几何+多点对抗是关键。作者称相对既往 Whisper 迁移等单模态 SOTA 有提升。

## 点评
把「模态互补」与「去语言泄漏」拆成交叉注意、多点对抗与双流形共识，针对零样本跨语设定合理。异构语料（任务、录音条件、希语 ASR 转写）可能仍残留域差，语言对抗未必消尽任务混杂；合并集上单模态 Acc 已很高，跨语跌落更说明迁移难度在语言/域偏移而非可分性本身。


# CoSTA: Cognitive-State-Conditioned TTS Data Augmentation Using ASR Transcripts for Alzheimer’s Disease Detection

- 论文编号：88
- 报告人：Yin-Long Liu
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/liu26_interspeech.pdf

## 问题
语音 AD 检测受病理数据稀缺制约；传统扰动难引入新语义或 AD 特异不流畅，而标准 TTS 常抹平病理韵律；用手工转写还是 ASR 转写驱动合成亦未系统比较。

## 方法
提出 CoSTA：用认知状态指令微调 CosyVoice2（AD/HC 两套）并在 F5-TTS 中加入 cognition embedding，使合成可控为 AD-like 或 HC-like。构建含 MT 与 36 路 ASR（18 预训练+18 微调，跨 Wav2Vec2/HuBERT/WavLM/Whisper）的转写池驱动合成；训练增强含自参考 2× 与类内交叉参考更高倍数；测试时用无指令零样本 CosyVoice2 做 TTA 概率平均。检测器为 WavLM 加权层融合+注意力池化+MLP。

## 实验与结果
ADReSS：基线准确率 81.67%。CS-Cond 相对预训练 TTS 更常超过基线（CosyVoice2 28/37 vs 7/37）。多数情况下 ASR 驱动优于 MT。增强倍数呈倒 U，约 2× 最优。摘要报告 CoSTA 相对基线提升 4.16%，测试集仅音频准确率 85.83%。CS-Cond 在 MCD/FAD 等客观指标上亦更接近真值。

## 结论
认知状态条件 TTS 提升合成样本对 AD 检测的效用；ASR 错误可增加诊断相关多样性；适度增强优于过度合成。

## 点评
把「病理说话风格」显式条件化，比无差别扰动更贴诊断目标；ASR 驱动有效说明识别错误可能编码病理声学线索。过度增强易过拟合 TTS 伪迹，部署需控制合成占比；TTA 在无类标时退回无条件合成，与训练时 CS-Cond 不完全对称。


# WSG: Clinically-Informed Weighted Speech Graphs for Dementia Detection

- 论文编号：2266
- 报告人：Yao Xiao
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/xiao26b_interspeech.pdf

## 问题
Speech graph 能刻画词检索结构，但既往节点仅为抽象词，未编码语义、发音切换与 Cookie Theft 的空间 CIU 信息，难对齐临床切换/叙事效率指标。

## 方法
提出 Weighted Speech Graphs（WSG）：仅用目标词（SVF 动物、PVF 以 p 开头真词、CTD 的 CIU）建有向图；边权为语义（ConceptNet Numberbatch）、音系（SoundVectors）、空间（CIU 坐标欧氏距离）与时间间隔的距离/相似度，再按拓扑特征极性选择。特征含 N、E、WC 及加权/未加权 diameter、ASP、density、ATD。用朴素贝叶斯与嵌套交叉验证上的 SFS；开源 PyWSG。

## 实验与结果
CognoMemory（SVF/PVF/CTD）与 ADReSS（CTD）。仅用目标词相对全转写显著提升（如 PVF F1/AUC 0.55/0.56→0.75/0.75）。SFS 常只选 1–2 个特征即可接近全基线特征集；PVF 常选 diameter(phon)（痴呆组均值 2.8 vs HC 5.3）；SVF 多见时间加权直径；CTD 多见空间加权 ASP/ATD 与 WC。ADReSS 上最终子集 F1/AUC 0.73/0.75，与目标词+基线特征相当。

## 结论
临床属性边权使极少特征即可匹配完整未加权特征集，并提供可解释的切换/空间/时间模式；目标词构图是关键前提。

## 点评
把临床切换与 CIU 空间叙事直接写进边权，比纯拓扑更可解释。依赖 ASR（CognoMemory）或词典抽取目标词，抽取误差会扭曲图；特征选择在小样本上折间波动大，最终子集宜视为稳健候选而非唯一真值。


# Etiology-Aware Speech Language Models for Dysarthric Speech Recognition

- 论文编号：1773
- 报告人：Moreno La Quatra
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/laquatra26_interspeech.pdf

## 问题
标准 ASR 忽略说话人神经病因，难利用病种特异声学–语音模式；如何把病因知识放进语音语言模型仍不清楚。

## 方法
在 SLM 上比较四种策略：标准 SFT；辅助病因分类头（EC，预测不进入解码器）；输入提示给出病因（EH）；自回归先预测病因再转写（EP）。在 Kimi（SAP 上 SFT 最强）上用 LoRA 做 EC/EH/EP；SAP 含 ALS、Parkinson、Stroke、Down Syndrome、Cerebral Palsy；零样本测 TORGO。

## 实验与结果
SAP：Kimi-EP 总体 WER 7.77%、SemScore 91.05，相对 SFT 8.30% 相对降 6.4%（p<0.001）。EC 病因准确率 81% 高于 EP 的 72%，但 WER 8.49% 更差。EH 为 8.22%。EP 在五类条件上均优于 SFT/EC/EH；低资源 Stroke 上 EP 相对 SFT 相对降约 19%。TORGO：EP 总体 15.8% 优于 EH/EC/SFT。EP 误分样本 WER 不差于正确预测，暗示「预测行为」本身迫使模型关注病理声学。

## 结论
病因推理须进入生成流才能惠及转写；自生成临床评估优于被动提示，且推理时无需病因标签。训练仍需病因标注。

## 点评
关键对照是「准确率高但未进解码器的 EC」vs「准确率较低但因果条件化的 EP」，说明放置位置重于分类精度。EH 有 oracle 病因仍逊于 EP，支持主动推理假说。健康说话人无 SAP 标签时 EP 被迫归因，跨域提示设计仍需谨慎。


# Confidence Score Guided Incremental and Speaker Adaptive Pseudo-Labeling for Semi-Supervised Elderly Speech Recognition

- 论文编号：1611
- 报告人：Chengxi Deng
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/deng26c_interspeech.pdf

## 问题
老年语音标注贵、伪标签不可靠，且说话人异质性强；直接过滤丢弃低置信样本会伤说话人覆盖，无可靠度排序的增量训练易早期污染并误差累积。

## 方法
为 Whisper 设计轻量 CEM（3 层残差 FFN，拼解码输出与 top-10 logits）估 token/话语置信度。按说话人内置信度降序均分 K 组再跨说话人聚合；从高到低增量：每步用当前模型重标下一子集并与已累积数据合并训练。再把每步微调换成说话人提示 SAT（提示长 4+LoRA），可选测试时适应与说话人自适应重标。骨干 Whisper-medium。

## 实验与结果
DementiaBank Pitt 与 JCCOCC MoCA：默认 10% 说话人有标、其余无标。相对全量伪标签半监督基线，提出方法绝对降 WER/CER 1.45%/2.27%（相对 6.21%/6.98%）。置信过滤优于随机；置信排序增量优于随机划分增量；增量+SAT 进一步提升，低置信子集伪标签质量改善最大（如 Pitt Rank5 WER 63.77→约 55）。

## 结论
置信度课程式增量与说话人自适应伪标可逐步提高老年语音半监督 ASR，并支撑未见说话人的测试时适应。

## 点评
「说话人内排序」避免扔掉整个人的困难话语，比全局 top-k 过滤更适合异质老年群体。课程从易到难抑制早期误差雪崩。依赖说话人 ID 已知，与病历场景匹配，但不适用于完全匿名无说话人聚类的数据。


# Label Correction Enhanced Dual-Stream Multiple Instance Learning for Weakly-Supervised Depression Detection in Speech

- 论文编号：1716
- 报告人：Xinzhou Xu
- 程序：Wednesday 30 September 2026 / Speech and Language Technologies for Health Applications 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/sun26e_interspeech.pdf

## 问题
语音抑郁检测在弱监督下同时面临不准标签（标注/问卷错误）与不精确标签（抑郁线索仅在录音局部）；既往工作少同时处理二者。

## 方法
提出 LC-DMIL：样本级 1D-CNN+Bi-LSTM 骨干上融合似然比翻转与原型余弦相似度校正（权重 γ），得到校正标签；再把样本切为实例袋，双流 MIL（max-rule 找关键实例 + 基于关键实例的 MIL-aggregator）融合输出；样本/实例损失含分类与熵项。输入 80 维 log Mel。

## 实验与结果
DAIC-WOZ（AVEC 2017 划分）：交换 PHQ-8∈[7,12] 的训练标签模拟不准监督。LC-DMIL UAR 0.651、F1 0.642，优于 DepAudioNet、SpeechFormer、SLLC 等（UAR 差异 p<0.005）。γ=0.3 优于 0.7；双流优于单流与 mean/attention 等替代。AVEC 2014 随机翻 3/7 标签时 UAR 0.670，亦优于仅 LC 或仅 MIL。

## 结论
标签校正处理不准监督、双流 MIL 处理不精确监督，二者结合在弱监督语音抑郁检测上有效。

## 点评
把「标错」与「标粗」拆成校正模块与实例袋学习，问题分解清晰。弱监督靠人为翻边沿 PHQ 分数构造，与真实标注噪声分布可能不同；μ、实例数等超参敏感，部署需验证集重调。

