# Indigenising Speech Technology: Building a TTS Model for te Reo Māori

- 论文编号：1443
- 报告人：Gianna Leoni
- 程序：Tuesday 29 September 2026 / Indigenous Voices in Speech Science and Technology
- 技术分类键：community
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/leoni26_interspeech.pdf

## 问题
主流 TTS 对毛利语等原住民语言质量差，公开语料常忽视正字/语音特点与说话人多样性；新西兰设备上亦无合适 Māori 或新西兰英语/双语声线。作者主张：精心策展的少量高质量数据可优于“越多越好”。

## 方法
Te Hiku Media 主导的数据主权流程：经 whakawhanaungatanga 获文本授权；内部语言专家人工校句、标长音、切句；族内广播员作男声、再扩女声。录制约男 24 小时（约 11h Māori + 13h 英语）、女 8+ 小时（约 3h Māori + 5h 英语）。质量保证含逐条听审与重录/改文本。训练沿用先前工作：IPA 音素化、借西班牙语预训练（语音相近）、男女微调。自建 90 句 Māori 基准与 100 句双语语码转换基准，由专家听评元音辅音、音高韵律与自然度。

## 实验与结果
无公开 WER/MOS 表；迭代以专家主观对照报告驱动，早期有机械切分感，后期更近母语流畅度；专名与稀有音、数字/缩写仍为难点，靠补录闭环。强调主观、文化恰当评测优于通用基准。

## 结论
原住民主导的策展、同意与部署控制可做出高质 Māori TTS 基础；质量与伦理优先于数据量。

## 点评
把数据主权写进工程全流程，比再刷架构更切原住民语境。强在基准自建与失败模式闭环；弱在定量指标少、模型细节指向前作，外部可复现性有限。
