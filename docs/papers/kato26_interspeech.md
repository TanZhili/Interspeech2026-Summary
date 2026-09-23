# Coco-VC: Degradation-Robust Streaming Voice Conversion System on the Listener Side

- 论文编号：3571
- 报告人：Ryo Kato
- 程序：Monday 28 September 2026 / Speech Synthesis, Voice Conversion and Audio Generation
- 技术分类键：tts
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kato26_interspeech.pdf

## 问题
电话场景中说话人难以知晓己方音色/信道/噪声导致听感差；传统 VC 多在说话人侧且假设较干净输入。需要听者侧、流式、对电话降质鲁棒的实时转换。

## 方法
Coco-VC：因果 ConvNeXt 学生内容编码器（零前瞻、20 ms 帧，重叠相加后算法延迟 40 ms）+ 轻量 Vocos 解码器。多教师蒸馏融合 ContentVec（说话人不变韵律）与 Whisper 编码器（语言内容）。非对称训练：教师看干净 16 kHz，学生看经编解码、失真、混响、噪声等管线破坏的 8 kHz，预测干净融合特征。演示在消费级笔记本上运行（如 M2 约 80 ms 端到端），GUI 可开关 VC 与切换目标说话人。

## 实验与结果
与同解码器的 StreamVC 比：FLEURS-8k 上 WER 0.338 vs 0.451（UT-MOS 略低 3.214 vs 3.271）；VCTK 上 UT-MOS 4.041 vs 3.701。私有投诉电话仿真：61840 h 域内数据 vs 960 h 公开数据，WER 0.125 vs 0.363，UT-MOS 3.35 vs 3.08。

## 结论
电话增强 + 多教师蒸馏可得到降质不变表示，使听者侧流式 VC 在标准硬件上可用，并改善严重电话条件下的可懂度。

## 点评
把场景从“说话人美化自己”翻转到“听者侧补救”，工程闭环（延迟、GUI、域内数据）完整。核心是非对称蒸馏当联合增强器；局限是私有数据不可复现，且噪声极端时 MOS 未必优于基线，需在可懂度与自然度间权衡。
