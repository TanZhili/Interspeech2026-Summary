# Do Machines Listen Like Humans? A Temporal Benchmark for Phonological Competition in End-to-End ASR

- 论文编号：401
- 报告人：Linkai Peng
- 程序：Monday 28 September 2026 / From Self-Supervised Pre-training to Phonetic Analysis of Speech Models
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/peng26_interspeech.pdf

## 问题
人类听辨是增量式的：词首 cohort 早竞争、韵脚 rhyme 晚竞争。不少工作把 ASR/LLM 当人类言语识别（HSR）模型，但未检验其词汇激活时间进程是否像人。假设：带 look-ahead 的非因果架构会偏离人类从过去到现在的竞争动态。

## 方法
构建时间基准：1,533 词、7 说话人合成/真人音频，训练小型端到端网络用 MSE 拟合每帧 word2vec 语义向量；用输出与目标/cohort/rhyme/无关词的余弦相似度轨迹，对照 Visual-World Paradigm 眼动固定比例，算点对点 RMSE/MAE。对比因果 vs 非因果 LSTM/CNN/RCNN/Transformer（参数量接近），并探测 wav2vec 2.0、HuBERT、Whisper 的 CTC/注意力词激活。

## 实验与结果
非因果模型词识别准确率更高（如 RCNN/ConvTransformer test Acc 0.84），但因果模型更贴近人类竞争时间进程（平均 RMSE/MAE 约 0.07/0.05 vs 0.22/0.14）：因果侧呈现早 cohort、晚 rhyme；多数非因果过早激活目标/韵脚、cohort 偏弱。有限 120 ms 前瞻的非因果 RCNN 介于中间。案例 “socket”：因果 RCNN 在 uniqueness point 压制 cohort、后升 rhyme；双向 LSTM 则从头就偏向目标。基础 ASR：wav2vec/HuBERT 激活偏晚（~400 ms，CTC 对齐），Whisper 竞争几乎平坦。

## 结论
时间因果性是类人增量竞争的必要架构约束；高转录精度不等于类人时间动态。大规模预训练不能单独保证类人加工，解释 ASR 为心理/神经模型需谨慎行为校验。

## 点评
把 VWP 时间进程做成可量化基准，直接分离“识别准”与“像人听”，对把 ASR 当认知模型的路线有清醒纠偏。局限作者已写明：词表小、孤立词、基础模型任务失配、词频/邻域未控。强在因果/非因果对照清晰，且显示仅看音素解码会高估非因果模型的类人程度。
