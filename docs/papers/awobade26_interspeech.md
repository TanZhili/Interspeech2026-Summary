# AfriVox-v2: A Domain-Verticalized Benchmark for In-the-Wild African Speech Recognition

- 论文编号：3140
- 报告人：Busayo Awobade
- 程序：Wednesday 30 September 2026 / Translation
- 技术分类键：translation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/awobade26_interspeech.pdf

## 问题
非洲语言/口音在 ASR 基准上覆盖不足；既有评测偏朗读、域粗、模型过时，难反映噪声自发场景与垂直行业词汇（金融、医疗、农业等）及数字/命名实体风险。

## 方法
AfriVox-v2：聚合 Waxal、Africa Next Voices、新建 Intron-YT（公开多媒体自发对话，母语者转写+元审）等，约 14+ 语种；Gemini-3 多标签域标注（10 域含 Numbers/Named Entities），人工抽检（高精度语约 precision 42%/recall 70%）。评测 Omni-CTC 300M/1B/7B、Gemini 3 Flash、Sahara-v2；报告 WER、域条件 WER、EWER/NWER。

## 实验与结果
自发语音整体更难，但跨语种/模型变化不均。AfriVox-v2 平均 WER：Sahara-v2 最低 20.49，优于 Omni-CTC-7B 27.85 与 Gemini 3 Flash 26.59。域上电信/体育等错误更高；Sahara-v2 各域最低（如农业 16.11）。数字与实体仍难（最好约 NWER 20.32、EWER 23.11）。作者指出部分语种 v2 反优于 v1，可能反映训练数据重叠而非真泛化。

## 结论
域垂直与 in-the-wild 评测暴露平均 WER 掩盖的部署风险；区域优化模型可胜过更大通用模型。基准拟推动更包容的非洲语音 AI。

## 点评
把“野生对话 + 行业域 + 实体/数字”做成评测轴，比只比朗读 WER 更贴近落地。域标签噪声（precision 约 42%）使域结论宜作趋势；作者机构自研 Sahara-v2 虽称同条件评测，读者仍需关注利益冲突与数据重叠可能抬高分。覆盖仍只是非洲语言的一小部分。
