# One-to-Many Electrolaryngeal Voice Conversion with Synthetic Data

- 论文编号：2150
- 报告人：Carlos Toshinori Ishi
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/wu26l_interspeech.pdf

## 问题
电子喉到自然语音（EL2NL）的时间对齐 VC（保节奏）数据极缺；多数用户无术前录音，需要一对多目标音色。仅压平 F0 的伪 EL 频谱不像真 EL，限制转换质量。

## 方法
三步：在 JVS 上预训练日语 QuickVC（QVC）；用 1 名喉切除患者约 13 分钟（100 句）EL，冻结 Whisper 编码器微调得 NL2EL，把 JVS 约 12998 句转为合成对齐 EL；再用合成对监督微调预训练 QVC 做一对多 EL2NL——Whisper 编码器吃合成 EL、说话人编码器吃对应 NL，只更新内容编码器与 flow，冻结说话人编码器以防从目标句偷语调。对比 QVC、QVC-mix、flat-F0 及 ours-100/1k/10k。

## 实验与结果
合成 EL 相对真 EL 的 MCD：ours 5.942 vs flat-F0 11.916。EL2NL：ours-10k 在 F0 RMSE/CORR、CER、音色相似度上优于基线（如 CER 0.366、Sim 0.923）；更多合成数据更好。主观（97 人）：相对 QVC / flat-F0 的 N-CMOS、I-CMOS 显著为正；S-MOS 3.03（真值对 4.51）。局限：/h/ 等难发音、仅中性语调。

## 结论
从小规模真 EL 学出频谱匹配的合成 EL，再规模化监督一对多 EL2NL，可同时提升语调自然度与可懂度，并保留多目标音色选择。未来需改进音素与表情语调。

## 点评
“先 NL→EL 造对齐数据，再 EL→NL”把稀缺瓶颈转成可扩展合成，比 flat-F0 更贴 EL 频谱。冻结说话人编码器以防语调泄漏是细腻设计。单患者日语数据与中性语调限制了跨语言/个性化表达；S-MOS 与真值差距说明一对多音色仍有空间。
