# Quality Adaptive Angular Margin Learning for Respiratory Sound Classification

- 论文编号：1213
- 报告人：June-Woo Kim
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/kim26k_interspeech.pdf

## 问题
呼吸音分类面临录音质量参差、类别严重失衡，以及 crackle/wheeze/both 细粒度重叠；固定角间隔学习未按样本质量调节，低质样本可能破坏决策边界。

## 方法
QLung：用谱熵与 RMS 构造无参考音频质量分数，自适应缩放角间隔；对数尺度角间隔稳定失衡训练；角分类器对特征与类权重单位化，在超球上施间隔。可挂在 AST、Audio-CLAP 等骨干。

## 实验与结果
ICBHI 官方 60–40：AST 上 CE 59.55% → QLung 62.01%（+2.46 Score）；Audio-CLAP 上 62.56% → 63.39%。SPRSound OOD：QLung+Audio-CLAP Score 59.80%，优于 BTS 等。消融显示固定间隔、质量间隔、失衡校正、角分类器逐步叠加有效。

## 结论
质量自适应角间隔可提升呼吸音判别与跨数据集泛化，无需依赖额外增强或元数据引导策略即可具竞争力。

## 点评
把“录音质量”直接写入间隔强度，比一律 ArcFace 更贴临床数据异质。OOD 优势是亮点。crackle 准确率有所下降、换来漏报减少，需结合临床代价权衡；质量分数启发式是否跨设备稳定仍待验证。
