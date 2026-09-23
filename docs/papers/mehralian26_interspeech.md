# Predict-Then-Adapt: Inferring Coordinates from Speech for Continuous Geo-Conditioned Dialectal ASR

- 论文编号：3333
- 报告人：Pouya Mehralian
- 程序：Tuesday 29 September 2026 / Language and Dialect Recognition
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/mehralian26_interspeech.pdf

## 问题
连续地理坐标条件（如 GLoRIA）可改善方言 ASR，但推理时常无可靠说话人坐标；离散方言标签又难以刻画连续变异。

## 方法
在冻结编码器上挂轻量 Coordinate Regression Head（CRH）：多头注意力池化 + MLP，SmoothL1 回归经度/纬度。两遍推理：(1) 关闭 GLoRIA 预测 \(\hat{c}\)；(2) 用 \(\hat{c}\) 打开坐标门控低秩适应再解码。骨干为 180M Cascaded Encoder Dual Features（12 层 Conformer + 6 层 Transformer），在 GCND 荷兰方言语料上适配。CRH 增参 <0.1%，时延开销 <3%。

## 实验与结果
CRH 大圆误差随时长下降，约 10–30 s 达 15–25 km 量级（30 s overall avg 23.72 km；插值约 16 km，外推约 38 km）。GLoRIA 对坐标扰动在 ≤15 km 几乎无影响，25 km 平均 <1 个 WER 点。10 s 无元数据设置：CRH+GLoRIA 平均 WER 32.62，优于同秩 LoRA（35.67），接近 oracle 坐标（32.04），远好于 Whisper large-v3 / OWSM。

## 结论
从语音推断坐标足以激活大部分地理条件收益，且保持 GLoRIA 可解释门控；外推区更难，未来可做不确定度感知条件化。

## 点评
把“缺坐标”问题收成可度量的定位误差与 WER 鲁棒半径对齐，工程闭环完整。两遍推理开销可控是亮点。脆弱点在训练坐标流形外的方言（如 Limburgs）与短时（3 s）回归到均值；语言学分辨率限制使误差难压到公里级邻域密度。
