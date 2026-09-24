# Where Do Backdoors Live? A Component-Level Analysis of Backdoor Propagation in Speech Language Models

- 论文编号：2813
- 报告人：Alexandrine Fortier
- 程序：Thursday 1 October 2026 / Speaker Diarization and Recognition
- 技术分类键：diarization
- 全文：https://www.isca-archive.org/interspeech_2026/fortier26_interspeech.pdf

## 问题
Speech LM 由音频编码器、连接器与 LM 拼装而成，常被视为黑盒；音频后门能否跨模态传播、各组件角色如何、多任务共享嵌入中后门是否可分离，尚不清楚。

## 方法
基于可互换的 SpeechLLM 变体：WavLM Large（微调顶 15 层）、三层 CNN 连接器、TinyLlama-1.1B+LoRA。脏标签后门：220ms 打字机点击（0 dB SNR）；ASR 目标句需全时重复触发，其他任务单次触发。攻击 ASR/情感/性别/年龄；基线 AER 跨 WavLM/HuBERT/wav2vec/Whisper。组件分析：单冻结、单训练、传播三类设定，隔离编码器/连接器/LM。另在多任务嵌入上检验后门样本可分离性假设。

## 实验与结果
全管线攻击跨任务高 AER（如 WavLM：ASR 99.2、情感 93.7、性别 94.4、年龄 94.2），良性性能基本保持。隐藏任一组件不足以防护；仅编码器可独自撑起双任务后门。传播攻击中，仅“毒编码器 + 情感”能传入洁净管线（AER 63.5%）。正文还报告：多任务嵌入中毒样与良性样不可直接分离，过滤型防御的可分假设受挑战（抽取后段截断，细节不全）。

## 结论
SLM 对音频后门高度脆弱；后门存续/擦除强烈依赖被攻击组件，编码器最关键；插件式复用预训练组件存在现实威胁。多模态管线应作为有独特脆弱性的系统来防护。

## 点评
组件级消融把“谁在背锅”说清楚，对供应链式预训练复用有直接安全含义。情感任务比 ASR 更易单组件维持，可能因全局标签对局部触发更敏感。全文后半（嵌入分析/结论）抽取截断，可分性结论以摘要与已读章节为准。
