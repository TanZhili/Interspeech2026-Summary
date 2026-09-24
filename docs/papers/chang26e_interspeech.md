# Personalized Electrolaryngeal Voice Conversion with a Single Pre-operative Utterance

- 论文编号：1942
- 报告人：Devin Chang
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/chang26e_interspeech.pdf

## 问题
个性化电子喉语音转换（ELVC）通常需要大量术前自然（NL）录音；临床往往只有极少甚至一句参考。直接对 EL 做零样本 VC 因域失配失败，需在仅一句 NL 参考下同时恢复可懂度与说话人音色。

## 方法
基准前端为 LLE-ELVC（HuBERT 邻域搜索 + WavLM 权重/重建 + HiFi-GAN）。对比：(1) 伪目标：用 FreeVC/Vevo/Seed-VC 把 240 句 NL 音色转到单句术前参考，再监督 LLE-ELVC；(2) 级联：先 LLE-ELVC 恢复可懂度，再零/一次样本 VC 转音色；并做特征级级联（跳过波形重编码）及对 Seed-VC 的监督精炼（LOUO 中间特征 + 伪目标，DTW 对齐）。用健康说话人模拟 EL/NL 对（4 对，TMHINT 320 句，240/40/40）。

## 实验与结果
直接零样本 SER 往往高于原始 EL（如 FreeVC >100%）。级联优于伪目标（Seed-VC 波形级联相似度 0.82 vs 0.74）。特征级 + Seed-VC 精炼：SER 59.65%、相似度 0.84、UTMOS 2.30，优于假设有 240 句术前数据的监督 LLE-ELVC（61.98%、0.75、1.86）。主观 ABX：精炼级联 77.71% 胜、监督基线 9.38%。

## 结论
一句参考下，先 EL 域可懂度再音色迁移的级联更有效；特征级联与监督精炼可进一步压 SER、抬相似度。未来需更大说话人集与真实患者数据、延迟评估。

## 点评
用模拟术前数据把“one-shot 个性化”立成可复现基准，并证明直接零样本不可行。级联把 intelligibility 与 timbre 解耦，与 DSR 两阶段思路一致；真实喉切除术前录音稀缺，当前结论依赖健康人 EL 模拟，迁移到患者仍是关键未解。
