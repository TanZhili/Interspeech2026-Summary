# VoxKit: Desktop Phone Alignment and Goodness of Pronunciation Analysis

- 论文编号：3591
- 报告人：Nina R Benway
- 程序：Tuesday 29 September 2026 / Speech and Language Learning Technologies
- 技术分类键：learning
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/benway26_interspeech.pdf

## 问题
临床语音研究需强制对齐后再做发音优良度（GOP），但桌面端缺少一体化流水线，命令行门槛阻碍采用。

## 方法
VoxKit（Python/PyQt6 可执行包）：注册说话人目录语料（.lab/.TextGrid），可选训/适配对齐器——Montreal Forced Aligner 或 Wav2TextGrid（wav2vec2）；生成、查看、比较对齐（重叠率、替换模式）；再以 LibriSpeech 预训练 wav2vec2 在 42 音素上算帧级后验，对数后验作 Acoustic Goodness，导出帧级与聚合 CSV。模块可扩展（stacker/engine/analyzer）。

## 实验与结果
软件演示/系统描述，无新算法榜单；面向儿童与临床群体下游分析。

## 结论
提供从原始音频到对齐再到 GOP 的桌面一体化工具，降低临床研究者门槛。

## 点评
缺口真实、工程抽象清楚；评分骨干来自成人 LibriSpeech，儿童/病理语音适应性需用户自行验证。
