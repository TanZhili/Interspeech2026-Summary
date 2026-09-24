# Speech Technologies for Language Learning & Assessment

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：10
- 论文数：12

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场面向语言学习与口语评测：口音会话 ASR 强调实体与填充停顿召回而非仅 WER；口语语法纠错把犹豫视为不确定信号而非噪声。水平评估从英语中级扩展到低资源巴斯克语 C1 判别，并比较多语言 SSL。

评分与反馈侧出现多代理多模态 SpeechLM 直接分析音频对齐 IELTS 构念、带自然语言理由的多粒度 SpeechLLM，以及用序数原型对齐替代大规模 MLLM 微调。发音检测诊断则从音系特征分解、语言特定混淆图、离散 token surprisal 到教师引导少样本无切分偏差建模，并转向以可懂度为中心的音段错误排序。

## 论文技术总结

# Beyond WER: Entity and Disfluency Recall in Accented Conversational ASR

- 论文编号：786
- 报告人：Fiza Husain
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/husain26_interspeech.pdf

## 问题
面向印尼、印度、拉美口音会话英语的语言学习场景，商业 ASR 虽 WER 尚可（约 13–21%），但命名实体召回仅约 53–55%、填充停顿召回接近 0（<5%），无法同时支持“逐字流利度反馈”与“实体正确、结构平滑的理解型反馈”。

## 方法
三阶段流水线：(1) 对现有转写做启发式 SQL 过滤（连续大写、缩写、敬称、句中大写等），得到实体密度约随机采样 2.8 倍的数据，每区域 10k；(2) 用 Gemini 2.5 Pro 生成参考转写（每区 250 条人工核验）；(3) 对 Qwen2.5-Omni-3B 按区域训 rank-32 LoRA，单次前向输出 verbatim（保留 um/uh 等）与 corrected 转写。另用六类错误 taxonomy + Claude Sonnet 4.5 法官（与人工 83.8% 一致）做诊断。指标在 verbatim 上算。

## 实验与结果
每区约 2k 持出测试。Qwen-ft-eh：实体召回 80–85%、filler 76–86%、WER 6–10%；相对 Parakeet 实体召回升 26–29pp，WER 相对降 53–60%。优于 Whisper 与 AssemblyAI Universal-3-Pro 的实体召回，并匹配零样本 Qwen3-Omni-30B（参数约 1/10）。EH vs RS 配对 bootstrap：印度/印尼/拉美实体召回分别 +4.19/+2.84/+2.76 pp（p<0.0001）。vLLM 服务 P95 约 800ms。

## 结论
对口音会话 ASR，训什么数据至少同如何训一样关键；轻量实体富集 + 区域 LoRA 可在不引入后处理 LLM 的情况下显著提升实体与停顿召回。局限包括银标参考、filler 仍略低于 30B、尚未覆盖语码转换等多语场景。

## 点评
把语言学习真正关心的实体与填充停顿从 WER 中拆出来评估，数据策展的因果贡献用 bootstrap 钉住，工程上很落地。参考依赖 Gemini、训练数据不可公开，复现与外推需谨慎；双输出格式把“流利度”和“可理解性”绑在同一前向里，是场景契合点。


# Exploring Hesitation as a Signal for Spoken Grammatical Error Correction

- 论文编号：1869
- 报告人：Seunghoon Han
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/han26c_interspeech.pdf

## 问题
口语语法纠错（SGEC）常规流水线把不流畅当作噪声先删再做文本 GEC，可能丢掉 L2 学习者因语法不确定而产生的犹豫线索。作者假设犹豫与语法错误共现，应被当作正信号而非噪声。

## 方法
在人工带犹豫标注的转写上：(1) 注入特殊标记——静音停顿 `[SP]`、填充停顿区 `[FP]`/`[/FP]`、重复区 `[REP]`/`[/REP]`；(2) 为每个 token 加犹豫类型嵌入（正常/SP/FP 区内/REP 区内）与 token 嵌入相加。基座 T5-base，输入格式 `gec: <marked transcript>`，在 S&I Corpus 2025 训练域上微调。对比：规则去不流畅（DD）、人工流畅转写（Fluent oracle）。用人工转写而非 ASR，以隔离犹豫信号与识别错误。

## 实验与结果
ERRANT span-based F0.5：Proposed 0.4790，优于 DD 0.4585（+2.05%p）与 Fluent 0.4606（+1.84%p）。犹豫附近（±1 token）误差上相对 Fluent +2.78%p（0.5087 vs 0.4809），远区仅 +1.15%p。按类型：FP 增益最大（相对 Fluent +9.10%p），SP 中等，REP 基线已高、增益小。按 ERRANT：对 U:NOUN 等多余类错误提升明显（如 +11.5%p）。

## 结论
保留并显式编码犹豫信息，比规则去流畅甚至人工流畅转写更能帮助口语 GEC，且增益集中在犹豫附近，支持“犹豫携带纠错线索”。落地需能输出犹豫标注的 ASR；本文用人工转写隔离效应，未在端到端 ASR 噪声下验证。

## 点评
挑战“先清不流畅再纠错”的默认流水线，实验设计干净：超越 Fluent oracle 这一点很有说服力。代价是控制设定与挑战赛 cascade 不可直接比绝对分；FP 上 Fluent 反而更差，也提示人工“清理”可能一并抹掉纠错线索。


# Discriminating Proficiency Levels in L2 Speech: A Comparative Study of Self-Supervised Models in Basque

- 论文编号：1948
- 报告人：Christoforos Souganidis
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/souganidis26_interspeech.pdf

## 问题
自动化口语评估（ASA）多集中在英语等资源丰富语言与中低水平；对低资源语言（如巴斯克语）高阶 C1 级细粒度区分更难，且缺乏大标注语料。需检验多语自监督语音表示能否做纯语音的能力等级二分类。

## 方法
在 C1-HABE（巴斯克官方 C1 口试独白，Pass/Fail，切 20 秒段）与公开 ICNALE（英语 B1 vs B2+ 独白，作可复现对照）上，微调 wav2vec 2.0 与 mHuBERT-147：CNN 冻结，mean-pool + 线性二分类头，交叉熵。多学习率选 EER，再五随机种子；段级预测聚合，并用 model soup / seed majority vote (SMV) / probability averaging majority vote (PMV) 融合。用混合效应逻辑回归比较架构与策略。

## 实验与结果
C1-HABE：mHuBERT-147 显著优于 wav2vec 2.0 xlsr（准确率预测更好，β=0.30，p=.036）；最佳约 ACC 0.795 / F1 0.715（SMV）。ICNALE：wav2vec 2.0 base 显著优于 mHuBERT（SMV 下 ACC 0.965 / F1 0.842）；策略上 SMV > MS > PMV。作者讨论差异可能来自 L1（声调语 vs 巴斯克/西语）、预训练语种覆盖、等级边界与语料构成等。

## 结论
mHuBERT-147 更适合巴斯克 C1 通过/未通过判别；英语 B2 对照上则是 wav2vec 2.0 base 更强。多语 SSL 可支持低资源高阶口语评估，但最优骨干依赖语言与任务设定。

## 点评
把“高阶邻近等级”与低资源语种组合起来，比常见 A2–B1 分类更贴近证书考试需求。巴斯克数据不可公开、两语料难度与标签定义不完全对齐，跨语结论需谨慎；ICNALE 上 SMV 极高准确率也可能受类不平衡与测试规模影响。


# A Multi-Agent Framework to Automate Feedback Generation for IELTS Speaking Test using Multimodal SpeechLMs

- 论文编号：1417
- 报告人：Hui Xin Koh
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koh26_interspeech.pdf

## 问题
IELTS 口语需在流利连贯、词汇、语法、发音四维上评分并给反馈。手工特征回归覆盖不足、分数向中心靠拢；ASR→LLM 流水线丢掉韵律与时间线索，且识别错误不可逆传播。通用 SpeechLM 又常校准不足、对低质量语音过打分。

## 方法
多代理 + 多模态 SpeechLM（Qwen-Omni）：直接听音频，四个角色代理分别对应官方四项准则，输出分项分数与反馈；元审阅代理对照原音频做跨准则一致性检查，按 IELTS 半档取整汇总总分并合成报告。支持 3B/7B/30B-A3B、单代理 vs 多代理、零样本 vs 九例 few-shot。按 Part1–3 分段评估再与全场平均。对比：手工特征多元线性回归；Whisper 转写 + GPT-5-nano 反馈。

## 实验与结果
新建约 22.63 小时、270 场模拟考，分数 4.0–9.0，考官给分与反馈。评分相关（平均）：Multi+Few-shot r/ρ/τ = 0.480/0.521/0.396，优于单代理与回归（r=0.117）；3B 多代理已显著强于回归。反馈语义相似（SBERT）：多代理约 0.82–0.83，ASR+LLM 仅 0.412。30B MoE 评分相关不如更小稠密模型，作者归因于稀疏激活有效容量约 3B。

## 结论
准则对齐的多代理 + 端到端听音，可提升与人工分数相关性和反馈语义相似度，并绕过 ASR 信息瓶颈；架构分解往往比单纯放大参数更有效。

## 点评
把 IELTS 四维 rubric 显式拆成独立代理，再由元审阅抑制晕轮与重复惩罚，设计与构念效度对齐。语料规模中等且非公开标准集；30B 变弱提示“更大≠更好”，部署时应优先验证多代理结构而非盲目换大模型。


# A Finetuned SpeechLLM for Joint Multi-Granular L2 Assessment and Natural-Language Rationales

- 论文编号：2335
- 报告人：Aditya Kamlesh Parikh
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/parikh26_interspeech.pdf

## 问题
自动 L2 口语评估常给不透明分数或细粒度标签，缺少与标签一致、可教的自然语言理由。现有系统很少在单次端到端中同时做多方面、多粒度评分并生成忠实理由；数据严重偏高分，偏好对齐对“近邻错误”又可能过激。

## 方法
以 Qwen2-Audio-7B-Instruct 为骨干（4-bit 冻结 + LoRA r=64），用 rubric 提示一次输出句级 Accuracy/Fluency/Prosody、词/音素级 Accuracy，以及 Rationale。训练用 SFT + Bounded DPO（BDPO）：对真值标签构造被拒标签（句级扰动一个方面、序列级扰动全部；约 88% 下调以抑制 “niceness bias”），BDPO 限制对被拒样本的过度打压。在 SpeechOcean762 上把 0–10 / 0–2 分数离散为五档序数标签。

## 实验与结果
多粒度模型句级 PCC：Accuracy 0.66、Fluency 0.73、Prosody 0.71；词/音素 Accuracy 0.52/0.42。相对单粒度，句级 Accuracy 更好，序列级有权衡。相对 GOPT/Azure PA/SimPO：句级竞争力强，词/音素 PCC 优于 SimPO，但音素仍落后 GOPT。理由：句级情感与内部预测高度自洽，对真实低分偏“柔化”；词/音素提及稀疏，与标签 PCC 仅 0.50/0.20（内部）与 0.35/0.07（外部）。

## 结论
SFT+BDPO 的 SpeechLLM 可联合多粒度评分并产出基本可信的句级理由；细粒度忠实度仍不足。BDPO 有助于在偏斜评分下保持 rubric 与标签–理由一致性。

## 点评
把“可解释评估”拆成 plausibility 与 faithfulness，比只报相关更诚实。联合多粒度有助于句级 grounding，但音素诊断仍明显弱于 GOP 类路线；理由里出现拼写启发式，说明文本先验仍可能压过声学证据。


# LOPA: Enhancing Spoken Language Assessment via Latent Ordinal Prototype Alignment

- 论文编号：1346
- 报告人：Hong-Yun Lin
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/lin26e_interspeech.pdf

## 问题
MLLM 做口语评估（SLA）成本高，且常把能力当普通回归/生成，忽略语言习得的序结构。轻量 Whisper 方案又多只用最后一层或转写特征，丢掉中间层声学/音系线索，潜空间相邻 CEFR 级重叠严重。

## 方法
冻结 Whisper Large-v3 编码器全部 32 层。Semantic-Anchored Layer Routing（SALR）对层做偏置初始化（末层锚点）的可学习加权融合；注意力时间池化后经 MLP 得到潜向量，再对有序分数期望回归。Latent Ordinal Prototype Alignment（LOPA）用可学习 CEFR 原型：吸引损失拉近同类，序约束使原型间距与分数差成比例。按 S&I 2025 的 P1/P3/P4/P5 分部分别训练。

## 实验与结果
S&I Eval：RMSE 0.361、PCC 0.828，\(\%\le0.5\) 83.3，与 Phi-4-MTL-APP（0.360/0.827）接近，优于 Whisper last-layer APP（0.383）与多种轻量基线。消融：去 LOPA→0.383、去 SALR→0.3739；配对 t 检验显示 LOPA 显著降误差。潜空间 ordinality 0.878→0.974，Silhouette −0.110→0.032。SALR 辅层偏好随部分变化（P1 偏浅层、P5 偏高层）。

## 结论
在不微调骨干、不用 LLM 的前提下，多深度路由 + 序原型正则即可达到接近大 MLLM 的 SLA 精度，并提供可解释的层偏好。

## 点评
用几何先验把“能力是有序的”写进潜空间，比单纯放大模型更贴 SLA 构念。SALR 末层仍占主导权重大，辅层增益虽在但权重很小；方法强在效率与可解释，对非 CEFR 半档量表的外推需另验。


# Adaptive Multimodal Expert Specialization by Meta-Learning for Spoken English Assessment

- 论文编号：1650
- 报告人：Cong-Thanh Vu
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/vu26_interspeech.pdf

## 问题
面试式口语英语评估依赖音视频多模态，但隐私与数据稀缺使深度模型难训；单模型多准则联合优化易冲突，且难以快速适配新说话人/任务。

## 方法
在 Vericant SEE（CEFR 对齐，五维约 20 子准则）上：视频切重叠片段构造元任务；提取 DisVoice 韵律、Qwen3-Embedding 文本、话轮/rubric 统计、OpenFace HAU。经投影与 Transformer 跨模态交互后，16-expert MoE（top-2 门控）+ 多头打分。用一阶 MAML 学可快速适配的初始化。分类用 BCE；回归用 soft-discretized（KL + load-balance + MSE + margin）。贝叶斯优化超参。

## 实验与结果
ETS Vericant（427 人，9–16 岁）：Prosody-Turn（M2）上 SEE 分类 F1 84.88%、回归 MSE 0.225，相对基线 [23] F1 81.78%、MSE 0.333（约降 32.4%）。消融：去 MAML、换 Dense、去 rubric 特征等均明显变差。MIT Interview 上 Turn+Prosody+HAU 达 F1 67.04，接近既有多模态工作。

## 结论
MoE 专长化 + 元学习可在极端小数据下提升多准则口语评分，并迁移到雇佣面试可雇佣性预测。局限是仍依赖预训练特征抽取。

## 点评
把“每个准则当可适配子任务”与 MoE 路由结合，直接回应数据稀缺与准则冲突。特征侧强依赖手工/预训练表征，细粒度声学差异可能被瓶颈；MIT 结果有波动，小样本重复实验的报告方式值得注意。


# Using Phonological-Level Wav2Vec2 for Mandarin Automatic Mispronunciation Detection and Diagnosis

- 论文编号：869
- 报告人：Jinghao Chen
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chen26g_interspeech.pdf

## 问题
普通话 MDD 中，端到端音素检测准确率提升后，诊断反馈仍常停在音素对错，未显式拆分音段与声调属性，难解释错误如何产生。

## 方法
用 Dragonmapper 等将转写转为 IPA（Pinyin 仅作中间层）；把每个音素映射为发音方式/部位、元音高度/前后/圆唇、双元音、声调等二值属性。在 Wav2Vec2-XLSR-53-CTC 上做多标签属性序列预测。对比 IPA-S/IPA-D（双元音是否拆分）与 Tone-Cat/Tone-PT（类别声调 vs 音高目标描述）。推理时属性比对得属性级反馈，再经 attributes-to-phoneme 转写得音素级诊断。母语 CV13-CN 训练，AISHELL-1 做跨库识别，LATIC L2 做 MDD。

## 实验与结果
AISHELL-1 上 IPA-D 显著降 AER（如 IPA-D×Tone-CAT 平均 AER 0.0183 vs IPA-S 约 0.033）。LATIC 音素 MDD：相对 Wav2Vec2 音素基线，IPA-D×Tone-CAT 的 FAR 9.97%→8.15%、DER 34.03%→27.86%；IPA-D×Tone-PT DER 最低 26.05%。Tone-PT 在属性级可降 tone FRR/DER，但 FAR 上升。混淆对上，只评区分性属性可进一步降 FAR（声调对平均约降 72%）。

## 结论
统一建模音段与声调语音学属性，可降低 FAR/DER 并提供更细诊断；双元音分解是主要增益来源，音高目标表示利于声调诊断但更敏感。

## 点评
把“错在哪”细化到 articulatory/tonal 属性，比单纯音素替换列表更符合 CAPT 反馈需求。LATIC 说话人少、错误稀疏，单对混淆统计波动大；Tone-PT 的 FAR–诊断分辨率权衡说明属性粒度需按应用选。


# Domain-Aware Mispronunciation Detection and Diagnosis Using Language-Specific Statistical Graphs

- 论文编号：3239
- 报告人：Hanh Nguyen
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/nguyen26g_interspeech.pdf

## 问题
MDD 中不同 L1 学习者的音素替换模式系统不同；仅用发音学类别构图（同类全连接、无向、等权）无法刻画跨类混淆、稀有同组替换与方向性错误。

## 方法
从训练数据统计定向替换频率，为每个 L1 建有向加权音素混淆图（边权为条件概率，排除正确发音）。MDD-LSSG：wav2vec2-large-xlsr-53 声学编码器 + 按 batch 的 L1 选图，共享参数 GCN 生成 L1 相关音素嵌入；规范音素序列查表得语言侧表示，与声学做 cross-attention 后 CTC 预测。在 L2-ARCTIC 上按说话人划分训练/测试。

## 实验与结果
检测 F1 59.52%，高于 L1-aware Aux/Look-up Embed（56.41/56.83）、MDDGCN（56.49）、CAT-GCN-MDD（58.24）。诊断 DER 20.88，与强基线接近。多数 L1 上 F1 最优；西班牙语 t-SNE 显示统计图把 /d/-/dh/、/t/-/th/ 等跨类高频混淆对拉近，而类别图仍按类别簇分离。

## 结论
用数据驱动的 L1 特定统计混淆图注入语言分支，比类别先验图与简单 L1 条件嵌入更能提升 MDD 检测，并改善音素嵌入几何。

## 点评
把“谁容易把谁错成谁”做成有向图先验，比扁平 L1 ID 更结构化。图依赖训练集替换统计，小 L1 或未见错误模式会偏；与声学侧融合仍是经典 cross-attn+CTC，增益主要来自语言先验质量。


# Light-weight Pronunciation Assessment via Discrete Speech Token Surprisal

- 论文编号：1153
- 报告人：Shammur Absar Chowdhury
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sara26_interspeech.pdf

## 问题
发音评估常依赖强制对齐、音素清单或昂贵的标注非母语数据，低资源/无学习者语料场景难落地。需要主要用母语资源即可工作的轻量方案。

## 方法
仅用母语（LibriSpeech）训练：HuBERT Layer9 + K-means（K=512）得离散单元；3-gram Token LM 算 surprisal（用标准差/尖峰率等描述，避免均值抹平稀疏错误）。可选 Text2DUnit（CANINE+LoRA 解码器）由参考文本预测规范单元，与学习者声学单元做质心 L2 代价的 DTW，得到距离、失配率、失配 surprisal 等。Ridge 融合为分数；也可无监督直接用特征当质量指标。

## 实验与结果
SpeechOcean762：Audio+transcript 轻监督 Acc/Flu/Pros PCC 0.661/0.763/0.753；无监督 DTW 距离 Acc −0.633。音频 alone 约匹配 aMRT（0.60）。100h vs 960h 母语训练差异很小。L2-ARCTIC 零样本迁移 Ridge(SO-train) Acc/Flu/Pron 0.506/0.492/0.526，本地轻校准可再升。

## 结论
母语离散单元 surprisal + 文本引导 DTW 可在少标或无标学习者数据下做发音评估，并跨库迁移；转写引导带来明显增益。

## 点评
把“不像母语音位配列”操作化为 token surprisal，避开 GOP 管线依赖，对零资源场景很实用。强依赖朗读参考文本时增益最大；无文本时 surprisal 相关较弱，更适合做粗筛而非细诊断。


# ALFreeD: Teacher-Guided Few-Shot Pronunciation Assessment via Segmentation-Free Deviation Modeling

- 论文编号：3247
- 报告人：Meenakshi Sirigiraju
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sirigiraju26_interspeech.pdf

## 问题
自动发音评估常依赖规范音素、强制对齐边界与大量标注；非母语偏差大时对齐易错，端到端模型又吃标注。需要少标、无音素分割的教师引导方案。

## 方法
ALFreeD：用 HuBERT 提教师/学习者帧嵌入；余弦距离 + DTW 得学习者对齐的帧级偏差序列；教师–教师偏差训 GMM-UBM，再用 i-vector 把学习者偏差压成句级向量以抑制非发音变异；仅训两层 MLP 预测分数。教师语音由 Google TTS（美音）合成。在 SpeechOcean762 上变化标注量 {300…2500}。

## 实验与结果
300 标样本 PCC 0.68（相对 GOP 0.62 约 +9.7%）；1000 样本达 0.71（可比 GOPT）；2500 样本 0.74（接近 3M 的 0.76，优于 HiPAMA 0.73）。HuBERT 约第 7 层最好；GMM 32 分量、i-vector 维 10 时最佳。

## 结论
教师–学习者表示空间偏差 + i-vector 聚合，可在无规范音素对齐、极少标注下达到接近全监督 E2E 的发音评分相关。

## 点评
用 TTS 教师作参考回避了母语录音成本，但“教师=合成美音”也可能引入风格/音色偏差。中层 HuBERT 最优符合语音学敏感层直觉；方法给的是句级分数，细粒度音素反馈仍待扩展。


# Automatic Assessment of L2 Speech Intelligibility: Segmental Error Ranking

- 论文编号：2522
- 报告人：Agnieszka Pludra
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/pludra26_interspeech.pdf

## 问题
现有 CAPT 常按“靠近母语”纠一切音段偏差，忽略交际目标——可懂度。需要用音段替换信息预测可懂度，并给出对交际影响最大的音素错误排序。

## 方法
从 VoxPopuli、speechocean762（排除儿童）、Pearson 内部数据筛选 600 条 5–15 秒录音；120 名 Prolific 评分者按 5 点可懂度量表评分（每条 5 人，Krippendorff α=0.67）。Azure 音素识别对齐规范 IPA，提取各音素误读率与音素对替换率；去稀疏特征后训多种回归，最佳为 AdaBoost DTR。用特征重要性得到可懂度导向的音段错误排序。

## 实验与结果
Leave-one-out：AdaBoost MSE 0.48、Corr 0.74，优于随机/均值基线，也略优于以 Azure WER 作相关基线（0.67）。重要音素包括元音 /ɛ ə ɪ i/ 与辅音 /z s ð v k t r l/ 等，讨论中联系功能负荷与常见 L2 难点。

## 结论
音段替换特征可在一定程度上预测可懂度，并由重要性排序引导学习者优先纠正影响交际的音素，支持以可懂度而非母语性为中心的 CAPT。

## 点评
把评估目标从 nativeness 拉回 intelligibility，排序可直接进教学反馈。依赖自动音素识别会误差传播；评分者 L1 匹配带来主观性（α 不高）；样本偏中高可懂度且未建模超音段，作者也承认音段解释力有上限。

