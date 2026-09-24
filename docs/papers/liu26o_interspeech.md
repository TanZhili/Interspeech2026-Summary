# WhisperVC: Decoupled Cross-Domain Alignment and Speech Generation for Low-Resource Whisper-to-Normal Conversion

- 论文编号：2002
- 报告人：Dong Liu
- 程序：Wednesday 30 September 2026 / Assistive Technologies 2
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/liu26o_interspeech.pdf

## 问题
耳语缺声带激励、谱形与时序与正常语音差异大，并行耳语–正常数据稀缺；单阶段同时学对齐、音色与生成易不稳，通用 VC 直接用于耳语可懂度崩坏。

## 方法
三阶段 WhisperVC：(1) 配对数据上 Whisper-large V3 内容编码器 + 双编码器 Conformer VAE，soft-DTW 把耳语特征对齐到正常空间；(2) 仅正常语音上 Length–Channel Aligner、说话人条件粗 mel 生成器 + OT-CFM 残差细化，门控路由使正常输入可跳过对齐；(3) 在预测 mel 上微调 HiFi-GAN。主评 AISHELL6-Whisper（约 30h）；英语另用 wTIMIT 对齐 + LibriTTS 生成。

## 实验与结果
AISHELL6：DNSMOS ovrl 3.07、UTMOS 2.83、CER 16.93%、WavLM 相似度 0.95。相对耳语输入质量大幅提升；Seed-VC 零样本 CER 46.4%。消融：去 VAE 对齐 CER→40.2%；残差 CFM 优于全 mel CFM；声码器适配再提质量。正常 VC 路径仍可用，门控有助于保内容。

## 结论
解耦跨域对齐与正常语音生成，可在低资源耳语转换上兼顾可懂度与自然度，并统一 W2N 与常规 VC。

## 点评
把“耳语→正常”最难的分布对齐单独做成 VAE+soft-DTW，再在正常空间做粗到细生成，工程上清晰。通用 VC 对照验证了域差。脆弱处是强依赖配对耳语数据与内容编码器微调，跨语/零资源仍难。
