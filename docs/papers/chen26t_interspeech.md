# A Preclinical Study of Electrolaryngeal Voice Conversion for a Novel Nasal Electrolarynx: Feature Choice and Data Augmentation

- 论文编号：1882
- 报告人：Ming-Chi Yen
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/chen26t_interspeech.pdf

## 问题
新型鼻式电子喉（NEL）声学异于颈式电子喉（CEL）：中高频共振、低频衰减、元音共振峰抬高；既有 ELVC 多针对 CEL，特征选择与数据稀缺下 NEL-to-NL 是否可直接套用尚不清楚。

## 方法
在统一 seq2seq 框架比较 VTN-VC 与带额外 VC 预训练的 ETN-VC，输入分别为 80 维 Mel 或 WavLM-Large 第 6 层特征。数据增强：F5-TTS 由 TWnews 生成 sNL，再用 LLE-VC（WavLM 邻域搜索，可选重建 WavLM 或对应 Mel）合成配对 sNEL，供 ETN 预训练后在真实 NEL–NL 上微调。预临床设置：同一健康说话人录 320 句 TMHINT（NL/CEL 录音棚，NEL 病房），240/40/40。

## 实验与结果
特征偏好设备相关：CEL-to-NL 更宜 WavLM（VTN SER 57.5%），NEL-to-NL 更宜 Mel（VTN SER 58.8% vs WavLM 62.0%）。ETN+Mel+10k 增强：CER/SER 降至 63.0%/53.8%（相对 VTN Mel 的 72.0%/58.8%）。A/B 可懂度：Mel 优于 WavLM，ETN Mel 优于 VTN Mel。UTMOS 等神经质量分则偏向 WavLM，与可懂度指标存在折中；零样本 SeedVC/Vevo 等对 CEL/NEL SER 仍很高。

## 结论
NEL 的设备特异频谱使 Mel 比通用 SSL 特征更保声学线索；LLE-VC 增强可稳定提升 NEL 转换。单健康说话人预临床，需真实患者 NEL 与自然度 MOS 验证。

## 点评
把“特征是否通用”做成 CEL/NEL 对照实验，结论清晰：SSL 预训练偏 NL，可能抹掉 NEL 共振。医疗场景优先 CER/SER 与听测而非 UTMOS 的取舍合理；病房噪声与单说话人设计限制了对外推广的强度。
