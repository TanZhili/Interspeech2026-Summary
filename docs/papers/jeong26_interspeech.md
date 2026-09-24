# An Empirical Analysis of Task-Induced Encoder Bias in Fréchet Audio Distance

- 论文编号：1549
- 报告人：Wonwoo Jeong
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/jeong26_interspeech.pdf

## 问题
FAD 是文生音频默认指标，但分数依赖编码器嵌入空间；训练任务决定保留/丢弃哪些声学特征，使 FAD 带系统性任务偏置。

## 方法
把评价拆成 Recall、Precision、Alignment（语义/结构），用对数自参照归一化跨编码器比较。在六种编码器（AudioMAE、EnCodec、Wav2Vec2、VGGish、CLAP、Whisper）与两数据集上，对加噪、混响、音高/包络变换、时间反转/块打乱等受控扰动测敏感度。

## 实验与结果
四轴权衡：AudioMAE 精度敏感最高；Whisper 结构检测强但对信号劣化近乎盲；VGGish 语义对齐强但惩罚合理类内变化（Recall 低）。CLAP 较均衡但无峰值。音高轨迹还有方向不对称（如 VGGish 对下移更钝）。

## 结论
没有单一编码器可当通用评价器；未来需面向人类感知的 evaluation-native 编码器，而非复用任意任务嵌入。

## 点评
把“FAD 看编码器”做成可操作的四轴诊断，对 TTA 评测选型很有用。归一化是分析工具而非新感知真值；结论呼吁原生评测编码器，但本文未提出替代模型。
