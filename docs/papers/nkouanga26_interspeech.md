# Mitigating Speaker Leakage in Cascaded Multi-talker ASR with Diarization-based Transcript Correction

- 论文编号：3191
- 报告人：Suresh Singh
- 程序：Wednesday 30 September 2026 / Multi-Speaker Processing, Personalization, and Adaptation
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/nkouanga26_interspeech.pdf

## 问题
级联多说话人 ASR（分离→单说话人 ASR）受分离说话人泄漏限制；已有纠正多偏词汇重标注，对泄漏伪影的稳健剪除不足。

## 方法
后处理剪枝范式：用预训练说话人日志模型作多模态校验，对已转写片段在满足三方共识时剪除——时间包含（Cac）、词汇交叉验证（Clex）、时间对齐（Ctemp）。不改分离/ASR 骨干，可插在 Sepformer/Mossformer + Universal-2 等级联后面。

## 实验与结果
Libri2Mix、LibriSpeechMix、AMI（SDM/IHM）上相对基线一致降 WER；AMI 上相对改进约 5.8%–10.55%。高泄漏子集（分离源转写相似>0.4）相对 cpWER/WER 降幅最高约 29%（Mossformer AMI IHM 65.58→46.39）。消融：仅文本易过删；声学条件贡献大，三方合用最佳。相对联合 Mossformer-Diar 更跨域稳健。

## 结论
基于日志的三方共识剪枝能有效抑制级联 MT-ASR 中的说话人泄漏，尤其在高泄漏与真实会议场景。

## 点评
把泄漏当“可检测伪影”而非只重标说话人，后处理可复用强基础模型，工程上务实。依赖日志与对齐质量；仅文本条件有害说明多模态约束必要。未改分离前端，上限仍受分离 residual 限制。
