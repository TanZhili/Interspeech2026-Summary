# Few-shot Class-variable Incremental Audio Classification via Prototype Adaptation and Pseudo Class-variable Training

- 论文编号：1024
- 报告人：Guoqing Chen
- 程序：Wednesday 30 September 2026 / Acoustic Event Detection 3
- 技术分类键：events
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/li26q_interspeech.pdf

## 问题
既有少样本类增量音频分类默认类别只增不减；现实中类数可增可减。需定义并求解 Few-shot Class-variable Incremental Audio Classification（FCIAC）。

## 方法
编码器 + 分类器：基座会话训编码器后冻结；分类器由 Class-variable Prototype Adaptation Network（CPAN：APGM/SAMP/PAMP/融合）随类增删动态生成与更新原型。基座阶段用 Pseudo Class-variable Training（PCTS）混伪类做加减类演练。增量时用旧类重构嵌入更新原型。代码公开。

## 实验与结果
LS-100 / NSynth-100 / FSC-89。LS-100 上全类平均准确率 AA 92.62%，优于 CEC、PAN、AMFO 等；增量类 AA 可达 97.91%（配合 PCTS）。消融：CPAN 与 PCTS 均提升，二者齐用最优。会话序列含 +5/−2 交替增减。

## 结论
原型自适应网络加伪类可变训练使模型同时应对类增加与删除，平均准确率超过先前少样本增量方法。

## 点评
把“类可变”写进问题定义是必要扩展；CPAN 模块分工清楚。评估仍是受控会话协议，真实开放世界中的类删除触发与旧类样本可得性更苛刻。编码器冻结限制对新声学域的适应。
