# A Transcript-anchored Pipeline With Large Language Models For Detecting Inappropriate Pauses In Dysarthric Speech

- 论文编号：534
- 报告人：Insung Lee
- 程序：Wednesday 30 September 2026 / Speech, Voice and Language Disorders
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/han26_interspeech.pdf

## 问题
构音障碍朗读中的不当停顿（IP）对可懂度与临床评估重要，但依赖转写锚定的位置信息；标准 ASR 常抑制赘语，MFA 等对齐在异常发音与韩语无空格下易出 <unk>，纯 VAD 又缺语言学语境。

## 方法
四阶段流水线：(1) 在 Autumn Paragraph 上微调 Whisper 做保留赘语/重复的 verbatim 转写；(2) MFA 对齐，候选停顿与 Silero-VAD 非语音重叠时用 VAD 边界替换，写入 [PAUSE x.xxs]；(3) GPT-5 做词典适配，把 <unk> 映射回原词并插入停顿标记；(4) 另一 LLM 按 SLP 定义将停顿分为合适或三类 IP（词内、赘语后、发音纠正中）并生成理由。数据 743 句韩语朗读（HC/轻中/重度），说话人独立 8:1:1。

## 实验与结果
停顿对齐（0.2 s collar）：Whisper+MFA+VAD 总体 F1 72.8，优于多数组合；微调 VAD alone 73.7。Whisper verbatim WER 微平均 18.3。SLP 专家评估（不含重度）：WhisperMFA 的 AP/IP macro-F1 在 HC 0.64、轻中度 0.68，优于 WhisperCTC 与 wav2vec 2.0。LightGBM 消融：加入 IP 特征使构音障碍检测 macro-ACC +8.4 pp、macro-F1 +7.2 pp。

## 结论
转写锚定 + LLM 词典适配/分类可在构音障碍上做可解释 IP 检测；对齐质量对下游判断关键。重度因转写不可靠未充分验证，未来需提升抗转写错误能力。

## 点评
把 MFA 时间精度、VAD 鲁棒性与 LLM 语言学判断串起来，针对韩语词典缺口用 LLM 桥接，是实用工程路线。专家评估显示对齐 F1 与「是否恰当」感知差距更大，说明仅停顿检测不够。重度排除与罗马化边界误判暴露了转写锚定路径的脆弱点。
