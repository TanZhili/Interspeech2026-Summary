# Automatic identification of the onset of creaky voice according to F0 instability

- 论文编号：1430
- 报告人：Joshua Penney
- 程序：Tuesday 29 September 2026 / Audio signal analysis
- 技术分类键：signal
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/puggaardrode26_interspeech.pdf

## 问题
嘎裂声（creak）研究常需标出 modal→creak 精确起点（如段性 /t/ 声门化），现有自动工具多只判断窗口内有无 creak，短段与边界仍靠人工。

## 方法
用 REAPER 估 F0 与 GCI（不惩罚八度跳）；在 RMS 峰值之后搜索；取 F0 导数达峰值 ≥80% 的首帧，再选最近 GCI 为 creak 起点。在先前 AusE /hVt/ 年轻说话人已标 glottalization 的 474 项上与人工起点比 creak 时长与 G/V 比；ICC 与混合效应模型复现短/长元音差异。

## 实验与结果
时长分布相近，自动法略偏长；ICC=0.768（95% CI [.712,.813]），一致性良好但未达优秀。人工与自动标注的 G/V 模型均显示短元音比例显著高于长元音，配对模式一致。有个别负时长异常（元音后残留周期）。

## 结论
基于 F0 不稳的自动起点标注可接近人工，并在语言学分析上得出同类结论，可减轻大量手工标注负担。边界是依赖已确认含 creak 的样本，且对元音后周期敏感。

## 点评
把“八度跳是噪声”翻转成“八度跳是 creak 信号”，补齐窗口检测器缺的时间定位。强处是用真实语音学问题（G/V）做功能等价验证；脆弱处是预筛选含 creak、阈值 80% 经验化，对无大跳的 creak 亚型可能漏检。
