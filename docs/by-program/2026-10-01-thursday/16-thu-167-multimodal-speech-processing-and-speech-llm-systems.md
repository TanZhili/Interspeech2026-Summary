# Multimodal Speech Processing and Speech LLM Systems

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：10
- 论文数：7

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场连接语音感知 LLM 的时间戳与领域适应、音频—语言模型提示学习泛化、多模态情绪无监督预训练、音视频“谁何时说了什么”，以及视频引导的 ASR 后修正与多说话人流式日志前端。主线是在单一 Speech-LLM/多模态骨干上模块化扩展能力，同时缩小语音—文本模态间隙与屏外说话人等现实缺口。

Speech-LLM 侧，两步生成（先转写再带时间戳重生成）与激活 LoRA 复用 KV-cache，在不损 WER 下把对齐误差压到数十毫秒量级；少量目标域语音经混合批即可逼近全量成对微调。ALM 提示学习用零样本熵正则融合 logits 缓解基类过拟合。情绪与场景理解则靠掩码/去噪重建与动量对比学通用表示，或用专用缺席 token 统一屏上/屏外说话人。

多媒体纠错与可穿戴多说话人理解方面，VLMM 捕获剧集视频上下文修正 ASR；源分离 + 统计分类器替代脆弱阈值日志，并用 Conformer 与多几何模型兼顾效率与不同智能眼镜麦克风布局。

## 论文技术总结

# Parameter-Efficient Adaptation of Speech-Aware LLMs for Timestamp Prediction

- 论文编号：2441
- 报告人：Avihu Dekel
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sunder26_interspeech.pdf

## 问题
词级时间戳对字幕、检索等重要，但 one-pass 交错生成会伤转写质量；独立对齐模型又难并入 speech LLM。需在单一 speech LLM 内做 SRWT，且参数高效、不破坏已有 ASR/AST 能力。

## 方法
两步：先 ASR 转写，再在转录条件上再生带词末时间戳与静音标记 的序列（10 ms 单位）。三种适配：Non-Mod 持续微调 projector+LoRAA；Mod-LoRA 冻结合并后的基座 LoRA，另训时间戳 LoRA（两 pass，需重算 KV）；Mod-aLoRA 用 activated LoRA，遇 `<|timestamp|>` 才激活适配器，可复用第一步 KV cache。基座为 Conformer 编码器 + Q-Former + 1B LLM。

## 实验与结果
训练数据含 LibriSpeech、MLS、CommonVoice、VoxPopuli 等，时间戳经 MFA 并按 CTC AAS 过滤。英文平均 AAS：Non-Mod 27.1 ms（相对最佳基线 Qwen3-FA 41.8 ms 降约 35%）；多语 Mod-aLoRA 21.2 ms 最佳。SRWT WER 与基座 ASR 同为英文 7.3%、多语约 5.3%。仅英语 SRWT 训练时，Mod-aLoRA 零样本多语 AAS 37.3 ms，远优于 Non-Mod 的 339.5 ms。

## 结论
两步 SRWT 保转写质量；Mod-aLoRA 兼顾模块化与 KV 复用，对齐误差达 SOTA，并具跨语零样本迁移。

## 点评
把“写什么”与“何时”拆开，再靠 aLoRA 复用基座 KV，切中 speech LLM 多任务扩展痛点。时间戳监督强依赖 MFA/过滤质量；Non-Mod 对齐更好但破坏模块化，实际选型需权衡。


# ZEBRA: Zero-Shot Entropy-Regularized Prompt Learning for Base-to-Novel Generalization in Audio-Language Models

- 论文编号：261
- 报告人：Asif Hanif
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hanif26_interspeech.pdf

## 问题
ALM 的 prompt learning 能抬高 base 类准确率，却常使 novel 类低于零样本，暴露 base-to-novel 泛化缺口：仅用 base 监督会过拟合并扭曲预训练语义对齐。

## 方法
提出 ZEBRA：在现有 COOP/COCOOP 等 prompt 方法上无新增参数。训练与推理将零样本 logits 与 prompt logits 线性融合（λ_zs=λ_pr=0.5）；训练时在交叉熵上减去（最大化）融合分布的自熵，抑制对 base 类过度自信。零样本 logits 一次性算好可复用，开销可忽略。骨干为 Pengi 的音/文编码器（对比式）。

## 实验与结果
11 个音频分类集、每 base 类 16-shot、50 epoch。COOP/COCOOP 平均 novel 相对零样本下降约 7.13%/4.74%；加 ZEBRA 后 novel 平均升至约 59.4%/59.5%（相对零样本 +4.19%/+4.31%），base 仍保持高位（约 80%/82%）。消融显示零样本 logits 融合贡献最大，熵项边际增益；训练/测试时间几乎不变，novel ECE 下降。

## 结论
零样本锚定 + 自熵正则可在不增参数下缩小 ALM prompt learning 的 base–novel 差距。

## 点评
问题诊断清楚：抬 base 伤 novel 是常见过拟合症状；融合零样本 logits 比再学参数更轻。局限是固定 λ 与 0.05 熵缩放靠经验，部分数据集（如 CREMA-D）novel 仍低于零样本，说明并非处处有效。


# MultiEmoVec: Learning Generalised Multimodal Emotion Representation by Momentum Contrast and Multi-task Reconstruction

- 论文编号：1563
- 报告人：Junchen Liu
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liu26m_interspeech.pdf

## 问题
多模态情感识别缺大规模标注，且情感库常有噪声与模态缺失；聚类或文本锚定对比在文本不可靠时脆弱，图融合计算重。需无情感标签的可迁移表征。

## 方法
MultiEmoVec 无监督预训练：Wav2Vec/MA-Net/DeBERTa 提语音/视频/文本特征；双重建含随机掩蔽单模态 20% 维的 masked reconstruction，与 mixup+掩蔽+高斯噪声的 denoising reconstruction；9 嵌入（3 单模态 + 6 交叉注意力）经 transformer 融合；MoCo 对比；ALS 按 EMA 平衡对比与重建损失。预训练后冻结编码器，轻量分类器微调下游。

## 实验与结果
CMU-MOSEI 预训练：Acc-7 55.31%、Acc-2 84.10%、BF1 89.08%，优于 MGAFR（52.24%）等，参数 16.28M（少约 6.8M）。模态消融显示文本贡献最大。模块消融：仅监督 42.91% Acc-7，MoCo 51.68%，完整模型最佳。跨库：MOSI Acc-7 38.78%（全训基线 39.19%）；IEMOCAP 4/6 类 WF1 74.54%/55.70%，接近全监督 78.36%/58.64%。

## 结论
掩蔽+去噪重建与 MoCo、ALS 结合，可学到跨库可迁移的多模态情感表征，并降低参数量。

## 点评
用重建显式应对缺失/噪声，比纯对比更贴情感数据现实；文本主导结果也提示“无监督”仍高度依赖转录语义。跨库成功部分因 MOSEI–MOSI 同 YouTube 分布，IEMOCAP 差距虽小但设定仍靠相同前端特征。


# Unified Audio-Visual Modeling to Recognize Which Face Spoke When and What in Scenarios with On- and Off-Screen Participants

- 论文编号：1592
- 报告人：Naoki Makishima
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/makishima26b_interspeech.pdf

## 问题
多说话人音视频说话人归属识别（AVSASR）需同时回答谁在何时说了什么；既有序列化方法假设说话人始终可见，而真实场景常有遮挡或画外说话人，强制关联会致错。

## 方法
在 [12] 的 Transformer 编解码序列化建模上扩展：目标序列含起止时间 token、文本与视频 token；新增 `[None]` 表示画外/不可见说话人，避免强制绑到某一脸轨。语音与多路嘴部视频分别编码，拼接后加片段嵌入再解码。在 LRS3 上仿真 2–3 人重叠混合，训练覆盖各类 on/off-screen 组合（I=3）。

## 实验与结果
指标 WER、VWER（谁说了什么）、VTER（谁在何时说）。全可见时 Proposed 与专用 AVSASR 接近（如 2 人 WER/VWER/VTER：25.4/27.9/3.6 vs 25.8/28.8/3.2）。含画外时 Proposed 明显更好：2 人 VWER/VTER 30.4/3.5，优于 AVSR+唇动检测（34.8/6.4），而旧 AVSASR 因错绑严重退化（括号内参考值更差）。画外+多人时 WER–VWER 差距拉大，音视频同步仍难。

## 结论
`[None]` token 使统一模型在含画外说话人时优于强制可见假设与分离流水线，全可见时几乎不损失。

## 点评
改动小但对准真实会议/隐私场景的关键假设漏洞。证据基于仿真混合与 5 fps 嘴部裁剪；作者也承认画外时靠音视频同步仍难，VWER 差距增大是主要边界。


# Speech Recognition on TV Series with Video-Guided Post-ASR Correction

- 论文编号：2970
- 报告人：John Hansen
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yang26o_interspeech.pdf

## 问题
TV 剧 ASR 面临多说话人、重叠、专有名词与长程上下文；唇读类 AV-ASR 依赖高分辨率对齐人脸，剧集中常不可用。现有后修较少显式利用视频语义上下文。

## 方法
提出免训练 VPC：先 ASR 得转写；再用 VideoLLaMA2 以 QA 抽取剧名识别与细粒度场景描述；最后用 GPT-4o 据视频上下文仅修正明显识别错误。评估于 Violin 英语 TV 子集（约 90 h，训/验/测 72/9/9 h）。

## 实验与结果
对 Librispeech 预训练再微调的 wav2vec2/HuBERT/WavLM/Conformer：VPC 相对原始 ASR 相对降 WER 约 13.06%/11.86%/20.75%/7.46%（WavLM 29.83→23.64）。无视觉的 GPT-4o  alone 几乎无效甚至变差。初步 AV-HuBERT 达 78.3% WER（人脸条件差）故未作主对比。100 片段消融显示 All-QA（粗+细）优于单一 QA。

## 结论
高层视频语义 + LLM 后修可在复杂多媒体下稳定降 WER，且不必改 ASR 骨干。

## 点评
相对唇读路线，改走语义上下文更贴剧集现实。依赖闭源 GPT-4o/VideoLLaMA2，修正边界靠提示“只改明显错误”，可能引入幻觉；相对提升在弱 ASR（WavLM）上更大，强 Conformer 增益较小。


# Closing the Speech-Text Gap with Limited Audio for Effective Domain Adaptation in LLM-Based ASR

- 论文编号：3383
- 报告人：Sergio Burdisso
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/banerasroux26_interspeech.pdf

## 问题
LLM-based ASR（编码器+投影器+LLM）可用纯文本域适应，但会使 LLM 远离投影器产生的“噪声”表示，形成 modality gap；目标域语音又昂贵稀缺。

## 方法
SLAM-ASR：冻结 WavLM-Large 与投影器，仅用 LoRA 适应 Llama-3.2-3B。Mixed Batching（MB）：batch 混合源域配对语音、投影最近邻噪声 token、字符扰动文本，以及目标域配对语音与扰动文本。比较纯文本、全配对与不同比例目标语音的 MB。源域 DefinedAI B/I/H；目标含 Banking 与 SlideSpeech Agriculture/Musical Instruments。

## 实验与结果
Banking 上纯文本 WER 6.38% vs 全配对 4.55%（模态差距明显）。MB 用约 10% 目标语音（Banking≈3h37）即可达到或超过全语音微调；约 60% 语音时峰值最好。Agriculture/MI 等 OOD 域趋势一致。相对标准 ASR 微调，文本/MB 对源域遗忘更轻。

## 结论
少量目标语音混入以文本为主的 MB，可弥合 modality gap，在极少音频下逼近或优于全语音适应。

## 点评
实用结论清楚：文本负责域语言、少量音频负责对齐。batch 成分与 τ=50% 等设定较细；全语音充足时 MB 优势收窄，说明方法主打低资源。


# Improving Streaming Speaker Diarization for LLM Based Multi-talker Speech Understanding

- 论文编号：1403
- 报告人：Ruizhi Li
- 程序：Thursday 1 October 2026 / Multimodal Speech Processing and Speech LLM Systems
- 技术分类键：audio-llm
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26f_interspeech.pdf

## 问题
智能眼镜多通道场景中，LLM 多为单通道输入；外部分离+简单 RMS 阈值说话人标注在噪声下不稳，且阵列几何因设备而异，难以一模型通吃。

## 方法
两阶段流式框架：NL-CMV 波束形成得几何无关方向表示；源分离输出 reference/self/other，多任务加分类头；第二阶段用 F0+RMS 上的 GBDT（或 SVM）标 Self/Other/Non-speech，再选提示驱动冻结 Gemma-3n 做归属 ASR/翻译。用 Conformer 替换 GRU，参数约 20M→5.5M；多设备共享下游、设备专用波束系数。

## 实验与结果
分离用仿真 Aria 类 5 麦数据训练；分类器用 1000 条真实多通道会话。IT/FR/ES–EN 真实评估：2-Stage MT 在多数指标最优（如 ES-EN Self/Other WER 7.77/9.05，SAER 0.21/0.45）；2-Stage Conf. 接近且更轻。翻译 Other BLEU（IT-EN）升至 57.04。多设备模型对 Device-A 降 WER，对 Device-B 接近专用模型。GBDT 各类 F1 更均衡（Self 91.4、Other 85.9、Non-speech 79.6）。

## 结论
分离+轻量统计分类优于单阶段与阈值式标注；Conformer 与多几何波束形成支持更高效、跨设备的流式归属理解。

## 点评
把空间处理从 LLM 解耦，适合眼镜部署；第二阶段依赖人工时间戳与 F0/RMS，极端噪声或多人旁听者可能仍难。仿真训分离、真实评下游的域差需留意。

