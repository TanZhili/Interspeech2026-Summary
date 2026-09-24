# Multilingual Speech 2

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：12
- 论文数：13

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖流式语音翻译等待策略、训练数据过滤与跨语对齐、低资源参数共享、离散单元声码器分析、语码混合强制对齐、翻译增强编码器预训练、鲁棒数据增强、副语言表达保留、大规模多语语料，以及 ITN 与视听上下文评测。

翻译系统侧，固定节拍等待易幻觉，学习式等待更贴近真实麦克风场景；S2ST 数据过滤开始直接在成对语音上用 Audio-LLM 做保留/丢弃；最优传输与梯度驱动参数共享用于缩小高低资源差距。

表征与数据侧，离散单元声码器系统分析簇大小与说话人/语言条件；YODAS v3 提供超百万小时高带宽立体声多语数据。鲁棒性议题包括语音学启发的 ASR 错误增强、跨模态对抗鲁棒迁移，以及笑声/哭声等非言语发声的保留。

评测与后处理方面，出现印地—英语语码混合对齐评估、罗马尼亚 ITN 多路线比较，以及用场景视听标签扩展 CXMI 的翻译上下文利用率度量（摘要末尾截断于相关统计）。

## 论文技术总结

# Learning to Wait: Real Streaming Speech-to-Text Translation with an LLM

- 论文编号：1323
- 报告人：Rogier van Dalen
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26u_interspeech.pdf

## 问题
LLM 流式语音翻译的 SOTA（Bestow）用固定 wait-k：按固定音频块节奏吐 token。标准测试集短、静音规整时看起来还行，但真实场景麦克风早开、说话犹豫或过快时，会幻觉或越落越远。

## 方法
在 Bestow 架构（Conformer 语音编码器 + 条件网络交叉注意力 + 冻结 3B LLM+LoRA）上，用可学习 wait policy 替代固定节奏：每步根据已见音频与已输出文本，输出 Wait/Emit 二分类分布；Emit 时再跑 LLM 生成下一 token。训练时用强制对齐得到参考 Wait/Emit 序列，对 wait policy 与 LLM 多任务联合损失，一次算齐所有 (t,u) 组合。解码时交错执行 wait/emit。

## 实验与结果
英→法/韩，训练约 3700h（LibriSpeech+CommonVoice+MuST-C，目标文与对齐由 GPT-4/QWEN 等生成）。评测 Fleurs；另构 SilFleurs（句首加 5s −20dB 噪声）暴露早开麦问题。英→法：Learned 在 Fleurs 上 COMET 0.767、延迟 1.72s（Fixed 3.57s）；SilFleurs 上 Learned 0.745，Fixed 跌到 0.593。英→韩：Learned Fleurs/SilFleurs 均为 0.820，Fixed 从 0.814 崩到 0.486。AlignAtt 基线对静音也明显更差。

## 结论
内容条件的可学习等待策略在保持质量的同时降低延迟，且对句首静音不敏感；固定 wait-k 在真实开麦条件下会灾难性幻觉。

## 点评
抓住了“评测分布 ≠ 真实开麦/语速”这一部署痛点，用 SilFleurs 把固定节奏的失败模式钉死。Wait policy 条件于已输出文本，相对 continuous integrate-and-fire 更合理。脆弱处是对齐与目标翻译依赖外部 LLM/强制对齐，且长句、快语速下的追赶行为正文未充分量化。


# Leveraging Audio-LLMs to Filter Speech-to-Speech Training Data

- 论文编号：1148
- 报告人：Qixu Chen
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/chen26l_interspeech.pdf

## 问题
端到端 S2ST 依赖大规模挖掘并行语音，噪声、切分错误与语义不一致会伤训练。启发式（时长比、ASR 长度比）或偏语义的 QE（如 BLASER）对声学劣化、合成伪影与语音对错位不够敏感；纯 ASR+文本 LLM 过滤又丢声学信息。

## 方法
两阶段 Rank→Distill：用 SNR、UTMOS、ASR 转写上的 LLM adequacy、BLEURT 等弱信号构造 clean/noisy 偏好对（含受控劣化），训 LambdaMART 排序器；对大池打分取 top-K/bottom-K 作 keep/drop 伪标签；再指令微调 Qwen2-Audio（4-bit+LoRA）直接对源/目标双音频判决 keep/drop。下游用 Fairseq S2UT（去掉辅助 CTC 等）在筛选数据上从头训练。

## 实验与结果
CVSS-C FR→EN + 20% SpeechMatrix：未过滤 ASR-BLEU 21.32；Audio-LLM 保留约 477k 对达 22.72（约 +1.4）。同预算下优于随机、BLEURT、BLASER、70B 文本 LLM。仅 Stage I 排序选 477k 得 21.91；去掉 Stage I 几乎不过滤。DE→EN 简化信号集上未过滤 13.27→过滤后 15.14。Audio Flamingo 3（单音频拼接）更弱。

## 结论
Rank→Distill 可把弱质量信号蒸馏成语音条件 keep/drop 模型，提升 S2ST；当前二值判决不便固定预算下灵活控量，未来可做概率/预算感知选择。

## 点评
把“排序比绝对打分更稳”做成伪标签流水线，再让 Audio-LLM 直接听双语音，针对 S2ST 挖掘数据里声学+语义耦合噪声。匹配预算的对比设计较干净。脆弱处是伪标签仍绑在手工阈值与劣化分布上，且二值过滤与实际保留量控制脱节；单作者稿还依赖特定 Audio-LLM 双音频能力。


# POTSA: A Cross-Lingual Speech Alignment Framework for Speech-to-Text Translation

- 论文编号：695
- 报告人：Xuanchen Li
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/li26k_interspeech.pdf

## 问题
SpeechLLM 的 S2TT 在高资源语对强、低资源弱。Whisper 等编码表示常按语言成簇而非按语义，翻译映射难跨语言复用；现有对齐多走 speech→text，易压扁声学细节，且各源语言独立，忽视跨语言共享表示。

## 方法
提出 POTSA：冻结语音编码器与 LLM，只训 Q-Former。(1) Bias Compensation：按语言估计全局偏置并减去，粗对齐。(2) 用语义相同的跨语言并行语音对，在选中的 Q-Former 层上对 token 序列做 Sinkhorn OT 损失，与翻译 CE 联合。(3) 基于 UCB 的在线 reward-guided 层调度，把 OT 集中在更有效的（偏底层）层。并行对采用随机语对双向对齐，而非英语锚点。

## 实验与结果
CoVoST2 先 ASR 再 En→Zh，再在 FLEURS 上五语→中文混合微调（每语约 10h）。相对 WhisperV3+Qwen2.5 基线，五语平均 BLEU +1.29（31.84 vs 30.55），零样本六语平均 +2.93（20.84 vs 17.91）。消融：去 Bias/OT 均降；英语可训锚点最差。OT 优于 MSE/余弦；调度仅在较低层优于全层对齐。R@1 与 1−JSD 显示跨语言一致性提升。

## 结论
少量并行语音 + OT 对齐即可增强跨语言表示一致性，缩小高低资源与零样本差距；机制可接入更大 SpeechLLM。

## 点评
把问题从“再堆数据”转到“源语言表示是否可比”，用粗偏置消除 + 细 OT 软匹配，比强制点对点更贴合未对齐的语音 token。层调度避免高层 CE 与对齐目标打架是实用细节。脆弱处是依赖并行语音对质量、OT 权重与层选择超参，以及英文锚点失败暗示对齐图结构敏感。


# Automated Gradient-Driven Parameter Sharing for Low-Resource Multilingual Speech-to-Text Translation

- 论文编号：1292
- 报告人：Ruiyan Sun
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/sun26d_interspeech.pdf

## 问题
多语 S2T（如 SeamlessM4T）均匀共享参数，在低资源下易出现梯度冲突与负迁移；共享–私有结构多靠人工或昂贵 NAS，配置搜索难扩展。

## 方法
提出 GDPS：从梯度行为自动定共享配置。(A) 语言间梯度余弦 + 聚类得分组；(B) 自任务/跨任务梯度相似度差 δ 映射共享比例；(C) Joint SVD + 正则 CCA 得子空间与能量比例，用于私有支路初始化。实例化：只特化 Encoder Layer 11 的 FFN2，分成共享与组私有分支（分析得 Group1=Bem，Group2=Aeb/Est/Gle，约 50% 共享），再分组微调。

## 实验与结果
IWSLT 2025 低资源四语→英（aeb/bem/est 各 20k，gle 7k）。相对 Unified FT：如 Gle BLEU 43.59→46.20、COMET 0.7257→0.7473；Aeb BLEU 7.64→8.74。相对提升最高约 BLEU 14.4%、BERTScore 11.9%、COMET 3.26%。消融显示 A/B/C 缺一则降；50% 共享优于 75%/25%；换到低冲突模块（L10 FFN2、Adapter）增益变小或变差。

## 结论
用训练动态直接导出共享配置，可在低资源多语 S2T 上稳定优于统一微调，无需手工架构搜索。

## 点评
把“哪一层冲突、哪些语该一组、共享多少”从经验变成可测的梯度统计，再只动冲突瓶颈 FFN，改动面可控。Purity Paradox（更深更自相似却更不纯）解释选层有说服力。脆弱处是阈值与 k=2 分组偏数据依赖，四语规模小，换骨干或语对需重跑分析；且相对吃外部大数据的 IWSLT SOTA 仍有差距。


# Multilingual Multi-Speaker Unit Vocoders: A Systematic Analysis of Discrete Speech Representations

- 论文编号：3330
- 报告人：Naman Kothari
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/kothari26_interspeech.pdf

## 问题
SSL+k-means 离散单元纠缠音素、说话人与语言信息，多语多说话人生成易出现说话人混叠与跨语干扰；单元声码器常被当作附属模块，簇大小与条件策略缺乏系统分析。

## 方法
以 BigVGAN 为骨干，输入改为离散单元 embedding；可选拼接 ECAPA-TDNN 说话人嵌入与语言嵌入，并加基于 mel 的辅助 LID（真实与生成 mel 的 CE，λ=1）。单元来自 Data2Vec-AQC 第 21 层，在 22 种印度语 1200h 上训 k-means（500/1k/2k/5k/10k）；声码器在孟加拉语、印地语、泰米尔语、泰卢固语四语 IndicVoices-R 上训练（约 71–134h/语）。对比：仅单元、+说话人、+语言+LID、说话人+语言+LID。

## 实验与结果
未见说话人测试：簇越大 WER 越低（如孟加拉语仅单元 500→10k：60.42→25.13）。无说话人条件时 SIM 约 0.16–0.21 且句内音色混乱；加 ECAPA 后 SIM 升约 4–5×（10k 时约 0.67–0.77）。语言条件在小簇上降 WER 更明显，大簇增益减弱甚至略伤（如印地 10k：说话人 23.99 vs 联合 24.84）。音素纯度/PNMI 随簇增大上升，簇纯度下降；500 簇时跨语同音素常共享簇 ID，10k 时趋于分语分离。

## 结论
簇大小主要通过音素可分性决定可懂度；显式说话人条件对防身份崩塌必不可少；语言监督主要在小簇、单元歧义大时有用。

## 点评
把声码器从流水线里拆出来做受控消融，结论可直接指导 Audio LLM/S2ST 的单元库存与条件设计。跨语共享表把“小库存混语、大库存分语”说清楚了。脆弱处是评测语仅四种、UTMOSv2 无趋势可报，且大簇带来更长离散序列与建模成本，正文未讨论下游 LM 负担。


# Evaluation of forced alignment of code-mixed speech: the case of Hindi-English

- 论文编号：2179
- 报告人：Ayushi Pandey
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/pandey26b_interspeech.pdf

## 问题
印地语–英语语码混合的强制对齐面临扩展音素表、拼写（nuqta 常缺）与说话人自由变体；现有工具与单语假设不足，音系分析与边界标注基础薄弱。

## 方法
在 PBCM 语料（约 6941 句、113 说话人）上用 MFA v1.0。实验1：针对 [ph]∼[f]、[Ã]∼[z] 五套词典 bootstrap（无映射、多数基线、映射到本土/擦音代理、最大 bootstrap）。实验2：用去歧义后的词典，比较三种声学训练——整句语码混合、单语印地短语块、孤立英语词——对齐句中英语词，以手工金标中点绝对误差评价。

## 实验与结果
[ph]∼[f]：无映射 F=0.72；多数基线完美；ph→p F=0.97，f→s 很差。金标显示说话人几乎稳定产出 /f/。[Ã]∼[z]：无映射 F=0.16；最大 bootstrap（Ã→c, z→s）最好 F=0.74。实验2：语码混合句训练平均误差 4.15 ms，约为单语印地（38.18 ms）或英语词（37.58 ms）的 1/10；<10 ms 覆盖 87.06% vs 约 42–48%。

## 结论
原则性词典设计（bootstrap）与语码混合句级声学训练对双语对齐均必要；语码混合数据即使词级也常优于更大单语印地训练。

## 点评
把 nuqta 缺失导致的双向变体问题说清楚了，并区分“几乎已稳定的 /f/”与“仍双变体的 Ã/z”。用句级混合数据训声学模型这一结论对下游语音工具很实用。局限是 MFA 版本较旧、手工金标规模有限，新版 MFA 与说话人条件发音概率仍待验证。


# Does Translation-Enhanced Speech Encoder Pre-training Affect Speech LLMs?

- 论文编号：3241
- 报告人：Tomoya Mizumoto
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/mizumoto26_interspeech.pdf

## 问题
Speech LLM 常用 ASR/SSL 编码器，表示偏语言特异，与 LLM 统一语义空间错位；Whisper 类预训练多为 X→en 单向翻译，英语输入侧未必学到跨语语义抽象。

## 方法
控制实验：Whisper-medium 式 Seq2Seq 编码器在 en/ja/zh/de（约 130k 小时，翻译目标由 Qwen2.5-32B 合成）上比较三种目标——仅 ASR、ASR+X→en、ASR+双向 X↔en（统一 75:25 转写/翻译比例，英文亦做 en→X）。丢弃解码器，接冻结 Llama-3.2-1B/3B，只训 CNN+线性 adaptor（约 6.2k 小时多任务），评 ASR/ST/意图/情感。

## 实验与结果
双向配置在 ASR 与 ST 上整体最优；1B 上日语 CER 29.2→19.7，en→X（含预训练未见的 fa/id/sv/tr）明显提升。3B 意图分类：双向使英语 57.3→64.5、德语 57.9→66.3；情感识别几乎不受预训练目标影响。解冻编码器时双向仍领先。

## 结论
编码器预训练加入双向翻译能改善与冻结 LLM 的跨模态对齐，并更好解锁其多语能力；增益对语义类任务明显，对依赖细粒度声学的情感任务有限。

## 点评
用“冻结 LLM、只换编码器目标”干净隔离因果，指出 Whisper 式不对称翻译对英语输入的盲区。合成平行数据规模与四语子集是现实折中，但也可能引入翻译噪声；情感无增益说明翻译目标主要塑形语义而非副语言表征。


# PiDA: Phonetically-Informed Data Augmentation for Robust Vietnamese Speech Translation

- 论文编号：1963
- 报告人：Xuan Tung Nguyen
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26f_interspeech.pdf

## 问题
级联越南语 ST 中 ASR 错误会传到 NMT；FLEURS Vi–En 上 clean 与 ASR 输入差约 6.79–10.64 BLEU。不清楚该注入何种噪声；通用随机/LLM 噪声未必匹配真实语音混淆。

## 方法
先用 PhoWhisper-large / wav2vec2-base 转写 FLEURS 训练集，按语音学关系把替换错误分为元音/辅音/声调/OOV/无关/正字变体，并用混合效应模型回归对 ∆TER 的影响。据此提出 PiDA：XPhoneBERT 音节嵌入建近邻索引，按训练 WER 统计标注删除/替换，再以温度 softmax 从 top-k 音近音节采样替换。用 clean+PiDA 微调 VinAI-Translate。

## 实验与结果
词内错误以音系混淆为主；元音混淆对 ∆TER 影响最大（系数 97.66）。clean & PiDA：PhoWhisper ST BLEU 28.29（相对 clean 微调 +2.04），wav2vec2 亦显著提升，且 MT BLEU 略升至 33.72。仅真实 ASR 噪声可提 ST 但伤 MT；MEDSAGE 无显著 BLEU 增益。k=5、τ=0.5 最优且较稳。

## 结论
越南语 ASR 替换多为系统性音系混淆；音近嵌入增强可在无音频、无 LLM 条件下提升级联 ST 且不牺牲干净文本 MT。

## 点评
用 LMM 把“该注入什么噪声”实证化，再把增强绑定到 XPhoneBERT 音近空间，比随机词表或英语中心 LLM 更贴合越南语音系。局限是单数据集、未建模 OOV 跨语映射，插入错误也未仿真。


# MoVE: Translating Laughter and Tears via Mixture of Vocalization Experts in Speech-to-Speech Translation

- 论文编号：42
- 报告人：Szu-Chi Chen
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/chen26_interspeech.pdf

## 问题
现有 S2ST 语义准确但常抹掉笑声、哭泣等非言语发声（NV），损害语用；真实 NV 数据稀缺，且单一适配器难同时建模冲突情感。

## 方法
合成管线：IndexTTS2 + 情感/NV 提示（CREMA-D/MSP-IMPROV/IEMOCAP、笑声检测、JVNV 哭泣），属性解耦投影稀有 NV 到多样说话人，再经静音/WER 过滤得 En⇔Zh 对。在冻结 Kimi-Audio 上：五路 LoRA 专家（Happy/Sad/Angry/Laugh/Cry）分阶段专训，再训 token 级 soft router 混合专家；并微调 detokenizer 以重建极端 NV。宣称约 30 分钟精选数据即可接近全量情感保真。

## 实验与结果
相对 Seamless/gpt-4o-audio/Kimi 等，MoVE NV Match 76%（基线最高约 14%），Nat. MOS 3.85、Emo. SMOS 3.79 最高；en→zh ASR-BLEU 32.5。同数据单 LoRA NV Match 仅 26%；A/B 偏好 MoVE 60%。自建数据 50h 单 LoRA 已优于 SynStard/SeamlessAlign 子集。路由无显式标签仍达约 63.7% 主专家对齐。

## 结论
合成表达数据 + AudioLLM 上的 MoE-LoRA，可高效保留笑声/哭泣等 NV；数据效率主要来自预训练先验而非 LoRA 本身。

## 点评
把 S2ST 的“表情塌缩”拆成数据与干扰两大瓶颈，用分专家再 soft 混合直接对症。NV Match 相对商业/开源基线跃升鲜明。脆弱处是依赖 IndexTTS2/Kimi 的 En–Zh 中心设定、合成–真实域差，以及主观评测规模较小。


# Cross-Modal Robustness Transfer (CMRT): Training Robust Speech Translation Models Using Adversarial Text

- 论文编号：2278
- 报告人：Gerasimos Spanakis
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/issam26_interspeech.pdf

## 问题
E2E-ST 多在干净语料上训练，对非母语/方言中常见的屈折形态变异脆弱；文本侧可用 MORPHEUS 对抗微调，但合成对抗语音昂贵，且 TTS 攻击需滤掉同音异形。

## 方法
CMRT 两阶段：先用词级强制对齐上的 WACO 对比学习 + 语音/文本 mixup + 对称 KL，拉齐语音与文本语义空间（CMRT-TR）；再冻结语音编码器，把对抗文本嵌入注入对齐后的语音流形做对抗 mixup 微调（CMRT-FN）。Speech-MORPHEUS：对转写做同 POS 屈折扰动，经 TTS 合成，并排除同音候选。骨干为 HuBERT/mHuBERT + Transformer，数据 CoVoST 2（En-De/Ca/Ar、Fr-En）。

## 实验与结果
相对 HuBERT-Transformer，CMRT-FN 在对抗测试上平均约 +3.4 BLEU，且优于未做对抗微调的 CMRT-TR；相对在 50k 对抗语音上微调的 TTS-Morpheus-FN，干净集掉点更小（约 0.6 vs 3.6 BLEU）。干净 TTS 回放分数不低于原测试，说明掉分来自屈折攻击而非 TTS 音质。

## 结论
在强跨模态对齐前提下，仅用对抗文本即可把屈折鲁棒性迁到语音模态，接近真对抗语音微调且更好保住干净性能。

## 点评
核心洞见是“对齐好了就能在嵌入空间换文本扰动”，避开造对抗语音。同音过滤对法语等尤其关键。脆弱处依赖强制对齐质量与 TTS 评测链，攻击覆盖的是形态屈折而非更广声学噪声。


# YODAS v3: Over 1 Million Hours of High-Bandwidth, Stereophonic, Multilingual Speech

- 论文编号：386
- 报告人：William Chen
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/chen26d_interspeech.pdf

## 问题
开源语音总量与专有数据差距大，且多为 16/24 kHz 单声道，难支撑全频带编解码、空间音频、立体声增强等；现有大规模集语言常严重偏英语。

## 方法
发布 YODAS v3：>1.1M 小时、147 语、48 kHz 多通道 OPUS、CC BY 3.0。按语言从维基构建关键词并搜 CC YouTube，优先新上传、去重相对 v2；保留最高质量音频、原语字幕（人工极少，约 3.7%）与非英语的英文字幕、描述与时间戳。分析语言/时长/有效带宽/有效声道；基线训 ASR 与 DAC 编解码。

## 实验与结果
22 语>10k 小时、73 语>5k；英语占比 <2%。约 92.5% 有效带宽>32 kHz，71%（约 780k 小时）为真多声道。ASR（OWSM v4 初始化）：更宽松 CTC 过滤通常更好，说明字幕可直接用。48 kHz DAC 在域内/LibriTTS 上 STOI 与说话人相似度优于低采样率及 AMUSE 等基线。

## 结论
提供首个百万小时级、真高带宽立体声且语言更均衡的开源弱标注语料，可直接支撑 ASR 与高保真编解码研究。

## 点评
采集侧按语言关键词与新视频优先，从源头缓解英语垄断；带宽/声道有效性检验比名义 48 kHz 更可信。弱标签依赖 YouTube ASR/locale，长视频与 Shorts 混杂，下游仍需任务向清洗。


# Inverse Text Normalization in Romanian: A Comparative Study of Rule-Based, Neural, and Large Language Model Approaches

- 论文编号：3454
- 报告人：Oana Sirbu
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/sirbu26_interspeech.pdf

## 问题
罗马尼亚语 ITN（口语数字/日期等→书面形式）此前缺乏系统研究；需处理性数一致、罗马数字、机构命名等，且缺少统一评测与跨域证据。

## 方法
制定罗马尼亚 ITN 指南与 24,753 条手工口语–书面对（新闻为主，另含 400 条 OOD：有声书/童话/影视/播客）。统一指标：Global / Copy / Norm WER 及 Mean WER。比较 NeMo/Pynini 文法、微调 mT5、few-shot LLM（o4-mini）、agentic 工具调用、微调 RoLlama3.1-8B。

## 实验与结果
域内 Mean WER：LLM 提示 1.21%、RoLlama 1.75%、NeMo 1.92%、Agentic 2.84%、mT5-small 8.38%。OOD：LLM 2.57%（接近人工 2.45%）、RoLlama 3.97%、NeMo 4.56%。文法高效无 GPU；few-shot 约 $0.0073/句，agentic 更便宜但更弱；mT5 多种规模均偏高误差。

## 结论
罗马尼亚 ITN 存在清晰精度–成本权衡：LLM few-shot 最准且跨域强，确定性文法在隐私/边缘场景仍具竞争力；纯小神经模型数值不稳定、覆盖不足。

## 点评
把 Copy/Norm 拆开评测很适合 ITN（既要改对数字又不能乱改上下文）。资源与指南开源便于复现。脆弱处是新闻域主导标注、API 模型版本漂移，以及 agentic 未跑赢强文法说明工具编排未必优于精心规则。


# Audiovisual CXMI: Scene-based Context Tagging for Spoken Language Translation Evaluation

- 论文编号：2175
- 报告人：Dayeon Ku
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/ku26_interspeech.pdf

## 问题
句级指标难衡量上下文利用；文本 CXMI 能量化上下文，但缺视听线索，实验中甚至给人译打分低于机译，与人类判断相反。

## 方法
提出 AV-CXMI：镜头检测 + ResNet 场景边界，再用分离人声、ECAPA 说话人聚类与 Jaccard 重叠 refine 场景。从视频/音频用 GPT-4o（及音频变体）提取 SETTING/REL/TIME/MOOD，并用分类器得 DIALOG/POLITENESS；标签与前 k=2 句构成扩展上下文。mBART 式模型在匹配标签条件下比较有无文本上下文的交叉熵差。韩–英影视翻译上验证。

## 实验与结果
AV-CXMI 与人类判断 Pearson r=0.400（p<0.003），系统效应 η²=0.519（p<0.001），优于纯文本 CXMI；在 77.8% 样本上恢复预期系统质量排序，缓解“人译被文本 CXMI 低估”现象。

## 结论
场景级视听标签扩展 CXMI，使口语/影视翻译评测更能反映情境一致性与人类偏好。

## 点评
抓住评测与人类语用判断错位这一痛点，用结构化 AV 标签而非原始多模态特征，便于解释与复现。依赖 LLM 标注与自洽解码有成本与偏差风险；场景 refine 对音乐/多人重叠仍可能不稳。

