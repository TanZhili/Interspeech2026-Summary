# Robust Streaming ASR with Decoupled Separation and Recognition

- 论文编号：1503
- 报告人：DeLiang Wang
- 程序：Thursday 1 October 2026 / ASR Under Real-World Constraints: Streaming, Adaptation, and Efficiency
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yang26h_interspeech.pdf

## 问题
流式 ASR 在噪声、混响与干扰说话人下研究不足；多条件训练（MCT）需大规模含噪数据且常伤干净语音表现。

## 方法
解耦框架：在线分离前端（DPDFNet、因果 oTF-CrossNet；另报全上下文 TF-CrossNet）+ 仅干净语音训练的流式后端。提出 FastMambaformer（FastConformer 中卷积换成 Mamba），并接 NeMo 预训练 FastConformer 与 SimulStreaming。前端与 MCT 基线见相当数据量；推理均零 look-ahead。

## 实验与结果
干净 LibriSpeech 上 FastMambaformer 优于同配置 FastConformer。含噪 LibriSpeech：oTF-CrossNet+干净后端平均 WER 36.1%，优于 noisy-trained MCT（36.9%）；接预训练后端同样受益。CHiME-4 实测：oTF-CrossNet+干净后端 24.56% 优于 MCT 26.17%；大模型+前端可进一步降到约 13.7%。LibriCSS：弱前端 DPDFNet 可伤性能，oTF-CrossNet 降低重叠 WER（如干净后端 26.51→22.93%）。

## 结论
足够强的在线分离可使干净训练流式 ASR 超过 MCT，且前端/后端可独立升级，无需任务专用再训。

## 点评
把稳健性外包给模块化前端，避开“为噪声重训 ASR”的代价，对大预训练模型尤其实用。收益高度依赖前端质量（DPDFNet vs oTF-CrossNet 反差大）；全上下文离线 TF-CrossNet 仍明显更好，流式稳健仍是硬问题。
