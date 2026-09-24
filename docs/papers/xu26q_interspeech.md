# Continual Generalized Category Discovery for Acoustic Signals via Instance-Adaptive Regularization and Dynamic Teacher Guidance

- 论文编号：2614
- 报告人：Qisheng Xu
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/xu26q_interspeech.pdf

## 问题
声学系统需在无标注流中持续发现新类并保住旧类（C-GCD）；直接搬视觉 C-GCD 会因谱时结构复杂、类重叠与基类偏置而大幅掉点。

## 方法
面向音频的 C-GCD：实例自适应正则平衡巩固与探索；GMM 自适应阈值；EMA 动态教师稳定伪标签。无回放设置下增量发现新类。

## 实验与结果
LibriSpeech 与 ShipsEar：相对视觉向强基线 Happy 等，旧类保持与总体累计准确率提升。ShipsEar 累计平均准确率 74.14%（+4.84）；CAA-Old 66.27%→75.00%，CAA-New 相对 Happy 仍略低（63.92 vs 71.56）。LibriSpeech 上 CAA-All 76.94%（+8.34），主要靠旧类保持。

## 结论
实例自适应正则与动态教师使音频 C-GCD 在新类发现与旧类保持上更稳，尤其提升累计准确与旧类保留。

## 点评
明确指出声学相对视觉的失败模式并改正则/伪标策略，问题对准。ShipsEar 新类准确仍落后 Happy，说明巩固–探索权衡未完全解决；无回放设定贴近部署但更难。
