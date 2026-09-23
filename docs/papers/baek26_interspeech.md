# SPARK: Efficient Audio-Text Matching for User-Defined Keyword Spotting via Spiking Neural Networks

- 论文编号：3336
- 报告人：Seung-Yeop Baek
- 程序：Monday 28 September 2026 / Information Extraction and Retrieval
- 技术分类键：retrieval
- 全文：https://www.isca-archive.org/interspeech_2026/baek26_interspeech.pdf

## 问题
用户自定义（文本注册）KWS 的 ANN 方案 MAC 重、能耗高，难 always-on；已有 SNN-KWS 多为闭集分类，开放词表未探索。

## 方法
SPARK：端到端脉冲域音–文匹配。SEE 提音频尖峰；STE 将音素嵌入时间展开后用 SDSA 做时空注意；SPE 拼接音文尖峰用 SDSA 提对齐特征；判别器出句级与音素级匹配概率，BCE 双损失。SDSA 用 Mask&Add 线性复杂度、乘法免。PLIF 神经元，仿真步 \(S=8\)。

## 实验与结果
LibriPhrase：相对 CMCD/PhonMatchNet，参数 287K（约 2.1× 更少），能量 18.44 µJ（相对 PhonMatchNet 约 21.7× 更低）。LE：AUC 99.07%、EER 3.97%；LH：AUC 82.71%、EER 24.98%，接近但略逊 PhonMatchNet。无预训练音频编码器。

## 结论
作者认为首个端到端 SNN 用户自定义 KWS 框架可在保持竞争力检出的同时大幅降能耗与参数。

## 点评
把开放词表验证迁入原生脉冲计算，针对边缘 always-on 约束。Hard 集上与强 ANN 仍有差距；能量为 45 nm 理论估算，实芯片事件驱动收益需再验证。
