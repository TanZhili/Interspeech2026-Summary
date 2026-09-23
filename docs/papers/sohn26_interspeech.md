# DTM-Codec: Dynamic Token Masking for VFR Speech Coding with Efficient Boundary Selection

- 论文编号：2984
- 报告人：Hoyeol Sohn
- 程序：Tuesday 29 September 2026 / Audio Coding and Signal Analysis
- 技术分类键：codec
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sohn26_interspeech.pdf

## 问题
变帧率（VFR）神经语音编解码可按信息密度分配时间分辨率，但侧信息（位置/时长）计入总码率后，相对固定帧率（FFR）的收益常不明确或仅部分指标有改善；既有工作也常缺同架构、严格匹配总码率的对照。问题是：在显式计入侧信息的 matched-total-bitrate 协议下，VFR 能否稳定优于 FFR。

## 方法
DTM-Codec（约 127M）基于 TAAE 两阶段 Transformer，前端/后端改为 STFT/iSTFT，瓶颈改为单码本 VQ（|C|=16384，14 bit/token）。Dynamic Token Masking 在 Stage-1 与 Stage-2 之间保留被选 token、掩码位填可学习 `<MASK>`，并传输二值 keep-mask 供位置感知解码。边界选择用 Path Length Equalization（PLE）：沿编码器轨迹余弦距离累积路径长度，O(N) 等分放置边界；训练时用 Robbins–Monro 控制器把 keep ratio 调到目标（文中 r=0.5）。总码率 = 内容码率 + 位置码率（Stage-1 每步 1 bit）。FFR 对照用均匀 stride 掩码、无位置比特，并以更大码本（|C|=65536，16 bit）匹配总码率。对抗+多尺度 mel/特征匹配训练；数据仅 LibriSpeech-960。

## 实验与结果
LibriSpeech test-clean（2620 句）上多档总码率对比外部系统与 matched FFR。例如 DTM@80Hz 总 1280 bps：UTMOSv2 3.42、UTMOS 4.20、PESQ 2.95、STOI 0.95、Spk-Sim 0.87、WER 2.98；@50Hz/800 bps：3.39 / 4.22 / 2.66 / 0.93 / 0.78 / 2.91；@40Hz/640 bps：3.43 / 4.19 / 2.49 / 0.92 / 0.74 / 3.27；@25Hz/400 bps：3.37 / 4.11 / 2.07 / 0.90 / 0.58 / 4.73，低码率相对 VARSTok/TAAE 等 WER 与感知指标明显更好。全文在 Table 2（FFR→VFR 相对增益）处截断，同架构 matched-rate 的逐指标相对变化数字未完整保留。

## 结论
作者认为在严格计入位置比特的匹配总码率设定下，掩码式 VFR（DTM）配合 PLE 可在低–中码率相对 FFR/外部系统带来广泛重建与可懂度提升；保留原 token 向量并用 `<MASK>` 填空优于平均/重复式上下采样。

## 点评
贡献在于把 VFR 争论拉回“总码率真匹配”这一可检验设定，并用 mask+位置比特替代合并/时长编码，使解码器知道哪些位置是真 token。正文 Table 2 截断，同架构 FFR 对照的完整相对增益需对照 PDF；仅用 LibriSpeech、单码本设定下的结论外推到多域音频也需保留余地。
