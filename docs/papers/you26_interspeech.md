# Uncovering the Impact of G2P Precision on Korean TTS: A Large-Scale Statistical Validation via a Novel Morphological Engine

- 论文编号：887
- 报告人：Heejo You
- 程序：Tuesday 29 September 2026 / Text Processing for Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/you26_interspeech.pdf

## 问题

韩语 G2P 常用 g2pk 延迟高、词界音变不准，相当于给 TTS 喂标签噪声，拖慢收敛并伤可懂度。需可解释、高速、形态深度整合的规则引擎，并用统计严谨方式验证对下游 TTS 的影响。

## 方法

提出规则 G2P：Kiwi 分析后构建 Sentence→Eojeol→Syllable 层次，音节指针连到语素实现 O(1) 边界判定；规则专用隔离词典；按优先级迭代扫描，命中后重置到 Eojeol 首音节再评估，模拟连锁音变。下游用 96 个 VITS（字素 / g2pk / 所提引擎各 32）训 500k 步，去掉 |z|&gt;1.96 离群后做 ANOVA。

## 实验与结果

G2P：平均 3.14 ms vs g2pk 14.98 ms；句级准确率 85.7% vs 27.2%，CER 0.002 vs 0.021。TTS：Proposed 组 CER 显著优于另两组；g2pk 与字素无显著差异。PESQ/WV-MOS 组间不显著，说明可懂度提升不以牺牲声学自然度为代价。训练曲线显示高质量 G2P 更早收敛。

## 结论

作者认为高精度规则 G2P 同时提升速度、可懂度与训练效率；不准确 G2P 不优于直接用字素。剩余错误多来自同形多义与分析器窗口限制。

## 点评

用大规模重复训练 + ANOVA 把“G2P 准不准有没有用”做成可复现的因果证据，方法学上扎实。规则引擎对连锁音变友好、可调试。同形歧义仍是上界；未覆盖神经 G2P/LLM 前端对比，但作为可引导数据的确定性基线价值高。
