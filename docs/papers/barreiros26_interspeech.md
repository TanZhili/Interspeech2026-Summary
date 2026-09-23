# Massive Open-Vocabulary Keyword Spotting

- 论文编号：1444
- 报告人：Leonor Barreiros
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/barreiros26_interspeech.pdf

## 问题
开放词表关键词检出 + 上下文偏置可改善稀有术语 ASR，但声学嵌入过高维，词表上千时内存/时延不可行（基线约数百词）。

## 方法
在 CB-Whisper 式 OV-KWS 上三维压缩：(1) sparsemax 门控 + 熵稀疏自动选出预测力最强 Whisper 层（实验得 14/16/32）；(2) MLP 把隐维压到 64；(3) 1D CNN+池化帧率减半。压缩嵌入预存词表库；检出词写入 Whisper 解码器热词提示。不微调 ASR。

## 实验与结果
相对未压缩基线，嵌入约小 128×。ACL6060：LHF-comp MER 21.9、实体召回 57.2，内存 11 MB vs 基线 1406 MB；Aishell（训练未见中文）召回 71.3、MER 14.7；内部葡语医学 16,062 词表内存 882 MB vs 112,929 MB，RTF 0.76 vs 4.52。KWS F1 在压缩后仍可比或更好。

## 结论
作者认为层选择+隐维+帧率压缩可使开放词表 KWS 支撑海量词表，并在不微调 ASR、甚至未见语言上保持可比实体召回。

## 点评
生产导向：把“能不能跑上万热词”变成可落地的压缩管线，且保留声学而非纯文本匹配。内部集 MER 略升提醒偏置幻觉风险；依赖 TTS 合成关键词音频的声学匹配质量。
