# UG-Bench: A Comprehensive Benchmark for Evaluating Large Audio-Language Models

- 论文编号：1517
- 报告人：Hui Wang
- 程序：Monday 28 September 2026 / Evaluation of Speech and Audio Analysis
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/zhou26c_interspeech.pdf

## 问题

LALM 任务多样，既有基准常偏理解或生成一端、接口不统一，难做可比综合评估；许多开源 LALM 尚不支持语音生成，进一步造成评测盲区。需要同时覆盖理解与生成、可扩展的统一框架。

## 方法

提出 UG-Bench：解耦输入标准化、模型接口、输出统一与任务评测四模块，覆盖四能力——语音感知、音频感知、语音生成、口语语言理解，共 19 任务、36 数据集、约 15.3 万测试样本（ASR/SER/S2TT、音频与音乐描述与分类、TTS、意图分类等）。对 11 个开源 LALM 与 5 个专用语音生成模型零样本评测；按任务内相对名次加权汇总最终排名（多数 LALM 无生成能力时该维排名靠后）。中文等非多数模型支持的任务不计入最终排名。

## 实验与结果

综合排名：Qwen2-Audio 第一（加权分 78.18），其后 Salmonn、WavLLM、Qwen-Audio 等；多数模型 SG 维均为末档。语音感知上 Qwen2-Audio 多项领先（如英文 ASR/翻译相关表现突出）；音频感知上其在多任务上亦居前，Audio-Flamingo 音频理解相对较强但综合靠后。生成侧专用 TTS 模型填补 LALM 空白。作者指出指令跟随与生成质量仍有明显缺口，语义理解有待加强。

## 结论

UG-Bench 提供可扩展的统一评测与加权排名，暴露当前开源 LALM“理解强、生成弱/不一”的格局，并作为后续研究基准。作者认为其有助于推动更全面的多模态语音系统。

## 点评

价值在工程化统一接口与“理解+生成”同台，避免只比单一 ASR/问答。加权排名便于总览，但生成维大量并列末位会压缩区分度；任务/语种覆盖仍偏英为主，模型提示模板差异虽有统一策略，仍可能影响公平性。
