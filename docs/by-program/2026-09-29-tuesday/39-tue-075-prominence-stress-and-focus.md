# Prominence, Stress and Focus

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Oral
- Area：2
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从可解释的无文本突显检测到跨年龄、双语与跨语言感知，再延伸到方言语调类型学与机器人 TTS 韵律期望。一条技术线把心理声学原则直接编进极小参数检测器；多条实验线则检验焦点的 F0 模式是否随年龄、L1 有无 post-focus compression 而变化。

感知研究用陌生语言刺激剥离词汇/语用因素，显示突显与 IP 边界线索的非普遍性。Venetan 宽焦点升调与机器人嗓音“更像机器反而更易听出逗号边界”的结果，共同说明：韵律范畴与听者期望强烈互动，不能假设单一普遍线索层级。

## 论文技术总结

# Auditory Contrast Network for Text-Free Prominence Detection

- 论文编号：250
- 报告人：Kosuke Shimizu
- 程序：Tuesday 29 September 2026 / Prominence, Stress and Focus
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/shimizu26b_interspeech.pdf

## 问题
词级感知凸显依赖与邻词的相对对比，但主流 CNN/SSL 检测器无显式邻比机制，且常需文本，不利端侧无文本场景。

## 方法
Auditory Contrast Network（≤238 参数）：对时长、能量、频谱、F0 等线索分别用小 MLP 算与前/后词的非线性对比，softmax 注意融合方向，再聚合原始线索与可选 surprisal。编码成对对比、线索独立与前向主导等心理声学原则。Helsinki Prosody→Emphases 跨库迁移评测。

## 实验与结果
仅声学：r=0.412，匹敌冻结 wav2vec2（94.6M，r=0.409），延迟约低 120×；加文本 r=0.451。学得权重显示前向上下文 >96%、±1 词局部最优、线索序 duration>energy>spectral≫F0。

## 结论
极轻量、可解释的对比架构可在无文本时达到大模型级相关，适合助听器与实时发音监测。

## 点评
把心理声学直接写进结构，可解释性是卖点；相关仍中等，任务是连续凸显评分而非焦点检测，外延需谨慎。


# F0 realization of prosodic focus across adulthood in Jianghuai Mandarin

- 论文编号：255
- 报告人：Xinxian Zhao
- 程序：Tuesday 29 September 2026 / Prominence, Stress and Focus
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhao26b_interspeech.pdf

## 问题
焦点的三区 F0 模式（焦上抬高、焦后压缩 PFC、焦前大致不变）在江淮官话是否成立，以及成年期（青/中/老）细粒度调节是否随衰老变化，此前多聚焦青年。

## 方法
60 名灌南籍母语者（20–30、40–50、60–70 各 20，性别匹配）产出中性焦点与三类窄焦点 SAVO 句；分析 mean F0 与 F0 excursion 等。

## 实验与结果
江淮官话总体呈现典型三区模式，各年龄组全局格局大体保留。窄焦点相对中性焦点的细调有年龄差：老年人在 mean F0 上表现出更大的焦后压缩。

## 结论
跨成年期焦点韵律表现为稳定全局 F0 格局 + 年龄敏感的细粒度调节。

## 点评
把方言类型学与语音衰老接到同一实验，补空白。强在三组均衡设计；需注意衰老与风格/努力差异的可能混淆，且结果主报 F0。


# Prosodic Realization of Focus in Yi-Mandarin Bilingual Speakers: On-Focus Expansion without Post-Focus Compression

- 论文编号：660
- 报告人：Ziyu Zhang
- 程序：Tuesday 29 September 2026 / Prominence, Stress and Focus
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26g_interspeech.pdf

## 问题
彝语（Nuosu）缺焦后压缩（PFC），北京话有；彝–普通话双语者在 L2 普通话中能否获得 PFC，以及焦上扩展（OFE）与 PFC 是否可分离。

## 方法
21 名彝语 L1–普通话 L2 说话人 vs 5 名北京话对照；同调三词句，初/中/末焦点 + 中性；ΔF0、Δ强度为主、时长为辅。混合效应模型与 Bonferroni 事后对比；问卷测普通话经验是否预测焦后 F0。

## 实验与结果
彝语组焦上 F0 扩展与北京对照相当，但各焦点条件下 F0 与强度均无焦后压缩；个体普通话背景不能预测焦后 F0。显示 OFE 完整、PFC 缺失的完全分离。

## 结论
当 L1 完全缺乏 PFC 时，即使长期双语接触也可能在 L2 中抑制该机制；支持 OFE 与 PFC 为相对独立、习得轨迹不同的韵律模块。

## 点评
用自然双语社群检验“无 PFC 的 L1 能否长出 PFC”，设计干净。对照北京组较小，经验测量若偏自陈可能解释力有限，但不影响主分离结论。


# The (non-)universality of prominence and Intonation Phrases: German and Hungarian listeners' perception of an unfamiliar language

- 论文编号：707
- 报告人：Farhat Jabeen
- 程序：Tuesday 29 September 2026 / Prominence, Stress and Focus
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/jabeen26_interspeech.pdf

## 问题
现有研究常用“母语者 vs. 陌生语言听者”或“同一听者群体标注陌生语言”来论证 IP 边界声学线索具有普遍性，但作者认为这可能只是听者把 L1 线索套用到陌生语言上。本文要检验：当把同一套乌尔都语（Urdu）刺激呈现给类型学差异较大的德语与匈牙利语听者时，突显（prominence）与 Intonation Phrase（IP）边界感知是否仍表现为跨语言一致。

## 方法
材料为 4 段乌尔都语朗读（2 男 2 女各一段，约 18 秒、5–8 个句法小句），拉丁字母转写并去掉标点。26 名德语听者、21 名匈牙利语听者按 Rapid Prosody Transcription（RPT）先用斜线标 IP 边界、再下划线标突显词，可反复听。用 Fleiss’ Kappa 做组内/组间一致性；用广义线性（混合）回归检验听者 L1 与刺激说话人的交互；对判定为突显的词做时间归一化 F0，并用 GAMMs 比较两组听者的 F0 轮廓（说话人均值归一化，含随机平滑与自相关校正）。

## 实验与结果
IP 边界：聚合 Kappa 为弱到中等（按说话人约 0.47–0.63），组内一致性随说话人变化；L1×说话人交互显著（χ²(3)=90.9, p<0.0001），两组内部均有说话人主效应，拒绝“IP 线索普遍且不受说话人影响”的 H3a/H1。突显：聚合一致性极低至无（约 0.16–0.28），德语听者标突显的词比例明显高于匈牙利语听者；德语组有说话人效应，匈牙利语组无。GAMM 显示突显感知、L1 与说话人有显著三阶交互；对 Female2、Male1、Male2，德语听者更倾向把上升 F0 判为突显，匈牙利语听者更倾向把下降 F0 判为突显，并存在 F0 scaling 差异。

## 结论
未受过训练的德、匈听者在陌生乌尔都语上对突显与 IP 边界的标注并不一致：突显更依赖 L1 特异的 F0 形状/标度，一致性也低于 IP；IP 识别同样受 L1 与说话人影响，不支持“IP 边界声学线索普遍”的主张。作者建议把先前高一致性结果 reinterpret 为听者沿用 L1 线索，而非线索本身普遍。局限包括德、匈在韵律层级上相关单位不同（如 pitch accent vs. AP/IP），跨语言可比性仍待进一步工作。

## 点评
这篇工作的关键不在于再测一次陌生语言 RPT，而在于用“同一刺激 + 两种类型学不同听者”做 between-group 对照，直接打穿“高一致性=普遍线索”的推理。把突显与 IP 对照，使“IP 更一致、突显更散”成为论证结构的一部分，而不是附带结果。脆弱处在于：没有乌尔都语母语基线、刺激说话人只有四人、且两组听者在韵律范畴上可能本来就不对齐，因此“非普遍”结论很强，但对“差异来自 L1 线索映射还是范畴不对齐”仍需后续拆解。


# Broad Focus Rise(-fall) Declaratives in Venetan: Investigating Typological Outliers in Italo-Romance Intonation

- 论文编号：2691
- 报告人：Elinor Payne
- 程序：Tuesday 29 September 2026 / Prominence, Stress and Focus
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/payne26_interspeech.pdf

## 问题
无标记陈述句用升调在类型学上少见；Venetan 虽有报道，但性质、分布与语音实现仍不清楚，且既往多依赖朗读或仅考察特定重音型。本文要在 gambellarese（中西部 Venetan）半自发口语中，弄清 broad focus declarative（BFD）里 rise(-fall) 的出现率、与词重音位置的关系，以及词末重音对声调对齐的影响。

## 方法
分析 8 名年长母语者（59–81 岁，日常以方言为主）半自发对话、社会语言学问卷式半结构化访谈与 map task，合计约 1 小时 22 分钟。人工筛出完整 IP 上的 BFD，排除窄焦点、延续升调与标记性强的产出；按核词重音分为 oxytonic / paroxytonic / proparoxytonic。听觉+ f0 目视先分为 FALL、RISE、RISE-FALL，再合并为 FALL vs. RISE(-FALL)，最终 269 个 token。RoI 为核音节前一音节起点到话语末；f0 转半音，用 GAMMs（含说话人/token 随机平滑）比较轮廓类型与词型（oxytonic vs. non-oxytonic）。

## 实验与结果
269 个 BFD 中 FALL 145、RISE(-FALL) 124（约 47%），与先前同类农村社区朗读语中约 50% 接近。轮廓类型与词型无显著关联（χ²(1)=0.008, p=0.929）。GAMM：轮廓类型与词型均有显著整体效应；RISE(-FALL) 整体 f0 更高、形状不同（相对时间约 0.596–1.000 差异显著）；oxytonic 相对 non-oxytonic 也有更高整体音高与不同形状。FALL 可大致看成 HLL 插值；RISE(-FALL) 核音节多为低谷后升至末音节峰，oxytonic 偏 HLH、非 oxytonic 偏 HLHL。RISE 与 RISE-FALL 的切分倾向随可用音段材料变化（oxytonic 更多纯 RISE）。

## 结论
至少在中部 Venetan 变体中，无标记陈述句存在与 FALL 并列、且明显不同于意大利语常见降调核调的 RISE(-FALL) 替代核调；选择大体正交于词重音位置，但实现受 oxytony/音段材料影响（可能涉及截断与 tonal crowding）。音系解读仍暂定（如 FALL 偏 H+L* L-L%，RISE(-FALL) 偏 L* 加 H-H%/H-L%），需更广系统与 sociolinguistic 分布研究。

## 点评
价值在于用半自发、偏单语方言的年长说话人数据，把“陈述句升调”从轶事与朗读比例推进到可量化的双核调系统证据，并与 Italian/Italo-Romance 常见 H+L* L% 形成对照。合并 RISE/RISE-FALL 是 pragmatic 的统计选择，但也意味着音系结论只能是临时的；若截断解释成立，则“两套核调”与“一套调因 crowding 表面分叉”仍需对齐测量来裁定。


# Should Robots Sound more like Machines than like Humans? User Expectations Affect the Perception of Prosody in TTS Voices

- 论文编号：3075
- 报告人：Ha Eun Shim
- 程序：Tuesday 29 September 2026 / Prominence, Stress and Focus
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/shim26_interspeech.pdf

## 问题
TTS/机器人语音设计常把自然度、情感、音色等与可懂度分开讨论；但对依赖韵律边界消歧的句法歧义句，这些“超语言学”线索可能改变理解。本文问：在机器人化身交互中，把声音做得更情感化/更单调，或更机器感/更人感，会如何影响听众对逗号所标韵律边界的感知与可懂度。

## 方法
刺激为 Direct Address 与 List 两类歧义句对（With/Without Comma），另有 tense/lax 元音 filler；每人听 40 句。基线用人声微调的 Matcha-TTS（Human-like Affective），再用 Praat 降 pitch 变异 40% 得 Monotonic，用 Delay 0.02 s + Amplitude 0.5 Pa 得 Machine-like，交叉共 4 种音色。被试间设计：160 名英语母语者（Prolific，19–30 岁）各听一种音色，与机器人化身做图片匹配“训练”任务（判断语音是否匹配目标图），再填 MOS-X2/Godspeed 类问卷。主要分析为混合效应逻辑回归（Picture Match × Voice Condition × Comma）及问卷累积链接模型。

## 实验与结果
训练任务：Picture Match、Comma 及二者交互均极显著；三维交互显著（χ²=9.93, p=.019）。整体上 Without Comma 更易判对（听众常听不出边界）；对比显示 Machine-like 相对 Human-like 在 With Comma 条件下准确率更高（β=−0.51, z=−2.29, p=.022），congruency 对比也有较小效应。Affective vs. Monotonic 对可懂度无实质影响。问卷：Voice Condition 主效应/与题项交互均不显著；事后看 Affective 更自然（p<.01），Human-like 略更“聪明”（p=.064）。

## 结论
对 TTS 句法歧义句，韵律边界本身很难被听出；单纯改变 pitch 情感幅度几乎不改善消歧可懂度，但使音色更机器感反而提高 With Comma 条件下的理解——作者认为这改变了用户对机器人语音能力的期望，从而偏置或促使听众去听那些本难察觉的边界。局限包括被试间设计无法直接比较音色、听努力等机制尚未测量。

## 点评
这篇把 HCI 里常见的“更自然人声更好”直觉反过来：与边界无关的 indexical 音色操纵，通过期望通道影响了本该由韵律决定的消歧。实验设计干净（同一 Matcha 输出上做正交操纵），也因此把效应锚定在期望而非额外韵律线索上。脆弱点在于机制仍是事后解释（期望 vs. 更仔细听），且 Without Comma 接近天花板，Machine-like 优势主要体现在 With Comma 一侧。

