# Emergence of Phonetic Representations in EMG-based Silent Speech Interfaces

- 论文编号：2499
- 报告人：Guillaume Toussaint
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/toussaint26_interspeech.txt

## 问题
表面 EMG 静默语音接口标注稀缺；不清楚不同任务（合成/识别/音素分类/对比预训练）学到的表征是否含音素信息，以及 SSL 预训练为何对合成帮助有限。

## 方法
在 Gaddy & Klein 单说话人 18.6h EMG–音频数据上，用残差卷积+12 层 Conformer，训练 EMG→mel（MSE）、→音素（CE）、联合、→字符（CTC），以及 emg2vec 对比预训练再微调。用线性探测评估音素可分性与 mel 回归；Wav2Vec2 算合成 WER；UMAP 可视化。

## 实验与结果
联合任务线性探测音素准确率最高（约 84%）；仅 mel 回归也可达约 74–80%（中层更好）。CTC 识别特征亦出现音素簇。对比预训练探测仅约 37–38%，接近随机，UMAP 无音素簇。不含 MSE 的设置合成 WER 大幅变差，说明声学回归损失对可懂合成必不可少；对比预训练对合成/音素探测无实质提升。

## 结论
EMG 模型即使无显式音素监督也会涌现线性可分音素表征；可懂合成依赖声学回归目标；现有对比 SSL 学到的空间与音素/合成需求错位。

## 点评
用线性探测系统拆开“表征里有没有音素”与“下游能不能合成”，解释了此前 SSL 对合成帮助微弱的现象。单说话人设定限制泛化结论；中层比末层更富音素信息对探针层选择有启示。
