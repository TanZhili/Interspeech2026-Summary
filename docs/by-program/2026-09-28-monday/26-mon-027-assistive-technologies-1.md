# Assistive Technologies 1

- 日期：Monday 28 September 2026
- 时间：14:30-16:30
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

本场覆盖人工耳蜗前端、声码化言语的房间适应、听力损失对话轮次感知、可穿戴无声语音、非规范语音个性化 ASR，以及脑机语音假体的低内存 CTC 解码。共同目标是在严格延迟、功耗与可达性约束下提升感知与交流。

硬件近端：因果卷积前端服务 CI 音素分类并在 STM32 上验证亚 10 ms；声学侧比较不同沉浸年龄对房间条件的适应，瞳孔指标跨组相似。感知侧显示听损老人判断话轮结束时更依赖音高运动而非时长/强度。新界面与解码：SoniSpeech 提供开放词表三模态无声语音数据；VI LoRA 不确定性引导难音素过采样；LightBeam 用延迟融合 LLM 将脑机 CTC 解码内存从约 320 GB 降到约 10 GB。

## 论文技术总结

# Lightweight Convolutional Front-ends for Real-time Framewise Phoneme Recognition in Cochlear Implants

- 论文编号：2689
- 报告人：Yuchu Guo
- 程序：Monday 28 September 2026 / Assistive Technologies 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/guo26d_interspeech.pdf

## 问题
人工耳蜗端侧需因果、≤约 10 ms 时延的语音处理；音素级 TF 掩蔽增强依赖帧级音素分类，但缺少在 MCU 约束下对轻量卷积前端架构取舍的系统评测。

## 方法
在严格因果设定下，为 LSTM/GRU（及文中提及的 Mamba/注意力变体）加轻量卷积前端：Conv1D-F、Conv1D-T、Conv2D，含标准/膨胀层深 L∈{1,2,4,6,8}。交叉熵训练 2 s 片段。在 STM32F746G 上用 Cube.AI 测 flash/RAM/MAC/时延（可变形卷积、注意力、Mamba 因平台限制未上板）。

## 实验与结果
加卷积前端普遍抬升帧级音素准确率（如 GRU+Conv2D 8L 达 38.94%，无前端 Large GRU 约 34.34%）。1D 结构多数保持亚 10 ms 时延与小内存；Conv2D 深网络工作内存与时延急剧上升（8L 时延约 14 ms、RAM 约 78 kB）。膨胀卷积以可预期方式扩感受野。深度并非越深越好，常在 L=2–4 附近见峰。

## 结论
作者认为因果轻量卷积前端可提升 CI 相关音素分类，1D+膨胀是部署友好折中；并给出 MCU 实测资源表供架构选型。

## 点评
贡献偏工程基准：准确率–时延–内存三元权衡写清楚。音素准确率绝对水平仍不高（约 30–39%），但正文引用此前工作称这一水平已可助掩蔽增强。平台限制使部分先进模块缺部署数据；全文抽取后半略残缺，以 Table 1 与方法描述为主。


# Adaptation to Room Acoustics in Understanding Vocoded Speech: A Comparison Between Listeners With Varying Immersion Age

- 论文编号：113
- 报告人：Epri Pratiwi
- 程序：Monday 28 September 2026 / Assistive Technologies 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/pratiwi26_interspeech.pdf

## 问题
房间混响损害人工耳蜗可用的包络线索；听者可对稳定房间声学适应，但不同目标语浸入年龄（早/晚/未浸入）在 CI 仿真（vocoded）下是否同样适应、以及努力（瞳孔）是否同步变化尚不清楚。

## 方法
51 名正常听力听者按新西兰英语浸入分为早/晚/未浸入三组。UCAMST-P 三词句，非 vocoded 与 8 通道噪声 vocoded；用 31 扬声器球阵列重放实测研讨室/教堂（2 m/5 m）与消声条件。块状呈现同一房间连续 10 句诱发适应。词正确率 + 峰值瞳孔扩张（PPD）作可懂度与努力指标；线性混合模型分析。

## 实验与结果
非 vocoded 接近天花板，难观察适应；vocoded 可懂度显著更低且随房间/句序变化更强。环境×语音类型×句序三者交互显著；浸入组×语音类型交互显著，但浸入组×句序不显著——跨句适应轨迹各组相似。PPD 在 vocoded 更大、随句序总体下降（努力减轻），模式跨组大体一致。

## 结论
作者认为浸入年龄可影响降质语音识别水平，但对稳定房间声学的适应机制在各组间可能相似。

## 点评
用空间重放保留 HRTF、并用瞳孔补行为指标，设计扎实。用 NH+vocoder 模拟 CI，避开植入者个体差异但也限制外推。天花板效应使非 vocoded 适应结论受限；主要信息在“适应轨迹不依赖浸入年龄”。


# Towards an understanding of prosodic cue weighting for turn-end classification in older adults with varying hearing abilities

- 论文编号：2534
- 报告人：Lorenza Zaira Curetti
- 程序：Monday 28 September 2026 / Assistive Technologies 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/curetti26_interspeech.pdf

## 问题
话轮结束判断依赖时长、强度、音高等韵律线索；感音神经性听力损失可能改变线索可及性与权重，进而影响话轮时机，但直接证据不足。

## 方法
在线实验：55–75 岁英语听者，Digit Triple Test 分典型听力（TH, n=55）与听力损失（HL, n=57，未助听）。40 对陈述疑问句 finished/continuing（截断使语义相同），提取末词时长 Ttw、强度 dBtw、终升时长 Trise、音程 STrise。听者仅凭韵律判“说完/继续”。报告 d′/偏差，并对各组 finished/continuing 做秩回归选模型。

## 实验与结果
两组均显著高于机会（TH d′=0.28，HL d′=0.10；正确率约 61%/54%），组间灵敏度与偏差无显著差异，均略偏“finished”。continuing 条件声学预测弱。finished：TH 保留 dBtw×Ttw（短词时高强度伤正确率）；HL 保留 Trise+STrise（较短、较小终升对应更高正确率）。提示听力损失改变所用韵律维度而非全面丧失敏感性。

## 结论
作者认为听力损失会重塑话轮结束判断所依赖的韵律维度：典型听力更靠边界强度（时长/强度），听力损失更靠音高运动。

## 点评
探索性但线索权重差异清晰，对接话轮时序障碍机制。在线无纯音测听、未助听、刺激为单说话人精心朗读，生态效度有限；组间总体灵敏度差不大，差异主要在“用什么线索”。


# SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces

- 论文编号：1625
- 报告人：Ruidong Zhang
- 程序：Monday 28 September 2026 / Assistive Technologies 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26y_interspeech.pdf

## 问题
可穿戴静默语音接口要么开放词表但硬件侵入（电极/舌超声），要么形态友好但封闭小词表；缺大规模、公开、非接触声学传感数据支撑开放词表研究。

## 方法
发布 SoniSpeech：眼镜式 FMCW 超声（18–28/29–39 kHz）+ 可听音频 + 正面视频，三模态严格同步；发声与静默双模式、内容平行。语料取自 SODA 当代对话英语（归一化、5–25 词），单说话人约 34.1 h、18,000 句、5,356 词型、全 ARPABET 音素。基线：4 通道差分 echo profile（200 Hz）→ ResNet-34 + CTC + SentencePiece 1k。

## 实验与结果
首个开放词表声学传感静默识别基准：发声+静默联合训练在静默测试达 26.3% WER（静默-only 约 33.7%）；发声测试约 15.8%。数据规模上升 WER 持续下降。跨模态评测显示超声回波可承载语音信息。

## 结论
作者认为该数据集打破可穿戴 SSI 的词表瓶颈，证明开放词表静默识别在眼戴声学传感上可行，并提供基线与三模态扩展方向。

## 点评
贡献主要是基础设施：形态、规模与当代口语语料选择到位。单说话人限制泛化；26.3% WER 仍有较大空间，但作为“可解性”证明足够。发声–静默联合训练收益说明共享运动模式可迁移。


# Data-Efficient ASR Personalization for Non-Normative Speech Using an Uncertainty-Based Phoneme Difficulty Score for Guided Sampling

- 论文编号：776
- 报告人：Niclas Pokel
- 程序：Monday 28 September 2026 / Assistive Technologies 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/pokel26_interspeech.pdf

## 问题
非规范/障碍语音数据少、声学变异大，个性化微调易过拟合；均匀对待样本或简单熵不确定度难以区分不可学噪声与可学发音难点。

## 方法
用 VI LoRA（或 MCD）对 Whisper 做高效认知不确定度估计；构造音素难度 PhDScore=加权(错误率+熵+(1−真值一致率))；按句内音素平均难度过采样难句做 Full FT/LoRA/VI LoRA。评测 UA-Speech（英语构音障碍）与 BF-Sprache（德语 Apert，经语义重链）；并与一年间隔两次言语治疗报告做纵向相关。

## 实验与结果
过采样降低非规范错误（如 LoRA 在极低可懂度说话人 ∆WER 约 −15 pp），但伴随规范语音遗忘；混入规范样本可缓解。效能与可懂度大致反相关。复合 PhDScore 优于纯熵；须用预训练模型不确定度（微调后信号失效）。PhDScore 与临床报告音素难点更吻合。

## 结论
作者认为 VI LoRA 不确定度驱动的音素难度过采样可数据高效地个性化障碍语音 ASR，并与临床评估对齐。

## 点评
把主动学习式“难样本优先”落到音素级临床可解释信号，且证明熵不够。个性化–遗忘权衡写清楚。依赖对齐到音素与小数据设定；德语仅单儿童病例，外推需谨慎。


# Lightbeam: An Accurate and Memory-Efficient CTC Decoder for Speech Neuroprostheses

- 论文编号：2947
- 报告人：Ebrahim Feghhi
- 程序：Monday 28 September 2026 / Assistive Technologies 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/feghhi26_interspeech.pdf

## 问题
Brain-to-Text ’24/’25 领先方案依赖 WFST CTC 解码器，峰值 RAM 约 320 GB，难本地部署；直接多模态 LLM 在小神经数据上又弱于 WFST。

## 方法
LightBeam：非 WFST 的 GPU CTC beam search（源自 FlexCTC），用较小 4-gram 浅融合处理同音词；按固定间隔（约 1–1.25 s）对正交假设做 delayed fusion（Llama 3.2 1B 替换 N-gram 分），终局再 LLM 标点。配基线 GRU 或因果 time-masked Transformer；可选生成式纠错（Llama 3.1 8B）。开源 Python 实现。

## 实验与结果
基线 GRU：B2T’24 WER 9.37 vs WFST 重实现 9.71；B2T’25 公开/私有 5.77/6.47 vs 6.31/6.72；RAM ~10 GB vs ~320 GB，RTF 仍 <1。Transformer 上同样显著优于 WFST；配合 GEC 达已发表 SOTA。

## 结论
作者认为将 LLM 纳入一阶段 delayed fusion 可在大幅降内存下提升神经语音解码精度，适合临床本地部署。

## 点评
工程痛点极具体（320→10 GB）。delayed fusion 避开 WFST 大图与纯端侧 LLM 微调的弱势。仍需 GPU 与周期性 LLM 调用；RTF 高于 WFST 但峰值仍实时。对神经解码工具链可访问性贡献大。

