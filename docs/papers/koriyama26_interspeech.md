# Benchmarking Large Language Models for Grapheme-to-Phoneme Conversion: A Japanese Case Study

- 论文编号：1800
- 报告人：Tomoki Koriyama
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/koriyama26_interspeech.pdf

## 问题
日语 G2P 需分词、多音汉字与数词–量词不规则读法；端到端 TTS 隐含学读音但可控性与稳健性不足。LLM 是否能替代传统形态分析器，以及何种调用方式更稳，尚缺大规模基准。

## 方法
两种模式：parse——LLM 做形态分析并输出各词假名，再规则后处理助词读法与长音规范化；direct——LLM 一步输出整句假名。在 JVS nonpara30 的 3000 句人工假名标注上算 kana CER；评测 30+ 专有/开源 LLM 与 OpenJTalk、MeCab 等传统工具。另将 LLM 假名喂入 LoRA 微调的假名输入 CosyVoice 2，与 E2E TTS 比发音 CER 与 UTMOS。

## 实验与结果
Claude Opus 4.6 parse CER 0.52%、Gemini 3.1 Pro direct 0.53%，优于最佳传统工具 OpenJTalk 1.03%。多数模型 parse 优于 direct；规模与日语持续预训练（Swallow）显著降错。假名 TTS：Gemini 3.1 Pro 假名 CER 2.38%（oracle 2.10%），低于 Gemini 2.5 Flash TTS 等 E2E（3.96%+），UTMOS 相当。

## 结论
强 LLM + 规则后处理可超传统日语 G2P；显式 G2P 再假名合成在发音准确上优于直接文本 E2E，且不明显损自然度。

## 点评
把“难规则”留给确定性后处理、把分词与读音估计留给 LLM，是务实的工程拆分。小模型 direct 极易崩；parse 在数词–量词切碎时也会引入错误，说明级联并非万能。基准句子来自 JVS，对更野文本泛化仍待验。
