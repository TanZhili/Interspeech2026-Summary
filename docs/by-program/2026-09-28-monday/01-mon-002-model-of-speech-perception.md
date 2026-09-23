# Model of Speech Perception

- 日期：Monday 28 September 2026
- 时间：11:00-13:00
- 形式：Oral（Area 1）
- 论文数：6
- 材料：官方程序中该场全部论文摘要。摘要写明问题、方法与主要结论；未在摘要中出现的数字与细节不写入。

## 技术趋势

本场从语音感知出发，把人类听者实验与计算模型并置。一侧用 Whisper、Qwen2.5-Omni-7B、Wav2Vec2.0 等神经模型对照 L2 元音知觉训练；另一侧用多层感知机与 Lobanov、Nearey 等归一化在 L2LP 框架下拟合非母语元音范畴。

感知侧还触及 Speech-to-Song 错觉中的音素分布偏差与听音指令模式，以及 informational / modulation / energetic masking 的相互作用如何抬升可懂度。这表明“刺激结构 + 听音任务设定”仍是解释主观现象的关键杠杆。

工程侧则把听感努力（LE）与可懂度（SI）预测推向增强语音、合成语音与双耳场景：PHOBI 与 HASANet+ 在大规模主观评分上给出高相关。另有工作用概率单纯形约束闭合 CLIP/CLAP 类对比模型的 modality gap，把几何先验引入跨模态对齐。

合起来看，本场瓶颈在于：人类实验成本高、归一化选择依赖听者画像、掩蔽机制相互抵消难以单点解释；走向则是把 LLM/多语 ASR、经典语音学归一化、听力学预测模型与几何表示学习放在同一感知问题谱系中比较。

## 技术内容

### 人类—模型对照与 L2 元音知觉

**English Vowel Perceptual Training under Multitalker Babble: A Comparison of Humans and Large Language Models**（论文 966；Wenwei Dong）
问题是 L2 听者在多说话人 babble 下的知觉训练代价高，难以确定最优说话人数。工作扩展先前对 2/6 人 babble 与 Wav2Vec2.0 的比较，引入 Whisper 与语音 LLM Qwen2.5-Omni-7B，衡量其与 L2 听者的一致性。摘要称语音 LLM 经 babble 训练后准确率提升，趋势更接近 L2 听者，且在 speech-shaped noise 下比 Whisper 与 Wav2Vec2.0 更接近人类准确率。

**How Speaker Normalization Procedures Influence the Computational Modelling of Non-native Vowel Perception: Implications for the L2LP model**（论文 1574；Jooyoung Lee）
研究归一化如何塑造 L2 元音知觉建模。用 DIMEx100 的 F1-F2 训练 MLP 分类 L1 西班牙语元音，仅改变 raw、gender-wise Z、Lobanov、Nearey 1/2、Gerstman 等归一化，再以 TIMIT 英语元音预测映射并对照人类数据。Lobanov 拟合最强（最低 MAE/RMSE、最高相关与范畴匹配）；作者在 L2LP 下解释为模拟无英语知识听者的 L1 范畴全复制，并提示 Nearey 或更适后续 L2 发展。

### 跨模态几何与听感主观现象

**Closing the Modality Gap via Simplex-Constrained Representations**（论文 2849；Shubham Gupta）
针对 CLIP、CLAP 等对比模型中持续存在的 modality gap，提出将嵌入从单位球面改到概率单纯形，以非负与单位质量和作为跨模态校准先验。通过轻量 softmax adapter 与 Total Variation 相似度，在五个多模态检索基准上将 centroid ℓ₂ gap 降低 97–99%，并称检索性能匹配或超过无约束模型。

**Effects of distributional bias in vowels and consonants on the Speech-to-Song Illusion**（论文 2956；Haruki Kagotani）
考察元音/辅音分布偏差与 speech-song / speech-rap 指令对 Speech-to-Song（STS）错觉强度的影响。120 名日语母语者对系统操纵音素分布的日语短句评分。偏置分布刺激诱发显著更强错觉；Rap 指令评分持续高于 Song 指令，说明音系结构与听音模式共同作用。

### 可懂度、听感努力与掩蔽机制

**Deep learning-based predictions of perceived listening effort and intelligibility across enhanced, synthetic, natural, and binaural speech**（论文 1891；Dirk Eike Hoffner）
评估两类深度学习模型对主观 LE 与 SI 的预测力，覆盖助听器增强、双耳场景与合成语音。PHOBI 基于识别器 phone 后验；HASANet+ 为模仿侵入式 SI 指标的师生模型。基于 39 名听者逾 10,500 条评分，两者测量—预测相关均超过 0.88（含未专门训练的 LE 指标）；PHOBI 平均略优，二者均可推广到训练未覆盖条件。

**Mutual Cancellation between Masking Effects Benefits Speech Intelligibility**（论文 1290；Yixin Gu）
研究 informational masking（IM）、modulation masking（MM）与 energetic masking（EM）的相互作用。用可懂度模型均衡高能量 glimpse 以约束 EM，英语句子由英语、普通话竞争语音或调制受控噪声掩蔽。结果表明语言不相似带来的 IM 释放会被电平线索减弱带来的 IM 抵消；降低掩蔽音在谱—时与时间域调制可改善听辨，MM 释放甚至可抵消 EM 以提升可懂度。

## 本场要点

- 语音 LLM（Qwen2.5-Omni-7B）在 babble 训练设定下比 Whisper/Wav2Vec2.0 更贴近 L2 听者趋势。
- 说话人归一化选择依赖听者画像：Lobanov 拟合 L2LP 初始态，Nearey 或对应后续发展。
- 单纯形几何约束可大幅压缩 CLIP/CLAP 类模型的 modality gap。
- STS 错觉强度同时受音素分布偏置与 song/rap 听音指令调节。
- PHOBI 与 HASANet+ 对 LE/SI 在增强、合成与双耳条件下相关均超过 0.88。
- IM、MM、EM 可相互抵消；调制释放甚至能抵消能量掩蔽以改善可懂度。

## 覆盖核对

- 966 | English Vowel Perceptual Training under Multitalker Babble: A Comparison of Humans and Large Language Models
- 1574 | How Speaker Normalization Procedures Influence the Computational Modelling of Non-native Vowel Perception: Implications for the L2LP model
- 2849 | Closing the Modality Gap via Simplex-Constrained Representations
- 2956 | Effects of distributional bias in vowels and consonants on the Speech-to-Song Illusion
- 1891 | Deep learning-based predictions of perceived listening effort and intelligibility across enhanced, synthetic, natural, and binaural speech
- 1290 | Mutual Cancellation between Masking Effects Benefits Speech Intelligibility
