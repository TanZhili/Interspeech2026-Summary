# Moot-Court: Training-Free Dialectical Reasoning for Depression Detection

- 论文编号：3099
- 报告人：Yuqing Sun
- 程序：Tuesday 29 September 2026 / Pathological Speech Assessment 1
- 技术分类键：health
- 全文：PDF 链接 https://www.isca-archive.org/interspeech_2026/sun26i_interspeech.pdf

## 问题
自动抑郁检测需要可解释、可扩展方案；向 LLM 注入语音多依赖微调/P-tuning，临床小数据易过拟合且“模型锁定”。纯文本 LLM 又丢掉声学生物标志。

## 方法
Moot-Court：冻结 LLM 的训练免费辩证推理。先将声学指标（latency、语速、F0、能量、jitter、shimmer 等）文本化，建多层蓝图 VL/VS/VP，并按精神病理网络抽出 Vext/Vint/Vevid 事实节点。Prosecutor 建致病图 GP、Defense 建情境图 GD（指示、强化、矛盾、排除等边类型）。k=5 法官多样温度裁决，Reflector 据对错场景写入正规则/负陷阱 Codex；奖励 S=α×β×W+δnew 驱动检索与 MODIFY/MERGE/ADD。骨干如 DeepSeek V3.2、Qwen3；音频描述用 Qwen-Audio。数据 DAIC-WOZ 官方划分，ZipEnhancer 降噪。

## 实验与结果
DeepSeek V3.2：F1 0.8856，Recall 0.9394，Precision 0.8378，优于多项全训/微调/指令微调基线（如 DepressInstruct F1 0.8235）。跨骨干仍高召回（≥0.9394）；Qwen3-30b F1 0.8234。消融：纯直接推理 F1 0.6296；加辩证无 Codex 0.7020；全框架 0.8856。文本+音频相对纯文本 F1 0.7890→0.8856。

## 结论
在不更新权重下，将多模态抑郁判定组织为对抗图辩论 + 自演化 Codex，可在 DAIC-WOZ 上超过微调模型并提升可追溯性。

## 点评
把 GRPO 式“经验蒸馏”搬到临床辩证结构，避开小样本微调过拟合，问题意识清楚。强在模块消融显示 Codex 能同时拉回召回与精度；弱在依赖强闭源 LLM API、声学仅符号化入 prompt，以及对 DAIC-WOZ 官方划分的外部泛化未测。
