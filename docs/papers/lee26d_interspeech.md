# SAM: A Mamba-2 State-Space Audio-Language Model

- 论文编号：639
- 报告人：Taehan Lee
- 程序：Wednesday 30 September 2026 / Audio Foundation Models and Generation
- 技术分类键：generation
- 全文：https://www.isca-archive.org/interspeech_2026/lee26d_interspeech.pdf

## 问题
Transformer 音频语言模型算力随序列长度二次增长。Mamba 等 SSM 在语言与图像理解中已显示潜力，但在音频–语言模型中如何与音频编码器交互、是否需要端到端微调、以及长未压缩 token 是否真正有利，尚缺系统表征级分析。

## 方法
SAM：EAT-base 音频编码器 → 两层 MLP 连接器 → 预训练 Mamba-2（130M/780M/2.7B）作 LLM。连接器对比 (a) 沿频率维拼接压缩为 64 token；(b)/(c) time-major / frequency-major 保留更长序列并插入 “&&” 分隔符。在 OpenAQA 上按 LTU 四阶段课程 + LoRA（in_proj/out_proj）训练，自回归 caption 交叉熵。另构 OpenReasonAQA（基于 ReasonAQA 的 BQ/MCQ，约 3.8M）强化指令跟随与推理。

## 实验与结果
SAM-2.7B（r=256, concat）AudioSet mAP 21.1、AudioCaps SPICE 17.6，可匹敌或超过更大 7B Transformer ALM 与 ssLALM-2.8B。联合微调音频编码器优于冻结；更小 SSM 对应更低 τ-effective rank、更高 token 相似度，且尺寸匹配的编码器迁移效果最好。未压缩长序列 (b/c) 未稳定超过压缩 (a)，长序列增加状态更新负担。OpenReasonAQA 使 MMAU-Sound 从约 22.8 升至 56.8（SAM+OR-2.7B），超过 Gemma3n-4B 的 sound 设置。

## 结论
Mamba-2 可作为参数更少却有竞争力的 ALM 骨干；实践上应联合微调编码器、优先紧凑信息丰富的音频 token，并用结构化 BQ/MCQ 监督解锁推理。未来拟探索 SSM–Transformer 混合结构。

## 点评
贡献不只是换骨干，而是用有效秩、编码器互换与连接器消融把“SSM 固定维状态瓶颈”说成可检验的设计原则：编码器会按容量压缩表征，盲目拉长序列未必帮 SSM。相对常见冻结编码器或堆长上下文的路线，这组结论更贴 SSM 归纳偏置。局限是主表仍偏描述/分类，强推理依赖额外数据配方；Clotho 等上并非全面 SOTA，混合架构是否补足全局交互仍待验证。
