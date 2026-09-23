# Read What You Hear: Reference-Free Hypotheses Evaluation with Acoustic Discrepancy

- 论文编号：3434
- 报告人：Zhihan Li
- 程序：Monday 28 September 2026 / Spoken Language Processing: Evaluation and Metrics
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/li26ka_interspeech.pdf

## 问题
无参考文本时评估 ASR 假设常靠内部置信度（易过自信）或纯语言模型复打分（忽略声学）；需一种无训练、强调声学接地、且能定位局部错误的参考无关度量，并用于假设精炼。

## 方法
READ：用现成自回归离散 TTS（CosyVoice2）在 teacher-forcing 下算给定文本假设时语音 token 的条件负对数似然，得到与语音帧对齐的声学差异序列；从同一 TTS 注意力图用动态规划抽取单调对齐，把差异映射回文本片段。应用：(1) 句级 N-best 重排；(2) 按争议/共识区间做段级选优组合；(3) 把段级结果作为额外候选喂入 ROVER。无需针对 ASR/数据集再训练。

## 实验与结果
候选含 Whisper、NeMo、Qwen2.5-Omni 等；测试 LibriSpeech、SPGI、SWBD、TED、码混 ASRU/TALCS 及 WHAM! 加噪。READ 差分与 WER 相关，噪声越大相关越强。Whisper-large N-best 句级重排相对 top-1 可降相对错误率，最高约 20%+（如 SPGI −21.46%、TALCS −20.91%）。段级组合多数集优于单句选择；与 ROVER 结合稳定超原版 ROVER。低 SNR 下相对最优单系统与 ROVER 优势更明显。

## 结论
作者认为用 AR-TTS 似然作声学差异度量可无训练地评估与精炼假设，尤其在噪声场景更有效；局部性支持细粒度组合。

## 点评
把 Bayes 分解中长期被忽视的 P(speech|text) 用现代 TTS 重新落地，思路干净、可解释。依赖 TTS 声学包络与对齐质量，对替换/删插错误类型的分辨作者承认仍待探；段级贪婪合并在争议区过长时退化为句级。与 LLM 生成式纠错互补而非替代。
