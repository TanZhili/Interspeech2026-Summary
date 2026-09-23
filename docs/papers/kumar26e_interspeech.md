# Lightweight Cross-Lingual Speaker Adaptation for Indic TTS

- 论文编号：2050
- 报告人：Tarun Kumar
- 程序：Tuesday 29 September 2026 / Low-Resource Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/kumar26e_interspeech.pdf

## 问题
印度语 TTS/克隆多依赖大模型；IN-F5 等虽相似好，但易丢词、推理慢，难低资源部署，且跨语种需额外录音。

## 方法
三阶段： (1) FastSpeech2+HiFi-GAN 多说话人预训练（约 119 h，印地/马拉地/泰米尔/泰卢固），CLS 统一音素，双位点 ECAPA-TDNN 说话人条件（韵律前 + 声学解码前）与余弦一致性损失；(2) 用 10 s 参考经 IN-F5 合成约 2 h，经音素 CER、音高、时长、log-likelihood 四级过滤得 2088 句；(3) 在过滤合成数据上微调说话人条件层。推理仅用非自回归 FS2。

## 实验与结果
相对 IN-F5：印地 WER 11.8%→9.6%，跨语平均相对降约 21.8%；SECS 0.87–0.88（略低于 IN-F5 的 0.89–0.91）；输出完全确定（\(\sigma_{F0}=\sigma_{syl}=0\)）；单句推理约 53× 更快、参数约 4.7× 更少。主观 MOS 全语种最高（印地 4.14），SMOS 与 IN-F5 接近。过滤以 CER 阶段剔除最多（5.3%）。

## 结论
10 s 参考 + 质量控制合成数据即可得到轻量、确定、跨语（CLS）的说话人适应 TTS，在可懂度与速度上优于克隆基线，相似可竞争。局限：单说话人演示，多说话人验证仍待做。

## 点评
把“慢且不稳的克隆教师”蒸馏成非自回归学生，四级过滤是落地关键。双位点条件与 CLS 支撑跨语一致。当前证据绑定一名印地男声与合成教师质量上限；SECS 受合成语料相似度天花板约束。
