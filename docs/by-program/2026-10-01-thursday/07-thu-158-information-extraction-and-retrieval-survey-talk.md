# Information Extraction and Retrieval / Survey Talk

- 日期：Thursday 1 October 2026
- 时间：09:00-11:00
- 形式：Oral
- Area：12
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场以表现力语音翻译综述开场，随后转向关键词检出、口语检索 tokenization、端到端声学命名实体识别，以及端侧少样本文本相似度编码器。信息抽取/检索线强调：零样本用户定义关键词需同时防冒名、离散 token 要可扩展且保持成对对齐、组织名实体依赖跨度结构约束，边缘设备则希望单轻量模型覆盖多类语音邻域分类。

综述覆盖 S2ST 架构、数据与合成、表征、LLM 用法与评测，突出保留说话人音色/情感及词级停顿、语速、重音、音高等局部表现力仍缺共识。应用论文则把说话人验证与音素监督 KWS 晚期融合、分阶段对比学习 + CTC/DTW 对齐训练 tokenizer，并用 LLM 增强与结构约束实体学习强化组织名识别。

## 论文技术总结

# Expressive Speech Translation

- 论文编号：
- 报告人：Philipp Koehn
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
语音到语音翻译仍具挑战，模型结构、训练数据、评估方法等尚未充分共识。前沿之一是在翻译中保留输入语音的表达性：从说话人声音、情绪与声学条件等全局属性，到停顿、语速变化、强调与单词级音高等局部属性。

## 方法
调研覆盖训练数据、数据合成方法、语音表征、模型结构、大语言模型的使用，以及评估指标等各方面。摘要未展开某一单一系统的实现细节。

## 实验与结果
未提供具体语料或数值结果。

## 结论
表达性保持是 speech-to-speech translation 的重要前沿；需要在数据、表征、架构、LLM 利用与评估上系统推进。

## 点评
把「表达性」拆成全局/局部属性，问题边界清晰。材料停留在议题地图，不含可复现配方。


# Personalized Keyword Spotting for User-Defined Keywords Leveraging Text-Independent Speaker Verification

- 论文编号：1130
- 报告人：Ming-Hsiang Hu
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/hu26c_interspeech.pdf

## 问题
用户自定义关键词检出（UD-KWS）学到说话人无关表示后，无法拒绝说对关键词的冒名者；文本相关 SV（如 PK-MTL）又绑死固定关键词，破坏零样本灵活性。需同时应对未见关键词与未见说话人（双零样本），且模型需适合边缘部署。

## 方法
提出 ZP-KWS：双分支解耦——冻结的 EfficientTDNN-Small（约 0.9M）说话人编码器（VoxCeleb2 预训练 + LibriPhrase GE2E 微调，短句嵌入稳定），与音素监督音频编码器（冻结预训练嵌入 + 可训 Conv1D–BiGRU，MFA 帧级音素对齐损失 Lalign）。文本经 G2P 后与音频经自注意力 Pattern Extractor/Discriminator 得到 putt；说话人余弦经标定线性层得 pspk。推理时乘法晚融合 pfinal = putt · pspk，可无重训切换 C-KWS / TB-KWS / TO-KWS。总损失 Lutt + Lphon + Lalign。

## 实验与结果
LibriPhrase Easy/Hard、Qualcomm、Google Speech Commands；关键词与说话人均未见。TO-KWS 上相对最强基线 PK-MTL，FRR@1%FAR 相对降幅最高约 60%（如 LibriPhrase Easy：29.47% vs 72.79%）；C-KWS EER 在多数集仍最优（Easy 2.38%）。消融：去掉 GE2E 后 TO FRR@1% 从 29.47% 升至 73.42%；去掉标定层 TO EER 恶化；总参数约 1.55M。

## 结论
功能解耦的 TI-SV + 音素监督 + 乘法门控，可在零样本关键词设定下加入生物识别安全，并在固定模型上切换严格度。未来关注噪声与失配下的置信度标定。

## 点评
把“关键词分数补偿说话人分数”的加性融合改为严格 AND，切中边缘误唤醒痛点；GE2E 短句微调是 TO 模式增益的主要来源。Hard 最小对上整体 FRR 仍高，说明音素混淆时 SV 只能互补、不能替代内容判别。


# wav2tok 2.0: Scalable Audio Tokenization Maintaining Explicit Pairwise Token Alignment for Efficient Audio Retrieval

- 论文编号：141
- 报告人：Adhiraj Banerjee
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/banerjee26_interspeech.pdf

## 问题
QbE-STD 需要可变长话语间保持相似的离散语音表示；wav2tok 用 CTC 显式对齐但聚类与对比–对齐紧耦合，难扩展；BEST-STD 可扩展但对齐仅隐式依赖 DTW 正样本采样。

## 方法
wav2tok 2.0 以 BEST-STD 为骨干（谱前端 + 双向 Mamba，约 4.7M 参数，VQ 码本）。两阶段训练：Stage I 用 SimCLR 式对比损失 + commitment，经 DTW 构造帧级锚–正对；Stage II 加入无 blank 的 CTC 成对对齐（对去重 token 序列做前向后向），并提出 DTW 对齐的帧级 token 预测损失 Lpair；λCTC 自适应缩放为对比损失量级的约一半，避免 CTC 主导或数值不稳。检索沿用 BEST-STD：1s 段、bigram 倒排索引 + Jaccard 精排。

## 实验与结果
LibriSpeech train-clean-360 训练，在 train-clean-100 检索，并测未见 TIMIT。离散一致性（Table 1）：码本 256 时 unigram/bigram Jaccard 达 0.83/0.75，优于 BEST-STD 与 wav2tok。QbE-STD（Table 2）：512 码本 LibriSpeech IV MAP/MRR 0.86/0.90，OOV 0.82/0.84；TIMIT 上仍领先；相对仅 CTC 的 wav2tok，帧级预测进一步抬高 MAP/MRR 与 MTWV。

## 结论
在可扩展骨干上把显式成对对齐做成一等训练信号，可同时提升 token 稳定（尤其 bigram）与检索指标，且不牺牲效率。未来可并入 OT 码本均衡，并扩展到多语/噪声/长音频与语音 LLM。

## 点评
分段训练把“先聚好再对齐”说清楚，自适应 λCTC 是可扩展配方的关键工程点。增益主要来自检索向目标而非通用 SSL 表征；大码本上 MAP/MRR 与 MTWV 的折中仍在，说明对齐不能消去词汇量–鲁棒性张力。


# Rethinking Organization Entity Modeling in End-to-End Acoustic Named Entity Recognition

- 论文编号：3115
- 报告人：Spandan Dey
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/dey26b_interspeech.pdf

## 问题
端到端声学 NER 中，组织名因多词跨度、缩写、OOV 与跨度内非实体词，比人名/地名更难；常规交叉熵不显式建模实体起止结构依赖，边界易截断或外扩。

## 方法
基于 Whisper-small（编码器冻结，解码器前九层冻结）：(1) LLM（Phi-3-medium）针对性语义增强——缩写展开与词汇改写，再经规则清理，XTTS-2 多说话人合成语音；(2) 训练期专用 `<org end>` 边界标记；(3) Structure-Constrained Entity Learning（SCEL）：在 LCE 上叠加实体差分、标签抑制、跨度覆盖、边界一致性，以及熵正则与置信度标定。数据为 Yadav 等英文声学 NER 库（约 150h，LibriSpeech+Common Voice，90:5:5）。

## 实验与结果
相对纯 LCE（Org-F1 30.35），SCEL 将 Org-F1 提到 40.00、WER 8.27；SCEL+TSA+`<org end>` 达 Org-F1 51.40（相对 SCEL +11.40）、WER 9.53。优于 ASR+Flair 流水线（Org-F1 19.04）与 WhisperNER（约 30–31）。合成单跨/多跨测集上，提议框架多跨 Org-F1 明显高于 CE 基线。

## 结论
组织类弱点可通过对数据增强、类别边界标记与结构损失组合显著改善，同时保持 ASR 与其他实体类别可用；未来扩展多语声学 NER。

## 点评
诊断（多词、缩写、跨度内虚词）与解法（TSA、org end、SCEL）一一对应，比单纯放大 Whisper 更可解释。Org-F1 提升伴随整体 F1/WER 小幅回退，说明类别特化存在权衡；LLM-TTS 增强对真实录音分布的外推仍是主要风险点。


# AnySimLite: A Lightweight Few-Shot Similarity Encoder for On-Device Speech-Adjacent Classification

- 论文编号：1316
- 报告人：Sourav Ghosh
- 程序：Thursday 1 October 2026 / Information Extraction and Retrieval / Survey Talk
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/ghosh26e_interspeech.pdf

## 问题
端侧语音相邻 NLP（意图、情感等）若为每任务部署专用大模型，存储压力大；许多任务可归约为“细粒度文本相似”（NTS），需要单一轻量编码器在少样本下覆盖多任务。

## 方法
提出 ANYSIMLITE：词嵌入通道（含注意力）+ 字符 Conv/池化通道，编码器输出后余弦相似；玩具任务 Event Title Similarity（同事件且同命名实体才算相似）。用 DBSCAN 聚类采样“困难”正负对（簇内/簇间约 8:2）把分类集改造成成对相似数据。消融选 B3 为基座，B8 用 MiniLM 蒸馏为部署变体。少样本：每类 20 个样例预计算 16 维嵌入后近邻分类。

## 实验与结果
TitleSim 消融 B3 F1 89.22（0.42M）；部署变体 Acc 90.83。跨任务（Table 2）：相对各任务 SOTA，最差降幅低于约 7%，参数远小于 qLLaMA LoRA-7B 等；SMS Spam 上 F1/Acc 达 97.50/99.28。Galaxy S25 Ultra：8-bit 约 700KB、推理 <30ms。相对最优结果平均准确率降约 2.24%±3.23%。

## 结论
词+字符轻量相似编码器配合困难对变换，可在极少参数下把多种语音相邻分类压到 NTS 少样本协议，并适合端侧。未来可探索分类以外任务。

## 点评
把多模型问题收成“一个相似核 + 每任务样例库”，工程叙事清晰；字符通道针对 OOV NE 与端侧词表限制。NTS 归约假设任务可用样例原型刻画，对细粒度多标签或强依赖语序的任务可能变脆；与大模型差距任务相关，不宜外推为通用 NLP。

