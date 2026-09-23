# Speaker-Specific, Forensic and Segmental Characteristics of Typical and Atypical Speech

- 日期：Wednesday 30 September 2026
- 时间：14:00-16:00
- 形式：Poster（Area 2 - Poster 5）
- Area：2
- 论文数：8
- 材料：官方程序摘要（[Program](https://interspeech2026.org/en-AU/pages/program/program)；[ISCA Archive](https://www.isca-archive.org/interspeech_2026/index.html)）。声学与法医数字仅出自摘要。

## 技术趋势

本场海报横跨发音语音学、法医说话人比对、双语节奏、方言音变、体位对共振峰影响、儿童擦音位置变异、痴呆检测隐私，以及阿萨姆语元音和谐。共同线索是：说话人特异信息存在于哪些频段/时间组织，以及如何在临床或取证场景中与音段描写对读。

发音与音变侧用超声动态分析喉位与舌背姿态解释美式英语软腭塞音；新西兰英语在奥克兰百年材料中重估短前元音漂移，并检验仰卧/坐/站对 F1/F2 的小幅但系统性影响；波兰儿童规范 /s/ 显示词首—词中光谱差异最大；阿萨姆语跨三大方言区确认和谐语境中 /ɛ/ 抬高。

法医与应用侧，带限倒谱（BLCC）扫描显示约 0–0.6 kHz 与 4–6 kHz 说话人区分力强、约 7 kHz 以上最弱；双语政治演讲中辅音节奏更保留说话人签名、元音节奏更随语言变化。痴呆检测则用信号级关键词对齐扰动与特征级对抗/互信息噪声，在近随机说话人识别下保持分类效用。

## 技术内容

### 发音姿态、方言音变与位置/体位效应

**The Role of Laryngeal Position in the Articulation of American English Velar Stop Consonants**（论文 207；presenter：Daejin Kim）  
用超声与多元统计把舌骨（HY）与舌背（TD）建模为发音姿态。TD 达目标时 /k/ 伴 HY 上升前移、/ɡ/ 伴下降后缩，并分别与后续/前接元音高低 f0 峰相关；/ɡ/ 的 TD 抬升更长、更大、更快，表明充分时空扩展与最大舌—软腭接触。结论：舌扩展程度、接触与喉位共同制约 AE 软腭塞音及其声学相关。

**Revisiting the NZE front vowel shift: evidence from New Zealand's largest and most linguistically diverse city**（论文 1526；presenter：Brooke Ross）  
对奥克兰当代说话人（n=67，两组年龄）与历史说话人（n=8）做 /e, æ, ɪ/ 百年音变的初步声学与统计分析。结果显示 /e/ 与 /æ/ 先升后降，历史说话人已出现 /ɪ/ 央化，与既往轨迹叙述不同；进一步分析提示 /ɪ/ 央化最初受相邻边音音系条件制约。

**Effects of body position on vowel formants in New Zealand English**（论文 1545；presenter：Qing Guan）  
9 名说话人 within-speaker /hVd/（11 元音）比较仰卧、坐、站。线性混合效应显示体位差异总体较小，最清晰对比涉及仰卧相对坐/站；效应随元音、年龄、性别变化，F2 在部分高前元音更显著，F1 体位差在女性更清晰。建议跨录音配置解释共振峰时记录体位。

**From onset to coda: spectral variation in normative Polish /s/ produced by children**（论文 1936；presenter：Oliwia Skórzewska）  
102 名 5–8 岁儿童、816 个规范 /s/：词位显著影响 CoG、偏度、峰度、spectral flux；词首—词中成对差异最强，词中—词尾大多较小且常不显著（偏度除外）。

**An Acoustic Investigation of Mid Front Vowel Harmony in Assamese**（论文 3034；presenter：Saurabh Nath）  
18 名成人（三大方言区各 3 男 3 女）词表与连贯言语；混合效应模型显示和谐语境下 /ɛ/ 抬高跨方言一致，但效应幅度随方言—语体组合变化，尤其在 F1（舌高）。

### 法医频带、双语节奏与隐私—诊断

**Band-Limited Cepstral Analysis of Speaker Sensitivity in Forensic Voice Comparison**（论文 1028；presenter：Shunichi Ishihara）  
162 名澳大利亚英语男性母语者约 30 秒连贯言语；0–8 kHz 以 0.6/1.2 kHz 子带扫描 BLCC，做似然比法医比对。各子带均含有用信息，约 7 kHz 以上最不具信息，0–0.6 kHz 与 4–6 kHz 提供强说话人区分线索。

**Speaker-Specific and Language-Dependent Temporal Organization in Bilingual Political Speech**（论文 1335；presenter：Nina Hosseini-Kivanani）  
10 名政治家卢森堡语/法语共 400 句；辅音节奏指标保留说话人签名，元音指标主要由语言驱动；法语元音与元音区间更长且更可变，辅音时序差较小；未见稳健语言×性别交互。

**Multi-Level Privacy-Preserving Dementia Detection from Speech via Targeted Adversarial Obfuscation and Representation Learning**（论文 2868；presenter：Henriette Flore Kenne）  
信号级 Cumulative Signal Attack 在关键词对齐区集中扰动使 WER=1.00 并保留韵律生物标志；特征级 GRL+互信息引导噪声抑制说话人维度。DementiaBank Pitt 上说话人识别近随机（EER=0.59，F1=0.003），痴呆分类 F1=0.78、AUC=0.86。

## 本场要点

- 软腭塞音需同时考虑舌扩展、接触与喉位及其 f0 相关。
- 法医 BLCC 指出低频与 4–6 kHz 为强说话人区，极高频信息最弱。
- 双语政治演讲中辅音/元音节奏分别偏说话人与语言驱动。
- 奥克兰材料提示 NZE 短前元音轨迹与既往叙述需修订。
- 体位与词位对共振峰/擦音光谱有小但系统性影响，应在方法学中记录。
- 痴呆检测可通过多级扰动在强隐私下保留诊断效用。

## 覆盖核对

| 论文 id | 标题 |
| --- | --- |
| 207 | The Role of Laryngeal Position in the Articulation of American English Velar Stop Consonants |
| 1028 | Band-Limited Cepstral Analysis of Speaker Sensitivity in Forensic Voice Comparison |
| 1335 | Speaker-Specific and Language-Dependent Temporal Organization in Bilingual Political Speech |
| 1526 | Revisiting the NZE front vowel shift: evidence from New Zealand's largest and most linguistically diverse city |
| 1545 | Effects of body position on vowel formants in New Zealand English |
| 1936 | From onset to coda: spectral variation in normative Polish /s/ produced by children |
| 2868 | Multi-Level Privacy-Preserving Dementia Detection from Speech via Targeted Adversarial Obfuscation and Representation Learning |
| 3034 | An Acoustic Investigation of Mid Front Vowel Harmony in Assamese |
