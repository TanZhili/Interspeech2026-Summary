# From Words to Sentences: Contextual Predictability Overrides Phonetic Ambiguity in Lexical Competition

- 论文编号：3106
- 报告人：Will Chih-Chao Chang
- 程序：Tuesday 29 September 2026 / Modeling L1 Acquisition
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/chang26g_interspeech.pdf

## 问题
孤立词识别中亚音位细节（如 VOT）梯度调节词汇竞争；句子语境可预测时，该调节是否仍存在，对区分 TRACE（锐化底层）与预测编码/贝叶斯（压制或降权底层）至关重要，既往证据未正交操纵两者。

## 方法
TTS 生成刺激后人工拼接同一套 VOT 连续体 token（No/Some/Max 模糊）。跨通道启动：听音启动 → 视觉探测词汇判断；identity advantage（Identical 快于 Competitor）作竞争消解指标。实验1（N≈58）：孤立词。实验2（N≈60）：嵌入高/低可预测句，并用 GPT-2 差分 surprisal 作连续预测性。

## 实验与结果
实验1：显著 identity advantage，且随 VOT 模糊线性/二次交互缩小，Max 模糊时优势消失。实验2：强 identity advantage，且高可预测语境更大（β=0.022, p<.05；连续 surprisal 亦显著）；但 VOT 与 identity advantage 的交互不再显著（线性/二次及三路均 n.s.）。

## 结论
句子可预测性可覆盖亚音位模糊对词汇竞争的调节，支持预测编码/贝叶斯降权底层证据的观点；孤立词模型未必直接推广到句子理解。

## 点评
正交设计干净，理论分叉明确。刺激为 TTS+拼接，生态效度有限；实验2无 VOT 效应也可能部分来自任务/功率，但与预测性主交互并存，整体仍支持“语境改写竞争动力学”。
