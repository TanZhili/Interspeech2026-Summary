# Speech Production and Perception 1

- 日期：Tuesday 29 September 2026
- 时间：16:30-18:30
- 形式：Poster
- Area：1
- 论文数：10

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场连接语音产生物理建模、自声感知与质量/相似度的人机对齐，并延伸到 EEG 注意切换解码与唇读转语音。产生侧关注一维噪声尺度因子相对三维湍流仿真的适用边界、声带接触/脱接触的更渐进几何建模，以及颈皮振动对耳周麦克风拾音的影响。

感知与评测侧用交互式滑杆逼近自然自声、大规模实验拆解“讨厌自己录音”的回放—意象差距，并检验 MOS 预测与说话人嵌入距离是否对齐人类。神经与视觉接口则提出状态引导的注意切换解码框架，以及用文本—视频对齐把冻结 TTS 改造为唇同步语音生成器；SSL 模型的跨语言发音编码则用芬兰语—俄语 EMA 探测。

趋势是：物理与感知约束进入合成与评测；“像人一样听/像自己一样听”成为模型对齐目标；多模态与脑机接口继续服务可穿戴听力与无声语音应用。

## 论文技术总结

# SELFIX: An Interactive System for Natural Self-Voice Approximation

- 论文编号：1395
- 报告人：Pavo Orepic
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/orepic26_interspeech.pdf

## 问题
录音自我声音因缺骨导滤波而显「不像自己」；既往多频段均衡搜索空间过大、维度不感知对齐，难收敛到普适滤波器。

## 方法
SELFIX：交互界面用感知动机的低维滑杆（音高 F0、声道长度 VTL、低频倾斜、梯形滤波器等，经 PSOLA 等变换），随机化无标签初始位置。被试反复调到「像自然说话自己」并评匹配度与信心（0–100）。初步研究 N=25（13 男/12 女）。

## 实验与结果
被试调整一致且匹配/信心评分高，支持界面效度。全体倾向增强低频（约 <600 Hz）；男性额外降低音高、增长声道长度。PCA 与性别×滑杆交互显示自我声音近似超出单纯频谱均衡。

## 结论
结构化感知参数可为可扩展个性化自我声音建模提供声学基础。

## 点评
把无引导 EQ 搜索换成说话人身份相关的少数维度，实验设计干净。强在性别差异发现；脆弱点在四参数未必覆盖个体差异全貌，且实验室朗读材料与日常自我暴露条件不同。


# Noise Scaling Factor for the One-Dimensional Voice Production Model

- 论文编号：559
- 报告人：Tsukasa Yoshinaga
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/yoshinaga26_interspeech.pdf

## 问题
气声等嗓音含声门湍流噪声；1D 声学模型常用 Fant 型噪声公式及任意缩放因子，该因子相对显式湍流的 3D 流声仿真是否普适，少有系统检验。

## 方法
对元音 /a/、/u/ 做 3D 可压 Navier–Stokes 流声仿真（正常与不完全闭合气声），与嵌入 Fant 噪声项的 1D 模型对比频谱；扫描缩放因子使谱差最小，考察常规值何时成立。

## 实验与结果
/a/ 正常发声、声门可完全闭合时，传统缩放因子与 3D 吻合较好。气声（声门不完全闭合）及 /u/ 存在声门上收缩时，最优缩放偏离常规值；谱差随因子变化有明确谷值。结论：湍流噪声建模需随声道流场构型调整。

## 结论
1D 噪声缩放并非全局常数；应按声门闭合与声门上几何调节，以兼顾精度与远低于 3D CFD 的计算成本。

## 点评
用 3D 真值标定 1D 经验参数，对气声病理与合成功用直接。强在正常 vs 气声、/a/ vs /u/ 对照；脆弱点在仅两元音与有限构型，外推到动态协同发音需更多验证。


# Improved modeling of vocal fold contacting and de-contacting in a geometric vocal fold model

- 论文编号：753
- 报告人：Tianyi Zhang
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26j_interspeech.pdf

## 问题
几何声带模型常把接触简化为正弦位移在中线截断，忽略部分接触阶段组织形变减速与分离时粘着力导致的初速降低，损害合成自然度。

## 方法
在 Titze 型几何模型上引入生物力学启发的渐进接触/去接触，并保留/改进声门面积脉冲左右偏斜机制；接入发音器官合成器。与无软接触的 2019 参考模型做 A/B 偏好与五分制 MOS（多组预发声参数、合成句）。

## 实验与结果
新模型在 A/B 中获 58.1% 偏好（95% CI [56.0%, 60.2%]）；MOS 均值 3.02 vs 旧模型 2.68。混合效应模型确认 NEW 主效应提升自然度。

## 结论
更真实的接触/去接触动力学可改善几何声源的感知自然度，利于低资源可控发音合成。

## 点评
针对声源周期中「短但关键」的碰撞阶段做机制修补，并用听感实验闭环验证。强在相对 2019 模型的对照清晰；脆弱点在整体 MOS 仍中等，自然度瓶颈可能还在声道/韵律等其它模块。


# The Effect of Neck Skin Vibration on the Periauricular Acoustic Receiver

- 论文编号：170
- 报告人：Ruoyan Li
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/li26b_interspeech.pdf

## 问题
自语时除口腔辐射外，颈部皮肤振动会再辐射空气声，可能污染耳周麦克风；许多自语仿真只建模口鼻辐射，忽略该路径。

## 方法
三路证据：(1) KEMAR 口模拟器扫频，耳周/额/口前麦克风同步；(2) 真人朗读，耳周麦克风 + 颈振传感；(3) 头几何 BEM（GPU 加速，球模验证）仿真。对比有无颈振耦合下耳周拾音差异。

## 实验与结果
摘要与结论导向：靠近颈部的耳周接收器测到与颈皮振动相关的显著空气声分量；假头–BEM 与真人–仿真对照支持该耦合。含义是自语声学模型需把颈振辐射纳入，而非仅口腔源。

## 结论
耳周器件设计与自他语音分离应考虑颈振空气声路径。

## 点评
把可穿戴耳周场景下的「被忽略声源」钉死，对助听器/耳机自语处理有工程意义。强在假头、真人、BEM 三角互证；脆弱点在被试少（正文写 S1–S2）与稳态朗读材料，动态语速/音高变化下耦合强度待扩展。


# Investigating Human-Model Discrepancies in Speech Quality Assessment via Acoustic and Prosodic Perturbations

- 论文编号：1478
- 报告人：Reo Shimizu
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/takagi26_interspeech.pdf

## 问题
MOS 预测模型常替代听测，但能否捕捉声学保真之外的韵律、口音与说话人特征差异仍不清楚；日语音高口音错误可改词义，尤其需要检验。

## 方法
对语音施加受控扰动并对比人类 MOS 与模型预测：Group A 声学退化（如低码率 MP3）；Group B 用可控音高口音 TTS 故意翻转口音；Group C 操纵平均 F0、F0 变化与语速（自然说话人差异 + 转换）。检验三假设 H1–H3。

## 实验与结果
多数模型能跟随声学退化（支持 H1）；对韵律/口音错误普遍不敏感，尽管主观分大幅下降（支持 H2）；说话人特征上呈双重分离——模型有人类没有的强平均 F0 偏置，却对人类敏感的语速与 F0 变异不敏感（支持 H3）。凸显标量 MOS 预测在声学保真之外的局限。

## 结论
自动 MOS 不宜单独代表「自然度」全维度；韵律与说话人特征需单独评测或改进表征。

## 点评
用正交扰动把「模型听什么」拆开，比相关分析更有因果清晰度。强在日语音高口音设定；脆弱点在扰动未必覆盖全部质量维度，且模型族若未在正文详列完整表时外推需克制。


# Do speech foundation models perceive speaker similarity as humans do?

- 论文编号：1172
- 报告人：Hayato Yagi
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/kishi26_interspeech.pdf

## 问题
语音基础模型嵌入可用于说话人验证，但其嵌入距离是否对应人类对「像不像」的连续相似度判断，尚不清楚。

## 方法
用 40+ 模型（Whisper、WavLM、HuBERT、Parakeet、Qwen3-TTS 等）逐层提说话人嵌入，算说话人对余弦距离，与人类感知相似度图（7 分量表均值）比 Spearman 相关（SRCC）；再做多元回归，量化训练目标、规模、层深等配置对对齐的贡献。

## 实验与结果
中间层常对齐较好，相关随层深变化因模型而异；部分 TTS 模型整体对应较低。配置回归显示哪些因素更促成人感对齐。正文图示相关分布于约 0–1 区间，具体最优 SRCC 以图/表为准。结论指向更感知对齐的基础模型设计。

## 结论
嵌入几何与人类相似度部分可对齐但非普遍；层位置与训练设定是关键杠杆。

## 点评
把「会验证」推进到「像人类那样量相似度」，评测面很宽。强在模型覆盖与层析；脆弱点在人类量表噪声与语料/语言覆盖有限，对齐高不等于身份感知机制同构。


# What Makes Us Hate Our Own Voice? Large-scale experiments on Playback–Imagery Gaps and Individual–Speech Feature Effects

- 论文编号：973
- 报告人：Koki Fukuda
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/fukuda26_interspeech.pdf

## 问题
厌恶录音自己的声音常归因于骨导–气导失配，但个体差异大；想象中的自我声音与回放评价是否系统不同、受何声学与特质调节，缺大规模证据。

## 方法
日语在线被试（质控后 N=459）：朗读后按平衡顺序完成 playback 与 imagery 两块，多维印象评分。混合效应估计回放–意象差距；验证 Pred1–3（回放更负、顺序调节、特质相关）；RQ1–2 用 70/30 发现–验证分割与 FDR 探索声学描述子及特质×声学交互。

## 实验与结果
回放比意象更负面，尤其不适感更高（discomfort β=0.490，报告含 95% CI）；自我像似度不一定同模式。差距受顺序与块结构调制。探索性分析显示听者对声学线索权重因人而异。178/637 因质控剔除。

## 结论
回放–意象差距支持自我声音厌恶的认知框架；应用上需听者自适应，并需更受控随访。

## 点评
大规模、预注册式分割与混合模型使「讨厌自己声音」从轶事变为可估计效应。强在顺序平衡与多维评分；脆弱点在在线录音质量控制与探索性交互的发现率。


# SGAD: A State-Guided Adaptive Decision Framework for Robust EEG-Based Auditory Attention Switch Decoding

- 论文编号：1815
- 报告人：Yuting Ding
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/ding26d_interspeech.pdf

## 问题
EEG 听觉注意切换解码（AASD）需在稳定与切换间兼顾准确与低延迟；固定时序平滑难两全。数据划分若未控制音频/说话人混淆会高估泛化。

## 方法
SGAD：因果状态检测推断注意转移态，再以状态引导自适应门控调节时序平滑强度；编码器先预训练再冻结，SGAD 用 L_dec+λ1 L_state+λ2 L_smooth 训练。提出六层评测协议（跨音频、说话人、被试等，含 LOSO/LOSSO）。数据 MS-AASD，男女讲者 0 dB 双耳混合，约 1 s 重叠窗。

## 实验与结果
指标：Acc、Sw-F1、切换检测延迟 SDL。摘要称 SGAD 在多协议下提升准确与稳定性并保持低延迟；不同协议表现差异提示划分相关偏差。具体数值表依正文实验段。

## 结论
状态依赖决策可打破固定平滑权衡；多协议评测对可靠 AASD 必不可少。

## 点评
同时改「怎么决策」与「怎么评」，对神经助听落地更务实。强在混淆控制意识；脆弱点在状态检测误差会传导到门控，且实验室 0 dB 双讲与真实噪声场仍有差距。


# LipAdapter: Text-to-Video Alignment is All You Need for Lip-to-Speech

- 论文编号：518
- 报告人：Souvik Ghosh
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/ghosh26b_interspeech.pdf

## 问题
端到端唇语转语音需大量数据且难泛化；在 VSR 语料上训的生成器音质弱，而直接喂原始视觉又引入噪声。如何用少量数据把冻结 SOTA TTS 改造成唇同步语音生成器。

## 方法
LipAdapter：冻结 VSR 与 TTS，经 text-to-video alignment 模块对齐音素表示与唇嵌入，使 TTS 在视觉引导下合成唇同步语音。模块化适配，训练约 30h，约为既往方法 1/15。

## 实验与结果
LRS3：LipAdapter（V+T, 30h）WER 21.2%，接近或优于用 430h 的 LipVoicer（21.4%）等；STOI-Net/DNSMOS/LSE 指标具竞争力。MultiVSR 上 WER 34.44%（vs LipVoicer 35.95%）。零样本多语（法/德/西/葡）有报告。另有人工 MOS。

## 结论
文本–视频对齐足以把强 TTS 转为唇同步合成，大幅降数据需求并具备跨语零样本潜力。

## 点评
「适配器 + 冻结大模型」路线对低资源唇语合成很实用。强在数据效率与模块复用；脆弱点在依赖上游 VSR 错误传播，以及零样本多语仍受视觉–语言覆盖限制。


# How Bilingual Are SSL Speech Models? Cross-Lingual Probing of Articulatory Encoding with Finnish and Russian EMA

- 论文编号：1324
- 报告人：Ruchi Pandey
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/pedro26_interspeech.pdf

## 问题
SSL 表征含丰富语音信息，但跨语言如何编码发音动作、对芬兰语–俄语等类型距离语对是否仍语言无关，缺少 EMA 探测证据。

## 方法
双语芬–俄说话人 EMA（舌/唇等 X/Z）；线性探测 SSL 层预测轨迹，Pearson r；约 5 分钟配对数据即可训。实验矩阵含跨模型、层、数据量、LOSO 说话人泛化、朗读 vs 自发、语言熟练度（Table 1）。

## 实验与结果
多语模型更优：如 MMS-300m、XLSR-53 (RU FT)、XLS-R (FI FT) 平均 r≈0.686–0.689（最高约 0.68）。中间层最有效；舌运动比唇更可预测；结构化任务准确更高；跨熟练度泛化强。

## 结论
SSL 含部分语言无关的发音子空间，支持跨语发音可解释性与相关语音技术应用。

## 点评
用同一双语者 EMA 控说话人，干净检验跨语发音编码。强在 LOSO 与任务类型分解；脆弱点在线性探测可能低估非线性编码，被试规模限制个体差异结论。

