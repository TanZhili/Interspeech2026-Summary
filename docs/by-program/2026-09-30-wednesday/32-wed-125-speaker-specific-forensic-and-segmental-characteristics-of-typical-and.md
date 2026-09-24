# Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Poster
- Area：2
- 论文数：8

## 技术趋势与评论

与评论

与评论

与评论

与评论

与评论

与评论

本场海报横跨发音语音学、法医说话人比对、双语节奏、方言音变、体位对共振峰影响、儿童擦音位置变异、痴呆检测隐私，以及阿萨姆语元音和谐。共同线索是：说话人特异信息存在于哪些频段/时间组织，以及如何在临床或取证场景中与音段描写对读。

发音与音变侧用超声动态分析喉位与舌背姿态解释美式英语软腭塞音；新西兰英语在奥克兰百年材料中重估短前元音漂移，并检验仰卧/坐/站对 F1/F2 的小幅但系统性影响；波兰儿童规范 /s/ 显示词首—词中光谱差异最大；阿萨姆语跨三大方言区确认和谐语境中 /ɛ/ 抬高。

法医与应用侧，带限倒谱（BLCC）扫描显示约 0–0.6 kHz 与 4–6 kHz 说话人区分力强、约 7 kHz 以上最弱；双语政治演讲中辅音节奏更保留说话人签名、元音节奏更随语言变化。痴呆检测则用信号级关键词对齐扰动与特征级对抗/互信息噪声，在近随机说话人识别下保持分类效用。

## 论文技术总结

# The Role of Laryngeal Position in the Articulation of American English Velar Stop Consonants

- 论文编号：207
- 报告人：Daejin Kim
- 程序：Wednesday 30 September 2026 / Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/kim26b_interspeech.pdf

## 问题
美式英语 /k/–/ɡ/ 音位对立的舌–喉协同机制不清；声学上有 CD/VOT/f0 差异，但少有同时量化舌背（TD）与舌骨（HY）运动并联系虚拟目标与气动约束的研究。

## 方法
10 名 AE 母语者，超声同步录音，DeepLabCut 追踪舌轮廓与 HY/MD；TD 距离相对 HY 定义姿态 landmarks（ONSET/TARGET/OFFSET、峰速）。目标词 keep/geek/coop/goop/cod/god 嵌句，共约 720 次。用 LMEM、VGLM、GAMM 分析声学（CD、VOT、VD、f0）与运动学。

## 实验与结果
/ɡ/：更长 CD、更短 VOT、更长后接元音、更低 f0。目标处舌形差异可忽略。/ɡ/ 在 TARGET/OFFSET 有更长 HY–MD 距离，HY 更退后；/k/ 更上抬 HY。/ɡ/ 的 TD ONSET→TARGET 距离更大、时长更长、峰速更高，支持更大时空扩张与更强舌–软腭接触。结果支持假设 2（气动/虚拟目标路径）而非单纯舌牵拉抬高 /k/ f0。

## 结论
AE 软腭塞音对立由舌扩张程度、舌–软腭接触与喉位共同塑造，并与声学相关物对应。

## 点评
把 HY 作为喉位代理并相对 HY 测 TD，比单看舌轮廓更能抓住对立。超声对软腭表面限位有限，「虚拟目标」仍是间接推断；VGLM 无随机效应，作者已用分轴 LMEM 补救，说话人变异仍需更大样本。


# Band-Limited Cepstral Analysis of Speaker Sensitivity in Forensic Voice Comparison

- 论文编号：1028
- 报告人：Shunichi Ishihara
- 程序：Wednesday 30 September 2026 / Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/ishihara26b_interspeech.pdf

## 问题
说话人鉴别信息在频谱上分布不均；需在连续语流中定位敏感子带并量化其贡献，以增强法医声纹比对的可解释性。

## 方法
对 AusEng 500+ 中 162 名成年男性约 30 s 访谈语流提 14 维全带 LFCC，再用 BLCC 线性变换扫描 0–8 kHz：0.6/1.2 kHz 宽、0.2/0.4 kHz 步进。GMM–UBM（256 分量）+ 逻辑回归校准做 LR 比对；六折轮换 test/background/calibration。实验 1 单子带 C_llr；实验 2 融合最多四个 0.6 kHz 子带的 LR。

## 实验与结果
全带 LFCC：C_llr≈0.136。各子带 C_llr<1，均含有用信息；近 8 kHz（约 >7 kHz）最弱。0.6 kHz 配置下 0–0.6 kHz 最强（C_llr≈0.583），4–6 kHz 亦强；1–3.5 kHz 相对偏弱。融合分散、互补的强子带可显著低于全带基线；相邻最高频弱子带融合最差。

## 结论
BLCC 可灵活剖析子带说话人敏感度；男声澳英连续语流中低端与 4–6 kHz 信息最强，最高频最弱。未来需跨语言、女性与不同时长验证。

## 点评
相对重分析原信号的滤波子带法，BLCC 从全带 CC 线性投影更高效可控。16 kHz 采样服务科学扫描，与典型手机物证带宽不完全一致，外推实务系统需谨慎。融合结果说明不同频区编码不同说话人线索，而非简单冗余。


# Speaker-Specific and Language-Dependent Temporal Organization in Bilingual Political Speech

- 论文编号：1335
- 报告人：Nina Hosseini-Kivanani
- 程序：Wednesday 30 September 2026 / Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/hosseinikivanani26b_interspeech.pdf

## 问题
节奏与时长组织对说服性公共演讲重要，但多语政治家在卢森堡语与法语间如何重组时域模式、以及说话人身份 vs 语言选择各占多少方差，尚不清楚。

## 方法
10 名双语政治家（5 女 5 男），每人各 20 句自发卢森堡语与法语（共 400 句），手工分句并标注 CV 层与停顿。计算 %V、ΔC/ΔV、rPVI/nPVI、语速等；用说话人 ICC 与语言 R² 分解方差，配对 t 检验与 Language×Gender 交互检验。

## 实验与结果
辅音类指标保留较强说话人特异签名（较高 ICC、较低语言 R²）；元音/声母间隔类指标主要由语言驱动（法语元音更长、更可变，FDR p<.01）。辅音时域语言差较小。未发现稳健的语言×性别交互。%V 等亦呈语言主导模式。

## 结论
双语公共演讲中，语言选择系统重组节奏时长：元音侧跟语言，辅音侧更像个人签名。

## 点评
把「身份 vs 语言」用 ICC/R² 拆开，比单报均值差更有信息。样本仅 10 人、政治体裁窄，外推日常双语需谨慎；CV 自动对齐后人工修正，标注一致性仍影响 ΔC 等敏感指标。


# Revisiting the NZE front vowel shift: evidence from New Zealand's largest and most linguistically diverse city

- 论文编号：1526
- 报告人：Brooke Ross
- 程序：Wednesday 30 September 2026 / Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/ross26_interspeech.pdf

## 问题
奥克兰作为新西兰最大、语言最多样城市长期被 NZE 社会语音叙事忽视；短前元音移位（SFVS）轨迹及 /ɪ/ 央化时间线是否符合既有「持续抬高 /e,æ/ + /ɪ/ 央化」叙述，需用历史+现时数据重审。

## 方法
现代 Auckland Voices（n=67，青年/40+，2010 年代）与历史奥克兰出生口述史（n=8，约 1900–1911 出生）。强制对齐+手工校正目标，提 F1/F2；性别线性变换后 LMM。实验 1 比较三组 /e,æ,ɪ/；实验 2 分析历史说话人 /ɪ/ 邻接边音条件。

## 实验与结果
相对较接近「标准」抬高型的 Older AV，Historical 与 Younger AV 的 /e,æ/ 均显著降低并后缩（F1 升、F2 降），呈抬高后回落。三组 /ɪ/ 质心均已降低后缩；青年相对 Older 仅 F1 显著更高。实验 2：历史说话人中邻接边音的 /ɪ/ 明显更后缩，去除后组间差异减弱，提示早期央化可能先受边音条件触发。

## 结论
奥克兰数据显示 /e,æ/ 的上升–回落与早期即已出现的 /ɪ/ 央化，挑战单一持续链移叙述；央化起初或受边音音系条件制约。

## 点评
把城市创新中心与历史档案对接，补上 NZE 叙事缺口。历史录音质量与小样本（n=8）限制推断力度；边音条件分析较有说服力，但仍需更多历史说话人与音系环境量化加固。


# Effects of body position on vowel formants in New Zealand English

- 论文编号：1545
- 报告人：Qing Guan
- 程序：Wednesday 30 September 2026 / Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/guan26_interspeech.pdf

## 问题
日常与 MRI 等场景下体位（仰卧/坐/站）少被纳入元音共振峰建模，跨实验合并 F1/F2 时可能引入系统偏移。

## 方法
9 名 NZE 母语者（两年龄段、男女）在隔音箱内完成相同 /hVd/ 词表（11 元音）的三种静态体位；麦克风约 20 cm。WebMAUS 对齐+手工校正，目标点提 F1/F2（Bark）。LMEM 含元音、年龄、性别及与体位交互，逐步简化后报 EMM 成对对比。

## 实验与结果
整体体位效应小，最清晰对比多涉及仰卧相对坐/站。元音特异对比仅见于少数元音，F2 在高前元音最明显。本数据中 F1 体位差在女性更清晰，F2 差在年轻女性条件显著。描述性 CoG 显示仰卧相对其他体位 F1/F2 略高。

## 结论
体位可引入小而条件化的共振峰偏移，合并或解释跨配置数据时应记录体位。

## 点评
within-speaker 三体位设计直接服务 MRI–实验室可比性。n=9 限制交互推断；麦克风随体位重定位虽控距，仍可能混入口腔辐射角差异。效应「小但不为零」对精细社会语音比较仍有提醒价值。


# From onset to coda: spectral variation in normative Polish /s/ produced by children

- 论文编号：1936
- 报告人：Oliwia Skórzewska
- 程序：Wednesday 30 September 2026 / Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/walczak26_interspeech.pdf

## 问题
感知上规范的波兰语儿童 /s/ 在词首/词中/词尾是否仍有亚音位谱差异，既往描述不足。

## 方法
PAVSig 中 102 名 5–8 岁儿童、8 个儿童词、约 816 个规范 /s/ 样本（两位言语病理专家判断）。手工切分，20 ms 帧提 CoG、偏度、峰度、spectral flux。LME：词位固定效应，说话人随机斜率（重音/前后音）+ 词随机截距；Bonferroni 校正成对对比。

## 实验与结果
词位显著影响谱特征；最强成对差在词首 vs 词中（CoG、flux、峰度、偏度）。词中–词尾对比通常较小且多不显著，偏度例外。词中 CoG 高于词首；词首偏度等与非词首分离更清晰。

## 结论
即使感知规范，儿童波兰语 /s/ 仍随词位呈现可测谱变异，词首–词中对比最突出；可为临床基线提供参考。

## 点评
把「听感正常」与「声学仍分位」分开，对隐蔽对比与临床基线有意义。词表仅 8 词且词位不平衡（4 首/2 中/2 尾），虽用 parent word 随机效应，概括力仍受限；未把年龄作协变量，5–8 岁发展差未评估。


# Multi-Level Privacy-Preserving Dementia Detection from Speech via Targeted Adversarial Obfuscation and Representation Learning

- 论文编号：2868
- 报告人：Henriette Flore Kenne
- 程序：Wednesday 30 September 2026 / Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/kenne26_interspeech.pdf

## 问题
痴呆检测语音同时暴露说话人身份与转写内容；既有隐私方法常只防单一威胁，或牺牲诊断效用。

## 方法
双层框架：(1) 信号级 Cumulative Signal Attack（CSA）：在关键词对齐片段用 PGD+CTC 把波形推向语义偏离目标转写，累计整形扰动以保韵律；(2) 特征级：共享编码器 + GRL 压制说话人支路，并用互信息引导噪声注入保护与痴呆相关的韵律维、破坏说话人维。在 DementiaBank Pitt 上评测 ASR WER、说话人 F1/EER 与痴呆 F1/AUC。

## 实验与结果
摘要报告 WER=1.00、说话人 EER=0.59、说话人 F1=0.003、痴呆 F1=0.78、AUC=0.86。相对噪声等基线，双层在保持较高痴呆 F1（约 0.79 vs 原 0.83）同时更强压制说话人；白盒窃听下说话人 F1 约 0.003、EER≈0.50、Whisper WER=1.00。

## 结论
信号语义混淆与特征层说话人对抗可同时抵御机器转写与说话人再识别，并保留可用诊断性能。

## 点评
把威胁拆成「听懂内容」与「认出是谁」两路分别打，比单点匿名更贴临床共享场景。关键词对齐扰动依赖转写质量；不可逆扰动利于隐私但不利于事后审计。效用仍用宏 F1/AUC，临床部署还需校准阈值与可解释性。


# An Acoustic Investigation of Mid Front Vowel Harmony in Assamese

- 论文编号：3034
- 报告人：Saurabh Nath
- 程序：Wednesday 30 September 2026 / Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/nath26_interspeech.pdf

## 问题
阿萨姆语据称有后接闭元音触发的中元音抬高和谐，但超声证据混杂、跨方言系统声学证据不足。

## 方法
COCAS 语料 18 名成人（西/中/东三大方言区各 3 男 3 女，50–65 岁）。词表与自然会话中提取 /CECi/ vs /CECa/ 的 /E/（共 371 token），MFA 对齐+手工校正，Fast Track 提中点 F1/F2（Nearey1 归一化），LMEM 含和谐语境、时长、方言、语体、性别。

## 实验与结果
各方言与语体下 /CECi/ 的 F1 均显著低于 /CECa/（抬高约 111–156 Hz，均 p<.001），F2 亦更高（更靠前）。和谐效应普遍，但 F1 幅度随方言×语体三阶交互变化；语体对 F2 影响有限。方言差总体不大。

## 结论
三大方言区均有稳定的声学 /E/ 抬高（及靠前），支持跨方言中前元音和谐的语音现实；实现幅度非完全均一。

## 点评
用一致材料跨三大方言补上既往「标准变体+超声」缺口。仅测 /E/…/i/ vs /a/，未系统测 /u/ 触发或鼻音/辅音丛阻断，范畴性 vs 梯度性仍待后续。会话 token 较少，风格差异解释需谨慎。

