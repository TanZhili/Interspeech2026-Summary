# YUE-PUB-Speech: A Speech-based Pragmatic Understanding Benchmark for Cantonese

- 论文编号：289
- 报告人：Ziwei Gong
- 程序：Wednesday 30 September 2026 / Behavioral, Cross-lingual, and Multimodal Speech Analysis
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/wen26b_interspeech.pdf

## 问题
语用理解依赖会话隐含义与韵律线索，但既有基准多为纯文本；粤语等低资源语言缺少对齐的文本–语音语用评测资源。

## 方法
基于 PUB 选取语用丰富实例，译为粤语并经人工校验，由 4 名母语者录音，得约 10.87 小时配对数据（1680 对话规模）、统一多选 QA，覆盖隐含义、预设、指称等。基准文本/音频单模态、文本–音频特征拼接（含 openSMILE）与音频语言模型。

## 实验与结果
加入语音相对纯文本提升语用理解；纯音频落后，说明需语义内容+语音线索。SFT 对粤语会话准则对齐关键约 10%（隐含义）。预设类最难；Gemini-2.5-Pro 等多模态在预设/指称上较强（指称峰值约 82.50%）；隐含义上 openSMILE 拼接有效。

## 结论
发布首个粤语多模态语用基准，表明语音信号对低资源语用推理有增益，并提供跨范式比较测试床。

## 点评
把 PUB 式语用推理带入口语粤语，填补「转写对了仍听不懂用意」评测空白。翻译–录音链路可能损失原语文化语用细微差别；多选格式便于评分但压缩真实开放推理。预设最难符合其依赖未陈述前提的本质。
