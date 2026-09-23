# A Finetuned SpeechLLM for Joint Multi-Granular L2 Assessment and Natural-Language Rationales

- 论文编号：2335
- 报告人：Aditya Kamlesh Parikh
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/parikh26_interspeech.pdf

## 问题
自动 L2 口语评估常给不透明分数或细粒度标签，缺少与标签一致、可教的自然语言理由。现有系统很少在单次端到端中同时做多方面、多粒度评分并生成忠实理由；数据严重偏高分，偏好对齐对“近邻错误”又可能过激。

## 方法
以 Qwen2-Audio-7B-Instruct 为骨干（4-bit 冻结 + LoRA r=64），用 rubric 提示一次输出句级 Accuracy/Fluency/Prosody、词/音素级 Accuracy，以及 Rationale。训练用 SFT + Bounded DPO（BDPO）：对真值标签构造被拒标签（句级扰动一个方面、序列级扰动全部；约 88% 下调以抑制 “niceness bias”），BDPO 限制对被拒样本的过度打压。在 SpeechOcean762 上把 0–10 / 0–2 分数离散为五档序数标签。

## 实验与结果
多粒度模型句级 PCC：Accuracy 0.66、Fluency 0.73、Prosody 0.71；词/音素 Accuracy 0.52/0.42。相对单粒度，句级 Accuracy 更好，序列级有权衡。相对 GOPT/Azure PA/SimPO：句级竞争力强，词/音素 PCC 优于 SimPO，但音素仍落后 GOPT。理由：句级情感与内部预测高度自洽，对真实低分偏“柔化”；词/音素提及稀疏，与标签 PCC 仅 0.50/0.20（内部）与 0.35/0.07（外部）。

## 结论
SFT+BDPO 的 SpeechLLM 可联合多粒度评分并产出基本可信的句级理由；细粒度忠实度仍不足。BDPO 有助于在偏斜评分下保持 rubric 与标签–理由一致性。

## 点评
把“可解释评估”拆成 plausibility 与 faithfulness，比只报相关更诚实。联合多粒度有助于句级 grounding，但音素诊断仍明显弱于 GOP 类路线；理由里出现拼写启发式，说明文本先验仍可能压过声学证据。
