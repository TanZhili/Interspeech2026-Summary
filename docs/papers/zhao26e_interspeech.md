# Decoding Order Matters in Autoregressive Speech Synthesis

- 论文编号：1339
- 报告人：Minghui Zhao
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhao26e_interspeech.pdf

## 问题
自回归语音合成默认从左到右生成，但声学依赖含全局韵律与前后协同发音；解码顺序是否最优、如何在统一框架比较，尚缺系统研究。

## 方法
用掩码扩散（MDM）训练顺序无关模型，推理可任意置换逐帧解掩。为隔离编码器归纳偏置，对 Mel 做参数无关标量量化（Q=100）并用现成 HiFi-GAN。比较 l2r、r2l、随机、top1 置信自适应、时长引导段内随机，以及 β 控制的随机插值。

## 实验与结果
LJSpeech：r2l 多项客观指标优于 l2r；top1 MOS 3.91（系统输出最高），vocoded 参考 3.99，r2l 3.87，uro 最差 3.50。top1 局部多为右→左连续扩展（ρ_r2l≈0.9）。量化 Mel 仍可被 HiFi-GAN 较好重建。随机性增大时 MCD 降、UTMOS 降，WER 非单调。

## 结论
左到右并非最优；有效顺序常保持局部连续帧簇并偏向局部右到左，以兼顾长程依赖与局部连贯。解码顺序应作为合成质量的关键建模选择。

## 点评
用 MDM + 标量 Mel 把“顺序”从 token 学习中干净拆出，结论有说服力。单说话人朗读语料与帧级更新限制外推；是否迁移到多说话人/神经编解码 token 仍待验证。
