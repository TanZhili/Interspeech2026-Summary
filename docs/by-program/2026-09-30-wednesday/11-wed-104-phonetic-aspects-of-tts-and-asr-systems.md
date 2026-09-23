# Phonetic Aspects of TTS and ASR Systems

- 日期：Wednesday 30 September 2026
- 时间：09:00-11:00
- 形式：Poster
- Area：2
- 论文数：7
- 材料：官方程序摘要（https://interspeech2026.org/en-AU/pages/program/program ；https://www.isca-archive.org/interspeech_2026/index.html）。不补写摘要未给出的数字与细节。

## 技术趋势

本场从语音学角度审视 TTS/ASR：音高抬升伪装、合成语音的语调感知、熟悉度与情感韵律、粤语人机对话中的音位实现、合成嗓音的种族身份感知、多语语音学特征识别，以及发声努力调制策略对噪声稳健性与 ASR 的影响。共同主题是合成与交互系统改变了听者与说话人的语音学行为，并反作用于自动识别。

多篇工作用 AI 克隆/SVC 控制实验材料，比较自然与合成语音在相似度、语调与情感识别上的交互；熟悉度既可能是促进也可能是负担。法医与社会语音学延伸到 ASR 对意志性音高抬升的脆弱性，以及听者对合成嗓音种族标签的刻板印象与可测声学相关。表征侧 PhonoQ-2.0 直接预测帧级语音学特征向量；发声努力聚类显示说话人策略异质并系统影响 Whisper/Wav2Vec2 的 WER。

## 技术内容

### 音高、语调感知与熟悉度

**Assessing the effect of volitional and synthetic pitch raising in female speakers on automatic speaker recognition**（论文 444；Kirsty McDougall）  
意志性音高抬升作为法医伪装形式。谱 x-vector 比较默认与抬升音高：识别准确率下降且说话人间异质；表现最差者抬升条件中位 f0 最高、抬升幅度最大且 f0 行程有限。合成 f0 操纵试点证实说话人特异效应，但无法完全复现意志性抬升策略。

**Intonation Perception in Real and Synthetic Speech across Varying Familiarity Levels: A Pilot Study of Equivalence Assessment**（论文 996；Hanrui Zhou）  
用 SVC 生成合成嗓音，比较自然与合成在相似度感知与语调识别两实验。相似度准确率上语音类型与语调显著交互，疑问可能作说话人识别线索但受合成特征影响；语调识别准确率上语音类型与熟悉度显著交互。

**A barrier or a booster? Familiarity effects on Mandarin emotion prosody recognition using AI-powered voice cloning**（论文 1038；Feng Xu）  
普通话成人在人类 vs AI 嗓音与熟悉度条件下做情感识别，采集准确率、反应时与 HRV。摘要称人类嗓音准确率显著更高、加工更快；HRV 未显著区分条件，表明合成语音解码受自上而下社会认知门控。

### 对话音位调制、社会感知与语音学特征

**Modulation of Phonetic Realizations in Cantonese Dialogue with Human and AI Interlocutors**（论文 1194；Peggy Pik Ki Mok）  
17 名粤语母语者在 Wizard-of-Oz 下与人或 AI 进行中性/负面脚本对话。相对人际互动，AI 互动中目标词时长更短并出现特定声调差异；负面语境元音空间面积更大但情绪效应边缘。摘要称对话者身份效应比既往报道更细粒度。

**Perceptual and Acoustic Correlates of Racial Identity in Text-to-Speech Voices**（论文 1479；Noah Khaloo）  
听者可对合成语音形成种族感知并出现刻板印象，同时偏向把嗓音评为“White”。GBDT 用声学特征区分被评为 Black/White 的嗓音，准确率 65%；较低 Residual H1*、高低频谱倾斜及噪声与共振峰等在标签间可靠变化。

**Multilingual Phonological Feature Recognition with Self-Supervised Speech Models**（论文 2735；Abner Hernandez）  
PhonoQ-2.0 基于 SSL 直接预测每帧 22 维语音学特征向量（方式、元音品质、部位、清浊），并以方式条件门控保证音系一致。域内平均宏 F1 91.3%、域外 88.9%，相对强 CTC 音素基线平均分别 +8.8/+8.6；未见语言从 66.9% 升至 73.6%。

**Vocal Effort Modulation Strategies: A Cross-Corpus Taxonomy with Noise Robustness and ASR Implications**（论文 2747；Lubos Marcinek）  
对 AVID 50 名说话人四档努力拟合 F0、RMS、谱倾斜与语速斜率并 K-means，得到三类稳定策略。ANOVA 显著；校正 LOSO 分类准确率 96–98%。噪声可恢复性、法语 Lombard 复制与 Whisper/Wav2Vec2 的系统 WER 差异验证鲁棒性。

## 本场要点

- 意志性音高抬升降低 ASR 且效应高度说话人特异。
- 合成语音与熟悉度交互影响语调与情感韵律感知。
- 粤语人–AI 对话出现时长与声调层面的音位调制。
- 合成嗓音可触发种族感知与可测声学相关。
- 帧级语音学特征识别跨语优于音素再派生路径。
- 发声努力策略分型对噪声稳健性与 ASR WER 有系统影响。

## 覆盖核对

| id | title |
|---|---|
| 444 | Assessing the effect of volitional and synthetic pitch raising in female speakers on automatic speaker recognition |
| 996 | Intonation Perception in Real and Synthetic Speech across Varying Familiarity Levels: A Pilot Study of Equivalence Assessment |
| 1038 | A barrier or a booster? Familiarity effects on Mandarin emotion prosody recognition using AI-powered voice cloning |
| 1194 | Modulation of Phonetic Realizations in Cantonese Dialogue with Human and AI Interlocutors |
| 1479 | Perceptual and Acoustic Correlates of Racial Identity in Text-to-Speech Voices |
| 2735 | Multilingual Phonological Feature Recognition with Self-Supervised Speech Models |
| 2747 | Vocal Effort Modulation Strategies: A Cross-Corpus Taxonomy with Noise Robustness and ASR Implications |
