# Beyond WER: Entity and Disfluency Recall in Accented Conversational ASR

- 论文编号：786
- 报告人：Fiza Husain
- 程序：Tuesday 29 September 2026 / Speech Technologies for Language Learning & Assessment
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/husain26_interspeech.pdf

## 问题
面向印尼、印度、拉美口音会话英语的语言学习场景，商业 ASR 虽 WER 尚可（约 13–21%），但命名实体召回仅约 53–55%、填充停顿召回接近 0（<5%），无法同时支持“逐字流利度反馈”与“实体正确、结构平滑的理解型反馈”。

## 方法
三阶段流水线：(1) 对现有转写做启发式 SQL 过滤（连续大写、缩写、敬称、句中大写等），得到实体密度约随机采样 2.8 倍的数据，每区域 10k；(2) 用 Gemini 2.5 Pro 生成参考转写（每区 250 条人工核验）；(3) 对 Qwen2.5-Omni-3B 按区域训 rank-32 LoRA，单次前向输出 verbatim（保留 um/uh 等）与 corrected 转写。另用六类错误 taxonomy + Claude Sonnet 4.5 法官（与人工 83.8% 一致）做诊断。指标在 verbatim 上算。

## 实验与结果
每区约 2k 持出测试。Qwen-ft-eh：实体召回 80–85%、filler 76–86%、WER 6–10%；相对 Parakeet 实体召回升 26–29pp，WER 相对降 53–60%。优于 Whisper 与 AssemblyAI Universal-3-Pro 的实体召回，并匹配零样本 Qwen3-Omni-30B（参数约 1/10）。EH vs RS 配对 bootstrap：印度/印尼/拉美实体召回分别 +4.19/+2.84/+2.76 pp（p<0.0001）。vLLM 服务 P95 约 800ms。

## 结论
对口音会话 ASR，训什么数据至少同如何训一样关键；轻量实体富集 + 区域 LoRA 可在不引入后处理 LLM 的情况下显著提升实体与停顿召回。局限包括银标参考、filler 仍略低于 30B、尚未覆盖语码转换等多语场景。

## 点评
把语言学习真正关心的实体与填充停顿从 WER 中拆出来评估，数据策展的因果贡献用 bootstrap 钉住，工程上很落地。参考依赖 Gemini、训练数据不可公开，复现与外推需谨慎；双输出格式把“流利度”和“可理解性”绑在同一前向里，是场景契合点。
