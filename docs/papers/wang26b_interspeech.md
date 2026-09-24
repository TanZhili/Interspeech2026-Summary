# FoleyGenEx: Unified Video-to-Audio Generation with Multi-Modal Control, Temporal Alignment, and Semantic Precision

- 论文编号：112
- 报告人：Shiyao Wang
- 程序：Wednesday 30 September 2026 / Generative Audio and Music
- 技术分类键：singing
- 全文：https://www.isca-archive.org/interspeech_2026/wang26b_interspeech.pdf

## 问题
现有视频到音频方法常在“多模态可控”与“帧级时序对齐”之间权衡：MultiFoley 可控但同步弱，MMAudio 同步强但缺参考音频条件与细粒度副词语义。

## 方法
FoleyGenEx 基于 MMDiT：条件注入参考音频以支持 AC-VTA/Foley 扩展；多模态动态掩码保证训推一致；掩码 MSE 聚焦对齐段；副词增强（速度/距离/音量信号处理 + LLM 重写字幕）强化语义精度。统一支持 TTA、VTA、TC-VTA、AC-VTA、FE 与潜空间局部编辑。

## 实验与结果
AudioCaps：CLAP_T 达 0.364/0.366（+AA），优于 MMAudio 0.348。VGGSound：FD_VGG 0.73–0.74、IS≈18.4–18.5，与 MMAudio 同步接近并在多项上更优。正文报告在 Greatest Hits 等上也具竞争力。

## 结论
在单一框架内同时获得强同步、参考音频可控与更细语义控制，缩小既有方法之间的能力缺口。

## 点评
掩码对齐 + 参考音频注入是对 MMAudio 生态的务实扩展；副词增强针对数据稀缺很对症。代价是系统复杂、依赖 Synchformer/CLIP，且副词控制的主观/定量评测细节正文相对简略。
