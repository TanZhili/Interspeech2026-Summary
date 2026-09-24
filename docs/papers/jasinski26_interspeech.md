# From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection

- 论文编号：338
- 报告人：Jan Jasiński
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/jasinski26_interspeech.pdf

## 问题
ASR 幻觉（流畅但与音频无关的转录）会拖垮下游系统，但传统 WER 等指标难以把它与普通误听区分开。现有文本指标多依赖参考转写，参考无关指标与 LLM 检测在部署场景下效果有限；真实语音上的人工标注数据也长期不足。

## 方法
在 HALAS 数据集上对 Whisper large v3 做话语级幻觉检测，比较三类范式并做融合：
1. **文本指标**：oracle（WER/CER/IER、BERTScore、SeMaScore、CHP 等）与 reference-free（CPS、PPL、对齐置信度、NCHP 等），用 Logistic Regression / Random Forest / XGBoost 分类。
2. **LLM**：以 GPT-4o mini、Gemini 系列零样本提示为基线，逐步加入更强推理模型、Whisper 非语音幻觉病理、few-shot，并尝试去掉参考转写。
3. **解码器内部状态**：对 Whisper 各层解码序列做 mean/max pooling 与 BLSTM 探测（自注意力 / 交叉注意力 / 最终输出，可加序列差分）。
4. **晚融合**：用 XGBoost 与 BLSTM 的 OOF 概率加音频时长，训练 Logistic Regression 元分类器。

## 实验与结果
数据为 HALAS（Earnings-22 上 Whisper large v3：858/3611 为幻觉）。主要数字：
- 单特征 AUC：oracle BERT 82.3%、CER 81.9%；reference-free 最强 CPS 68.2%。
- 文本分类：XGBoost 全特征 F1 62.8%；仅 reference-free 降至 37.7%。
- LLM：最佳 oracle 配置 F1 58.7%；reference-free 降至 32.8%，仍不如轻量 XGBoost。
- 内部状态：中间层线性可分性约 AUC 81–82%；最优 BLSTM（参考无关）AUC 87.6%、F1 65.5%。
- 晚融合：Acc 90.7%、F1 68.3%、AUC 90.0%，优于单一范式。

## 结论
幻觉信号在 Whisper 解码中间层被编码；参考无关的内部状态探测可超过依赖参考的文本/LLM 方法。文本与内部状态部分互补，晚融合达到最佳整体检测效果。三类方法对单功能词插入类幻觉仍普遍失效。

## 点评
工作把“有没有参考转写”这一部署约束放在中心：oracle 文本特征看起来强，但一旦去掉参考就崩；内部状态探测绕开了这一瓶颈，且不引入 LLM 的延迟。晚融合说明两类错误不完全重叠，但元分类器仍依赖音频时长等弱路由信号，单字幻觉仍需声学侧信息。
