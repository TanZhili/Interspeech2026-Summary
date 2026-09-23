# Towards Unified Song Generation and Singing Voice Conversion with Accompaniment Co-Generation

- 论文编号：481
- 报告人：Ziyu Zhang
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26e_interspeech.pdf

## 问题
歌曲生成与 SVC 长期割裂：前者缺细粒度零样本音色克隆，后者忽视人声–伴奏协同；两者输入模态与优化目标冲突，朴素多任务易梯度对抗。

## 方法
UniSinger：多模态编码器（Qwen2.5 指令、Zipformer 音素、HuBERT+VQ 语义、CAM++ 说话人、自训 VAE 44.1 kHz 潜变量）接入 MM-DiT flow matching。四阶段课程用任务特异模态掩码：纯文本歌曲 → 纯 SVC → 说话人克隆歌曲 → 指令条件下伴奏协同 SVC。跨任务说话人空间先在 SVC 中纯化再迁移到歌曲生成。

## 实验与结果
约 20k+5k 小时内部歌曲。歌曲生成：PER 19.61%、Spk-Sim 68.85%，多项 SongEval 领先 DiffRhythm+/YuE 等。SVC：PER 0.151、Spk-Sim 0.712；带伴奏变体 Harmony MOS 3.891。消融去任务掩码、去 SVC 阶段或去歌曲阶段均显著损伤对应任务。

## 结论
统一框架首次同时支持说话人克隆歌曲生成与伴奏协同 SVC，课程掩码化解冲突并带来任务互惠。

## 点评
核心是用模态掩码课程把异构任务接到同一潜空间，并把 SVC 学到的说话人表征转给歌曲生成。强在伴奏协同与可懂度；主观音质仍受野外数据伪影制约，相对超大规模 YuE 在相似/质量上未必全面领先。
