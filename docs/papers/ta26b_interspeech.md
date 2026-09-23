# Progressive Weak Supervision for Speech Emotion Recognition

- 论文编号：1587
- 报告人：Bao Thang Ta
- 程序：Monday 28 September 2026 / Speech Emotion Recognition and Representation 1
- 技术分类键：emotion
- 全文：https://www.isca-archive.org/interspeech_2026/ta26b_interspeech.pdf

## 问题
情感标签固有模糊，SSL 编码器早期预测又高度不确定；硬 one-hot 交叉熵从一开始就强迫单类承诺，与数据与模型状态都不匹配。标签平滑又均匀放松、不感知当前预测。

## 方法
Progressive Weak Supervision（PWS）：若真标签落在当前 top-k，则构造软目标（真类质量 α，其余在 top-k 内均分），用 KL；否则硬 CE。k 三阶段：前 10% 固定 k_init → 10–75% 线性衰减至 1 → 末 25% 标准 CE。WavLM-Base + 注意力池化 + MLP；默认 α=0.7、E=200。

## 实验与结果
IEMOCAP（4 类，session 5-fold）与 ViSEC（越南语，说话人分层 5-fold）。k_init=3 时 UA：IEMOCAP 78.08%（相对 CE +4.66）、ViSEC 85.70%（+11.90），优于 CE/标签平滑等。α=0.7 最佳；去掉 warm-up 或过早收紧均掉分。

## 结论
使监督强度随模型成熟度渐进收紧，可同时应对标签模糊与早期不确定，并跨英越语言有效；无改结构、开销可忽略。

## 点评
把 curriculum 做到“监督信号本身”而非样本排序，且 top-k 软目标模型感知，比均匀平滑更贴 SER。k 上限受 4 类设置约束，多类细粒度情感是否同样单调增益未测；仍依赖单一金标，未直接建模标注者分歧。
