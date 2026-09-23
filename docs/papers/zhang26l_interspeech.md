# CTMusic: A Traditional Chinese Instrumental Music Dataset Towards Text-to-Music Generation

- 论文编号：882
- 报告人：Haotian Guo
- 程序：Tuesday 29 September 2026 / Singing Voice and Music Generation
- 技术分类键：singing
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26l_interspeech.pdf

## 问题
文本到音乐模型训练数据高度偏西方流行/电子，非西方仅约 5.7% 时长；缺少面向传统中国器乐的文本–音频配对资源，限制风格生成。

## 方法
构建 CTMusic：741 对、约 42.7 小时；独奏 601（12 种乐器）、合奏 140。来源为数字专辑与 Bilibili 等，机筛+人工去短于 20 s/人声/噪声，裁剪≤400 s、44.1 kHz、−14 LUFS。三位民乐专业背景标注者按三段模板写描述，合奏文本经 DeepSeek 释义增强。验证：在 CTMusic 上两阶段（独奏→合奏）LoRA 微调 Stable Audio Open，并提出 SA-TTT（每四块插入门控 TTT 层）。

## 实验与结果
相对预训练 SA，SA-LoRA 在独奏/合奏测试上 FD、KL、CLAP 与主观 OVL/TA 全面提升；SA-TTT 进一步最好（如 stage1 FDopenl3 156.77、CLAP 0.38；stage2 137.49、0.51）。预训练模型对国乐生成能力明显不足，凸显专用数据必要。

## 结论
首个面向文本生成传统中国器乐的配对数据集，并证明 LoRA/TTT 适配可显著改善风格与文本对齐。

## 点评
核心贡献是数据与文化域适配，TTT 是增强而非全新生成范式。规模相对西方大数据仍小，合奏子集尤其有限；标注依赖专家模板，扩展自动标注质量是作者自述的下一步。
