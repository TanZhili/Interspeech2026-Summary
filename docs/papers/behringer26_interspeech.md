# Assessing the Impact of Noise and Speech Enhancement on the Intelligibility of Speech Codecs

- 论文编号：1459
- 报告人：Lyonel Behringer
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/behringer26_interspeech.pdf

## 问题

极低码率神经语音编解码常只在干净语音上评质量，缺少噪声与真实通信管线下的句级可懂度评估；可懂度易触顶（ceiling），且客观指标与主观结果在噪声条件下关联尚不充分。

## 方法

对经典编解码（AMR-WB 6.6 kbps、EVS 8 kbps）与神经编解码（LPCNet 1.6、Lyra V2 3.2、DAC 1.5、Mimi 1.1 kbps）做众包句级听测：材料来自 Clarity Speech Corpus，混入 DEMAND 四类噪声（DLIVING/PRESTO/TCAR/TMETRO），SNR 5/15/25 dB，可选 DeepFilterNet2 增强后再编码。听者转写句子并评听努力（P.800 Annex B 五分制）。转录规范化后算词正确率 SI 与 WER。用 LMM 分析 codec×噪声×SNR×SE；并与 STOI/ESTOI 及多种 ASR（Whisper-B/L、Parakeet、Canary）条件级/样本级相关。

## 实验与结果

有效 160 人、7670 条响应。干净与 25 dB 接近顶；低 SNR 下经典编解码更抗噪，神经编解码掉得更狠。SE 显著提升 DAC、LPCNet、Mimi 的可懂度（Δ 约 0.060/0.082/0.036）与听努力；对 AMR-WB、EVS、Lyra、参考不显著。PRESTO/TMETRO 最伤神经编解码。在 SI≥0.95 子集上，听努力仍能区分：DAC 听努力最低（接近参考）。条件级上 ASR 客观 SI 与主观相关高于 STOI/ESTOI（Whisper-B 条件级 PC 0.973）。

## 结论

作者认为神经编解码噪声鲁棒性弱于经典编解码；编码前 SE 可缩小差距；听努力可缓解可懂度顶棚；条件级 ASR 比 STOI/ESTOI 更宜作客观代理。低 SNR 标注者一致性下降是局限。

## 点评

把“通信管线=可选 SE + 编解码 + 噪声”做成系统听测，结论对部署很实用：低码率神经编解码不该只报干净 MOS。听努力作顶棚补丁设计干净。客观相关强调条件级而非样本级，避免过度解读单句 ASR。众包与 IAR 在极低 SNR 变差，细粒度噪声对比需谨慎。
