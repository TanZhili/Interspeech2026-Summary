# Bridging Languages and Modalities: Lightweight Cross-Lingual Text and Speech Summarization for Low-Resource Scenarios

- 论文编号：2655
- 报告人：Chaimae Chellaf
- 程序：Tuesday 29 September 2026 / Corpus Creation, Summerisation and Understanding
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/chellaf26_interspeech.pdf

## 问题
跨语言摘要需在另一种语言中压缩并重构语义；级联「翻译/ASR→摘要」易误差传播，低资源语音跨语言摘要资源尤为稀缺。现有端到端工作多偏高资源文本或高资源语对。

## 方法
统一轻量框架：文本经 BGE-M3 句向量、语音经与之对齐的 SENSE 话语嵌入；去掉 BARThez 编码器 token embed，改为句/话语级输入，经线性投影（GeLU）送入修改后的 seq2seq（SBARThez），解码器仍产出法语摘要。两阶段训练：先在 MLSUM 法语上用句嵌入适配；再按任务用文本或语音嵌入微调。嵌入模型冻结，仅训投影层与 seq2seq（约 140M 可训参数）。发布低资源语音评测集 ABT-SpeechSUM（亚美尼亚、布列塔尼、突尼斯阿拉伯语），由译文用 GPT-4o mini 合成法语摘要并人工抽检。

## 实验与结果
文本 CrossSum（X→FR）：高资源上级联常更强，但日语上 SBARThez 更优；多数低资源语上 SBARThez 超过级联与 mT5-large，且可训参数仅 140M（总约 700M）。语音：SBARThez-speech 在三种低资源语上 Rouge-L/BertScore 优于 Whisper 级联基线；仅用译文句嵌入训练的 SBARThez-text 跨模态评测语音时仍有竞争力，布列塔尼与亚美尼亚上可超过级联。Table 4 数值行在全文抽取中被截断，具体分数无法完整复述。

## 结论
语义对齐的句/话语嵌入可支撑低资源跨语言、跨模态摘要，且参数量显著小于十亿级级联；ABT-SpeechSUM 为该方向提供开放基准。

## 点评
把跨语言摘要做成「共享语义嵌入空间上的轻量解码」，避开 ASR/MT 级联，对无 MT 覆盖的语言尤其有意义。强在可训参数少与跨模态零资源迁移迹象；脆弱点在合成参考摘要、法语单目标、以及语音集规模很小（如 Breton 训练仅约 0.41h），自动指标提升未必等于事实保真。正文末表抽取不全，已在结果中标明。
