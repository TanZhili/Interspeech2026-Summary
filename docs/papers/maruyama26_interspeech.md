# Real-Time CARFAC/SAI-derived Pitchogram for Seeing and Correcting Pronunciation in Mandarin Chinese Tones

- 论文编号：3575
- 报告人：Yuka Maruyama
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/maruyama26_interspeech.pdf

## 问题
普通话四声学习中，传统频谱图时间细结构变化快，初学者难实时解读；需更稳定的音高可视化 CAPT。

## 方法
用 Google CARFAC/SAI 生成 pitchogram。感知原型：听参考+看图选调；产出原型：双屏实时自语音图 vs Google TTS 参考图对照。16 kHz、约 28 ms 帧；默认 22 个 HSK1–2 词，可手动扩词表。Windows 命令行、单键切换，无需校准。

## 实验与结果
演示系统，无正式用户学习效果统计；作者主张 pitchogram 有助直观感知与纠正四声。

## 结论
CARFAC/SAI pitchogram 可作为声调 CAPT 的可行可视化组件；未来可自动扩词表与加文本反馈，并扩展到其他声调语言。

## 点评
替代 mel 谱做实时对照，思路直观、门槛低；尚缺对照实验证明优于频谱图，词汇规模也偏小。
