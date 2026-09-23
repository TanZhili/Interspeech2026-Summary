# Deterministic Prompting for Speaker-Stable Low-Resource Greek TTS

- 论文编号：2481
- 报告人：Alexandros Potamianos
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/syllas26_interspeech.pdf

## 问题

现代希腊语缺高质量单说话人语料，低资源 TTS 易损韵律、可懂度与说话人一致性。众包多说话人数据碎片化，全参微调易学成“平均声”；LLM 生成的风格提示在推理时还会引入说话人漂移。

## 方法

数据策展：WhisperX 对齐 + 置信度/时长/声学过滤，整理 CSS10、过滤后 Common Voice（约 15.5 h）与人工核验有声书（约 3.5 h 男声）。在多语言 Parler-TTS（880M）上先全参微调解码器，再用确定性提示（属性分位数分箱、固定拼接）替代 LLM 风格描述，最后在 3.5 h 单说话人数据上做 LoRA（约 25M/5% 参数）锚定身份。推理用统一 canonical 确定性提示与贪心解码。

## 实验与结果

Det.+LoRA：WER 10.7%（人类 ASR 底 7.8%，差 2.9 pp）、CER 3.7%；MOS-I 4.00（人类 4.36）、MOS-C 4.24（人类 4.30）。无 LoRA 时 LLM 提示 WER 更好，加 LoRA 后确定性提示反超（10.7% vs 21.1%）。LLM+LoRA 的 MOS-C 仅 3.56。希腊 VITS 微调未达正式评测质量。失败模式含重音错位、幻觉音节、标点–韵律不匹配。

## 结论

作者认为多语言先验 + 确定性提示 + 说话人 LoRA 是少数据希腊单说话人 TTS 的可行配方；高质量转录比堆时长更重要。局限为单一男声朗读风格与部分主观差异未达显著。

## 点评

把“提示随机性”和“多说话人平均声”拆开治理：确定性提示降条件方差，LoRA 专锚身份，二者协同才稳。客观 SIM-S 仍一般，主观侧重系统内一致性而非严格仿某参考说话人，评价口径需读清。ASR WER 对形态丰富希腊语可能低估/高估感知错误。
