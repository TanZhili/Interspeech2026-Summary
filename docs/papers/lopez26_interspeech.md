# Robustness Assessment of Large Audio Language Models in Multiple-choice Evaluation

- 论文编号：2503
- 报告人：Fernando López
- 程序：Tuesday 29 September 2026 / Audio & Speech Language Models: Evaluation, Representations, and Emerging Capabilities
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/lopez26_interspeech.pdf

## 问题
LALM 多用 MCQA 报单一准确率，但对选项顺序、题干/正答/干扰项措辞敏感，且题面文本可能含捷径，使模型不听音频也能答题；现有框架很少量化这些脆弱性。

## 方法
固定音频，对 MMAU（test-mini）、MMAR、MMSU 施加孤立与混合扰动：全部 24 种选项排列；用 gemini-2.5-flash 与 gemma-3-12b-it 生成题干/正答/干扰项各 7 版（含原文）；混合扰动以 0.5 概率独立施加各改动。评测 Audio Flamingo 2/3、Qwen2.5-Omni-7B、Kimi-Audio-7B-Instruct，并加无音频文本 LLM 对照。指标含准确率均值/方差/极值、Consistency Rate（CR）与更严的 Correctness Rate（CoR，须在全部扰动下都答对）。

## 实验与结果
默认设定与公开报告接近。文本 LLM 可明显高于随机，如 gemma-3-27B-it 在 MMAU 达 48.3%（高于随机约 22.6 点）。选项顺序与题干改写方差中等；正答改写方差升高；干扰项改写冲击最大（如 AF2 在 MMAU 准确率 std 达 13.7%）。混合扰动下 CoR 显著低于均值准确率。AF3 总体准确率与稳健性较好；Qwen2.5-Omni 对干扰项改写 CoR 更稳；AF2 最弱。模型偏好更长选项（选最长项约 42–52%，而数据中最长为正答约 45%；当最长为正答时选中率升至约 71–78%）。

## 结论
MCQA 准确率会被语言偏置与措辞扰动抬高或剧烈波动；建议以文本对照为基线，并用混合扰动 + CoR 做可负担的稳健性评测。

## 点评
把“听懂了还是读题蒙对了”拆开，用无音频 LLM 与扰动方差直接打脸单点准确率排行榜。CoR 比均值 accuracy 更能暴露脆弱模型。扰动靠 LLM 改写，虽抽样人工校验语义保留，仍可能引入风格分布偏移；本文刻意固定音频，信号级稳健性留作正交方向。
