# Don't Listen to Me: A Lightweight, Low-Latency Model for Own-Voice Cancellation in Far-Field Speech Enhancement

- 论文编号：3430
- 报告人：Mads Østergaard
- 程序：Thursday 1 October 2026 / Source Separation 2
- 技术分类键：separation
- 全文：https://www.isca-archive.org/interspeech_2026/stergaard26_interspeech.pdf

## 问题
远场设备增强后回传用户时，往返时延常超过 10–20 ms，用户自己的声音出现可感知延迟伪影。需要低算法时延地从噪声多说话人混合中去掉已注册（enrolled）的“本机声”，同时保留其余语音并做去噪——即 own-voice cancellation（OVC），与目标说话人提取（TSE）互补。

## 方法
以短 enrollment（2 s）条件化时域网络。基线为 TD-SpeakerBeam；提出 Mamba-MinGRU masker：Mamba 块 + MinGRU 时间混合，因果配置算法时延固定 2 ms（kernel \(L=32\)）。辅助网络可用 ConvTasNet 或更轻的双向线性 RNN（5 块）提说话人嵌入，经逐元素乘适配。损失为可处理静音的 thresholded SDR（active/inactive）。训练：LibriSpeech + WHAM! 动态混合，最多一个干扰说话人；并在 LibriMix 多说话人上测鲁棒性。

## 实验与结果
OVC 与 TSE 难度接近（非因果 F 条件约 13 dB SDR）。因果 Mamba-MinGRU + 线性 RNN 嵌入（c4）：F/D 上 SDR 11.98/11.35，主网 0.33 GMAC/s、辅网 0.26 GMAC/s，远低于 TD-SpeakerBeam 的约 5 GMAC/s。small 变体（d2）单线程 RTF 0.82、F 上 SDR 11.47。同基频说话人更难消本机声；3–5 说话人时 SDR 改善约降 2 dB。

## 结论
OVC 可作为远场流式去噪的实用目标；线性 RNN 主网与辅网在约 2 ms 时延下接近 ConvTasNet 级效果且算力更低，便于流式设备部署。

## 点评
把 hearing-aid 文献里的本机声延迟问题形式化为“消 enrolled、留他人”，与 TSE/AEC 边界清晰。主网轻量是亮点；训练默认双说话人、多说话人明显掉点，且未充分测混响，实场仍需扩展。
