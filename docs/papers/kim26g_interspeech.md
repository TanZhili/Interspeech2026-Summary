# Latency-Configurable Streaming Speech Enhancement via Asymmetric Temporal Padding

- 论文编号：817
- 报告人：Yunsik Kim
- 程序：Tuesday 29 September 2026 / Real-Time, Low-Latency and Edge Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/kim26g_interspeech.pdf

## 问题
流式增强的延迟–质量常被当成因果/非因果二选一，多数模型锁死在单一延迟点。需要在固定参数量的卷积架构里系统配置延迟，并解决非对称 padding 在分块流式中污染状态缓存的问题。

## 方法
LaCo-SENet（基于 PrimeK-Net，1.37M）：训练时用固定总 padding、按比例 r 拆成左右非对称 padding，改变过去/未来占比而不改感受野与参数量。双缓冲流式：状态缓冲保过去、输入级与特征级 lookahead 缓冲供未来；选择性状态更新只写入当前块帧，防止 lookahead 泄漏进后续状态。同一骨干用不同 padding 比训出一族模型，覆盖约 12.5–75 ms（以至更高上界）。

## 实验与结果
VoiceBank+DEMAND：全因果 12.5 ms 达 PESQ 3.35±0.02，不低于先前约 46.5 ms 因果 SOTA（3.27）；随 lookahead 增至 75 ms 升到 3.43，200 ms 对称上界约 3.47。STOI/CSIG/CBAK/COVL 同步小幅上升。与多延迟点文献模型对比显示低延迟端优势明显。

## 结论
非对称时域 padding 可作为训练期延迟旋钮；配合双缓冲与选择性状态更新，可在固定预算下扫离散延迟–质量曲线，并在全因果极低延迟仍保持强 PESQ。

## 点评
把“延迟配置”从换模型改成换 padding 比，工程上很实用；选择性状态更新是能落地的关键细节。注意每个延迟点仍需单独训练，不是运行时一模型切换；与下文 LCA 的单模型多模式形成互补路线。
