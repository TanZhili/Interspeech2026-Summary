# TDScore: Learning Synthetic Speech Quality Predictors from TTS Training Dynamics without Human annotation

- 论文编号：449
- 报告人：Natacha Miniconi
- 程序：Wednesday 30 September 2026 / Speech Synthesis Evaluation 2
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/miniconi26_interspeech.pdf

## 问题
主观听测贵、难扩展；有监督 MOS 预测器仍依赖大量人工标注，且跨语言/合成范式泛化差。需要不依赖听者标注、又能服务 TTS 开发（如 checkpoint 选择）的质量信号。

## 方法
TDScore：从零训练 TTS，定期合成并收集中间 checkpoint 音频，用训练迭代 k 与训练 loss 作伪标签；用外部客观质量曲线截断饱和 checkpoint，并加入自然参考句。基于 SSL-MOS 架构，分别训练预测归一化迭代（Ite）与标准化 loss 的模型，用 pairwise ranking（BCE over score differences）。TTS 骨干：FastSpeech 2、FastPitch、F5-TTS，均在 Blizzard 2023 法语 NEB 约 51h 上训练。

## 实验与结果
域内 BC（法）：TDScore–F5–Ite 系统/句级 SRCC 0.74/0.54，优于 DeepFake proxy（0.60/0.50）等无 MOS 方法，并接近/超过部分有监督结果。域外 BVCC：F5–Ite 0.73/0.66；SOMOS：0.38/0.22。迭代预测在自建测试集上最强（F5–Ite 句级 0.90）；loss 预测更不稳，且整体 Ite 优于 Loss。作者归因于 loss 振荡、迭代更能表征学习状态，且 F5 训练中质量提升更平滑。

## 结论
TTS 训练动态，尤其是迭代索引，可作为无人工标注的合成质量伪监督；跨语言仍有差距但优于若干无 MOS 代理。局限是依赖当前 TTS 训练轨迹形态，统一多架构联合训练是未来方向。

## 点评
用“checkpoint 质量单调改善”作免费标签，直接对准开发期需求，比再造一套 MOS 数据更省。Ite 稳、Loss 弱也符合直觉：loss 样本依赖且震荡。脆弱处在于伪标签质量高度依赖“训练过程是否真有可感知递进”——非 F5 架构相关性明显变差，说明方法对生成范式敏感，扩展到任意未来 TTS 前需要更稳的 checkpoint 筛选与多系统联合训练。
