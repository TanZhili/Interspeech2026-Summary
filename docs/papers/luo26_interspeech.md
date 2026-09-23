# FCPE: A Fast Context-based Pitch Estimation Model

- 论文编号：500
- 报告人：Ruoyi Zhang
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/luo26_interspeech.pdf

## 问题
单声道基频估计对 MIDI 转写与歌声转换很关键；深度模型（如 RMVPE）准但算力高、难实时。需在噪声鲁棒与效率间折中。

## 方法
FCPE：16 kHz 波形→log-mel（1024/160）→嵌入，可选谐波嵌入；堆叠轻量 CNN 块（深度可分离 Conv1D + GLU/Swish，Conformer 卷积模块风格）建模帧间上下文；输出 360 维分音分箱概率（C1–B7，20 分音间隔），BCE 训练；推理用局部加权平均解码（置信度阈值 0.05）。训练用 DDSP 重合成 M4Singer/VCTK 作真值，加随机移调、噪声与 mel 掩码（空白/高斯）强迫上下文推断。

## 实验与结果
MIR-1K 干净 RPA 96.79%（10.64M 参），接近 RMVPE（90.42M，97.77%）；多 SNR 白噪/真实噪声下仍有竞争力。RTX 4090 上 RTF 0.0062，显著快于既有深度基频器。已用于 RVC/SVC 社区。

## 结论
深度可分离卷积 + 上下文训练策略可在接近 SOTA 精度下大幅降延迟与参数，适合实时应用。

## 点评
问题抓的是工业实时基频，而非再堆大 U-Net。强处是重合成真值与掩码增强对噪声鲁棒；脆弱处是分类+局部平均仍可能倍频/半频错，且重合成分布与真实歌声差距需留意。
