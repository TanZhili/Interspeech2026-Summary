# Cross-Attention is Half Explanation in Speech-to-Text Models

- 论文编号：40
- 报告人：Luisa Bentivogli
- 程序：Monday 28 September 2026 / Speech Representations and Alignment
- 技术分类键：representation
- 全文：https://www.isca-archive.org/interspeech_2026/papi26_interspeech.pdf

## 问题
S2T 中 cross-attention 常被用作音字对齐、时间戳、同传引导等，默认它反映输入–输出依赖。NLP 对 attention-as-explanation 争论已久，语音域仍缺系统验证；encoder 上下文混合可能使 CA 与原始声学相关性脱节。

## 方法
将 decoder **cross-attention（CA）** 与特征归因显著性对比：
- 输入显著性 \(SM_X\)：SPES 对 mel 频谱扰动聚类得 token 级 saliency，再沿频率聚合并下采样到编码器时间步；
- 编码器输出显著性 \(SM_H\)：对 encoder 隐状态做类似扰动归因，隔离上下文混合；
- 多层多头 CA 可按层/头/全局平均；与 saliency 算 Pearson 相关。
模型：自训 monolingual ASR（125M）与开放数据 FAMA 多任务多语 small/large（474M/878M，en/it ASR+ST）；测试 EuroParl-ST。

## 实验与结果
（抽取在 §4.4 聚合函数处截断；主结论取自摘要与引言汇总。）
- CA 与输入 saliency **中等**相关，跨头/层聚合时更明显；
- CA 大约只覆盖约 **50%** 输入相关性；相对 encoder saliency 最好约 **52–75%**；
- 趋势在单语/多语、单任务/多任务、多尺度上一致；CA 更贴近 encoder 输出而非原始输入，提示上下文混合影响。

## 结论
Cross-attention 提供有用但不完整的解释线索，不宜单独当作 S2T 行为的充分代理；正式特征归因仍更全面，CA 可作轻量辅助。

## 点评
把 NLP 的 attention 解释争论落到语音 encoder–decoder，并用 \(SM_X\) vs \(SM_H\) 拆开上下文混合，问题意识强。标题数字“一半”来自约 50% 输入覆盖。**详细相关表与聚合消融未完整进入抽取**，精确分层/头结果需回原文。
