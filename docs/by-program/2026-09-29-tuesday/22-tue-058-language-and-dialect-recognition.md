# Language and Dialect Recognition

- 日期：Tuesday 29 September 2026
- 时间：14:00-16:00
- 形式：Oral
- Area：4
- 论文数：6

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场覆盖口语语种识别（LID）的对抗鲁棒、方言表征几何、跨库泛化，以及方言 ASR 的地理条件与语义漂移校正。安全侧首次系统展示 SOTA LID 在白盒梯度攻击下的脆弱，并提出含对抗样本挖掘、无教师防御蒸馏与语言一致性正则的自防御再训练。表征侧对 Wav2Vec 2.0 中五类中国方言做几何探测，描述低层声学差异—中层高散布细粒度音系—深层收缩但仍吻合传统分类的三阶段轨迹。

跨域与方言 ASR 方面，半正对比学习用音—文双模态与“同语不同域”半正样本处理跨库泛化；Predict-Then-Adapt 在测试时从语音回归经纬度再做地理条件解码；西/法十变体方言偏见基准揭示非均匀差距与形态句法“纠正”、话语标记失败机制；DASR-CPO 以无参考对比偏好优化抑制普通话主导先验造成的语义漂移。整体上，方言/语种问题从分类准确率扩展到鲁棒、可解释几何、地理条件与语义正确性。

## 论文技术总结

# Improving Adversarial Robustness in Spoken Language Identification through Self-Defensive Distillation

- 论文编号：3091
- 报告人：Spandan Dey
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/dey26_interspeech.pdf

## 问题
对抗攻击在 ASV/ASR 中研究较多，但独立 LID 前端被攻击可拖垮多语后端，文献中系统分析与防御不足。需在白盒梯度攻击下评估 SOTA LID 并构建主动防御。

## 方法
提出 Self-Defensive Adversarial Re-Training（SDART）：在对抗重训（ART）上叠加 (1) 对抗样本挖掘 ASM（随 epoch 提高攻击比例，PGD 步长在 [0.010,0.035] 均匀采样）；(2) 无教师、基于在线标签平滑（OLS）的防御蒸馏，用上一 epoch 按语言聚合的软标签；(3) 动态 α 与按预测熵加权的软标签；(4) 仅用正确分类的干净样本更新语言软标签矩阵。主干主要为 ECAPA-TDNN，输入 80 维 log Mel；攻击含 FGSM/PGD。

## 实验与结果
VoxLingua-10（十大语）与 Common Voice 同语种；评测 EER 与 \(C_{avg}\)。基线 ECAPA 在 PGD（0.03, 5 步）上显著变差。VoxLingua-10 上 SDART：干净 EER 2.801、FGSM 3.666、PGD 3.544，优于 ART、TRADES、DD、MART。Conformer 与 Common Voice 上多数设置亦最优；从 Conformer 迁移攻击到 ECAPA 的黑盒场景中 SDART 仍低于基线 EER。

## 结论
SDART 在多种架构与语料上同时改善干净与对抗 LID 表现，优于常见主动防御；未来拟扩展到更多攻击与其他语音任务。

## 点评
把 ASM 的渐进域暴露、语言条件软标签与“只用干净正确样本引导”串成 teacher-free 蒸馏，针对 LID 的跨语一致性而非通用 logit pairing。脆弱点是攻击设定集中于白盒 FGSM/PGD 与固定步长区间，更强或自适应攻击下的外推未充分验证。


# Probing the Layer-wise Geometry of Chinese Dialect Representations in Wav2Vec 2.0

- 论文编号：975
- 报告人：Zhen Peng
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/peng26c_interspeech.pdf

## 问题
Wav2Vec 2.0 层间如何编码方言特征不清楚；现有探测多面向标准语，中文方言工程应用常默认用顶层或简单聚合，可能丢掉中间层细粒度语音信息。

## 方法
MagicHub 五方言：西南官话（四川、武汉）、中原官话（郑州）、吴语（上海）、粤语（广州）；Azure TTS（zh-CN-XiaoxiaoNeural）生成对应标准普通话作参考锚点；VAD 去静音，16 kHz。冻结 Wav2Vec 2.0 XLSR-53 的 24 层 Transformer，提取隐状态。几何探针：与锚点的归一化 DTW 距离；方言质心两两欧氏距离 + MDS；凝聚层次聚类建谱系树。

## 实验与结果
几何指标呈三阶段：L1–8 声学主导、距离高且与物理差异一致；L9–19 距离平台、保留细粒度可分性；L20–24 距离骤降（流形收缩）。MDS：L1 无序；L12 非官话靠近、官话分离且空间分散；L24 整体向中心收缩。层次聚类 L12 对郑州等局部音系敏感，L24 自发呈现与传统分类一致的宏观分支（吴/粤 vs 官话）。

## 结论
中文方言表征经历声学→语音分化→空间收敛；深层收缩可视为特征过滤器，突出宏观分类。建议口音等细粒度任务优先中间层，宽泛方言分类可用深层。

## 点评
用无参几何探针把“层该怎么用”落到可操作建议，比只报分类准确率更有解释力。合成普通话锚点便于控内容，但也可能引入 TTS 声学偏置；五方言规模有限，谱系对齐是否稳健需更大说话人池验证。


# Robust Language Identification Using Semi-positive Contrastive Learning

- 论文编号：2502
- 报告人：Shubham Sharma
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sharma26_interspeech.pdf

## 问题
低资源口语语言识别易过拟合录音条件等域特征，跨语料泛化差；多模态方法常把同语样本一视同仁，未显式建模同语异域方差。

## 方法
提出 Semi-positive Contrastive Learning（SpCL）：双模态音频–文本编码器映射到共享 512 维空间。目标矩阵 \(T\)：同语同域为 1，同语异域为 \(\alpha\in(0,1)\)，异语为 0。总损失 \(\lambda L_{con}+(1-\lambda)L_{cls}\)（\(\lambda=0.3\)）。文本侧用静态模板或由音素序列构成的动态 caption；推理仅用音频编码器+分类器。音频编码器试 wav2vec2 音素变体与 Whisper，文本为 RoBERTa。

## 实验与结果
12 种印度语言，训练见域 Ekstep+DatasetM(rs)，未见域 yt 与 IndicVoice。SpCL whisp（dynamic）准确率：Seen 98.76%、yt 91.42%、IndicVoice 54.52%，优于 MFCC/音素 Conformer、UDA、Whisper 微调等基线。VoxLingua33 上 SpCL whisp dynamic 93.0%（MuSeLI 96.1%）。消融：\(\alpha=0.7\) 与动态 caption 对未见域帮助最大。

## 结论
半正对比与动态 caption 可在无显式域适应下提升跨域 SLID；Whisper 音频编码器最稳。未来拟在联合嵌入空间做推理。

## 点评
把“同语异域”单独加权，比二元对比更贴合域偏移几何。强在训练要文本、推理只要音频。脆弱点是 IndicVoice 全体仍偏低，且域标签需在训练期可知；\(\alpha\) 需调参。


# Predict-Then-Adapt: Inferring Coordinates from Speech for Continuous Geo-Conditioned Dialectal ASR

- 论文编号：3333
- 报告人：Pouya Mehralian
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/mehralian26_interspeech.pdf

## 问题
连续地理坐标条件（如 GLoRIA）可改善方言 ASR，但推理时常无可靠说话人坐标；离散方言标签又难以刻画连续变异。

## 方法
在冻结编码器上挂轻量 Coordinate Regression Head（CRH）：多头注意力池化 + MLP，SmoothL1 回归经度/纬度。两遍推理：(1) 关闭 GLoRIA 预测 \(\hat{c}\)；(2) 用 \(\hat{c}\) 打开坐标门控低秩适应再解码。骨干为 180M Cascaded Encoder Dual Features（12 层 Conformer + 6 层 Transformer），在 GCND 荷兰方言语料上适配。CRH 增参 <0.1%，时延开销 <3%。

## 实验与结果
CRH 大圆误差随时长下降，约 10–30 s 达 15–25 km 量级（30 s overall avg 23.72 km；插值约 16 km，外推约 38 km）。GLoRIA 对坐标扰动在 ≤15 km 几乎无影响，25 km 平均 <1 个 WER 点。10 s 无元数据设置：CRH+GLoRIA 平均 WER 32.62，优于同秩 LoRA（35.67），接近 oracle 坐标（32.04），远好于 Whisper large-v3 / OWSM。

## 结论
从语音推断坐标足以激活大部分地理条件收益，且保持 GLoRIA 可解释门控；外推区更难，未来可做不确定度感知条件化。

## 点评
把“缺坐标”问题收成可度量的定位误差与 WER 鲁棒半径对齐，工程闭环完整。两遍推理开销可控是亮点。脆弱点在训练坐标流形外的方言（如 Limburgs）与短时（3 s）回归到均值；语言学分辨率限制使误差难压到公里级邻域密度。


# Dialect Bias in Speech Recognition Across 10 Spanish and French Varieties

- 论文编号：458
- 报告人：Rodrigo Nieto
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nieto26_interspeech.pdf

## 问题
ASR 方言偏差研究多聚焦英语，西语与法语等全球语言的系统差距机制不清；Common Voice 等资源多为朗读标准文本，难以暴露形态与话语标记等方言特征。

## 方法
从 Apple Podcasts 构建约 20 小时、性别平衡、按国家方言分层的评测语料（西语 5 种、法语 5 种，共 10 方言、129 说话人），人工转写保留方言正字法。评测七个模型（含 Whisper v2/v3、Otter、GPT-4o-Transcribe、Wav2Vec2、Qwen2-7B、SALMONN-7B）。对 Whisper v3：JSD word-shift 做词汇分析；用 pyannote 与 Whisper L16 说话人嵌入做方言分类与声学距离–WER 相关；LoRA 微调并分别冻结编码器/解码器定位误差源。

## 实验与结果
方言间 WER 差异显著（西语 Kruskal–Wallis H=179.24；法语 H=63.18）。西语：阿根廷/多米尼加最好，智利最差，并非人口规模单调；法语：欧洲变体整体优于加拿大与非洲。性别差距因方言而异。词汇侧见 voseo“矫正”、区域词与 pues 等话语标记失败；声学侧方言–性别分类准确率西语约 83–86%、法语约 67–77%，与 WER 相关。微调：冻结编码器接近全 LoRA，冻结解码器几乎无增益，显示偏差主要在解码器。

## 结论
西法 ASR 误差系统反映相对训练分布的语言/声学距离；公平 ASR 需建模方言语言特征。语料与诊断框架可复用于其他语言。

## 点评
把基准、JSD 错误词与解码器定位串成因果链，比单纯报 WER 更有解释力。播客语体与门控发布限制外推到全部语域；小数据 LoRA 无法消除差距，也点出仅靠轻量适应不够。


# DASR-CPO: Reference-Free Contrastive Preference Optimization for Correcting Mandarin Semantic Drift in Low-Resource Chinese Dialect ASR

- 论文编号：1228
- 报告人：Tao Zhang
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26s_interspeech.pdf

## 问题
Whisper 等预训练 ASR 在低资源中文方言上常出现 Mandarin Semantic Drift：把方言词解成音近但义错的高频普通话同音词（如“阆中→郎中”）；LoRA SFT 降 CER，却不显式压制这些竞争假设。

## 方法
提出 DASR-CPO：离线从基线假设挖掘混淆（去调拼音编辑距离≤2 的高频替换）构成硬负例；用全序列动态匹配在 BPE 下定位方言跨度；在 teacher-forcing 参考上对跨度打分，取最强负例做 reference-free CPO，并与 SFT CE 混合 \(L_{SFT}+\lambda L_{CPO}\)。骨干 Whisper-Large-v3 + LoRA（q/v，r=32）；Stage1 SFT 3 epoch，Stage2 CPO 2 epoch（β=0.5，λ=1.0，冻结编码器）。

## 实验与结果
MagicData 四川话 ASR-CSICHDIACSC（4.53 h，24 说话人，8:1:1）。相对 Pure LoRA：CER 24.85%→22.58%，方言实体 F1 72.82→74.15，Recall +1.55，假正例 39→32；优于 Context Bias 重加权。推理无额外开销。局限：划分非说话人无关、依赖词表与挖掘质量。

## 结论
把方言适应写成对漂移跨度的偏好排序，可在极低资源下同时改善 CER 与实体语义，且零推理开销；未来拟扩到更多方言与语码转换。

## 点评
针对“音近义错”这一解码先验问题，跨度级硬负对比比纯似然或 token 重加权更贴病灶。非 speaker-disjoint 与小词表可能夸大泛化；CER 绝对值改善有限，但实体指标更能说明语义收益。

