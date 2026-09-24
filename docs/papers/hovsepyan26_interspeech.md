# Exploratory analysis of yellow mongoose vocalization: detection from in-the-wild recordings and call classification

- 论文编号：2168
- 报告人：Sevada Hovsepyan
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/hovsepyan26_interspeech.pdf

## 问题
黄獴（YM）行为生态依赖叫声类型解析，但野外录音噪声大、部分叫声标签模糊（含 undefined），需同时做野外检测与幼崽叫声分类探索。

## 方法
分类：手工谱时特征 + 随机森林，对比小型 CNN；9 类幼崽叫声（8 已知 + undefined）。检测：在含幼崽/成体/他种与噪声的野外录音上比较 rVAD 与 wSeg；对短时误检做时间合并后处理。置换检验分析特征重要性。

## 实验与结果
5 折：RF 均准 0.684±0.016，CNN 0.61±0.029。测试准确约 0.67；部分类型（如 begging call）F1 较高，undefined 与已知类有混淆，子群或暗示未描述新类型。rVAD 重叠/灵敏度优于 wSeg；未合并时 precision 低（约 0.19），合并邻近预测可提升 precision 且保持灵敏度。

## 结论
手工特征 RF 对 YM 幼崽叫分类有效；通用 VAD 类工具经简单时序平滑可辅助野外录音筛查，但假阳性仍需人工复核。探索性分析指向可能的新叫型。

## 点评
生物声学里“先分清叫型、再从噪声中捞出来”的双问题设定务实。undefined 类既是噪声也是发现源。检测 precision 低说明更适合作为候选段生成器而非全自动标注；样本量不均限制细类结论强度。
