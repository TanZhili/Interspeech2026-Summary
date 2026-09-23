# Modelling diphthong dynamics: A GAMM-based analysis of Australian English diphthongs

- 论文编号：2861
- 报告人：Ksenia Gnevsheva
- 程序：Wednesday 30 September 2026 / Diphthongs and Monophthongs
- 技术分类键：phonetics
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/gnevsheva26_interspeech.pdf

## 问题
双元音常只在 20%/80% 两点测 onset/offset，丢掉轨迹中段形状与变化速率；多点测量后统计仍常落在单点上。需检验性别与城乡位置对澳大利亚英语双元音全轨迹的影响。

## 方法
Sydney Speaks 与 Voices of Regional Australia（Braidwood）自然口语，可比子集：中老年、相近职业分、Sydney 仅 Anglo-Celtic；共 27+31 人。Fast Track 提 F1/F2（20–80% 七点），修正 Lobanov 归一，限塞音间。对 FACE、FLEECE、GOAT、MOUTH、PRICE 分别拟合 GAMM（mgcv bam）：Gender、Location 及其交互的参数项与 by-factor 平滑，控制时长与说话人/词项随机平滑。

## 实验与结果
Gender 对五元音均显著；Location 对 FACE、FLEECE、MOUTH 显著。女性与城市说话人整体更“领先”变化（远离 broader 实现）。部分差异在中段或斜率上更清晰：如 PRICE 性别差在轨迹中部；FLEECE 终点更开但全轨迹更单化，静态终点会误判为更保守。

## 结论
全轨迹 GAMM 能揭示单点分析会低估、漏掉甚至误判的社会语音差异；双元音变化可涉及轨迹形状/时序，而非仅平行平移目标点。

## 点评
方法学贡献大于“再报一个社会分层”：用具体反例说明静态测点如何误读音变方向。区域男性职业分偏低需谨慎解释 Location×Gender；扩展到更多社会与语言变量是自然下一步。
