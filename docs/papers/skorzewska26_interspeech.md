# Informativity of high-frequency bands on the place of articulation shift in retroflex sibilants produced by children

- 论文编号：2606
- 报告人：Oliwia Skórzewska
- 程序：Tuesday 29 September 2026 / Modeling L1 Acquisition
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/skorzewska26_interspeech.pdf

## 问题
波兰儿童舌尖后擦音/塞擦音易出现部位偏移（sigmatism）；标准分析常低通截止，可能丢掉儿童前腔更短带来的高频诊断线索。需量化至 16 kHz 的噪声能量对部位分类的信息量。

## 方法
PAVSig 库：约 186 名 4–8 岁儿童，分析 /ʂ ʐ tʂ/（文中 IPA）在 retroflex（规范）、dental、postalveolar、interdental 四类部位。帧级提取 28 个 500 Hz 带宽 Noise Energy（至 16 kHz）、摩擦共振峰积分能量 FNE 及其比值 FNER 等共 34 特征；线性混合模型估计部位效应与边际 R²。

## 实验与结果
Dental 实现几乎全频带显著偏离规范，FNER(12,23) 对塞擦音可解释约 29% 部位方差。Interdental 在 8.5–10 kHz（NE13–15）等有特异高频偏离。FNER 相对单带 NE 更稳定且跨清浊更可比。高频至 16 kHz 携带诊断相关信息。

## 结论
扩展高频噪声能量与比值特征可更好刻画儿童卷舌咝音部位偏移，有助于辅助构音障碍评估；新特征提供相对不依赖浊音的度量。

## 点评
针对儿科录音常被“砍频”的实践痛点，用 LME+边际 R² 把频带信息量说清楚。类别极不均衡（interdental 仅 8 人）限制功效；临床落地还需与听感评判/分类器闭环验证。
