# Edit the Moment, Keep the Rest: Time-Localized Audio Editing via Instruction

- 论文编号：3044
- 报告人：Jinwoo Jung
- 程序：Wednesday 30 September 2026 / Acoustic Signal Analysis and Generation
- 技术分类键：signal
- 全文：https://www.isca-archive.org/interspeech_2026/jung26c_interspeech.pdf

## 问题
指令式音频编辑多只能粗粒度改内容，难以在多声事件混叠中指定某一时刻实例（增/删/替/移/延）而不破坏其余区域。

## 方法
EMKR 基于 Stable Audio Open：在线构造（指令、输入、目标）三元组，指令含参考区间 \(R\) 与编辑区间 \(E\)；四标量时间嵌入经 cross-attention 与 timestep 双路径注入。对移动/延长任务引入源事件掩码 SEM（\(R\) 上为 1）与干净潜变量拼接，强制保留源实例声学身份。支持 add/remove/replace/move/extend。自 SAO-Instruct 初始化训 60k step。

## 实验与结果
合成测试 1000 条。区域级：add/replace 的 Target F1seg(0.1s) 超 80%，远高于 AUDIT/AudioEditor/ZETA/SAO-Instruct；move/extend 优势更明显。整段 FAD/FD/KL 与 F1seg 最优。主观（10 人）Faithfulness/Quality/Temporal/Content 全面领先。消融：无 SEM 时 move Target F1 38.3→有 SEM 64.3。

## 结论
显式区间条件 + SEM 可在多声场景做约 100 ms 精度的时域局部编辑并保非编辑区。特别改善移动与延长这类保真关键任务。

## 点评
把“改哪一段”从自然语言歧义提升为结构化 \(R/E\)，再加 SEM 区分同类别多实例，问题抓得准。评测分区 Non-Edit/Source/Target 比整段 FAD 更能暴露“其实没改”的假阳性（如 SAO-Instruct）。训练/测试同为在线混合合成，真实录音泛化仍是下一步。
