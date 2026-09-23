# Designed Vocalizations Dataset: Sound-Designed Human and Animal Voices for Non-human Voice Conversion

- 论文编号：932
- 报告人：Seolhee Lee
- 程序：Monday 28 September 2026 / Long-Form Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/lee26i_interspeech.pdf

## 问题
人到非人语音转换（H2NH-VC）对游戏/影视等重要，但公开数据与基准稀缺，多依赖内部语料，难以公平对比与泛化评估。

## 方法
发布 Designed Vocalizations Dataset：从 VCTK 与 Freesound 收集言语与非言语源（动物、感叹、拟声等），用 Dehumaniser 2 内置与自研预设（部分经 Cubase 后处理）生成设计音色。训练为非并行 raw/designed；测试为 (source, reference) 对，reference 为同源经预设 \(G_p\) 处理。提供预设风格与源音色的 seen/unseen 划分。用 H2NH-VC 作基线评测。

## 实验与结果
训练约 5,654 源 × 40 预设 → 226,160 设计样本；测试 120 源 × 47 预设 = 5,640。四场景：seen–seen MOS 3.81、Cos.Sim 0.667；unseen–unseen MOS 3.49、Cos.Sim 0.610；交叉约 3.66。能量相关 PCC-E/RMSE-E 跨场景几乎不变；未见源时 CER/WER 反而更低（作者推测转换较弱、输出更接近源）。

## 结论
作者认为该公开数据集与基准可支撑非人设计发声转换的可复现研究，并给出基线结果供后续对比。

## 点评
贡献在资源与评测协议而非新算法：用专业 DSP 预设把“设计音色”可复现化，并显式拆开源/风格泛化。局限是基线仅一个模型，且 ASR 指标在弱转换时可能误导；效果模块覆盖仍可扩展。
