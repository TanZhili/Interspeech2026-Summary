# Probing Low Frame Rate Degradation in Neural Audio Codecs

- 论文编号：3493
- 报告人：Alex Gichamba
- 程序：Tuesday 29 September 2026 / Quality, Intelligibility and Evaluation of Speech and Codecs
- 技术分类键：evaluation
- 全文：https://www.isca-archive.org/interspeech_2026/gichamba26_interspeech.pdf

## 问题

低帧率神经音频编解码利于自回归 TTS（生成代价随序列长度线性），但 6.25 Hz 常出现可懂度断崖；先前归因于音素碰撞，机制仍不清，不知失败是否内禀于帧率。

## 方法

在 DAC（16 kHz）上做受控帧率消融（约 1.6–100 Hz），固定 nq=12、|V|=1024（码率 R=120·fr bps）。对比固定裁剪时长 Tclip=0.38 s 与固定每例 token 数 K=19。用 MFA 对齐统计 phones/frame；测码本利用率与熵效率；评 WER（MMS-1B）、STOI、MCD、SPK-SIM、UTMOS。并对照公开 DAC/Mimi/SNAC/WavTokenizer 等。

## 实验与结果

固定 Tclip 时 12.5→6.25 Hz：WER 10.62%→107.4%，STOI 0.89→0.46。固定 K 后 6.25 Hz 恢复至 WER 15.37%、STOI 0.89。音素碰撞与码本饱和均非断崖主因（利用率&gt;98.7%，η 几乎平坦）。匹配序列长度后可延至 3.125 Hz（WER 29.36%，375 bps）与 1.6 Hz（WER 63.22%，192 bps），退化随音素负载平滑。

## 结论

作者认为断崖主要来自低帧率下每例 token 过少、解码器学不到跨 token 连贯；修正训练配置后低帧率效率收益比原先设想更可达。

## 点评

用“固定时长 vs 固定序列长度”一刀切出训练配置伪影，推翻简单音素碰撞叙事，对 tokenizer 设计很有启发。残差退化仍随信息容量下降，属预期。评测侧重重建可懂度，未直接测下游自回归 TTS 延迟与质量权衡。
