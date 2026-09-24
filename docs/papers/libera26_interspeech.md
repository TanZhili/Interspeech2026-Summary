# WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation

- 论文编号：2803
- 报告人：Luca Della Libera
- 程序：Wednesday 30 September 2026 / Streaming Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/libera26_interspeech.pdf

## 问题
多数语音语言模型依赖文本预训练、多码本层级或混合架构，偏离文本式单流自回归范式。能否用单码本同时建模语义与声学？

## 方法
WavSLM：FocalCodec-Stream 将 WavLM-6 特征压成单流离散 token（50 Hz，可流式，块大小 4，理论延迟 80 ms）；解压特征接 WavLM-large 第 7–24 层作因果骨干，next-chunk 预测（C=4）。无文本监督，约在 Libri-Light 60k 小时训练。变体词汇量 2k/4k/65k（约 305–370M 参数）。滑窗注意力支持持续生成。

## 实验与结果
似然评测：WavSLM-4k 声学一致性 Avg 69.5，多项与更大文本预训练模型可比（如 Spk 88.5、Gend 90.5）。生成：WavSLM-2k UTMOS 3.72、Sim 91.8，优于 LLaMA-Mimi 1.3B/8B 的 UTMOS，且 RTF 更高。消融显示窗口与块大小影响一致性–质量权衡。

## 结论
充分表达的单码本表征可使纯语音、单流、可流式 SLM 在更小规模下达到有竞争力的一致性与生成质量。

## 点评
刻意剥离文本与多码本复杂性，把问题还原为“表征是否够好”。结果支持中层 WavLM+单码本路线；与 7B 级文本预训练模型比参数与数据更省，但口语内容任务仍有差距。
