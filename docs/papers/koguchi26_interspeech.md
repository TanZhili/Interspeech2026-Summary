# Instantaneous Pitch Estimation via Wave-U-Net-Based Fundamental Waveform Enhancement

- 论文编号：3202
- 报告人：Junya Koguchi
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/koguchi26_interspeech.pdf

## 问题
瞬时基频估计（IPE）需要从含谐波与噪声的语音中提取基波再算瞬时频率，但传统基于自相关、相位偏差等准则的通道选择在域外信号与未见噪声下脆弱，帧级离散估计又难以平滑跟踪 vibrato、chirp 等连续变化。

## 方法
将基波滤波表述为增强问题：Wave-U-Net 以语音波形为输入、直接回归基波波形，再对其解析信号求瞬时频率，从而省去复杂滤波器组的通道选择。训练损失为基波与残差（谐波+噪声）的 MAE 以保证混合一致性，并加带幅度掩码的瞬时频率 MAE（λ=5）；幅度低于 −100 dB 阈值的区域不计入 IF 损失。网络 L=6 层上下采样，输出 tanh，其余 Leaky ReLU，上采样用插值而非转置卷积以减轻混叠。

## 实验与结果
训练/评测覆盖 Bagshaw、Keele、CMU ARCTIC、PTDB-TUG、MOCHA-TIMIT、MIR-1K、MDB-stem-synth（共约 20.67 小时，说话人/歌手/乐器不重叠），噪声来自 NOISEX92、QUT-NOISE（30% 概率、SNR 0–30 dB）。对比 IRAPT、Halcyon、NINJAL。干净条件 RPA50：Proposed 88.47，Halcyon 86.80，NINJAL 84.87，IRAPT 83.84；SNR 0 dB 时 Proposed 仍 86.40，而 NINJAL 降至 62.35、Halcyon 76.30。CAPRICEP 调制响应显示干净条件下 NINJAL 随机分量更小，噪声下 Proposed 更稳，作者推测下采样混叠可能残留谐波。

## 结论
DNN 直接提取基波后再做 IPE，可省略通道选择，并在强噪声下优于确定性 IPE。未来拟改进抗混叠下采样并用于实际语音/歌声分析。

## 点评
做法抓住的是“先可靠滤出单正弦再求导相位”这一 IPE 链路中最脆的一环，用增强式回归替代启发式通道打分，自然带来噪声鲁棒。相对 NINJAL 等在干净强调制上的精度，代价是相位细结构可能受网络混叠影响；适用边界更偏含辅音、噪声的一般场景，而非纯元音 vibrato 精分析。
