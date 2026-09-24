# CSER: Semantic Evaluation of LLM Auto-Repair for Code-Switching ASR

- 论文编号：3390
- 报告人：Tien Dat Bui
- 程序：Thursday 1 October 2026 / Speech Benchmarks, Evaluation, and Resources
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/bui26_interspeech.pdf

## 问题
语码转换（CS）ASR 仍主要用 WER/CER/PIER 等字符串匹配指标；在 ASR–LLM 语音助手中，音译/同音误识可能仍保留意图，传统指标无法衡量语义保持与 LLM 自动修复后的下游意图质量。

## 方法
提出 Code-Switching Semantic Error Rate（CSER）：ASR 假设经 LLM 做 CS 感知规范化（映射音译 OOV、保结构、去标点小写、禁止幻觉新内容）后，由另一 LLM 从参考生成针对 CS 实体与意图谓词的探测问题，再抽取参考/假设答案并由判别器判等价，CSER=1−问题级成功率。配套越–英 CS 基准：爬取种子实体 + GPT-4o 造句，人工录制（句内/句间）与 TTS（多样/媒体域）四套测试集，训练集约 794K 句。对比 Azure、Google v1/Chirp 3 等商用系统，以及 Conformer-CTC 的 VN / VN-EN Phonetic / VN-EN 训练体制；评测用 Gemini 2.0 Flash 作裁判，与数据生成模型族分离。

## 实验与结果
Phonetic 训练常 PIER 远差于正字法 CS 训练（如 Set 4：58.65 vs 24.72），但 CSER 接近（12.16 vs 10.08），说明 LLM 可修复“phay buc→Facebook”类音译。Google Chirp 3 各集 CSER 最低（约 10.47/9.14/22.03/23.52）；Google v1 在部分集 WER 尚可但 CSER 很高（Set 4 达 51.33）。VN 单语在 Set 2 PIER 82.10 但 CSER 仅 17.20，相对 VN-EN 的 CSER 改善远小于 PIER 暗示的幅度。

## 结论
作者认为面向意图的 CSER 是 CS ASR–LLM 管线的必要补充，能反映音译的语义韧性；目标 CS 训练（含 phonetic）可接近生产级语义表现。局限包括计算开销与裁判偏差风险，未来拟做人相关与蒸馏裁判。

## 点评
把评测目标从“词对不对”挪到“意图能不能过 LLM 修复”，对助手场景很贴切。CSER 强依赖规范化与裁判 LLM 设定，测的是管线上限而非纯 ASR；与 PIER 并读才看得出“词错但语义可救”的悖论。
