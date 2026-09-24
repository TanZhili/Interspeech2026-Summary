# Clinical and Inclusive Speech Technology

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Long Oral
- Area：
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场为临床与包容性语音技术长文 oral：构音障碍严重度估计的数据扩充、病理语音隐私保护变声、口吃研究与终端用户需求对齐、儿童语音发育自动测量、神经多样性话语的五十年回顾，以及 EEG 引导目标语音提取中的捷径学习。线索是技术必须对非典型语音稳健，并与临床与社区真实需求对齐。

数据稀缺推动伪标签教师、弱监督对比预训练与大规模典型语音迁移；纯数据驱动谱包络估计在病理模式上脆弱，物理知情声道共振模型被引入以增强可懂度与临床属性保留。社会与方法论层面，范围综述与利益相关方调查揭示研究议程与口吃者/言语治疗师需求的错位；神经多样性相关论文的话语分析批评医疗化、缺位参与与能力歧视语言。儿童侧 TinyVox/BabAR 把音素识别接到发育指标；脑机接口侧则指出试次内捷径导致跨试次泛化失败。

## 论文技术总结

# Something from Nothing: Data Augmentation for Robust Severity Level Estimation of Dysarthric Speech

- 论文编号：1390
- 报告人：Jaesung Bae
- 程序：Wednesday 30 September 2026 / Clinical and Inclusive Speech Technology
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/bae26_interspeech.pdf

## 问题
构音障碍严重度评估缺标注、难泛化；SAP 仅少量句子有 SLP 评分，直接监督受限，跨病因/语言更脆弱。

## 方法
三阶段：Whisper-large 教师在 SAP 有标子集上回归并给未标注样本伪标；用伪标 SAP + LibriSpeech（健康标为 1）做标签感知对比预训练（离散/连续/二值配对）；再在有标 SAP 上微调。评测 UASpeech、DysArinVox、EasyCall、EWA-DB、NeuroVoz 等未见集。

## 实验与结果
基线 SAP 测试 SRCC 0.719，跨域说话人级平均 SRCC 0.732；完整框架跨域平均 SRCC 0.761，并保持 SAP 内表现。消融显示弱监督与引入 LibriSpeech 对跨域稳健性关键。

## 结论
伪标 + 标签感知对比 + 健康语料扩增，可在几乎“无额外人工标注”下提升构音障碍严重度估计的跨域鲁棒性。

## 点评
充分利用 SAP 大量未标注与健康语音做表示塑形，问题抓得准。跨域标签体系（可懂度/MOS/TOM/MoCA/H-Y）异质，相关不等于临床可互换；伪标噪声仍可能固化教师偏差。


# Phy-VC: Physics-Informed Voice Conversion for Privacy-Preserving Pathological Speech

- 论文编号：378
- 报告人：Suhita Ghosh
- 程序：Wednesday 30 September 2026 / Clinical and Inclusive Speech Technology
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/ghosh26_interspeech.pdf

## 问题
病理/老年语音匿名化需去身份又保留诊断线索；纯数据驱动谱包络估计对口吃重复、不稳发声等 OOD 模式脆弱，黑盒声码器常抹平临床属性。

## 方法
Phy-VC 在 DDSP-QbE 上加入物理声道瓶颈：预测可微 articulatory 参数→面积函数→Webster 代理求共振峰/带宽→Lorentzian 滤波；目标池韵律映射减轻源说话人泄漏；可用 α6（喉高/有效声道长）可控改说话人大小。标准语音训练，评测口吃、痴呆、老年、情感等。

## 实验与结果
相对 Emo-StarGAN、KNN-VC、DDSP-QbE，正文报告在多数据集上可懂度、韵律与自然度更优并保持有效匿名；SLP 专家评估确认临床相关属性显著保留。

## 结论
把 articulatory–acoustic 耦合作为归纳偏置，可提升病理语音匿名 VC 的稳健性与可解释可控性。

## 点评
物理约束对准“非典型发声 OOD”很有说服力，且给出临床专家验证路径。实现与损失项较多，依赖 Praat 等伪标签监督；匿名–效用权衡的攻击面细节需结合全文表格细读。


# Aligning Stuttered-Speech Research with End-User Needs: Scoping Review, Survey, and Guidelines

- 论文编号：1704
- 报告人：Hawau Olamide Toyin
- 程序：Wednesday 30 September 2026 / Clinical and Inclusive Speech Technology
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/toyin26b_interspeech.pdf

## 问题
口吃语音技术研究增长，但任务命名混乱、评测少锚定终端用户；PWS 与 SLP 对“正确转写/有用输出”的需求常与现有基准脱节。

## 方法
范围综述 228 篇（2010–2025）并标注领域/语言/利益相关者/开源；提出任务分类法（意图 vs 逐字识别；分类/检测/严重度等）；调查 40 名 PWS 与 30 名 SLP；对照分析对齐缺口并给出指南。

## 实验与结果
文献以 stutter identification 为主（约 170 篇），识别与治疗工具相对少；任务命名与输出粒度不一致。调查显示 PWS/SLP 对“意图转写 vs 逐字转写”、临床文档与沟通辅助等优先项存在分歧，且与主流研究侧重不完全一致。文末给出面向用户中心评测与跨学科协议的具体建议。

## 结论
当前议程与终端用户需求存在系统错位；标准化任务命名并更早纳入 PWS/SLP 是缩小差距的关键。

## 点评
把综述分类法与利益相关者调查并置，对社区议程设置很有价值。样本与检索范围仍有偏；“指南”可操作性取决于后续基准是否真正按分类法重建。


# BabAR: from phoneme recognition to developmental measures of young children's speech production

- 论文编号：1132
- 报告人：Marvin Lavechin
- 程序：Wednesday 30 September 2026 / Clinical and Inclusive Speech Technology
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/lavechin26_interspeech.pdf

## 问题
婴幼儿语音发展研究依赖昂贵人工音素转写，难规模化；儿童（尤其低龄）ASR/音素识别仍极难，公开跨语标注稀缺。

## 方法
整理 TinyVox（PhonBank 标准化）：>50 万条 IPA 转写发声、560 名儿童、5 语、约 388 小时。训练 BabAR：比较多种 SSL 预训练（含儿童日长录音），用 CTC；微调时提供约 20 秒周围音频上下文。在留出纵向数据上提取典型/规范发声比例等发展指标并与文献对照。

## 实验与结果
多语儿童日长录音预训练显著优于成人-only 等替代；加长上下文进一步降错。替换多落在宽语音类别内，适于粗粒度发展分析。自动成熟度指标与文献发展估计对齐。相对既往约 60% PER 的儿童音素系统，正文报告显著改进（精确数字见全文表）。

## 结论
大规模跨语儿童音素数据 + 儿童中心 SSL + 上下文微调，使自动发展度量变得可行。

## 点评
TinyVox/BabAR 直接打通“标注债”与发展科学发展需求。音素清单跨语归一与 CTC 对齐误差仍在，细粒度临床音位诊断需谨慎；公开资源对复现价值高。


# Making Room for Speech Diversity: A 50 Year Retrospective of Speech Science and Technology through a Neurodivergent Lens

- 论文编号：2962
- 报告人：Shaomei Wu
- 程序：Wednesday 30 September 2026 / Clinical and Inclusive Speech Technology
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/lietz26_interspeech.pdf

## 问题
Interspeech 对“非典型/多样语音”兴趣上升，但研究话语如何框定神经多样性、是否真正包容利益相关者，缺少长时段批判性回顾。

## 方法
以神经多样语音为案例，对 1976–2025 年 Interspeech 与 ICASSP 相关论文做范围综述与内容/话语分析，考察动机、数据与评价实践、贡献表述及语言用法。

## 实验与结果
识别三类反复问题：（1）医疗化/干预主义框定，把神经多样特质当待矫正缺陷；（2）神经多样个体极少参与研究过程；（3）能力主义语言加剧边缘化。据此提出更贴近“all voices”目标的路径：问题定义扎根体验、伙伴式合作、反能力主义实践。

## 结论
多样性技术议程若停留在“矫正非典型”，会偏离包容目标；需要从话语、流程到评价标准的结构性转变。

## 点评
话语分析补足纯技术综述盲区，对社区反思有直接价值。作为回顾性立场文，不提供新系统/数据集；分类与编码主观性需读者结合方法部分判断外推力度。


# Breaking Shortcut Learning for Cross-Trial EEG-Guided Target Speech Extraction via Two-Stage Training

- 论文编号：595
- 报告人：Wonchul Shin
- 程序：Wednesday 30 September 2026 / Clinical and Inclusive Speech Technology
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shin26_interspeech.pdf

## 问题
端到端 EEG 引导目标语音提取（TSE）在 within-trial 上 SI-SDR、attended-source accuracy 很高，但严格 cross-trial 时会崩塌。原因是 trial 内注意目标固定，模型可把 trial 特异 EEG 结构当“捷径”映射到目标说话人，而非学到与语音对齐的注意相关表征。

## 方法
提出 TRUST-TSE 两阶段框架。(1) Stage 1：对比预训练 EEG 编码器，将 EEG 段与对应 attended 语音的 mel 嵌入对齐；关键是 attended-speaker negative sampling——负样本取自同一 attended 说话人的其他非对齐段，使 trial 身份线索对对比损失无用。(2) Stage 2：冻结 EEG 编码器，用其嵌入条件化提取器；损失为基于 EEG–source 相似度差的 confidence-weighted SI-SDR（权重 \(w=\tanh(\kappa\Delta)\)），强调 EEG 对 attended/ignored 区分清晰的样本。诊断实验含 NeuroHeed 线性探针测 trial 可解码性，以及 test-time EEG shuffle、trial-wise EEG–audio permutation 等 mismatch 压力测试。

## 实验与结果
在 KUL 上，NeuroHeed within-trial 中位准确率近 90%，cross-trial 低于 chance，且常出现强负 SI-SDR。线性探针 8-way trial 分类准确率约 55–76%（远高于 12.5% chance）。两种 mismatch 压力测试下 within-trial SI-SDR/准确率几乎不变（约 12 dB / 87%），表明高分可不依赖段级 EEG–语音对齐。全文抽取在 Stage 1 负采样细节与完整对比表处截断，KUL/DTU 上 TRUST-TSE 相对端到端基线的完整数字未完整读到；摘要称其在严格 cross-trial 协议下优于端到端基线。

## 结论
作者认为 within-trial 高分常由 trial 捷径驱动，两阶段对比预训练加置信加权提取是提升 trial 鲁棒性的可行路径；TRUST-TSE 作为起点，代码已公开。

## 点评
问题诊断扎实：探针 + mismatch 实验把“高 within-trial ≠ 真正注意跟踪”说得很清楚。两阶段把表征学习与提取解耦，负采样设计直接针对 trial 身份捷径。全文在方法后半与主实验结果处被截断，点评无法核对 DTU/消融的具体增益；若完整结果与摘要一致，价值在评价协议与训练范式，而非单纯刷 within-trial 数字。

