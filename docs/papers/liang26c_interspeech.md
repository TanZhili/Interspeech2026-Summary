# Text-Independent Speaker Verification Using Discrete Audio Tokens

- 论文编号：1135
- 报告人：Zheng Liang
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liang26c_interspeech.pdf

## 问题
神经音频编解码（NAC）离散 token 在生成任务成功，但直接做 ASV 明显弱于 Fbank；究竟是说话人信息被压缩丢掉，还是常规 CE 训练挖不出 token 中的说话人线索。

## 方法
诊断：同 ECAPA-TDNN 上对比原 Fbank、解码重构波形再提 Fbank、EnCodec token（各码本嵌入求和）。提出 CFKD：Fbank 教师与 token 学生共享骨干，用余弦嵌入对齐损失 L_KD 与分类损失加权（λ）；学生用 24 kHz EnCodec 全 32 层 RVQ。评 ECAPA-TDNN1024 与 ResNet34；另在 VoxCeleb2 上扫码率，并做特征维乱序探针。

## 实验与结果
诊断（Vox1）：原 Fbank EER 2.21 → 重构 2.57 → token 3.38，说明信息大体保留但难用。CFKD（λ=40）：ECAPA token 3.38→2.25（相对约 −35%），接近教师；ResNet 7.55→4.03。错误交集显示师生有互补“盲区”。乱序后 ECAPA 对 Fbank/token 均稳，ResNet 在 Fbank 崩溃、在 token 上基线已差且乱序几乎不变，表明 token 维缺乏谱邻接、1D 更合适。Vox2 上 24 kbps EER 1.05，相对 Codec-ASV 报告的 2.08 约 −49.5%。

## 结论
瓶颈在可及性而非信息丢失；CFKD 能逼近 Fbank 教师，且 1D 骨干更适配离散表示。

## 点评
诊断三元组把“编解码伤说话人”与“训练范式挖不出”拆开，结论对 codec-LM 生态很有用。最优 λ=40 远高于同质蒸馏惯例，跨特征蒸馏强度需小心调；教师质量上限仍约束学生。
