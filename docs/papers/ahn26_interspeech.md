# Context-Adaptive Automated Audio Captioning with Symmetric Dual-MoE and Dynamic Reward Routing

- 论文编号：2897
- 报告人：Seyun Ahn
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/ahn26_interspeech.pdf

## 问题
AAC 常优化统一目标，RL 奖励又多静态加权，难以按声学场景调整生成策略与评价侧重。

## 方法
对称双 MoE：策略侧在 BART 解码器上层插入 LoRA 专家，由交叉注意状态路由（top-1）；奖励侧分解语义、语法、词汇多样性与 ATFT 细粒度音文对齐，声学全局表示动态加权；组内标准化后用 GRPO 更新。先 CE 监督再 RL。

## 实验与结果
Clotho：BLEU4 0.174、CIDEr 0.414、FENSE 0.464、MOS_n/a 最高。AudioCaps：语义与 SPIDEr-FL 领先，CIDEr 略逊纯 CIDEr-RL。消融去掉任一奖励或任一侧 MoE 均降；交叉注意路由优于纯文本/纯音频路由。词汇多样性相对 SFT 有提升但仍低于人工。

## 结论
策略与奖励双侧上下文自适应可协同提升字幕对齐与人类偏好，尤其对齐敏感指标。

## 点评
把“场景不同、该强调什么”同时写进生成与打分，比单侧 MoE 或固定奖励更一致。奖励分解与路由增加训练复杂度；AudioCaps 上 CIDEr 未全面碾压说明与 n-gram 目标仍有张力。
