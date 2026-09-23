# Automatic Lyric Transcription for Greek Songs: Scaling and Task Composition Effects in Whisper Adaptation

- 论文编号：1371
- 报告人：Dimitrios Damianos
- 程序：Tuesday 29 September 2026 / Multilingual, Cross-lingual & Low-Resource ASR
- 技术分类键：asr
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/frangiadaki26_interspeech.pdf

## 问题
歌词转写（ALT）因旋律、节奏与伴奏比语音难，希腊语此前无系统 ALT 基准；Whisper 零样本在歌声上退化严重。

## 方法
从 GAD 策展 GAD-ALT：Demucs 分离人声、CTC 强制对齐、gpt-4o-mini 段级英译，17,458 段约 19.65 h，按歌划分。对比 Whisper Small/Medium/Large-v3：仅转写、2:1/4:1 转写–翻译多任务、两阶段（先冻编码器在 Common Voice 希腊语上适应解码器，再全开歌声微调）。

## 实验与结果
零样本 WER 92.3/65.1/53.6；最佳为 Large-v3 两阶段 27.2%。小模型受益于多任务正则（Small 2:1→33.6%），大模型更适合专注转写/两阶段。人声干声优于混音；人工增强/混音训练反而变差。错误类型含语义替换、边界漂移、幻觉、正字歧义等。

## 结论
建立希腊 ALT 首个基准；规模与任务组成交互明确，两阶段+大模型最有效。

## 点评
贡献在低资源 ALT 管线与受控消融，揭示“多任务主要帮小模型”。歌声–语音域差仍主导错误结构；阶段一用朗读稿可能声学上仍远歌声，作者已提示可换更富韵律中间域。
