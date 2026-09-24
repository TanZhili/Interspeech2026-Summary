# Multimodal Emotion Recognition

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：3
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从类别/维度情感识别扩展到比较推理、风格语言—音频预训练、纵向日志情感推断，以及视觉副语言与时间变化的模态门控。LALM 被训练做成对话语上的唤醒/效价/支配比较，并用语义描述与 GeMAPS 声学证据生成可解释推理轨迹。合成爱尔兰盖语嗓音实验则检验视听通道在情感感知中的相对作用。

表征侧 ParaSpeechCLAP 用双编码器覆盖更丰富的内禀与情境风格描述，并可用于风格提示 TTS 的推理时奖励。纵向语音日记显示群体层面语言学模型远强于声学，但个体日常监测仍需个性化。视觉微姿态通过运动引导空间去噪提升信噪比；情感识别中模态重要性被显式建模为随时间与类别变化的动态过程。

## 论文技术总结

# Comparative Reasoning: Making an Audio Language Model Better at Comparing Emotions

- 论文编号：2935
- 报告人：Abinay Reddy Naini
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/naini26_interspeech.pdf

## 问题
大音频语言模型（LALM）多做单音频推理，跨两段语音的比较判断（如谁 arousal/valence/dominance 更高）较弱，且现有序数 SER 偏好学习很少显式建模可解释的比较推理。

## 方法
提出 reasoning-guided ordinal SER：输入成对语音与属性定义提示，预测哪一段属性更高。用 Qwen3-Omni-Captioner 语义描述 + 18 维 GeMAPS LLD 的均值/标准差（归一化后离散为 low/medium/high）喂给 Qwen3-Next-80B，生成 <5 句的比较推理轨迹；错答则条件于正确标签重生成。骨干 Qwen2.5-Omni-3B + LoRA，对比标签-only 的 SFT/DPO 与带推理的 SFT-CoT/DPO-CoT（DPO 对正确/错误推理–答案对）。MSP-Podcast v2.0 上用约 5% 话语构造每属性 10k 训练对（共识分差 >1）。

## 实验与结果
MSP-Podcast 测试：零样本平均偏好准确率 0.637；SFT 0.875、DPO 0.879、DPO-CoT 0.881，均超过 WavLM/HuBERT+RankNet 与 RankList（后两者用 240k 对，平均约 0.76–0.80）。跨域 BIIC/WHiSER 上 LALM 变体总体优于 SSL 基线，DPO-CoT 在 BIIC 平均 0.770。仅训 arousal 时 DPO-CoT 跨情绪平均 0.785，对 valence 退化小于标签-only。推理轨迹可给出音高、响度、犹豫等可解释依据。

## 结论
适当适配的 LALM 能以远少于传统序数系统的数据做好情绪偏好比较；DPO 对照正确/错误推理可提升利用推理并抑制幻觉，增强可解释性与跨域/跨维迁移。

## 点评
把成对比较、声学可感知证据与偏好优化绑在一起，切中 LALM 的多音频短板，数据效率对比（10k vs 240k）很有说服力。SFT-CoT 有时略逊于纯标签 SFT，说明推理监督质量与长度约束关键；依赖外部大模型造轨迹，部署成本与轨迹忠实度仍是实际瓶颈。


# Exploring the effect of the visual channel in vocal expression of affect in an Irish (Gaelic) synthetic voice

- 论文编号：1363
- 报告人：Ailbhe Ní Chasaide
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/giovannini26_interspeech.pdf

## 问题
先前用声源改造合成爱尔兰语情感语音时，高/低激活态常重叠、单一音质不唯一对应情感；加入面部表情是否能增强目标情感并更好区分同激活水平情感，尚不清楚。

## 方法
对爱尔兰 TTS 中性句做 VSG/LF 声源改造（f0、Ee、Rd；sad/happy 另调时长与共振峰）得到 angry/happy/sad/bored/relaxed；Daz 3D 男头像按 FACS 做较细微表情并唇同步，另加 interested 对 bored。验证测选视觉强度后，31 名听者在 voice-only、congruent、incongruent 条件下做三组对立量表（Happy–Sad、Interested–Bored、Angry–Relaxed），用混合效应有序逻辑回归分析。

## 实验与结果
voice-only 与 congruent 目标识别率均很高；congruent 相对 voice-only 强度提升多不显著，angry 甚至出现反向。incongruent 常把感知拉向中性（如 happy 加 sad 脸，Happy–Sad 识别从约 94% 降至 58%），但几乎不翻转极性，显示本实验中语音通道主导。congruent 显著改善同类激活态区分（如 Happy–Sad 中 happy vs angry，p=.038；sad vs bored，p=.006）。

## 结论
匹配视觉未系统增强情感强度，但有助于细化高/低激活情感；冲突视觉会削弱强度。作者将此联系到 AAC 中情感声源与表情扩展。

## 点评
用同句声源改造 + 可控 3D 表情把通道主导与“细化 vs 增强”拆开，结论对合成多模态情感设计有直接含义。视觉刻意偏弱、听者爱尔兰水平不一，通道优势是否普适仍需强度系统操纵验证。


# ParaSpeechCLAP: A Dual-Encoder Speech-Text Model for Rich Stylistic Language-Audio Pretraining

- 论文编号：1437
- 报告人：Anuj Diwan
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/diwan26_interspeech.pdf

## 问题
现有 speech–caption 对齐（如 ParaCLAP）只覆盖窄情态标签；音高、音色、清晰度等 intrinsic 与更广 situational 风格以自然语言描述时，缺少统一嵌入与可用评测/奖励手段。

## 方法
基于 ParaSpeechCaps 训练 CLAP 式双编码器：WavLM-Large 均值池化语音端 + Granite Embedding 278M 文本端，投到 768-D。分别训 Intrinsic、Situational 与两者合并的 Combined；Intrinsic 额外用文本编码器生成的类别嵌入做多标签分类损失，并类均衡采样。下游：风格 caption 检索、属性分类，以及风格提示 TTS 的 best-of-N（N=10）推理时奖励选样。

## 实验与结果
相对 ParaCLAP / ParaCLAP-PSC / VoxProfile 等，多数指标更优。专用模型在对应子集更强（如 Situational R@1 24.79，Intrinsic R@1 18.62）；Combined 在组合评估最好（R@1 14.31）。TTS 引导：CMOS 3.61→3.70，Intrinsic/Situational tag recall 57.9%/69.2%→62.4%/74.3%，NMOS/WER 不降。消融显示新编码器、多任务分类与类均衡均必要。

## 结论
ParaSpeechCLAP 首次较广覆盖 intrinsic+situational 风格对齐，专用与统一策略互补；可用作免训练的 TTS 风格筛选奖励。局限是推理需选对变体，Combined 与专用仍有差距，best-of-N 成本随 N 线性增长。

## 点评
把“宽风格标签空间”落到可发布的双编码器，并把模型当 TTS 奖励用，应用面比纯检索宽。评测仍主要在 ParaSpeechCaps holdout，对外部情感基准覆盖有限；分类提示模板敏感度未深入分析。


# Daily Affect Inference from Longitudinal Speech-based Journals: A Comparison of Acoustic and Linguistic Models

- 论文编号：2383
- 报告人：Michelle D Schlicher
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/schlicher26_interspeech.pdf

## 问题
日常语音日记兼具声学与语义，能否在群体与个体层面推断当日 arousal/valence/stress；声学与语言学哪条更有效，尚缺可比纵向语料与系统对照。

## 方法
德国大学生 2 周晚间日记：“今日亮点与低点？”+ MDBF（V/A/C）与 PSS-4；仅分析口语组：61 人、769 段（约 90% 女性）。Whisper 转写后对比：微调 GBERT-large、零样本 Mistral-7B-Instruct；声学侧 eGeMAPS+节奏/停顿特征随机森林，以及微调 wav2vec2 情感回归。说话人独立 5 折 CCC/RMSE；并用说话人中心化 LME 看日间声学与情绪。

## 实验与结果
群体层：语言远强于声学。Mistral 对 valence CCC .466、stress .360；GBERT 对 arousal CCC .122 最优；eGeMAPS/w2v2 多数近零或负。说话人层：Mistral 更像抓特质而非日间状态，RMSE 随个体均值系统变化。LME 在 FDR 后仅 valence 上停顿数（负）与预训练情感模型预测 valence（正）显著；arousal/stress 无显著声学日间关联。

## 结论
自由叙说语义更适合追踪日回顾式情绪/压力；全局声学模型难监控个体日波动，需个性化。日记反映的是当日总结而非瞬时状态，亦限制预测。

## 点评
把“日记是回顾而非瞬时”说清楚，并同时报群体 CCC 与说话人内 LME，避免被表面上的 LLM 分数误导。样本小、性别极偏、自我报告偏差大；声学近零与经典 SER 文献冲突，外推临床需谨慎。


# Enhancing Visual Paralinguistics: Motion-Guided Spatial Denoising for Non-Verbal Interaction Analysis

- 论文编号：868
- 报告人：Junjie Wan
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wan26_interspeech.pdf

## 问题
自然 HCI 中微动作被静态背景“幽灵关键点”淹没；重骨干隐式学时空依赖成本高且易过拟合，固定权重晚期融合又忽略不同微动作对 RGB/姿态依赖不同。

## 方法
双流：ResNet-18 RGB + 姿态热图流。MG-SRM 用一/二阶时间差分作运动先验，对空间/时间分支做仿射调制与门控聚合（零初始化残差）。CLF 为每类学姿态流权重 p_c，融合 S_rgb+(1+tanh(p_c))·S_pose，避免实例级注意力过拟合。在 MA-52 上评测。

## 实验与结果
MG-SRM+CLF：Top-1 67.02%、F1-Mean 0.6993，超复现 PCAN（66.40%）与 MMN（62.71%）。消融：基线 65.88%；+CLF 66.42%；+MG-SRM 66.43%；两者 67.02%。实例级注意力 66.72% 低于 CLF。倒放掉 1.34%；相对 Transformer 编码器变体高 0.98%。增参约 0.072M、+1.8G FLOPs。GradCAM 显示注意力更贴手–头动态。

## 结论
显式运动引导空间去噪加类别自适应融合，以极低开销提升嘈杂场景微动作识别，可作为多模态对话系统的视觉前端。

## 点评
把语音增强里的“减噪/高通”类比迁到姿态热图，对 ghost keypoint 问题切得准；CLF 用类别偏置换稳定也很务实。仅 MA-52 单一基准，与语音通道的联合情感/意图实验未做。


# Modality Importance is Not Static: Temporal Dynamics via Gating in Multimodal Emotion Recognition

- 论文编号：1399
- 报告人：Jiyeon Ryu
- 程序：Wednesday 30 September 2026 / Multimodal Emotion Recognition
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ryu26_interspeech.pdf

## 问题
对话情绪跨话轮展开，但多数 MER 做静态句级融合，隐含模态重要性时间不变；是否真存在随时间、随类别变化的模态权重，缺少可控证据。

## 方法
解耦单模态编码与融合：冻结 GPT-2 / HuBERT / VideoMAE（视频可解冻末两块），导出 768-D 特征。对比静态 MLP、无门控 GRU、local/contextual/emotion-query 门控。emotion-query 用可学习类查询与前一时刻状态产生类条件模态分布，再边缘化为时间步权重（上下文 K=8）。IEMOCAP 6 类 LOSO；用时间与时间×模态遮挡及 AOPC 做忠实归因。

## 实验与结果
静态 logits MLP Macro-F1/UA≈0.48；无门控 GRU≈0.557；emotion-query 0.5731/0.5734，优于同协议 Transformer/MulT/MMER，且参数约 0.076M。相对静态 mean(F1,UA) 约 +9.01，相对无门控 +1.63。hap/fru/sur 提升更明显。门控轨迹显示文本平均权重最高但各模态 std>0；AOPC 随 top-k 遮挡单调上升。

## 结论
模态重要性非平稳；时间建模是主增益，类条件动态门控再补一小步。MER 宜视为动态决策而非静态融合。未来需更自然对话语料验证。

## 点评
目标明确是证伪“静态模态重要性”，用协议对齐消融 + 扰动归因，比堆 SOTA 更有分析价值。IEMOCAP 部分剧本、干净转写抬高文本权重；未宣称跨数据集 SOTA。

