# Building Tailored Speech Recognizers for Japanese Speaking Assessment

- 论文编号：1672
- 报告人：Yotaro Kubo
- 程序：Tuesday 29 September 2026 / Prosody, Pronunciation and Specialized Speech Processing
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kubo26_interspeech.pdf

## 问题
日语口语评估需要带音高重音标记的音位转写，以保留误重音、误读等说话人错误；通用 ASR/多语语音转写会因语言模型“规范化”抹掉这些错误。CSJ core 中带手标重音的数据仅约 45 小时（训练约 2.3 万句），远小于全量 CSJ，数据稀疏。

## 方法
流式可部署架构：去掉量化的预训练 Mimi 语音编码器 + 随机初始化因果 Llama-2 风格 Transformer（d=512，24 层，8 头）上的多任务 CTC。(1) 音位字母（PA，片假名+重音撇号，243 token）；(2) 正字法字符 TT（2309 token，可用无重音的 noncore）；(3) Harvest 估计的 fo 轨迹 10 类分类。任务权重 PA/TT/fo=0.3/0.6/0.1。解码用 lattice fusion：由 PA/TT 的 CTC 混淆网络经 blank 去除得格子；TT 格子经 UniDic 发音词典 FST 转为 PA 格子并与 PA 格子按发音权重归一化后取并，再最短路径。对比显式 conditioning、Whisper/TT-only 作外部 TT 源等变体。选用 CTC 以尽量少做错误纠正。

## 实验与结果
主评测 CSJ core eval1/2/3，外加 JSUT basic5000。含重音的平均 mora-label 错误率：从 PA-only 约 12.3% 量级降到完整方法约 7.1%（摘要）；Table 1 中 MT+LF 在 eval1–3 含重音分别为 7.0/7.7/9.1，优于 Whisper†、Multipa† 与 PA-only。多任务主要得益于 TT+noncore；单独 fo 帮助有限，与 TT 合用有增益。JSUT 上 TT 不准时 fusion 帮助变弱，换 Whisper 作 TT 源可改善。Whisper 在 CSJ 上 CER 高、倾向忽略说话人错误，在无错误朗读 JSUT 上则很强。

## 结论
多任务利用廉价正字法标注与 fo，再经 FST 融合 PA 与词典诱导的 PA 分布，可在稀疏重音标注下做出更准确的日语音位+重音识别，优于通用多语系统。相对优势取决于 TT 源质量与领域是否匹配。

## 点评
问题设定抓住了“评估向 ASR 不能规范化”这一关键冲突，CTC+多任务+词典融合是针对小标注、要保留错误的务实组合。脆弱点在于词典路径会把 TT 错误或规范发音偏好注入 PA，自发语与朗读外域表现分化；fo 辅助本身弱，说明音高重音仍主要靠稀缺 PA 监督。
