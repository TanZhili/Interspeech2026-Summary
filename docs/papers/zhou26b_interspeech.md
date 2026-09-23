# Intonation Perception in Real and Synthetic Speech across Varying Familiarity Levels: A Pilot Study of Equivalence Assessment

- 论文编号：996
- 报告人：Hanrui Zhou
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhou26b_interspeech.pdf

## 问题
语言训练语料建设成本高，AI 声克隆（此处用 F0 条件的 SVC）可降低成本，但现有评价多基于陈述句；普通话疑问语调依赖句末升/高平 f0，且熟悉度影响加工。需检验自然 vs 合成、熟悉 vs 陌生在说话人相似度感知与语调识别上是否等价。

## 方法
17 名普通话成人（相似度任务全员；语调识别 11 人）。4 名女性说话人（2 熟悉、2 陌生）录 10 句中性六字句的陈述/疑问；合成用 seed-vc 类 SVC，客观说话人嵌入余弦相似度陈述约 0.55、疑问约 0.51，再经语音专家筛选。2×2×2 被试内设计（speech type × familiarity × intonation）。任务：(1) 成对同/异说话人判断 + 1–7 相似度评分；(2) 陈述/疑问二分类。PsychoPy；混合效应模型分析 ACC/RT/评分。

## 实验与结果
相似度 ACC：自然–自然对高于自然–合成对（约 0.917 vs 0.851）；speech type × intonation 交互显著——纯自然对中疑问 ACC 高于陈述（0.946 vs 0.875），混入合成后无显著差。熟悉声音 RT 更短（约 0.748 s vs 0.848 s），但相似度评分更低。语调识别整体 ACC 很高（>95%）；Firth 回归显示 familiarity × speech type 交互：自然语上陌生略高于熟悉，合成语上熟悉略高于陌生（简单效应本身未达显著）。疑问 RT 边际更长。

## 结论
疑问语调可能作为说话人识别线索，但受合成特征影响；熟悉度对语调识别的贡献随 speech type 变化。SVC 合成在受控实验中有一定感知可行性，但对复杂韵律与社会线索（熟悉度）仍不足，语料建设仍有挑战。

## 点评
把语调类型与熟悉度同时放进克隆语音评价，比只测自然度/可懂度更贴近训练语料需求。交互效应提示“疑问有助于识人”在合成条件下会打折扣。样本小、语调任务天花板效应明显，主要依赖 RT；试点性质决定外推需更大被试与更广语料。
