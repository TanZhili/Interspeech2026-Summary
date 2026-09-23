# Prominence, Stress and Focus

- 日期：Tuesday 29 September 2026；时间：16:30-18:30；形式：Oral；Area：2；论文数：6
- 材料：官方程序摘要。仅依据摘要归纳，不补写摘要未给出的数字或机制。

## 技术趋势

本场从可解释的无文本突显检测到跨年龄、双语与跨语言感知，再延伸到方言语调类型学与机器人 TTS 韵律期望。一条技术线把心理声学原则直接编进极小参数检测器；多条实验线则检验焦点的 F0 模式是否随年龄、L1 有无 post-focus compression 而变化。

感知研究用陌生语言刺激剥离词汇/语用因素，显示突显与 IP 边界线索的非普遍性。Venetan 宽焦点升调与机器人嗓音“更像机器反而更易听出逗号边界”的结果，共同说明：韵律范畴与听者期望强烈互动，不能假设单一普遍线索层级。

## 技术内容

### 突显检测与焦点产出

**Auditory Contrast Network for Text-Free Prominence Detection**（论文 250；Kosuke Shimizu）ACN 至多 238 可训练参数，编码成对对比、线索独立与前向主导；仅用三声学特征、无文本。跨语料迁移 r=0.412，匹配冻结 wav2vec2（r=0.409）且延迟低约 120×；加文本升至 0.451。学到权重显示前向主导、±1 词局部性，以及时长>能量>频谱≫F0 的线索层级。

**F0 realization of prosodic focus across adulthood in Jianghuai Mandarin**（论文 255；Xinxian Zhao）江淮官话青/中/老三组产出中性与三类窄焦点。全局三区 F0 模式跨年龄大体保留；细粒度上老年说话人相对青年/中年在平均 F0 上显示更大的焦点后压缩。

**Prosodic Realization of Focus in Yi-Mandarin Bilingual Speakers: On-Focus Expansion without Post-Focus Compression**（论文 660；Ziyu Zhang）彝语缺 PFC、北京官话有 PFC。彝—汉双语者在 L2 普通话上焦点上 F0 扩展可比北京对照组，但各位置焦点后 F0/强度均无压缩；个体普通话背景不预测焦点后 F0，支持焦点上扩展与 PFC 为相对独立模块。

### 跨语言感知、方言语调与机器人嗓音期望

**The (non-)universality of prominence and Intonation Phrases: German and Hungarian listeners' perception of an unfamiliar language**（论文 707；Farhat Jabeen）向德语与匈牙利语听者播放乌尔都语片段做 Rapid Prosody Transcription。两组依赖不同 F0 轮廓与标度感知突显，IP 边界识别的评分者间/内一致性也有差异，显示线索非普遍。

**Broad Focus Rise(-fall) Declaratives in Venetan: Investigating Typological Outliers in Italo-Romance Intonation**（论文 2691；Elinor Payne）在 gambellarese 半自发宽焦点陈述中，升（降）调与降调大致同样常见，且不论词重音位置，指示存在有别于意大利语常见 H+L* L% 的无标记升核调；并考察词末重音对升（降）调对齐的语音效应。

**Should Robots Sound more like Machines than like Humans? User Expectations Affect the Perception of Prosody in TTS Voices**（论文 3075；Ha Eun Shim）机器人形象听辨中，情感化或单调音高对可懂度影响很小；使嗓音更机器化（音段上与该韵律对立无关）反而提高带逗号句的可懂度，暗示机器嗓音期望可偏置听者对韵律边界的感知。

## 本场要点

- 极小可解释 ACN 可用无文本声学特征逼近大模型突显相关。
- 江淮官话焦点全局 F0 稳、细粒度随年龄变；彝—汉双语显示 PFC 可不随 L2 获得。
- 陌生语言感知实验支持突显/IP 线索的非普遍性。
- Venetan 宽焦点升调构成 Italo-Romance 类型学例外候选。
- 机器人 TTS 的“机器感”可改变听者对韵律边界的期望与可懂度。

## 覆盖核对

| id | title |
|---|---|
| 250 | Auditory Contrast Network for Text-Free Prominence Detection |
| 255 | F0 realization of prosodic focus across adulthood in Jianghuai Mandarin |
| 660 | Prosodic Realization of Focus in Yi-Mandarin Bilingual Speakers: On-Focus Expansion without Post-Focus Compression |
| 707 | The (non-)universality of prominence and Intonation Phrases: German and Hungarian listeners' perception of an unfamiliar language |
| 2691 | Broad Focus Rise(-fall) Declaratives in Venetan: Investigating Typological Outliers in Italo-Romance Intonation |
| 3075 | Should Robots Sound more like Machines than like Humans? User Expectations Affect the Perception of Prosody in TTS Voices |
