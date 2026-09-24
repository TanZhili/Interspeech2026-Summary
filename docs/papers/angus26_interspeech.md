# Argmax Pro: Frontier-level Real-time Speech-to-text with Speakers and Custom Vocabulary on Mobile Devices

- 论文编号：3602
- 报告人：Atila Orhon
- 程序：Thursday 1 October 2026 / Speech Recognition, Enhancement and Real-Time Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/angus26_interspeech.pdf

## 问题
云端 ASR 在延迟可靠性、可用性、按分钟计费与隐私上受限，而首代端侧实时系统常缺说话人分离、自定义词表等能力，或在实时模式下牺牲精度，难以成为云端的对等替代。

## 方法
Argmax Pro 在 iOS/Android 上编排三个十亿级 Transformer：Parakeet v2 做语音转写，采用可自纠错的流式推理（interim/final 词），使预录与实时输入精度对齐；Canary v2 CTC 配合 CTC-WS 做上下文偏置/自定义词表，可扩至约 3000 词且不拖累端侧延迟；Streaming Sortformer v2 经 FastMSS 合成数据微调，增强对真实声学、音量与背景噪声的稳健流式说话人分离。推理分别落在 Apple Neural Engine、高通/联发科 NPU 与 Google Tensor TPU，以控制续航、发热与与其他 App 的资源争用。

## 实验与结果
正文以系统描述为主，定量结果多指向相关工作：关键词（尤其人名/公司/产品）精度在 Contextual Earnings-22 等分析中达 frontier 水平；自定义词表规模相对多数云平台（常 <500）扩展到 3000。本文未给出完整独立 WER/DER 表格。

## 结论
作者认为该统一实时系统可在广泛移动设备上提供带说话人与自定义词表的近云端级端侧 STT，作为 feature-rich 云端方案的对等替代。

## 点评
这是工程集成型演示：把流式纠错 ASR、大词表偏置与稳健流式 diarization 绑到 NPU 上，解决“端侧功能不全或实时掉精度”的产品缺口。方法细节依赖引用论文，本文本身缺少自包含的对照实验数字，评估边界需结合配套基准工作理解。
