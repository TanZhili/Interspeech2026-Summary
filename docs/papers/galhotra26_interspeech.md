# Advancing Infant Distress Detection: Two- and Three-Way Classification in Real-World Audio Environments

- 论文编号：3234
- 报告人：Kaya de Barbaro
- 程序：Wednesday 30 September 2026 / Speech Science and Computational Modeling to Study Children and their Everyday Environments | CHILDSPACE -- Child Home Interaction & Language Dynamics: Speech, Psychology, Affect, Computation, and Environments
- 技术分类键：children
- 全文：https://www.isca-archive.org/interspeech_2026/galhotra26_interspeech.pdf

## 问题
多数婴儿痛苦分类器在实验室数据上训练，迁到家庭日长录音大跌；现有公开真实数据多把 fuss 与 cry 合并，无法建模看护者随痛苦等级变化的反应。

## 方法
在 deBarbaroCry（婴儿佩戴 LENA 家庭录音）上重标 cry / fuss / non-distress，发布 deBarbaroFussCry（约 4.75h fuss、3.15h cry、其余非痛苦，共 66h 候选段；三分类 κ=0.847）。先强化二分类（痛苦 vs 非），再扩展三分类；比较传统、深度与混合模型，并做跨数据集泛化。

## 实验与结果
最佳二分类 macro F1=0.803（相对先前真实场景基线约 +17.8%）；三分类 macro F1=0.624（首个真实场景等级基准）。实验室训练模型在真实数据上显著退化；真实数据训练模型跨域更稳。数据与代码开源。

## 结论
真实家庭标注与分级（fuss vs cry）对生态有效婴儿痛苦检测必要；二分类可明显提升，三分类仍难但可建立基准。

## 点评
把“等级痛苦”写成发育理论与自动化看护质量测量的前置条件，动机清楚。跨数据集对照再次证明清洁数据乐观偏差。三分类 F1 仍中等，类别不平衡与短 fuss 边界是下一瓶颈。
