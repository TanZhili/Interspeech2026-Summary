# Modeling L1 Acquisition

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：1
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场从一语习得与自发口语加工角度考察韵律、切分、象似性、语义相关与词汇竞争。语码转换研究把语言通用的宏观韵律特征用于诊断西—英语自发语料中 CSW 与单语产出差异，并强调说话人因素；婴儿导向语上的词切分计算模型则检验“编码梯度语音细节是否必然损害边界检测”，相对成人导向语给出不同结论。习得时间（AoA）建模把词象似性与音系 surprisal/熵对照，揭示儿童与成人加工的发展性分离。

自发时长与句子语境下的词汇竞争进一步把语义/预测性推到前台：语义相关对词时长呈显著非线性效应；跨通道启动实验显示，孤立词中次音素模糊度对竞争的梯度调制在句子语境中被语境可预测性覆盖。儿童捲舌咝音部位偏移则用高频能量等摩擦噪声特征服务早期构音诊断。整体上，本场连接计算切分、信息论与心理语言学实验，突出语境与说话人变异相对纯音段表征的主导作用。

## 论文技术总结

# The Sound of Code-Switching: Prosodic Profiles of Spontaneous Spanish-English Speech

- 论文编号：249
- 报告人：Debasmita Bhattacharya
- 程序：Tuesday 29 September 2026 / Modeling L1 Acquisition
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bhattacharya26_interspeech.pdf

## 问题
语码转换（CSW）的韵律相对单语产出了解不足；既往多基于朗读、少说话人或窄特征，结论矛盾（无差异 / 混合 / 根本不同）。需在大规模自发对话上检验 CSW 是否系统不同于英/西单语，以及熟练度与多语属性如何调节。

## 方法
Bangor Miami 语料（35 小时、约 46900 句、~2400 CSW）。提取语言无关音高、能量、时长等特征做分布比较（含 Cohen’s d）；用 k-means（k=2）检验可否仅凭韵律分离 CSW 与单语；再按学校媒介、经验年数等熟练度元数据分组，比较组间韵律差异及 CSW 是否更接近高熟练语的单语韵律。

## 实验与结果
大量特征上 CSW 与英/西单语显著不同（效应多为小–中等）。k-means 区分 CSW vs 合并单语准确率约 0.843，vs 英/西约 0.837/0.868（相对英西互分基线 0.636 显著更好）。熟练度因素更强塑造单语组间差异（常 >70–80% 特征显著），CSW 内部仅经验年数等少数因素影响过半特征；CSW 韵律更接近说话人高熟练语（以学校媒介界定）的单语模式。说话人因素总体强于多语句法属性。

## 结论
自发西–英 CSW 在宏观韵律上可与单语区分，且更多由说话人熟练度侧因素驱动；对自然多语合成有启示。

## 点评
把 CSW 韵律从“个案感知线索”推到语料级、可聚类的宏观画像，设计清楚。效应量不大说明差异可测但未必感知巨大；熟练度靠自报/学校媒介代理，因果仍受限于相关设计。


# Gradient phonetic detail is less detrimental to word segmentation in infant-directed speech

- 论文编号：2920
- 报告人：Gabriel Scharff
- 程序：Tuesday 29 September 2026 / Modeling L1 Acquisition
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/scharff26_interspeech.pdf

## 问题
词切分模型常把输入理想化为词典音位串；成人向语（ADS）上纳入发音变异会使多种算法 F 分数平均下降约 0.12。婴儿向语（IDS）结构更短、孤立词更多，语音细节是否同样损害切分尚不清楚。

## 方法
在带辅音（非元音）发音变异标注的 IDS 语料上，对比音位转录 vs 语音细节转录，评测四种无监督切分算法（含 TP、DiBS、PUDDLE、AG 等）。另用 1/10 语料模拟较少语言经验。报告 token F-score。

## 实验与结果
全语料：TP 几乎无降（音位 0.30 → 语音 0.32）；DiBS 中等下降（0.41→0.34）；PUDDLE 近持平（0.40→0.39）；AG 中等下降（0.58→0.52）。1/10 语料上部分算法降幅略大（AG 降 0.08）。整体低于 ADS 文献平均降 0.12 的程度；机会基线约 0.09–0.10。

## 结论
IDS 上编码语音细节对词切分的损害弱于先前 ADS 报告，部分算法甚至无降；提示在 IDS 中找词可能比假设的更耐受语音变异。

## 点评
直接对接 Beech & Swingley 的 ADS 结果，控制“有无细节”这一变量，对习得输入理想化很有针对性。IDS 只标辅音变异、语料与算法集不完全对齐 ADS，跨研究比较仍有口径差；“更稳健”是相对结论而非绝对容易切分。


# Word Iconicity and Phonological Surprisal as Predictors of Age of Acquisition

- 论文编号：1551
- 报告人：Alexander Kilpatrick
- 程序：Tuesday 29 September 2026 / Modeling L1 Acquisition
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kilpatrick26_interspeech.pdf

## 问题
象似词跨语言更早习得，但儿童实验显示音系非典型形式更难学；成人加工却偏好高 surprisal/非典型形式。象似性与音系不可预期性对 AoA 与成人加工的相对贡献是否分离，尚缺大规模检验。

## 方法
英语大词表：众包象似性、多源 AoA、以及音位 surprisal/entropy（首/末/最大/平均等）。XGBoost 比较各预测子对 AoA 与成人记忆/语义/词汇判断任务的重要性；线性回归与滑动窗口/四分位模型考察象似性效应随 AoA 的变化，并与平均 surprisal 交互。

## 实验与结果
AoA 主要由频率、具体性、音长主导；surprisal/entropy 对 AoA 贡献弱，却对成人加工任务更重要。回归中象似性显著预测更早 AoA（b=−0.442, t=−17.14, p<.001）；平均 surprisal 对 AoA 为正但相对较弱/不一致。滑动窗显示象似性效应在早期习得更强。

## 结论
发展解离：形式–意义透明性支架早期词汇学习，而音系不可预期性更支持成人加工效率。

## 点评
用同一信息论工具同时对 AoA 与成人加工建模，清晰拆开“象似早学”与“surprisal 利成人”的表面矛盾。AoA 与象似性均为常模/众包估计，因果方向仍可争辩；跨语言推广需谨慎。


# Non-linear Effects of Semantic Relevance on Word Duration in Spontaneous Speech

- 论文编号：1062
- 报告人：Kun Sun
- 程序：Tuesday 29 September 2026 / Modeling L1 Acquisition
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sun26c_interspeech.pdf

## 问题
自发语音词长受频率、长度、语速与 n-gram 可预测性影响已充分，但语义语境多被浅层代理且常线性建模；语义相关（semantic relevance）已在阅读/EEG 中验证，是否及如何非线性影响产出时长未知。

## 方法
Buckeye 会话语料词级时长；用分布嵌入与近因加权相似度计算目标词对局部语境的 semantic relevance。GAMM 建模，控制词长、对数频率、短语语速、音系删音等，说话人随机效应；比较含/不含 relevance 的模型 AIC，并探索与频率的交互。

## 实验与结果
含 semantic relevance 的模型 AIC 最优；去掉它 ∆AIC≈23.2。smooth 项高度显著（p<.001）。非线性：中低相关度上升伴随时长缩短（促进），高相关度区反而拉长；探索分析显示对低频词尤其明显（语境中心词竞争/强调可能）。

## 结论
Semantic relevance 独立于频率/长度预测产出时长，且呈促进–抑制转折的非线性；提示产出与理解的语境机制不同。

## 点评
把理解侧语义拟合指标迁到产出计时并用 GAMM 抓拐点，方法匹配理论（促进 vs 竞争）。相关度依赖嵌入与窗口设定；“高频/低频依赖”偏探索，需预注册复现。


# From Words to Sentences: Contextual Predictability Overrides Phonetic Ambiguity in Lexical Competition

- 论文编号：3106
- 报告人：Will Chih-Chao Chang
- 程序：Tuesday 29 September 2026 / Modeling L1 Acquisition
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chang26g_interspeech.pdf

## 问题
孤立词识别中亚音位细节（如 VOT）梯度调节词汇竞争；句子语境可预测时，该调节是否仍存在，对区分 TRACE（锐化底层）与预测编码/贝叶斯（压制或降权底层）至关重要，既往证据未正交操纵两者。

## 方法
TTS 生成刺激后人工拼接同一套 VOT 连续体 token（No/Some/Max 模糊）。跨通道启动：听音启动 → 视觉探测词汇判断；identity advantage（Identical 快于 Competitor）作竞争消解指标。实验1（N≈58）：孤立词。实验2（N≈60）：嵌入高/低可预测句，并用 GPT-2 差分 surprisal 作连续预测性。

## 实验与结果
实验1：显著 identity advantage，且随 VOT 模糊线性/二次交互缩小，Max 模糊时优势消失。实验2：强 identity advantage，且高可预测语境更大（β=0.022, p<.05；连续 surprisal 亦显著）；但 VOT 与 identity advantage 的交互不再显著（线性/二次及三路均 n.s.）。

## 结论
句子可预测性可覆盖亚音位模糊对词汇竞争的调节，支持预测编码/贝叶斯降权底层证据的观点；孤立词模型未必直接推广到句子理解。

## 点评
正交设计干净，理论分叉明确。刺激为 TTS+拼接，生态效度有限；实验2无 VOT 效应也可能部分来自任务/功率，但与预测性主交互并存，整体仍支持“语境改写竞争动力学”。


# Informativity of high-frequency bands on the place of articulation shift in retroflex sibilants produced by children

- 论文编号：2606
- 报告人：Oliwia Skórzewska
- 程序：Tuesday 29 September 2026 / Modeling L1 Acquisition
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/skorzewska26_interspeech.pdf

## 问题
波兰儿童舌尖后擦音/塞擦音易出现部位偏移（sigmatism）；标准分析常低通截止，可能丢掉儿童前腔更短带来的高频诊断线索。需量化至 16 kHz 的噪声能量对部位分类的信息量。

## 方法
PAVSig 库：约 186 名 4–8 岁儿童，分析 /ʂ ʐ tʂ/（文中 IPA）在 retroflex（规范）、dental、postalveolar、interdental 四类部位。帧级提取 28 个 500 Hz 带宽 Noise Energy（至 16 kHz）、摩擦共振峰积分能量 FNE 及其比值 FNER 等共 34 特征；线性混合模型估计部位效应与边际 R²。

## 实验与结果
Dental 实现几乎全频带显著偏离规范，FNER(12,23) 对塞擦音可解释约 29% 部位方差。Interdental 在 8.5–10 kHz（NE13–15）等有特异高频偏离。FNER 相对单带 NE 更稳定且跨清浊更可比。高频至 16 kHz 携带诊断相关信息。

## 结论
扩展高频噪声能量与比值特征可更好刻画儿童卷舌咝音部位偏移，有助于辅助构音障碍评估；新特征提供相对不依赖浊音的度量。

## 点评
针对儿科录音常被“砍频”的实践痛点，用 LME+边际 R² 把频带信息量说清楚。类别极不均衡（interdental 仅 8 人）限制功效；临床落地还需与听感评判/分类器闭环验证。

