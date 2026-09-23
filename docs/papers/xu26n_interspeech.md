# Automatic Graphical Representations of Language for Dementia Detection

- 论文编号：1233
- 报告人：Si-Ioi Ng
- 程序：Monday 28 September 2026 / Clinically Useful Speech Representations 1
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/xu26n_interspeech.pdf

## 问题
Cookie Theft 图画描述中，基于 23 个 content information units（CIUs）的分析能反映描述的信息相关性与效率，但现有 CIU 分析依赖人工标注、对未见词鲁棒性差，且多关注空间分布，较少刻画 CIU 之间的时间动态（如空话、拖延过渡、反复纠缠少数 CIU）。

## 方法
流水线：录音下采样至 16 kHz → WhisperX 得到带词级时间戳的转写 → 微调 BERT-base-uncased 做 23 类多标签 CIU 识别（辅以低权重 ranking loss）→ 用 Layer-wise Relevance Propagation（LRP）定位各 CIU 对应词/跨度并取 onset 时间 → 将 CIU 序列建成有向时间图（边权为相邻 CIU 时间间隔），提取 unique nodes、归一化 walk length/cycles、degree centralization、relative edge jitter 等图特征，并与 unfilled pause rate、speech rate 对比。训练数据为 Pitt + WRAP（2,783 转写 / 1,352 说话人），测试与统计在 W-ADRC（Normal vs Clinical）。

## 实验与结果
W-ADRC 上 CIU 识别：人工转写 F1 0.879±0.086，ASR 转写 F1 0.865±0.098；LRP 定位准确率 0.910±0.067（“girl 的动作”类仅 0.741）。组间比较（校正年龄/性别/教育）：Clinical 组词数更少、停顿率更高、语速更慢；unique nodes 显著更少（Hedge’s g=0.80）；归一化 walk length、mean/std edge weight、relative edge jitter 等也显著更差；Normal 组归一化 cycle 反而更高，作者解释为有目的补充说明而非病理固着。

## 结论
自动化 CIU 识别 + 时间图特征可扩展、可解释地补充既有空间—语义 CIU 分析，支持认知—语言能力筛查。未来需改进临床语音的 WhisperX 切分与低敏感 CIU 定位，并做成临床可视化界面。

## 点评
做法把“说了哪些内容单元”与“单元间多久、是否迂回”绑在一张时间图上，比单纯计数 CIU 或静音率更贴近“空话/低效叙事”的临床描述。弱点在于依赖 ASR 与 LRP 定位质量（动作类 CIU 明显更弱），且图特征仍与话语长度强相关，归一化能否完全去掉长度混杂还需谨慎解读。
