# Speech Emotion Recognition and Representation 3

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：3
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场情感识别与表征从封闭标签走向开放词汇推理、模糊情感分布、边缘–云协作描述，以及说话人不变与跨语泛化。大音频语言模型带来更丰富输出，但细粒度声学时序、模糊性推理与部署隐私仍是短板。

方法上出现 utterance 感知声学 Q-Former、不确定度引导的投机解码、模糊感知目标与思维链、层向任务向量合并融合 ASR 知识、轻量多尺度 SE 块，以及熵对抗去说话人、条件 Transformer U-Net 音视频稳健识别、扩散桥矫正过/欠拟合表征。跨语属性（唤醒/效价/支配）适应所需数据量因任务而异，提示“低资源”阈值依赖目标属性。

## 论文技术总结

# AcoustEmo: An Utterance-Aware Acoustic Q-Former for Open-Vocabulary Emotion Reasoning

- 论文编号：2364
- 报告人：Liyun Zhang
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26ea_interspeech.pdf

## 问题
面向开放词汇情感推理的 MLLM 常把整段音频压成全局 token，难以捕捉单句内部的微韵律、突变语调等局部时序线索，限制了 EMER 等需细粒度声学证据的任务。

## 方法
提出 AcoustEmo：视觉仍用 ViT + Global Visual Q-Former；声学用时间戳同步滑动窗按转写句边界切分帧级特征（如 ImageBind），每句经 Utterance-Aware Acoustic Q-Former（K=32 可学习 query 交叉注意）得到局部 token，并与全局 Acoustic Q-Former token 拼接；再与指令（含时间戳）一起送入 LLaMA-2（7B）+ LoRA 做因果语言建模。

## 实验与结果
在 EMER-Fine 测试集上，AcoustEmo Avg/Acc/Recall 为 67.55/65.40/70.15，超过 MicroEmo（66.21）与 AffectGPT（61.75）等。消融：去掉 Utterance-Aware A-QF 降至 61.20；固定 2s 窗降至 62.85；去掉全局声学 Q-Former 降至 64.10。定性例子中能抓住句末短暂声颤并预测 anxious/concerned，而全局基线判为 calm/neutral。

## 结论
句级对齐的局部声学建模可增强开放词汇情感推理；全局上下文仍有补充价值。未来拟做连续效价–唤醒追踪并降低动态切分开销以支持端侧实时应用。

## 点评
把 MicroEmo 一类“局部视觉动态”思路迁到声学，并用转写时间戳做软对齐，问题定位准确。相对全局池化的增益与消融一致，说明边界对齐比单纯加窗更重要。讽刺（声学与语义冲突）与低 SNR 叠音仍会出错，提示局部 token 质量仍受前端分离与噪声制约。


# Edge–Cloud Collaborative Speech Emotion Captioning via Token-Level Speculative Decoding in Audio-Language Models

- 论文编号：901
- 报告人：Ting Dang
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xue26b_interspeech.pdf

## 问题
Speech Emotion Captioning (SEC) 依赖大音频–语言模型，边缘设备算力不足、全量上云又有时延与生物特征隐私风险；小模型又难以刻画细粒度副语言与情感 grounding。静态边云切分忽略 token 难度差异。

## 方法
Uncertainty-Guided Speculative Decoding (UGSD)：边缘用 Qwen2.5-Omni-3B 起草 caption，以 token 熵作不确定性；若长度 L 块内最大熵超过阈值 γ，则只把该块（连同已接受前缀与设备端声学特征）送给云端 Qwen3-Omni-30B 校验；rank≤R 接受，否则用云端 argmax 纠正并丢弃后缀。L 在 {3,5,7} 间自适应。原始波形永不离开设备。

## 实验与结果
MER2024 英/中各 332 条。相对 edge-only：英文 BLEU 等相对提升约 21.6%–76.4%；中文 BLEU-1 +21.0%、ROUGE-L +38.5%、METEOR +111.7%。动态 L：总时延 40.21s→28.67s（1.4×）、OTPS 1.53→13.05（8.5×）；仅 18.2% token 上云。云端换成 7B 时增益变小但仍为正。

## 结论
作者认为 UGSD 在质量–效率–隐私间取得实用折中，适合 edge-first SEC；紧凑特征仍可能泄漏部分说话人/内容信息。

## 点评
把 speculative decoding 从单机加速改造成“难 token 才上云”，切中 SEC 部署痛点。评价在仿真边云环境，真实网络抖动未充分建模；熵阈值与 R 仍需验证集调参。


# Disentangling Reasoning in Large Audio-Language Models for Ambiguous Emotion Prediction

- 论文编号：2031
- 报告人：Jiaheng Dong
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/yu26f_interspeech.pdf

## 问题
SER 常压成单一标签，忽略情感模糊性；LALM 虽能生成更丰富输出，但对模糊情感的分布式推理仍弱，且常见 CoT/RL 后训练面向“唯一正确答案”任务，易坍缩到确定性解释。

## 方法
把模糊情感识别重写为分布推理：用多标注者投票得到软标签 p^GT，并用 GPT-4o 按 Keywords→文本分析→音频分析→综合 协议生成 ambiguity-aware CoT。在 Qwen2-Audio-7B-Instruct 上以 LoRA 接入：KL 对齐预测情感分布与软标签；SFT/DPO/GRPO（及注入金标轨迹的 GRPOz）均可插拔该目标。分布从情感词 token logit 的 softmax 读出。

## 实验与结果
IEMOCAP（5-fold LOSO）与 CREMA-D。指标 JS↓、BC↑、R²↑、Brier↓。IEMOCAP 上 GRPOz 最佳（JS 0.20、BC 0.82）；CREMA-D 上 DPO 最佳（JS 0.17、BC 0.86）。相对 Base/Audio-Reasoner 一致提升。消融：KL 优于仅 CE；跨域时 CoT 对泛化帮助更大。

## 结论
作者认为分布对齐与结构化 CoT 可拆开决策层不确定性与推理增强，并在多种后训练策略上有效；未来可扩展更广任务与模型。

## 点评
把“模糊情感”正式做成软标签+推理轨迹，比单标签 SER 更贴人感知。CoT 依赖闭源模型合成，轨迹质量与成本是隐患；不同数据集上 DPO/GRPOz 谁更强与类别维度有关，说明后训练选择不能一刀切。


# AdaLTM: Adaptive Layer-wise Task Vector Merging for Categorical Speech Emotion Recognition with ASR Knowledge Integration

- 论文编号：80
- 报告人：Chia-Yu Lee
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26_interspeech.pdf

## 问题
把 ASR 知识并入 SER 时，特征级融合受转写错误影响，多任务学习又因目标冲突（ASR 要抑情感、SER 要情感变异）产生梯度干扰；域外 ASR 任务向量还会丢掉副语言线索。

## 方法
AdaLTM：在 WavLM-Large 上分别于 MSP-Podcast 微调得到域内 ASR/SER 模型，提取任务向量 ΔW=W_ft−W_base；冻结骨干与向量，仅学习每层系数 λ_ASR^{(l)}, λ_SER^{(l)}（25 层含前端）做加权合并，再对 24 层隐状态做可学习加权求和送分类头。对比 LibriSpeech 域外 ASR 向量与全局/静态合并。

## 实验与结果
MSP-Podcast v1.12 八类情感。MTL 基线 UAR 约 29%，而 Dual-Vector AdaLTM 达 UAR 38.94%、MaF1 35.20%；SER-Only 略高（39.09%）但 Dual 显著优于冻结基线（37.05%）。域内优于域外（38.94% vs 38.68%）；层自适应优于静态全局 λ=0.5（38.30%）。可训练参数约 0.46M。

## 结论
作者认为权重空间层自适应合并可规避 MTL 梯度冲突，并强调域一致 ASR 知识；局限是需要域内转写以提取 ASR 向量，且前期仍要分别微调专家模型。

## 点评
用 task vector 绕开“ASR↔SER 梯度打架”很干净，层系数可视化也解释了语言锚定与韵律主导。Dual 略低于 SER-Only 符合容量挤兑直觉；没有可靠转写的低资源情感数据会卡住整条管线。


# SETEAB: Multiscale approach with Squeeze-and-Excitation Temporal Enhanced Aware Block for Speech Emotion Recognition

- 论文编号：1208
- 报告人：Kiet Anh Hoang
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/vo26_interspeech.pdf

## 问题
轻量 SER（如 TIM-Net 的 TAB）存在归一化不足、特征冗余与前后向等权相加等问题；大 SSL 模型精度高但 FLOPs 大，难上边缘设备，跨语料泛化也仍弱。

## 方法
SETEAB：Mel 频谱经 depthwise 卷积下采样（R=2/4）→ SE-Res2Block 做多尺度通道重标定 → 双向 TEAB 栈（LN、点扩、depthwise 时序、门控残差，膨胀 2^{i−1}，n=8）→ 全局可学方向权重 a/b 的加权双向融合 + 层级 λ_i 聚合。训练用 EmoBox 协议、Adam、label smoothing 与 SpecAugment 等增强。

## 实验与结果
语内：SETEAB(R=2) 平均 UA 47.69%，R=4 平均 F1 45.23%，均优于 TIM-Net/MS-SENet；参数约 0.4–0.5M、0.06–0.12 GFLOPs，远低于 wav2vec 2.0 base（95M/33.53G）。跨语料：12 组中 7 组最优，平均 WA 37.53%（高于 MS-SENet 34.31% 等）。消融显示 BiF、SE-Res2、DW-Sub、TEAB 均有贡献。

## 结论
作者认为 SETEAB 在精度、算力与跨语料稳健性间取得平衡，适合实用 SER。

## 点评
在 TIM-Net 族上做系统小改（门控残差+可学双向权重+深度可分下采样），工程收益清晰。跨语料方差偏大（±8.20），说明仍对某些训测对敏感；相对大 SSL 绝对精度未必全面领先，但效率优势突出。


# How Language-Independent Are Emotional Attributes? A Study on Training Data Scaling and Cross-Lingual Generalization

- 论文编号：2143
- 报告人：Dániel Halmai
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/halmai26_interspeech.pdf

## 问题
高资源语言（如英语）有大量维度情感标注，低资源语言不清楚需要多少目标语数据才能让跨语适应超过从零训练，以及 arousal/valence/dominance 的语言独立性是否不同。

## 方法
WavLM Large 骨干，在 MSP-Podcast（英语约 104h）与 BIIC-Podcast（台湾华语约 102h）上做回归预测三维度（MSE）。对比 Direct（仅华语 1/2/5/10/20/100h）与 Transfer（先英语再华语子集微调）；冻结卷积、Adam、5 随机种子，报告 Pearson 与 CCC，Mann-Whitney U 检验显著性。

## 实验与结果
测试集：Transfer 在 1–2h 对三维度均显著优于同量 Direct；arousal 上 Transfer-10h Pearson 0.624 可显著超过 Direct-100h 的 0.606；valence 约需 20h 适应才追上 Direct-100h；dominance 上多组 Transfer 即可持平或更好。纯跨语（0h）与同语 100h 差距约 0.05–0.1。

## 结论
作者认为 arousal 相对更跨语可迁移，valence 更依赖目标语数据；任务特异适应是低资源维度 SER 的有效路径。

## 点评
用配对语料与数据缩放曲线直接回答“低资源阈值”，问题清晰、结论可操作。仅英→华单向、dominance 绝对值偏低可能含标注噪声；未做类别情感，结论限于维度属性。


# SISER: Speaker-Invariant Speech Emotion Recognition with Entropy-Based Adversarial Training

- 论文编号：2186
- 报告人：Eunseo Choi
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/choi26e_interspeech.pdf

## 问题
SER 受说话人变异与标注稀缺双重制约；对抗式去说话人常配浅层判别器，对抗压力不足，且 GRL 不约束失败后的目标分布形状。

## 方法
SISER：wav2vec 2.0（微调时仅解冻最后两层 Transformer）作编码器，ECAPA-TDNN 作说话人分类器，情感头为多层 FC。交替训练：先更新 SC 的说话人 CE；再固定 SC，用情感 CE + 最大化说话人后验熵联合更新 ENC/EC（λ=0.5）。无增强以隔离模块贡献。

## 实验与结果
IEMOCAP 四类（happy 含 excitement），10-fold leave-one-session。测试 UA/WA：基线（CNN+GRU+熵，无增强）51.15/50.14；wav2vec vanilla 56.46/54.45；GRL+ECAPA 56.95/56.01；SISER 60.63/58.53，接近原方法有增强版本（59.91 UA）。消融：换 ECAPA 相对浅层 FC 提升约 6–7 UA；t-SNE 显示情感簇更分离。

## 结论
作者认为强说话人判别器+熵最大化是说话人不变表示的关键；简单分类头已够用，更复杂头可再涨点。

## 点评
把“判别器容量”当作一等公民，消融说服力强。无增强设定公平但绝对分可能偏低；熵最大化在说话人极少的折上是否过度抹平情感仍需警惕。


# Robust Audio-Visual Emotion Recognition via Conditional Transformer U-Nets with Frequency-Injected Visual Stream

- 论文编号：2770
- 报告人：Hanwook Chung
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chung26b_interspeech.pdf

## 问题
噪声与混响严重损害 SER，进而拖累音视频情感识别（AVER）；现有多模态工作较少显式建模恶劣声学，视觉侧也少用频域线索刻画微表情动态。

## 方法
双路 CTr U-Net：音频流对 log-Mel 做 inverse-filtering CTF 前端增强，再进情感编码器+情感条件辅助特征解码器；视觉流用 EfficientFace 特征，在 CTr 的 Q/K/V 上注入空间维 FFT 对数幅度（frequency-injected）；瓶颈特征经融合解码器（含 prompt generation module）分类。两阶段训练：先 MAE 训前端，再联合交叉熵与重建正则。

## 实验与结果
CREMA-D / RAVDESS / IEMOCAP，噪声与 RIR 分 seen/unseen。干净 AVER：CREMA-D UAR/WAR 89.14/89.11，RAVDESS 91.69/90.97。鲁棒 AVER（cCTrU-FE）相对干净训练基线大幅稳住（如 CREMA-D 平均 UAR 86.14 vs 74.41）。鲁棒 SER 在 IEMOCAP+NOISEX 多 SNR 上优于多项基线（如 0 dB seen improvised UAR 75.76）。频注入与情感条件解码均有消融增益。

## 结论
作者认为 inverse-filtering 前端、频注入视觉与情感条件辅助解码共同提升恶劣声学下的 AVER 稳健性。

## 点评
把 dereverberation 直接嵌进 LMFB 域并与视觉频注入并联，工程完整。对比表跨论文设定不一，绝对排名需谨慎；RAVDESS 上个别先前工作 WAR 仍更高，显示数据集依赖。


# Diffusion Bridge Learning Between Overfitted and Underfitted Representations for speech emotion recognition

- 论文编号：2996
- 报告人：Shi-wook Lee
- 程序：Thursday 1 October 2026 / Speech Emotion Recognition and Representation 3
- 技术分类键：emotion
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lee26w_interspeech.pdf

## 问题
SSL 编码器在 SER 上易过拟合语料特异线索，跨语/跨域退化；训练早期表征更稳健但可分性弱，晚期更可分却过专，单检查点难以兼得。

## 方法
Diffusion Bridge Learning：从同一 HuBERT Large 骨干取晚期（过拟合）与早期（欠拟合）表征 A/B，定义类原型 μ；用条件去噪扩散在表征空间学习样本↔原型双向桥，配合配对对齐、循环一致、分类 CE 与 logit-pair KL 正则。推理可对 sample→prototype 翻译后分类。

## 实验与结果
英（IEMOCAP+MSP-IMPROV）↔日（JTES）交叉评估，指标 WAR。异质桥 overfit–underfit(B) 增益最大：英→日高权重 (λ_pair,λ_cycle)=(10,1) 时 +6.42 pp（45.32→51.74，p=0.0011）；日→英 +4.00 pp（35.74→39.74，p=0.0015）。同阶段桥增益较小；过拟合侧分类器较难被平滑改善。

## 结论
作者认为原型引导的扩散桥可重塑类中心几何、缓解过专方向，提升跨语稳健性；未来拟做直接跨域桥与更高效扩散日程。

## 点评
把“早/晚检查点互补”做成可训练的随机桥，视角新颖，跨语数字也扎实。依赖同一骨干不同阶段表征，部署需存双端点；增益主要落在欠拟合侧分类器，过拟合侧收益有限。

