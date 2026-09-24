# PiDA: Phonetically-Informed Data Augmentation for Robust Vietnamese Speech Translation

- 论文编号：1963
- 报告人：Xuan Tung Nguyen
- 程序：Wednesday 30 September 2026 / Multilingual Speech 2
- 技术分类键：multilingual
- 全文：https://www.isca-archive.org/interspeech_2026/nguyen26f_interspeech.pdf

## 问题
级联越南语 ST 中 ASR 错误会传到 NMT；FLEURS Vi–En 上 clean 与 ASR 输入差约 6.79–10.64 BLEU。不清楚该注入何种噪声；通用随机/LLM 噪声未必匹配真实语音混淆。

## 方法
先用 PhoWhisper-large / wav2vec2-base 转写 FLEURS 训练集，按语音学关系把替换错误分为元音/辅音/声调/OOV/无关/正字变体，并用混合效应模型回归对 ∆TER 的影响。据此提出 PiDA：XPhoneBERT 音节嵌入建近邻索引，按训练 WER 统计标注删除/替换，再以温度 softmax 从 top-k 音近音节采样替换。用 clean+PiDA 微调 VinAI-Translate。

## 实验与结果
词内错误以音系混淆为主；元音混淆对 ∆TER 影响最大（系数 97.66）。clean & PiDA：PhoWhisper ST BLEU 28.29（相对 clean 微调 +2.04），wav2vec2 亦显著提升，且 MT BLEU 略升至 33.72。仅真实 ASR 噪声可提 ST 但伤 MT；MEDSAGE 无显著 BLEU 增益。k=5、τ=0.5 最优且较稳。

## 结论
越南语 ASR 替换多为系统性音系混淆；音近嵌入增强可在无音频、无 LLM 条件下提升级联 ST 且不牺牲干净文本 MT。

## 点评
用 LMM 把“该注入什么噪声”实证化，再把增强绑定到 XPhoneBERT 音近空间，比随机词表或英语中心 LLM 更贴合越南语音系。局限是单数据集、未建模 OOV 跨语映射，插入错误也未仿真。
