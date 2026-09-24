# PolyBench: Benchmarking LLM-based TTS Systems for Chinese Polyphone Disambiguation

- 论文编号：998
- 报告人：Feifan Chen
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lu26_interspeech.pdf

## 问题
LLM-TTS 直接吃文本、多音字消歧隐式完成，ASR 的 CER/WER 难抓发音错；既有中文多音字评测集存在标注错误、覆盖不足与领域偏斜。

## 方法
构建 PolyBench：从《现代汉语词典》第 7 版筛出 494 个高频多音字与 88 个多音词，DeepSeek 生成句子并人工校对，得 Main（6016 句，含 Common/Surname/Dialectal/Colloquial/Literary）、DictWords（2137 词）与 ALLinONE（494 句、同句多读）。用 Qwen3-Omni-Instruct 自动标发音（ALLinONE 上标注准确率 93.06%，接近人工）。评测 3 个 G2P 与 17 个 LLM-TTS，指标 CER、Poly-CharAcc、Poly-PyAcc。

## 实验与结果
Main 上 FireRedTTS-2 最佳，Poly-PyAcc 82.02%（Common 86.01%），仍有约 18% 错读；方言/口语类全面偏低。CharAcc 系统间差约 4%，PyAcc 差约 15%，且 PyAcc 常低于 CharAcc 10–20 个百分点。DictWords 上多数更高、系统差距更大；ALLinONE 上最优也仅 202/494 字全对。G2PW 在姓氏/文言类仍有竞争力。

## 结论
PolyBench 暴露当前 LLM-TTS 多音字消歧仍不足，尤其方言与口语；Qwen3-Omni 可作大规模自动标注器。未来拟扩大字表并改进拼音标注。

## 点评
把“能认出字 ≠ 读对音”拆成 CharAcc/PyAcc，击中 LLM-TTS 评测盲区。自动标注误差会扰动绝对值，但大差距排名仍可用；口语类与词典标音本就不一致时，低分可能混入标注定义问题。
