# Beyond Speaker Independence: Evaluating Cross-Lingual Acoustic-to-Articulatory Inversion Across Finnish and Russian

- 论文编号：1914
- 报告人：Ruchi Pandey
- 程序：Tuesday 29 September 2026 / Cross-Linguistic and L2 Phonetic Studies
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/pandey26_interspeech.pdf

## 问题
声学到发音转换（AAI）在说话人属性与跨语言域偏移下易退化；既有 EMA 数据偏英语、说话人少，且先前跨语言研究常把语言与录制协议混淆，也少单独剥离性别因素。本文要在统一录制协议的芬兰–俄语双语语料上建立说话人无关基准，并量化跨性别与跨语言偏移。

## 方法
在 FROST-EMA（18 名双语者，仅用 L1）上做标准化预处理：插值、20 Hz 低通、1250→50 Hz、按句 z-score。目标为原始 10 维 EMA 或 5 维 tract variables（LA、LP、TTCL、TBCL、TDCL）。前端：MFCC 或冻结的 Wav2Vec2 / XLSR-53 / MMS-300；后端：BiLSTM 或轻量注意力 Attn-lite；MSE 训练。评估协议含组内 LOSO、语内跨性别、性别内跨语言及 L+G 组合。

## 实验与结果
域内：舌传感器优于唇，Z 轴优于 X；TV 中 LA 中等、LP 最弱。跨性别相对域内约降 Δr≈0.05–0.10，且存在方向不对称。跨语言降幅更大（约 0.10–0.20），L+G 最差；舌 CL 在跨语言时退化更明显。消融：Wav2Vec2 与 MMS 优于 MFCC，XLSR-53 较弱；BiLSTM 整体优于 Attn-lite；TV 与 EMA 聚合相关相近但 TV 更利于诊断。

## 结论
语言错配比性别错配损害更大，二者叠加最差；SSL 前端排名在偏移下大体保持；循环结构在低资源 EMA 上更有利。未来将扩展到 L2/口音条件与说话人自适应。

## 点评
贡献在于用同一语料协议把性别与语言偏移拆开，并系统扫前端/目标/后端，对非英语 AAI 很有参考价值。脆弱点是 RUS-F 仅 2 人、部分跨域数字需谨慎；且仅 L1、无腭迹导致省略 CD，跨语言对“部位/腭化”相关维度的退化解释仍偏推断。
