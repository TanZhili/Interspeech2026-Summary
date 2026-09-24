# GRATS : A Natural Multi-Speed Mandarin Dataset for Speech Time-Scale Modification Benchmarking

- 论文编号：1842
- 报告人：Yu Tsao
- 程序：Thursday 1 October 2026 / Speech Synthesis Evaluation and Benchmarking
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/aghniya26_interspeech.pdf

## 问题
STSM 评测多依赖英语语料或人工变速参考；普通话是声调语言，音高–时长协调敏感，人工缩放无法代表自然语速下的韵律与发音变化。

## 方法
发布 GRATS：25 名说话人、60 句、五档自然录制语速（0.5×/0.75×/1.0×/1.25×/1.5×），共 7500 条平行句、8.1 小时、44.1 kHz；卡拉 OK 式视觉提示控速，无后处理变速。协议：以自然 1.0× 为输入，系统输出与同说话人同句自然目标语速对比。指标含 Whisper CER、PESQ、STOI、DNSMOS、音节时长 MAE、WORLD F0 相关（MFA 对齐）。

## 实验与结果
Phase Vocoder 各档 CER 最低；CLPCNet 等神经法 DNSMOS/STOI 更好，说明可懂度与听感可脱钩。时长 MAE 在 0.5×/1.5× 呈 U 形升高，F0 相关随极端语速下降。实现语速 α 与标称因子总体对齐但仍有自然偏差。

## 结论
自然多语速平行数据使评测对准“是否接近真实目标语速实现”，而非复现确定性缩放；普通话 STSM 需多指标联合解读。

## 点评
把参考从“缩放后的同一条”换成“同文本再录的目标语速”，对声调语言特别关键。局限是朗读、台湾华语；客观指标不能替代音调忠实度听测。
