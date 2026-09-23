# Pronunciation Diversity
- 日期：Tuesday 29 September 2026 / 时间：09:00-11:00 / 形式：Long Oral / 论文数：5
- 材料：官方程序论文摘要。未出现的数字与细节不写。

## 技术趋势

本跨领域长论文/综述场围绕发音多样性：生成语音模型能否再现语用制约的语调变异、SSL/ASR 模型如何编码非标准音系过程（AAE 辅音丛缩减）、双语者对语音助手的语音趋同，以及可控口音规范化与无提示偏误检测。主题从描写/评测生成多样性，落到模型内部表征与人机语音适应，再到可调节的发音转换与 MDD。

方法光谱宽：Functional PCA 与贝叶斯回归比较人类与 GSM 语调；层析探测 wav2vec 2.0 / Whisper；词汇影子实验测 VOT 与元音时长趋同；掩码离散扩散上的可控口音规范化；以及 CROTTC-IF 的 prompt-free MDD。共同张力是：多样性既是需要保留/理解的社会语音事实，也是 ASR 差距与学习/配音场景中需要可调强度的对象。

综述条目在 JSON 中无 paper_id，按 Survey Talk 处理；其余论文照常列出。

## 技术内容

### 生成语调、非标准音系编码与人机语音适应

**Pronunciation Diversity**（论文 N/A；presenter：Farhat Jabeen）
Survey Talk。回顾评测生成语音模型（GSM）模拟概率语调变异的研究；并以印地语话语助词 “-hii” 为例，用 Functional Principal Component Analysis 与 Bayesian regression 比较人类与 GSM 语调变异及其语用制约。摘要目标是标示 GSM 生成语用合适口语的潜力与局限。官方条目未提供 paper_id。

**Layer-wise Probing of wav2vec 2.0 and Whisper for Consonant Cluster Reduction in African American English**（论文 808；presenter：Hamid Mojarad）
对 AAE 辅音丛缩减做说话人无关层析探测：缩减检测与底层丛身份恢复。两模型高准确区分缩减与规范形式；缩减段仍保留底层塞音线索，表明 CCR 被编码为结构化梯度音系变异而非简单删除，并关联 ASR 差距来源。

**Bilingual Speaker Phonetic Alignment to Voice Assistants**（论文 2391；presenter：Alyssa Allen）
西班牙语主导的西–英双语者在线词汇影子实验中，对人类或语音助手声音在 VOT 与元音时长上的语音趋同。摘要称跨语言与条件均观察到趋同，表明双语者对机器声音亦以类人方式响应；条件与语言效应受方言区、性别等社会信息调节。

### 可控口音规范化与无提示 MDD

**Controllable Accent Normalization via Discrete Diffusion**（论文 1056；presenter：Qibing Bai）
DLM-AN 在自监督语音 token 上做掩码离散扩散；Common Token Predictor 识别可能编码母语发音的源 token 并选择性重用以上下文初始化反向扩散，重用越多口音保留越多；flow-matching Duration Ratio Predictor 调节总时长以贴近母语节奏。多口音英语数据上摘要称 WER 最低，口音减弱有竞争力且强度控制平滑可解释。

**Beyond Acoustic Sparsity and Linguistic Bias: A Prompt-Free Paradigm for Mispronunciation Detection and Diagnosis**（论文 711；presenter：Haopeng Geng）
针对 CTC 忽略短暂偏误与显式规范先验偏向目标音，提出 prompt-free 框架：CROTTC 强制单调帧级对齐，IF 策略隐式注入偏误信息。摘要报告 L2-ARCTIC 与 Iqra'Eval2 上的 F1，并论证声学与显式先验解耦带来稳健 MDD。

## 本场要点
- GSM 语调多样性需相对句法–语用结构评测，而非只听自然度。
- AAE CCR 在现代语音模型中呈梯度结构化编码，相关 ASR 公平性。
- 双语使用者会对语音助手产生跨语言语音趋同。
- 离散扩散 + token 重用提供可解释的口音强度旋钮。
- Prompt-free MDD 试图摆脱规范音提示带来的偏置。
- 综述条目无 paper_id，覆盖核对中记为 N/A。

## 覆盖核对
`N/A | Pronunciation Diversity`
`808 | Layer-wise Probing of wav2vec 2.0 and Whisper for Consonant Cluster Reduction in African American English`
`2391 | Bilingual Speaker Phonetic Alignment to Voice Assistants`
`1056 | Controllable Accent Normalization via Discrete Diffusion`
`711 | Beyond Acoustic Sparsity and Linguistic Bias: A Prompt-Free Paradigm for Mispronunciation Detection and Diagnosis`
