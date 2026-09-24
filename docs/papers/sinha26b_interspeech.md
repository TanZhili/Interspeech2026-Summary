# Error Diversity and Performance Variability in Zero-Shot Children's Speech Recognition

- 论文编号：2666
- 报告人：Abhijit Sinha
- 程序：Wednesday 30 September 2026 / Robust ASR: Hallucinations and Biases
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/sinha26b_interspeech.pdf

## 问题
成人预训练 SSL 零样本迁到儿童语音时，常只比全局 WER；相近 WER 是否对应相似错误结构、层是否句级最优、错误能否被 LLM 纠正，仍不清楚。

## 方法
冻结 Wav2Vec2/HuBERT/Data2Vec Large 各层，作 Kaldi DNN-HMM 声学特征；仅用成人数据训（英：WSJCAM0；美：Mini LibriSpeech），测 PFSTAR 与 CMU Kids。分析 S/D/I 比例；句级 oracle 选最低 WER 层；用 Mistral-7B-Instruct（零样本与 LoRA 文本微调）做后处理纠错。

## 实验与结果
PFSTAR 最优 WER 约 5.15–5.69%，层间跨度可达 9–13%；CMU Kids 最优约 21–22%，最差可至 86%。PFSTAR 插入相对更多，CMU Kids 替换主导；成人 WSJCAM 几乎无插入。LLM 纠错几乎不改假设；LoRA 文本微调反而恶化。Oracle 增益：PFSTAR 约 1.3–1.6%，CMU Kids 约 5–6%，且不稳定性高 4–6 倍。

## 结论
相近最优 WER 掩盖层间错误结构差异；域差越大层互补越重要；儿童零样本错误主因是声学表征而非可文本修补的语言不一致。

## 点评
把「选一层」拆成错误结构/句级 oracle/可恢复性三条轴，比刷表更有设计含义。LLM 几乎无效强化了「先改声学」的结论；CMU Kids 高不稳定性是自适应层选择的直接动机。
