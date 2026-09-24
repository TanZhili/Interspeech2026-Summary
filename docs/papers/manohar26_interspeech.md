# SCRIBE: Diagnostic Evaluation and Rich Transcription Models for Indic ASR

- 论文编号：3436
- 报告人：Kavya Manohar
- 程序：Wednesday 30 September 2026 / Robust and Real-World ASR Systems
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/manohar26_interspeech.pdf

## 问题
ASR 作为听写工具时，纠错成本取决于错误类型而非计数；WER 把词法/标点/数字/实体混成标量，并对黏着语 sandhi 合法合并施加结构性惩罚（可相对抬高约 30%）。印地语系富文本转写缺乏可操作诊断。

## 方法
SCRIBE：输出诊断向量 [ERlex, ERpunc, ERnum, ERent]，经 sandhi 容忍对齐与领域词表注入；聚合为 SCRIBE-WER。配套 LLM（Gemini）策展管线把 verbatim 转富文本，并发布 FLEURS-RO、IN22-Legal 基准与 Hindi/Malayalam/Kannada 开源富转写模型（Whisper 三阶段微调）。

## 实验与结果
相对 IndicWhisper/IndicConformer，SCRIBE-ASR 在 FLEURS-RO 与法律 OOD 上 WER/WERS 更低；数字错误近饱和（ERnum 常 <1%）。马来alam 法律集 WER 44.52% 而 ERlex 仅 15.96%，显示约 30% 相对膨胀来自形态对齐。人工评分：SCRIBE 分项与专家 Spearman |ρ| 约 0.36–0.92，WER 在多维（尤其马来alam）不显著。标点仍是主瓶颈。

## 结论
分类诊断 + sandhi 对齐使评测对齐专家纠错成本；富转写模型与开源工具为印地 ASR 提供可行动反馈回路。

## 点评
把“听写可用性”从 WER 单标量拆开，对黏着语尤其关键。人评验证强。策展依赖 LLM，残留幻觉需人工把关；标点仍难，说明诊断清楚后下一步应攻韵律/边界。
