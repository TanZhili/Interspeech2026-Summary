# corpusgen: An Open-Source Toolkit for Phoneme-Coverage-Optimized Speech Corpus Design Across Languages

- 论文编号：3603
- 报告人：Fariha Jaigirdar
- 程序：Wednesday 30 September 2026 / Speech Analysis, Data Resources and Research Tools
- 技术分类键：data
- 全文：https://www.isca-archive.org/interspeech_2026/syed26_interspeech.pdf

## 问题
为 TTS/ASR 设计音素覆盖充分的语料仍常依赖语言特定、临时脚本；低资源语言尤缺统一的评估–选择–生成工具链。

## 方法
开源 Python 包 corpusgen：espeak-ng/Phonemizer 做 G2P，PHOIBLE 提供多语音素清单（文称覆盖 2186 语），CoverageTracker 维护音素/双音素/三音素计数。命令分为 evaluate（覆盖率、JSD/熵/PCD、饱和曲线）、select（greedy、CELF、stochastic greedy、ILP、分布感知、NSGA-II）与 generate（仓库检索 / LLM API / 本地模型 + 音位控制评分）。提供 pip、CLI、Python API，Apache-2.0。

## 实验与结果
演示跨英语、孟加拉语、阿拉伯语等流程，比较达 95%/100% 音素覆盖所需句数及 CELF 相对 greedy 的加速。正文称在 12 语系共 40 种语言上验证；强调覆盖优化选择可用显著少于随机基线的句子接近最优音素覆盖（具体数字以演示/视频为主）。

## 结论
把音素覆盖评估、集合覆盖式选择与缺口补全生成收成语言无关工具包，降低低资源语料设计门槛。

## 点评
算法菜单完整、基础设施（PHOIBLE+espeak）务实，对“一起说话”主题友好。G2P/清单映射误差与生成句自然度仍是风险；正文定量对比偏演示叙述，复现需依赖开源包与配套材料。
