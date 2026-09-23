# Reducing Speaker Residual by Considering Pinhole Effect in Voice Anonymization

- 论文编号：2346
- 报告人：Zeyan Liu
- 程序：Wednesday 30 September 2026 / Speaker Privacy Preservation and Anonymization
- 技术分类键：speaker
- 全文：https://www.isca-archive.org/interspeech_2026/liu26q_interspeech.pdf

## 问题
解耦式匿名化后，说话人属性仍会泄漏到内容/韵律等非身份表征，提升 linkability。既有方法多只净化部分支路或依赖隐式瓶颈，缺少可直接优化、跨流统一的残差抑制目标。

## 方法
基于 pinhole 效应：any-to-one 伪说话人映射下，同源说话人匿名句在嵌入空间的成团程度反映残差与可链接性。对已训好的框架做微调：批内共用伪说话人特征，用冻结说话人编码器提匿名语音嵌入，定义 pinhole loss 为 between/within scatter 经广义特征向量投影后的迹比（越小可分性越弱）；仅更新 content encoder、prosody encoder 与波形生成器，并联合原生成目标。在 x-vector、ASRBN、ASRBN-GST 及 a2o/RS/GAN/IDMap-Diff 等伪说话人策略上评测；数据为 LibriTTS 训练、LibriSpeech/IEMOCAP 按 VPC2024 评。

## 实验与结果
Table 1 中各配置加微调后 EER 普遍上升（如 x-vector a2o 平均 EER 5.71→21.65；ASRBN a2o 30.80→45.49；ASRBN-GST IDMap-Diff 48.20→50.75），WER/UAR 变化通常很小。泄漏探针：内容分类准确率显著下降（如 x-vector 84.7→44.4；ASRBN 16.5→3.6）；ASRBN-GST 学习韵律支路 36.9→9.3。

## 结论
直接优化 linkability 的 pinhole 微调可跨多种匿名框架与伪说话人方法稳定提升隐私，同时大体保持效用，是抑制残差说话人属性的实用后处理策略。

## 点评
把“残差泄漏”操作化为可微的同类成团度量，避免只改某一支路却漏掉其他流。设计刻意用共享伪说话人放大残差信号以便优化，与推理阶段多样伪说话人策略仍兼容。收益在较弱基线（如纯 x-vector）上更戏剧性，在已强解耦系统上仍有边际提升；探针与 ASV 一致，但威胁模型仍是 VPC 式半知情 ASV，未覆盖更强自适应攻击。
