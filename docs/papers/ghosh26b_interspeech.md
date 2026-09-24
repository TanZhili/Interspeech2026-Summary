# LipAdapter: Text-to-Video Alignment is All You Need for Lip-to-Speech

- 论文编号：518
- 报告人：Souvik Ghosh
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/ghosh26b_interspeech.pdf

## 问题
端到端唇语转语音需大量数据且难泛化；在 VSR 语料上训的生成器音质弱，而直接喂原始视觉又引入噪声。如何用少量数据把冻结 SOTA TTS 改造成唇同步语音生成器。

## 方法
LipAdapter：冻结 VSR 与 TTS，经 text-to-video alignment 模块对齐音素表示与唇嵌入，使 TTS 在视觉引导下合成唇同步语音。模块化适配，训练约 30h，约为既往方法 1/15。

## 实验与结果
LRS3：LipAdapter（V+T, 30h）WER 21.2%，接近或优于用 430h 的 LipVoicer（21.4%）等；STOI-Net/DNSMOS/LSE 指标具竞争力。MultiVSR 上 WER 34.44%（vs LipVoicer 35.95%）。零样本多语（法/德/西/葡）有报告。另有人工 MOS。

## 结论
文本–视频对齐足以把强 TTS 转为唇同步合成，大幅降数据需求并具备跨语零样本潜力。

## 点评
「适配器 + 冻结大模型」路线对低资源唇语合成很实用。强在数据效率与模块复用；脆弱点在依赖上游 VSR 错误传播，以及零样本多语仍受视觉–语言覆盖限制。
