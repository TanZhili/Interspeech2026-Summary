# Prosodic ABX: A Language-Agnostic Method for Measuring Prosodic Contrast in Speech Representations

- 论文编号：478
- 报告人：Haitong Sun
- 程序：Monday 28 September 2026 / From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/sun26_interspeech.pdf

## 问题
自监督语音表示对音位对比敏感已有 ABX 评测，但对重音、音高等韵律对比是否在表示几何中突出，尚缺直接、少标注的度量。分类探测需标签与训练，且均值池化会抹掉时变韵律。

## 方法
**Prosodic ABX**：构造音位相同、韵律不同的最小对 \(A,B\)，及另一说话人同韵律样本 \(X\)；编码后用 DTW 比 \(d(R_A,R_X)\) 与 \(d(R_B,R_X)\)，正确则得分 1，报告错误率。构建英语词重音、日语音高重音录音最小对（并含 TTS 合成），Mandarin 用 MCAE 声调对。评 17 个 S3M 全层及 mel/MFCC；并做人听 ABX。

## 实验与结果
S3M 远优于随机与声学基线；英语重音上最差 S3M 仍优于人（约 26% vs 29% 错误），日语/普通话人优于最佳模型（9% vs 19%；2% vs 5%）。英语词级人–模型错误相关 \(r=0.94\)。TTS 作层选择代理：日/中层相关 \(r\approx0.93\)，英语较弱。上下文内比上下文外更好（中位 \(\Delta\) 9.4%），层/模型排序高度相关。三语任务错误率彼此相关，提示共享 F0 等线索。

## 结论
韵律 ABX 可无训练地度量词汇韵律在表示中的突出度；结果跨合成语音、上下文内外与任务常稳健，适合低资源选模型与层。

## 点评
把音位 ABX 扩到韵律并用 DTW 保留轮廓，比探测分类更贴“几何突出度”问题，且数据集公开有实用价值。脆弱点：英语合成语音代理不稳、最小对规模有限（英/日）、与下游聚类/发音反馈的因果链仍需验证。
