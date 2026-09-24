# FlashTTS: Fast Streaming TTS with MTP Acceleration and X-pred Mean Flow Distillation

- 论文编号：1692
- 报告人：Hanke Xie
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/xie26b_interspeech.pdf

## 问题
对话系统要求 TTS 低延迟且支持流式文本输入；单码本 LLM-TTS 常需缓冲整句，自回归慢且多步流匹配抬高首包延迟。

## 方法
FlashTTS（Qwen2.5-0.5B）：滞后多轨堆叠输入（语音/文本/语言并行）支持增量文本；Stage2 加 Multi-Token Prediction 并行预测多 token；声学端用 X-pred mean flow + 块注意力，2-NFE 出 Mel，再 HiFi-GAN。约 30 万小时开源数据训练。与 CosyVoice2（10-NFE）等同规模基线对比。

## 实验与结果
MiniMax 多语子集：MTP-3（2-NFE）FPL 325 ms、TPS 73、RTF 0.632、WER 18.8、SIM 0.695；相对 CosyVoice2 的 FPL 843 ms/RTF 0.913/WER 26.2 明显更快更清晰。Stage1 2-NFE FPL 377 ms。CMOS 与基线接近或略优。

## 结论
原生流式输入轨 + MTP + 2-NFE mean flow 可把首包延迟压到约 325 ms，同时保持零样本克隆与跨语可懂度，适合作对话级联 TTS。

## 点评
同时砍“等整句”与“慢解码”两条延迟路径，工程完整。MTP 抬速时对 SIM/CMOS 有轻微代价，需按场景选 MTP-3/5。
