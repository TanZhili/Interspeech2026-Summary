# Entity Binding Failures in Speech LLM Reasoning: Diagnosis and Chain-of-Thought Intervention

- 论文编号：640
- 报告人：Ming-Hao Hsu
- 程序：Monday 28 September 2026 / Reasoning with Speech/Audio Language Models
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/hsu26_interspeech.pdf

## 问题
Speech LLM 在复杂推理上落后文本侧；既有解释多笼统为信息稀释。作者发现差距并非均匀：空间/句法/事实任务 S2T≈T2T，但需实体跟踪的逻辑任务（如 web of lies）S2T 跌至随机。

## 方法
在 VoiceBench BBH 四类各 250 题上对比 Qwen2.5-Omni 与 Phi-4-Multimodal 的 S2T/T2T。诊断为编码器池化模糊离散边界导致 **实体绑定失败**。提出推理时 **EA-CoT**：先枚举实体、记录声明、再逐步推理；其他任务用同构结构化控制提示。用 BL(1024) 分解 token 预算 vs 指令效应；消融格式/逐步/实体枚举；并用 T2T 姓名腐蚀与 MMSU 声学基准检验特异性。

## 实验与结果
web of lies 主导模态差距；排除后差距大幅缩小。EA-CoT 使该任务 S2T 提升约 +13.2（Qwen）/ +24.4 pp（Phi-4），且语音增益超过文本增益。预算扩大 alone ≤1.5 pp，增益几乎全来自指令。消融中实体枚举贡献最大（约全效应 59%）。T2T 100% 姓名腐蚀仅降约 3.6 pp；误转写姓名仍可逻辑正确。通用 CoT 与 MMSU 上无增益，支持特异性。

## 结论
S2T 推理短板主要是实体绑定的引出失败而非能力缺失；显式文本锚定可大幅弥合差距，代价是更长生成与延迟。

## 点评
任务级拆解把笼统“模态鸿沟”钉到绑定问题上，并有因果式提示干预与严格对照，说服力强。边界：TTS 评测、7B 模型、延迟开销；未来需表示层对齐以去掉显式 CoT。
