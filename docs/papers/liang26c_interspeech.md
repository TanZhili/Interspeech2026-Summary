# Text-Independent Speaker Verification Using Discrete Audio Tokens

- 论文编号：1135
- 报告人：Zheng Liang
- 程序：Wednesday 30 September 2026 / Speaker Verification: Architectures, Losses, and LLMs
- 技术分类键：speaker
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/liang26c_interspeech.pdf

## 问题
神经音频编解码（NAC）离散 token 能重建音色，但直接做 ASV 远差于 Fbank；究竟是说话人信息丢失，还是常规训练挖不出压缩离散表征里的线索。

## 方法
诊断：同 backbone 上 Original Fbank / 解码重建 Fbank / EnCodec token（RVQ 嵌入求和）。提出 Cross-Feature Knowledge Distillation（CFKD）：Fbank 教师与 token 学生同构，用余弦对齐嵌入（L_CLS+λ L_KD）。评 ECAPA-TDNN1024 与 ResNet34；另做特征维打乱探针与多码率 VoxCeleb2 实验。

## 实验与结果
诊断（Vox1）：EER 2.21→重建 2.57→token 3.38，说明压缩保留多数说话人线索、难点在可学性。CFKD（λ=40）ECAPA token EER 3.38→2.25（相对约 −35%），接近教师；ResNet 7.55→4.03。错误交集显示师生有互补盲区。打乱特征维：ECAPA 对 Fbank/token 近不变；ResNet 在 Fbank 上崩溃、在 token 上本就差且打乱几乎不变，暗示 codec 潜空间缺谱邻接、1D 更合适。Vox2 全码率 24 kbps 上 EER 1.05，相对先前 codec-ASV 明显更好。

## 结论
性能落差主要是可及性而非信息缺失；嵌入级跨特征蒸馏可逼近 Fbank 教师，且 1D 骨干更适配离散 token。

## 点评
诊断三元组把“丢信息 vs 难学”说清，比单纯堆蒸馏损失更有解释力。强依赖高质量 Fbank 教师；最优 λ 远大于同质蒸馏常规值，超参迁移需重调。
