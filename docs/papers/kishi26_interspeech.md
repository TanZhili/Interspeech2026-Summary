# Do speech foundation models perceive speaker similarity as humans do?

- 论文编号：1172
- 报告人：Hayato Yagi
- 程序：Tuesday 29 September 2026 / Speech Production and Perception 1
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/kishi26_interspeech.pdf

## 问题
语音基础模型嵌入可用于说话人验证，但其嵌入距离是否对应人类对「像不像」的连续相似度判断，尚不清楚。

## 方法
用 40+ 模型（Whisper、WavLM、HuBERT、Parakeet、Qwen3-TTS 等）逐层提说话人嵌入，算说话人对余弦距离，与人类感知相似度图（7 分量表均值）比 Spearman 相关（SRCC）；再做多元回归，量化训练目标、规模、层深等配置对对齐的贡献。

## 实验与结果
中间层常对齐较好，相关随层深变化因模型而异；部分 TTS 模型整体对应较低。配置回归显示哪些因素更促成人感对齐。正文图示相关分布于约 0–1 区间，具体最优 SRCC 以图/表为准。结论指向更感知对齐的基础模型设计。

## 结论
嵌入几何与人类相似度部分可对齐但非普遍；层位置与训练设定是关键杠杆。

## 点评
把「会验证」推进到「像人类那样量相似度」，评测面很宽。强在模型覆盖与层析；脆弱点在人类量表噪声与语料/语言覆盖有限，对齐高不等于身份感知机制同构。
