# SDP-Codec: A Speaker-Decoupled Speech Codec with Pitch Injection for Low-Bitrate Coding and Zero-Shot Voice Conversion

- 论文编号：3108
- 报告人：Hounsu Kim
- 程序：Wednesday 30 September 2026 / Neural Audio Codec Architectures
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26v_interspeech.pdf

## 问题
说话人解耦 codec 可降码率并支持 VC，但强抑制泄漏常靠多阶段/辅助训练，简单设计又易在局部 token 残留说话人信息。

## 方法
SDP-Codec 单阶段训练：局部 token 来自预训练 SSL（vq-wav2vec）连续预量化特征再经紧凑单码本；全局说话人分支；归一化 F0 经 pitch 编解码注入，全局条件反归一化 + soft-label 音高重建损失。评 16/24 kHz 重建、零样本 VC 与说话人探测准确率。

## 实验与结果
可比码率下重建有竞争力；零样本 VC 在说话人相似度、F0 相关与 MOS 上表现强；对比系统中说话人探测准确率最低，暗示泄漏更少。

## 结论
连续预量化 SSL 特征 + 显式 F0 注入与 soft-label 音高损失，可在单阶段管线中兼顾低码率、解耦与 VC。

## 点评
把“解耦 vs 训练复杂度”折中做实，用探测准确率直接量泄漏，比只报 VC-SIM 更硬。内容保真仍是作者自承短板；下游 SLM 尚未实测。
