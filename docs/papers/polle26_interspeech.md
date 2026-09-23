# Synthetic Speech, Real Signal: Paralinguistic Preservation and Cross-Lingual Augmentation via Voice Cloning

- 论文编号：2993
- 报告人：Roseline Polle
- 程序：Tuesday 29 September 2026 / Multilingual and Cross-Lingual Paralinguistic Analysis and Processing
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/polle26_interspeech.pdf

## 问题
合成语音增强在 ASR 等语言任务中常见，但在情感、临床生物标志物等副语言任务中研究较少；语音克隆通常只评 WER、说话人相似度与 MOS，不清楚克隆后是否保留下游副语言分类所需信号。临床抑郁/焦虑检测几乎全是英语标注数据，低资源语言难以直接迁移。

## 方法
评测八个开源克隆模型（XTTS v2、Zonos、E2-TTS、F5-TTS、OpenAudio S1-mini、CosyVoice 2/3、MaskGCT）。流程：Whisper medium 转写，去首尾静音并截断至 10s；两种文本条件——Repeat（复述原转写）与 Standard（所有说话人读同一固定段）。特征用 WavLM Large 1024 维嵌入，Logistic Regression（L2，C=0.001）做分类，指标为 AUC，并定义保留分数 \(P=(A_c-0.5)/(A_r-0.5)\)。RQ1：公有数据与自有英语临床语料上，Real vs Cloned 五折说话人无关交叉验证。RQ2：将英语临床语音克隆为日语（Qwen 3 235B 翻译），对比 in-language JP、raw EN→JP、cloned EN→JP。RQ3：说话人嵌入余弦相似度与 AUC 退化的相关性。

## 实验与结果
数据含 IEMOCAP、MELD、MUSTARD、VCTK 与自有 EN（约 82k 样本）/JP（约 14k）临床集。RQ1：176 组配置均显著高于随机；相对 Real 中位退化 3.2 pp，中位 \(P=0.87\)；Repeat 下五模型 \(P\geq0.90\)，Standard 中位 \(P=0.75\)。RQ2（N=10k EN 说话人）：四模型克隆条件均显著优于 raw EN（如 OpenAudio 抑郁 +3.3 pp，CosyVoice 3 焦虑 +4.0 pp），仍低于 JP in-language 参考。缩放分析约从 1k 说话人起克隆优于 raw baseline。RQ3：临床与 IEMOCAP 上说话人相似度与退化强相关（如 general \(r=0.87\)），噪声语料上较弱。

## 结论
现代克隆模型在 Repeat 下可保留多数副语言判别信号（最优 >90% above-chance），并可用作英→日临床增强，优于原始跨语种迁移；与 in-language 仍有差距。局限：仅一对语言、分类器固定为 LR、特征仅 WavLM、临床数据不可公开复现。

## 点评
把“克隆质量”直接接到下游副语言 AUC，并用 Repeat/Standard 拆开语义与副语言贡献，设计清楚。跨语增强在段落朗读上也有增益，说明收益不全来自译文语义。脆弱点是依赖自有临床语料与单一 WavLM+LR 探针，以及英→日外推是否成立未知。
