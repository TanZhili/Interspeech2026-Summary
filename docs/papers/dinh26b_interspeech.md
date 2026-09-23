# LitCodec: ASR-Guided Streaming Speech Coding with Unified Quantization

- 论文编号：3474
- 报告人：Son Dang Dinh
- 程序：Monday 28 September 2026 / Neural Speech Codecs: Low-Bitrate and Disentangled Coding
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/dinh26b_interspeech.pdf

## 问题
波形编解码低码率损音素；语义编解码多用非因果 SSL 或双支路，难流式；需同时满足因果、单码本、语义保真。

## 方法
LitCodec：因果 Conformer 编解码 STFT 特征；量化前对嵌入做 CTC ASR 监督（SpecAugment 掩蔽仅加在语义支路）；FSQ 单码本统一语义–声学 token；动态 chunk 训练兼顾流式/离线。推理卸掉 ASR 头。V1 800 bps/50 Hz，V2 640 bps/40 Hz；4 帧@50 Hz 算法延迟 80 ms。

## 实验与结果
LibriSpeech：V1 PESQ 2.56、STOI 0.925、WER 2.8%，流式设定最优；V2 640 bps WER 3.1%（EnCodec 750 bps 为 29.0%）。消融：无 ASR 监督 WER 升至 3.5%；量化后监督弱于量化前；动态 chunk 提升流式稳健。

## 结论
量化前因果 ASR 监督 + FSQ 单流可在流式低码率下同时保住听感与可懂度。

## 点评
相对双支路语义码，把语言结构“压进瓶颈之前”更契合流式单 token 序列。UTMOS/说话人相似度非全面领先；英语 LibriSpeech 外的泛化与噪声条件未充分展示。
