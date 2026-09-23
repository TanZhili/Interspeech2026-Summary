# Ada-Mic: Orientation-Adaptive and Robust Close-to-Mic Speech Detection on Smartphone Using Generalized Cross-Correlation Features

- 论文编号：224
- 报告人：Irina Kezele
- 程序：Monday 28 September 2026 / Spatial Audio 1
- 技术分类键：spatial
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/fong26_interspeech.pdf

## 问题
无热词唤醒常用“贴近话筒说话”检测，但能量/爆破音等特征随手机姿态（DoA）变化，限制可持机角度，妨碍自然交互。需在双麦手机上把距离与朝向解耦。

## 方法
Ada-Mic：在现有贴近话筒检测骨干旁加 GCC-PHAT 分支（隐式编码 DoA 与多径），两支特征拼接后分类近/远。骨干对比扩展双通道的 ProxiMic 式 CNN 与 LoRA 微调 HuBERT。自采约 38 h 华为多机型双麦语音（66 人，距离 2/5/15/30 cm，底/顶麦直射与间接姿态）；Mate60 作测试；叠加音乐/办公室噪声 SNR 5–20 dB。GCC 过采样到 [−2τ,2τ] 再亚采样 100 点；GCC 支额外 FLOPs 约 7.6%（ProxiMic）/<0.01%（HuBERT）。

## 实验与结果
近=2/5 cm，远=15/30 cm。安静下平均准确率约提升 1–3%（未达显著）；Music/Office 噪声下提升更明显（平均约至 5%），Wilcoxon p<0.05。过渡距离 5/15 cm 改善约 5%；难姿态上最高约 +24%。安静场景因基线已高、样本力不足，统计不显著但趋势正向。

## 结论
GCC 插件可提升朝向鲁棒的贴近话筒检测，扩展可用姿态范围，利于无热词交互；适用于多数双麦手机，开销小。

## 点评
用经典 GCC-PHAT 当“姿态侧信道”而非显式估角，工程落地性强。自采姿态覆盖与 Mate60 外推测试有说服力；安静不显著与单测机型是边界。隐私友好（纯音频）相对摄像头方案是实际优势。
