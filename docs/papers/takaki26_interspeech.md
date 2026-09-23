# Head-Worn Dipole Microphone Array-based Speech Enhancement System for Single-Sided Deafness

- 论文编号：3601
- 报告人：Ken Takaki
- 程序：Wednesday 30 September 2026 / Speech and Language Processing for Health and Accessibility
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/takaki26_interspeech.pdf

## 问题
单侧聋（SSD）最难听的是聋侧侧向语音，而常规助听器/眼镜阵列多为前向指向，侧向增强硬件与处理不足。

## 方法
眼镜侧梁线性阵：4 全向 MEMS + 4 偶极（开口朝内外，约 11 mm 声程）；假头消声室测传递函数；16 kHz MVDR 波束形成。仿真：TIMIT 目标扫方位，语音形噪声自 ±45°/±135°，比较单麦、三全向 BF、三偶极 BF、2 偶极+1 全向 BF。演示实时 BF 与耳机输出。

## 实验与结果
90° 侧向：三全向 / 三偶极 / 2 偶极+1 全向 SDR 约 2.28 / 3.24 / 3.06 dB，ESTOI 约 0.453 / 0.484 / 0.495；相对共址三全向，2 偶极+1 全向约 +0.78 dB SDR、+0.04 ESTOI（摘要）。偶极相关 BF 在 −45°–0° 亦常优于纯全向 BF。

## 结论
侧向偶极阵列可提升 SSD 关键侧向可懂度相关客观指标；演示用于传播 SSD 需求与偶极麦特性。

## 点评
把阵列指向从“朝前”改到“朝聋侧”，问题定义清楚。强在假头实测+客观指标；弱在仿真用 oracle 噪声协方差、未报告真人 SSD 听力试验。
