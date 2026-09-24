# URGENT-MOS: Unified Multi-Metric and Preference Learning for Robust Speech Quality Assessment

- 论文编号：1671
- 报告人：Wei Wang
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/wang26aa_interspeech.pdf

## 问题
URGENT 等协议同时要绝对多指标与成对偏好，但现有 SQA 多只做其一；异构标注与跨域鲁棒性不足。

## 方法
URGENT-MOS：多分支特征提取 + Absolute Metric Prediction Module（分范畴多指标头）与 Naturalness-Conditioned Preference Module（交叉注意力偏好）。联合训练人类 MOS、客观指标与由 MOS 构造的偏好对（任意/语料内/同参考匹配，δ=0.5）。释放偏好标注数据；覆盖 TTS/VC/SE/VoIP 等。

## 实验与结果
偏好准确率跨 SOMOS、TMHINT-QI、UR25、CHiME-7、LIVETALK 等整体强于 DNSMOS/UTMOS 等，且比 SpeechEval/SpeechJudge 更跨域稳健。绝对相关（LCC/SRCC）在多数据集上常居前列或次优（如 F4C1M5Dref）。全指标监督未必优于自然度子集。

## 结论
在共享架构中联合多指标绝对预测与偏好学习，可更好对齐现代评测协议并提升跨域稳健性。

## 点评
直接回应 URGENT 协议缺口，工程完整（代码+偏好数据）。偏好对由 MOS 派生，与真人口头偏好仍有差距；特征分支数与监督范围有可调权衡。
