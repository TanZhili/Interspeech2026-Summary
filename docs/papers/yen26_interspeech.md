# MDM-ASR: Bridging Accuracy and Efficiency in ASR with Diffusion-Based Non-Autoregressive Decoding

- 论文编号：488
- 报告人：Sabato Marco Siniscalchi
- 程序：Monday 28 September 2026 / Robust and Efficient ASR
- 技术分类键：asr
- 全文：https://www.isca-archive.org/interspeech_2026/yen26_interspeech.pdf

## 问题
Seq2seq Transformer ASR 中 AR 精度高但逐 token 慢；NAR（含近期扩散/流匹配 ASR）可并行但相对强 AR 仍有明显差距。训练只见 oracle mask、推理却对自生成错误去噪，加剧训练–推理失配。

## 方法
MDM-ASR：预训练语音编码器 + Transformer **离散掩码扩散（MDM）解码器**；非因果自注意力，每步并行预测掩码位置，交叉注意条件于声学。
- **ISCT（Iterative Self-Correction Training）**：先对真值 mask 重建，再对模型自输出再 mask 并二次监督，暴露中间错误；
- **Position-Biased Entropy-Bounded Confidence sampler**：结合熵界与位置偏置的推理采样，权衡步数与质量。
架构其余与常规 encoder–decoder 一致，仅解码策略改为扩散迭代。

## 实验与结果
摘要称在多基准上相对既有 NAR 持续提升，并与强 AR 基线可比，同时保留并行解码效率；文中还计划消融缩放、ISCT 与采样器。
（PDF 抽取在采样器小节截断，具体 WER 表未进入可读全文。）

## 结论
用音频条件 MDM 替换左到右 AR，配合 ISCT 与置信采样，可在保持 NAR 吞吐的同时显著缩小与 AR 的精度鸿沟。

## 点评
把文本 MDM 的双向精炼迁到 ASR，并用自纠训练对症“自生成噪声”，路线清晰。强在与既有流匹配中间分布手搓不同、更数据驱动；**实验数字因抽取截断不可用**，加速比与绝对 WER 需回 PDF。
