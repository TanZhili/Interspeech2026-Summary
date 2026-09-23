# Grammar-Guided Hierarchical Parsing for Long-form Audio Activity Recognition

- 论文编号：2157
- 报告人：Peng Zhang
- 程序：Monday 28 September 2026 / Audio Understanding and Representation Learning
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/zhang26da_interspeech.pdf

## 问题
长时音频活动–子活动–事件本有层级与次序，MultiAct 等按层独立解码易全局不一致，且常需多层监督。

## 方法
仅用事件检测器（SlowFast+ActionFormer）得有序事件段与类后验；从训练脚本诱导 Hierarchical Activity Grammar（PCFG）：活动→子活动序列，子活动→锚点事件夹噪声非终结符（吸收杂音/漏检）。Earley 风格 MAP 解码最大化声学证据 + λ 语法先验，输出 Act–Sub–Event 解析树，由此导出子活动切分与活动类别，训练不需子活动/活动标签。

## 实验与结果
MultiAct（约 8.97 h）。事件 mAP 几乎不变（略升）。子活动：Eval Edit 24.6→35.3，但高 IoU F1/帧准确率未必升（边界受事件提案限制）。活动：Val Top-1 73.3%，Eval 66.7%/mAUC 75.0（无高层标签）。λ≈0.3 最佳；噪声节点显著提升各指标。

## 结论
语法引导解析可在仅事件监督下恢复可解释层级结构并改善时间次序一致性；边界精度与语法权重敏感仍是局限。

## 点评
把长时活动识别从多层神经网络头换成“事件证据 + 程序语法先验”，强在可解释与跨层一致性。Edit 升而严格 IoU 不升暴露其对检测器时间粒度的依赖；语法由训练脚本诱导，开放域活动扩展成本高。
