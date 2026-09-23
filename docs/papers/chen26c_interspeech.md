# Beyond Pitch: Multidimensional Cue Reweighting of Two High-Falling Tones in Pingdingshan Mandarin

- 论文编号：361
- 报告人：Zhuo Chen
- 程序：Monday 28 September 2026 / Tones
- 技术分类键：phonetics
- 全文：https://www.isca-archive.org/interspeech_2026/chen26c_interspeech.pdf

## 问题
声调发生常描述为从发声到音高；反向过程——音高对比减弱后其他线索增强——在汉语声调系统中少有表观时间证据。平顶山官话 T2 与 T4 均为高降调，是否正经历多维线索再加权尚不清楚。

## 方法
32 名老中青说话人录孤立词与载句；同步声学与 EGG。提 f0、能量、时长、OQ/SQ，并用自动检测二值化 creaky voice；时段 fPCA / logistic fPCA + 线性混合模型；条件随机森林（300 树）估 T2/T4 线索相对权重。

## 实验与结果
两调均为高起点降调，后半段音质与能量分化。随代际：T4 的音高差异收窄，OQ、creak、时长差异扩大（年轻人 T2 creak 减少、T4 creak 增多）。随机森林：老年以 F0 主次成分主导；中年重心集中于 F0 PC1；青年 F0 仍重要但时长与 Creak PC1 权重显著上升，部分个体发声权重甚至超过音高。连读整体压缩但不打乱代际趋势。

## 结论
平顶山两高降调正从音高主导转向音高—发声—时长协同以维持对立，为声调演化中“音高侵蚀→次线索音系化”提供表观时间证据。

## 点评
生产端多线索 + 代际对比设计扎实，把“次线索补位”量化为随机森林权重，比单看 creak 有无更有说服力。样本代际人数有限、多数人亦通普通话，感知端是否同步再加权尚待补齐。
