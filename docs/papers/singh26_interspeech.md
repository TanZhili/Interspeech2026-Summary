# Low-Burden Data Augmentation for Dysarthric ASR via Zero-Shot Voice Cloning

- 论文编号：1501
- 报告人：Satwinder Singh
- 程序：Thursday 1 October 2026 / Beyond Speech Technologies in Healthcare
- 技术分类键：health
- 全文：https://www.isca-archive.org/interspeech_2026/singh26_interspeech.pdf

## 问题
构音障碍 ASR 数据稀缺且说话人差异大；合成增强常需多句注册或说话人特调，再次落入采集瓶颈。需检验零样本声纹克隆能否用极低负担数据改善识别。

## 方法
用 Higgs Audio V2，对 TORGO 每位构音障碍说话人仅取一句参考（平均 7.2s，“The quick brown fox…”），以 LibriSpeech 100h 去重/过滤文本为提示生成 TORGO-Synth（8289 句，约 18h，训练 15h）。严格剔除与 TORGO/SAP-1102 词表重叠的提示。微调 Whisper-medium：Zero-shot / Real / Clone / Hybrid，仅在留出真实 TORGO 上评 WER；并用 SAP-1102 子集做跨库测试。TitaNet 嵌入做说话人相似分析；另扫 5–50h 合成量。

## 实验与结果
总体 WER：Zero-shot 31.62%，Real 24.44%，Clone 26.00%，Hybrid 25.12%。中重度组 Clone/Hybrid 优于 Real（39.95%/37.49% vs 42.19%）。合成量在约 15h 为最优点，再增易过拟合伪迹。SAP-1102：Clone 整体约 12.8%（Zero-shot 14.5%），CP 组从 54.7% 降至 41.6%。t-SNE 显示多数说话人克隆簇紧、M05 较散。

## 结论
单句注册的零样本克隆可提供可扩展训练信号，接近真实微调并在中重度与跨库上有时更优；存在合成量“甜点”与对中度说话人可能引入分布偏移的代价。

## 点评
把“低负担”落到单句注册与词表隔离，实验控制清楚。中重度受益、中度恶化提示克隆并非普适补丁；TORGO 以 CP 为主，跨库 CP 增益更大符合源分布偏置。全文结论段抽取不完整，跨库细表以正文已给数字为准。
