# Spashta Audio-Bench: Unified ASR and TTS Evaluation Framework across Indian Languages

- 论文编号：1777
- 报告人：Bikash Dutta
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dutta26_interspeech.pdf

## 问题
印度语言语音评测碎片化：模型在互不重叠的数据集上、用不一致的预处理与指标评测，难以复现与公平比较；TTS 又常只看主观自然度，掩盖可懂度失败。

## 方法
Spashta Audio-Bench 做成类 HuggingFace Evaluate 的可插拔框架：数据层接入公开测试集，预处理统一 16 kHz 单声道与 UTF-8 小写去标点，模型层注册 ASR/TTS checkpoint，评分引擎多指标汇总并出排行榜。ASR 报 WER/CER；TTS 用 IndicConformer 作 oracle 算 TTS→ASR 退化（可懂度），并报 FAD、DNSMOS/P.808 预测 MOS。在七个语料（IndicTTS、IndicVoices/R、RASA、Nirantar、OpenSLR、SVARAH 等，至多 22 语 + 印度口音英语，累计约 644 小时评测音频）上评十个开源 ASR/TTS，均用公开权重、不加微调。

## 实验与结果
ASR：无单一架构通吃——如 AudioX-S 在 IndicTTS WER 26.74% 优于 IndicConformer 31.58%，AudioX-N 在 RASA 最强（20.90%）；同语言跨数据集 WER 可差逾 30 点；低资源语（如 Maithili 58.29%、Dogri 56.71%）远差于 Hindi 23.76%，Urdu 最低 9.38%。TTS：自然度与可懂度脱节——Parler 预测 MOS 约 4.13–4.15 但 TTS→ASR WER 非最低；MMS-TTS 可懂度最好（WER 36.14%、CER 9.60%）而 pMOS 相对较低；Veena FAD 最低（IndicTTS 3.52）但 TTS→ASR WER 最高（53.79%）。讨论强调参数放大不保证跨语鲁棒，领域敏感与架构归纳偏置仍关键。

## 结论
作者认为模块化统一评测能暴露单数据集、单指标看不见的结构问题，并释放可复用基础设施，使多指标评测成为印度语言低资源语音的默认做法。

## 点评
贡献在评测基础设施与“TTS 可懂度–自然度双轴”，而非新识别/合成模型。用 IndicConformer 作 TTS oracle 实用但会把 oracle 偏差带进可懂度排序；预测 MOS 对印度语语音学校准不足也是正文自承的限制。
