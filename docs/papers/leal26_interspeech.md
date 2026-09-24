# Tarsila-ASR: A Multi-Domain Test Suite for Benchmarking Brazilian Portuguese Speech Recognition

- 论文编号：450
- 报告人：Sidney Leal
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/leal26_interspeech.pdf

## 问题
巴西葡萄牙语（BP）自发语音含填充词、犹豫、截断与口音差异，现有公开资源虽多，但缺少统一、多域的自发语音评测基准，难以公平比较开源 ASR 并推动领域适配。

## 方法
Tarsila-ASR 汇总既有公开语料的测试子集（CORAA 各子集、CV17、MLS、MuPe、NURC-SP、TEDx 等），统一保留 text/duration/audio，并加 origin 与 voice-gender-classifier 估计的 gender；音频统一 16 kHz。得到 62,094 条、72.46 小时（女/男约 48%/52%）。在此基准上零样本评测 MuPe-ASR、Whisper-large-v3、Omnilingual 7B；再将各自发语音语料的 train/val 拼成约 1,156 小时训练 + 39 小时验证，微调 Distil-Whisper、Whisper-medium/large-v3、Omnilingual 300M/1B（7B 仍零样本），报告 WER/CER、RTF、BERTScore、SeMaScore（mDeBERTa-V3-base）。

## 实验与结果
零样本均值 WER：MuPe-ASR 21.63、Whisper-large-v3 33.03、Omnilingual 7B 51.71，朗读子集明显好于自发子集。微调后 whisper-large3-ft-75k 达到整体最优：WER 15.40、CER 9.11、BERTScore 97.84；distil-whisper-ft-200k WER 16.52 且平均 RTF 更低。与既往系统比，wlarge3-ft-75k 在 CV17/CORAA/NURC-SP/MuPe 上均值 WER 15.82，优于 MuPe-ASR 的 21.27。训练步数并非越长越好（如 ft-200k 优于 ft-750k）。

## 结论
作者认为统一多域自发语音基准暴露了预训练与真实对话域差，领域微调可将错误率压到约 15–19% 并刷新 BP 自发语音开源 SOTA；资源与 checkpoint 已公开。后续拟扩展基准、改进转写规范化与风格平衡，并联合考察准确率、效率与语义保真。

## 点评
工作重心是“把已有公开测试集合起来 + 系统微调”，对 BP 对话 ASR 很务实。强项是子集级 WER 与效率/语义多指标并存，能看见朗读–自发权衡；弱项是基准依赖既有测试划分与标注惯例，结论对数据拼合与 checkpoint 选择敏感，未必直接迁移到其他语言变体。
