# CycleCodec: Distillation-Free Factorized Neural Speech Codec via Cycle-Consistent Speaker Swapping

- 论文编号：806
- 报告人：Yang Ai
- 程序：Wednesday 30 September 2026 / Speech Synthesis: Speech Features, Codec and Representations
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/zheng26_interspeech.pdf

## 问题
因子化神经语音编解码常靠 ASR/SSL 蒸馏拆开内容与说话人，低资源或未见语言缺可靠 teacher；无蒸馏的 TiCodec 等又易残留跨流泄漏，可控合成不稳。

## 方法
在 TiCodec 骨干上从零训练：帧级离散时变码 `q`（单码本大小 256，约 0.6 kbps）承载内容/韵律，全局连续嵌入 `g` 承载说话人。架构上缩小码本容量抑制时变流泄漏，并用可学习 query 的 Transformer 聚合器（N=8、L=4）+ 说话人对比损失强化 `g`。核心自监督是 cycle-consistent speaker swapping：批内置换配对，用源 `q`+目标 `g` 合成 swap 语音，再编码约束 `q_swap≈q_src`、`g_swap≈g_tgt`，并用源 `g` 解码回 cycle 语音施加 mel 重建损失。两阶段训练：先 `L_codec+L_spk`，再冻结编码器与量化器，对解码器做 cycle 微调。

## 实验与结果
LibriTTS（24 kHz）训练；重建与零样本 VC 在英语（LibriTTS）、普通话（Seed-TTS-ZH）、越南语（VieNeu-TTS）上评测。重建上 CycleCodec 全面优于 TiCodec，PESQ/STOI/V/UV F1 也优于蒸馏式 LSCodec，但 WER 仍高于 LSCodec。零样本 VC：英语上逊于 LSCodec、优于 TiCodec；跨语言时 CycleCodec 的 WER 低于 LSCodec（如 Seed-tts-zh：13.488 vs 15.426；VieNeu：25.706 vs 31.606），说话人相似度仍具竞争力。消融显示去掉 cycle 对内容保持伤害最大；迭代 VC 中 CycleCodec 的 WER 漂移小于 TiCodec。小规模听感：英/中 VC 自然度 MOS 相对 TiCodec 提升。

## 结论
不依赖预训练 teacher，仅靠编解码内部的 cycle 说话人交换与容量/对比约束，即可在跨语言设定下获得更稳的说话人–内容解耦与可控合成。

## 点评
抓住的是“低资源因子化”里 teacher 不可用时，用 codec 自洽的 swap→再分析→swap-back 代替外部语义监督。相对蒸馏路线，跨语言内容保持更稳；相对纯重建指标，WER 仍偏弱，说明内部约束对细粒度声学细节友好、对 ASR 级内容对齐未必最强。依赖说话人标签做对比损失，且第二阶段冻结分析路径，解耦上限仍受第一阶段表示质量制约。
