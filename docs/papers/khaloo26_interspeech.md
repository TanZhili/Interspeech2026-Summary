# Perceptual and Acoustic Correlates of Racial Identity in Text-to-Speech Voices

- 论文编号：1479
- 报告人：Noah Khaloo
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/khaloo26_interspeech.pdf

## 问题
TTS 日益像人，听者能否从全合成语音感知种族身份、是否伴随人格刻板印象，以及 Black/White 标签对应的声学相关物是什么；既往对合成语音存在偏“听成白人”的报告。

## 方法
EasyPeasy AI 合成 32 个英语音色（平台标注 Black/White × Male/Female 各 8）。144 名美国英语听者（Prolific）：人格块对 16 个声音评 6 维人格 + 像人程度；种族块对另 16 个声音做种族等多选（刺激避开 AAE 形态音系线索，只留音质/元音质量）。用 %Reported Black 的 k-means 得感知标签（White / Black / Ambiguous）。VoiceSauce 提 F0、F1–F4、Residual H1*、谱倾斜谐波、CPP 等，XGBoost 在男性感知标签上做 Black vs White 分类。

## 实验与结果
性别平台标签与听者一致很高（男 98.6%、女 93.6%）。种族聚类显示偏 White 的评定偏向；Ambiguous 中多数为平台 Black Female。男性感知为 Black 的声音在愉快、专业、可信、能力上显著更低；女性无显著种族效应。像人程度正向预测各人格维。声学：全特征 CV 准确率约 65%，顶 15 特征约 66%；Black 评定声音 Residual H1*、CPP、部分高/低频谐波倾斜更低，F4 更高；F1/F2 在部分元音上有局部差。

## 结论
听者能从合成语音中形成种族感知，但偏向评成 White；稳定评成 Black 的男性声音人格评分更低。现代 TTS 可编码与 MAE/AAE 相关的细粒度声学差异；开发与部署需警惕刻板印象的社会后果。

## 点评
感知标签（非平台标签）+ 可解释声学特征 + 人格联动，比只问“像不像某一种族”更完整。65% 分类准确率不算高，但 top 特征与 Residual H1* 主导模式仍有语音学解释。女性效应弱、Ambiguous 偏 Black Female，说明性别×种族交互是部署合成语音时的敏感点。
