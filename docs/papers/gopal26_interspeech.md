# Language-Aware Distillation for Multilingual Instruction-Following Speech LLMs with ASR-Only Supervision

- 论文编号：2446
- 报告人：Shreyas Gopal
- 程序：Thursday 1 October 2026 / Cross-Lingual and Multilingual Speech Recognition 2
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/gopal26_interspeech.pdf

## 问题
用 ASR 配对数据做上下文蒸馏可训英语 Speech LLM，但多语共用静态 Q-Former query 易语言干扰，低资源语被主导语淹没；大规模任务 SFT 又昂贵。

## 方法
冻结 Whisper-large-v3 编码器与 Llama-SEA-LION-v3-8B-IT；可训 Q-Former + 语言感知模块：query bank（每语一组）与门控网络（卷积 LID 或注意力池化），对输入语音做 soft 混合或 hard 选择（STE）；调度教师强迫稳定早期门控。损失：输入蒸馏（音频尾嵌入对齐文本头）、输出蒸馏（LLM 末隐状态对齐）+ LID CE。仅用约 5.8K 小时多语 ASR 数据。

## 实验与结果
相对匹配多语基线 ML-DiVA：开放指令跟随平均约 +14%（hard-gating；印尼 3.04→3.71）。自建 Audio-MLQA 上相对既有 Speech LLM 基线约 +32%；相对 ML-DiVA 闭集平均约 +3%（3.96 vs 3.85）。消融：L=256 显著降蒸馏损失；硬选择优于软混合；两种门控 LID 准确率均 >94.9%。

## 结论
语言感知 query 路由可在 ASR-only、骨干冻结条件下缓解多语干扰，高效扩展指令跟随与口语 QA；并释放多语评测数据。

## 点评
在 DiVA 式蒸馏上加 LID 门控，用最小可训容量打多语，工程上很实用。评测依赖 GPT-4.1 与 TTS 合成问句，与真实口音/噪声分布有差距；中文相对最弱、与主导语差异大，说明 bank 规模与数据配比仍是瓶颈。
