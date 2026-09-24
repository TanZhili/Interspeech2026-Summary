# Speech, Voice and Language Disorders

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：13
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场连接口吃感知、不流畅 ASR、嗓音障碍的日常监测，以及构音障碍识别与韵律异常检测。感知实验显示普通话口吃者在 VOT 范畴边界形成与通达上呈非典型，而非范畴感知本身受损；ASR 侧则用持续学习与显式不流畅标记缓解“模型学会省略不流畅”的信息损失。

嗓音临床走向生态化：无线加速度计+麦克风估计日常发声效率（EVE），以及环境噪声与嗓音声学同步建模 Lombard 效应，区分创伤性/非创伤性发声过度亚型。构音障碍方面，PPG 音素编辑增强病理性误读模式；基于转写锚定与 LLM 的流水线自动检测不当停顿并给出时间对齐与理由。

## 论文技术总结

# Voice Onset Time Categorical Perception in Mandarin-Speaking People Who Stutter: A Zoom-In Nonword Study

- 论文编号：2907
- 报告人：Yusuke Kiyama
- 程序：Wednesday 30 September 2026 / Speech, Voice and Language Disorders
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/kiyama26_interspeech.pdf

## 问题
口吃者（PWS）在产出上已有非典型 VOT，但感知侧的范畴感知结论不一致；既往多用真词、粗粒度连续统，可能混入词汇加工，且少同时做辨认与辨别。

## 方法
22 名普通话 PWS 与 18 名流利对照（PWNS），用非词软腭塞音 /ko55/–/kho55/ 的 VOT 连续统。先用 11 步连续统在 20 名母语者上定界，再 zoom-in 到 31 步中边界附近 10 个刺激。任务含字母决策、辨认（80 试次）与 AX 辨别（4/5/6 步距，120 试次）。用 probit 得边界位置与宽度，LME 分析 RT 与 d′，并在 PWS 内探索 %SS 与各指标关系。

## 实验与结果
字母决策 RT 组间无差，PWNS 准确率更高。辨认：PWS 边界更偏 /kh/（M=8.64 vs 7.43，趋势 p=.060），边界宽度无显著差；PWNS 在 between 条件 RT 显著长于 within，PWS 该不对称减弱（Group×Category，p=.004）。辨别：组间 d′ 与 RT 无显著差；更严重口吃与 within 条件更快 RT 相关，IES 显示未以准确率换速度。

## 结论
纯音位层面范畴感知能力未见组间受损，但声学–音位映射与实时通达非典型；严重程度相关的 within 加工加速可能反映右半球代偿。局限为样本偏小，未来需更大样本、更多语音特征与 EEG 等神经指标。

## 点评
非词 + zoom-in 设计把问题从「词汇加工混杂」收窄到音位通达效率，RT 不对称比边界宽度更能说明「通达」而非「锐度」差异。解释依赖 STG/右半球文献，正文未直接测神经，SEVERE 组相关宜作探索性；与真词研究的差异提示刺激词汇地位是既往分歧的重要来源。


# Learning to Hear Hesitation: Continual Learning for Disfluency-Aware ASR

- 论文编号：2080
- 报告人：Henri-Leon Kordt
- 程序：Wednesday 30 September 2026 / Speech, Voice and Language Disorders
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/kordt26_interspeech.pdf

## 问题
主流 ASR 常被训练为省略不流畅，导致信息丢失与幻觉；在小规模带标注不流畅数据上直接微调易灾难性遗忘，而全量联合重训不现实。

## 方法
在 whisper-small.en 上引入四类不流畅标记（FILLER、REP、DISRUPT、PAUSE），用 EWC、ER、A-GEM、Weight Averaging（WA）做持续学习。两阶段：(1) 在 SME 上引入标记并保留 LibriSpeech；(2) 从选定检查点顺序适应 Pitt 与 Delaware。用 pWER、标记 micro/macro-F1 及 BWT/FM/FWT/IM 等 CL 指标；用可学习门控的 head-attribution 与零掩码消融分析解码器交叉注意力头。

## 实验与结果
标记引入：WA 在 SME pWER 最低（9.64%）且 LS 最好，但标记 F1≈0；FT/ER/A-GEM 标记 micro-F1 约 0.73–0.75，SME pWER 约 12%。成功发标记时，少数交叉注意力头跨方法一致；掩蔽 Top-5 FILLER 相关头可减少约 57% FILLER 发射而 pWER 变化小。顺序适应：WA A-WER 最好（18.90%），ER 标记 A-F1 最好（0.49）；PAUSE 最难，ER 优势明显。LS 保留同样 WA 最优（4.68%）。

## 结论
CL 可在不联合重训下提升不流畅 ASR 与标记保持，但最优方法取决于目标：标记引入与保留偏 ER，ASR/干净语音稳定性偏 WA；标记学习对应稳定的交叉注意机制。局限为单一骨干与单一任务顺序。

## 点评
把「发出不流畅标记」与「保干净 ASR」拆开用 CL 权衡，比单纯微调更贴近真实增量部署。注意力头消融给出机制线索：强正则/权重平均可能压住标记专用回路。PAUSE 与 REP 的方法敏感性说明不流畅类型并非同等可学，部署时需按临床目标选 CL 策略。


# Measuring Vocal Efficiency in Daily Life in Patients with Voice Disorders Using Wireless Accelerometer and Microphone Sensors

- 论文编号：3457
- 报告人：Ahmed Yousef
- 程序：Wednesday 30 September 2026 / Speech, Voice and Language Disorders
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/yousef26c_interspeech.pdf

## 问题
声带效率（VE，常简化为 SPL/Ps）多在实验室 /p/-元音任务中测，难以反映日常自然发声；需把 VE 扩展为生态指标（EVE）。

## 方法
14 名女性（7 声带小结患者，7 年龄匹配健康对照）。实验室同步麦克风 SPL、口内压估计 Ps、颈表加速计（ACC），舒适音高下计算实验室 VE，并拟合个体 ACC RMS→Ps 线性校准。随后无线颈带（ACC+内置麦）日常监测约 3 天、12 h/天；场内用校准估 Ps、麦算 SPL（不存原始音频），对非歌唱浊音帧算 EVE=SPL(dB)/Ps(dB)。以匹配对照 mean±1 SD 为个性化常模，统计分布与越界发声时间占比。

## 实验与结果
患者中位 EVE 低于对照：实验室 3.94 vs 4.83（p=0.03），日常 4.07 vs 4.68（p=0.08）。日常 SD/IQR 组间分离更强（SD 0.44 vs 1.02，r=0.91）。患者日常在常模外发声时间中位约 91.8% vs 对照 35.9%（p=0.03，r=0.81）；多数偏低。3/7 患者实验室与日常偏离方向不一致。

## 结论
初步支持 EVE 作为日常发声功能生态标记；变异性与越界时间比单纯中位更有区分力。局限为小样本，场内 ACC 位移与麦朝向可能影响估计。

## 点评
把实验室校准搬到 ACC+麦双传感日常监测，抓的是「临床快照 vs 真实行为」缺口。日常均值组差变弱而变异性/越界时间变强，说明生态指标更适合看行为约束而非单点均值。个性化常模依赖单对照，对照变异会传导到患者越界比例，解释时需谨慎。


# Mispronunciation Modeling via PPG-Based Phone Editing: A Data Augmentation Framework for Dysarthric Speech Recognition

- 论文编号：891
- 报告人：Tsai-Hsiu Ko
- 程序：Wednesday 30 September 2026 / Speech, Voice and Language Disorders
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/ko26_interspeech.pdf

## 问题
构音障碍 ASR 受数据稀缺与高度个体化误读影响；现有增强多改时长/音高/音色等全局特征，难刻画说话人特异的音素替换等细粒度发音缺陷。

## 方法
说话人依赖增强三件套：(1) 用 PPG 抽取器得到构音障碍与配对对照音素序列，规则对齐构建 40×40 语音映射矩阵 M；(2) 若对角准确率低于 α=70%，按替换概率 >β=5% 最多选两个音素，在 PPG 上交换概率分布（每句最多改一个音素）；(3) 改自 UUVC 的 PPG-to-speech（连续 PPG、去掉时长网络，源–滤波–能量+HiFi-GAN），先 VCTK 预训练再 UASpeech 微调；(4) 按音素时长比做 WSOLA 音素级变速。用增强数据微调 HuBERT Large。

## 实验与结果
UASpeech：对照+构音障碍 block 1/3 训练，block 2 测试。合成语音 MOSNet 2.55（真值 2.68），SES 0.71。相对同规模 GAN 基线 [6]，总体 WER 19.53% vs 21.88%（绝对降 2.35%）；低/极低可懂度分别降 3.69%/4.54%。消融显示映射编辑优于随机替换，风格转换与音素级变速均有贡献，三者合用最好。

## 结论
PPG 音素编辑可把个体误读模式注入典型语音，在 UASpeech 上优于 GAN 增强，尤其惠及重度构音障碍。

## 点评
用可解释映射矩阵驱动局部 PPG 编辑，比全局声学扰动更贴近「这个说话人怎么错」。插入被排除、每句只改一音素偏保守，可能低估复杂错读；强依赖配对对照与对齐质量，临床配对不足时扩展性受限。


# Modeling Lombard Effects in Voice Disorders Using Daily-Life Monitoring of Ambient Noise and Voice Acoustics

- 论文编号：2777
- 报告人：Ahmed M. Yousef
- 程序：Wednesday 30 September 2026 / Speech, Voice and Language Disorders
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/yousef26_interspeech.pdf

## 问题
Lombard 效应多在实验室噪声回放中研究；嗓音障碍患者在真实环境噪声下的多维度发声调节（含音质）了解不足，既往日常监测多只看 SPL/F0 与分箱噪声均值。

## 方法
14 名 PVH（双侧小结）、10 名 NPVH（肌紧张性发声障碍为主）、18 名健康对照，2–4 天、≥10 h/天佩戴颈表 ACC（估 SPL、F0、CPP、H1H2）与肩麦噪声剂量计（Leq，说话段剔除）。3 分钟窗汇总噪声（均值、SD）与嗓音统计，用相关与线性/二次 Ridge·Lasso/GBR 预测嗓音指标，报告 PDP 斜率。

## 实验与结果
噪声升高时 SPL、F0、CPP 升、H1H2 降；CPP 与 Leq 相关最强（r=0.36–0.53）。非线性模型最优，CPP 最大 test r²=0.32。PVH 在高噪声环境时间占比最高（>70 dBA：26.1%）。相对 NPVH，PVH 的 SPL–Leq mean 斜率更陡（0.65 vs 0.47 dB/dB），CPP–Leq mean 斜率更大（0.18 vs 0.11）；Leq SD 对 SPL 的斜率在 PVH 达 0.86。F0 对噪声均值的响应对照最大。

## 结论
日常 Lombard 呈多维、子类型特异：PVH 在 SPL/CPP 上调节更强，NPVH 相对受限；CPP 可捕捉超出 SPL/F0 的音质效应，噪声变异与均值同等重要。局限含组间年龄差异与噪声 alone 解释力有限。

## 点评
把 Leq 均值与变异同时建模，并用 CPP/H1H2 补足既往「只看响度/音高」的盲区，能区分 PVH 与 NPVH。窗口级 train/test 分割不声称说话人泛化，斜率更适合作组内解释。预测 r² 不高说明还需环境、距离等上下文特征。


# A Transcript-anchored Pipeline With Large Language Models For Detecting Inappropriate Pauses In Dysarthric Speech

- 论文编号：534
- 报告人：Insung Lee
- 程序：Wednesday 30 September 2026 / Speech, Voice and Language Disorders
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/han26_interspeech.pdf

## 问题
构音障碍朗读中的不当停顿（IP）对可懂度与临床评估重要，但依赖转写锚定的位置信息；标准 ASR 常抑制赘语，MFA 等对齐在异常发音与韩语无空格下易出 <unk>，纯 VAD 又缺语言学语境。

## 方法
四阶段流水线：(1) 在 Autumn Paragraph 上微调 Whisper 做保留赘语/重复的 verbatim 转写；(2) MFA 对齐，候选停顿与 Silero-VAD 非语音重叠时用 VAD 边界替换，写入 [PAUSE x.xxs]；(3) GPT-5 做词典适配，把 <unk> 映射回原词并插入停顿标记；(4) 另一 LLM 按 SLP 定义将停顿分为合适或三类 IP（词内、赘语后、发音纠正中）并生成理由。数据 743 句韩语朗读（HC/轻中/重度），说话人独立 8:1:1。

## 实验与结果
停顿对齐（0.2 s collar）：Whisper+MFA+VAD 总体 F1 72.8，优于多数组合；微调 VAD alone 73.7。Whisper verbatim WER 微平均 18.3。SLP 专家评估（不含重度）：WhisperMFA 的 AP/IP macro-F1 在 HC 0.64、轻中度 0.68，优于 WhisperCTC 与 wav2vec 2.0。LightGBM 消融：加入 IP 特征使构音障碍检测 macro-ACC +8.4 pp、macro-F1 +7.2 pp。

## 结论
转写锚定 + LLM 词典适配/分类可在构音障碍上做可解释 IP 检测；对齐质量对下游判断关键。重度因转写不可靠未充分验证，未来需提升抗转写错误能力。

## 点评
把 MFA 时间精度、VAD 鲁棒性与 LLM 语言学判断串起来，针对韩语词典缺口用 LLM 桥接，是实用工程路线。专家评估显示对齐 F1 与「是否恰当」感知差距更大，说明仅停顿检测不够。重度排除与罗马化边界误判暴露了转写锚定路径的脆弱点。

