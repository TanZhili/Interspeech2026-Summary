# AccentDrift: Real-time Streaming Accent Conversion via Sparse Speech Tokenization

- 论文编号：710
- 报告人：Sang-Hoon Lee
- 程序：Wednesday 30 September 2026 / Domain Adaptation & Accented ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/lee26g_interspeech.pdf

## 问题
实时流式口音转换（AC）对 L2 交互很重要，但现有系统多依赖平行语料、非流式架构、生成质量或口音/音色控制不足。

## 方法
AccentDrift：信息瓶颈视角下用稀疏语义量化（FSQ/iFSQ）从连续语音抽语言信息；口音适配器向稀疏语义 token 注入口音风格，音色适配器（因果 DiT + CAM++，HiFTNet 声码）分层生成说话人声学。全因果：cache-aware FastConformer、有限上下文 Transformer、因果 DiT/声码；并行流，标称约 520 ms（最小约 0.5 s）延迟。无需口音标签与口音配对数据，做零样本 AC（可选零样本音色转换）。

## 实验与结果
LibriTTS/VCTK/GLOBE 训练；L2-ARCTIC 主观、VCTK 印度口音客观。相对 Vevo-Style：流式下 WER 6.27 vs 13.8，SPK-SIM 0.72，口音相似度更高；NMOS/AMOS 可比。密集语义（CosyVoice3）难转口音。消融：NeMo-ASR 中层表征、更窄 IB、lookahead、chunk 大小影响延迟–质量权衡；GRL 抑口音泄漏。

## 结论
稀疏语义 tokenization + 分层风格适配可实现低延迟流式 AC，在保内容与音色下接近或优于非流式并行 AC 基线。

## 点评
把 AC 做成“先压成稀疏语言 token 再分层注口音/音色”，并真正落地因果流式栈，是相对并行 AC 的关键差异。不依赖口音标注利于扩展。仍需继续压解码延迟才更贴全双工；客观评测口音类相对有限，极端口音泄漏与长上下文仍是风险。
