# Voice Quality Aspects of Speech

- 日期：Tuesday 29 September 2026
- 时间：09:00-11:00
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

本口头场从嗓音质量（voice quality）与发声类型切入音系与社会语音问题：极端高调是紧模态还是假声、f0 压缩时发声线索能否支撑调类区分、英语塞音后气声、声门/超声门设置的声学相关及其说话人特异性，以及吱嘎声在英汉中的性别分布。方法上以多维声学度量、多基频跟踪器稳健性检验与语料库混合效应建模为主。

核心瓶颈是：f0 不可靠或空间压缩时，仅靠基频难以分离调类或音质范畴；同时把群体平均声学相关当作“客观”嗓音设置指标，可能掩盖显著的说话人×音质交互。若干摘要明确挑战传统描写（假声标签、年轻女性吱嘎刻板印象）或提醒处理吸气后过渡对英语清浊对立刻画的影响。

跨语言与小语种证据并置：湘语开慧、晋语获济、澳大利亚英语、Nakanamanga，以及英汉对比吱嘎，显示发声类型既可能是 F0 相关生理副产品，也可能是对比维持或语种描写修正的关键线索。

## 论文技术总结

# Tense Voice, Not Falsetto: An F0-specific Physiological Byproduct of Extreme High-Pitch Tone in Kaihui Xiang

- 论文编号：693
- 报告人：Yi Zhang
- 程序：Tuesday 29 September 2026 / Voice Quality Aspects of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26i_interspeech.pdf

## 问题
湘语极高调 T4 传统听感常被记为假声，但有限声学证据暗示紧模态嗓音。需厘清其为假声还是紧模态，以及音质调整是 F0 生理副产品还是调类固有特征。

## 方法
16 名开慧湘语母语者（9 女 7 男，均>40 岁）在载句中朗读 104 个单音节词、覆盖六调与多样 CV/V 环境；排除噪声/普通话干扰后分析。VoiceSauce 在九等分时间点提取 F0、H1*–H2* 等共振峰校正谱倾斜、HNR、CPP；说话人内 z 分数化。用 GAMM（mgcv）以 T4 为参照建模 Tone 与时间平滑及说话人/音节随机平滑。

## 实验与结果
T4 为最高 F0 登记；H1*–H2* 等显著低于多数其他调，呈更平的低频谱倾斜，符合紧模态而非假声的陡倾斜+湍流。T6 在多指标上与 T4 接近或在 F0 汇合处不可区分；HNR/CPP 未显示 T4 特殊噪声极端。结论：紧张为极端 F0 的生理副产品（F0-specific），非独立调类特征。

## 结论
开慧湘语 T4 为紧模态而非假声；听感“假声”可能来自极端纵向紧张与假声“薄”音色的感知重叠。局限：主要为声学证据、老年样本、句中载句环境。

## 点评
用全调库对照与多维嗓音参数系统反驳传统听感分类，并区分 F0-specific vs tone-specific，理论贡献清晰。高龄样本与正式诱发中的普通话干扰限制外推；高频倾斜动态复杂，提示后续需连续语流与感知验证。


# The role of phonation type in Chinese Jin tones: a study using acoustic metrics

- 论文编号：1368
- 报告人：Xiaojing Du
- 程序：Tuesday 29 September 2026 / Voice Quality Aspects of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/du26b_interspeech.pdf

## 问题
获嘉（晋语汉新片）声调汇聚使 T1 与历史入声 T5 的 F0 空间压缩；T5 韵母末常有声门紧缩与不规则激励，晚期 F0 弱且依赖跟踪器。问：在 F0 不可靠时 T1–T5 对立是否仍可由发声相关线索支撑。

## 方法
17 名母语者，70 个单音节词×5 调×5 遍共 5950 token。TBU 手工切分。在统一低 F0 设置下比较 Praat 自相关、YIN、REAPER 三套时域跟踪器。VoiceSauce 提 HNR05 与 H1*–H2*。MDS 分别用仅 F0、F0+时长、再加 HNR05、再加 H1*–H2* 可视化调空间；多线索模型固定用 Praat F0。

## 实验与结果
三跟踪器 F0-only MDS 拓扑大体一致：T5 始终最靠近 T1，分离度 Praat < YIN/REAPER，分歧集中韵尾。加时长改善有限；加 HNR05 与 H1*–H2* 显著拉开 T5 与 T1，分散指数 μx 由约 2.02 升至约 6.94 再到约 8.12。

## 结论
入声韵尾不规则使单靠 F0 证据弱；发声敏感量在周期性退化处补充区分，支持获嘉入声的多线索而非纯 F0 账户。尚无感知实验与“真”韵尾 F0 金标准。

## 点评
方法上把跟踪器选择本身当作诊断对象，对入声/非模态研究很有启发。MDS 展示的是声学空间扩展而非感知可辨性；下一步需操纵 F0 与发声的感知实验。


# An investigation of post-stop breathiness in Australian English

- 论文编号：1555
- 报告人：Thomas Powell-Davies
- 程序：Tuesday 29 September 2026 / Voice Quality Aspects of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/powelldavies26_interspeech.pdf

## 问题
英语词首塞音对立常被简化为短/长滞后 VOT，但释放段可含送气后的气声过渡（类似孟加拉语等报道）。澳大利亚英语中该现象缺乏系统描写，影响对立如何计量与社会语言学解读。

## 方法
Talking About Tasmania 词表：37 人、/p t k/ 在 /æ/ 前的 9 词×5 遍，载句 elicitation；排除后 1638 token。在 Praat 中除总 VOT 外另标无周期送气（aspiration）与≥两周期的气声过渡（breathiness），再接模态元音。用 GLMM/LMM 建模气声有无与时长，固定效应含性别、年龄组、调音部位、音节数。

## 实验与结果
约 42% token 有气声相；女约 55%、男约 21%；软腭略低于双唇/齿龈。气声时长多在 8–30 ms（最长至 72 ms）。仅送气时长仍呈 p < t ≈ k；并入气声后齿龈与软腭总 VOT 均值几乎持平（约 90.8 vs 90.6 ms）。模型中性别与部位对气声出现显著，时长模型因素未达显著。

## 结论
词首清塞音后气声在塔斯马尼亚样本中高度常见且受社会/语言因素调节；是否计入 VOT 会微调部位等效应。现象似属塞音释放实现，而非说话人整体嗓音设置。

## 点评
把一维 VOT 拆成送气+气声，方法可复用到其他英语变体。样本限词表与 /æ/ 环境；自发语中的普遍性尚待验证，但对社会语音学计量口径有直接提醒。


# Acoustic correlates of voice quality settings: variation within and between individual speakers

- 论文编号：2053
- 报告人：Alice Paver
- 程序：Tuesday 29 September 2026 / Voice Quality Aspects of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/paver26_interspeech.pdf

## 问题
感知嗓音质量评估常被指主观，声学量常被当作“客观”构音设置相关物；多数研究跨说话人汇总，可能把人际差异误当设置效应，且上声道设置相关物不足。司法语音更需说话人内变异证据。

## 方法
PASR 英式男语音学家 4 人，朗读 Rainbow passage，六种伪装：default、breathy、fronted tongue body、nasal、denasal、lowered larynx；三会话×三重复。MFA 对齐后 VoiceSauce 提 CPP、多谱倾斜、多带宽 HNR 与长时共振峰 F1–F4。LME 含 setting × measure × speaker 三阶交互；以 default 为基线做估计边际均值对比。全文末尾略有截断。

## 实验与结果
群体：气声与鼻音谱倾斜升高；气声噪声量（CPP/HNR）降低；气声抬高 F1–F4，鼻音抬高 F2–F4 等。但 measure×quality×speaker 显著：除气声谱倾斜与 F2–F4 几乎人人一致外，多数效应仅部分说话人显著，甚至由单人驱动；denasal 群体效应在个体上无一显著。前舌体等预期共振峰模式也常仅个别说话人出现。

## 结论
声学相关物多为相对各人基线的说话人依存调整，非跨人不变移位；司法与理论解读须多维、相对说话人，不能依赖孤立变量绝对阈值。

## 点评
直接挑战“声学=客观构音标签”的默认假设，对司法比较尤其重要。样本仅 4 名男语音学家、故意伪装，外推自然语与女性受限；气声伴随 LTF 上升也可能含测量伪迹或协同构音，正文已讨论。


# Phonetic evidence for contrastive voicing in Nakanamanga coronal plosives

- 论文编号：2832
- 报告人：Shubo Li
- 程序：Tuesday 29 September 2026 / Voice Quality Aspects of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26ha_interspeech.pdf

## 问题
Nakanamanga（瓦努阿图中部大洋洲语）齿龈/冠状塞音是一音位还是两音位长期争议，影响历史构拟。近年音系分析主张 Tongoa 变体有清齿 /t̪/ 与浊前鼻化后齿龈 /ⁿd/，但缺声学证据。

## 方法
8 名 Tongoa 母语者；12 个词中 CV.CV 词表，目标为第二音节首 /t̪/ 或 /ⁿd/，图画诱发、载句朗读各 5 遍。Praat 手工标 VOT、闭塞时长及 /ⁿd/ 鼻/口音闭塞（以强度降中点分界）。排除噪声后 443 token；LME 固定效应含 Phoneme、音节数、前元音长短，随机截距说话人与词。

## 实验与结果
/t̪/ 一律清、正 VOT 均值 29 ms、闭塞 80 ms；/ⁿd/ 一律浊前鼻化、负 VOT 均值 −98 ms、闭塞 98 ms；鼻:口闭塞比 1.88（鼻约 65%）。Phoneme 对 VOT/闭塞效应稳健跨说话人与词项。

## 结论
声学支持 /t̪/–/ⁿd/ 对立且 /ⁿd/ 确为前鼻化；类型上属 true voicing + 前鼻化。对中部瓦努阿图接触与历史构拟有启示；Nguna 变体与气流测量待后续。

## 点评
把争议音系主张落到可重复的 VOT/闭塞证据，贡献扎实。词中位置与词表受限；鼻口比低于文献气流法报道，可能因强度切分口径，文中已说明。


# A Corpus-Based Study of Creaky Voice Production in English and Mandarin

- 论文编号：3235
- 报告人：Charles Chang
- 程序：Tuesday 29 September 2026 / Voice Quality Aspects of Speech
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26ja_interspeech.pdf

## 问题
吱嘎音在英语社会语音学中常被与年轻女性绑定，但产出证据混杂；跨语言对照少且方法不一。需在可比语料与统一声学指标下比较普通话与美式英语朗读中的性别差异。

## 方法
平行朗读语料：66 名大陆普通话者（34F）与 61 名美式英语单语者（28F），各读 5 句中性内容、可比长度与结构。MFA 对齐后取元音中央 70% 的 F0、H1–H2c、HNR35、CPP（VoiceSauce）；排除极短长与中段不可跟踪 F0 的 token，最终普通话 3002、英语 2872。LME：Language、Gender、交互 + VowelHeight，随机 Talker/Word。

## 实验与结果
F0：女性显著更高，无语言主效应/交互。H1–H2c：男性更低（更吱嘎），英语整体低于普通话，无交互。HNR35：男性更低；交互显著，性别差普通话更大（主要因普通话男性更低）。CPP：无显著性别/语言效应。总体支持两语中男性更吱嘎。

## 结论
产出上男性吱嘎于女性，与“主要是年轻女性特征”的流行印象及部分感知文献相悖，而与近期加拿大英–法语料一致；普通话性别差甚至更大，或与男性吱嘎负面评价并存。局限含英语远程设备不一、排除不可跟踪 F0（可能低估吱嘎）、仅朗读。

## 点评
方法对齐的跨语种语料是核心贡献，直接挑战英语吱嘎的性别刻板印象。感知–产出错位与普通话男性评价需分开讨论；设备与朗读风格限制跨语言绝对水平比较，作者对 within-gender 语言差已保持谨慎。

