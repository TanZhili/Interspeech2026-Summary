# Vocal Effort Modulation Strategies: A Cross-Corpus Taxonomy with Noise Robustness and ASR Implications

- 论文编号：2747
- 报告人：Lubos Marcinek
- 程序：Wednesday 30 September 2026 / Phonetic Aspects of TTS and ASR Systems
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/marcinek26_interspeech.pdf

## 问题
Lombard/发声努力下说话人会改 F0、能量、谱倾斜、语速，但个体策略长期被当成均值附近的噪声；尚无对多维声学剖面的正式聚类分类，effort 可控 TTS 也多做统一变换、忽略策略类型。

## 方法
AVID 50 人（25F/25M）四档努力（soft→very loud）：对每人拟合 F0、RMS、谱倾斜、语速相对努力等级的 OLS 斜率，z-score 后 K-means；以稳定性选 k=3。校正 LOSO 多项逻辑回归评估可预测性。验证：(1) 84 万含噪句、12 类噪声、多 SNR 上重聚类 ARI；(2) 法语 FLombard 同流程余弦对应；(3) Whisper-base / Wav2Vec2-base 按簇分层 WER。

## 实验与结果
三簇：C1 High Modulators（高 F0/RMS 斜率，男偏）；C2 Spectro-Temporal（正倾斜斜率、最强减速，女偏）；C3 Conservative（各维变化最小）。ANOVA 各特征 p<10⁻⁵，η²=0.25–0.55。性别关联方向性但不显著（χ²=4.37, p=0.113）。校正 LOSO 准确率 96–98%，macro-F1=0.97。噪声：SNR≥+10 dB 时 ARI≈0.86 可恢复。FLombard Conservative 与 AVID C3 余弦 0.873。ASR：各 SNR 上 WER 次序 C3<C2<C1（大调制反而更差）。

## 结论
发声努力存在三种稳定、可预测的策略类型；高 SNR 下可稳健恢复，跨语料有部分对应；当前 ASR 更惩罚 High Modulator 的大声学偏离。可为簇条件、说话人自适应 TTS/数据增强提供结构。

## 点评
把“努力调节个体差”做成可解释分类法，并对噪声、跨语料、ASR 做三角验证，工程指向明确。轮廓系数一般、GMM 分区不一致，说明策略本质连续；性别效应未显著却常被叙述，需更大样本再谈机制。WER 反序对“越 Lombard 越好识别”的直觉是有力纠偏。
