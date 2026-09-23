# Discrete vs. Continuous: A Comprehensive Study of Unified Audio Understanding in LALMs

- 论文编号：2074
- 报告人：Jing Peng
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/peng26h_interspeech.pdf

## 问题
LALM 里连续特征与离散 token 并存，但既有对比常偏语音、在 LLM 外评估，或忽视声学离散表示与规模效应。需要弄清：对统一音频理解（speech / sound / music），哪类表示更合适，以及 backbone 放大能否弥补前端信息损失。

## 方法
提出 UniARC（基于 XARES-LLM）：音频嵌入接任务 prompt，在统一 seq2seq 指令框架下评测。两种策略：(1) SmolLM2-135M/360M + LoRA 参数高效微调；(2) Llama-3-1B/8B 冻结 backbone，两层 MLP 投影器 + 10-frame 时序拼接做探测。连续编码器含 HuBERT、WavLM、Wav2Vec 2.0、Whisper；离散含 K-means（1000 中心）聚类 token，以及 DAC、WavTokenizer、带语义蒸馏的 SpeechTokenizer。离散索引再映回 codebook 嵌入，与连续表示统一经投影器对齐 LLM。

## 实验与结果
任务覆盖 ASR、意图、情感、说话人/语言识别、环境与事件、caption、音乐流派/乐器等（LibriSpeech、SLURP、CREMA-D、ESC-50、GTZAN、Clotho 等，见表 1）。正文可读部分给出的核心结论：理解任务上编码器效力主要由语义信息丰富度决定；带强语义约束的离散 token 可超过连续特征，而偏重信号重建的高保真表示常在理解任务上失败；放大语言 backbone 难以补偿前端表示不足，前端往往设定性能天花板。抽取全文后半（结果表与分析）出现大量乱码，具体数值表无法可靠读取。

## 结论
作者主张：语义兼容性优先于单纯声学保真或盲目放大 LLM；并给出在语义密度、保真度与效率之间取舍的实践指引。更细的定量对比因抽取损坏未能完整复述。

## 点评
这是表示范式 × 模型规模 × 数据量的系统评测，抓的是「前端语义密度是否构成 LALM 理解上限」。设计上把连续/离散都投影到同一指令框架，便于公平比较。正文后半 OCR/抽取严重乱码，点评只能依赖摘要与方法段的定性主张；若需精确数字应回查 PDF。可能脆弱处在：冻结探测与 LoRA 设定会放大/缩小不同编码器差距，且 codec 采样率等实现细节也会影响结论外推。
