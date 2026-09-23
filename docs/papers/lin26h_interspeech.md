# Improving Cross-Dataset Speech Intelligibility Prediction for Hearing-Impaired Listeners with Few-Shot Adaptation

- 论文编号：1567
- 报告人：Guojian Lin
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/lin26h_interspeech.pdf

## 问题

听障可懂度预测模型跨数据集（听者、声学、助听器设定）性能骤降；主观标注昂贵，目标域标签稀缺。仅靠增广或点对点回归，难以在少样本下学到可区分高/低可懂度的域不变表示。

## 方法

提出 CFA-SIPNet：源域（CPC3）监督预训练 + 目标域少样本适配。双通道 WavLM/Whisper 融合后经位置编码与三层 Transformer；预训练损失为 MSE + 排序对比损失。适配时冻结 SFM 与 Transformer，只更新插入各层的 bottleneck adapter（128 维）、embedding 模块与评分 MLP；并用基于真值差阈值 τ=0.4 的 embedding 对比损失，总损失加权 MSE、排序与 embedding 对比。

## 实验与结果

源域 CPC3（约 15k 训练）；目标域 Arehart 听障子集 8100 句，12 听者训练/3 未见听者测试。每听者抽 100 句作 few-shot（&lt;20% 目标训练量）。跨数据集：RMSE 26.05、PCC 0.75，优于 ZipEnhancer+MP-SENet 的 2-Clips（28.48/0.72）与零样本，并优于多数全量域内训练结果。相对该 SOTA 相对 RMSE 降 8.5%、PCC 升 4.2%。消融显示去掉 adapter+对比或源预训练均变差；few-shot 适配优于联合训练/全参微调/仅域内训练。

## 结论

作者认为源预训练与少样本适配互补，能以少量目标标注达到甚至超过全量域内训练的跨集泛化，适合听障可懂度评估落地。

## 点评

抓住“标签贵、域移大”：用冻结骨干 + 轻量 adapter 与可懂度结构对比，比盲目 2-Clips 增广更省标注。few-shot 抽样强调分数均匀，避免适配偏到某一分数段。目前在 CPC3→Arehart 设定上验证；听者与采样率差异大，换更复杂声学或更广听者时还需检验。
