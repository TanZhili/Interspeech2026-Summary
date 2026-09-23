# English Vowel Perceptual Training under Multitalker Babble: A Comparison of Humans and Large Language Models

- 论文编号：966
- 报告人：Wenwei Dong
- 程序：Monday 28 September 2026 / Model of Speech Perception
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dong26b_interspeech.pdf

## 问题
二语（L2）听者对母语中缺失的语音对比感知困难，高变异语音训练（HVPT）在多说话人 babble（MTB）背景下可能有益，但用真人听者逐一试不同 babble 说话人数成本高。此前工作对比了荷兰语 L2 听者与 Wav2Vec2.0 在 2/6 说话人 babble 训练下的元音辨别，但单语模型在 speech-shaped noise（SSN）上远弱于听者。本文问：多语模型（Whisper、speech LLM）能否像听者一样从 MTB 训练中受益、谁的提升趋势更接近听者，以及与测试噪声匹配的训练是否优于 babble。

## 方法
数据与先前听者实验一致：英式单音节词中的 /E/–/æ/ 与 /eI/–/aI/；pre/posttest 各 64 试次（quiet 与 SSN），训练 100 试次；babble 由 2 或 6 名美式英语说话人朗读段落混合而成。70 名荷兰母语者做二选一 HVPT，训练期给纠正反馈，半分到 2/6-talker babble；测时 quiet 与 SSN。模型侧对 Wav2Vec2.0（wav2vec2-base-960h）、Whisper-large-v3、Qwen2.5-Omni-7B 先测预训练表现，再在 2-talker、6-talker、quiet、SSN 四类训练集上微调后复测。指标为选词正确率：Whisper 用识别文本与两选项的编辑距离；LLM 用提示直接二选一，并以 LoRA 微调；Wav2Vec2.0 用强制对齐置信度与 CTC 微调。

## 实验与结果
听者：元音对与 test×背景交互显著；/eI/–/aI/ 优于 /E/–/æ/；quiet 优于 SSN；仅在 SSN 上 posttest 显著高于 pretest（约 +3.44%），2 与 6 talker 训练条件无显著主效应。Quiet 测集上 babble 训练后听者 6-talker 总均提升约 2.59%（不显著）；Wav2Vec2.0 仅在 2-talker 上总均 +4.68%，LLM 在 2/6-talker 上分别 +4.68%/+3.12%，Whisper 近乎天花板无提升。SSN 测集上各方均受益，且 6-talker 优于 2-talker；听者 6-talker 后 /E/–/æ/ 80.89%、/eI/–/aI/ 93.21%；Wav2Vec2.0 与 Whisper 平均多在 70% 以下，LLM 最高平均约 78.12% 与 90.62%，更接近听者。Quiet/SSN 训练：quiet 测集上 quiet 训练三模型均有提升（LLM 总均 +4.68%），SSN 训练仅 LLM 总均 +9.37%；SSN 测集上 quiet 训练使 Wav2Vec2.0 下降 7.81%，Whisper/LLM 分别 +6.25%/+9.37%，SSN 训练使 Whisper 总均提升最大（+28.12%）。

## 结论
多语模型也能从 MTB 训练中受益；在 SSN 上 speech LLM 准确率与听者更接近、趋势更一致，而 Whisper/Wav2Vec2.0 在 quiet 上偏高、SSN 上偏弱。匹配噪声训练可带来更大提升（尤其 Whisper 在 SSN→SSN），但 babble 训练对逼近听者模式仍有参考价值。局限包括 quiet 上的天花板效应、模型与听者测试流程不完全对等，以及抽取文本末尾讨论略有截断。

## 点评
工作把 L2 感知训练条件筛选问题转成可复用的神经模型探针，核心不在刷 ASR 分数，而在看谁在 quiet/SSN 上的相对难度与训练增益像听者。Speech LLM 的提示式二选一更贴近听者任务，LoRA 微调也更像“短时感知适应”；弱点是模型天花板、微调轮数少、以及用识别/编辑距离代理感知判断，可能夸大或扭曲与真人的可比性。
