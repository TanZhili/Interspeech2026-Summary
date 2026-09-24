# ANCHOR: Autoregressive Non-intrusive Chunk-Ordered Refinement for Joint Multi-Resolution Speech Quality Modeling

- 论文编号：927
- 报告人：Zhuoyan Tao
- 程序：Wednesday 30 September 2026 / Speech and Audio Quality Assessment
- 技术分类键：evaluation
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/tao26_interspeech.pdf

## 问题
流式/生成系统需要从部分音频增量估计质量，但多数非侵入式预测器假定完整话语，前缀输入上退化。

## 方法
扩展 ARECHO，提出 ANCHOR：在统一自回归解码器中联合预测 chunk 级与 utterance 级伪 MOS（UTMOS、PLCMOS、NISQA 等），用分辨率感知层次先出 chunk token 再出全句 token（粗到细）。前缀长度 {2,4,6,8}s 监督；含局部失真压力测试。

## 实验与结果
相对 ARECHO，2s 前缀上 PLCMOS 误差降约 48%，4/6s 亦有增益。前缀→全句收敛分析显示有效感知语境约 4–6s。压力测试表明对局部腐败外推更稳，而非仅拟合截断边界。

## 结论
多分辨率自回归细化可改善增量质量估计，并揭示感知质量随时间累积的大致视界。

## 点评
贡献在于推理体制（增量伪 MOS），而非新主观真值。对 Teams/DNS 类生产指标很实用；依赖教师伪标签，教师偏差会遗传。
