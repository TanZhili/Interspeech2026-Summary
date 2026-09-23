# TinyGiantALM: A Compact Audio-Language Model for Intent-Aware Reasoning under Resource Constraints

- 论文编号：491
- 报告人：Vinh-Thuan Ly
- 程序：Monday 28 September 2026 / Audio Reasoning Challenge
- 技术分类键：audio-llm
- 全文：https://www.isca-archive.org/interspeech_2026/ly26_interspeech.pdf

## 问题
音频推理顶尖系统依赖 7B–30B+ 规模与昂贵 RL，难部署于资源受限环境。小模型若被动吞下全部声学 token，易在混叠场景“致盲”；是否可用架构先验（按用户意图过滤声学）弥补参数不足。

## 方法
TinyGiantALM（约 1.5B）：三流冻结编码器——Whisper-Large-v3-turbo（16 kHz）、HTS-AT（48 kHz）、CLAP 全局语义锚；时间流池化至 N=300 后拼接。Query-guided Projector：2 层 E-Branchformer 编码局部—全局依赖 → 用户指令 masked mean pooling 作 query 的 cross-attention 精炼 → CLAP 驱动的 soft gate 仿射调制。注入 Qwen3-0.6B 的 `<audio>` 位，按 CoTA 的 Plan/Audio Analysis/Logic/Summary CoT 格式做 NTP。在单卡 A100 上训 3 epoch，推理约 5GB VRAM。

## 实验与结果
MMAR 零样本总准确率 46.4%，显著高于多数 7B–13B LALM（如 SALMONN-13B 33.2%、Qwen2-Audio 30.0%），混模态 Sound–Music 达 45.5%（对比若干大模型 9.1%）。挑战单模型榜约第 13：Rubrics 23.77、Acc 46.40，远低于 30B+ Qwen3-Omni+RL（Acc 74）。消融显示 Query 与 CLAP gate 组合相对 Vanilla +8.40；Mix S-M +36.36，但 Mix All 与 Spatial Analysis 有回退。

## 结论
意图感知精炼可在边缘友好规模上保住较强感知与部分推理；详尽多步叙事仍受语言模型规模限制，稠密混叠与空间任务上 gating 有噪声代价。

## 点评
把“小模型该听什么”做成 query 条件投影 + 全局门控，对准混模态崩盘这一痛点，效率叙事与消融都较完整。Rubrics 远低于 Acc 说明答案对了但推理链欠丰；CLAP 全局锚在 Mix All / 空间任务上的负增益也提醒：意图过滤不是万能，过滤会丢掉细物理线索。
