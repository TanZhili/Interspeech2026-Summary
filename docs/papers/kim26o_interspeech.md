# AdaTT: Text-Guided Instrument Timbre Transfer with Target-Adaptive Structural Control

- 论文编号：1828
- 报告人：Dabin Kim
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/kim26o_interspeech.pdf

## 问题
乐器音色迁移需保留谱级内容（旋律/节奏），又要把源乐器特有的表现细节（如小提琴音高主导颤音）改写成目标乐器习惯。标准 ControlNet 刚性复制细粒度控制，易造成音色歧义与不自然。

## 方法
在冻结 Stable Audio Open 上建 SAO-ControlNet，注入量化 \(f_0\)（CREPE）与 RMS 控制。AdaTT 加 CSP（帧级缩放 ControlNet 输出）与 TG-CSP（文本引导、分别缩放 \(f_0\)/RMS 通道）。半自动造数：按音高簇内跨乐器对，网格搜索 \(\alpha,\beta\) 再专家筛选，得 1321 对迁移伪标签（约 4.4h）。两阶段训练：先重构 ControlNet，再冻结其上训 AdaTT。

## 实验与结果
URMP+Solos，13 乐器。AdaTT：CLAP 0.490、F1 MIDI 0.302、KAD 0.495；主观 TIM/NAT/STR/QUL 均优于 ControlNet 与 SmartControl。相对 MusicMagus/ZETA 等推理编辑，结构保持（F1 MIDI）与质量优势明显。控制分辨率过细会抬 Chroma、压 CLAP，折中取 144-bin \(f_0\) + 32-bin RMS。

## 结论
文本自适应缩放异构结构控制，可在保持谱级内容的同时提升目标音色保真与自然度。局限：仅单声部，不保留空间混响等线索。

## 点评
问题切到“表现细节≠谱级内容”，比单纯“保旋律换音色”更细。TG-CSP 在输入端拆开 pitch/loudness 再文本调制，直接针对异构控制纠缠。伪标签依赖 SAO-ControlNet 网格搜索+专家，可扩展性与偏差需注意；单声部设定也限制真实编曲场景。
