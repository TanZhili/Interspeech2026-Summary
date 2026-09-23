# WaveNorm: A Low-Complexity Time-Domain Neural Adaptive Gain Control for Real-Time Speech Applications

- 论文编号：2115
- 报告人：Harish Rajamani
- 程序：Monday 28 September 2026 / Generative and Self-Supervised Speech Enhancement
- 技术分类键：enhancement
- 全文：https://www.isca-archive.org/interspeech_2026/ijjada26_interspeech.pdf

## 问题
传统 AGC 用固定攻放时间常数，在动态音量/噪声下易削波、增益泵动、噪声放大与响应滞后，且对内容无感知。需要低延迟、边缘可部署的内容感知响度归一化。

## 方法
WaveNorm：因果时域端到端 AGC。编码器为三层扩张分组 Conv1D（dilation 2/4/8）+ BN/PReLU，捕捉多尺度包络；GRU（隐层 32）瓶颈保证增益轨迹平滑；对称转置卷积解码器隐式施加增益并重建波形。感受野约 27 样本（~0.56 ms）。训练对齐 ITU-T 响度归一化目标，损失为 0.5 MSE + 0.5 多分辨率谱损失。宣称约 49M MACs、55 KB 内存。

## 实验与结果
相对 WebRTC AGC 与 Carnival AGC：干净 TIMIT 与噪声 VoiceBank+DEMAND 上输出 RMS 更集中、电平不变性更好；时域可变增益示例中过渡更均匀。作 Silero VAD 前端：FPR 最低 0.272、AUC 最高 0.96。作 DFN2/DTLN/GTCRN 前端时 NISQA/DNSMOS 全面提升（如 DFN2 NISQA 3.22→3.57）。输出 ASL 约 −26 dBov、响度 −26~−28 LUFS，符合 P.56/P.79。

## 结论
作者认为轻量时域神经 AGC 可在边缘实时稳定归一化响度，并作为模型无关前端改善 VAD 与抑噪。

## 点评
把 AGC 从启发式包络检测换成内容感知波形映射，并用 RMS 分布与下游任务验证“电平不变性”的实用价值，工程导向明确。复杂度数字利于嵌入式选型。局限是主结果偏分布与下游，缺少与传统 AGC 在主观泵动/可懂度上的系统听感对照；训练依赖 DNS3 等构造的宽动态数据，极端远场+强噪仍需实机验证。
