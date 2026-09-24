# Emotion, Prosody, and Articulation

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Long Oral
- Area：
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场连接副语言感知、多模态情感融合与发音/声学工具：音频讽刺识别强调时间韵律不一致；联邦对抗学习同时护数据隐私与 SER 鲁棒性；多模态情感融合把“单模态精炼”与“跨模态交互”在架构上拆开；另两篇从发音地标库与交互式共振峰校正工具侧支撑可复现的发音与小语种语音学研究。

情感与韵律侧，局部韵律动态与整句情绪基线的错配成为可计算信号；不确定性估计与起终点定位无需帧级标签即可对齐人类感知。隐私与对抗威胁推动联邦学习 + 对抗训练 + 测试随机化的两阶段防御。多模态方面，纠缠式融合被替换为隔离通路、各自精炼、延迟全交互的先验。

发音与资源侧，用物理声道合成器按地标模式生成大规模带精确时间标注的词库，反转“地标标注稀缺”问题；面向少文献语言的交互式共振峰可视化与多算法校正，则把人工核验嵌入可复现工作流。

## 论文技术总结

# ProSarc: Prosody-Aware Sarcasm Recognition Framework via Temporal Prosodic Incongruity

- 论文编号：3451
- 报告人：Prathamjyot Singh
- 程序：Thursday 1 October 2026 / Emotion, Prosody, and Articulation
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/singh26e_interspeech.pdf

## 问题
口语讽刺大量依赖韵律，但既有音频方法多用句级统计或隐式时序编码，缺少把讽刺显式建模为“局部韵律动态相对全局情绪基线的不一致”。

## 方法
ProSarc 双路径：Global Emotion Encoder 用 librosa 提 10 维句级韵律统计 → MLP → pglobal；Temporal Prosody Encoder 用 Wav2Vec2/HuBERT/WavLM（仅微调最后两层）→ BiLSTM → 多头注意力 → 注意力池化得 plocal。Prosodic Incongruity Analyzer 由 [plocal;pglobal] 产生标量不一致分数 s，做自适应融合后再分类（加权 BCE）。用 at·dt 弱监督估计讽刺起时；分类头 MC dropout（T=10）给不确定性。最佳配置为 WavLM-Large。

## 实验与结果
MUStARD++：F1 75.3、Acc 73.3；MUStARD：F1 77.0；PodSarc：F1 62.9；德语 MuSaG：F1 65.6。相对无不一致建模，10 次运行 Wilcoxon p=0.002、Cohen’s d=1.51。优于先前音频-only 报告（如 MUStARD++ 上 Ray 64.5、Tiwari 66.6）。预测讽刺起时多落在句后 70–80% 位置。人类评价显示不确定性与感知歧义相关（正文 Table 6 抽取截断）。

## 结论
显式时序韵律不一致可提升纯音频讽刺检测，并在脚本/自发/跨语料上泛化；弱监督起时与不确定性提供可解释性。

## 点评
把心理语言学“韵律反差”落成可学习标量门控，比堆 SSL 容量更有机制叙事；大编码器仍主导增益，不一致项是边际但统计显著的补强。自发与跨语 F1 明显低于脚本对话，说明夸张韵律假设在自然对话中变弱。后文不确定性人评表抽取不全，相关结论以摘要为准。


# A Two-Stage Defence for Robust Federated Speech Emotion Recognition

- 论文编号：1125
- 报告人：Yi Chang
- 程序：Thursday 1 October 2026 / Emotion, Prosody, and Articulation
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chang26b_interspeech.pdf

## 问题
边缘设备上的 SER 同时面临数据隐私与对抗攻击脆弱性：集中上传语音有泄露风险，DNN 又易被 FGSM、PGD、DeepFool 等人不可感知扰动误导。现有联邦 SER 多偏隐私，对推理阶段白盒攻击的系统性防御不足。

## 方法
提出两阶段防御的联邦对抗学习框架。各客户端本地提取 log Mel spectrogram；训练阶段从第二轮起将本地数据对半拆分，一半生成白盒对抗样本后与干净半集联合做 vanilla adversarial training（损失为干净与对抗项的 α 加权）；服务器做联邦平均聚合。推理阶段对 log Mel 做随机缩放与随机 padding，以削弱单步与迭代攻击。

## 实验与结果
计划在意大利情感语料 DEMoS 上验证：排除中性类后保留 9,365 条、七类情感（anger、disgust、fear、guilt、happiness、sadness、surprise），68 说话人、平均时长约 2.86±1.26 秒。正文声称两阶段防御优于 vanilla FL 与任一单阶段防御。全文抽取在实验设置与数据集介绍处截断，具体 EER/准确率等数字未见。

## 结论
作者认为该框架可在本地保护语音数据，并对一系列白盒对抗攻击提升模型鲁棒性；随机化与对抗训练互补，覆盖单步与迭代攻击。

## 点评
把隐私（FL）与鲁棒性（对抗训练 + 测试时随机化）绑成同一流水线，针对 SER 边缘场景较贴切。全文抽取在结果段前截断，无法核验攻击强度与干净样本性能折损；随机化对干净数据的影响依赖 β、γ 调参，正文完整版中的消融未见。


# Segregate, Refine, Integrate: Decomposing Multimodal Fusion for Sentiment Analysis

- 论文编号：1299
- 报告人：Alexandros Potamianos
- 程序：Thursday 1 October 2026 / Emotion, Prosody, and Articulation
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/filippakopoulos26_interspeech.pdf

## 问题
多模态情感分析需同时精炼单模态表征并建模跨模态交互，二者常被缠在同一融合操作里；DeepMLF 等用可学习 fusion token，但 token 池未区分模态，交互拓扑缺少结构性约束。

## 方法
提出 SeRIn（Segregate, Refine, Integrate）：在冻结预训练 LM 上，将 fusion token 分成 audio / visual / audiovisual 三组；用无参数的模态约束注意力掩码隔离单模态通路，AV 通路只读不写；MM Block 内以 Internally Gated Cross-Attention（IGCA）注入对应编码器上下文，再以模态约束 IGSA 巩固；仅在最终 Integration Head 解除隔离做全交互。AV Encoder 与 DeepMLF 对齐并固定，以隔离“交互拓扑”这一变量。

## 实验与结果
摘要称在 CH-SIMS 与 CMU-MOSEI 上相对已有方法达到 SOTA、各项指标均提升；消融显示收益来自结构化交互而非额外容量；视觉损坏下门控出现无监督的模态重加权。全文抽取在 MM Block / IGSA 公式中途截断，表格与具体数值未见。

## 结论
作者认为将单模态精炼与跨模态整合在架构上分阶段，比仅靠优化惩罚更能保证模态特化；交互拓扑应与深度、容量并列为融合设计轴。

## 点评
用掩码固定“何时混、何时不混”，比软正交损失更可解释。全文后半（完整实验与门控分析）缺失，SOTA 数字无法从可读写正文核对；依赖 DeepMLF 式冻结 LM + fusion token，适用范围主要在该范式内。


# An Acoustic Landmark Database of the English Lexicon via Articulatory Synthesis

- 论文编号：1374
- 报告人：Mateo Cámara
- 程序：Thursday 1 October 2026 / Emotion, Prosody, and Articulation
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/camara26_interspeech.pdf

## 问题
声学 landmark 标注语料稀缺，人工标注贵且有分歧；连续语音中协同发音又使“应有”事件模糊。自动标注（如 Auto-Landmark on TIMIT）尚缺独立校验，难作可靠 ground truth。

## 方法
用 Pink Trombone 物理声道合成器，从 CMUDict→IPA 词表生成整部英语词表：为每个音素手工映射静态构音目标，词内线性插值做有限协同发音，固定音长与 f0，分别合成成人男/女两套解剖参数。按规则在闭塞、爆破、摩擦启停、鼻音闭开、元音/滑音中点等物理时刻算法放置八类 landmark（V、G、Sc、Sr、Fc、Fr、Nc、Nr）。产出 ALLIE-PT：波形 + 关键帧 JSON + landmark 时间戳。

## 实验与结果
单性别统计：115,487 词、1,100,803 个 landmark；辅音类 676,646、元音/滑音类 424,157，辅音/元音 landmark 比约 1.595。频次最高为 V（279,980），其次 Sc/Sr（各 153,181）、G（144,177）等。语料 >200,000 合成词、双配置、48 kHz/16-bit；可懂度用 STOI（正文抽取段未给出具体分数）。音位结构分析在 4.3 节开头截断。

## 结论
作者认为由构音命令“生成”而非从声学事后推断 landmark，可提供无人工标注误差的沙盒，用于验证 landmark 理论并训练/评测自动检测器；词级、非韵律、有限协同发音是刻意简化边界。

## 点评
把标注问题倒转为可控合成，适合做检测器基准与词典级统计。常音长、常 f0、弱协同发音远离自然连续语音，迁移到真实数据时需额外适配；全文抽取未含 STOI 数值与后续音位模式细节。


# NewAppVoice: Tools for Visualizing and Correcting Acoustic Measures

- 论文编号：2560
- 报告人：Amélie Elmerich
- 程序：Thursday 1 October 2026 / Emotion, Prosody, and Articulation
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/elmerich26_interspeech.pdf

## 问题
羌语、藏语支等少文书写语言缺乏参考共振峰值，Praat / VoiceSauce 等自动提取常有系统误差，必须靠目视与手改；大批量脚本又缺少交互反馈，可复现性差。

## 方法
NewAppVoice 以 .wav + TextGrid 为输入，在统一界面同步显示波形、语图、多算法轨迹与结果表。基频并行三种算法（STRAIGHT、SHR、Praat 自相关）；共振峰并行 STRAIGHT（LPC 点）与 Praat Burg（连续轨迹），可对照频谱/LPC 包络手工改错；并支持强度（dB RMS / 线性 RMS）、HNR、CPP 等。MATLAB App Designer 开发，已编译为免许可证的 macOS/Windows 可执行文件。

## 实验与结果
以白马藏语 /dzɑ̀/「月亮」、麻窝羌语 /ti/「黑熊」等实例演示：如 Straight F4 估到约 5000 Hz 而频谱峰在 3500–4000 Hz，可用 Praat 列校正（表中 F4 4861→F4Praat 3731 等）。属工具演示与案例分析，无大规模基准对比数字。全文在 HNR 小节标题处截断。

## 结论
作者认为将多算法提取与持续可视化、结构化手改结合，能提高少书语言声学测量的可靠性与可复现性；软件开源开放获取。

## 点评
面向纪实语音学痛点——“无参考值时如何发现并改正自动错误”——交互比纯批处理更务实。全文抽取未覆盖语音质量模块后半与系统评测；效果依赖标注者对语图/频谱的判读能力，非端到端自动鲁棒性声明。

