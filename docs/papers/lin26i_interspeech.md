# RAISE: Resolving Ambiguity in Audio Understanding with Imagination and Selective Extraction

- 论文编号：1739
- 报告人：Yueqian Lin
- 程序：Thursday 1 October 2026 / Acoustic Event Detection 4
- 技术分类键：events
- 全文：https://www.isca-archive.org/interspeech_2026/lin26i_interspeech.pdf

## 问题
Audio LLM 在噪声干扰或细粒度歧义下易出现感知幻觉；单次前向无法对照原始信号验证感知。鸡尾酒会重叠说话、相近音色乐器等任务分别需要源隔离与比较参照，但现有系统对所有查询套用同一单遍策略。

## 方法
提出训练无关框架 RAISE：语义路由（gpt-4o-mini，仅看问题与选项）将查询分到 DIRECT / IMAGINE / EXTRACT。Auditory Imagination 用 Stable Audio Open 为可合成候选生成参照音频，再与原音频联合比较推理；Selective Extraction 先让 Audio LLM 描述目标声特征，再用 SAM-Audio 开集分离得到干净信号后重问。工具失败则回退 DIRECT。骨干为 Qwen2-Audio-7B、Qwen2.5-Omni-7B、Qwen3-Omni-30B-A3B-Thinking（需支持多音频输入）。

## 实验与结果
在 MMAR 与 MMAU 上，相对单遍基线最高提升 +12.4%（Qwen2-Audio@MMAR：45.1→57.5）；Qwen3-Omni 在 MMAR/MMAU 为 +10.2% / +6.6%。路由将约 75.8%（MMAR）/ 82.2%（MMAU）查询走 DIRECT，摊销耗时约 9.1 s / 7.6 s。CoT、Self-Refine 无益甚至下降；静态全量 Extraction/Imagination 低于基线；单工具路由低于完整 RAISE。增益集中在时序推理、感知、和声、情感等子类。

## 结论
通过在推理时用生成与分离实例化证据，RAISE 无需参数更新即可缓解感知歧义；局限是依赖外部工具并增加被路由样本的延迟，作者建议蒸馏生成器与批处理分离来缓解。

## 点评
核心洞察是“感知瓶颈不能靠更多文本推理补救”，用 analysis-by-synthesis 与分离做验证，消融设计清晰。强依赖多音频输入骨干与工具质量；错误回归多来自过度剥离有用上下文或参照过窄，路由误判时代价不小。
