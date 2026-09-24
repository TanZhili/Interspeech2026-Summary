# Behavioral, Cross-lingual, and Multimodal Speech Analysis

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：3
- 论文数：11

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场海报把行为状态（压力、情感、填充停顿）、跨语/低资源情感与语用，以及视听/多模态反讽与讽刺检测串在一起。压力检测从实验室 TSST 声学—韵律预测，扩展到医院工作者的语音+轨迹晚融合；情感侧同时追问声学相对文本的贡献（芬兰自发语）、填充停顿的大规模斯拉夫议会建模，以及微笑言语在嘈杂人群噪声下的决策偏置变化。

跨语资源建设密集：MMEE 多语多情感强调检测基准、KuralHub 暴露类型学能力边界、YUE-PUB-Speech 粤语语用多模态、TIMBRE 对 49 层×26 语料做层间跨语 SER 大图。视听与多模态则用眼动揭示普通话反讽的眼/口注意不对称，以及文本锚定正交残差校正分离讽刺中的共鸣与失调。

## 论文技术总结

# Automatic Detection of Stress from Speech in the Trier Social Stress Test

- 论文编号：671
- 报告人：Wieland R. Cremer
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/drimalla26_interspeech.pdf

## 问题
压力多用自评与唾液生物标志，难无创高频采集；需验证语音能否在被试间设计下区分 TSST 与友好对照，并预测生理/情感反应。

## 方法
50 名健康德语大学生随机分入 TSST 或 f-TSST；收集唾液皮质醇、sAA 与 PANAS。眼动眼镜麦克录音，Sortformer 说话人分离后提 MFCC、Praat 嗓音参数与 eGeMAPS（共 144 维+性别）。嵌套交叉验证训练 LR/SVM/RF/XGB 分类与 SVR/RFR/XGB 回归。

## 实验与结果
操作检验：TSST 后皮质醇与负情绪显著升高。分类最佳 XGB 准确率 0.82±0.11、RF AUC 0.85，显著优于多数类基线。SHAP 突出浊音谱流变、极低/低频能量、浊音段速率与 shimmer 变异。全样本 SVR 可优于虚基线预测皮质醇反应性；部分模型可预测 ΔNA；sAA 与 ΔPA 较难。

## 结论
声学–韵律特征可无创区分急性格社会压力情境，并部分预测皮质醇与负情绪反应。

## 点评
被试间 TSST vs f-TSST 避免先前被试内设计的顺序污染。眼动镜麦克与分离后拼接改变停顿结构，可能影响时长类线索。n=50、大学生样本限制外推；回归效应中等，不宜替代生物标志而宜作辅助监测。


# Looking for Affect in Spontaneous Finnish Speech through Linguistic Interpretability

- 论文编号：2452
- 报告人：Kalle Lahtinen
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/lahtinen26_interspeech.pdf

## 问题
效价与唤醒在自发语音中分别多大程度依赖文本 vs 声学，芬兰语既往研究多单模态，互补作用不清。

## 方法
FinnAffect 标注子集（12k 句，效价/唤醒 [-1,1]）。系统比较 127 组显式/隐式特征组合：文本侧 ModernBERT、FinnSentiment、情感词典、Trankit 语言学特征（口语/标准转写）；音频侧 ExHuBERT、eGeMAPS；可选交叉用另一维标注。MLP 回归，报告 CCC。

## 实验与结果
效价：文本+音频组合显著优于单模态，最佳测试 CCC≈0.42–0.43（含 ModernBERT+ExHuBERT+FinnSentiment±唤醒）；纯音频约 0.21，词典/语言学显式特征较弱。唤醒：声学主导，模态互补增益不大。口语 vs 标准转写差异多不显著。

## 结论
自发芬兰语中，效价感知更依赖语–音互补，唤醒主要靠声学，与跨语言既有发现一致。

## 点评
用可解释显式特征与预训练表征并排消融，比端到端黑盒更能回答「哪类线索在起作用」。训练标注多为单听者，测试为五人金标，标注噪声会压 CCC 上限；口语转写标准化用 GPT，可能引入额外偏差。


# Umm... With Transformers? Insights from Filled Pause Use across Four Slavic Parliaments

- 论文编号：3262
- 报告人：Ivan Porupski
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/porupski26_interspeech.pdf

## 问题
填充停顿（FP）研究多依赖小规模单语语料；性别、年龄、语速等效应能否在大规模议会语域推广，以及情感、政治取向、执政地位等新变量是否相关，尚不清楚。

## 方法
约 4000 小时克罗地亚/捷克/波兰/塞尔维亚议会发言（ParlaSpeech），transformer 自动检 FP；用 Mundlak 校正的 GEE 负二项模型分解说话人内/间效应，预测 FP 率，纳入性别、年龄、语速、情感、左右取向与执政/在野。

## 实验与结果
复制：年龄与语速均负向关联 FP（全局每增十年 IRR≈0.86；每音节/秒 IRR≈0.65，尤以说话人内效应强）。性别：全局女性更高 FP，但主要由 HR/RS 驱动（男性 IRR≈0.40–0.53），CZ/PL 无显著差，方向与多数会话语料「男性更多」相反。情感正向关联 FP（全局 IRR≈1.06）；在野相对执政倾向更低 FP（议会特异）。取向效应因国而异。

## 结论
大规模斯拉夫议会语料显示 FP 预测因子高度语域依赖；语速的说话人内效应支持规划负荷解释，性别与年龄模式不可简单从会话语料外推。

## 点评
Mundlak 分解把「习惯」与「当下状态」分开，是相对普通回归的关键增益。情感靠自动模型（R²≈0.65），误差会渗入 FP 关联。仅议会正式语域，对日常对话概化需谨慎。


# Eye and Mouth Cues in Audiovisual Perception of Mandarin Irony: Evidence from Eye-tracking

- 论文编号：1544
- 报告人：Shifeng Xia
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/xia26_interspeech.pdf

## 问题
反语理解依赖听视整合；韵律研究较多，面部区域（眼/口）在普通话反讽指责与反讽表扬中的作用仍不足。纯音频下反讽表扬识别很差；安静实验室条件易天花板效应，噪声是否会在“看嘴保可懂度”与“看眼取意图”之间权衡也不清楚。

## 方法
44 名普通话母语者（19–24 岁）完成眼动实验。材料 120 句，覆盖真诚表扬/反讽指责、真诚指责/反讽表扬；一位女说话人录制视听刺激，噪声条件为 8 人 babble、SNR −10 dB。三模态：Visual-only、AV-Quiet、AV-Noise。被试判断意图为表扬或批评。Eyelink 1000 Plus 记录注视；AOI 为眼、口、全脸；分析比例注视时长（arcsin）与 AOI 内平均瞳孔大小；线性混合效应模型：AOI × Attitude × Modality + (1|Participant) + (1|Sentence)。

## 实验与结果
反讽指责正确率：VO 94.70%、AV-Quiet 82.67%、AV-Noise 88.18%；三模态下眼部注视均显著长于口部。反讽表扬正确率：VO 92.42%、AV-Quiet 仅 16.62%、AV-Noise 67.58%；正确解读时 VO/AV-Noise 更看口，AV-Quiet 眼口注视差不显著，但 AV-Quiet 下看眼时瞳孔显著更大。真诚指责各模态更看眼且正确率很高；真诚表扬仅在 AV-Quiet 更看眼。错误解读的反讽表扬在 AV-Noise 更看口。

## 结论
两类反语的视觉加工不对称：反讽指责稳定依赖眼部，反讽表扬更依赖口部且在安静视听下整合成本更高（瞳孔增大）。噪声会把注意推向口部。全文 Discussion 后半与 Conclusion 在抽取中截断，作者最终边界表述不完整。

## 点评
用眼动把“意图线索（眼）vs 音段线索（口）”拆开，并对照指责/表扬两类反语，比只报正确率更能说明多模态策略差异。AV-Quiet 下反讽表扬正确率极低却仍出现眼区高认知负荷，提示正负字面义与面部线索冲突是主要难点。单说话人、实验室 SNR、以及全文后部截断，限制对跨说话人/生态效度结论的外推。


# Do Speech Emphasis Models Generalize across Languages and Emotions?

- 论文编号：2783
- 报告人：Megan Wei
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/wei26e_interspeech.pdf

## 问题
既有强调检测多在英语中性朗读/合成数据上训练，跨语言族、跨情绪唤醒与感知–合成标签的泛化能力不明。

## 方法
发布 MMEE：7 语（含变体）、34 情绪/风格、约 1 万句（14.13 h）、每句 10 人三级感知标注。基准 EmphaClass 与 WhiStress，覆盖单语、跨语、多语、跨唤醒、跨数据集与数据规模设定。

## 实验与结果
单语零样本跨语衰减明显，尤其类型距离大的语言；多语训练显著提升稳健性。高/低唤醒情绪间双向迁移稳健；感知与合成基准可相互迁移，提示共享韵律结构；较小训练规模下性能仍较稳。WhiStress 总体准确率常高于 EmphaClass；Pearson 相关显示跨语难度更大。

## 结论
强调建模需多语多情绪数据：多语训练优于单语零样本；情绪唤醒与标签来源并非主要瓶颈。

## 点评
用专业演员表达语料填补「多语+情绪+人类分级标注」空白，直接服务 TTS/翻译中的强调控制。Cohen’s κ 中等（约 0.29–0.52）反映强调主观性；专有语料可复现性依赖公开发布范围。


# KuralHub: Exposing Typological Capability Frontiers in Multilingual Speech Emotion Recognition

- 论文编号：3502
- 报告人：Jubeerathan Thevakumar
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/thavarasa26_interspeech.pdf

## 问题
SER 进展受高资源语言偏置；跨语迁移是否主要由预训练数据量决定，还是受语言结构类型约束，缺乏大规模系统证据。

## 方法
KuralHub：在 29 语、33 个公开数据集上评测 11 个冻结自监督骨干（HuBERT、Wav2Vec2、WavLM、Whisper 等变体）+ 轻量分类头，统一五类情绪设定；报告跨语与语系差异。

## 实验与结果
跨语可迁移性更受类型结构约束而非预训练数据量：对汉语、阿姆哈拉语等可较好适应，但对达罗毗荼语族（如泰米尔、卡纳达）系统失败，模型间方差很小（泰米尔均值 UAR 约 0.31）。单纯放大参数无法消除该瓶颈。

## 结论
暴露类型能力边界，呼吁类型感知预训练与公平 SER 路线图；开源基准服务低资源语言。

## 点评
把「数据多少」与「结构远近」对照，比只报平均 UAR 更有诊断价值。数据集在 elicitation、标签体系与样本量上异质，语系失败也可能混入录音/标注质量；但仍提供强信号：达罗毗荼语需专门表征策略。


# YUE-PUB-Speech: A Speech-based Pragmatic Understanding Benchmark for Cantonese

- 论文编号：289
- 报告人：Ziwei Gong
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/wen26b_interspeech.pdf

## 问题
语用理解依赖会话隐含义与韵律线索，但既有基准多为纯文本；粤语等低资源语言缺少对齐的文本–语音语用评测资源。

## 方法
基于 PUB 选取语用丰富实例，译为粤语并经人工校验，由 4 名母语者录音，得约 10.87 小时配对数据（1680 对话规模）、统一多选 QA，覆盖隐含义、预设、指称等。基准文本/音频单模态、文本–音频特征拼接（含 openSMILE）与音频语言模型。

## 实验与结果
加入语音相对纯文本提升语用理解；纯音频落后，说明需语义内容+语音线索。SFT 对粤语会话准则对齐关键约 10%（隐含义）。预设类最难；Gemini-2.5-Pro 等多模态在预设/指称上较强（指称峰值约 82.50%）；隐含义上 openSMILE 拼接有效。

## 结论
发布首个粤语多模态语用基准，表明语音信号对低资源语用推理有增益，并提供跨范式比较测试床。

## 点评
把 PUB 式语用推理带入口语粤语，填补「转写对了仍听不懂用意」评测空白。翻译–录音链路可能损失原语文化语用细微差别；多选格式便于评分但压缩真实开放推理。预设最难符合其依赖未陈述前提的本质。


# TIMBRE: Layer-Wise Cross-Lingual Speech Emotion Recognition Across 49 Layers and 26 Corpora

- 论文编号：579
- 报告人：Anatoly Marchenko
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/marchenko26_interspeech.pdf

## 问题
跨语言语音情感识别（SER）中，情感线索在何种表征深度上能跨类型学差异泛化仍不清楚。已有工作或只看末层、或只做语料内 probing、或仅覆盖少数语料，尚未把大模型每一层与大规模跨语料迁移系统结合。

## 方法
对 wav2vec2-xls-r-1b 的 49 个提取点（48 个 Transformer 层 + CNN 特征编码器）做 mean-pool 线性探测：在 26 个情感语料（23 语、14 语系）上，标签统一为 angry/happy/sad/neutral，每类最多 500 句；对每层做 26×26 跨语料 logistic regression（C=1.0，训练语料 z-score），共 31,850 次实验。另对比 27 维手工艺声学特征（扰动、F0、MFCC、频谱、共振峰、能量）与全层 mean-pool 的同协议迁移，并对 25 个语料做特征组 leave-one-out 消融。

## 实验与结果
跨语料平均 F1 在 layer 15（约 31% 深度，作者称 CRIS）达峰值 0.392，L45 跌至 0.296（相对峰值 −24.6%）。Romance 相对优势呈 U 形，tonal 相对优势随深度上升；组内/组间迁移在 L15 统计上难区分，整体迁移更受语料表达强度与诱发方式驱动。同分类器下 mean-pool wav2vec2 平均 F1 0.355，声学特征 0.252（约 +41%），声学保留约 71% 基线质量但仅在 3/26 语料上胜出。消融中 MFCC 最重要（平均 ΔF1≈−0.097）。

## 结论
作者认为 L15（或 L12–L18 平台）是冻结 mean-pool 特征做跨语言 SER 的较优提取层；类型学影响层间迁移曲线形状，而语料表达性/诱发风格比语系归属更能解释整体可迁移性。局限包括多为表演/朗读语料、Romance/tonal 样本量小、仅探测单一 SSL 模型、线性探针可能低估层容量等。

## 点评
核心贡献是把“中层情感信息”从语料内现象扩展为大规模跨语料证据，并给出可操作的层选择建议。用固定 LogReg、不调参换可比性，结论对该协议更稳健，但对微调/更强分类器未必直接外推。类型学解释与表演语料、规模共变存在混杂，正文也承认应作探索性解读。


# Hearing Smiles in the Crowd: How Babble Noise Shapes Smiled Speech Perception

- 论文编号：1178
- 报告人：Rong Li
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/li26t_interspeech.pdf

## 问题
听觉“微笑语音”研究多在干净条件下进行，而真实场景常有多说话人 babble 掩蔽。噪声是否削弱 smile-like 检测，以及在 smile-like 内部对 amused 与 spread-lip 的区分是否同等受损，尚不清楚。

## 方法
基于 AMuS 语料，选取覆盖 amused / spread-lip / neutral 的 Speaker B（法语男）与 Speaker C（英语女）；干净语音归一化至 70 dB，与 NOISEX-92 食堂 babble 混合，条件为 Quiet、−3 dB、−6 dB。任务 1：smile-like vs. neutral；任务 2：仅 smile-like 上 amused vs. spread-lip。经 Prolific 招募并通过耳机与注意力筛查后，有效样本为英语流利 38 人、法语流利 37 人。用二项 GLMM（Noise×Category、Speaker 交互，被试与刺激随机截距）分析正确率，并用 SDT（d′、准则 c、AUC）分离敏感度与反应偏向。

## 实验与结果
任务 1：相对安静与中性，spread-lip 与 amused 在 −3/−6 dB 准确率显著下降，中性相对稳定；amused 全程高于 spread-lip，且二者噪声效应近似平行。d′ 由 1.87→1.00→0.58，c 由 0.09→0.49→0.69（更保守、更少报“听到微笑”）；AUC 由 0.97→0.83→0.73。任务 2：安静时 amused 明显更准，噪声下 amused 准确率骤降而 spread-lip 上升并出现交叉；d′ 1.28→0.82→0.55，c 由 −0.51（偏 amused）翻转为 0.25/0.64；AUC 0.93→0.84→0.77。Speaker 效应主要出现在任务 1 的中性与 spread-lip。

## 结论
噪声不仅降低微笑判断的感觉证据，也促使听者在不确定下转向更保守的决策策略；任务 1 中 amused 比机械 spread-lip 更易识别，与更丰富的情感声学线索一致。局限包括仅两名说话人及语料说话人/语言/性别混杂，正文末段也提醒谨慎外推。

## 点评
工作把微笑语音感知从“能否听出来”推进到噪声下敏感度与准则如何联动变化，对无视觉的嘈杂通信与相关语音技术评测有直接含义。实验设计清晰，但说话人覆盖极窄，Speaker 差异也可能混入性别与语言，结论更适合作为机制证据而非大规模人群效应估计。


# Stress Detection Across Daily Activities: A Context-Aware Multimodal Framework with Trajectory and Ambient Speech

- 论文编号：1262
- 报告人：Wei-Heng Huang
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/huang26e_interspeech.pdf

## 问题
医院等场景的压力监测依赖 HRV 等生理信号时难扩展；纯语音虽可被动采集，但压力高度依赖情境，声学 alone 跨场景不够稳。需要把可被动获取的室内移动轨迹作为互补上下文。

## 方法
提出 Trajectory Speech Embedding（TSE）：日级双塔 + late fusion。音频用 openSMILE LLD（8 韵律 + 16 频谱），按日对 24 维描述子各算 15 个统计量得 360 维，再经带 [REP] token 的 Transformer 得 za；轨迹由医院室内 RSSI 定位得到分钟级序列，合并为 session（位置+时长），加正弦时间嵌入，经预训（next-location）再微调的 Trajectory Transformer 得 zt；拼接后 MLP 做二分类，并加音频/轨迹辅助损失（λ=0.5）。在 TILES-2018 上，自报压力按全局均值 μ=1.8 二值化（约 31.9% 压力），主体独立 80/10/10 划分；另有 Coordinate TSE 使用真实坐标。

## 实验与结果
Table 1：Audio Transformer MCC 0.074、F1 34.20；Trajectory Transformer MCC 0.091；TSE MCC 0.142、F1 38.65；Coordinate TSE 最佳（MCC 0.147、BACC 58.91、F1 38.81）。相对 Bi-LSTM 音频基线（MCC 0.109），框架将 MCC 提高 0.038；摘要亦报告相对 audio-only 基线 F1 +9.32%。轨迹预训练 next-location Top-1/Top-3 为 38.85%/60.40%。按 session 数分层时，高机动性下融合 F1 可达 51.5%；低机动性时轨迹往往强于音频。错误恢复分析显示：音频失败被轨迹救回的日子 session 更多，轨迹失败被音频救回的日子工作时长更短、位置多样性更高。

## 结论
联合建模环境语音与移动轨迹可稳定提升医护人员日级压力识别；未来拟做更细粒度上下文、更长时依赖，并扩展模态与部署场景。

## 点评
抓住“压力=声学×空间情境”这一实际缺口，用 late fusion 与 next-location 预训练把室内定位序列变成可迁移上下文，比硬拼特征更干净。标签靠问卷全局均值切分、日级聚合也牺牲时间分辨率；MCC 绝对水平仍偏低，说明真实医院噪声与主观标签下任务本身很难，轨迹收益更像稳健性补丁而非已可上线监测器。


# T-ORR: Text-Anchored Orthogonal Residual Rectification for Robust Multimodal Sarcasm Detection

- 论文编号：2222
- 报告人：Qi Chen
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/chen26w_interspeech.pdf

## 问题
多模态讽刺检测（MSD）依赖文本字面义与视听传递的冲突；常规将各模态投到共享空间做融合，容易纠缠瞬时冲突线索与无关噪声，削弱稀疏 incongruity 信号。

## 方法
T-ORR 以冻结 DeBERTa-v3-Large / WavLM / DINOv2-Large 提特征，文本为锚：（1）Dynamic Locality-Constrained Alignment：按文本预测动态时间中心与可学习高斯窗口，约束交叉注意力对齐音视频；（2）Structure-Preserving Geometric Decomposition：映射到文本流形后，用 QR 得文本子空间正交基，正交投影得 Resonance，残差为 Dissonance，并对 resonance 加 Decoupled Topology Constraint；（3）Contrastive Incongruity Routing：构造 Literal 态（文本+resonance）与 Incongruous 态（门控文本×dissonance），拼接二者及绝对差后 MLP 分类，并对真诚样本加门控稀疏约束。总损失为任务 CE + λ1 Lstruct + λ2 Lgatesparsity。

## 实验与结果
在 MUStARD / MUStARD++ 上按 speaker-independent 协议评测。T-ORR F1 达 76.8%（MUStARD）与 72.4%（MUStARD++），高于 DIP（74.3 / 69.1）及同骨干 Simple-Concat（70.8 / 66.1）。消融：去掉动态对齐 74.2、去掉 CIR 改拼接 73.5、去掉拓扑约束 74.9、去掉门控稀疏 75.3。定性上，真诚样本门控激活约 0.05，讽刺目标词可升至约 0.88；失败多见于依赖外部常识、视听无明显冲突的讽刺。

## 结论
将 MSD 重述为文本锚定的信号分离与冲突路由，几何解耦能更干净地隔离模态 incongruity，在 MUStARD 系列上取得正文报告的最优结果。

## 点评
相对“堆注意力融合”，正交残差把“该听字面”与“该抓冲突”拆成可解释子空间，CIR 与稀疏门控也对准了讽刺决策的直觉。收益主要来自融合几何而非更强骨干，消融支持这一点；但对纯常识/语境讽刺几乎无观测量冲突时会失效，说明方法强在可观测跨模态矛盾，而非一般语用推理。

