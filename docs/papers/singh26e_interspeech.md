# ProSarc: Prosody-Aware Sarcasm Recognition Framework via Temporal Prosodic Incongruity

- 论文编号：3451
- 报告人：Prathamjyot Singh
- 程序：Thursday 1 October 2026 / Emotion, Prosody, and Articulation
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/singh26e_interspeech.pdf

## 问题
口语讽刺大量依赖韵律，但既有音频方法多用句级统计或隐式时序编码，缺少把讽刺显式建模为“局部韵律动态相对全局情绪基线的不一致”。

## 方法
ProSarc 双路径：Global Emotion Encoder 用 librosa 提 10 维句级韵律统计 → MLP → pglobal；Temporal Prosody Encoder 用 Wav2Vec2/HuBERT/WavLM（仅微调最后两层）→ BiLSTM → 多头注意力 → 注意力池化得 plocal。Prosodic Incongruity Analyzer 由 [plocal;pglobal] 产生标量不一致分数 s，做自适应融合后再分类（加权 BCE）。用 at·dt 弱监督估计讽刺起时；分类头 MC dropout（T=10）给不确定性。最佳配置为 WavLM-Large。

## 实验与结果
MUStARD++：F1 75.3、Acc 73.3；MUStARD：F1 77.0；PodSarc：F1 62.9；德语 MuSaG：F1 65.6。相对无不一致建模，10 次运行 Wilcoxon p=0.002、Cohen’s d=1.51。优于先前音频-only 报告（如 MUStARD++ 上 Ray 64.5、Tiwari 66.6）。预测讽刺起时多落在句后 70–80% 位置。人类评价显示不确定性与感知歧义相关（正文 Table 6 抽取截断）。

## 结论
显式时序韵律不一致可提升纯音频讽刺检测，并在脚本/自发/跨语料上泛化；弱监督起时与不确定性提供可解释性。

## 点评
把心理语言学“韵律反差”落成可学习标量门控，比堆 SSL 容量更有机制叙事；大编码器仍主导增益，不一致项是边际但统计显著的补强。自发与跨语 F1 明显低于脚本对话，说明夸张韵律假设在自然对话中变弱。后文不确定性人评表抽取不全，相关结论以摘要为准。
