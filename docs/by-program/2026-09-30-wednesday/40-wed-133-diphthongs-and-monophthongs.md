# Diphthongs and Monophthongs

- 日期：Wednesday 30 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：2
- 论文数：5

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从语音学角度讨论单元音与双元音的动态分析：何时需要全轨迹建模，何时静态度量已足够；并以具体语言案例给出时长对比与滑音/分音节对立的证据。

方法论上，综述强调连续非实验室语音中稳态难识别，以及元音序列仍常被压成 DCT 或共振峰变化率等静态指标。实证工作则用 GAMM 与多变量函数主成分分析（MFPCA）同时刻画 F1/F2 全轨迹，并关联性别、地域、年龄与社会阶层等社会语言学因素。

语言案例覆盖 Nakanamanga 单元音时长对立，以及意大利语与罗马尼亚语 /ia/ 的双元音—分音节对立在时长与共振峰动态上的实现差异。

## 论文技术总结

# On the challenges and benefits of dynamic vowel analyses

- 论文编号：
- 报告人：Johanna Cronenberg
- 程序：Wednesday 30 September 2026 / Diphthongs and Monophthongs
- 技术分类键：phonetics
- 材料：官方程序摘要，没有对应的会议论文 PDF

## 问题
如何分析单元音、双元音与 hiatus（元音序列）的动态特性。传统上单元音由其稳态定义，但在连续、非实验室语音中，因发音交叠增强，稳态常难识别；元音—元音序列虽被视为固有动态，却常为降复杂度与计算效率，仍用 DCT 系数或共振峰变化率等静态度量来分析。

## 方法
报告概述近期关于单元音、双元音与 hiatus 动态的研究，展示新的动态分析方法如何为元音及元音序列提供新见解，并讨论在何种情形下更直接的静态分析已经足够。

## 实验与结果
摘要未给出具体语料、统计量或数值结果。

## 结论
动态分析能带来额外洞见，但并非处处必要；需依情形在动态与静态分析间取舍。

## 点评
问题来自语音学测量惯例与连续语音现实之间的张力。摘要点名了静态度量例子（DCT、formant rate of change），但未展开新方法的具体公式。


# Phonetic evidence for contrastive length in Nakanamanga monophthongs

- 论文编号：1597
- 报告人：Shubo Li
- 程序：Wednesday 30 September 2026 / Diphthongs and Monophthongs
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26z_interspeech.pdf

## 问题
瓦努阿图中部大洋洲语 Nakanamanga 是否有音系性元音长短对立、且是否覆盖全部五个元音音色，此前仅有最小对立对论证，缺少时长声学证据。

## 方法
14 名母语者（8 女 6 男）朗读 50 词表（双音节 CV.CV，目标在首音节），载体句中五次重复；Praat 手工切分，EMU/emuR 提取时长。共 2,622 token。线性混合效应模型：Duration ~ VowelLength + VowelQuality + WordLength + (1|Speaker)+(1|Word)，并检验 Length×Quality 交互。

## 实验与结果
短元音均值 85 ms，长元音 177 ms，比值 2.08；Length 主效应约 +82.6 ms（p<.001）。五音色比值 1.88–2.24，各对均显著；Length×Quality 交互不显著，说明长短差距跨音色稳定。闭元音本征更短、词长有轻微压缩，但不掩盖长短对立。

## 结论
时长为 Nakanamanga 全系统短–长对立提供清晰语音证据，支持十元音（五对）音系分析，并与同区域 Nafsan（约 1.91）等数量语言可比。

## 点评
用受控词表 + 混合模型把“词典里的冒号”落到可重复的声学比率，对低资源大洋洲语描写很关键。词表中短元音多落在动词、诱发略偏，但效应量足够大；后续应补感知实验与自然语流/社会语言学变异。


# To glide or not to glide: Acoustic realization of the diphthong-hiatus contrast in Italian and Romanian

- 论文编号：2433
- 报告人：Johanna Cronenberg
- 程序：Wednesday 30 September 2026 / Diphthongs and Monophthongs
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cronenberg26_interspeech.pdf

## 问题
/ia/ 可实现为单音节双元音 /ja/ 或异音节 hiatus /i.a/。意大利语倾向双元音、罗马尼亚语倾向 hiatus，但词汇重音与词内位置如何促进或阻断滑音化，大规模语料上的声学证据不足。

## 方法
意语约 168h、罗语约 300h 广播/电视语料，强制对齐后提取 /i,j/+ /a,ə/ 序列（最终约意 23,681、罗 17,895 token），标注重音与词首/词中。时长按发音速率归一化后 log 变换；F1/F2 转 Bark、去均值、时间归一并用 FPCA，对 PC1/PC3 得分做 LMER（语言×重音×位置）。

## 实验与结果
意大利语重音 vs 非重音时长差清晰（词首约 0.37、词中约 0.56 log 单位）；罗马尼亚各条件重叠大，但非重音序列整体长于意大利语。共振峰：意语重读时更陡、更外周；罗语仅非重音词中 /ia/ 明显更平、更像滑音。两语有大量重叠，对立呈梯度。

## 结论
重音与词位以语言特异方式调节 /ia/ 实现：意语重音可阻断滑音化，罗语更倾向在非重音词中位置滑音化；为后续感知分类研究提供生产基线。

## 点评
用大规模自然语料 + FPCA 把“范畴标签”还原为时长与轨迹形状的连续空间，比小样本实验室词表更能暴露梯度。无说话人 ID、靠 segment 随机效应是局限；感知实验需把重音/位置纳入刺激设计，否则可能低估范畴稳定性。


# Modelling diphthong dynamics: A GAMM-based analysis of Australian English diphthongs

- 论文编号：2861
- 报告人：Ksenia Gnevsheva
- 程序：Wednesday 30 September 2026 / Diphthongs and Monophthongs
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gnevsheva26_interspeech.pdf

## 问题
双元音常只在 20%/80% 两点测 onset/offset，丢掉轨迹中段形状与变化速率；多点测量后统计仍常落在单点上。需检验性别与城乡位置对澳大利亚英语双元音全轨迹的影响。

## 方法
Sydney Speaks 与 Voices of Regional Australia（Braidwood）自然口语，可比子集：中老年、相近职业分、Sydney 仅 Anglo-Celtic；共 27+31 人。Fast Track 提 F1/F2（20–80% 七点），修正 Lobanov 归一，限塞音间。对 FACE、FLEECE、GOAT、MOUTH、PRICE 分别拟合 GAMM（mgcv bam）：Gender、Location 及其交互的参数项与 by-factor 平滑，控制时长与说话人/词项随机平滑。

## 实验与结果
Gender 对五元音均显著；Location 对 FACE、FLEECE、MOUTH 显著。女性与城市说话人整体更“领先”变化（远离 broader 实现）。部分差异在中段或斜率上更清晰：如 PRICE 性别差在轨迹中部；FLEECE 终点更开但全轨迹更单化，静态终点会误判为更保守。

## 结论
全轨迹 GAMM 能揭示单点分析会低估、漏掉甚至误判的社会语音差异；双元音变化可涉及轨迹形状/时序，而非仅平行平移目标点。

## 点评
方法学贡献大于“再报一个社会分层”：用具体反例说明静态测点如何误读音变方向。区域男性职业分偏低需谨慎解释 Location×Gender；扩展到更多社会与语言变量是自然下一步。


# Variation and change in dynamicity of Australian English diphthongs in Sydney

- 论文编号：3206
- 报告人：Benjamin Purser
- 程序：Wednesday 30 September 2026 / Diphthongs and Monophthongs
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/purser26_interspeech.pdf

## 问题
澳大利亚英语双元音是音变热点，但既有研究多静用点测或把 F1/F2 分开建模，难以同时抓住两共振峰随时间的协同动态。

## 方法
ANU Corpus of Sydney Speech 中 119 人自发口语，约 57,269 token（FACE、FLEECE、NEAR、GOAT、MOUTH、PRICE）。10%–90% 九点提取 F1/F2，修正 Lobanov 归一后对各元音做 multivariate FPCA（MFPCA）；对 PC1/PC2 得分拟合混合效应模型，预测项含年龄组、性别、社会阶层、音系语境、时长、语速、词频及年龄×性别交互。

## 实验与结果
前两 PC 解释各元音约 75%–85% 方差。社会模式与既有音变方向一致：青年与女性更靠前（如 FACE 更高更前、GOAT 更高更后、MOUTH/PRICE 更开等）。MOUTH、PRICE 还见中产相对工人阶层的差异。语言语境（尤其鼻音前、词末）系统塑造动态性；部分 PC 主要反映语言而非社会条件。

## 结论
联合建模 F1×F2 轨迹可更整体地刻画双元音动态与社会/语言驱动；社会分层方向与静态研究一致，但揭示了高度与前后维度如何共变。

## 点评
相对分通道 GAMM/DCT，MFPCA 把“形状”压成可回归的分数，适合同时看多类双元音。未展开族裔、且过滤较严；大样本下需靠效应量门槛避免琐碎显著，文中已有意识地只报实质影响。

