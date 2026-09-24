# Stabilizing Instruction Supervision for Instruct-TTS via Controllable Diversification and Drift Filtering

- 论文编号：1227
- 报告人：Yizhong Geng
- 程序：Tuesday 29 September 2026 / Instruction-following and Controllable Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/geng26b_interspeech.pdf

## 问题
Instruct-TTS 常用 LLM 把结构化标签改写成自然语言指令，但无约束改写超过 40% 存在语义漂移（执行化、角色扮演、改属性），污染监督并削弱泛化；单纯扩多样性与单纯过滤也无法兼顾覆盖与保真。

## 方法
数据中心稳定配方：(1) 音高/语速/音量扰动 + 模板属性提示做属性对齐监督；(2) 约束人设×句法×属性槽位的可控多样化改写；(3) 异族 LLM 验证器打分投票过滤三类漂移。在 CosyVoice 2 上对中文约 90h 语料做 SFT，评 InstructTTSEval（中文）APS/DSD/RP。

## 实验与结果
约束改写使漂移 40.4%→15.4%。完整配方指令跟随平均准确率 56.4%（无 SFT 34.5%，朴素 SFT 51.0%），NR/CMOS 均 4.16。消融：去漂移过滤伤害最大（→48.9%）；去多样化与去属性监督亦降点；属性监督对音高/语速/音量 APS 增益最大。

## 结论
指令监督不稳定主要是数据质量问题；覆盖扩展、漂移过滤与属性对齐三者互补，过滤是最大单项贡献。漂移分类或可推广到其他指令生成任务。

## 点评
把 TTS 标签改写中的失败模式显性分类并量化，比“再换模型”更切中要害。评测依赖 Gemini judge，作者用多模型族缓解自评估偏差；情感维度上朴素 SFT 有时更高，说明过滤也可能去掉部分有用的情绪描述，需权衡保真与覆盖。
