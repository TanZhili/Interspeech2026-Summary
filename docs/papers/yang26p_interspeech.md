# RobustSpeechFlow: Learning Robust Text-to-Speech Trajectories via Augmentation-based Contrastive Flow Matching

- 论文编号：3086
- 报告人：Jinhyeok Yang
- 程序：Thursday 1 October 2026 / Flow Matching for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/yang26p_interspeech.pdf

## 问题
流匹配 TTS 在零样本相似度与自然度上已较强，但对齐仍易出现 skip/repeat，尤其在小模型或低 NFE 时更严重。已有偏好数据/DPO、ASR/CTC 辅助监督、架构加强等方法有效，但常需额外数据策展或外部模型，不利于轻量部署。

## 方法
**RobustSpeechFlow** 是面向 TTS 的对比流匹配训练策略，无需外部对齐器或偏好集：
- 正样本：标准条件流匹配，在 Supertonic 自编码器潜空间上回归速度场。
- 负样本：批内随机负样本 + **长度保持的失败模式增强**——以 0.5 概率做 repeat（覆盖另一段）或 skip（前移后续帧并用静音潜表示填尾），在潜空间制造声学上相近但局部文本–语音对应被破坏的 hard negatives。
- 总损失：\(L = L_{\mathrm{pos}} - \lambda_{\mathrm{rand}} L_{\mathrm{rand}} - \lambda_{\mathrm{aug}} L_{\mathrm{aug}}\)，推理流程不变。

## 实验与结果
训练：英/韩各约 10k 小时内部数据，固定 SupertonicTTS（0.06B）架构与预训练 text-to-latent，比较 Baseline / ContrastiveFM / RobustSpeechFlow。Seed-TTS-eval：WER 1.44→1.38（相对 Baseline 降约 4.2%），SIM 保持 0.60，为表中最低 WER。自建 ZERO500（每语 50 音色×10 文本）：NFE=24 时英 CER 0.48%→0.35%、韩 CER 0.81%→0.57%；低 NFE 下韩语收益更明显。训练曲线显示后期对齐更稳。

## 结论
用长度保持的 skip/repeat 潜空间增强作对比负样本，可在不改推理、不引入外部模型的前提下提升内容保真；在紧凑模型与低 NFE 上更稳。局限：公开基准上说话人相似度仍落后大模型，作者归因于紧凑架构与编解码器而非目标本身；客观 ASR 指标也受识别误差与文本规范化影响。

## 点评
把对比流匹配的负样本从「随机错条件」换成「同句对齐失败的硬负样本」，直接对准生产里最痛的 skip/repeat，是很务实的训练侧改动。强在零额外推理成本与易集成；脆弱处在增强覆盖率/span 启发式是否覆盖真实失败分布，以及 SIM 瓶颈是否真能靠放大模型消解——若负样本过强也可能压制合理韵律变异。
