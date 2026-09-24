# WhispEar: A Bidirectional Framework for Scaling Whispered Speech Conversion via Pseudo-Parallel Whisper Generation

- 论文编号：1827
- 报告人：Yingda Shen
- 程序：Thursday 1 October 2026 / Voice Conversion
- 技术分类键：voice-conversion
- 全文：https://www.isca-archive.org/interspeech_2026/fang26b_interspeech.pdf

## 问题
耳语缺基频与周期激励，W2N 困难；平行耳语数据稀缺，DSP 伪耳语分布偏差大，现有方法音色/韵律保留差。

## 方法
WhispEar 三阶段：(1) 从 SenseVoice-Large 蒸馏轻量语义 tokenizer（Transformer+FSMN+FSQ），用耳语与正常语音促说话方式不变；(2) 共享 Flow-Matching Transformer（自 CosyVoice2）按方向指示 d∈{w2n,n2w} 从语义 token 生成 mel；(3) 先用真实平行数据训较易的 N2W 统一 tokenizer，再对大量正常语音零样本生成伪平行耳语，最后用真实+伪数据训更难的 W2N。发布双语语料 wEar（真实约 18 h / 146 说话人 + 伪约 3026 h）。

## 实验与结果
wTIMIT（英）与 wEar（中）测试：WhispEar-Scaled（约 3000 h 伪数据）英 SIM 0.577、WER 22.44%、UTMOS 3.75、F0 CoRR 0.513；中 SIM 0.750、CER 14.93%，全面优于 WESPER、DistillW2N、MaskCycleGAN、CosyVoice2。消融：对齐真实对 + 模型伪对（A+P）优于 RAW/DSP；伪数据预训练规模增大后再用真实对齐 SFT，各项持续提升。

## 结论
双向统一语义表征 + 可扩展伪平行耳语生成可缓解数据瓶颈，并带来一致的 W2N 增益；wEar 为后续研究提供双语基准。

## 点评
“先易后难”（N2W→扩数据→W2N）与数据中心 scaling 路线很契合耳语稀缺场景。性能仍强依赖伪数据质量与少量真实对齐微调；噪声鲁棒与多语扩展被作者列为后续工作，部署效率也未充分讨论。
