# Layer-wise Probing of wav2vec 2.0 and Whisper for Consonant Cluster Reduction in African American English

- 论文编号：808
- 报告人：Hamid Mojarad
- 程序：Tuesday 29 September 2026 / Pronunciation Diversity
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/mojarad26_interspeech.pdf

## 问题
商用 ASR 对非裔美式英语（AAE）词错率可高达主流美音的约两倍；辅音丛缩减（CCR，如 test /tEst/→[tEs]）是重要音系来源，但现有层探测多关注一般音位/口音，很少剖析模型内部如何编码 AAE CCR——是简单删除，还是保留底层停顿线索的梯度变体。

## 方法
数据来自 CORAAL 的 DCA/DCB/DTA（156 说话人）。用 MFA + CMU 字典训练定制声学模型并对齐；为易 CCR 词生成缩减发音变体；聚焦七类单语素双辅音丛（/ft,nd,nt,st,sk,pt,mp/），词型上限采样后得 6760 token（3409 规范 / 3351 缩减）。冻结 wav2vec2-base 与 Whisper-small 的 12 层编码器，按 MFA 时间戳对丛帧均值池化为 768 维。探测器用单隐层 MLP（200 ReLU），说话人独立 4-fold。任务一：缩减检测（不平衡/平衡/逐丛）。任务二：对共享鼻音 C1 的 /nt/ vs /nd/ 做片段恢复（仅缩减训练、仅规范训练、仅 C1 训练）。另设计协同发音门控探测（截断处）。

## 实验与结果
摘要与引言结论：两模型均能高准确率区分缩减与规范形式；缩减段仍保留底层停止音线索，表明 CCR 被编码为结构化梯度音系变异而非单纯删除。正文抽取在协同发音探测方法处截断，层间准确率曲线与逐丛数字表未见。

## 结论
作者认为现代语音编码器对 AAE CCR 有结构化音系编码；探测有助于从“黑盒 WER 偏置”转向理解偏差机制。边界是全文截断导致定量层结果不可核验，且仅覆盖高频双辅音丛。

## 点评
工作把 ASR 公平性问题落到可检验的音系过程编码上，双探针（检测+恢复）设计直接对应“删没删 / 删了还知不知道是什么”。强处是说话人独立、控词频与单语素限制；脆弱处是强制对齐标签噪声、probe 表达力有限，以及抽取截断使“高准确率”缺少层间证据支撑。
