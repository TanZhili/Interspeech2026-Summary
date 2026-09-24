# Speech Production and Perception 2

- 日期：Thursday 1 October 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：1
- 论文数：9

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场海报连接语音产生/感知的声学线索、超声/MRI 发音成像、统一 ASR–TTS 连续表征，以及二语重音与肌肉动力学测量。一端是低资源语言的分类与音素发现，另一端是物理声道模型与深度学习自动化测量，共同强调“可观测发音证据”如何支撑识别、合成与教学。

声学上，辅音分类可受益于邻接元音中点共振峰等外在线索；发音侧则探索超声静默识别的物理一致性增强、清洁语音上的声学–发音反演，以及颏舌骨肌厚度的自动量化。学习系统侧出现统一 LLM（自回归 ASR + 流匹配 TTS）与极低资源类型学迁移音素发现。心理语言学与二语研究则检验词频/音节惊讶度与词重音时空手势协调。

## 论文技术总结

# Vowel Allophony Improves Maximum-Likelihood Classification of Warlpiri Consonants

- 论文编号：3107
- 报告人：Coralie Cram
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/cram26_interspeech.pdf

## 问题
澳大利亚语言塞音部位对立多、方式对立少；仅靠辅音内在线索往往不足以区分密集部位连续统。Warlpiri 五部位塞音（无音位浊音对立）中，邻接元音的哪些外在线索最有助于分类仍不清晰。

## 方法
用 DoReCo 半自发叙事（14 名女性，25–50 岁）中的 VCV，对 /p t ó c k/ 做最大似然高斯分类。线索组：S=辅音内在（时长、爆破谱矩、E-H/M、强度、边界 F1–F4）；T=邻接元音前/后 25% 的 F1–F4 过渡；M=元音中点 F1–F4。对 CV/VC 分别训练 7 种 S/T/M 组合，分层 10 折宏平均 F，置换检验（Bonferroni α=0.005）。

## 实验与结果
仅 S 时辅音宏 F 约 0.654（CV）/0.647（VC），较易混淆。加入 M 比加入 T 提升更大：CV 上 SM 0.702 显著优于 ST 0.681；STM（0.691）反不及 SM。VC 类似，SM≈0.681、STM≈0.691。元音分类主要靠 M（F≈0.79–0.82），加 S/T 几乎不伤元音准确率。CV 整体略好于含 S 的 VC，作者联系再音节化/爆破与后接元音更近。

## 结论
辅音内在线索不足；邻接元音中点的音位变体信息对 Warlpiri 部位分类帮助最大，且不明显牺牲元音可分性。最大似然分类可为低资源语言感知建模提供系统级上界与混淆预测工具。

## 点评
把“最优听者能用什么线索”落到可比较的分类器消融，比单对对比更系统。中点变体增益大于过渡，对“澳大利亚语言弱化元音对辅音协同”的常见叙述是有益修正。局限是强制对齐爆破与半自发语体噪声；混淆矩阵细分析留作未来工作。


# Towards Robust Ultrasound-based Silent Speech Recognition Learning Physics-Aware and Context-Rich Representations

- 论文编号：2646
- 报告人：Qisheng Xu
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/wen26d_interspeech.pdf

## 问题
基于 Ultrasound Tongue Imaging（UTI）的 Silent Speech Recognition 面临两类瓶颈：探头位移与散斑噪声等成像物理变异使同一发音在表示空间不稳定；协同发音带来的长程时序依赖又难被逐帧独立建模抓住。

## 方法
提出物理感知与上下文丰富表示学习框架：用 k-means 对高帧率 UTI 序列做时序聚类下采样，得到紧凑且保留关键调音上下文的定长序列；训练时施加物理启发增强——空间平移模拟探头位移、高斯噪声模拟散斑、时序掩码强迫依赖长程上下文；前端用 3D-CNN 提局部时空特征，再经双向 GRU 建模全局时序，以 CTC 端到端解码。

## 实验与结果
在 UXTD 儿童词级数据上比较 ST-GRU、ST-LSTM、ST-Transformer。Overlap 设置下 Ours 的 WER/CER 为 0.1595/0.1009，相对最佳基线 WER 降约 36.5%；Unseen 设置下为 0.0597/0.0227，相对最佳基线 WER/CER 分别降约 50.4%/69.1%。消融表明 3D-CNN 与数据增强均必要；物理增强使同内容不同采集条件的表示余弦相似度由 0.7697 升至 0.9630。

## 结论
一致性（物理增强）与完备性（聚类下采样 + 3D-CNN/BiGRU）共同提升 UTI-SSR 鲁棒性与跨说话人泛化；低资源下时空归纳偏置优于大容量 Transformer。未来拟探索自监督预训练与更大规模数据。

## 点评
把超声成像的物理伪影直接做成增强先验，比单纯堆更深网络更贴 UTI 特性。聚类下采样在压缩冗余的同时保留调音关键帧，对长序列与小数据场景合理。ST-Transformer 崩溃也提示：UTI-SSR 更吃局部运动与噪声抑制，而非全局注意力容量。局限是目前主要在 UXTD Type-A 词级设定，句子级与更强探头变异仍待验证。


# Acoustic-to-Articulatory Inversion of Clean Speech Using an MRI-Trained Model

- 论文编号：734
- 报告人：Sofiane Azzouz
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/azzouz26_interspeech.pdf

## 问题
rt-MRI 可同时获得声学与完整声道形状，但机内录音噪声大，即使去噪也与安静环境语音差异明显；实际应用需要能对干净语音做 acoustic-to-articulatory inversion，而不能假定始终有 MRI 噪声条件下的音频。

## 方法
同一法语女说话人分别采集约 2.5 小时 rt-MRI（136×136，20 fps）去噪语音与对应干净录音；用专家校正的音素切分做层级对齐（句→词→音素内时间归一化）。输入用 HuBERT-Base 嵌入，经两层全连接 + 两层 Bi-LSTM 回归 8 个调音器轮廓（各 50 点，MSE）。对比三设定：M2M（去噪训测）、M2C（去噪训/干净测）、C2C（干净训测）；并与 DTW 对齐对照。

## 实验与结果
平均 RMSE：M2M 1.51 mm、C2C 1.56 mm、M2C 1.64 mm；C2C 接近 M2M，明显优于跨域 M2C。音素对齐优于 DTW（M2C-DTW 1.71 mm、C2C-DTW 1.68 mm）。舌等调音器误差相对较大，咽壁等较小。

## 结论
在 MRI 轮廓监督下，用干净语音训练/测试可将平均误差做到约 1.56 mm（接近像素尺度 1.62 mm），说明声学–调音反演可用于真实安静场景，而不仅限于机内去噪语音。

## 点评
核心贡献是把“MRI 监督–干净声学输入”的域落差用音素级对齐桥起来，而不是只做更强去噪。C2C 接近 M2M、又显著好于 M2C，说明训练域匹配比硬跨域推理更关键。未建模 Lombard/仰卧姿势效应、且为单说话人，是走向多说话人实用系统时的主要边界。


# UniVoice: Unifying Autoregressive ASR and Flow-Matching based TTS with Large Language Models

- 论文编号：2194
- 报告人：Wenhao Guan
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/guan26b_interspeech.pdf

## 问题
现有 LLM 语音框架常把 ASR 与 TTS 割裂；离散 codec token 便于统一建模但量化损失会损害识别精度与合成保真度。需要在连续表示空间里同时做自回归理解与高保真生成。

## 方法
UniVoice 以 SmolLM2-360M 为骨干：ASR 支路用 Whisper 编码器 + adapter 池化进入 LLM，因果掩码自回归预测文本；TTS 支路用 OT 条件 flow matching，以文本前缀引导的 speech infilling 在 DiT 风格 Transformer（去掉 AdaLN-zero，时间嵌入拼到噪声 mel 序列前）上重建被掩码 mel，双向注意力；总损失为 λ·LM + CFM，推理时 TTS 用参考音/文做 prompt 并经 BigvGAN 声码。

## 实验与结果
在 LibriHeavy 50K 小时训练。统一模型 SIM 0.56、TTS WER 4.06、UTMOS 3.72，LibriSpeech ASR WER clean/other 为 3.0/6.3，相对多个统一基线有竞争力；相对专用 CosyVoice2 等仍有 SIM/自然度差距。消融：infilling 优于 speaker embedding 条件；TTS 用 Full Mask 明显优于 AR Mask；λ=0.005 优于 0.01。

## 结论
单一连续表示 LLM 可同时胜任自回归 ASR 与 flow-matching 零样本 TTS；双注意力掩码与文本前缀 infilling 是打通因果/双向分歧的关键。当前聚焦 ASR+TTS，未来拟扩展更多语音任务并开源。

## 点评
用连续 mel + FM 避开离散 token 信息损失，同时用双掩码解决 AR/非 AR 结构冲突，设计动机清晰。联合训练相对单任务有可懂度收益但也有自然度折中，且去掉 AdaLN 可能削弱说话人适应——作者也承认 SIM 落后专用 TTS。参数量（0.4B）与 50K 小时数据下能逼近更大统一模型，对端侧一体化交互有实用意义。


# How do word frequency and syllable surprisal affect response time and acoustic duration in sentence formulation?

- 论文编号：1080
- 报告人：Ivan Yuen
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/yuen26_interspeech.pdf

## 问题
词频与音节频率（本文用音节 surprisal）都会影响启动反应时（RT）与声学时长，但多数研究只在单一语言层面上操作；若按 Levelt 式“离散、分阶段、串行”生产模型，应预期跨层加性效应，这一点在真实词的单/双音节材料上尚未厘清。

## 方法
20 名德语被试在句中/句末位置产出控制词频与重读音节 surprisal 的单、双音节词。词频来自 SUBTLEX-DE/CELEX，音节 surprisal 由 deWaC 上训练的语言模型估计。测量问句 onset 到句反应 onset 的 RT，以及重读元音时长；对 log 变换后的 RT 与长元音时长做线性混合效应模型，检验词频×音节 surprisal 等交互。

## 实验与结果
未得到假设的加性效应，而是选择性交互：单音节词 RT 受词频与位置影响（低频反而更快、句中更慢）；双音节词 RT 主要受音节 surprisal 边缘影响，且方向与预期不完全一致。长元音时长上，单音节仅见句末拉长；双音节出现词频×surprisal 交互，高 surprisal 在低频词上反而伴随更短时长，与“高 surprisal→更长”预期相反。

## 结论
词频与音节 surprisal 对 RT 与声学时长的作用因音节类型而异，且两指标不镜像同一过程；结果更支持跨层交互式生产解释，而非严格离散串行阶段模型。

## 点评
把词层与音节层可预测性正交操纵并同时看规划（RT）与实现（时长），直接检验经典串行假设，问题设定扎实。低频单音节更快、高 surprisal 时长更短等反预期结果，提示“心理词库预编译音节”叙事不能简单外推到真实词跨层组合。刺激集合较小、低频单音节 surprisal 范围受限，是解释交互方向时需谨慎的地方。


# Extreme Few-Shot Phoneme Discovery for Indigenous Australian and Pacific Languages via Typological Transfer Learning

- 论文编号：284
- 报告人：Prasanth Yadla
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/yadla26_interspeech.pdf

## 问题
诸多原住民澳/太平洋语言转录极少（常不足 10 小时），常规声学单元发现假设远超 100 小时无标注音频；通用多语 SSL 又偏向印欧音系，在不足 1 小时的极端低资源设定下难以发现卷舌、元音长度等细微对立。

## 方法
提出 Typological Anchor Selection（TAS）：用 PHOIBLE 音位库存 Jaccard 重叠、谱系权重与源语言时长对数加权选源语（验证上偏好爪哇语、他加禄语）。在源语上预训练 VQ-VAE，再保留码本、降学习率适配目标语（≤60 分钟），并用自适应 commitment 权重缓解遗产录音噪声与码本坍塌；后处理做共现/时长/层次聚类映射到类音位单元。

## 实验与结果
目标语：Te Reo Māori、Pitjantjatjara、Nauruan。相对 XLS-R，平均 NMI 提升 18.8%、cluster purity 提升 15.6%（置换检验 p<0.01）。多源（Jav+Tag）优于单源；码本 K=40 对 Māori 最优；仅 15 分钟目标数据即可达到 XLS-R 用 60 分钟的水平（NMI 0.48，Purity 0.64）。

## 结论
类型学引导的迁移可为不足一小时音频的音位发现提供可复现路径，适配后的 VQ-VAE 对遗产录音更稳健；输出宜作需母语语言学家校验的初步假设。

## 点评
用 PIO 选锚点语种而非盲目多语预训练，把类型学先验写进数据选择，切中濒危语言文档化痛点。评价指标是扰动下的簇稳定性而非相对金标音位准确率，上限解读需克制。对声调语言/语系孤立语会退化到随机初始化，且未显式建模音高，是应用边界。


# Lexical stress-conditioned spatiotemporal gestural coordination in L2 English

- 论文编号：3116
- 报告人：Paul McGuire
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/mcguire26_interspeech.pdf

## 问题
台湾国语（TWM）缺少感知上显著的词重音对立；L2 英语学习者常过度依赖 F0，而超喉调音在整音节时空协调上如何实现重音对比仍不清楚——既有 EMA 研究多看元音中点位移，较少覆盖辅音手势与跨音节协调。

## 方法
用 EMA 记录 TWM 说话人产出 conflict（名词/动词）中第二音节 /flIkt/ 的调音轨迹（TT、TD、LL、JAW）。以六个收缩 landmarks 做时间配准后，对多维轨迹做 multivariate FPCA；在 PC1–PC2 空间用 PERMANOVA 检验重/非重条件是否可分。两位英语教师 9 点口音评分（AR）作描述性语境。因辅音簇实现失败排除 4 人，保留 6 人共 98 token。

## 实验与结果
六人均表现为重音音节更长，但区间模式因人而异。FPCA 空间中 4/6 人重音条件可分（如 08F p=0.001, R²=0.413），AR 最高的 01M、07F 不可分，且出现收缩目标顺序反转。扰动图显示可分说话人常伴随注册时间轴拉长、元音段更大下颌下降、/f/ 达成时下唇略高等联合时空重组；仅有时长差不足以解释可分性。

## 结论
部分 TWM L2 说话人仅凭超喉调音时空模式即可区分英语词重音；口音更重者协调更不稳定。FPCA+landmark 配准适于整音节分析，未来需更大样本把 AR、声学线索与调音协调一并建模。

## 点评
把重音问题从“有没有更大位移”推进到“整音节手势是否可分”，并刻意不把声学信息喂进分析，能直接回应“F0 依赖之外调音是否携带信息”。小样本、单音节结构、AR 仅描述性使用，限制了因果推断；辅音簇筛除本身也可能偏向调音更稳定的说话人。


# Automated Measurement of Geniohyoid Muscle Thickness During Speech Using Deep Learning and Ultrasound

- 论文编号：1664
- 报告人：Alisher Myrgyyassov
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/myrgyyassov26_interspeech.pdf

## 问题
超声常用于舌轮廓，颏舌骨肌（GH）对舌位与下颌重要，但成像与标注难、人工量厚度耗时且评定者间变异大，限制大规模语音与临床研究。

## 方法
SMMA 两组件：(1) 超声帧标准化后由 CNN 分割 GH（224×224），训练 50 epoch、Dice+Focal（0.8/0.2）、超声增广；比较 Attention UNet、UNet、UltraUNet、SwinUNet、DeepLabv3；(2) 对掩膜形态学后处理，骨架化取中轴，仅用骨架 25%–75% 分位段计算平均厚度（边界垂直距离×2），可选曲率与截面积。数据：11 名粤语者（5 男 6 女）1650 张标注图，按说话人 7:2:2；SuperSonic Aixplorer + SC6-1，30 fps，声同步。

## 实验与结果
分割：人工间 Dice 约 0.90–0.92；UltraUNet Dice 0.9037±0.0035、IoU 0.8263，选为骨干。厚度相对声学家：随机图 MAE 0.88 mm、r=0.707；高质量临床选图 MAE 0.53 mm、r=0.901。孤立元音 /a:/、/i:/、/u:/（各 6 次，共 198）：/a:/ 最厚 7.29±0.90 mm，/u:/ 6.65±0.79，/i:/ 5.95±0.84（ANOVA p=0.019；/a:/ vs /i:/ Cohen’s d>1.3）。男性在 /i:/、/u:/ 厚约 5–8%。重复 CV 5.06%。

## 结论
SMMA 可接近人工水平自动量化言语中 GH 厚度，元音模式与下颌下降激活一致；消除人工标注瓶颈，便于言语运动与吞咽/构音障碍评估。局限含 N=11、单语、单声学家真值、图像质量强影响误差。

## 点评
把“分割质量接近评定者一致性”和“骨架中段厚度”串成可复现流程，填的是 GH 语音学研究的方法空白，而非新声学特征。骨架均匀形态假设与孤立元音对齐较易；连续语流、不规则掩膜与病理样本是主要脆弱点，文中亦承认需音素对齐与质量阈值。


# Articulatory Dynamics using Physical Vocal-tract Models

- 论文编号：840
- 报告人：Takayuki Arai
- 程序：Thursday 1 October 2026 / Speech Production and Perception 2
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/arai26_interspeech.pdf

## 问题
声道可视化与建模对语音学、教学与病理重要，但静态物理模型难以呈现动态协同发音；可编程动态物理模型（尤其线性凸轮对应 Articulatory Phonology 手势分数）对调音动态的仿真能力尚缺系统检验。

## 方法
使用带鼻腔与 VP 耦合旋钮的 VTM-UT30-D9，以线性凸轮实现手势分数式时序控制。实验一：按 LA、TBCD、TRCD、VEL 等 tract variables 产出 [bɑb]/[bɑm]，测量语谱与不同 VP 开度下 [ɑ] 的冲激响应。实验二：对 nonsense [ɑbɹɑ] 系统改变 −LA 与 TBCD 起始间距 d（Step 0–7，每步 10 次，共 80 次），用 wav2vec 2.0（Matlab speech2text）判断是否识别为辅音簇，并做趋势与相邻步检验。

## 实验与结果
[bɑm] 在元音后段出现鼻化相关抗共振；随 VP 旋钮 0°→45°，极–零对逐步插入，F1 可被零点抵消。对 [ɑbɹɑ]，d 增大导致 [b] 与 [ɹ] 间插入类 schwa；ASR 在 Step 0–1 几乎总判为辅音簇，Step 6–7 为 0%；Cochran–Armitage 显示正确率随步数显著单调下降（χ²=42.538, p<0.001），相邻步仅 Step1→2 经 Bonferroni 校正后显著。

## 结论
动态物理模型能按 AP/TD 手势分数实现鼻化协同与时序重叠，并复现目标缺失 schwa 式插音；线性凸轮是连接手势时序与声学输出的直观实验平台。

## 点评
把抽象 gestural score 落到可听、可测的机械声道上，对教学演示与协同发音机制论证都很有说服力。实验设计以时序参数扫描为主，量化指标依赖外部 ASR 对“是否听出插音”的二值判断，对感知边界的解释需结合人耳实验进一步确认。模型块数与几何简化也限制了对真实舌形多样性的覆盖。

