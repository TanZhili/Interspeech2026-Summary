# SoniSpeech: A Large-Scale Open-Vocabulary Tri-Modal Dataset for Wearable Silent Speech Interfaces

- 论文编号：1625
- 报告人：Ruidong Zhang
- 程序：Monday 28 September 2026 / Assistive Technologies 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/zhang26y_interspeech.pdf

## 问题
可穿戴静默语音接口要么开放词表但硬件侵入（电极/舌超声），要么形态友好但封闭小词表；缺大规模、公开、非接触声学传感数据支撑开放词表研究。

## 方法
发布 SoniSpeech：眼镜式 FMCW 超声（18–28/29–39 kHz）+ 可听音频 + 正面视频，三模态严格同步；发声与静默双模式、内容平行。语料取自 SODA 当代对话英语（归一化、5–25 词），单说话人约 34.1 h、18,000 句、5,356 词型、全 ARPABET 音素。基线：4 通道差分 echo profile（200 Hz）→ ResNet-34 + CTC + SentencePiece 1k。

## 实验与结果
首个开放词表声学传感静默识别基准：发声+静默联合训练在静默测试达 26.3% WER（静默-only 约 33.7%）；发声测试约 15.8%。数据规模上升 WER 持续下降。跨模态评测显示超声回波可承载语音信息。

## 结论
作者认为该数据集打破可穿戴 SSI 的词表瓶颈，证明开放词表静默识别在眼戴声学传感上可行，并提供基线与三模态扩展方向。

## 点评
贡献主要是基础设施：形态、规模与当代口语语料选择到位。单说话人限制泛化；26.3% WER 仍有较大空间，但作为“可解性”证明足够。发声–静默联合训练收益说明共享运动模式可迁移。
