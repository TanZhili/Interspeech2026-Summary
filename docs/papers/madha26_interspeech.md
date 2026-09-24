# DLLM-TTS: Block Discrete Diffusion Language Model for Text-to-Speech Synthesis

- 论文编号：788
- 报告人：Wasim Madha
- 程序：Thursday 1 October 2026 / LLM Based Speech Synthesis
- 技术分类键：tts
- 全文：https://www.isca-archive.org/interspeech_2026/madha26_interspeech.pdf

## 问题
自回归 codec LM 音质与可懂度好，但需大规模数据且逐 token 解码延迟高；非自回归流匹配/扩散虽并行，常需显式时长建模或对齐弱，易漏词/重复。块离散扩散（BD3-LM）在文本上有效，尚未用于条件语音 codec 生成。

## 方法
DLLM-TTS 把 TTS 建成对 X-Codec2（单流 FSQ，|V|=6561，50 Hz）token 的条件块离散扩散。序列切成块（默认 B=32，约 0.64 s），块内掩码扩散并行预测，块间顺序生成。用 staircase attention：噪声块内双向、对前序干净块因果、干净块内因果。训练最小化掩码位置交叉熵；用 EOS 处理变长，无需显式时长。0.6B Transformer 自 Qwen2 初始化。推理：参考文本+参考 codec + 全掩码生成段；每块最多 T 步置信度采样（τ=0.6），可提前停止；默认 T=16 时 RTF=0.15。

## 实验与结果
两阶段：Emilia 采样 16K 小时 20 epoch，再 4K 小时高质量合成数据微调，合计约 20K 小时。Seed-TTS-eval（英）：WER 2.25、CER 1.05、SIM 0.750、MOS 4.25，接近或优于若干更大数据/参数系统。消融：T 从 8→32，WER 14.58%→2.25%；T=64 反而变差。B=32 优于 8/16。掩码目标被视为隐式数据增强，解释相对自回归的数据效率（相对 60K–250K 小时约 3–12× 减少）。

## 结论
块离散扩散可在无显式时长标注下兼顾局部声学一致性与跨块文本对齐，以较小数据与 RTF 0.15 实现实用、有竞争力的零样本 TTS。

## 点评
关键是把“块内并行 + 块间因果”对准语音的局部相干与全局对齐需求，staircase mask 替代了时长模型。速度–质量由 B 与 T 直接调节；T 过大变差说明过度去噪并非单调受益。相对纯 NAR，保留了顺序结构；相对纯 AR，换来并行与数据增强。脆弱处包括块边界伪影风险（文中主观 MOS 未明显受损）以及对 codec 单流设定的依赖。
