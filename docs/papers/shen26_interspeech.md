# CoDeTT: A Context-Aware Decision Benchmark for Turn-Taking Evaluation

- 论文编号：974
- 报告人：Huan Shen
- 程序：Thursday 1 October 2026 / Turn-taking
- 技术分类键：dialogue
- 全文：https://www.isca-archive.org/interspeech_2026/shen26_interspeech.pdf

## 问题
Turn-taking 评测常停留在二元句末/是否开口，交互场景窄，难以比较模型或诊断「动作对了但意图错了」的失败；现有全双工基准多把决策当黑盒。

## 方法
提出 **CoDeTT** 上下文感知决策基准：在系统状态（Speaking/Idle）下映射到四类宏观动作（Maintain、Stop & Listen、Takeover、Dismiss），再细分为 14 种场景（backchannel、打断、未完成犹豫、旁听、第三方协作等）。约 300 小时中英多轮数据、18k 标注实例，每条含五轮历史；合成（Gemini/Qwen-TTS）+ 真实（Candor、MagicData-RAMC）混合，经 ASR 校验与声景仿真。两阶段漏斗评测：先统一四动作，再对 Omni-SLM 做 14 类意图；引入 **Semantic Misalignment Rate (SMR)** 量化「动作正确但意图错误」。

## 实验与结果
专用控制器在 Takeover 高、Maintain/Dismiss 弱。Omni-SLM（Qwen3-Omni、MiniCPM-o、GPT-4o-audio、Gemini3-Pro）动作更均衡，但 SMR 暴露差距：Gemini3-Pro SMR 约 15–25% 最低；MiniCPM 在部分策略 SMR 常 >40%（「幸运猜对」）。历史长度非单调：适度历史降 Incomplete/Completion 的 SMR，过长（H=5）在打断类易过承诺、损敏捷性。说话人角色归因（Collaboration/Exclusion）仍是瓶颈。

## 结论
CoDeTT 把 turn-taking 评测从计时任务升级为可诊断决策问题；SMR 显示功能成功常掩盖弱语用 grounding，并揭示上下文连贯性与交互敏捷性的权衡。

## 点评
贡献是评测协议与诊断指标，而非新模型。SMR 和 14 类分层对全双工系统很有用。需注意大量合成数据与自动标注链路可能引入分布偏置；专用控制器因无意图输出无法报 SMR，跨范式对比仍主要在动作层。
