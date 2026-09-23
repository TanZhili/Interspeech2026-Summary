# DiFlow-TTS: Compact and Low-Latency Zero-Shot Text-to-Speech with Discrete Flow Matching

- 论文编号：1043
- 报告人：Son Nguyen
- 程序：Monday 28 September 2026 / Text-to-Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26d_interspeech.pdf

## 问题
零样本 TTS 中 AR 延迟高，连续流匹配空间复杂；离散扩散训练与采样配置强耦合。需要在因子化编解码离散空间做更灵活的离散流匹配。

## 方法
DiFlow-TTS：以预训练 FACodec 得韵律/内容/声学离散码与说话人嵌入。Phoneme-Content Mapper 将音素对齐到内容码并产内容嵌入；Factorized Discrete Flow Denoiser 在离散流匹配框架下用分头同时预测韵律与声学概率速度，条件于内容嵌入与参考提示的韵律/声学/说话人。PCM 确定性，流去噪器并行生成多属性。

## 实验与结果
作者报告相对基线在自然度、内容准确与韵律保持上有竞争力，模型可小至约 11.7×，推理加速可达约 34×（摘要/贡献声明）。作为 DFM 应用于因子化语音码的首批框架之一。

## 结论
作者认为在因子化离散码上做离散流匹配是可行的紧凑低时延零样本 TTS 方向，并提供分属性速度场分解设计。

## 点评
相对连续 FM，离散有限支撑降低优化难度；分头建模韵律/声学是相对同质 DFM 的关键扩展。正文抽取后半数字表不完整，规模与对比细节以作者声明为主；强依赖 FACodec 解耦质量。
