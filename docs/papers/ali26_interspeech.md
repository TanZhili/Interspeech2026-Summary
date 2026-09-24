# Fed-SpeechLLM: Federated Learning Speech Language Models for Multilingual ASR

- 论文编号：689
- 报告人：Daniele Giuseppe Falavigna
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/ali26_interspeech.pdf

## 问题
SpeechLLM 适于多语 ASR，但集中训练与隐私约束冲突；联邦学习面临声学与跨语双重 non-IID。语言偏斜客户端会使标准 FL 退化。

## 方法
Fed-SpeechLLM：在双语英/意设置评测联邦 SpeechLLM。选择性聚合语音编码器与投影层，LLM 骨干冻结（LoRA 可适配）。提出语言感知梯度聚合与基于采样聚类的客户端选择，缓解多语不平衡。Flower + FedAvg，每轮约 30% 客户端、本地 10 epoch、共 100 轮。数据：LibriSpeech-100 与 MLS 意大利语。

## 实验与结果
单语 FL 接近中心化（LS 约 6–7% vs 中心约 6%；MLS 约 22% vs 约 20%）。双语全客户端：LS/MLS 约 16.8/19.7，相对中心仍有差距。客户端平衡、服务端微调与早/晚语言偏置显著影响收敛；早期英语偏置可将 LS 联邦–中心差距缩至约 5 点。Whisper 作编码器的消融验证编码器选择影响。

## 结论
在复合非 IID 下，语言感知聚合与客户端采样策略可使联邦 SpeechLLM 收敛并接近中心化性能，为隐私约束多语 ASR 提供可行路径。

## 点评
首次系统分析 SpeechLLM 联邦适配，抓住“语言偏斜”这一新轴。仍偏双语音读语料；真实设备异构与通信预算未充分展开。
