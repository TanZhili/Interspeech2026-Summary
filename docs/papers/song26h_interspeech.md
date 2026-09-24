# MER-Live: An Interactive Browser Demo of Prosody-Driven Multimodal Emotion Recognition

- 论文编号：3607
- 报告人：Haoyu Song
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/song26h_interspeech.pdf

## 问题
多数 SER 系统按离线、已知边界的段级 logit 平均评估；实时部署需要滑动窗、低延迟，并在不同速率下融合语音、视频与文本。现有演示也容易被误解为关键词分类。

## 方法
MER-Live 以语音为主、视频与文本为辅的浏览器实时多模态情感识别演示。声学分支 MSMC（约 6.77M 参数）输入最近 3 秒的 128×300 log-mel，经 Masked Auto-Encoder 在约 17.7k IEMOCAP 段上无标签预训练后四类微调；文本仅为 ASR 软概率的置信度加权 tie-breaker。各模态权重 \(w_m=2\max(0,(1-p^{neu}_m)-0.15)\)，经归一化与 EMA（α=0.20）及 0.10 滞后平滑。模型导出 TensorRT FP16；UI 每 250 ms 更新，支持十折 hold-out 热切换、5 秒录制平均、与开源 wav2vec 2.0 SER 基线并排对比。

## 实验与结果
10-fold IEMOCAP 上部署用音频 MSMC：74.03% WA、66.39% UA；多模态合成评估可超 83%。H200 上 batch 5 时 TensorRT FP16 0.24 ms，相对 PyTorch FP32 约 14×。合成视听文本概率下，音频相对 vision+text 基线约提升 6–9%。

## 结论
演示了轻量韵律主导的端到端实时多模态情感管线。局限包括：实时模式因 3 秒感受野准确率上限约 60%；ASR 文本分支依赖 Chrome/Edge；当前经明文 WebSocket，getUserMedia 需 localhost 或 TLS。

## 点评
把“同词不同调”做成可当场验证的交互，切中韵律主导主张。融合规则透明但多模态数字来自合成概率流而非真视频标注；实时与离线协议差距也说明部署评估需单独报告。
